#!/usr/bin/env python3
"""Master reproducible pipeline. Regenerates every number cited in REPORT.md
into output/results.json. Assumes prices are cached (run fetch_all_prices.py and
fetch_marketcap.py first, or use the committed data/prices cache)."""
import sys, csv, json, random, statistics as st
sys.path.insert(0, 'src')
import backtest as bt, analyze as az

def events(fp): return list(csv.DictReader(open(fp)))
VAR = {'A': (30, 7), 'B': (45, 7), 'C': (30, 3), 'D': (21, 7)}

def core(evs, subsetfn=lambda t: True, eo=30, xo=7):
    tr, sk = bt.run_variant(evs, eo, xo); az.enrich(tr)
    tr = [t for t in tr if subsetfn(t)]
    raw = az.vstats([t['ret'] for t in tr]); exc = az.vstats([t['excess'] for t in tr])
    return {'n': len(tr), 'raw': raw, 'excess': exc,
            'boot_raw': az.bootstrap([t['ret'] for t in tr]),
            'boot_exc': az.bootstrap([t['excess'] for t in tr]),
            'sign_p_raw': az.sign_test_p([t['ret'] for t in tr]),
            'sign_p_exc': az.sign_test_p([t['excess'] for t in tr]), 'skipped': sk}

def mc(trades, iters=3000):
    ends = []
    for s in range(iters):
        random.seed(s)
        o = trades[:]; random.shuffle(o); o.sort(key=lambda t: t['entry_date'])
        chosen = []; busy = None
        for t in o:
            if busy is None or t['entry_date'] > busy:
                chosen.append(t); busy = t['exit_date']
        cap = 1500.0; loss = 0.0
        for t in chosen:
            pl = cap * t['ret'] - 2.0; tax = 0.0
            if pl > 0:
                off = min(loss, pl); loss -= off; tax = (pl - off) * 0.26375
            else:
                loss += -pl
            cap = cap + (cap * t['ret'] - 2.0) - tax
        ends.append(cap)
    ends.sort(); n = len(ends)
    return {'median': ends[n//2], 'p5': ends[int(.05*n)], 'p95': ends[int(.95*n)],
            'min': ends[0], 'max': ends[-1], 'p_loss': sum(1 for x in ends if x < 1500)/n,
            'p_sub1000': sum(1 for x in ends if x < 1000)/n}

def bh(px, d0, d1):
    i = bt.day_on_or_before(px, d0); j = bt.day_on_or_before(px, d1)
    a, b = px['adj'][i], px['adj'][j]
    seg = [px['adj'][k] for k in range(i, j+1) if px['adj'][k]]
    peak = seg[0]; mdd = 0
    for v in seg:
        peak = max(peak, v); mdd = min(mdd, v/peak - 1)
    return {'ret': b/a - 1, 'maxdd': mdd}

def main():
    R = {'meta': {}, 'audit': {}, 'core': {}, 'splits': {}, 'capital': {},
         'robustness': {}, 'regime_cohort': {}, 'external': {}}
    P = events('data/events_pdufa_bio.csv')
    O = events('data/events_original16.csv')
    G = events('data/events_regime_2022_2023.csv')

    # ---- AUDIT: original-16 replication ----
    tro, _ = bt.run_variant(O, 30, 7); az.enrich(tro)
    so = az.vstats([t['ret'] for t in tro])
    _, cap0 = bt.simulate(tro, 1500, 2.0, use_allowance=False)
    _, cap1 = bt.simulate(tro, 1500, 2.0, use_allowance=True, allowance=1000.0)
    R['audit'] = {'n': len(tro), 'mean': so['mean'], 'median': so['median'], 'hit': so['hit'],
                  'pf': so['pf'], 'std': so['std'],
                  'excess_mean': az.vstats([t['excess'] for t in tro])['mean'],
                  'cap_noFB': cap0['end'], 'cap_FB': cap1['end'], 'cap_maxdd': cap0['maxdd']}

    # ---- CORE cohort P, all variants + subsets ----
    R['core']['variants'] = {k: core(P, eo=eo, xo=xo) for k, (eo, xo) in VAR.items()}
    R['core']['subsets'] = {
        'full': core(P), 'tradeable': core(P, lambda t: t['tradeable']),
        'source_verified': core(P, lambda t: t['confidence'] == 'source-verified'),
        'tradeable_nonother': core(P, lambda t: t['tradeable'] and t['confidence'] != 'other')}

    # ---- SPLITS (variant A) ----
    tr, _ = bt.run_variant(P, 30, 7); az.enrich(tr)
    def grp(keyfn):
        from collections import defaultdict
        d = defaultdict(list)
        for t in tr: d[keyfn(t)].append(t)
        return {str(k): {'n': len(v), 'raw': az.vstats([x['ret'] for x in v]),
                         'excess': az.vstats([x['excess'] for x in v])} for k, v in d.items()}
    R['splits'] = {'outcome': grp(lambda t: t['outcome']),
                   'mcap': grp(lambda t: t['mcap_tier']),
                   'regime': grp(lambda t: t['regime']),
                   'confidence': grp(lambda t: t['confidence'])}

    # ---- CAPITAL ----
    trad = [t for t in tr if t['tradeable']]
    _, g = bt.simulate(trad, 1500, 2.0, use_allowance=False)
    R['capital'] = {'honest_greedy_end': g['end'], 'honest_greedy_maxdd': g['maxdd'],
                    'mc_full': mc(tr), 'mc_tradeable': mc(trad),
                    'bench': {b: bh(bt.load_prices(b), '2024-12-31', '2026-06-30')
                              for b in ['XBI', 'IBB', '^GSPC']}}

    # ---- ROBUSTNESS: timing grid + frictions ----
    grid = {}
    for eo in [25, 30, 35, 45]:
        for xo in [2, 7, 12]:
            t2, _ = bt.run_variant(P, eo, xo); az.enrich(t2)
            grid[f'{eo}/{xo}'] = {'raw': az.vstats([x['ret'] for x in t2])['mean'],
                                  'exc': az.vstats([x['excess'] for x in t2])['mean']}
    base = az.vstats([t['ret'] for t in tr])['mean']
    fric = {'base': base}
    for slip in [0.005, 0.015]:
        fric[f'slip_{slip}'] = sum((1+t['ret'])*(1-slip)/(1+slip)-1 for t in tr)/len(tr)
    EUR = bt.load_prices('EURUSD=X')
    fxv = []
    for t in tr:
        i = bt.day_on_or_before(EUR, t['entry_date']); j = bt.day_on_or_before(EUR, t['exit_date'])
        if i is not None and j is not None and EUR['adj'][i] and EUR['adj'][j]:
            fxv.append((1+t['ret'])*(EUR['adj'][i]/EUR['adj'][j])-1)
    fric['fx_eur'] = az.vstats(fxv)['mean']
    # gap risk hold -7..+3
    def through(evs):
        rr = []
        for e in evs:
            px = bt.load_prices(e['ticker'])
            if not px: continue
            t = bt.trade(px, e['pdufa_date'], 7, -3)
            if t: rr.append(t['ret'])
        return az.vstats(rr)
    R['robustness'] = {'grid': grid, 'frictions': fric,
                       'gap_approved': through([e for e in P if e['outcome']=='Approved']),
                       'gap_crl': through([e for e in P if e['outcome']=='CRL']),
                       'gap_all': through(P)}

    # ---- REGIME cohort 2022-2023 ----
    trg, skg = bt.run_variant(G, 30, 7); az.enrich(trg)
    R['regime_cohort'] = {'n_priced': len(trg), 'n_events': len(G), 'unavailable': skg['no_prices'],
        'raw': az.vstats([t['ret'] for t in trg]), 'excess': az.vstats([t['excess'] for t in trg]),
        'by_year': {y: {'raw': az.vstats([t['ret'] for t in trg if t['pdufa_date'][:4]==y]),
                        'excess': az.vstats([t['excess'] for t in trg if t['pdufa_date'][:4]==y])}
                    for y in ['2022','2023']}}

    # ---- external cross-reference (pdufa.bio published run-up-by-year, T-120..T-1) ----
    R['external']['pdufa_bio_runup_T120'] = {
        '2020': 12.9, '2021': 7.3, '2022': -5.1, '2023': -3.8, '2024': 12.6, '2025': 13.0, '2026': 11.5}

    # coverage meta
    tickers = sorted({e['ticker'] for e in P})
    priced = sum(1 for t in tickers if bt.load_prices(t))
    R['meta'] = {'cohortP_events': len(P), 'cohortP_tickers': len(tickers),
                 'cohortP_priced_tickers': priced, 'regime_events': len(G)}

    json.dump(R, open('output/results.json', 'w'), indent=2, default=lambda o: round(o,6) if isinstance(o,float) else str(o))
    print("wrote output/results.json")
    # headline
    fa = R['core']['subsets']
    print(f"\nHEADLINE (Variant A -30->-7):")
    for k in ['full','tradeable','source_verified']:
        s=fa[k]; print(f"  {k:16} n={s['n']:3d}  raw {s['raw']['mean']*100:+.2f}% (t={s['raw']['tstat']:+.2f})  "
                        f"excess {s['excess']['mean']*100:+.2f}% (t={s['excess']['tstat']:+.2f}) med {s['excess']['median']*100:+.2f}% hit {s['excess']['hit']*100:.0f}%")
    print(f"  XBI buy&hold same span: {R['capital']['bench']['XBI']['ret']*100:+.1f}%  vs MC-tradeable median {R['capital']['mc_tradeable']['median']:.0f} EUR")

if __name__ == '__main__':
    main()
