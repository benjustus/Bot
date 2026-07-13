# Research Stream 4 — Liquidity & Data Artifacts

**Question:** Is the pre-PDUFA excess concentrated in small/illiquid names *real
exploitable alpha*, or an illusion from (a) data artifacts and (b) bid-ask
spreads you cannot cross?

**VERDICT: Not real tradeable alpha.** The gross "micro-cap edge" is roughly
one-third data artifacts / untradeable tail prints and two-thirds uncrossable
spread + capacity. After removing artifacts, winsorizing 1/99, and charging
realistic spreads, the lowest-liquidity bucket collapses from **+7.1% to +0.4%
mean / −2.4% median (t = 0.15)** — statistically and economically zero. Metric =
`excess` (XBI-adjusted adjclose return, T-30 → T-7). IS = 2025 (303 ev),
OOS = 2026 (128 ev).

---

## 1. Liquidity buckets — the edge is real *in gross terms* and mean-driven

**IS — excess by point-in-time ADV ($) quartile** (edges $3.9M / $37.5M / $235M):

| bucket | n | mean | median | hit | t | boot95 |
|---|--:|--:|--:|--:|--:|---|
| Q1 low ADV | 75 | **+7.13%** | +2.84% | 56% | +1.95 | [+0.4, +14.7] |
| Q2 | 76 | +0.72% | +1.87% | 54% | +0.38 | [−3.0, +4.2] |
| Q3 | 76 | −1.07% | −1.06% | 45% | −0.70 | [−4.4, +1.6] |
| Q4 high ADV | 76 | −1.54% | −2.86% | 36% | −1.95 | [−3.1, +0.0] |

Excess rises **monotonically as liquidity falls**, but it is **mean-driven**:
Q1 median (+2.8%) is < half the mean (+7.1%), and Q1 is the *only* positive
quartile — with a bootstrap CI whose lower bound (+0.4%) already sits on zero.

**IS — by entry price:** `<$2` mean +6.98% but **median −0.54%** (pure tail);
`$2-5` mean +8.98% / median +7.93% / t=2.11 (the one robust-looking cell — see §4);
`$5-20` +2.35%; `>$20` −0.94%. **IS — by float (shares):** smallest float
(`<10M`, n=13) mean −0.82% / **median −8.20%** — the tiniest names *lose* at the
median; the signal peaks in the `50-200M` mid-float tier (+4.17%, t=2.04), not the
smallest.

**Concentration:** in Q1, the top 3 names (ADCT +154%, RNAZ +122%, PHIO +73%)
supply **65% of the bucket's summed excess** and 34% of all positive excess —
3 of 75 events carry the result.

---

## 2. Artifact detection — 24 flagged events; removing them kills significance

Scanned each event's T-35→T-3 window for: single-day adjclose ratio >1.5×/<0.67×,
raw-close vs adjclose inconsistency, and |ret|>80% on ADV<$1M; plus a full-history
contamination check (adjclose >$3000 or >4× single-day jump).

**Taxonomy (all samples):** 22 data-quality-only, 1 liquidity-only (ADCT — a
*real* $1.32→$3.44 drift, adj=close, but ADV $320K), 2 both (RNAZ, PHIO).
**54% of data-flagged events have ADV < $5M** — the reverse-split / pump / bad-print
cluster (EQ, PHIO, RNAZ, PBM, INTS, OTLK, JAGX, LYEL). The few *liquid* flagged
names (SRPT −24%, AGIO, SRRK) are genuine event gaps, not errors, and sit outside
the low-liq bucket.

**Worst offenders (ticker, entry, ret, ADV$, flags):**

| ticker | entry | ret | ADV$ | flags |
|---|---|--:|--:|---|
| ADCT | 2025-05-13 | +160.6% | 319,615 | big_ret_illiq (real move, untradeable) |
| RNAZ | 2025-01-07 | +123.0% | 453,404 | adj_jump, close_jump, big_ret_illiq, global_contam |
| PHIO | 2025-04-07 | +86.4% | 111,951 | adj_jump, close_jump, big_ret_illiq |
| RNAZ | 2025-02-11 | −84.4% | 43.7M* | adj_jump, close_jump, global_contam |
| OTLK | 2026 (OOS) | −50.2% | 559,073 | adj_jump, close_jump |
| URGN | 2025 | −49.3% | 7.5M | adj_jump, close_jump |
| AQST | 2026 (OOS) | −50.4% | 14.5M | adj_jump, close_jump |
| BCTX | 2025 | −45.9% | 5.1M | adj_jump, close_jump |

*RNAZ is the canonical trap: historical adjclose runs to **94,248** (reverse-split
contamination in 2022-24), and in 2025 it trades a **$300 nominal price on ~4,000
shares/day** — a book you cannot cross. Its $43.7M ADV is itself a stale pump-era
artifact.

**Low-liquidity Q1 recompute:**

| version | n | mean | median | t | boot95 |
|---|--:|--:|--:|--:|---|
| raw (all) | 75 | +7.13% | +2.84% | +1.95 | [+0.4, +14.7] |
| artifacts excluded | 64 | +4.18% | +2.81% | +1.62 | [−0.6, +9.2] |
| excluded + winsor 1/99 | 64 | +4.18% | +2.81% | +1.62 | [−0.6, +9.2] |
| **excluded + winsor + cost** | 64 | **−0.89%** | −2.44% | −0.35 | [−5.7, +4.1] |

Removing 11 artifact/untradeable-tail events alone drops the mean 7.1%→4.2% and
**pushes the CI across zero** (t 1.95→1.62). Winsorization adds nothing further —
because the artifacts *were* the >99th-pctile tail.

---

## 3. Cost realism — spreads finish the job

Tiered half-spread per side: ≥$20M ADV 0.20% · $5-20M 0.50% · $1-5M 1.50% ·
<$1M 3.50% (round-trip = 2×). Cross-checked with a `min(5%, 35/√ADV)` model.

**IS gross → net (tiered) by ADV quartile:**

| bucket | gross | net | | OOS gross | OOS net |
|---|--:|--:|---|--:|--:|
| Q1 low | +7.13% | **+1.84%** | | +7.74% | +3.51% |
| Q2 | +0.72% | −0.24% | | −2.69% | −3.61% |
| Q3 | −1.07% | −1.47% | | +1.78% | +1.38% |
| Q4 high | −1.54% | −1.94% | | −1.15% | −1.55% |

Spreads remove ~5.3% from Q1 gross. Combined with artifact removal + winsor,
the **pooled IS+OOS clean/winsor/cost NET** by quartile is:

| bucket | n | mean | median | t | boot95 |
|---|--:|--:|--:|--:|---|
| **Q1 low** | 75 | **+0.37%** | −2.44% | +0.15 | [−4.3, +5.2] |
| Q2 | 99 | +0.68% | +0.65% | +0.50 | [−1.9, +3.4] |
| Q3 | 107 | +0.59% | −0.36% | +0.71 | [−1.0, +2.3] |
| Q4 high | 126 | −1.79% | −2.19% | −2.39 | [−3.3, −0.3] |

No bucket carries a positive, significant, tradeable edge. Q1 = zero; Q4 (crowded
large caps) is significantly *negative*.

---

## 4. Stress-testing the two "survivors"

**(a) $2-5 entry-price bucket** (median-positive, t=2.11 gross): after cost
+4.64% / median +6.84% / **t=1.08** (CI [−3.5, +12.9] crosses 0); clean+cost t=1.01.
Median ADV in this bucket is **$340K** (p25 $17K). Significance evaporates and the
capacity is negligible.

**(b) OOS Q1 low-ADV** (gross +7.74%): median only +0.68%; the mean rests on **two
names** (GLSI +87%, a genuine $14.6→$27.2 drift at $3.8M ADV, and FBIO +44%). After
winsor+cost the **median goes to −2.3%** and t=1.05 (CI [−4.5, +22.7]). n=11 — noise.

**Capacity (IS Q1):** median ADV $736K, min $3,330. At a 10% participation cap you
can deploy **~$74K/day (median), $333/day (min)** — not an institutional strategy
even where a genuine drift exists.

---

## Bottom line

A genuine phenomenon exists — occasional real pre-PDUFA drift in illiquid names
(ADCT, ESLA, GLSI) — but it is (i) tail/unpredictable, (ii) **not separable ex-ante**
from reverse-split / pump / bad-print noise (RNAZ, PHIO, OTLK, EQ), and (iii)
**uncrossable at any meaningful size** (median low-liq ADV <$1M; 3-7% round-trip
spreads). Stripped of artifacts and charged realistic costs, the micro-cap edge is
**+0.4% mean / −2.4% median, t=0.15 — indistinguishable from zero**, and does not
validate OOS. The apparent edge is a data-and-spread illusion, not exploitable alpha.
