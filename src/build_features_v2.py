#!/usr/bin/env python3
"""Expanded point-in-time feature set for the subset/interaction alpha search.
Adds price-derived features (ATR, beta-vs-XBI, relative strength vs XBI, 6-month
momentum, downside vol) and merges openFDA review priority + prior-approval count.
Every feature is measured as of the entry day (T-30); targets (excess, beat_xbi)
are for evaluation only. Extends data/features.csv -> data/features_v2.csv.
"""
import sys, csv, statistics as st, datetime as dt, math
sys.path.insert(0, 'src')
import backtest as bt

XBI = bt.load_prices('XBI'); VIX = bt.load_prices('^VIX'); TNX = bt.load_prices('^TNX')

def daily_rets(px, i0, i1):
    out = []
    for k in range(i0 + 1, i1 + 1):
        a, b = px['adj'][k - 1], px['adj'][k]
        if a and b: out.append(b / a - 1)
    return out

def load_fda():
    d = {}
    try:
        for r in csv.DictReader(open('data/fda_designations.csv')):
            d[(r['ticker'], r['pdufa_date'])] = r
    except FileNotFoundError:
        pass
    return d
FDA = load_fda()

def compute(ev):
    px = bt.load_prices(ev['ticker'])
    if not px: return None
    tr = bt.trade(px, ev['pdufa_date'], 30, 7)
    if not tr: return None
    ei = bt.day_on_or_before(px, tr['entry_date'])
    xi = bt.day_on_or_before(XBI, tr['entry_date'])
    if ei is None or xi is None: return None
    # excess target
    xa, xb = XBI['adj'][bt.day_on_or_before(XBI, tr['entry_date'])], XBI['adj'][bt.day_on_or_before(XBI, tr['exit_date'])]
    xret = xb / xa - 1 if xa and xb else None
    excess = tr['ret'] - xret if xret is not None else None
    # --- new point-in-time features (all end at entry ei) ---
    def sret(k0, k1, series=px):
        a, b = series['adj'][k0], series['adj'][k1]
        return (b / a - 1) if (a and b) else None
    # relative strength vs XBI (stock minus XBI) over 21 / 63 / 126 trading days
    rs = {}
    for h in (21, 63, 126):
        if ei - h >= 0 and xi - h >= 0:
            s = sret(ei - h, ei); x = sret(xi - h, xi, XBI)
            rs[h] = (s - x) if (s is not None and x is not None) else None
        else:
            rs[h] = None
    mom126 = sret(ei - 126, ei) if ei - 126 >= 0 else None
    # beta vs XBI over 120d before entry
    beta = None
    if ei - 120 >= 0 and xi - 120 >= 0:
        sr = daily_rets(px, ei - 120, ei); xr = daily_rets(XBI, xi - 120, xi)
        n = min(len(sr), len(xr))
        if n > 30:
            sr, xr = sr[-n:], xr[-n:]
            mx = sum(xr) / n; msr = sum(sr) / n
            cov = sum((xr[i] - mx) * (sr[i] - msr) for i in range(n)) / n
            var = sum((xr[i] - mx) ** 2 for i in range(n)) / n
            beta = cov / var if var > 0 else None
    # ATR14 normalised by entry price
    trs = []
    for k in range(max(1, ei - 13), ei + 1):
        h, l, pc = px['hi'][k], px['lo'][k], px['close'][k - 1]
        if h and l and pc: trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    atr = (sum(trs) / len(trs) / tr['entry_px']) if (trs and tr['entry_px']) else None
    # downside deviation of daily returns over 60d before entry
    dr = daily_rets(px, max(0, ei - 60), ei)
    dnvol = math.sqrt(sum(min(0.0, x) ** 2 for x in dr) / len(dr)) if dr else None
    fda = FDA.get((ev['ticker'], ev['pdufa_date']), {})
    return {
        'ticker': ev['ticker'], 'pdufa_date': ev['pdufa_date'], 'outcome': ev.get('outcome', ''),
        'confidence': ev.get('confidence', ''), 'cohort': ev.get('_cohort', ''),
        'year': ev['pdufa_date'][:4], 'entry_date': tr['entry_date'], 'exit_date': tr['exit_date'],
        'entry_px': round(tr['entry_px'], 4), 'ret': round(tr['ret'], 6),
        'excess': round(excess, 6) if excess is not None else '',
        'beat_xbi': (1 if excess and excess > 0 else 0) if excess is not None else '',
        'rs_21': round(rs[21], 6) if rs[21] is not None else '',
        'rs_63': round(rs[63], 6) if rs[63] is not None else '',
        'rs_126': round(rs[126], 6) if rs[126] is not None else '',
        'mom_126': round(mom126, 6) if mom126 is not None else '',
        'beta_xbi': round(beta, 4) if beta is not None else '',
        'atr14': round(atr, 5) if atr is not None else '',
        'dnvol_60': round(dnvol, 5) if dnvol is not None else '',
        'review_priority': fda.get('review_priority', ''),
        'prior_fda_approvals': fda.get('prior_fda_approvals', ''),
    }

def cohort(fp, c):
    rows = list(csv.DictReader(open(fp)))
    for r in rows: r['_cohort'] = c
    return rows

def splt(r):
    if r['cohort'] == 'P':
        return 'IS' if r['year'] == '2025' else ('OOS' if r['year'] == '2026' else 'other')
    return 'OOS_regime' if r['cohort'] == 'regime2223' else 'orig'

if __name__ == '__main__':
    # merge the v1 point-in-time features (adv_usd, premom, prevol, regime cols) by key
    v1 = {(r['ticker'], r['pdufa_date']): r for r in csv.DictReader(open('data/features.csv'))}
    evs = cohort('data/events_pdufa_bio.csv', 'P') + cohort('data/events_regime_2022_2023.csv', 'regime2223')
    rows = []
    for e in evs:
        r = compute(e)
        if not r: continue
        base = v1.get((r['ticker'], r['pdufa_date']), {})
        for k in ['adv_usd', 'premom_60_30', 'prevol_60_30', 'xbi_above_200d', 'xbi_ret_63d', 'vix', 'tnx', 'tnx_chg_63d']:
            r[k] = base.get(k, '')
        r['split'] = splt(r)
        rows.append(r)
    cols = list(rows[0].keys())
    with open('data/features_v2.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    from collections import Counter
    print(f"features_v2: {len(rows)} events -> data/features_v2.csv")
    print("cols:", cols)
    for c in ['rs_63', 'beta_xbi', 'atr14', 'review_priority', 'prior_fda_approvals']:
        got = sum(1 for r in rows if r[c] not in ('', None))
        print(f"  {c}: {got} non-empty")
    print("review_priority:", dict(Counter(r['review_priority'] or 'unmatched' for r in rows)))
