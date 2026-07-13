# Research Stream 5 — Machine Learning (skeptical / refutation)

**Question:** Can a model using ONLY pre-entry (T-30) information select pre-PDUFA trades that
beat XBI out-of-sample, after costs?

## VERDICT: NO (null result). Refuted.
No model produces a statistically or economically reliable selection of 2026 trades that beats XBI
after 1% round-trip cost. Tree models overfit catastrophically (in-sample AUC up to 0.93 → below-chance
0.43–0.46 out-of-sample). A linear model shows a whiff of above-chance ranking (OOS AUC 0.607) but it is
**not significant (permutation p = 0.095)**, is driven by macro/calendar regime differences rather than
firm-level skill, is **not corroborated by the other 4 models** (which rank 2026 trades at-chance or
backwards), and **vanishes after costs**.

## 1. Out-of-sample discrimination (train 2025 → test 2026)
| model | OOS AUC 2026 | in-sample AUC | walk-fwd AUC | regime 22-23 AUC | acc@0.5 |
|---|---|---|---|---|---|
| logistic | **0.607** | 0.721 | 0.582 | 0.571 | 0.586 |
| random_forest | 0.453 | 0.808 | 0.514 | 0.377 | 0.484 |
| gradient_boost | 0.458 | 0.896 | 0.513 | 0.607 | 0.539 |
| xgboost | 0.456 | 0.880 | 0.541 | 0.448 | 0.547 |
| lightgbm | 0.429 | 0.926 | 0.535 | 0.421 | 0.508 |

Base rate (always-trade beats XBI): IS 47.5%, OOS-2026 54.7%. Only logistic clears 0.5 OOS, and only
marginally. The 4 tree models have huge in-sample AUC that collapses **below 0.5** OOS — textbook
overfit/anti-generalization, the expected outcome for flexible learners on this sample size.

## 2. ECONOMIC test on 2026 (the one that matters)
Baseline: full 2026 set = **+0.19% gross / −0.81% net** mean excess; "take none" = 0.00%. Because the
full set loses to XBI after costs, a selector must average **>1% gross** just to beat doing nothing.

**Pre-specified, threshold-free rule (trade top-half by predicted prob), net of 1% round-trip:**
| model | gross % | net % | SE % | t-stat (gross vs 0) |
|---|---|---|---|---|
| logistic | +1.32 | +0.32 | 2.29 | +0.58 |
| random_forest | +0.93 | −0.07 | 2.32 | +0.40 |
| gradient_boost | −1.03 | −2.03 | 1.89 | −0.55 |
| xgboost | −0.56 | −1.56 | 1.85 | −0.30 |
| lightgbm | −1.86 | −2.86 | 1.78 | −1.05 |
| **ensemble (avg prob)** | +0.83 | **−0.17** | 2.31 | +0.36 |
| full set (reference) | +0.19 | −0.81 | 1.34 | — |

Every model's selected-basket gross excess is **within ~1 SE of zero** (|t| ≤ 1.05); none is
distinguishable from chance. Net of cost, only logistic is marginally positive (+0.32%) — well inside
noise — and the 5-model average net is −1.24%. Rank correlation between predicted prob and realized 2026
excess (Spearman): logistic +0.145, RF −0.01, GB −0.03, XGB −0.02, LGBM −0.08 — i.e. 4 of 5 models rank
trades **at-chance or backwards** out-of-sample.

**Mirage warning:** a naive tuned-threshold rule (threshold fit on 2025) showed RF +2.54% and logistic
+1.19% net. Those are small-n artifacts (10–49 trades): RF's "profit" comes from a model with
below-chance AUC (0.453) and zero rank-correlation. Under the pre-specified top-half rule with proper
SEs, nothing survives. This is exactly the trap a skeptical desk must reject.

## 3. Leakage / overfitting guards
- **Label-shuffle (20 perms):** shuffling the target collapses logistic OOS AUC 0.607 → 0.494, confirming
  the edge is label-dependent, not look-ahead leakage. Trees' shuffled null sits ~0.52–0.53 (small-sample
  noise) while their real AUC (0.43–0.46) is *below* their own null — negative real skill, no leakage.
- **Permutation p-value (logistic OOS AUC):** 0.095 — not significant at 5%.
- Walk-forward expanding-window CV (train strictly before each fold's earliest pdufa_date; never shuffle
  across time) agrees with the clean 2025→2026 split: logistic ~0.58, trees ~0.51–0.54.

## 4. Feature importance
Logistic coefficients are dominated by **calendar/macro**: quarter (−0.80), xbi_above_200d (−0.64),
xbi_ret_63d (+0.53), tnx (−0.51). Note `xbi_above_200d` is **constant (=1) across all of 2026**, so it adds
zero within-2026 discrimination — it only shifts the intercept. The linear "signal" is largely the model
detecting that 2026 is a different macro regime than 2025 on average, **not** skill at ranking individual
names. Firm-level features (mktcap, adv, float, entry_px, premom) carry small, unstable weights and the
tree models place most importance on the same low-signal firm/macro variables while overfitting their noise.

## 5. Effective sample size — why ML power is limited here
- n_train = 303 events (2025) but only **165 unique PDUFA dates** and ~129 unique macro vectors; n_test =
  128 (2026) / **76 unique dates**. Macro features (vix, tnx, xbi_*) are shared across clustered dates →
  **pseudo-replication**: the effective number of independent observations for any macro-driven signal is
  closer to ~76–165, far below the nominal row count.
- Labels are ~50/50, so there is no class-imbalance lever; a coin-flip already "beats XBI" 54.7% of 2026.
- ~14 features against a few-hundred effective samples with a near-50/50 target is a small-data regime:
  flexible models overfit (seen directly: IS AUC → OOS < 0.5), and even a regularized linear model cannot
  push its edge to significance (p = 0.095). This is *why* ML cannot establish an out-of-sample edge here,
  and why a positive in-sample AUC is not evidence of a tradeable signal.

## Bottom line
Trying to REFUTE, we could not reject the null. No model — linear, RF, GBM, XGBoost, or LightGBM, nor
their ensemble — selects pre-PDUFA trades that beat XBI out-of-sample after 0.5%/side costs. The closest
any model came was logistic at +0.32% net on its top-half basket (t≈0.6, indistinguishable from zero),
against a full-set baseline that itself loses 0.81% net to XBI.
