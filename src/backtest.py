#!/usr/bin/env python3
"""Reproducible pre-PDUFA run-up backtest engine.

Convention (matches the audited note): entry = last trading close on or before
(PDUFA - entry_offset calendar days); exit = last trading close on or before
(PDUFA - exit_offset calendar days). Returns use split/div-adjusted close.
"""
import csv, datetime as dt, math, statistics as st
from bisect import bisect_right
from pathlib import Path

def load_prices(ticker):
    fp = Path('data/prices') / f'{ticker}.csv'
    if not fp.exists():
        return None
    with open(fp) as f:
        r = list(csv.reader(f))[1:]
    if not r:
        return None  # empty cache = delisted/missing
    dates = [x[0] for x in r]
    adj = [float(x[5]) if x[5] not in ('', 'None') else None for x in r]
    hi  = [float(x[2]) if x[2] not in ('', 'None') else None for x in r]
    lo  = [float(x[3]) if x[3] not in ('', 'None') else None for x in r]
    return {'dates': dates, 'adj': adj, 'hi': hi, 'lo': lo}

def _iso(d):
    return d.strftime('%Y-%m-%d') if isinstance(d, dt.date) else d

def day_on_or_before(px, target):
    """Index of last trading day <= target (ISO str). None if out of range."""
    i = bisect_right(px['dates'], _iso(target)) - 1
    return i if i >= 0 else None

def trade(px, pdufa, entry_off, exit_off):
    d0 = dt.datetime.strptime(pdufa, '%Y-%m-%d').date()
    ent_t = (d0 - dt.timedelta(days=entry_off)).isoformat()
    ext_t = (d0 - dt.timedelta(days=exit_off)).isoformat()
    ei = day_on_or_before(px, ent_t)
    xi = day_on_or_before(px, ext_t)
    if ei is None or xi is None or xi <= ei:
        return None
    ep, xp = px['adj'][ei], px['adj'][xi]
    if not ep or not xp:
        return None
    ret = xp / ep - 1.0
    # max adverse excursion over holding (worst intraday low vs entry)
    lows = [px['lo'][k] for k in range(ei, xi + 1) if px['lo'][k]]
    mae = (min(lows) / ep - 1.0) if lows else None
    highs = [px['hi'][k] for k in range(ei, xi + 1) if px['hi'][k]]
    mfe = (max(highs) / ep - 1.0) if highs else None
    return {'entry_date': px['dates'][ei], 'exit_date': px['dates'][xi],
            'entry_px': ep, 'exit_px': xp, 'ret': ret, 'mae': mae, 'mfe': mfe,
            'hold_days': xi - ei}

def run_variant(events, entry_off, exit_off):
    """events: list of dict(ticker,pdufa_date,outcome,...). Returns trades list
    (with event fields merged) and a 'skipped' breakdown."""
    trades, skipped = [], {'no_prices': 0, 'window_out_of_range': 0}
    for e in events:
        px = load_prices(e['ticker'])
        if px is None:
            skipped['no_prices'] += 1
            continue
        t = trade(px, e['pdufa_date'], entry_off, exit_off)
        if t is None:
            skipped['window_out_of_range'] += 1
            continue
        t.update(e)
        trades.append(t)
    return trades, skipped

# ---------- statistics ----------
def _mean(x): return sum(x) / len(x) if x else float('nan')

def stats(trades):
    r = [t['ret'] for t in trades]
    n = len(r)
    if n == 0:
        return {'n': 0}
    wins = [x for x in r if x > 0]
    losses = [x for x in r if x <= 0]
    mean = _mean(r)
    sd = st.pstdev(r) if n > 1 else 0.0
    sd_s = st.stdev(r) if n > 1 else 0.0
    downside = [min(0.0, x) for x in r]
    dstd = math.sqrt(_mean([d * d for d in downside])) if n else 0.0
    gains = sum(wins); loss_abs = abs(sum(losses))
    pf = (gains / loss_abs) if loss_abs > 0 else float('inf')
    # 95% CI on mean via t-approx and bootstrap
    se = sd_s / math.sqrt(n) if n > 1 else float('nan')
    tcrit = 1.96 + 2.4 / max(n - 1, 1)  # rough small-sample bump
    ci = (mean - tcrit * se, mean + tcrit * se) if n > 1 else (float('nan'), float('nan'))
    # one-sample t stat vs 0
    tstat = mean / se if se and se == se and se > 0 else float('nan')
    return {
        'n': n, 'mean': mean, 'median': st.median(r), 'hit': len(wins) / n,
        'avg_win': _mean(wins) if wins else 0.0, 'avg_loss': _mean(losses) if losses else 0.0,
        'pf': pf, 'best': max(r), 'worst': min(r), 'std': sd, 'std_sample': sd_s,
        'sharpe_trade': mean / sd if sd > 0 else float('nan'),
        'sortino_trade': mean / dstd if dstd > 0 else float('nan'),
        'se': se, 'ci95': ci, 'tstat': tstat,
        'expectancy': mean,
    }

def bootstrap_ci(trades, stat_fn, iters=10000, seed=42):
    import random
    random.seed(seed)
    r = [t['ret'] for t in trades]
    n = len(r)
    if n < 2:
        return (float('nan'), float('nan'))
    vals = []
    for _ in range(iters):
        samp = [r[random.randrange(n)] for _ in range(n)]
        vals.append(stat_fn(samp))
    vals.sort()
    return (vals[int(0.025 * iters)], vals[int(0.975 * iters)])

# ---------- capital simulation with German tax ----------
def select_nonoverlapping(trades):
    """Greedy: order by entry date, skip trades whose entry precedes the current
    open position's exit (all-in capital can hold only one position)."""
    ts = sorted(trades, key=lambda t: t['entry_date'])
    chosen, busy_until = [], None
    for t in ts:
        if busy_until is None or t['entry_date'] > busy_until:
            chosen.append(t); busy_until = t['exit_date']
    return chosen

def simulate(trades, capital=1500.0, fee_roundtrip=2.0, tax_rate=0.26375,
             allowance=0.0, use_allowance=False):
    """All-in roll-over with per-trade German withholding tax (Abgeltungsteuer).
    Loss pot (Verlustverrechnungstopf) carries forward; optional annual
    Sparerpauschbetrag allowance. Returns (rows, summary)."""
    ch = select_nonoverlapping(trades)
    cap = capital
    loss_pot = 0.0
    year_allow = {}
    rows = []
    peak = cap; maxdd = 0.0
    tax_total = 0.0
    for t in ch:
        year = t['exit_date'][:4]
        if use_allowance and year not in year_allow:
            year_allow[year] = allowance
        gross_before = cap
        # apply return and round-trip fee
        gv = cap * t['ret']              # gross P/L in currency
        cap_after_pl = cap + gv - fee_roundtrip
        tax = 0.0
        taxable = gv - fee_roundtrip     # fees reduce taxable base (approx: treat as cost)
        if taxable > 0:
            # offset with loss pot
            offset = min(loss_pot, taxable)
            taxable -= offset; loss_pot -= offset
            if use_allowance:
                a = min(year_allow.get(year, 0.0), taxable)
                taxable -= a; year_allow[year] = year_allow.get(year, 0.0) - a
            tax = taxable * tax_rate
        else:
            loss_pot += -taxable         # add loss (incl fee) to pot
        cap = cap_after_pl - tax
        tax_total += tax
        peak = max(peak, cap); maxdd = min(maxdd, cap / peak - 1.0)
        rows.append({**t, 'cap_before': gross_before, 'pl': gv, 'fee': fee_roundtrip,
                     'tax': tax, 'cap_after': cap, 'loss_pot': loss_pot})
    # CAGR over the chain span
    if ch:
        d0 = dt.datetime.strptime(ch[0]['entry_date'], '%Y-%m-%d').date()
        d1 = dt.datetime.strptime(ch[-1]['exit_date'], '%Y-%m-%d').date()
        yrs = max((d1 - d0).days / 365.25, 1e-9)
        cagr = (cap / capital) ** (1 / yrs) - 1 if cap > 0 else -1.0
    else:
        yrs, cagr = 0.0, 0.0
    summary = {'n_chain': len(ch), 'start': capital, 'end': cap, 'ret_total': cap / capital - 1,
               'tax_total': tax_total, 'maxdd': maxdd, 'cagr': cagr, 'years': yrs}
    return rows, summary
