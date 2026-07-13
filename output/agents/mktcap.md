# Research Stream 1 — Market-Cap Buckets: Pre-PDUFA Alpha vs XBI

**Mandate:** refute exploitable XBI-*excess* alpha in any market-cap bucket. Judge on **excess** (ret − XBI, T‑30→T‑7), report raw too. Discovery on IS (2025) first; confirm on OOS (2026) and OOS_regime (2022‑23) without tuning.

**Data notes / caveats**
- `marketCap` is the **current** value — a coarse proxy for size *at the PDUFA date*. Bucketing error is unavoidable.
- IS (n=303) and OOS (n=128) have **full** marketcap coverage. OOS_regime (n=32) has only **13/32** mapped (old 2022‑23 names absent from the current-universe file), so the regime check is **partial/inconclusive** by bucket.
- Buckets are the 7 user-specified USD ranges. `n/a` (no mcap) is reported but not judged.

## Headline verdict

**NO market-cap bucket shows XBI-excess with a genuine t>2 in-sample that ALSO stays positive on the hold-out and is not outlier-driven.** Market cap does **not** reveal exploitable alpha.

- Only **one** bucket even approaches significance in-sample (**300–500M**, naive t=2.00). It is *not* outlier-driven — but it is **not truly significant** (correct small-sample t‑p=0.069, fails BH and Bonferroni) and it **flips sharply negative out-of-sample** (OOS −7.6%, PF 0.23). Refuted.
- The large-cap control (**>5B**, n=177) is **flat (~0)** in and out of sample — exactly what market efficiency predicts, and a clean sanity check that the pipeline isn't manufacturing signal.

## In-sample (2025) — EXCESS by bucket

| bucket | n | raw mean | exc mean | exc median | mean−med gap | hit | Sharpe/tr | PF | t | t‑p(df) | boot 95% CI | MaxDD |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| <100M | 30 | +1.93% | +0.56% | −2.97% | **+3.53%** | 47% | 0.01 | 1.04 | 0.08 | 0.940 | [−13.0,+15.2]% | −97% |
| 100–300M | 24 | +8.02% | +6.66% | +2.98% | +3.69% | 58% | 0.19 | 2.03 | 0.91 | 0.374 | [−5.1,+22.5]% | −55% |
| **300–500M** | **13** | +17.25% | **+11.89%** | +16.22% | −4.33% | 62% | 0.55 | 3.71 | **2.00** | **0.069** | **[+0.55,+23.0]%** | −31% |
| 500M–1B | 11 | +5.40% | +5.01% | −0.94% | +5.95% | 45% | 0.22 | 1.97 | 0.74 | 0.474 | [−6.7,+18.4]% | −33% |
| 1–2B | 23 | +0.77% | −1.32% | −0.54% | −0.78% | 48% | −0.07 | 0.80 | −0.35 | 0.731 | [−8.9,+5.5]% | −65% |
| 2–5B | 25 | +3.73% | +0.23% | +0.68% | −0.46% | 56% | 0.02 | 1.05 | 0.09 | 0.927 | [−4.5,+5.0]% | −56% |
| >5B (control) | 177 | +3.15% | +0.17% | −1.13% | +1.30% | 44% | 0.02 | 1.05 | 0.26 | 0.797 | [−1.1,+1.5]% | −94% |

*t‑p uses the correct Student‑t (df=n−1), which is why 300–500M's naive t=2.00 maps to p=0.069, not <0.05.*

## Clean-version checks (outlier robustness, IS)

| bucket | raw exc mean (t) | winsor 1/99 (t) | screen px<2 & adv<1e6 (n, mean, t) |
|---|--:|--:|--:|
| <100M | +0.56% (0.08) | −0.13% (−0.02) | 24: **−6.11%** (−0.75) |
| 100–300M | +6.66% (0.91) | +3.00% (0.67) | 21: +2.31% (0.62) |
| **300–500M** | +11.89% (2.00) | **+11.89% (2.00)** | 12: **+13.70% (2.22)** |
| 500M–1B | +5.01% (0.74) | +5.01% (0.74) | 11: +5.01% (0.74) |
| 2–5B | +0.23% (0.09) | +0.23% (0.09) | 25: +0.23% (0.09) |
| >5B | +0.17% (0.26) | +0.17% (0.26) | 177: +0.17% (0.26) |

**Outlier read‑out:**
- **<100M is a false-positive trap.** Raw mean is positive but **median is −2.97%** (mean−median gap +3.5pp) and hit-rate <50%. It is propped by **RNAZ +122%** (a reverse-split artifact at split-adjusted px≈$101 — importantly **NOT caught** by the `px<2` screen, only by winsorization) plus illiquid ~$1 names (PHIO, ESLA). After the liquidity screen it is **−6.11%**. No edge; actively dangerous.
- **100–300M** is winsor-sensitive (+6.66%→+3.00% once ADCT's +154% at px=1.32 is clipped) — suggestive at best, never significant.
- **300–500M is genuinely NOT outlier-driven** (median +16.2% ≥ mean +11.9%; unchanged by winsor; +13.7%/t=2.22 after screen). Its problem is small n and the hold-out, not outliers.

## Hold-out — OOS 2026 (EXCESS)

| bucket | n | exc mean | exc median | hit | t | PF | boot 95% CI |
|---|--:|--:|--:|--:|--:|--:|--:|
| <100M | 4 | −5.53% | −8.20% | 25% | −1.15 | 0.25 | [−12.7,+2.6]% |
| 100–300M | 10 | +8.95% | +0.25% | 50% | 0.77 | 2.37 | [−11.4,+32.2]% |
| **300–500M** | 5 | **−7.57%** | −11.89% | 40% | −1.34 | 0.23 | [−17.3,+2.4]% |
| 500M–1B | 13 | −3.42% | +4.04% | 62% | −0.58 | 0.63 | [−15.4,+6.6]% |
| 1–2B | 6 | +5.59% | +10.12% | 83% | 0.86 | 2.42 | [−6.9,+15.2]% |
| 2–5B | 11 | +4.85% | +4.46% | 73% | 1.63 | 3.16 | [−0.8,+10.3]% |
| >5B | 79 | −0.60% | +0.15% | 52% | −0.57 | 0.84 | [−2.6,+1.5]% |

- **300–500M (the only IS candidate) FAILS the hold-out decisively** — it becomes one of the *worst* buckets OOS (−7.6%, PF 0.23), dragged by VNDA 2026 events (−18%/−19%).
- **2–5B** looks nice OOS (+4.85%, t=1.63) but was **flat in-sample** (t=0.09) — claiming it would be tuning on the hold-out, which the mandate forbids.
- OOS_regime (partial): no bucket has enough mapped names to confirm anything (300–500M has n=0).

## Multiple testing (IS excess, 7 buckets)

7 buckets × 2 metrics = up to 14 tests → ~0.7 "significant" cells expected by chance at α=0.05. Benjamini–Hochberg and Bonferroni (α=0.0071) on the excess t‑p values: **the smallest p is 300–500M at 0.069, which fails BH (crit 0.0071) and Bonferroni**. No bucket survives correction. The lone near-hit is exactly the ~1 marginal cell chance predicts.

## Bucket ranking by IS excess significance (t‑stat)

1. **300–500M** t=+2.00 (p=0.069) — *not outlier-driven, but not significant after correction and flips −7.6% OOS* → **refuted**
2. 100–300M t=+0.91 — positive both samples (+6.7%/+9.0%) but never significant, winsor-sensitive
3. 500M–1B t=+0.74 — negative OOS (−3.4%)
4. >5B t=+0.26 — flat control, ~0 both samples
5. 2–5B t=+0.09 — flat IS; OOS strength can't be claimed
6. <100M t=+0.08 — negative median, −6.1% after clean; nano trap
7. 1–2B t=−0.35 — negative IS

**Conclusion:** No bucket clears the bar of (t>2 IS) ∧ (survives hold-out positive) ∧ (not outlier-driven). Market cap does **not** expose exploitable pre-PDUFA alpha vs XBI. The one in-sample flag (300–500M) is a small-n, multiple-comparison artifact that reverses out-of-sample.
