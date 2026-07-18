# Institutionelles Alpha-Labor — Abschlussbericht

**Stand: 18. Juli 2026 · 27 unabhängige Research-Agents · 78 untersuchte Strategien · empirische Falsifizierungs-Batterie auf Daten 1926–2026**

---

## 0. Kernaussage (Executive Summary)

**Im strengen Sinne des Mandats — eine Strategie, die mit hoher Wahrscheinlichkeit eine echte, reproduzierbare, nach Kosten handelbare Marktineffizienz darstellt und ALLE Falsifizierungstests besteht — hat KEINE der 78 untersuchten Strategien vollständig bestanden.**

Das ist das ehrliche Ergebnis, und es ist konsistent mit der besten verfügbaren Meta-Evidenz (McLean & Pontiff 2016: ~58 % Renditeverfall nach Publikation; Harvey/Liu/Zhu 2016: t > 3 als Mindesthürde; Hou/Xue/Zhang 2020: Mehrheit der Anomalien nicht replizierbar).

Was überlebt, sind **keine "Free Lunches", sondern drei Kategorien zweiter Ordnung**:

1. **Persistente, ökonomisch erklärbare Risikoprämien** mit nicht-profitmaximierender Gegenseite (Trendfolge auf Futures, Qualitäts-/Profitabilitätsprämie, Varianz-Risikoprämie). Sie sind real und handelbar, aber ihre Rendite ist Bezahlung für ein Risiko oder eine Dienstleistung — nicht die Ausbeutung eines Fehlers.
2. **Friktionsgeschützte Struktureffekte kleiner Kapazität** (Turn-of-Month-Flusseffekt). Real, seit Jahrzehnten stabil, aber zu klein, um institutionelles Kernkapital zu tragen.
3. **Ausführungsabhängige Reste klassischer Anomalien** (residuales Momentum mit Vol-Scaling), deren Netto-Alpha nur mit institutioneller Ausführungsqualität und aktivem Crowding-Management überlebt.

34 von 78 Strategien wurden vollständig verworfen (KILL), 40 als WEAK eingestuft (existent, aber grenzwertig oder nicht skalierbar), nur 4 erhielten von den unabhängigen Agents ein CANDIDATE — und eines davon (Net Payout Yield) wurde durch unsere eigene Out-of-Sample-Empirie anschließend gekippt (Abschnitt 5.1).

---

## 1. Studiendesign

### 1.1 Unabhängige Research-Agents

27 Agents, jeder mit exklusivem Mandat für genau eine Anomalieklasse, strikt isoliert (kein Agent durfte die Outputs der anderen lesen), jeder mit **adversarialer Nullhypothese** („Es gibt KEIN Alpha in deiner Klasse") und einheitlichem, maschinenlesbarem Urteilsformat (KILL / WEAK / CANDIDATE plus Scores auf den sieben Mandatskriterien). Die Mehrzahl der Agents hatte Websuche verfügbar und hat Post-Publication-Evidenz bis Juli 2026 herangezogen (u. a. die Fed-Studie „The Disappearing Overnight Drift" vom Juli 2026, die Supreme-Court-Entscheidung *FS Credit v. Saba* vom Juni 2026 und die Momentum-Crowding-Unwinds vom Januar und Juni/Juli 2026).

Abgedeckte Klassen: PEAD, Analystenrevisionen, Insiderkäufe, Spin-offs, Index-Rekonstitution, Aktienrückkäufe, SEOs/Net Issuance, IPOs, Reverse Splits, Saisonalitäten, Faktorprämien, Low-Vol/BAB, Liquidität, Cross-Sectional Momentum, Mean Reversion, Trendfolge/TSMOM, Optionen/Vol, Short Interest, ETF-Flows, CEF-Discounts, Merger Arbitrage, Rohstoffe/Futures, Makro/FOMC, Overnight-Effekt, Small/Micro Caps, Biotech-Katalysatoren, ADRs/Cross-Listings. Alle Einzeldossiers: `research/agents/01–27_*.md`.

### 1.2 Zentrale empirische Falsifizierungs-Batterie

Unabhängig von den Agents wurden 20 mit freien, survivorship-bias-freien Daten testbare Strategien einer einheitlichen Batterie unterzogen (`research/empirics/run_tests.py`, Ergebnisse in `results.json`):

- **Daten:** Ken-French-Bibliothek (CRSP-basiert, monatlich/täglich ab 1926/27), SPY/QQQ/IWM-Tages-OHLC (Yahoo, 1993–2026), VIX (FRED, 1990–2026).
- **Echtes Out-of-Sample:** Für jede Strategie wurde der Zeitraum NACH dem Publikationsjahr der Originalstudie als OOS-Fenster definiert — der härteste verfügbare Hold-out, weil er zusätzlich den realen Arbitrage-Druck nach Bekanntwerden enthält.
- **Tests:** Newey-West-t-Statistiken (voll & OOS), Moving-Block-Bootstrap (5 000 Reps) für Sharpe-Konfidenzintervalle, Sign-Flip-Permutationstests (5 000 Reps), Deflated Sharpe Ratio (Bailey & López de Prado, N = 20 Trials), Benjamini-Hochberg-FDR (10 %) über die gesamte Batterie, eine konservative White's-Reality-Check-Variante (Max-t-Verteilung unter H0), Dekaden-Stabilität, Skewness/Max-Drawdown, Kostenszenarien (konservativ / sehr konservativ, strategie-spezifischer Turnover).
- **Artefakt-Kontrollen:** Für Kalender- und Overnight-Effekte wurden zusätzlich **saubere Spread-Konstruktionen** getestet, die die Aktienprämie als Störgröße eliminieren — mit entscheidenden Konsequenzen (Abschnitt 3).

### 1.3 Ranking-Logik

Rangliste NICHT nach Rendite, sondern nach dem Mandats-Score: 40 % Wahrscheinlichkeit echter Ineffizienz, je 10 % Reproduzierbarkeit, Signifikanz nach Multiple-Testing-Korrektur, Regimestabilität, Handelbarkeit, Kapazität, Kostenrobustheit (`research/empirics/aggregate.py`, `ranking.json`). Agent-Urteile wurden anschließend gegen die empirische Batterie abgeglichen; **bei Konflikt schlägt die Out-of-Sample-Empirie das Agent-Urteil.**

---

## 2. Datenrestriktionen (Ehrlichkeitsvorbehalt)

Ohne CRSP/Compustat/IBES/TAQ-Lizenzen sind einige Klassen hier **nicht direkt empirisch testbar** (PEAD auf Einzeltitelebene, Analystenrevisionen, Insider-Filings, Deal-Spreads, Borrow-Fees, Optionsflächen). Für diese Klassen stützt sich das Urteil auf die publizierte Replikationsliteratur und die Websuche der Agents — das ist der wissenschaftlich ehrliche Weg, aber es bleibt Sekundärevidenz. Chen-Zimmermann (Open Source Asset Pricing) war aus diesem Netzwerk nicht abrufbar (GitHub-Releases blockiert). Kein Test in diesem Projekt erhebt den Anspruch, eine institutionelle Produktionsvalidierung zu ersetzen.

---

## 3. Ergebnisse der empirischen Batterie (1926–2026)

Sharpe-Angaben annualisiert; „OOS" = nach Publikationsjahr; Netto-Sharpe unter [konservativen, sehr konservativen] Kostenannahmen; BH = Benjamini-Hochberg-FDR 10 % bestanden.

| Strategie | Sharpe In-Sample | Sharpe OOS | t (NW, OOS) | DSR | BH | Netto-Sharpe OOS | Befund |
|---|---|---|---|---|---|---|---|
| Momentum (MOM, 12-1) | 0,55 | 0,29 | 1,59 | 0,40 | ✗ | [0,18 / 0,03] | ~47 % Verfall; Skew −3,1; überlebt nur institutionell |
| Short-Term Reversal | 0,90 | 0,14 | 0,98 | 0,14 | ✗ | [−0,45 / −1,33] | nach Kosten tot |
| Long-Term Reversal | 0,35 | 0,16 | 0,88 | 0,19 | ✗ | [0,08 / −0,05] | tot |
| Value (HML) | 0,43 | 0,15 | 0,73 | 0,15 | ✗ | [0,12 / 0,07] | massiver Verfall |
| Size (SMB) | 0,30 | 0,01 | 0,08 | 0,03 | ✗ | [−0,03 / −0,09] | tot (seit 1981) |
| Profitability (RMW) | 0,41 | 0,26 | 0,97 | 0,17 | ✗ | [0,21 / 0,13] | positiv, aber statistisch nicht belastbar |
| Investment (CMA) | 0,52 | −0,05 | −0,15 | 0,02 | ✗ | [−0,10 / −0,17] | OOS negativ |
| Low-Volatility (VAR-Spread) | 0,12 | −0,06 | −0,25 | 0,01 | ✗ | [−0,11 / −0,19] | OOS negativ |
| Low-Beta (BETA-Spread) | −0,08 | −0,52 | −1,88 | 0,00 | ✗ | [−0,57 / −0,64] | OOS deutlich negativ |
| Net Issuance (NI-Spread) | 0,48 | −0,07 | −0,26 | 0,01 | ✗ | [−0,11 / −0,17] | **OOS tot — kippt Agent-CANDIDATE** |
| Accruals (AC-Spread) | 0,62 | 0,24 | 1,23 | 0,27 | ✗ | [0,17 / 0,07] | verfallen |
| Turn-of-Month (Timing) | 1,04 | 0,52 | 3,21 | 0,88 | ✓ | [0,45 / 0,36] | **Überlebender** — alle 10 Dekaden positiv |
| **TOM-Spread (sauber)** | 0,95 | 0,30 | 1,91 | 0,48 | ✓ | [0,24 / 0,16] | Saisoneffekt real, aber klein |
| Halloween (long Nov–Apr) | 0,46 | 0,58 | 3,05 | 0,81 | ✓ | [0,57 / 0,55] | Scheineffekt (siehe Spread) |
| **Halloween-Spread (sauber)** | 0,20 | 0,12 | 0,61 | 0,09 | ✗ | [0,10 / 0,08] | **Artefakt der Aktienprämie — KILL** |
| Januar-Effekt Microcaps | 0,71 | 0,42 | 2,87 | 0,91 | ✓ | [0,29 / 0,10] | real, aber Mikro-Kapazität |
| Overnight SPY (long) | 1,38 | 0,89 | 4,03 | 0,92 | ✓ | [0,39 / −0,37] | Scheineffekt (siehe Spread) |
| **Overnight−Intraday-Spread** | 0,85 | 0,15 | 0,74 | 0,11 | ✗ | [−0,49 / −1,46] | **Artefakt + Kosten — KILL** (deckt sich mit Fed-Studie 7/2026) |
| Variance Risk Premium | 1,06 | 0,43 | 1,95 | 0,46 | ✓ | [0,25 / ~0] | real, aber Skew −8,9: Versicherungsprämie |

**Zentrale Lehren der Batterie:**

1. **Der Post-Publication-Verfall ist die stärkste Regelmäßigkeit im Datensatz.** Der mittlere Sharpe-Verfall der klassischen Querschnittsanomalien liegt bei ~60–100 %. Size, Investment, Low-Vol/Low-Beta und Net Issuance sind out-of-sample tot oder negativ.
2. **Zwei berühmte „Anomalien" sind Dekompositionen der Aktienprämie, keine Alphas.** Halloween und der Overnight-Effekt sehen in der Long-only-Version spektakulär aus (t > 3 bzw. > 4); die sauberen Spread-Tests (t = 0,61 bzw. 0,74) zeigen, dass fast der gesamte Effekt die Marktprämie selbst ist. Das ist genau die Sorte Fehler, die dieses Labor verhindern soll.
3. **Nur drei Effekte bestehen die Multiple-Testing-Korrektur auch in sauberer Konstruktion:** Turn-of-Month, Januar-Microcap-Saisonalität (mit Mini-Kapazität) und die Varianz-Risikoprämie (die eine Risikoprämie ist).

---

## 4. Was verworfen wurde — nach Verwerfungsgrund

**34 KILL-Urteile.** Die häufigsten Todesursachen, mit prominenten Beispielen:

- **Out-of-Sample-Verfall nach Publikation:** S&P-Inklusionseffekt (von +8,9 % Ankündigungsrendite in den 1990ern auf ~0 seit 2013, Greenwood & Sammon), Pre-FOMC-Drift (Lucca & Moench — nach 2015 verschwunden), klassische SUE-Drift, IVOL (Ang et al.), rohe Size-Prämie, naiver Overnight-Drift (Fed-Bestätigung Juli 2026; NightShares-ETFs nach 14 Monaten liquidiert).
- **Kosten/Borrow-Fees fressen die Bruttorendite:** Short-Term Reversal, Liquiditätsprovision (Nagel-Proxy), Amihud-Prämie, Reverse-Split-Shorts (Microcap-Borrow 20–50 % p. a.), IV-Crush-Verkauf um FDA-Events, ETF-NAV-Arbitrage für Nicht-APs.
- **Kein Arbitrage-Mechanismus / strukturell unzugänglich:** China-A-H-Premium (Kapitalverkehrskontrollen), DLC-Arbitrage (Universum durch Unifikationen praktisch verschwunden; LTCM-Lektion), IPO-Underpricing (Zuteilung, nicht handelbar).
- **Data-Mining / widersprüchliche Literatur:** Hedging-Pressure-Faktor (Zeitreihenbruch durch CFTC-Reklassifizierung), FOMC-Zyklus-Wochen, Post-FDA-Drift (Vorzeichen je nach Studie umgekehrt), Kursziel-Revisionen, Short-Squeeze-Harvesting.
- **Basiert auf wenigen Ausreißern / einem Regime:** Leveraged-ETF-Front-Running (> 80 % der Gewinne in 2,5 Monaten Q4 2008), aggregiertes Short Interest als Timing-Signal (2008-abhängig).

Die vollständige Liste mit Begründungen steht in `research/empirics/ranking.json` und den Einzeldossiers.

---

## 5. Die Rangliste der Überlebenden

Geordnet nach dem Mandats-Score (Reproduzierbarkeit, Signifikanz nach MTK, Regimestabilität, Handelbarkeit, Kapazität, Kostenrobustheit, p(echte Ineffizienz)) — **nicht nach Rendite**. Alle Renditeangaben sind konservative Erwartungen nach Kosten, abgeleitet aus OOS-Empirie und Netto-Literatur; sie sind Schätzungen, keine Zusagen.

### 5.1 Vorab: Ein gekipptes CANDIDATE (Lehrstück)

**Net Share Issuance / Net Payout Yield** erhielt vom unabhängigen Agent das höchste CANDIDATE (Score 3,5; ökonomisch bestechend: Management-Timing als Gegenseite). Unsere eigene Batterie zeigt jedoch: Der NI-Spread (Lo20−Hi20, French-Daten) hat seit Publikationsjahr 2008 einen Sharpe von **−0,07** (t = −0,26) und fällt bei Benjamini-Hochberg durch. Nach der Mandatsregel „Out-of-Sample-Scheitern ⇒ verwerfen" wird die Strategie **auf WEAK/verworfen herabgestuft**. Dass ausgerechnet das bestbewertete Agent-CANDIDATE an der eigenen Empirie scheitert, ist der beste Beleg dafür, warum das Studiendesign beide Ebenen braucht.

### 5.2 Rang 1 — Diversifizierte Multi-Horizont-Trendfolge auf Futures (TSMOM/CTA-Stil)

*Einstufung: persistente Verhaltens-/Fluss-Prämie, teils echte Ineffizienz. p(echte Ineffizienz) ≈ 0,5–0,6. Das einzige CANDIDATE, das Agent-Urteil UND externe Live-Evidenz übersteht.*

- **Warum sie überlebt:** Einzige Strategieklasse mit (a) ~150 Jahren dokumentierter Evidenz über Assetklassen (Hurst/Ooi/Pedersen), (b) **realen Netto-Live-Track-Records** statt Backtests (SG Trend Index, BTOP50 — auditierte Fonds-Performance nach allen Kosten), (c) bestandenem Härtetest im OOS-Regimewechsel (2022: SG Trend > +20 % bei gleichzeitigem Aktien-Anleihen-Absturz), (d) ökonomischer Gegenseite, die nicht wegarbitriert werden kann (Hedger, Zentralbanken, rebalancierende Institutionen handeln nicht profitmaximierend), (e) niedrigen Kosten (Futures: 1–5 Bp je Trade).
- **Regelwerk (vollständig):** Universum ≥ 50 liquide Futures (Aktienindizes, Staatsanleihen, Währungen, Rohstoffe). Signal: Vorzeichen der Überschussrendite über 3, 6 und 12 Monate (gleichgewichtet kombiniert). Position: Signal × Zielrisiko je Markt (z. B. 40 bp Tagesvol-Beitrag), Skalierung über inverse Ex-ante-Vol (60-Tage), Portfolio-Cap bei 10–15 % Ziel-Vol. Wöchentliches Rebalancing, Roll nach Liquiditätskalender. Keine diskretionären Overrides.
- **Benötigte Daten:** Tages-Settlements + Volumina/OI aller Kontrakte (CSI/Bloomberg), Rollkalender, FX-Kurse.
- **Erwartung (netto, nach Fonds-Kosten):** Rendite 4–8 % p. a. über Cash bei 10–12 % Vol; **Sharpe 0,4–0,7**; Sortino ≈ 0,6–0,9 (positive Skewness!); Profit Factor ≈ 1,3–1,5; Max-Drawdown-Erwartung 15–25 %, Flachphasen von 5–9 Jahren (2012–2017!) sind dokumentierter Bestandteil; Turnover ~300–600 % p. a. je Seite.
- **Kapital:** ab ~20–50 Mio. USD sinnvoll (Diversifikation über Märkte), Kapazität der Klasse nachweislich > 100 Mrd. USD.
- **Risiken:** Whipsaw-Regime; Crowding (CTA-AUM); Karriererisiko der Flachphasen; Trendbrüche an Wendepunkten.
- **Ursache der Edge:** langsame Kapitalflüsse, Underreaction, Hedging-Flows; Prämie überlebt Publikation seit > 30 Jahren, weil die Gegenseite strukturell weiterliefert und die Flachphasen schwache Hände aussieben.

### 5.3 Rang 2 — Turn-of-Month-Flusseffekt (als Overlay, nicht als Kernstrategie)

*Einstufung: friktionsgeschützter Struktureffekt, wahrscheinlich echte (kleine) Ineffizienz. p ≈ 0,5. Bestes empirisches Testergebnis der gesamten Batterie in sauberer Konstruktion.*

- **Warum sie überlebt:** In unserer Batterie der robusteste Effekt: Timing-Version OOS-Sharpe 0,52 (t = 3,21, DSR 0,88), sauberer Spread OOS 0,30 (t = 1,91), **BH-bestanden, alle 10 Dekaden seit 1926 positiv**, Kosten minimal (4 Index-Future-Trades/Monat). Ökonomische Ursache dokumentiert (Ogden 1990): Gehalts-, Renten- und Rebalancing-Flüsse konzentrieren sich am Monatswechsel — der Zahlungskalender ist nicht arbitrierbar.
- **Aber:** Der Agent (isoliert, Websuche) meldet fast vollständigen Decay im engen Fenster liquider Märkte seit ~2015 — unsere Daten zeigen 2011–2026 weiterhin positive, aber abgeschwächte Werte. Kapazität begrenzt (der Effekt bewegt ~4 Handelstage/Monat im Index); als eigenständige Fondsstrategie ungeeignet.
- **Regelwerk:** Long S&P-500-Futures (ES) von Schluss T−1 (letzter Handelstag des Monats) bis Schluss T+3, sonst Cash/Collateral; Umsetzung ausschließlich in Futures; keine Einzelaktien.
- **Erwartung (netto):** 2–3,5 % p. a. Zusatzrendite auf das Overlay-Notional bei ~7–8 % Vol der aktiven Tage; Sharpe 0,3–0,45; Sortino ≈ 0,3–0,5; Profit Factor ≈ 1,3–1,5; Max-DD ~15–20 %; Turnover 24 Round-Trips p. a.; Kapital: ab 1 Mio. USD (Futures-Mindestgröße), Kapazität realistisch einstellige Mrd. USD.
- **Risiken:** weiterer Decay durch Bekanntheit; Ereignisrisiko in den 4 Halte-Tagen; Regimeabhängigkeit geringer als bei allen Alternativen, aber nicht null.
- **Ursache der Edge:** kalendergebundene, unelastische Zahlungsströme; zu klein und zu banal, um institutionelles Arbitragekapital anzuziehen — genau deshalb noch da.

### 5.4 Rang 3 — Qualitäts-/Profitabilitätsprämie (RMW/QMJ, long-only-Tilt oder Long-Short)

*Einstufung: überwiegend Risikoprämie/Preisfehler-Hybrid mit höchster Kapazität unter den Überlebenden. p ≈ 0,4.*

- **Warum sie überlebt:** OOS seit 2014 positiv (Sharpe 0,26 brutto, netto 0,13–0,21 — schwach, aber als einzige Querschnittsprämie kostenrobust wegen Turnover < 20 % p. a.), 86 % positive Dekaden, international repliziert, Krisen-Konvexität (Quality outperformt in Drawdowns: 2008, 2020, 2022). Ökonomische Story (Benchmark-Zwang, Lottery-Präferenzen, Agency-Probleme der Gegenseite) ist plausibel, aber nicht beweisbar.
- **Ehrlicher Vorbehalt:** t = 0,97 OOS heißt: Die Prämie ist statistisch NICHT von null unterscheidbar; QMJ hatte seit 2021 den schwersten Drawdown seit 20 Jahren. Wer sie handelt, handelt eine Hypothese mit gutem ökonomischen Fundament, kein bewiesenes Alpha.
- **Regelwerk:** Universum Large/Mid Caps entwickelter Märkte; Score = Gross Profitability (Novy-Marx) + Accruals-Qualität + Leverage-Konservatismus (je z-Score, gleichgewichtet); langes Quintil kaufen (long-only-Tilt gegen Benchmark oder marktneutral gegen kurzes Quintil mit Borrow-Fee-Filter); Rebalancing vierteljährlich, Turnover-Bremse 15 % je Quartal.
- **Erwartung (netto):** long-only-Tilt: 1–2 % p. a. aktive Rendite bei 3–4 % Tracking Error (IR 0,3–0,5); Long-Short: Sharpe 0,15–0,3; Sortino ähnlich (Skew ≈ −0,4); Profit Factor ≈ 1,2; Max-DD der Long-Short-Variante ~20–25 %; Kapital ab 10 Mio. USD; **Kapazität sehr hoch (≫ 100 Mrd. USD)** — der eigentliche Grund für Rang 3.
- **Risiken:** lange Underperformance-Phasen (Karriererisiko); Crowding über Quality-ETFs; Zinsregime-Sensitivität.
- **Ursache der Edge:** institutionelle Anleger meiden „langweilige" Qualität zugunsten von Story-Aktien; Prämie ist klein genug, um Arbitrage nicht zu lohnen, und groß genug, um sie zu ernten.

### 5.5 Rang 4 — Residuales Momentum mit Volatility-Scaling (nur mit institutioneller Ausführung)

*Einstufung: verfallenes, aber nicht totes Verhaltens-Alpha; ausführungsgebunden. p ≈ 0,35.*

- **Warum sie (bedingt) überlebt:** Klassisches 12-1-Momentum ist OOS auf Sharpe 0,29 verfallen (t = 1,59, BH ✗, Skew −3,1, Max-DD −58 %) — als naive Strategie verworfen. Die Literatur (Blitz/Huij/Martens; Barroso & Santa-Clara; Frazzini/Israel/Moskowitz mit realen AQR-Ausführungsdaten) zeigt aber: Residualisierung + Vol-Scaling verdoppeln die risikoadjustierte Rendite und entschärfen die Crash-Mode; reale institutionelle Handelskosten liegen eine Größenordnung unter den akademischen Schätzungen. Zwei Momentum-Crowding-Unwinds allein im Jahr 2026 (Januar; Juni/Juli, AI-Basket −19 % in zwei Wochen) sind zugleich Warnung und Bestätigung der Mechanik.
- **Regelwerk:** Universum Top-1000-Liquidität; Signal = 12-1-Residualrendite aus rollierender FF3-Regression (36 M), skaliert mit 1/realisierter 6-M-Vol; Dezil-Long-Short, Beta- und Sektor-neutralisiert; Ziel-Vol 10 %, Vol-Scaling nach Barroso/Santa-Clara (Ex-ante-Vol-Ziel des Faktors); monatliches Rebalancing mit Trade-Netting und Limit-Order-Ausführung; Crowding-Monitor (Positionierungsperzentile) mit De-Risking-Regel.
- **Erwartung (netto, institutionelle Ausführung):** Sharpe 0,3–0,5; Sortino 0,4–0,6 (Vol-Scaling reduziert Linksschiefe, eliminiert sie nicht — Nov. 2020: −25 % trotz Schutz); Profit Factor ≈ 1,25–1,4; Max-DD 20–30 %; Turnover 600–900 % p. a. je Seite (!); Kapital: erst ab ~100 Mio. USD mit eigener Ausführungsinfrastruktur sinnvoll; Kapazität einstellige bis niedrige zweistellige Mrd. USD.
- **Risiken:** Momentum-Crashes bei Marktwenden; Crowding (2026 live demonstriert); Kostenexplosion bei schlechter Ausführung — für Retail-Umsetzung ist die Strategie **tot**.
- **Ursache der Edge:** Underreaction/Anchoring; die Crash-Eigenschaft selbst ist die Arbitrage-Barriere (Karriererisiko), deshalb verfällt der Rest nicht vollständig.

### 5.6 Rang 5 — Varianz-Risikoprämie (Short Variance, ausdrücklich als Risikoprämie deklariert)

*Einstufung: mit hoher Sicherheit KEINE Ineffizienz, sondern eine Versicherungsprämie. p(echte Ineffizienz) ≈ 0,15 — gelistet, weil sie alle statistischen Tests besteht und die Einordnung Teil des Auftrags ist.*

- **Empirie:** IV−RV-Payoff OOS (2010–2026): Sharpe 0,43 (t = 1,95, BH ✓, alle Dekaden positiv) — aber Monats-Skew **−8,9**, Sortino nur 0,19, und die Kostenszenarien drücken den Netto-Sharpe auf 0,25 bis ~0. Ein einziges Volmageddon-Ereignis (Feb. 2018: XIV −96 % an einem Tag; März 2020) kostet mehrere Jahre Prämie.
- **Regelwerk (falls gehandelt):** systematischer Verkauf 1-Monats-Varianz (Varianzswaps oder delta-gehedgte Straddles) auf S&P 500, Notional ≤ 1 % NAV Vega, hartes Stop-Regime bei VIX-Spikes, Rekapitalisierungsreserve ≥ 3× Worst-Case-Monat; niemals gehebelte Short-Vol-ETPs.
- **Erwartung:** 1–3 % p. a. Prämienbeitrag aufs Gesamtbuch bei strikter Sizing-Disziplin; Profit Factor ≈ 1,9 in ruhigen Zeiten — der Faktor ist irreführend, das Risiko sitzt im Tail; Max-DD im Stressfall ein Mehrfaches der Jahresprämie.
- **Ursache der „Edge":** strukturelle Nachfrage nach Absicherung (Mandate, Retail-Puts, 0DTE-Flows); der Verkäufer ist der Versicherer. Wer das als Alpha verbucht, hat den Test des Mandats nicht verstanden — deshalb Rang 5 trotz bestandener Statistik.

### 5.7 Ehrenvolle Nennung ohne Rang (Kapazitäts-Mikroeffekte)

**Januar-Microcap-Saisonalität** (OOS t = 2,87, BH ✓, alle Dekaden positiv, netto-Sharpe 0,10–0,29): real, aber ein Ein-Monats-Effekt in Microcaps — Kapazität wenige zehn Mio. USD, für institutionelles Kapital irrelevant. Dokumentiert der Vollständigkeit halber.

---

## 6. Explizite Mandatsantwort

> „Wenn keine Strategie diese Kriterien erfüllt, sage das ausdrücklich."

**Keine der 78 untersuchten Strategien erfüllt ALLE Mandatskriterien gleichzeitig** (Reproduzierbarkeit + Signifikanz nach Multiple-Testing + Regimestabilität + Handelbarkeit + Kapazität + Kostenrobustheit + hohe Wahrscheinlichkeit echter Ineffizienz). Die fünf gelisteten Überlebenden sind die Redlichkeits-Rangliste des „besten Rests":

- **Trendfolge** und **Quality** bestehen fast alles, sind aber wahrscheinlich überwiegend Risikoprämien (p echte Ineffizienz ≈ 0,5 bzw. 0,4).
- **Turn-of-Month** ist wahrscheinlich eine echte Ineffizienz, aber kapazitätslimitiert und im Decay.
- **Residuales Momentum** ist wahrscheinlich ein echter Verhaltensrest, aber nur mit institutioneller Ausführung netto positiv.
- **Die Varianz-Risikoprämie** besteht jeden statistischen Test und ist trotzdem keine Ineffizienz.

Das ist kein enttäuschendes Ergebnis, sondern das erwartbare Ergebnis eines funktionierenden Falsifizierungsprozesses: **Ein Verfahren, das fast alles tötet und das Überlebende korrekt als Risikoprämie etikettiert, ist genau das, was institutionelles Research von Data-Mining unterscheidet.**

---

## 7. Reproduktion

```
research/
├── agents/          27 unabhängige Dossiers (01–27), je mit YAML-Urteilsblock
├── data/            Ken-French-Rohdaten, SPY/QQQ/IWM-OHLC, VIX (FRED)
├── empirics/
│   ├── ff_parse.py  Parser für French-Dateien
│   ├── run_tests.py Falsifizierungs-Batterie (NW, Bootstrap, Permutation, DSR, BH-FDR, Reality Check, Kosten)
│   ├── aggregate.py Aggregation der Agent-Urteile → Mandats-Score-Ranking
│   ├── results.json Batterie-Ergebnisse (20 Strategien)
│   └── ranking.json Gesamt-Ranking (78 Strategien)
└── REPORT.md        dieser Bericht
```

Batterie reproduzieren: `cd research/empirics && python3 run_tests.py && python3 aggregate.py` (benötigt pandas/scipy/statsmodels/pyyaml; Seed fixiert, deterministisch).

*Hinweis: Dieser Bericht ist Research, keine Anlageberatung. Alle Kennzahlen sind historisch bzw. konservative Schätzungen ohne Gewähr.*
