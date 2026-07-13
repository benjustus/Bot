#!/usr/bin/env python3
"""Monte-Carlo roll-over simulation (Stream 11).

Bootstraps >=100k roll-over paths from a pool of realised trade returns and
reports P(profit), ruin probability, expected value, CVaR and drawdown, for
all-in vs fixed-fraction position sizing. All-in is the user's original design;
fixed-fraction shows how sizing controls the ruin tail.

Bootstrap-with-replacement of K draws per path is the standard MC; it slightly
overstates the opportunity to diversify vs the real non-overlapping constraint,
which we note. Returns are RAW (what actually hits the account); XBI buy-and-hold
over the same span (+76.5%) is the external benchmark to beat.
"""
import sys, csv, random, statistics as st
sys.path.insert(0, 'src')
import backtest as bt, analyze as az

def pool_returns(subset='tradeable', eo=30, xo=7):
    evs = list(csv.DictReader(open('data/events_pdufa_bio.csv')))
    tr, _ = bt.run_variant(evs, eo, xo); az.enrich(tr)
    if subset == 'tradeable':
        tr = [t for t in tr if t['tradeable']]
    return [t['ret'] for t in tr], [t['excess'] for t in tr if t['excess'] is not None]

def simulate(returns, paths=100000, k=22, start=1500.0, fee=2.0, tax_rate=0.26375,
             sizing='allin', frac=0.05, seed=7):
    random.seed(seed)
    n = len(returns)
    ends, dds, rets = [], [], []
    for _ in range(paths):
        cap = start; peak = start; mdd = 0.0; loss_pot = 0.0
        for _ in range(k):
            r = returns[random.randrange(n)]
            stake = cap if sizing == 'allin' else cap * frac
            pl = stake * r - fee
            tax = 0.0
            if pl > 0:
                off = min(loss_pot, pl); loss_pot -= off; tax = (pl - off) * tax_rate
            else:
                loss_pot += -pl
            cap = cap + pl - tax
            if cap <= 0:
                cap = 0.0
            peak = max(peak, cap); mdd = min(mdd, cap / peak - 1 if peak > 0 else 0)
        ends.append(cap); dds.append(mdd); rets.append(cap / start - 1)
    ends.sort()
    m = len(ends)
    cvar5 = sum(ends[:int(0.05 * m)]) / int(0.05 * m)
    return {
        'sizing': sizing, 'k': k, 'paths': paths,
        'ev_end': sum(ends) / m, 'median_end': ends[m // 2],
        'p_profit': sum(1 for e in ends if e > start) / m,
        'p_loss': sum(1 for e in ends if e < start) / m,
        'p_down50': sum(1 for e in ends if e < start * 0.5) / m,
        'p_down80': sum(1 for e in ends if e < start * 0.2) / m,
        'cvar5_end': cvar5, 'p5_end': ends[int(0.05 * m)], 'p95_end': ends[int(0.95 * m)],
        'worst_end': ends[0], 'best_end': ends[-1],
        'median_maxdd': sorted(dds)[m // 2], 'p95_maxdd': sorted(dds)[int(0.95 * m)],
    }

def show(r):
    print(f"  [{r['sizing']:5}] EV=€{r['ev_end']:.0f} median=€{r['median_end']:.0f} "
          f"P(profit)={r['p_profit']*100:.0f}% P(loss)={r['p_loss']*100:.0f}% "
          f"P(<-50%)={r['p_down50']*100:.1f}% P(<-80%)={r['p_down80']*100:.2f}% "
          f"CVaR5=€{r['cvar5_end']:.0f} [p5 €{r['p5_end']:.0f}, p95 €{r['p95_end']:.0f}] "
          f"medMaxDD={r['median_maxdd']*100:.0f}% p95MaxDD={r['p95_maxdd']*100:.0f}%")

if __name__ == '__main__':
    import json
    rets, exc = pool_returns('tradeable')
    print(f"pool: {len(rets)} tradeable trades, mean raw {st.mean(rets)*100:+.2f}%, "
          f"mean excess {st.mean(exc)*100:+.2f}%, std {st.pstdev(rets)*100:.1f}%")
    out = {}
    print("Monte-Carlo, 100k paths, K=22 roll-over trades, start €1500, 2€/trade, German tax:")
    for sizing in ['allin', 'frac']:
        r = simulate(rets, paths=100000, sizing=sizing)
        show(r); out[sizing] = r
    # benchmark note
    out['benchmark_note'] = 'XBI buy-and-hold over the cohort span (Dec-2024..Jun-2026) = +76.5%, maxDD -26%'
    json.dump(out, open('output/agents/montecarlo.json', 'w'), indent=2)
    print("wrote output/agents/montecarlo.json")
