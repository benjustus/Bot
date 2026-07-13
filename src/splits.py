#!/usr/bin/env python3
"""Segment splits, capital simulation, robustness, CRL gap-risk analysis."""
import sys, csv, json, math, statistics as st, datetime as dt
from collections import defaultdict
sys.path.insert(0, 'src')
import backtest as bt, analyze as az

EUR = bt.load_prices('EURUSD=X')

def load_events(fp): return list(csv.DictReader(open(fp)))

def split_table(trades, keyfn, title, key='ret'):
    groups = defaultdict(list)
    for t in trades:
        groups[keyfn(t)].append(t)
    print(f"\n--- {title} ---")
    print(f"{'group':16}{'n':>4} {'meanRAW':>9}{'medRAW':>9}{'hit':>7}{'PF':>6}  {'meanEXC':>9}{'hitEXC':>8}{'t_exc':>7}")
    rows={}
    for g in sorted(groups, key=lambda x:str(x)):
        ts=groups[g]
        raw=az.vstats([t['ret'] for t in ts]); exc=az.vstats([t['excess'] for t in ts])
        rows[g]={'raw':raw,'excess':exc}
        if raw['n']==0: continue
        em = exc.get('mean',float('nan')); eh=exc.get('hit',float('nan')); et=exc.get('tstat',float('nan'))
        print(f"{str(g):16}{raw['n']:>4} {raw['mean']*100:>+8.2f}%{raw['median']*100:>+8.2f}%{raw['hit']*100:>6.1f}%{raw['pf']:>6.2f}  "
              f"{em*100:>+8.2f}%{eh*100:>7.1f}%{et:>+7.2f}")
    return rows

def capital_variants(trades):
    print(f"\n{'='*70}\nCAPITAL SIMULATION (all-in roll-over, Variant A)\n{'='*70}")
    res={}
    for lbl,kw in [('no Freibetrag',dict(use_allowance=False)),
                   ('with Freibetrag 1000/yr',dict(use_allowance=True,allowance=1000.0))]:
        rows,summ=bt.simulate(trades, capital=1500.0, fee_roundtrip=2.0, **kw)
        res[lbl]=summ
        print(f"\n{lbl}: chain trades={summ['n_chain']}  end={summ['end']:.0f} EUR "
              f"({summ['ret_total']*100:+.1f}%)  tax={summ['tax_total']:.0f}  maxDD={summ['maxdd']*100:.1f}%  "
              f"CAGR={summ['cagr']*100:+.1f}% over {summ['years']:.2f}y")
    return res

def robustness(events):
    print(f"\n{'='*70}\nROBUSTNESS\n{'='*70}")
    out={}
    # entry/exit shifts +/-5d
    print("\nEntry/Exit timing grid (mean RAW% / mean EXCESS% / hit%):")
    print(f"{'entry|exit':>10}", end='')
    exits=[2,7,12]
    for xo in exits: print(f"{'-'+str(xo)+'d':>18}", end='')
    print()
    for eo in [25,30,35,45]:
        print(f"{'-'+str(eo)+'d':>10}", end='')
        for xo in exits:
            tr,_=bt.run_variant(events,eo,xo); az.enrich(tr)
            r=az.vstats([t['ret'] for t in tr]); e=az.vstats([t['excess'] for t in tr])
            print(f"  {r['mean']*100:+5.1f}/{e['mean']*100:+5.1f}/{r['hit']*100:4.0f}", end='')
        print()
    # fees, slippage, FX on Variant A
    tr,_=bt.run_variant(events,30,7); az.enrich(tr)
    base=az.vstats([t['ret'] for t in tr])['mean']
    def mean_after(fn):
        return sum(fn(t) for t in tr)/len(tr)
    print(f"\nFrictions on Variant A (mean raw/trade, n={len(tr)}):")
    print(f"  base (adj close, no cost)      : {base*100:+.2f}%")
    # per-trade fee on 1500 capital -> 2/1500 = 0.133% each way already tiny; model % slippage
    for slip in [0.005,0.015]:
        m=mean_after(lambda t: (1+t['ret'])*(1-slip)/(1+slip)-1)  # buy up, sell down
        print(f"  + slippage {slip*100:.1f}%/side        : {m*100:+.2f}%  (Δ {(m-base)*100:+.2f}pp)")
    # FX: convert USD trade return to EUR using EURUSD at entry/exit
    def fx_ret(t):
        ei=bt.day_on_or_before(EUR,t['entry_date']); xi=bt.day_on_or_before(EUR,t['exit_date'])
        if ei is None or xi is None: return None
        # EURUSD=X is USD per EUR; a EUR investor's return in EUR = (1+usd_ret)*(fx_e/fx_x)-1
        fe,fx=EUR['adj'][ei],EUR['adj'][xi]
        if not fe or not fx: return None
        return (1+t['ret'])*(fe/fx)-1
    fxv=[fx_ret(t) for t in tr]; fxs=az.vstats(fxv)
    print(f"  + USD/EUR FX (EUR-denominated) : {fxs['mean']*100:+.2f}%  (Δ {(fxs['mean']-base)*100:+.2f}pp), sd {fxs['std']*100:.2f}%")
    out['fx']=fxs
    return out

def crl_gap_risk(events):
    """What the -7d exit avoids: hold-through-event return (T-7 -> T+3)."""
    print(f"\n{'='*70}\nCRL / EVENT-GAP RISK (why the -7d exit exists)\n{'='*70}")
    approved=[e for e in events if e['outcome']=='Approved']
    crl=[e for e in events if e['outcome']=='CRL']
    # hold from -7d to +3d (through the decision)
    def through(evs):
        rr=[]
        for e in evs:
            px=bt.load_prices(e['ticker'])
            if not px: continue
            t=bt.trade(px,e['pdufa_date'],7,-3)  # entry -7, exit +3
            if t: rr.append(t['ret'])
        return az.vstats(rr)
    for lbl,evs in [('Approved',approved),('CRL',crl),('All',events)]:
        s=through(evs)
        if s['n']:
            print(f"  hold -7d..+3d {lbl:9}: n={s['n']:3d} mean={s['mean']*100:+6.2f}% med={s['median']*100:+6.2f}% "
                  f"worst={s['worst']*100:+6.1f}% hit={s['hit']*100:.0f}%")

if __name__=='__main__':
    events=load_events('data/events_pdufa_bio.csv')
    tr,_=bt.run_variant(events,30,7); az.enrich(tr)
    print(f"{'='*70}\nSEGMENT SPLITS — pdufa.bio cohort, Variant A (-30->-7), n={len(tr)}\n{'='*70}")
    outcome=split_table(tr, lambda t:t['outcome'], "By eventual FDA outcome")
    size=split_table(tr, lambda t:t['mcap_tier'], "By market-cap tier (current proxy)")
    regime=split_table(tr, lambda t:t['regime'], "By XBI regime at entry (63d trailing)")
    conf=split_table(tr, lambda t:t['confidence'], "By source confidence")
    cap=capital_variants(tr)
    rob=robustness(events)
    crl_gap_risk(events)
    json.dump({'note':'see console'}, open('output/splits_done.json','w'))
