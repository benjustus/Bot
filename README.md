# Pre-PDUFA Run-up — Independent Backtest Audit

Independent quant-researcher audit, replication and extension of a Pre-PDUFA
run-up strategy backtest. **Full findings: [`REPORT.md`](REPORT.md)** (German).

## TL;DR

- The original 16-event note is **arithmetically correct** — replicated to <0.01pp
  (mean +7.31%, median +8.64%, PF 4.10, end €2,082/€2,398, −24.8% DD all match exactly).
- Its conclusion is **not** robust: tiny sample (n=16), winner/survivorship selection,
  no CRLs, and **no beta adjustment**.
- On **431 verified events (2025–2026, incl. 119 CRLs)** the raw run-up is real but
  small (+3.4%, t≈5) and is **almost entirely biotech-sector beta (XBI)**. The
  beta-adjusted excess is **+1.0%, not statistically significant** (t≈1.1–1.5,
  95% CI includes 0, hit rate ≈50%, median ≈0%).
- Eventual **CRLs ran up as much as approvals** → run-up carries **no** predictive
  information about the outcome.
- In the same bull span, **buy-and-hold XBI returned +76.5%** (−26% DD) — beating the
  all-in strategy's Monte-Carlo median (+49%) at half the risk. **No exploitable edge.**

## Data provenance (all real; nothing estimated or invented)

| Data | Source | Notes |
|---|---|---|
| Daily prices | Yahoo Finance v8 (`query1`), split/div-adjusted | cached in `data/prices/` |
| PDUFA dates + outcomes (2025–26) | pdufa.bio `/decisions` (server-rendered, deterministically parsed) | 445 events, Approved/CRL |
| Approvals 2022–23 (regime cohort) | drugs.com new-drug-approvals archive | approvals-only (winner-biased) |
| Market cap (proxy) | Yahoo v7 quote (crumb) | **current** value, coarse tier only |
| Benchmarks | XBI, IBB, ^GSPC, EURUSD=X (Yahoo) | beta adjustment, FX, regime |
| External cross-ref | pdufa.bio `/runup-by-year` (1,754 events, 2020+) | regime dependence |

Raw fetched pages are archived under `data/raw/` with retrieval date.

## Reproduce

```bash
pip install pandas numpy scipy requests
python3 src/parse_pdufa_bio.py      # HTML → data/events_pdufa_bio.csv
python3 src/fetch_all_prices.py     # Yahoo prices → data/prices/ (cached; reruns are free)
python3 src/fetch_marketcap.py      # market-cap proxy → data/marketcap.csv
python3 src/run_all.py              # ALL cited numbers → output/results.json
```

Individual stages: `src/analyze.py` (core stats, raw + XBI-excess), `src/splits.py`
(outcome/size/regime splits, capital sim, robustness, gap-risk), `src/backtest.py`
(engine), `src/yahoo.py` (range-aware price cache).

## Honest limitations

- Clean dual-outcome sample is concentrated in **2025–2026** (a biotech bull regime);
  2022–2023 only via a smaller approvals-only cohort + external reference. A fully
  unbiased 2010–2024 sample was **not** reconstructable from free/reachable sources
  (ex-ante PDUFA calendars are paywalled; the Web Archive is egress-blocked here).
- Market-cap tier is a **current-value proxy**, not point-in-time.
- **Review type** and **short interest**: not reliably available for free → left as
  explicit data gaps (not estimated).
- "Unavailable in feed" ≠ proven delisting (this environment's Yahoo mirror has some
  coverage gaps, e.g. FOLD/MRNS return "Not Found" though still listed).

Not investment advice. Past patterns do not predict the future.
