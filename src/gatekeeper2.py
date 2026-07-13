#!/usr/bin/env python3
"""Gegenbeweis / robustness gatekeeper v2 (Agents 1+5+6+9+10, unified).

Independently re-runs an EXPANDED univariate hypothesis family on the v2 feature
set (adds relative strength vs XBI, beta, ATR, momentum, prior-approval count,
and PRIORITY vs STANDARD review) as ONE multiple-testing family, then demands
out-of-sample replication. Same skeptic's court as gatekeeper.py, more features.
"""
import sys, csv, math
import numpy as np
from scipy import stats
sys.path.insert(0, 'src')

def load():
    mc = {r['ticker']: r for r in csv.DictReader(open('data/marketcap.csv'))}
    rows = []
    for r in csv.DictReader(open('data/features_v2.csv')):
        if r['excess'] == '':
            continue
        m = mc.get(r['ticker'], {})
        r['mcap'] = float(m['marketCap']) if m.get('marketCap') else None
        r['excess'] = float(r['excess']); r['entry_px'] = float(r['entry_px'])
        for c in ['rs_21','rs_63','rs_126','mom_126','beta_xbi','atr14','dnvol_60',
                  'adv_usd','premom_60_30','prevol_60_30','xbi_ret_63d','vix','tnx','tnx_chg_63d',
                  'prior_fda_approvals']:
            r[c] = float(r[c]) if r[c] not in ('', 'None', 'N/A') else None
        r['tradeable'] = (r['entry_px'] >= 2 and r['mcap'] is not None and r['mcap'] >= 100e6)
        rows.append(r)
    return rows

def med(rows, f):
    v = sorted(x[f] for x in rows if x[f] is not None)
    return v[len(v)//2] if v else None

def tstat(vals):
    v = [x for x in vals if x is not None]
    if len(v) < 3: return len(v), float('nan'), float('nan'), float('nan')
    t, p = stats.ttest_1samp(v, 0.0)
    # winsorize 1/99 to blunt nano-cap artifacts for the point estimate
    return len(v), float(np.mean(v)), float(t), float(p)

def bh(pv, q=0.05):
    m=len(pv); order=sorted(range(m), key=lambda i: pv[i]); passed=[False]*m; thr=0
    for rank,i in enumerate(order,1):
        if pv[i] <= q*rank/m:
            thr=q*rank/m
            for j in order[:rank]: passed[j]=True
    return passed, thr

def build_hyps(IS):
    H=[]
    H.append(('base','all tradeable', lambda r: True))
    # median splits on numeric features (hi / lo)
    for f,label in [('rs_21','RS21'),('rs_63','RS63'),('rs_126','RS126'),('mom_126','mom126'),
                    ('beta_xbi','beta'),('atr14','atr'),('dnvol_60','dnvol'),
                    ('premom_60_30','premom'),('prevol_60_30','prevol'),
                    ('adv_usd','adv'),('vix','vix'),('tnx','tnx'),('xbi_ret_63d','xbimom')]:
        m=med(IS,f)
        if m is None: continue
        H.append((f'{label}','hi', (lambda ff,mm: (lambda r: r[ff] is not None and r[ff]>=mm))(f,m)))
        H.append((f'{label}','lo', (lambda ff,mm: (lambda r: r[ff] is not None and r[ff]<mm))(f,m)))
    # specific hypotheses of interest
    H.append(('beta','low<0.5', lambda r: r['beta_xbi'] is not None and r['beta_xbi']<0.5))
    H.append(('RS63','strong>+10%', lambda r: r['rs_63'] is not None and r['rs_63']>0.10))
    H.append(('RS63','weak<-10%', lambda r: r['rs_63'] is not None and r['rs_63']<-0.10))
    H.append(('prior','first_timer(0)', lambda r: r['prior_fda_approvals']==0))
    H.append(('prior','experienced(>0)', lambda r: r['prior_fda_approvals'] is not None and r['prior_fda_approvals']>0))
    # review priority (only on covered subset)
    H.append(('review','PRIORITY', lambda r: r['review_priority']=='PRIORITY'))
    H.append(('review','STANDARD', lambda r: r['review_priority']=='STANDARD'))
    # a couple of promising 2-way interactions (small microcap + strong RS; low beta + priority)
    H.append(('combo','smallcap&strongRS', lambda r: r['mcap'] is not None and r['mcap']<1e9 and r['rs_63'] is not None and r['rs_63']>0))
    H.append(('combo','priority&strongRS', lambda r: r['review_priority']=='PRIORITY' and r['rs_63'] is not None and r['rs_63']>0))
    return H

def run():
    data=load()
    IS=[r for r in data if r['split']=='IS' and r['tradeable']]
    OOS=[r for r in data if r['split']=='OOS' and r['tradeable']]
    REG=[r for r in data if r['split']=='OOS_regime']
    H=build_hyps(IS)
    res=[]
    for fam,name,f in H:
        n,mean,t,p=tstat([r['excess'] for r in IS if f(r)])
        no,meano,to,po=tstat([r['excess'] for r in OOS if f(r)])
        nr,meanr,_,_=tstat([r['excess'] for r in REG if f(r)])
        res.append({'family':fam,'name':name,'is_n':n,'is_mean':mean,'is_t':t,'is_p':p,
                    'oos_n':no,'oos_mean':meano,'reg_n':nr,'reg_mean':meanr})
    valid=[r for r in res if r['is_p']==r['is_p'] and r['is_n']>=12]
    ps=[r['is_p'] for r in valid]; passed,thr=bh(ps)
    for r,pa in zip(valid,passed): r['bh']=pa
    for r in res: r.setdefault('bh',False)
    raw_sig=[r for r in valid if r['is_p']<0.05]
    survivors=[r for r in valid if r['bh'] and r['oos_mean']>0 and (r['reg_n']<10 or r['reg_mean']>0)]
    import json
    json.dump({'n_hyp':len(valid),'bh_thr':thr,'exp_fp':0.05*len(valid),
               'raw_sig':len(raw_sig),'survivors':len(survivors),'results':res},
              open('output/agents/gatekeeper2.json','w'),indent=2,default=str)
    print(f"EXPANDED family: {len(valid)} hypotheses. Expected FP@0.05: {0.05*len(valid):.1f}. Raw-significant: {len(raw_sig)}.")
    print(f"BH-FDR pass: {sum(r['bh'] for r in valid)} (thr p<={thr:.4f}). Survive BH+hold-out: {len(survivors)}\n")
    print(f"{'family':10}{'hyp':16}{'ISn':>4}{'ISexc':>8}{'t':>6}{'p':>7}{'BH':>3}{'OOSn':>5}{'OOSexc':>8}{'REGexc':>8}")
    for r in sorted(res, key=lambda x: (x['is_p'] if x['is_p']==x['is_p'] else 9)):
        if r['is_n']<12: continue
        rm = (r['reg_mean']*100 if r['reg_n'] else float('nan'))
        print(f"{r['family']:10}{r['name']:16}{r['is_n']:>4}{r['is_mean']*100:>+7.2f}%{r['is_t']:>6.2f}{r['is_p']:>7.3f}{'Y' if r['bh'] else '.':>3}{r['oos_n']:>5}{r['oos_mean']*100:>+7.2f}%{rm:>+7.2f}%")
    print("\nVERDICT:", "NO hypothesis survives multiple-testing + hold-out." if not survivors
          else f"{len(survivors)} survive: "+", ".join(f"{s['family']}/{s['name']}" for s in survivors))

if __name__=='__main__':
    run()
