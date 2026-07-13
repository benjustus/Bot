#!/usr/bin/env python3
"""Overfitting / hold-out gatekeeper (Stream 12).

Independently re-runs EVERY conditioning hypothesis from the discovery streams as
ONE multiple-testing family, then demands out-of-sample replication. A candidate
"edge" is only credible if its in-sample XBI-excess survives Benjamini-Hochberg
FDR across the whole search AND stays positive on the 2026 + 2022-23 hold-outs.

This is the skeptic's court: the whole point is that scanning ~35 sub-samples of
a noisy dataset WILL throw up a few "significant" cells by pure chance.
"""
import sys, csv, math
import numpy as np
from scipy import stats
sys.path.insert(0, 'src')

def load():
    rows = list(csv.DictReader(open('data/features.csv')))
    mc = {r['ticker']: r for r in csv.DictReader(open('data/marketcap.csv'))}
    out = []
    for r in rows:
        if r['excess'] == '':
            continue
        m = mc.get(r['ticker'], {})
        r['mcap'] = float(m['marketCap']) if m.get('marketCap') else None
        r['excess'] = float(r['excess'])
        r['entry_px'] = float(r['entry_px'])
        r['adv'] = float(r['adv_usd']) if r['adv_usd'] else None
        for c in ['premom_60_30', 'prevol_60_30', 'xbi_ret_63d', 'vix', 'tnx', 'tnx_chg_63d']:
            r[c] = float(r[c]) if r[c] not in ('', 'None') else None
        r['xbi_above_200d'] = r['xbi_above_200d']
        # tradeable screen
        r['tradeable'] = (r['entry_px'] >= 2 and r['mcap'] is not None and r['mcap'] >= 100e6)
        out.append(r)
    return out

def tstat(vals):
    v = [x for x in vals if x is not None]
    if len(v) < 3:
        return len(v), (np.mean(v) if v else float('nan')), float('nan'), float('nan')
    t, p = stats.ttest_1samp(v, 0.0)
    return len(v), float(np.mean(v)), float(t), float(p)

def bh_fdr(pvals, q=0.05):
    """Benjamini-Hochberg: return boolean pass and the largest threshold."""
    m = len(pvals)
    order = sorted(range(m), key=lambda i: pvals[i])
    passed = [False] * m
    thresh = 0.0
    for rank, i in enumerate(order, 1):
        if pvals[i] <= q * rank / m:
            thresh = q * rank / m
            for j in order[:rank]:
                passed[j] = True
    return passed, thresh

def hypotheses(data):
    """Yield (family, name, filterfn) over the tradeable universe."""
    def q(field, lo, hi):
        return lambda r: (r[field] is not None and (lo is None or r[field] >= lo) and (hi is None or r[field] < hi))
    H = []
    H.append(('base', 'all tradeable', lambda r: True))
    # market cap (7 buckets, $)
    for name, lo, hi in [('<100M',0,1e8),('100-300M',1e8,3e8),('300-500M',3e8,5e8),
                         ('500M-1B',5e8,1e9),('1-2B',1e9,2e9),('2-5B',2e9,5e9),('>5B',5e9,None)]:
        H.append(('mktcap', name, q('mcap', lo, hi)))
    # regime
    H.append(('regime', 'XBI>200dMA', lambda r: r['xbi_above_200d']=='1'))
    H.append(('regime', 'XBI<200dMA', lambda r: r['xbi_above_200d']=='0'))
    H.append(('regime', 'VIX<15', q('vix', None, 15)))
    H.append(('regime', 'VIX15-25', q('vix', 15, 25)))
    H.append(('regime', 'VIX>25', q('vix', 25, None)))
    H.append(('regime', 'rates_rising', lambda r: r['tnx_chg_63d'] is not None and r['tnx_chg_63d']>0))
    H.append(('regime', 'rates_falling', lambda r: r['tnx_chg_63d'] is not None and r['tnx_chg_63d']<0))
    H.append(('regime', 'XBI_mom>0', lambda r: r['xbi_ret_63d'] is not None and r['xbi_ret_63d']>0))
    H.append(('regime', 'XBI_mom<0', lambda r: r['xbi_ret_63d'] is not None and r['xbi_ret_63d']<0))
    # liquidity (ADV $ quartiles, approx fixed cutoffs)
    for name, lo, hi in [('ADV<3M',0,3e6),('ADV3-15M',3e6,15e6),('ADV15-60M',15e6,60e6),('ADV>60M',60e6,None)]:
        H.append(('liquidity', name, q('adv', lo, hi)))
    # price buckets
    for name, lo, hi in [('px<2',0,2),('px2-5',2,5),('px5-20',5,20),('px>20',20,None)]:
        H.append(('price', name, q('entry_px', lo, hi)))
    # pre-entry momentum / vol
    H.append(('premom', 'premom>0', lambda r: r['premom_60_30'] is not None and r['premom_60_30']>0))
    H.append(('premom', 'premom<0', lambda r: r['premom_60_30'] is not None and r['premom_60_30']<0))
    H.append(('prevol', 'prevol_hi', lambda r: r['prevol_60_30'] is not None and r['prevol_60_30']>0.05))
    H.append(('prevol', 'prevol_lo', lambda r: r['prevol_60_30'] is not None and r['prevol_60_30']<=0.05))
    # confidence
    H.append(('conf', 'source-verified', lambda r: r['confidence']=='source-verified'))
    return H

def run():
    data = load()
    IS = [r for r in data if r['split']=='IS' and r['tradeable']]
    OOS = [r for r in data if r['split']=='OOS' and r['tradeable']]
    REG = [r for r in data if r['split']=='OOS_regime']  # 2022-23 (any liquidity; small)
    H = hypotheses(data)
    results = []
    for fam, name, f in H:
        n, mean, t, p = tstat([r['excess'] for r in IS if f(r)])
        no, meano, to, po = tstat([r['excess'] for r in OOS if f(r)])
        nr, meanr, tr, pr = tstat([r['excess'] for r in REG if f(r)])
        results.append({'family':fam,'name':name,'is_n':n,'is_mean':mean,'is_t':t,'is_p':p,
                        'oos_n':no,'oos_mean':meano,'reg_n':nr,'reg_mean':meanr})
    # BH-FDR across the whole family (drop nan p)
    valid = [r for r in results if r['is_p']==r['is_p'] and r['is_n']>=10]
    ps = [r['is_p'] for r in valid]
    passed, thr = bh_fdr(ps, 0.05)
    for r, pa in zip(valid, passed):
        r['bh_pass'] = pa
    for r in results:
        r.setdefault('bh_pass', False)
    exp_fp = 0.05 * len(valid)  # expected false positives at raw p<0.05
    raw_sig = [r for r in valid if r['is_p'] < 0.05]
    # a candidate "survives" only if BH-pass AND OOS mean>0 AND regime mean>0 (replication)
    survivors = [r for r in valid if r['bh_pass'] and r['oos_mean']>0 and (r['reg_n']<10 or r['reg_mean']>0)]
    import json
    json.dump({'n_hypotheses':len(valid),'bh_threshold':thr,'expected_false_pos':exp_fp,
               'raw_significant':len(raw_sig),'survivors':len(survivors),'results':results},
              open('output/agents/gatekeeper.json','w'), indent=2, default=str)

    print(f"Tested {len(valid)} hypotheses (one multiple-testing family).")
    print(f"Expected false positives at raw p<0.05: {exp_fp:.1f}. Observed raw-significant: {len(raw_sig)}.")
    print(f"Benjamini-Hochberg (FDR 5%) passing: {sum(r['bh_pass'] for r in valid)}   BH threshold p<={thr:.4f}")
    print(f"Survivors (BH-pass AND positive on BOTH hold-outs): {len(survivors)}\n")
    print(f"{'family':10}{'hypothesis':16}{'IS n':>5}{'IS exc':>8}{'t':>6}{'p':>7}{'BH':>4}{'OOSn':>5}{'OOSexc':>8}{'REGexc':>8}")
    for r in sorted(results, key=lambda x: (x['is_p'] if x['is_p']==x['is_p'] else 9)):
        if r['is_n'] < 10: continue
        print(f"{r['family']:10}{r['name']:16}{r['is_n']:>5}{r['is_mean']*100:>+7.2f}%{r['is_t']:>6.2f}{r['is_p']:>7.3f}"
              f"{'Y' if r['bh_pass'] else '·':>4}{r['oos_n']:>5}{r['oos_mean']*100:>+7.2f}%{(r['reg_mean']*100 if r['reg_n'] else float('nan')):>+7.2f}%")
    print("\nVERDICT:", "NO hypothesis survives multiple-testing + hold-out replication."
          if not survivors else f"{len(survivors)} candidate(s) survive: "+", ".join(f"{s['family']}/{s['name']}" for s in survivors))
    return results, survivors

if __name__ == '__main__':
    run()
