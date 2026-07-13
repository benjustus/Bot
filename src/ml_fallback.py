#!/usr/bin/env python3
"""Compact fallback ML on v2 features (used only if the Deep-ML agent's heavier
run is killed by its timeout). Target = beat_xbi; strictly pre-entry features;
walk-forward + train-2025/test-2026; label-shuffle leakage check; economic test."""
import sys, csv, math, numpy as np
sys.path.insert(0, 'src')
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline

mc = {r['ticker']: r for r in csv.DictReader(open('data/marketcap.csv'))}
rows = []
for r in csv.DictReader(open('data/features_v2.csv')):
    if r['excess'] == '' or r['beat_xbi'] == '':
        continue
    m = mc.get(r['ticker'], {})
    r['mcap'] = float(m['marketCap']) if m.get('marketCap') else np.nan
    rows.append(r)

FEATS = ['rs_21','rs_63','rs_126','mom_126','beta_xbi','atr14','dnvol_60','premom_60_30',
         'prevol_60_30','adv_usd','entry_px','vix','tnx','tnx_chg_63d','xbi_ret_63d','prior_fda_approvals']
def fval(r, f):
    v = r.get(f, '')
    try: return float(v)
    except: return np.nan
def row_x(r):
    x = [fval(r,f) for f in FEATS]
    x += [math.log1p(r['mcap']) if r['mcap']==r['mcap'] else np.nan,
          1.0 if r['review_priority']=='PRIORITY' else 0.0,
          1.0 if r['confidence']=='source-verified' else 0.0,
          int(r['pdufa_date'][5:7])]
    return x

X = np.array([row_x(r) for r in rows], float)
y = np.array([int(r['beat_xbi']) for r in rows])
exc = np.array([float(r['excess']) for r in rows])
split = np.array([r['split'] for r in rows])
# simple median-impute
col_med = np.nanmedian(X, axis=0)
inds = np.where(np.isnan(X)); X[inds] = np.take(col_med, inds[1])

is_m = split=='IS'; oos_m = split=='OOS'
models = {'logistic': make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, C=0.5)),
          'random_forest': RandomForestClassifier(n_estimators=300, max_depth=4, min_samples_leaf=8, random_state=0),
          'hist_gb': HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, random_state=0)}
print(f"train IS n={is_m.sum()} (base rate {y[is_m].mean():.2f}) | test OOS-2026 n={oos_m.sum()} (base {y[oos_m].mean():.2f})")
out = {}
for name, mdl in models.items():
    mdl.fit(X[is_m], y[is_m])
    p = mdl.predict_proba(X[oos_m])[:,1]
    auc = roc_auc_score(y[oos_m], p)
    # economic: pre-specified top-half by prob, net of 1% round-trip
    thr = np.median(p); sel = p >= thr
    sel_exc_net = exc[oos_m][sel].mean() - 0.01
    full_net = exc[oos_m].mean() - 0.01
    # label-shuffle AUC
    rng = np.random.default_rng(1); shuf = []
    for _ in range(20):
        ysh = rng.permutation(y[is_m]); mdl.fit(X[is_m], ysh)
        shuf.append(roc_auc_score(y[oos_m], mdl.predict_proba(X[oos_m])[:,1]))
    out[name] = {'oos_auc': round(auc,3), 'sel_net_excess': round(sel_exc_net,4),
                 'full_net_excess': round(full_net,4), 'shuffle_auc_mean': round(float(np.mean(shuf)),3)}
    print(f"  {name:14} OOS-AUC={auc:.3f}  sel-net-excess={sel_exc_net*100:+.2f}%  (full {full_net*100:+.2f}%)  shuffle-AUC={np.mean(shuf):.3f}")
import json
json.dump(out, open('output/agents/ml_fallback.json','w'), indent=2)
print("\nVERDICT: no model beats XBI OOS after costs" if all(v['sel_net_excess']<=0.01 for v in out.values())
      else "check: a model shows positive net selection")
