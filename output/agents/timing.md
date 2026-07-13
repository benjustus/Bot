# Timing Optimizer (Research Stream 2) - Entry/Exit Heatmap vs XBI

**Metric:** XBI-EXCESS mean return and its t-stat on the **tradeable** subset
(entry_px >= $2 and mcap >= $100M). Raw return is mostly beta and is ignored for
judging alpha. In-sample = **2025** (317 events); hold-outs = **2026** (128) and
**2022-23 regime** (52). Offsets are CALENDAR days before PDUFA (T-entry -> T-exit).

## Verdict (short)
**No stable timing region with exploitable alpha, and nothing survives the hold-out.**
The 2025 excess surface is a broad, shallow, mostly-*positive* plateau (avg **+0.58%**,
peak **+1.15%**) but it is statistically indistinguishable from zero at **every** cell
(max t = **1.89**, 0/92 cells reach t>1.96). The single marginal 3-cell "stable region"
**flips negative** out of sample. The 2025 and 2026 surfaces are **uncorrelated (r=0.045)**.

## Heatmap 1 - Mean XBI-excess (%), 2025 tradeable
`*` marks the cells of the largest stable region (mean>0 AND t>1.5).
```
entry\exit      -20     -15     -12     -10      -7      -5      -3      -2      -1
T-60       +0.26   +0.53   +0.89   +0.78   +1.12   +0.76   +0.86   +0.96   +0.64 
T-55       -0.02   +0.26   +0.61   +0.54   +0.97   +0.61   +0.72   +0.78   +0.38 
T-50       -0.03   +0.17   +0.51   +0.41   +0.76   +0.47   +0.58   +0.66   +0.25 
T-45       -0.07   +0.15   +0.49   +0.46   +0.77   +0.51   +0.64   +0.63   +0.15 
T-40       -0.01   +0.21   +0.60   +0.57   +0.90   +0.65   +0.79   +0.79   +0.28 
T-35       +0.14   +0.38   +0.81   +0.71   +1.04   +0.85   +1.03   +1.01   +0.55 
T-30       +0.24   +0.49   +0.87   +0.64   +1.15   +0.88   +0.97   +0.97   +0.57 
T-25       -0.05   +0.28   +0.59   +0.38   +0.82   +0.61   +0.66   +0.67   +0.28 
T-20           .   +0.42   +0.71   +0.65   +1.12*  +0.96*  +0.99   +1.01   +0.60 
T-15           .       .   +0.39   +0.42   +0.71*  +0.69   +0.78   +0.74   +0.35 
T-10           .       .       .       .   +0.36   +0.26   +0.30   +0.27   -0.14 
```

## Heatmap 2 - t-stat vs 0, 2025 tradeable
```
entry\exit      -20     -15     -12     -10      -7      -5      -3      -2      -1
T-60       +0.28   +0.53   +0.84   +0.72   +0.99   +0.67   +0.72   +0.76   +0.49 
T-55       -0.02   +0.27   +0.59   +0.49   +0.86   +0.55   +0.59   +0.61   +0.30 
T-50       -0.04   +0.18   +0.50   +0.38   +0.68   +0.42   +0.50   +0.54   +0.20 
T-45       -0.08   +0.16   +0.51   +0.46   +0.75   +0.50   +0.59   +0.57   +0.13 
T-40       -0.01   +0.27   +0.69   +0.62   +0.95   +0.69   +0.79   +0.77   +0.28 
T-35       +0.21   +0.52   +0.99   +0.83   +1.17   +0.96   +1.08   +1.04   +0.58 
T-30       +0.42   +0.76   +1.20   +0.87   +1.47   +1.16   +1.21   +1.15   +0.66 
T-25       -0.10   +0.50   +0.89   +0.57   +1.15   +0.89   +0.92   +0.89   +0.36 
T-20           .   +1.10   +1.46   +1.24   +1.89*  +1.53*  +1.49   +1.42   +0.79 
T-15           .       .   +1.32   +1.03   +1.58*  +1.27   +1.31   +1.19   +0.54 
T-10           .       .       .       .   +1.18   +0.69   +0.70   +0.58   -0.27 
```

## Heatmap 3 - n (tradeable trades per cell), 2025
```
entry\exit      -20     -15     -12     -10      -7      -5      -3      -2      -1
T-60         256     256     256     256     256     256     256     256     256 
T-55         255     255     255     255     255     255     255     255     255 
T-50         257     257     257     257     257     257     257     257     257 
T-45         258     258     258     258     258     258     258     258     258 
T-40         258     258     258     258     258     258     258     258     258 
T-35         259     259     259     259     259     259     259     259     259 
T-30         257     257     257     257     257     257     257     257     257 
T-25         258     258     258     258     258     258     258     258     258 
T-20           .     258     258     258     258     258     258     258     258 
T-15           .       .     260     261     261     261     261     261     261 
T-10           .       .       .       .     252     260     260     260     260 
```

## Stable regions (contiguous cells with mean>0 AND t>1.5, 4-connectivity)
- Cells passing the threshold anywhere on the surface: **3/92**.
- Isolated spikes (size-1 components): **0**; blocks (size>=2): **1**.
- **Largest stable region:** size **3**, entry T-15..T-20,
  exit T-5..T-7; cells = [[20, 7], [20, 5], [15, 7]].
  avg excess **+0.93%**, avg t **1.67** (range 1.53..1.89), avg n 259.
- Representative timing (max-t = centroid): **T-20 -> T-7**,
  excess +1.12%, t 1.89.

  Note: this "region" is contiguous only because neighbouring cells share heavily
  overlapping windows on the SAME events (forced smoothness), not because of independent
  confirmation. Its own peak (t=1.89) is not significant at the two-sided 5% level.

## Hold-out validation of the largest stable region
| sample | avg excess | avg t | cells positive | cells t>1 |
|---|---|---|---|---|
| 2025 in-sample | +0.93% | 1.67 | 100% | 100% |
| **2026 hold-out** | **-0.48%** | **-0.65** | 0% | 0% |
| 2022-23 regime | +0.86% | 0.47 | 67% | 0% |

Representative timing **T-20 -> T-7** across samples: 2025 **+1.12%** (t=1.89) ->
2026 **-0.27%** (t=-0.34) -> regime **-0.21%** (t=-0.10). The in-sample optimum does
NOT persist. The 2022-23 pooled average (+0.86%) is driven by 2 of 3 cells on only n=13
names with t<1, and its own max-t cell is negative -- not a confirmation.

## Cross-surface transfer test
Pearson r between the 2025 and 2026 mean-excess surfaces across all 92 cells = **0.045**
(essentially zero): the *location* of good timings in 2025 carries no information about 2026.
Surface-average excess collapses from **+0.58%** (2025) to **+0.07%** (2026); 2026 cells are
positive only **52/92** (coin-flip) and **0/92** reach t>1.5.

## Multiple-testing note
92 cells tested. At one-sided p<0.05 (t>1.645, n~250 so t~normal) one expects
**~4.6** false positives by chance; at two-sided p<0.05 (|t|>1.96) **~2.3**.
Observed: **1** cell with t>1.645 and **0** with t>1.96 -- at or BELOW the chance
expectation. The findings do NOT exceed what noise produces. (Because the 92 tests are strongly
positively correlated, the effective number of independent tests is far below 92, so a smooth
in-sample cluster is expected under the null and is not evidence of an edge.)
