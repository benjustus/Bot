# Research Stream "Combinations" — feature-combo alpha search

**Question.** Does ANY 2-, 3- or 4-way AND-combination of pre-entry features define a
subset of PDUFA events with *reproducible* alpha vs XBI (metric = `excess`, XBI-adjusted
T-30→T-7), after multiple-testing correction and out-of-sample hold-out?

## Verdict: **NO.**
After Benjamini-Hochberg FDR correction across the whole family, **0 combinations pass**,
and therefore **0 survive** the hold-out. The strongest in-sample winners are a single
regime artifact that is untestable or fails forward.

## Method
- **Universe (primary):** tradeable = `entry_px>=2 AND marketCap>=100e6`. `excess` winsorized
  1%/99% per split. IS n=257, OOS-2026 n=128, OOS-regime(2022-23) n=32 (tradeable).
- **Predicates:** 13 numeric features binarized hi/lo at their **IS-tradeable median**
  (rs_21, rs_63, rs_126, mom_126, premom_60_30, beta_xbi, atr14, dnvol_60, prevol_60_30,
  adv_usd, prior_fda_approvals, marketCap, vix) + `xbi_above_200d` (both directions) +
  `review_priority==PRIORITY`. = **15 base features / 29 directional predicates.**
- Enumerated **all** 2/3/4-way AND-combos (≤1 predicate per feature): 22,596 formed;
  **10,054 tested** with n≥15 on IS (= multiple-testing denominator N).
- BH-FDR q=0.05 across the family; then validate each candidate on OOS-2026 and OOS-regime.

## Results
| Quantity | Value |
|---|---|
| Combinations tested (BH denominator N) | **10,054** |
| Raw-significant (p<0.05) | **1,202** |
| Expected by chance (0.05·N, global null) | ~503 |
| Raw-significant AND positive | 841 (collapse to 312 independent clusters) |
| **Passing BH-FDR (q=0.05)** | **0** |
| BH rank-1 hurdle q/N | 5.0e-6 |
| Smallest observed p | 7.25e-5 (≈15× too large) |
| **Survivors (BH-pass AND hold-out excess>0, n≥10)** | **0** |

**Why 1,202 > 503 is not evidence.** The one-sample test is vs 0, but the tradeable
universe already drifts **+1.22% (t=1.66)** in-sample, so many subsets clear p<0.05 by
inheriting baseline drift, not by adding alpha. All 841 positive hits "beat" only zero,
none is a clean excess-over-baseline signal. Crucially, BH-FDR — which scales the bar to the
family size — rejects **every** one: the empirical p-curve sits above the BH line at every
rank (r20: p=6.2e-4 vs line 9.9e-5; r100: p=2.7e-3 vs 5.0e-4). Per-combo n≈15-25 caps
achievable significance, so no combo can clear the corrected threshold.

## Closest miss (and why it fails)
The top in-sample cluster is **"low RS + low momentum + high beta, while XBI < 200-day MA"**
— e.g. `rs_63_lo + mom_126_lo + beta_xbi_hi + xbi_above_200d_no`: IS n=21, **mean +10.3%,
t=+4.87, p=9e-5, hit 95%**. Spectacular in-sample. But:
- It is **regime-locked**: every top combo requires `xbi_above_200d_no`. In **OOS-2026 all
  128 events had XBI above its 200-day MA**, so these combos select **0 events forward** —
  literally untestable on the primary hold-out.
- On the **2022-23 regime hold-out** (where XBI was below its 200d MA) the same combos shrink
  to **n=2-3** and go flat/negative (mean −1.5% / +1.4%, t≈0). No reproducible edge.

This is exactly the failure the brief anticipated: searching ~10k combinations throws up
correlated in-sample winners by chance, and the biggest one here is a market-regime proxy,
not a tradeable PDUFA edge.

## Generalization & sensitivity
- Of 841 in-sample winners, only 328 are even testable on OOS-2026 (the rest are
  regime-locked); 88% stay nominally positive — but OOS-2026 baseline is already +0.55% and
  none is statistically significant, so this reflects mild positive drift, not combo alpha.
  On the regime hold-out only 3 are testable and **0/3** stay positive.
- **Full-universe sensitivity** (no tradeability screen): 10,801 tested, 706 raw-sig,
  **BH kmax=0** — identical verdict.

## Bottom line
No 2-, 3-, or 4-way feature combination defines a subset with reproducible alpha vs XBI.
The in-sample "winners" are (a) inflated by a mildly positive universe baseline and (b)
dominated by a single XBI-downtrend regime cluster that either cannot be tested or reverses
out-of-sample. After correction and hold-out: **nothing survives.**
