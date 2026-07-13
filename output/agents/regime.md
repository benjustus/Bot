# Research Stream 3 — Market Regime: is pre-PDUFA XBI-excess exploitable in any regime?

**Metric:** `excess` = raw return − XBI over the identical T-30→T-7 window.
**Universe:** tradeable (entry_px≥2 AND marketCap≥100e6); full-set shown as sensitivity.
**Splits:** IS = 2025 (n=257 tradeable). Hold-outs: OOS = 2026 (n=122), OOS_regime = 2022-23 (n=13).
**Stance:** refute. Report an edge only if positive+significant in-sample AND it survives a hold-out.

## Headline verdict

**NO regime shows positive, significant XBI-excess that survives the hold-out.** The unconditional
excess is not significant in any split (IS +1.15%, t=1.47, sign-p=0.53; boot CI includes 0), so the
regime splits are slicing a fundamentally ~zero-mean, noisy distribution. Where in-sample regimes
*look* positive, they are (a) mutually collinear, (b) partly outcome-mix confounded, and (c) either
untestable or sign-flipping in the hold-outs.

## What looked positive in-sample (2025)

Three regimes had bootstrap 95% CI above 0 — but they are ~the **same bet** ("weak XBI tape"):
corr(below-200d, neg-momentum)=**0.80**, corr(below-200d, rising-rates)=0.54.

| IS regime (tradeable) | n | mean | t | boot95 | sign-p |
|---|---|---|---|---|---|
| xbi_above_200d==0 (below 200d MA) | 156 | +2.71% | +2.76 | [+0.77,+4.62] | 0.092 |
| xbi_mom_63d<0 (neg 3-mo momentum) | 133 | +2.24% | +2.15 | [+0.19,+4.24] | 0.118 |
| rates_rising (tnx_chg>0) | 87 | +3.29% | +2.46 | [+0.71,+5.94] | **0.031** |

Mirror image (also in-sample): when XBI is **strong** the trade is flat-to-negative —
xbi_above_200d==1: mean −1.27%, median −3.07%, hit 33.7%, sign-p=0.001; xbi_mom_63d>0: median −2.04%, sign-p=0.009.
VIX buckets and tnx-level splits show nothing (all boot CIs span 0; IS has no tnx<3 rows and VIX is ~all 15-25).

## Why none of it is an exploitable edge

1. **Untestable in the 2026 hold-out.** 2026 is a single tape: *all 122* names are above-200d with
   ~all positive momentum. The below-200d / neg-momentum edge cannot be validated there at all.
2. **Sign flips in the 2022-23 hold-out (the only genuinely different tape).**
   Below-200d, tradeable n=9: **−4.6%** (wrong sign). Neg-momentum: 2026 n=5 → **−10.0%**; 2022-23 n=9 → **−4.6%**.
   Full-set 2022-23 below-200d is +3.65% but insignificant (boot CI [−1.3,+8.7], sign-p=0.69) and the
   tradeable subset is negative — i.e. noise, not signal.
3. **rates_rising** is the only IS regime significant on both boot and sign tests, but it is the **most
   outcome-mix confounded** (83.9% approvals in-regime vs 71.2% out; outcome is unknown at entry, so that
   part isn't tradeable). In OOS 2026 it keeps a positive sign but loses significance (+1.33%, boot CI
   [−1.5,+4.4]); in tradeable 2022-23 it flips negative.
4. **Multiple testing.** ~11 splits tested on IS; ~0.5–1 false positive expected at p<0.05. The positives
   are collinear (≈1 independent hypothesis) and none replicate.

## Regime ranking (by hold-out robustness, best→worst)

1. **rates_rising** — positive sign in IS + OOS, but never significant OOS and outcome-mix confounded. Not an edge.
2. **below-200d / neg-momentum (weak tape)** — strongest in-sample, but untestable in 2026 and sign-flips negative in 2022-23. Not an edge.
3. **VIX buckets, tnx-level, XBI uptrend** — no positive significant excess anywhere.

**Bottom line:** the "regime edge" appears only in-sample (2025) and vanishes or reverses out-of-sample.
Treat it as a single-tape / multiple-testing artifact. Full per-regime stats (IS + both hold-outs, tradeable and full-set) in `output/agents/regime.json`.
