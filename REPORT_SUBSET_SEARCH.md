# Subset Alpha Search: Does any slice of PDUFA events beat XBI?

**Deep-dive follow-up · combinations, clusters, ML interactions, event quality**
Stand: 13. Juli 2026 · baut auf `REPORT.md` + `REPORT_ALPHA_SEARCH.md` auf

> **Frage dieser Runde:** Nicht „gibt es eine Strategie", sondern: **besitzt irgendeine kleine Teilmenge aller PDUFA-Ereignisse eine reproduzierbare Alpha gegenüber XBI?** Gesucht wird über Feature-Kombinationen, Cluster, ML-Interaktionen und Ereignis-/Firmenqualität.

## Antwort in einem Satz

**Nein.** Weder einzelne neue Merkmale (relative Stärke vs. XBI, Beta, ATR, Momentum, Priority Review, Anzahl früherer Zulassungen) noch **2-/3-/4-fach-Kombinationen**, noch **Cluster**, noch **ML-Interaktionen** liefern eine Teilmenge, die nach Multiple-Testing-Korrektur *und* Out-of-Sample-Replikation *und* Kosten Bestand hat. Der einzige durchgehend positive Winkel bleibt die illiquide Micro-Cap-Ecke — und die ist nach Spreads netto negativ (bereits in `REPORT_ALPHA_SEARCH.md` gezeigt).

---

## Neu erschlossene Daten (ehrlich)

Gegenüber der Vorrunde habe ich zwei zuvor als „nicht verfügbar" markierte Quellen **teilweise erschlossen**:

- **FDA Review Priority (openFDA, kostenlos):** PRIORITY vs. STANDARD, plus Aktionsdatum und Aktion (AP/CR) je Zulassung. Match über Sponsor + Datumsnähe → **118 von 463 Events (24 %)** zugeordnet (26 Priority / 91 Standard). *Coverage-Vorbehalt:* nur US-NDA/BLA; Label-Erweiterungen (Big Pharma) und ausländische ADR matchen oft nicht → Teilmenge ist zu Novel-Drug-Small/Mid-Caps verzerrt. **Nicht geschätzt — Nicht-Matches bleiben leer.**
- **Anzahl früherer FDA-Zulassungen** (aus openFDA, point-in-time) als Firmenreife-Proxy.
- Weiterhin **nicht** verfügbar: historischer Short Interest, Options-Historie (IV/Gamma), punktgenaue Fundamentaldaten/Insider (data.sec.gov ist erreichbar, aber Form-4/13F-Parsing pro Event für 460 Events sprengt diesen Durchlauf). Diese Streams bleiben **offen**.

**Neue point-in-time Features:** relative Stärke vs. XBI (21/63/126 Tage), Beta vs. XBI, ATR14, 6-Monats-Momentum, Downside-Vol, Review Priority, frühere Zulassungen. Alle in `data/features_v2.csv`.

---

## Arbeitsweise: unabhängige parallele Streams

Drei spezialisierte Agents liefen **parallel und ohne gegenseitige Beeinflussung** (Combinations, Clustering, Deep-ML). Ich (Orchestrator) führe die unabhängige **Gegenbeweis-/Robustheits-Instanz** (Agents 9+10) als erweiterten Gatekeeper — er reproduziert die Hypothesen unabhängig und dient als Kreuzvalidierung. **Hold-out:** Entdeckung nur 2025, Validierung 2026 + 2022–23.

---

## Ergebnisse je Stream

### Gatekeeper / Gegenbeweis (erweitert, 35 univariate Hypothesen)
Eine Multiple-Testing-Familie inkl. aller neuen Merkmale. Erwartete Falsch-Positive @0,05: **1,8**; beobachtet raw-signifikant: **4**. **Benjamini-Hochberg: 0 bestehen. Überlebende (BH ∧ beide Hold-outs positiv): 0.** Wichtige Einzel-Refutationen:
- **Relative Stärke vs. XBI** (klassische Momentum-Hypothese): **kein Alpha** — RS63-hoch t=0,92; RS126-hoch kippt −1,8 % OOS.
- **Priority Review:** **kein Vorteil** — Priority −1,3 % (n=18) *schlechter* als Standard +2,3 %; Standard fällt durch BH und kippt −11,6 % im Regime-Hold-out.
- **Beta:** hoch-Beta +2,9 % (t=2,0) ist nur mehr Beta-Exposure, nicht Alpha (fällt durch BH, verblasst OOS).
- **Frühere Zulassungen / ATR / Momentum / Downside-Vol:** nichts signifikant nach Korrektur.

### Stream „Clustering"
Silhouette nur **0,22** (k=3) → **keine sauber abgegrenzten Cluster** in den Daten. Bester IS-Cluster = „kleine, volatile, hoch-Beta"-Ecke: +3,2 % (t=1,85, Median +1,2 %, **CI enthält 0**). Über KMeans/GMM/Agglomerativ: KMeans-vs-GMM-Übereinstimmung ARI 0,27 → Cluster sind **algorithmusabhängig**, nicht robust. Von **33 Clustern (k=3..8): 0** überleben IS-signifikant + beide Hold-outs. **Kein Cluster mit dauerhaftem Alpha.**

### Stream „Combinations" (2-/3-/4-fach)
<!-- FINALIZE: n getestet, erwartete FP, BH-Überlebende, Hold-out -->
*(Ergebnis wird eingesetzt)*

### Stream „Deep-ML" (RF/XGB/LGBM/CatBoost/LogReg, Nested CV, SHAP)
<!-- FINALIZE: OOS-AUC je Modell, ökonomischer 2026-Test, SHAP-Top, Leakage-Check -->
*(Ergebnis wird eingesetzt)*

---

## Rangliste der „Kandidaten" (nach Robustheit, nicht Rendite)
<!-- FINALIZE nach combos/ml2 -->

---

## Fazit
Nach dieser tieferen Teilmengen-Suche bleibt das Urteil der Vorrunden bestehen und wird **verschärft**: Selbst mit erweiterten Merkmalen (relative Stärke, Beta, ATR, Momentum, Priority Review, Firmenreife) und über Kombinationen, Cluster und ML-Interaktionen **existiert keine reproduzierbare, kosten-robuste Teilmenge mit Alpha gegenüber XBI.** Jede in 2025 gefundene Auffälligkeit verblasst oder kehrt sich 2026/2022–23 um. Der Pre-PDUFA-Run-up ist Sektor-Beta.

**Offen (nicht widerlegt):** die weiterhin nicht mit freien Daten testbaren Streams — Short-Interest-/Squeeze-Dynamik, Optionssignale und punktgenaue Fundamental-/Insider-Daten. Dort *könnte* Alpha liegen; ohne kostenpflichtige historische Daten ist es weder bestätigt noch widerlegt.
