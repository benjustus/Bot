#!/usr/bin/env python3
"""Build the shared per-event feature table used by every research stream.

Every feature is POINT-IN-TIME as of the entry day (T-30 by default): only
information available before entry is used (no look-ahead). Target labels
(excess return, beat_xbi) are for evaluation only and must never be used as
model inputs.

Split: cohort-P 2025 = in-sample (discovery); cohort-P 2026 = out-of-sample
hold-out; 2022-2023 approvals cohort = separate regime hold-out.
"""
import sys, csv, statistics as st, datetime as dt
sys.path.insert(0, 'src')
import backtest as bt

XBI = bt.load_prices('XBI'); VIX = bt.load_prices('^VIX'); TNX = bt.load_prices('^TNX')

def idx(px, date):
    return bt.day_on_or_before(px, date)

def ret(px, i, j):
    if i is None or j is None or i < 0 or j is None: return None
    a, b = px['adj'][i], px['adj'][j]
    return (b/a - 1) if a and b else None

def series_ret(px, i0, i1):
    out = []
    for k in range(i0+1, i1+1):
        a, b = px['adj'][k-1], px['adj'][k]
        if a and b: out.append(b/a - 1)
    return out

def feat_row(ev, entry_off=30, exit_off=7):
    px = bt.load_prices(ev['ticker'])
    if not px: return None
    tr = bt.trade(px, ev['pdufa_date'], entry_off, exit_off)
    if not tr: return None
    ei = idx(px, tr['entry_date'])
    d0 = dt.date.fromisoformat(ev['pdufa_date'])
    # excess over XBI on the base window
    xr = ret(XBI, idx(XBI, tr['entry_date']), idx(XBI, tr['exit_date']))
    excess = (tr['ret'] - xr) if xr is not None else None
    # point-in-time liquidity: avg $volume over 20 trading days ending at entry
    dv = []
    for k in range(max(0, ei-19), ei+1):
        c, v = px['close'][k], px['vol'][k]
        if c and v: dv.append(c*v)
    advol = (sum(dv)/len(dv)) if dv else None
    # pre-entry momentum & vol (T-60 .. T-30, before entry)
    i60 = idx(px, (d0 - dt.timedelta(days=60)).isoformat())
    premom = ret(px, i60, ei) if i60 is not None else None
    prevol = (st.pstdev(series_ret(px, i60, ei)) if (i60 is not None and ei-i60 > 3) else None)
    # regime at entry
    xi = idx(XBI, tr['entry_date'])
    xbi_ma200 = None; xbi_63 = None
    if xi is not None and xi >= 200:
        ma = st.mean([x for x in XBI['adj'][xi-200:xi] if x])
        xbi_ma200 = 1 if (XBI['adj'][xi] and XBI['adj'][xi] > ma) else 0
    if xi is not None and xi >= 63:
        xbi_63 = ret(XBI, xi-63, xi)
    vi = idx(VIX, tr['entry_date']); vix = VIX['adj'][vi] if vi is not None else None
    ti = idx(TNX, tr['entry_date']); tnx = TNX['adj'][ti] if ti is not None else None
    tnx_63 = ret(TNX, ti-63, ti) if (ti is not None and ti >= 63) else None
    return {
        'ticker': ev['ticker'], 'pdufa_date': ev['pdufa_date'], 'outcome': ev.get('outcome',''),
        'confidence': ev.get('confidence',''), 'cohort': ev.get('_cohort',''),
        'year': ev['pdufa_date'][:4],
        'entry_date': tr['entry_date'], 'exit_date': tr['exit_date'],
        'entry_px': round(tr['entry_px'],4), 'ret': round(tr['ret'],6),
        'excess': round(excess,6) if excess is not None else '',
        'beat_xbi': (1 if (excess is not None and excess > 0) else 0) if excess is not None else '',
        'mae': round(tr['mae'],6) if tr['mae'] is not None else '',
        'adv_usd': round(advol,0) if advol else '',
        'premom_60_30': round(premom,6) if premom is not None else '',
        'prevol_60_30': round(prevol,6) if prevol is not None else '',
        'xbi_above_200d': xbi_ma200 if xbi_ma200 is not None else '',
        'xbi_ret_63d': round(xbi_63,6) if xbi_63 is not None else '',
        'vix': round(vix,2) if vix else '', 'tnx': round(tnx,3) if tnx else '',
        'tnx_chg_63d': round(tnx_63,4) if tnx_63 is not None else '',
    }

def load(fp, cohort):
    rows = list(csv.DictReader(open(fp)))
    for r in rows: r['_cohort'] = cohort
    return rows

def split(r):
    if r['cohort'] == 'P':
        return 'IS' if r['year'] == '2025' else ('OOS' if r['year'] == '2026' else 'other')
    if r['cohort'] == 'regime2223':
        return 'OOS_regime'
    return 'orig'

if __name__ == '__main__':
    evs = (load('data/events_pdufa_bio.csv', 'P')
           + load('data/events_regime_2022_2023.csv', 'regime2223'))
    rows = []
    for e in evs:
        fr = feat_row(e)
        if fr:
            fr['split'] = split(fr)
            rows.append(fr)
    cols = list(rows[0].keys())
    with open('data/features.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    from collections import Counter
    print(f"features: {len(rows)} events -> data/features.csv")
    print("by cohort:", dict(Counter(r['cohort'] for r in rows)))
    print("by split :", dict(Counter(r['split'] for r in rows)))
    print("with excess:", sum(1 for r in rows if r['excess'] != ''))
    print("with adv_usd:", sum(1 for r in rows if r['adv_usd'] != ''))
    print("with regime:", sum(1 for r in rows if r['xbi_above_200d'] != ''))
