# Research Stream: Clustering — do PDUFA events form clusters with durable OOS alpha vs XBI?

**Verdict: NO.** No well-separated cluster carries durable positive out-of-sample alpha. The clusters that look best in-sample are either (a) a macro/regime artifact that *reverses* out-of-sample, or (b) a positive-skew small-cap-volatility bucket whose mean survives the benign 2026 tape but *inverts* in the 2022-23 bear regime. Weak cluster separation and poor cross-algorithm membership stability confirm these are not robust, delimited clusters.

## Setup
- Tradeable universe (entry_px>=2 & marketCap>=100e6): **IS(2025)=257, OOS(2026)=122, OOS_regime(2022-23)=13**.
- 15 point-in-time features; median-imputed (IS) + StandardScaler **fit on IS only**; features transformed for OOS/regime with the IS-fit pipeline.
- `excess` (XBI-adjusted return) winsorized at IS 1/99 = [-27.2%, +41.2%]; it is the metric, never a clustering input.
- Clustering: KMeans k=3..8 (+ GaussianMixture, Agglomerative for robustness). Significance = bootstrap 95% CI lower bound > 0 (n>=8).

## Cluster separation is weak (no clearly-delimited clusters)
Silhouette by k (IS): k=3:0.223, k=4:0.171, k=5:0.169, k=6:0.154, k=7:0.163, k=8:0.156
- Max silhouette = **0.223 at k=3** — that is weak structure; the feature space is a continuum, not discrete blobs. Chosen **k=3**.

## Chosen partition: KMeans k=3
| cluster (named by defining z-features) | n_IS | IS mean | IS t | IS boot95 CI | IS-sig+? | OOS n | OOS mean | REG n | REG mean |
|---|---|---|---|---|---|---|---|---|---|
| c0: hi-log_mcap / lo-atr14 / lo-dnvol_60 | 158 | +0.20% | +0.32 | [-1.02, +1.45] | False | 76 | -0.11% | 5 | -0.99% |
| c1: hi-mom_126 / hi-rs_126 / hi-rs_63 | 21 | +1.53% | +0.37 | [-6.22, +9.64] | False | 8 | -2.21% | 1 | -5.86% |
| c2: lo-log_mcap / hi-dnvol_60 / hi-beta_xbi | 78 | +3.20% | +1.85 | [-0.08, +6.59] | False | 38 | +3.08% | 7 | -4.60% |

**Best IS cluster = c2 "lo-log_mcap / hi-dnvol_60 / hi-beta_xbi"** (small, volatile, high-beta biotech): IS mean +3.20% (t=+1.85, median +1.19%, hit 54%). OOS-2026 **+3.08%** (holds up), but OOS_regime 2022-23 **-4.60%** (collapses). Note it is **not** IS-significant (CI includes 0).

## The decisive hold-out scan: 8 IS-significant clusters, 0 durable
Across k=3..8 (33 KMeans clusters; ~1.65 false positives expected at 0.05), **8** clusters were IS-significant-positive. These are not 8 independent findings — they are re-discoveries of ~2 recurring motifs at different k. Their out-of-sample fate:

| k | cluster | IS mean (t) | OOS-2026 | OOS_regime 22-23 | motif |
|---|---|---|---|---|---|
| 4 | c0 | +1.50% (+1.98) | -3.81% | -20.13% | MACRO (hi-tnx/lo-xbi_ret) |
| 4 | c3 | +4.15% (+2.14) | +3.78% | -4.38% | VOL small-cap (hi-dnvol/atr/beta) |
| 5 | c0 | +1.64% (+2.12) | -4.02% | -20.13% | MACRO (hi-tnx/lo-xbi_ret) |
| 6 | c3 | +8.27% (+2.00) | +6.07% | n/a (n=0) | VOL small-cap (hi-dnvol/atr/beta) |
| 6 | c4 | +3.73% (+2.36) | -1.45% | -12.08% | MACRO (hi-tnx/lo-xbi_ret) |
| 7 | c2 | +3.98% (+2.66) | +2.21% | -12.08% | MACRO (hi-tnx/lo-xbi_ret) |
| 8 | c0 | +8.28% (+2.06) | +5.98% | n/a (n=0) | VOL small-cap (hi-dnvol/atr/beta) |
| 8 | c7 | +2.93% (+1.94) | -1.47% | -12.08% | MACRO (hi-tnx/lo-xbi_ret) |

- **4/8** stay positive in OOS-2026 (≈ coin-flip), and **0/8** stay positive across BOTH holdouts.
- **MACRO motif** (enter after XBI weakness, high rates): IS-positive but OOS-2026 *negative* and 2022-23 *catastrophic* (-12% to -20%). A pure 2025-regime artifact.
- **VOL small-cap motif** (high dollar-volume turnover, high ATR/pre-vol, low mcap, high beta): IS-positive AND OOS-2026-positive, but **negative in every 2022-23 regime cell where data exists** (e.g. k=4 c3: -4.38%). The highest-mean versions (k=6/8, n=14-17) have zero regime events, so cannot be validated, and n=14-17 with 6+ separating features is overfit. Its mean sits well above its median (k=3 c2: +3.20% mean vs +1.19% median) — a lottery/right-skew property of volatile small caps, not harvestable alpha; it reverses precisely in the bear regime where you'd need it.

## Stability & robustness
- KMeans across 10 seeds: ARI mean **0.99** (trivially stable — same algorithm).
- KMeans vs GaussianMixture ARI **0.27**, vs Agglomerative ARI **0.64** — the *same events do not reliably co-cluster across algorithms*; the partition is method-dependent.
- GMM and Agglomerative reproduce the SAME two motifs and the SAME failure: their small-cap/high-vol cluster is IS-positive (GMM +3.22%, Agglo +2.94%) and OOS-2026-positive-ish (+1.23%, +1.80%) but negative in 2022-23 (-7.42%, -3.88%); their macro cluster fails both holdouts.

## Multiple-testing note
- 33 KMeans clusters x 3 algorithms were screened; ~0.05x(clusters) false positives are expected purely by chance. 8 IS-hits > 1.65 expected reflects non-independent nested clusters plus outcome right-skew, not durable signal — confirmed by the 0/8 both-holdout survival.

## Bottom line
Any partition of a ~zero-mean, right-skewed noisy variable yields high-mean clusters in-sample; here they do not replicate. No well-separated cluster shows durable positive OOS alpha. The refutation stands: at best silhouette k=3, the top cluster is not IS-significant and reverses in-regime; the IS-significant clusters at higher k fail at least one hold-out, and none survive both OOS-2026 and OOS_regime 2022-23.
