"""Zentrale Falsifizierungs-Batterie.

Fuer jede mit freien Daten testbare Strategie wird eine Monats-Renditereihe
(Long-Short oder Timing) konstruiert und derselben Batterie unterzogen:

  - Newey-West-t-Statistik (voller Zeitraum und NUR Post-Publikation = echtes OOS)
  - Subperioden: Dekaden-Sharpes, Anteil positiver Dekaden (Regimestabilitaet)
  - Moving-Block-Bootstrap (Block 12, 5000 Reps) fuer Post-Pub-Sharpe-KI
  - Sign-Flip-Permutationstest (5000 Reps) auf Post-Pub-Mittelwert
  - Deflated Sharpe Ratio (Bailey & Lopez de Prado) mit N Trials = Batteriegroesse
  - Benjamini-Hochberg-FDR ueber alle Post-Pub-p-Werte der Batterie
  - Kostenszenarien (strategie-spezifischer Turnover x Kosten je Trade)

Konvention: Renditen in Prozent pro Monat.
"""
import json
import numpy as np
import pandas as pd
from scipy import stats
import ff_parse as ff

RNG = np.random.default_rng(42)
N_BOOT = 5000
N_PERM = 5000


# ---------------------------------------------------------------- utilities
def nw_tstat(x, lags=6):
    """Newey-West-t-Statistik fuer H0: mean = 0."""
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    T = len(x)
    if T < 24:
        return np.nan, np.nan, T
    m = x.mean()
    e = x - m
    s2 = e @ e / T
    for L in range(1, lags + 1):
        w = 1 - L / (lags + 1)
        s2 += 2 * w * (e[:-L] @ e[L:]) / T
    se = np.sqrt(s2 / T)
    t = m / se
    p = 1 - stats.norm.cdf(t)  # einseitig: H1 mean > 0
    return t, p, T


def ann_sharpe(x, freq=12):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    if len(x) < 24 or x.std(ddof=1) == 0:
        return np.nan
    return x.mean() / x.std(ddof=1) * np.sqrt(freq)


def max_drawdown(x):
    x = np.asarray(x, float) / 100.0
    w = np.cumprod(1 + x)
    peak = np.maximum.accumulate(w)
    return float(((w - peak) / peak).min())


def block_bootstrap_sharpe(x, n=N_BOOT, block=12):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    T = len(x)
    if T < 36:
        return np.nan, np.nan, np.nan
    nblocks = int(np.ceil(T / block))
    sh = np.empty(n)
    for i in range(n):
        starts = RNG.integers(0, T - block, nblocks)
        idx = (starts[:, None] + np.arange(block)).ravel()[:T]
        b = x[idx]
        sh[i] = b.mean() / b.std(ddof=1) * np.sqrt(12)
    return (float(np.quantile(sh, 0.025)), float(np.quantile(sh, 0.975)),
            float((sh <= 0).mean()))


def perm_pvalue(x, n=N_PERM):
    """Sign-Flip-Permutation: unter H0 (symmetrisch um 0) ist das Vorzeichen
    jeder Beobachtung austauschbar."""
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    if len(x) < 24:
        return np.nan
    obs = x.mean()
    signs = RNG.choice([-1.0, 1.0], size=(n, len(x)))
    null = (signs * np.abs(x)).mean(axis=1)
    return float((null >= obs).mean())


def deflated_sharpe(x, n_trials, freq=12):
    """DSR nach Bailey & Lopez de Prado (2014). SR in Periodeneinheiten."""
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    T = len(x)
    if T < 36:
        return np.nan
    sr = x.mean() / x.std(ddof=1)
    g3 = stats.skew(x)
    g4 = stats.kurtosis(x, fisher=False)
    # erwartetes Maximum von n_trials unabhaengigen Null-Sharpes
    emc = 0.5772156649
    z1 = stats.norm.ppf(1 - 1.0 / n_trials)
    z2 = stats.norm.ppf(1 - 1.0 / (n_trials * np.e))
    sr0 = np.sqrt(1.0 / (T - 1)) * ((1 - emc) * z1 + emc * z2)
    denom = np.sqrt(max(1 - g3 * sr + (g4 - 1) / 4.0 * sr ** 2, 1e-12))
    dsr = stats.norm.cdf((sr - sr0) * np.sqrt(T - 1) / denom)
    return float(dsr)


def decade_stats(s):
    out = {}
    for dec, grp in s.groupby(s.index.year // 10 * 10):
        if len(grp) >= 24:
            out[str(dec)] = round(ann_sharpe(grp.values), 2)
    pos = sum(1 for v in out.values() if v > 0)
    return out, (pos / len(out) if out else np.nan)


def evaluate(name, s, pub_year, cost_pa, n_trials, freq=12):
    """s: pd.Series (PeriodIndex M), Monatsrenditen in %. cost_pa: Kosten-Drag
    p.a. in % fuer (konservativ, sehr konservativ)."""
    s = s.dropna()
    full_t, full_p, full_T = nw_tstat(s.values)
    oos = s[s.index.year > pub_year]
    ins = s[s.index.year <= pub_year]
    oos_t, oos_p, oos_T = nw_tstat(oos.values)
    dec, dec_pos = decade_stats(s)
    lo, hi, p_boot = block_bootstrap_sharpe(oos.values)
    modern = s[s.index.year >= 2011]
    res = {
        "strategie": name,
        "publikationsjahr": pub_year,
        "n_monate_gesamt": int(full_T),
        "sharpe_gesamt": round(float(ann_sharpe(s.values)), 2),
        "t_nw_gesamt": round(float(full_t), 2),
        "sharpe_insample": round(float(ann_sharpe(ins.values)), 2) if len(ins) >= 24 else None,
        "sharpe_postpub": round(float(ann_sharpe(oos.values)), 2) if len(oos) >= 24 else None,
        "t_nw_postpub": round(float(oos_t), 2) if not np.isnan(oos_t) else None,
        "p_nw_postpub": round(float(oos_p), 4) if not np.isnan(oos_p) else None,
        "sharpe_2011_2026": round(float(ann_sharpe(modern.values)), 2) if len(modern) >= 24 else None,
        "decay_pct": None,
        "dekaden_sharpes": dec,
        "anteil_positive_dekaden": round(float(dec_pos), 2) if not np.isnan(dec_pos) else None,
        "boot_ci_sharpe_postpub": [round(lo, 2), round(hi, 2)] if not np.isnan(lo) else None,
        "boot_p_sr_le_0": round(p_boot, 4) if not np.isnan(p_boot) else None,
        "perm_p_postpub": round(perm_pvalue(oos.values), 4),
        "dsr_postpub": round(deflated_sharpe(oos.values, n_trials), 3),
        "skew_monatlich": round(float(stats.skew(s.dropna().values)), 2),
        "max_drawdown": round(max_drawdown(s.values), 2),
        "kosten_drag_pa": cost_pa,
    }
    if res["sharpe_insample"] and res["sharpe_postpub"] is not None and res["sharpe_insample"] > 0:
        res["decay_pct"] = round(100 * (1 - res["sharpe_postpub"] / res["sharpe_insample"]), 0)
    # Netto-Sharpes unter Kostenszenarien (auf Post-Pub-Reihe)
    if len(oos) >= 24:
        vol_pa = oos.std(ddof=1) * np.sqrt(12)
        mean_pa = oos.mean() * 12
        res["netto_sharpe_postpub"] = [
            round(float((mean_pa - c) / vol_pa), 2) for c in cost_pa
        ]
    else:
        res["netto_sharpe_postpub"] = None
    return res


# ---------------------------------------------------------------- strategies
def build_strategies():
    S = []
    f3 = ff.factors_monthly()
    f5 = ff.factors5_monthly()
    mom = ff.mom_monthly()
    st = ff.strev_monthly()
    lt = ff.ltrev_monthly()

    # (Name, Serie %/Monat, Publikationsjahr, Kosten-Drag p.a. % [konservativ, sehr konservativ])
    S.append(("Momentum (MOM-Faktor, 12-1)", mom.iloc[:, 0], 1993, [1.7, 4.2]))
    S.append(("Short-Term Reversal (1M)", st.iloc[:, 0], 1990, [7.2, 18.0]))
    S.append(("Long-Term Reversal (5J)", lt.iloc[:, 0], 1985, [0.8, 2.0]))
    S.append(("Value (HML)", f3["HML"], 1993, [0.4, 1.0]))
    S.append(("Size (SMB)", f3["SMB"], 1981, [0.4, 1.0]))
    S.append(("Profitability (RMW)", f5["RMW"], 2013, [0.4, 1.0]))
    S.append(("Investment (CMA)", f5["CMA"], 2015, [0.4, 1.0]))

    var = ff.portfolios("VAR")
    S.append(("Low-Volatility (VAR Lo20-Hi20)", var["Lo 20"] - var["Hi 20"], 2006, [1.2, 3.0]))
    beta = ff.portfolios("BETA")
    S.append(("Low-Beta (BETA Lo20-Hi20)", beta["Lo 20"] - beta["Hi 20"], 2014, [1.2, 3.0]))
    ni = ff.portfolios("NI")
    S.append(("Net Issuance (NI Lo20-Hi20)", ni["Lo 20"] - ni["Hi 20"], 2008, [0.5, 1.2]))
    ac = ff.portfolios("AC")
    S.append(("Accruals (AC Lo20-Hi20)", ac["Lo 20"] - ac["Hi 20"], 1996, [0.6, 1.5]))

    # --- Saisonalitaeten auf taeglichem Marktfaktor seit 1926
    fd = ff.factors_daily()
    mkt = (fd["Mkt-RF"] + fd["RF"])
    # Turn-of-Month: letzter Handelstag + erste 3 des Monats
    per = mkt.index.to_period("M")
    is_tom = np.zeros(len(mkt), bool)
    pos_in_month = pd.Series(np.arange(len(mkt)), index=mkt.index).groupby(per).cumcount()
    month_len = pd.Series(1, index=mkt.index).groupby(per).transform("sum")
    is_tom |= (pos_in_month.values < 3)
    is_tom |= (pos_in_month.values == (month_len.values - 1))
    tom_excess = fd["Mkt-RF"].where(is_tom, 0.0)
    tom_m = tom_excess.groupby(per).sum()
    tom_m.index = pd.PeriodIndex(tom_m.index, freq="M")
    S.append(("Turn-of-Month (Mkt, T-1..T+3)", tom_m, 1988, [0.5, 1.2]))

    # TOM-Spread: long TOM-Tage, short Nicht-TOM-Tage (skaliert auf gleiche
    # Tagesanzahl) -> eliminiert die Aktienpraemie als Stoergroesse
    tom_cnt = pd.Series(is_tom.astype(float), index=fd.index).groupby(per).sum()
    non_cnt = pd.Series((~is_tom).astype(float), index=fd.index).groupby(per).sum()
    non_sum = fd["Mkt-RF"].where(~is_tom, 0.0).groupby(per).sum()
    scale = (tom_cnt / non_cnt).values
    tom_spread = pd.Series(tom_m.values - scale * non_sum.values, index=tom_m.index)
    S.append(("TOM-Spread (TOM minus Nicht-TOM)", tom_spread, 1988, [0.5, 1.2]))

    # Halloween / Sell-in-May: Mkt-RF nur Nov-Apr
    mrf = f3["Mkt-RF"]
    is_win = pd.Series(mrf.index.month, index=mrf.index).isin([11, 12, 1, 2, 3, 4])
    hal = mrf.where(is_win, 0.0)
    S.append(("Halloween (Nov-Apr long, sonst Cash)", hal, 2002, [0.1, 0.3]))
    # Halloween-Spread: long Nov-Apr, short May-Okt (Saisondifferenz ohne Praemie)
    hal_spread = mrf.where(is_win, 0.0) - mrf.where(~is_win, 0.0)
    S.append(("Halloween-Spread (NovApr minus MaiOkt)", hal_spread, 2002, [0.2, 0.5]))

    # Januar-Effekt Small Caps: (ME Lo10 - Hi10) nur im Januar
    me = ff.portfolios("ME")
    smb_jan = (me["Lo 10"] - me["Hi 10"]).where(
        pd.Series(me.index.month, index=me.index) == 1, 0.0)
    S.append(("Januar-Effekt Microcaps (SMB nur Jan)", smb_jan, 1983, [0.8, 2.0]))

    # --- Overnight-Effekt SPY (Close->Open) vs Intraday
    spy = ff.spy_daily()
    adj = spy["adjclose"] / spy["close"]
    on = (spy["open"] * adj / (spy["close"] * adj).shift(1) - 1) * 100
    intra = (spy["close"] / spy["open"] - 1) * 100
    on_m = on.groupby(on.index.to_period("M")).sum().dropna()
    intra_m = intra.groupby(intra.index.to_period("M")).sum().dropna()
    S.append(("Overnight SPY (Close->Open)", on_m, 2008, [5.0, 12.6]))
    S.append(("Intraday SPY (Open->Close, Kontrolle)", intra_m, 2008, [5.0, 12.6]))
    # ON-ID-Spread: long overnight, short intraday (der eigentliche Anomalie-Claim)
    oni = (on_m - intra_m).dropna()
    S.append(("Overnight-minus-Intraday SPY", oni, 2008, [10.0, 25.2]))

    # --- Variance Risk Premium: implizite Varianz (VIX^2) minus realisierte
    vix = ff.vix_daily()
    vix_m_end = vix["vix"].groupby(vix.index.to_period("M")).last()
    rv = (mkt / 100.0) ** 2
    rv_m = rv.groupby(per).sum()
    rv_m.index = pd.PeriodIndex(rv_m.index, freq="M")
    iv_m = (vix_m_end / 100.0) ** 2 / 12.0
    common = iv_m.index.intersection(rv_m.index)[:-1]
    # Payoff Short-Varianz-Swap im Folgemonat, skaliert in %-Punkte (x100)
    vrp = pd.Series(
        (iv_m.loc[common].values - rv_m.shift(-1).loc[common].values) * 100.0,
        index=common).dropna()
    # Kosten in Einheiten der Payoff-Skala: ~30% bzw. ~70% der historischen
    # Bruttopraemie (Var-Swap-Spreads, VIX-Futures-Rollkosten)
    gross_pa = float(vrp.mean() * 12)
    S.append(("Variance Risk Premium (Short Var)", vrp, 2009,
              [round(0.3 * gross_pa, 2), round(0.7 * gross_pa, 2)]))

    return S


def main():
    strategies = build_strategies()
    n_trials = len(strategies)
    results = [evaluate(n, s, py, c, n_trials) for n, s, py, c in strategies]

    # Benjamini-Hochberg ueber Post-Pub-p-Werte (einseitig, NW)
    ps = [(i, r["p_nw_postpub"]) for i, r in enumerate(results)
          if r["p_nw_postpub"] is not None]
    ps.sort(key=lambda x: x[1])
    m = len(ps)
    passed = set()
    max_k = 0
    for rank, (i, p) in enumerate(ps, 1):
        if p <= 0.10 * rank / m:  # FDR 10%
            max_k = rank
    for rank, (i, p) in enumerate(ps, 1):
        if rank <= max_k:
            passed.add(i)
    for i, r in enumerate(results):
        r["bh_fdr10_bestanden"] = i in passed

    with open("/home/user/Bot/research/empirics/results.json", "w") as f:
        json.dump(results, f, indent=1, ensure_ascii=False)

    cols = ["strategie", "sharpe_insample", "sharpe_postpub", "t_nw_postpub",
            "dsr_postpub", "perm_p_postpub", "bh_fdr10_bestanden",
            "anteil_positive_dekaden", "netto_sharpe_postpub", "skew_monatlich"]
    df = pd.DataFrame(results)[cols]
    pd.set_option("display.width", 250)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
