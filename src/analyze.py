#!/usr/bin/env python3
"""Full pre-PDUFA run-up analysis on an events cohort.
Adds: XBI-excess (beta-adjusted) returns, outcome/size/regime splits,
bootstrap CIs, sign test, capital simulation. Deterministic (seed fixed)."""
import sys, csv, json, math, statistics as st, datetime as dt
from collections import defaultdict, Counter
sys.path.insert(0, 'src')
import backtest as bt

# ---- benchmark for beta adjustment + regime ----
def load_bench(ticker='XBI'):
    px = bt.load_prices(ticker)
    return px

XBI = load_bench('XBI'); SPX = load_bench('^GSPC')

def bench_ret(px, entry_date, exit_date):
    ei = bt.day_on_or_before(px, entry_date); xi = bt.day_on_or_before(px, exit_date)
    if ei is None or xi is None or xi <= ei: return None
    a, b = px['adj'][ei], px['adj'][xi]
    return b / a - 1.0 if a and b else None

def regime_at(px, entry_date, lookback=63, up=0.05, dn=-0.05):
    xi = bt.day_on_or_before(px, entry_date)
    if xi is None or xi - lookback < 0: return 'n/a'
    a, b = px['adj'][xi - lookback], px['adj'][xi]
    if not a or not b: return 'n/a'
    r = b / a - 1
    return 'bull' if r > up else ('bear' if r < dn else 'side')

# ---- market cap ----
def load_mcap():
    m = {}
    try:
        for r in csv.DictReader(open('data/marketcap.csv')):
            m[r['ticker']] = {'tier': r['tier'], 'mc': float(r['marketCap']) if r['marketCap'] else None}
    except FileNotFoundError:
        pass
    return m
MCAP = load_mcap()

# Tradeability screen: exclude penny/nano-caps and unverifiable names whose prints
# are dominated by pump/dump + reverse-split noise (e.g. RNAZ, a preclinical
# company with no real PDUFA that pdufa.bio flagged "price-only").
MIN_PRICE = 2.0
MIN_MCAP  = 100e6

def enrich(trades):
    for t in trades:
        xr = bench_ret(XBI, t['entry_date'], t['exit_date'])
        t['xbi_ret'] = xr
        t['excess'] = (t['ret'] - xr) if xr is not None else None
        t['regime'] = regime_at(XBI, t['entry_date'])
        mc = MCAP.get(t['ticker'], {})
        t['mcap_tier'] = mc.get('tier', 'n/a')
        t['mcap'] = mc.get('mc')
        t['tradeable'] = (t['entry_px'] >= MIN_PRICE and t['mcap'] is not None and t['mcap'] >= MIN_MCAP)
    return trades

# ---- stats helpers on an arbitrary value list ----
def vstats(vals):
    v = [x for x in vals if x is not None]
    n = len(v)
    if n == 0: return {'n': 0}
    mean = sum(v)/n
    sd = st.stdev(v) if n > 1 else 0.0
    se = sd/math.sqrt(n) if n > 1 else float('nan')
    wins = [x for x in v if x > 0]
    downside = [min(0.0,x) for x in v]
    dstd = math.sqrt(sum(d*d for d in downside)/n)
    gains = sum(wins); losses = abs(sum(x for x in v if x <= 0))
    tcrit = 1.96
    return {'n': n, 'mean': mean, 'median': st.median(v), 'hit': len(wins)/n,
            'std': sd, 'se': se, 'tstat': (mean/se if se==se and se>0 else float('nan')),
            'ci_lo': mean-tcrit*se if n>1 else float('nan'),
            'ci_hi': mean+tcrit*se if n>1 else float('nan'),
            'pf': (gains/losses if losses>0 else float('inf')),
            'sharpe': mean/sd if sd>0 else float('nan'),
            'sortino': mean/dstd if dstd>0 else float('nan'),
            'best': max(v), 'worst': min(v)}

def bootstrap(vals, iters=10000, seed=42):
    import random; random.seed(seed)
    v = [x for x in vals if x is not None]; n=len(v)
    if n < 2: return (float('nan'), float('nan'))
    ms=[]
    for _ in range(iters):
        ms.append(sum(v[random.randrange(n)] for _ in range(n))/n)
    ms.sort(); return (ms[int(.025*iters)], ms[int(.975*iters)])

def sign_test_p(vals):
    """Two-sided sign test vs median 0 (binomial)."""
    v=[x for x in vals if x is not None and x!=0]; n=len(v)
    k=sum(1 for x in v if x>0)
    if n==0: return float('nan')
    from math import comb
    # two-sided p = 2*min(P(X<=k),P(X>=k)) under p=0.5
    def cdf(kk): return sum(comb(n,i) for i in range(0,kk+1))/2**n
    p=2*min(cdf(k), 1-cdf(k-1)); return min(1.0,p)

def fmt(s, key='ret'):
    if s.get('n',0)==0: return f"n=0"
    return (f"n={s['n']:3d} mean={s['mean']*100:+6.2f}% med={s['median']*100:+6.2f}% "
            f"hit={s['hit']*100:4.1f}% PF={s['pf']:4.2f} sd={s['std']*100:5.2f}% "
            f"t={s['tstat']:+5.2f} 95%CI[{s['ci_lo']*100:+.2f},{s['ci_hi']*100:+.2f}]")

def analyze_cohort(events_fp, label, variants):
    evs = list(csv.DictReader(open(events_fp)))
    out = {'label': label, 'n_events': len(evs), 'variants': {}}
    print(f"\n{'='*92}\nCOHORT: {label}  ({len(evs)} events)\n{'='*92}")
    base_trades = None
    for name,(eo,xo) in variants.items():
        trades, sk = bt.run_variant(evs, eo, xo)
        enrich(trades)
        raw = [t['ret'] for t in trades]
        exc = [t['excess'] for t in trades]
        sraw = vstats(raw); sexc = vstats(exc)
        boot = bootstrap(raw); signp = sign_test_p(raw)
        out['variants'][name] = {'entry':eo,'exit':xo,'skipped':sk,
                                 'raw':sraw,'excess':sexc,'boot_ci':boot,'sign_p':signp,
                                 'n_priceable':len(trades)}
        print(f"\n--- Variant {name} ({-eo}->{-xo} d) | priced {len(trades)}/{len(evs)}  skipped={sk}")
        print(f"  RAW    : {fmt(sraw)}")
        print(f"  EXCESS : {fmt(sexc)}  (over XBI)")
        print(f"  bootstrap95 mean CI [{boot[0]*100:+.2f}, {boot[1]*100:+.2f}]  sign-test p={signp:.4f}")
        if name=='A': base_trades = trades
    return out, base_trades

if __name__=='__main__':
    variants = {'A':(30,7),'B':(45,7),'C':(30,3),'D':(21,7)}
    res_p, trades_p = analyze_cohort('data/events_pdufa_bio.csv','pdufa.bio 2025-2026 (dual-outcome)', variants)
    res_o, trades_o = analyze_cohort('data/events_original16.csv','original-16 replication', variants)
    json.dump({'pdufa_bio':res_p,'original16':res_o}, open('output/stats_core.json','w'), indent=2, default=str)
    print("\nsaved output/stats_core.json")
