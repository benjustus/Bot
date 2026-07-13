# Institutionelle Alpha-Suche: Pre-PDUFA vs. XBI

**12 unabhängige Research-Streams · eine Frage**
Stand: 13. Juli 2026 · Fortsetzung des Audits (`REPORT.md`)

> **Die einzige Frage:** Existiert *irgendeine* reproduzierbare Pre-PDUFA-Strategie mit statistisch belastbarer **Überrendite gegenüber XBI** (nicht: „gibt es einen Run-up")?

## Antwort in einem Satz

**Nein.** Über **6 mit echten Daten testbare Streams**, **26 formal geprüfte Hypothesen** und zwei Out-of-Sample-Perioden hinweg überlebt **keine einzige** Konditionierung die Kombination aus *Beta-Adjustierung + Multiple-Testing-Korrektur + Hold-out-Replikation + realistischen Kosten*. Der einzige durchgehend positive Winkel (illiquide Micro-Caps) ist nach echten Spreads **netto negativ**. Fünf weitere Streams (FDA-Designationen, klinische Daten, Firmenkennzahlen, Short Interest, Optionen) sind mit frei verfügbaren Daten **nicht testbar** — sie bleiben *offene Fragen*, nicht widerlegt.

---

## Methode: 12 Streams, unabhängig gerechnet, am Ende zusammengeführt

Fünf Discovery-Agents (Market Cap, Timing, Regime, Liquidität, ML) liefen **parallel und unabhängig** auf einem gemeinsamen, streng *point-in-time* gebauten Feature-Datensatz (`data/features.csv`, 463 Events; jedes Merkmal nur mit vor dem Einstieg bekannter Information). Zwei Meta-Streams (Monte-Carlo, Overfitting-Gatekeeper) habe ich als Orchestrator gerechnet — der Gatekeeper **reproduziert die Hypothesen der Agents unabhängig** und dient als Kreuzvalidierung. Ergebnis: **alle Streams konvergieren.**

**Hold-out-Disziplin (entscheidend):** Entdeckung nur auf **2025 (In-Sample, n=257 handelbar)**. Validierung auf **2026 (Hold-out, n=122)** und **2022–23 (Regime-Hold-out, anderes Zins-/Vola-Regime)**. Auf den Hold-outs wurde nichts optimiert.

**Datenlage der 12 Streams (ehrlich gekennzeichnet):**

| # | Stream | Testbar mit realen Daten? | Beleg |
|---|---|---|---|
| 1 | Market Cap | ✅ ja | Marktkap. (aktueller Proxy) + Kurse |
| 2 | Timing (Heatmap) | ✅ ja | Kurse |
| 3 | FDA-Designationen (Priority/Orphan/Fast-Track/Breakthrough) | ❌ **nein** | kein freier strukturierter Feed; nur Einzelabruf pro Medikament |
| 4 | Klinische Datenqualität (Ph-III) | ❌ **nein** | subjektiv/manuell, nicht strukturiert |
| 5 | Firmenkennzahlen (Cash Runway, Burn, Secondary, Insider, Institutionelle) | ❌ **nein** | historisch nicht frei; Yahoo liefert nur *aktuelle* Snapshots (z. B. `heldPercentInstitutions=119,8 %` — unbrauchbar) |
| 6 | Short Interest | ❌ **nein** | Yahoo liefert nur *aktuellen* Snapshot (`sharesShort`), keine historische Zeitreihe |
| 7 | Optionen (IV/OI/Gamma) | ❌ **nein** | Yahoo liefert nur *aktuelle* Chains, keine Historie |
| 8 | Liquidität (Volumen/Float/Spread) | ✅ ja | Volumen aus Kursreihe (point-in-time), Float aktuell |
| 9 | Market Regime (XBI-200d, VIX, Zinsen) | ✅ ja | XBI, ^VIX, ^TNX |
| 10 | Machine Learning | ✅ ja | nur point-in-time-Features |
| 11 | Monte-Carlo | ✅ ja | realisierte Trades |
| 12 | Overfitting-Detektor / Gatekeeper | ✅ ja | alle Hypothesen |

Die Streams 3–7 habe ich **nicht** geschätzt oder erfunden. Ich habe die Nicht-Verfügbarkeit für 6 und 7 direkt am Yahoo-Endpunkt verifiziert (nur aktueller Snapshot). Sie sind der wahrscheinlichste Ort für eine noch unentdeckte Edge und erfordern **kostenpflichtige historische Punkt-in-Zeit-Daten** (FINRA-SI-Historie, ORATS/CBOE-Options, S&P-Capital-IQ-Fundamentaldaten, FDA-Designations-Datenbank).

---

## Ergebnisse je testbarem Stream

**Metrik durchgehend: XBI-Excess** (Rendite minus XBI über dasselbe Fenster). Rohe Rendite ist Sektor-Beta und zählt nicht als Alpha.

### Stream 1 — Market Cap (7 Buckets)
Kein Bucket mit *t>2 in-sample **und** positiv im Hold-out **und** nicht ausreißergetrieben*. Einziger IS-Kandidat **300–500 Mio.** (+11,9 %, t=2,0, n=13) → fällt durch BH/Bonferroni **und** kippt out-of-sample auf **−7,6 %** (PF 0,23). Der `<100 Mio.`-„Vorteil" ist eine **Nano-Falle**: getragen von RNAZ +122 % (Reverse-Split-Kurs ~101 $ — vom 2-$-Filter *nicht* gefangen) und ~1-$-Titeln; nach Liquiditätsfilter −6,1 %. `>5 Mrd.`-Kontrolle flach (+0,2 % IS / −0,6 % OOS) — konsistent mit Markteffizienz.

### Stream 2 — Timing (Heatmap T-60→T-10 × T-20→T-1, 92 Zellen)
**Keine Zelle** erreicht zweiseitig t>1,96 in-sample. Größte „stabile" Region: nur 3 Zellen (Einstieg −15…−20, Ausstieg −5…−7), Ø-Excess **+0,9 %**, t max 1,89. Diese Region im **2026-Hold-out: −0,48 %** (0 % der Zellen positiv) — Vorzeichen kippt. Fenster überlappen stark → effektive unabhängige Tests ≪ 92; eine zusammenhängende Region ist **kein** Beleg. **Kein stabiles Timing-Alpha.**

### Stream 9 — Market Regime (XBI-Trend, VIX, Zinsen)
Drei IS-Regime sehen positiv aus (below-200d +2,71 %/t2,76; neg-Momentum +2,24 %/t2,15; steigende-Zinsen +3,29 %/t2,46) — aber sie sind **0,80 kollinear** (≈ *eine* Wette „schwache XBI-Phase"), im 2026-Hold-out **nicht testbar** (2026 ist durchgehend eine Über-200d-Phase) und im 2022–23-Hold-out **vorzeichen-negativ** (−4,6 %). Unkonditioniert ist der Excess selbst insignifikant (IS +1,15 %, t=1,47). **Kein Regime-Alpha, das repliziert.**

### Stream 8 — Liquidität & Artefakte (die entscheidende Prüfung)
Illiquidestes Quartil (ADV < ~3 Mio. $, n=75): **brutto** Ø-Excess **+7,1 %** (Median +2,8 %, t=1,95, PF 2,10) — *sieht* aus wie die Edge. **Netto** nach realistischen Spreads (0,2 %/0,5 %/1,5 %/3,5 % pro Seite nach ADV):
- gestaffeltes Modell: **+1,8 % Ø, Median −2,4 %, t=0,51, PF 1,20**
- √-Spread-Modell: **−0,4 % Ø, Median −5,1 %, t=−0,11, PF 0,96**

**3 von 75 Namen** (ADCT +154 %, RNAZ +122 %, PHIO +73 %) liefern **65 %** des Bucket-Excess; dazu 24 Artefakt-Events (RNAZ: 300-$-Aktie, ~4.000 Stück/Tag, historischer adjclose bis 94.248). Kombiniert (bereinigt + winsorisiert + Kosten) bleibt Q1 gepoolt IS+OOS: **+0,37 % Ø / −2,44 % Median, t=0,15** (Boot-CI [−4,3 %, +5,2 %]) — **null**. Kapazität: Q1-Median-ADV ~0,74 Mio. $/Tag → **~74.000 $/Tag handelbar** (bei 10 % Beteiligung) — nicht skalierbar. **Antwort:** Bruttopreis-Illusion + Artefakte + unüberwindbare Spreads; **netto null bis negativ.** Keine handelbare Edge.

### Stream 10 — Machine Learning (Walk-Forward, kein Leakage)
Ziel = XBI schlagen. Nur point-in-time-Features. Label-Shuffle-AUC ≈ 0,50 (kein Leakage bestätigt). OOS-AUC 2026: **Logistic 0,61**, Random Forest 0,45, Gradient Boost 0,46 (Bäume ≤ Zufall out-of-sample, hoch überangepasst: IS-AUC 0,72–0,81). Logistic-Walk-Forward-AUC 0,58; Permutations-p = **0,095 (nicht signifikant)**. **Ökonomisch** (vor-spezifizierte Top-Hälfte-Selektion, netto 1 % Round-Trip, auf 2026): Logistic **+0,32 %**, Random Forest −0,07 %, Ensemble **−0,17 %** — alle innerhalb ~1 SE von null; bei **4 von 5 Modellen Spearman(Prob, realisiert) ≤ 0** (sie ranken *rückwärts*). Die scheinbaren +1–2,5 % kommen nur aus tuned-Threshold-Kleinst-n-Artefakten. Getrieben werden die Modelle von **Regime-/Kalender-Features** (XBI-Momentum, Zinsen, Quartal), die Stream 9 bereits entlarvt hat. **Kein statistisch belastbares, selektierbares Alpha.**

### Stream 11 — Monte-Carlo (100.000 Roll-over-Pfade, handelbares Universum)
| Sizing | EV | Median | P(Gewinn) | P(<−50 %) | CVaR₅ | Median-MaxDD |
|---|---|---|---|---|---|---|
| **All-in** | 2.475 € | 2.238 € | 78 % | **3,4 %** | **647 € (−57 %)** | −29 % |
| **Fixe 5 %** | 1.505 € | 1.506 € | 56 % | 0,0 % | 1.417 € | −2 % |

All-in „funktioniert" nur, weil es volles Kapital in einen steigenden Sektor hebelt (Beta) — mit 3,4 % Ruin-Wahrscheinlichkeit und CVaR₅ −57 %, und der Median (+49 %) **unterbietet XBI-Buy-&-Hold (+76,5 %)**. Prudente fixe Größe = **nach Kosten flach** (kein Wachstum ohne den Beta-Hebel). Bestätigt: der „Gewinn" ist Exposure, kein Alpha.

### Stream 12 — Overfitting-Gatekeeper (die Beweislast)
**26 Hypothesen als *eine* Multiple-Testing-Familie.** Erwartete Falsch-Positive bei roh p<0,05: **1,3**. Beobachtet: 5. **Benjamini-Hochberg (FDR 5 %): 0 bestehen.** **Überlebende (BH ∧ positiv auf *beiden* Hold-outs): 0.** Mehrere „signifikante" IS-Zellen **kippen out-of-sample negativ** (XBI-Momentum<0: IS +2,24 % → OOS −9,99 %; Mcap 300–500M: +15,5 % → −7,6 %). Lehrbuch-Overfitting.

---

## Rangliste (nach Signifikanz → Reproduzierbarkeit → Robustheit → Handelbarkeit → Nettorendite)

| Rang | „Kandidat" | Signifikanz (korrigiert) | Repliziert Hold-out? | Handelbar? | Netto n. Kosten | Urteil |
|---|---|---|---|---|---|---|
| 1 | Illiquide Micro-Caps (ADV<3M) | roh t=1,95, BH ✗ | teils positiv | ❌ Spreads 1,5–3,5 %/Seite | **Median −2,4 bis −5,1 %** | **Verworfen** (Artefakte + unüberwindbare Kosten) |
| 2 | ML-Logistic-Selektion | Perm-p=0,095 ✗ | schwach | teils | +0,32 % netto (n.s.) | **Verworfen** (nicht signifikant, regime-getrieben, 4/5 Modelle ranken rückwärts) |
| 3 | Regime „schwache XBI-Phase" | t=2,76 roh, BH ✗ | ❌ kippt −4,6 % | ✅ | — | **Verworfen** (kollinear, single-tape, Vorzeichen kippt) |
| 4 | Steigende Zinsen | t=2,46 roh, BH ✗ | ❌ verliert Signif. | ✅ | — | **Verworfen** (Outcome-Mix-Konfundierung) |
| 5 | Mcap 300–500 Mio. | t=2,0 roh, BH ✗ | ❌ −7,6 % | ✅ | — | **Verworfen** (n=13, kippt OOS) |
| — | Basis-Strategie (long, T-30→T-7) | t=1,47, n.s. | — | ✅ | ~Beta | **Kein Alpha** |

**Kein Kandidat überlebt.** Die Rangliste ist eine Liste des Scheiterns, geordnet danach, *wie knapp* jeder scheitert.

---

## Fazit

**Existiert eine ausnutzbare Überrendite gegenüber XBI? Nach allem, was mit realen, frei verfügbaren Daten testbar ist: nein.**

- Der rohe Run-up ist real, aber **Sektor-Beta** — unkonditioniert und in jeder getesteten Konditionierung ist der XBI-Excess statistisch nicht von null zu trennen, sobald man Multiple Testing und Hold-out ehrlich anwendet.
- Der einzige Winkel mit durchgehend positivem Brutto-Excess (illiquide Micro-Caps) ist **nach echten Spreads netto negativ** und teils Datenartefakt.
- Kein Timing, kein Market-Cap-Bucket, kein Regime, kein ML-Modell liefert repliziertes, kosten-robustes Alpha.
- **Falls Alpha existierte, müsste das exakte Regelwerk hier stehen. Es gibt keines** — jede Regel, die man aus 2025 destilliert, kehrt sich 2026/2022–23 um.

**Wo eine Edge *noch* verborgen sein könnte (ehrlich offen, nicht widerlegt):** in den 5 nicht testbaren Streams — v. a. **Short-Interest-Dynamik** (Squeeze-Potenzial), **Optionspreis-Signale** (IV-Rank, Gamma) und **Insider-/Secondary-Timing**. Diese erfordern kostenpflichtige *historische Punkt-in-Zeit*-Daten. Ohne die kann ihre Existenz weder bestätigt noch widerlegt werden — die Beweislast liegt bei der Strategie.

**Institutionelles Urteil:** Als Long-only-Katalysator-Strategie ist Pre-PDUFA-Run-up **kein handelbares Alpha, sondern teuer verpacktes Biotech-Beta.** Wer das Beta will, kauft XBI (billiger, liquider, kein −80 %-CRL-Gap-Tail, kein Ruin-Risiko). Weiterforschen lohnt nur mit (a) kostenpflichtigen SI-/Options-/Fundamentaldaten und (b) einem **beta-neutralen** Design (long Name / short XBI), das isoliert, ob *überhaupt* Rest-Alpha existiert — die vorliegenden Zahlen sagen: kaum.

---

## Grenzen & Reproduktion

- **Zeitraum:** In-Sample 2025, Hold-outs 2026 + 2022–23. 2026 ist eine einzige Marktphase (limitiert Regime-Validierung); 2022–23 handelbar klein (n≈13). Ein voller 2010–2024-Zyklus mit ex-ante-PDUFA-Kalendern war frei nicht rekonstruierbar (Paywall/egress-blockiert). „Kein Alpha" ist damit *innerhalb der testbaren Evidenz* gezeigt, nicht als Unmöglichkeitsbeweis über alle denkbaren Daten.
- **Market-Cap/Float:** aktueller Proxy, nicht punktgenau historisch.
- Alle Zufallszahlen fix geseedet. Streams:
```
python3 src/build_features.py        # gemeinsamer point-in-time Feature-Datensatz
python3 src/gatekeeper.py            # 26 Hypothesen, BH-FDR, Hold-out (Stream 12)
python3 src/montecarlo.py            # 100k Pfade (Stream 11)
# Discovery-Agents: output/agents/{mktcap,timing,regime,liquidity,ml}.{json,md}
```
Nur reale historische Daten. Keine erfundenen Kurse, Termine oder Kennzahlen.
