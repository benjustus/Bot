# Quant-Research-Audit: Pre-PDUFA-Run-up-Strategie

**Unabhängige Prüfung, Erweiterung und Widerlegung/Bestätigung**
Stand: 13. Juli 2026 · Rolle: unabhängiger Quant-Researcher (nicht Verkaufsberater)
Kursdaten: Yahoo Finance v8 (split-/dividendenbereinigt) · Termine/Outcomes: pdufa.bio, drugs.com, Firmen-PR
Reproduzierbar: gesamte Pipeline in `src/`, alle Zahlen aus `python3 src/run_all.py` → `output/results.json`

---

## Ergebnis in drei Sätzen

Es gibt einen **kleinen, real messbaren rohen Run-up** von ca. **+3,4 %** über das Fenster −30 → −7 Tage — aber auf **431 verifizierten Events** (statt 16) ist dieser fast vollständig **Biotech-Sektor-Beta (XBI)**: der beta-bereinigte Überschuss beträgt nur **+1,0 %, ist statistisch nicht von null unterscheidbar** (t = 1,1–1,5, 95 %-KI enthält null, Trefferquote ≈ 50 %, Median ≈ 0 %). In genau dem Bullen-Sample, in dem die Strategie am besten aussieht, hätte **schlichtes Halten des XBI-Index +76,5 % gebracht — mehr als der All-in-Median der Strategie (+49 %) und bei halbem Drawdown und ohne Einzelaktien-Gap-Risiko.**

**→ Eine robuste, ausbeutbare Pre-PDUFA-Edge existiert nach dieser Analyse nicht.** Das rohe Muster ist Sektor-Beta, das man über XBI billiger und risikoärmer bekommt. Details und alle Vorbehalte unten.

---

## 1 · Audit des vorhandenen Backtests

Ich habe die 16 Original-Trades **unabhängig und exakt reproduziert** (eigener Yahoo-Abruf, eigene Engine). Ergebnis vorweg: **Die Rechnung des Originals ist korrekt — der Fehler liegt nicht in der Mathematik, sondern in den Daten.**

### 1.1 Was rechnerisch stimmt (exakt reproduziert)

| Kennzahl | Original | Meine Reproduktion | Diff |
|---|---|---|---|
| Ø Rendite/Trade (A) | +7,31 % | +7,31 % | < 0,005 pp |
| Median | +8,64 % | +8,64 % | 0 |
| Trefferquote | 68,75 % | 68,8 % | 0 |
| Profit Factor | 4,10 | 4,10 | 0 |
| Std/Trade | 11,46 % | 11,46 % | 0 |
| Endkapital o. FB | 2.082 € | 2.082 € | 0 € |
| Endkapital m. FB | 2.397 € | 2.398 € | 1 € (Rundung) |
| Kapital-Drawdown | −24,8 % | −24,8 % | 0 |

Alle 16 Einzelrenditen stimmen auf < 0,01 pp. Die Steuerlogik (26,375 %, Verlustverrechnungstopf, Sparerpauschbetrag) ist **korrekt umgesetzt** — z. B. GERN: Gewinn 288,48 € − Verlusttopf 158,35 € = 130,13 € steuerpflichtig × 26,375 % = 34,32 € ✓. **Kein Rechenfehler gefunden.**

### 1.2 Die eigentlichen Schwächen (methodisch, nicht rechnerisch)

**(a) Selection/Survivorship-Bias — der schwerste Punkt.** Das Original räumt selbst ein, 7 übernommene Firmen (RETA, PRVB, MRTX, SAGE, DAWN, APLS, KRTX) rausgelassen zu haben. Das ist genau der Bias, der die Strategie schönrechnet: übernommene Biotechs sind überproportional **Gewinner** (man wird zum Aufpreis gekauft, weil das Medikament wertvoll ist). Zusätzlich sind **alle 16 Events dem Autor bekannte, überwiegend zugelassene Medikamente** — d. h. mit Rückschau-Wissen ausgewählt. CRLs (Ablehnungen) fehlen komplett. In meinem großen Sample (s. u.) laufen eventuelle CRLs **genauso stark** hoch wie Zulassungen — der Run-up trennt Gewinner und Verlierer **nicht**.

**(b) Fehlende Beta-Adjustierung (Look-Ahead-nahe Verzerrung durch Regime).** Das Original misst nur **rohe** Renditen. 2023–2025 war ein starker Biotech-Zeitraum (XBI). Wer irgendeine Biotech-Aktie 23 Tage hielt, verdiente im Schnitt Geld — unabhängig von PDUFA. Die +7,31 % sind zu einem großen Teil **Sektor-Beta**, keine PDUFA-spezifische Alpha-Quelle. Das Original hat diese Konfundierung nicht kontrolliert.

**(c) Stichprobe viel zu klein (n = 16, Kette n = 12).** Ein bis zwei Events dominieren jede Kennzahl. Der Sign-Test auf den 16 Roh-Renditen ergibt **p = 0,21** — d. h. selbst der rohe Effekt ist bei n = 16 **nicht signifikant**. Sharpe/CAGR sind bei dieser Größe nicht belastbar.

**(d) Event-Kontamination.** Bei 4/16 fiel der FDA-Entscheid vor den geplanten Ausstieg — die Prämisse „nie durchs Event halten" ist real verletzt. (Vom Autor korrekt geflaggt.)

**(e) Regime-Blindheit.** Das Sample liegt zufällig im Biotech-Bullenmarkt. pdufa.bio's eigene Studie über **1.754 Events** zeigt: der Run-up (T-120→T-1) war **+12,9 % (2020), aber −5,1 % (2022) und −3,8 % (2023)**. Ein 2022er-Sample hätte die Strategie widerlegt. Das Original hat den Regime-Charakter nicht getestet.

**(f) All-in-Positionierung = Ruin-Risiko (unterschätzt).** Bei 16 handverlesenen Namen kam kein Totalschaden vor. Im großen Sample tritt er auf (s. Kapitalsimulation: −55 % Drawdown real).

**Fazit Audit:** Zahlen korrekt, Schlussfolgerung nicht tragfähig. Die drei fehlenden Kontrollen — **große unverzerrte Stichprobe, Beta-Adjustierung, Regime-/Outcome-Split** — sind genau das, was die vermeintliche Edge auflöst.

---

## 2 · Datenbasis-Erweiterung: was ehrlich möglich war

Das Ziel „≥ 100 Events, idealerweise 2010–heute, nur echte Daten" ist mit **frei/erreichbaren** Quellen nur teilweise erreichbar. Ich lege offen, was ging und was nicht:

| Quelle | Status in dieser Umgebung | Nutzung |
|---|---|---|
| Yahoo Finance v8 (Kurse) | ✅ erreichbar, echte adj. Tages-OHLC | Alle Kurse. Reproduziert Original exakt. |
| pdufa.bio `/decisions` | ✅ direkt abrufbar, server-gerendert, **deterministisch geparst** | **445 Events 2025–2026 mit Outcome (Approved/CRL)** |
| drugs.com Zulassungs-Archiv | ✅ erreichbar (Zulassungsdaten, nur Approvals) | **53er Regime-Kohorte 2022–2023** |
| pdufa.bio `/runup-by-year` | ✅ (aggregierte Fremdstudie, 1.754 Events 2020+) | Externe Regime-Referenz |
| Web-Archiv (historische PDUFA-Kalender) | ❌ **egress-blockiert** | — (hätte 2014–2024 ex-ante Kalender geliefert) |
| BiopharmaWatch / BioPharmCatalyst Vollhistorie | ❌ Paywall (6 von 6.738 Zeilen frei) | — |
| Stooq (delisted-Kurse) | ❌ Anti-Bot-Challenge | — |
| Yahoo quoteSummary (hist. Aktienzahl) | ❌ nur *aktuelle* Marktkap. (Crumb-Flow) | Market-Cap-Tier als **Näherung** |

**Ergebnis-Datenbasis (alles real, nichts geschätzt/erfunden):**

- **Kohorte P — pdufa.bio 2025–2026:** 445 Events, davon **431 mit Kursen (97 %)**, **326 Approved / 119 CRL**. Das ist das **saubere Kern-Sample: dual-outcome (inkl. Verlierer), PDUFA-datiert.** 28× größer als das Original und ohne dessen Gewinner-Selektion.
- **Kohorte O — Original 16** (2023–2025), exakt repliziert (Audit-Referenz).
- **Kohorte G — Regime 2022–2023:** 53 Events aus drugs.com-Zulassungen, kleine/mittlere Biotechs, jeder Ticker per Yahoo-Firmenname validiert. **33 mit Kursen.** *Nur Zulassungen* → Gewinner-verzerrt (der optimistische Fall).

**Wichtige Ehrlichkeits-Kennzeichnung zur Datenqualität (neu gefunden, im Original nicht adressiert):**

1. **pdufa.bio-Confidence-Tags.** Nur ~20 Events sind „source-verified"; 318 sind „price-only" (algorithmisch aus Kursmuster erschlossen). Darunter **False Positives**: z. B. **RNAZ (TransCode)** — eine präklinische Firma **ohne zugelassenes Medikament und ohne echten PDUFA** — taucht mit zwei „PDUFA"-Events und ±100 %-Sprüngen auf (Pump/Reverse-Split-Rauschen). Solche Nano-Cap-Ausreißer trieben in der Rohauswertung den Mittelwert des `<500 Mio.`-Tiers (Median dort nur +1,5 %!). **→ Ich führe deshalb konsequent einen „handelbaren" Filter (Kurs ≥ 2 $, Marktkap. ≥ 100 Mio.) und werte zusätzlich nur „source-verified" aus.**
2. **„Delisting" ≠ real.** In dieser Umgebung liefert der Yahoo-Spiegel für manche **eindeutig noch gelistete** Titel (FOLD/Amicus, MRNS/Marinus) „Not Found". „Nicht verfügbar" mischt also echte Übernahmen und Feed-Lücken — ich behaupte daher **nirgends** ein reales Delisting, sondern nur „im Feed nicht verfügbar". Für Kohorte P (97 % Abdeckung) ist das irrelevant; für 2022–2023 (37 % fehlend) ist es ein echter Vorbehalt.

---

## 3 · Reproduzierbarer Backtest — Timing-Varianten (Kohorte P, n = 431)

Konvention wie Original: Einstieg = letzter Handelsschluss ≤ (PDUFA − x Kalendertage), Ausstieg analog; Renditen auf adj. Close. **Zusätzlich zur rohen Rendite die entscheidende beta-bereinigte „Excess"-Rendite (Rendite minus XBI über dasselbe Fenster).**

| Variante | roh Ø | roh Median | roh Hit | roh t | **Excess Ø** | **Excess Hit** | **Excess t** | Excess 95 %-KI |
|---|---|---|---|---|---|---|---|---|
| **A** −30→−7 | +3,38 % | +2,24 % | 60,8 % | +3,7 | **+0,96 %** | 49,7 % | **+1,1** | [−0,7 %, +2,8 %] |
| **B** −45→−7 | +4,10 % | +3,65 % | 60,1 % | +3,8 | **+0,81 %** | 50,3 % | **+0,8** | [−1,3 %, +2,9 %] |
| **C** −30→−3 | +3,56 % | +2,13 % | 59,9 % | +3,8 | **+0,68 %** | 49,2 % | **+0,8** | [−1,1 %, +2,5 %] |
| **D** −21→−7 | +2,09 % | +1,22 % | 57,1 % | +3,1 | **+0,44 %** | 49,9 % | **+0,7** | [−0,8 %, +1,7 %] |

**Lesart:** In **jeder** Variante ist die **rohe** Rendite signifikant positiv (t > 3) — aber die **beta-bereinigte** Rendite ist in **jeder** Variante **~0–1 % und nicht signifikant** (KI enthält null, Excess-Trefferquote ≈ 50 %, Excess-Median ≈ 0). Das rohe Signal ist Sektor-Beta.

Nach Datenqualitäts-Subsets (Variante A):

| Subset | n | roh Ø (t) | **Excess Ø (t)** | Excess Median | Excess Hit |
|---|---|---|---|---|---|
| Full (inkl. Nano-Cap-Rauschen) | 431 | +3,38 % (3,7) | +0,96 % (1,1) | −0,17 % | 49,7 % |
| **Handelbar** (≥ 2 $, ≥ 100 Mio.) | 379 | +3,58 % (5,0) | **+1,04 % (1,5)** | +0,04 % | 50,4 % |
| Source-verified (klein!) | 19 | +8,32 % (1,3) | +7,73 % (1,3) | +3,77 % | 68,4 % |
| Handelbar & verifiziert-nah | 277 | +4,42 % (5,0) | +1,67 % (2,0)* | +0,04 % | 50,5 % |

\* Der einzige „grenzwertig signifikante" Excess (t = 1,98) liegt exakt an der 5 %-Schwelle und würde eine **Mehrfachtest-Korrektur** (4 Varianten × mehrere Subsets) nicht überstehen. Das 19er-source-verified-Sample sieht besser aus, ist aber mit KI [−3 %, +20 %] wertlos für eine Signifikanzaussage — und selbst potenziell selektiert (pdufa.bio verifiziert eher auffällige Katalysatoren).

---

## 4 · Kapitalsimulation (1.500 €, All-in, Roll-over, deutsche Steuer)

Modell: volles Kapital pro Trade, 2 € Gebühr/Trade, 26,375 % Abgeltungsteuer mit Verlustverrechnungstopf, optional Sparerpauschbetrag (1.000 €/Jahr ab 2023), überlappende Termine übersprungen. **Der entscheidende Unterschied zum Original ist die unverzerrte, große Trade-Menge.**

| Szenario | Kette | Endkapital | Max-DD | Bemerkung |
|---|---|---|---|---|
| **Original 16 (repliziert)** | 12 | **2.082 € / 2.398 €** | −24,8 % | Handverlesene Gewinner |
| **Kohorte P handelbar — greedy-Kette** | 22 | **1.377 €** (−8,2 %) | **−54,9 %** | Ein realer Pfad: verliert Geld |
| Kohorte P handelbar — Monte-Carlo (3.000 Ziehungen) | ~22 | Median **2.242 €** | Tail bis −60 % | 5 %-Perzentil 1.143 €, Min 598 € |

**Monte-Carlo-Risikoprofil (handelbar, All-in):** Median +49 %, aber **P(Verlust) = 18 %**, P(< 1.000 €) = 2 %, schlimmster Pfad −60 %. Der positive Median ist **kein Alpha, sondern Beta** — Beweis:

> **Passives Halten im selben Zeitraum (2024-12-31 → 2026-06-30):**
> **XBI +76,5 %** (Max-DD −26,3 %) · IBB +44,3 % · S&P 500 +27,5 %.

Der Biotech-Index **XBI (+76,5 %)** schlug den All-in-Median der Strategie (+49 %) deutlich — bei **halbem Drawdown und ohne Einzelaktien-Gap-Risiko**. Die Strategie hat in ihrem besten Regime **den Index unterboten**. (Vorbehalt: Die Strategie ist zeitweise in Cash, XBI voll investiert — aber genau das misst die Excess-Rendite pro Trade, die ≈ 0 ist. Beide Metriken sagen dasselbe: kein Mehrwert.)

---

## 5 · Zusätzliche Filter

### 5.1 FDA-Outcome (Approved vs. CRL) — direkte Antwort auf „war vor dem Termin ein Unterschied erkennbar?"

| Gruppe | n | roh Ø | roh Median | Excess Ø | Excess Hit |
|---|---|---|---|---|---|
| Eventuell **Approved** | 317 | +2,84 % | +2,31 % | +0,60 % | 49,8 % |
| Eventuell **CRL** | 114 | **+4,87 %** | +2,15 % | +1,97 % | 49,1 % |

**Klares Ergebnis: Nein.** Die später **abgelehnten** Titel (CRL) liefen im Fenster −30→−7 **stärker** hoch als die später zugelassenen. Der Pre-PDUFA-Run-up enthält **keine Vorabinformation** über den Ausgang — man kann ihn **nicht** nutzen, um dem CRL-Absturz auszuweichen. Das widerlegt jede „Smart-Money-weiß-es-vorher"-Erzählung.

**Gap-Risiko (warum −7 d aussteigen):** Hält man durch den Entscheid (−7 d → +3 d): Approved +0,73 % (schlimmster −54 %), **CRL −6,90 % (schlimmster −80 %)**, alle −1,29 %. Durchhalten hat **negativen** Erwartungswert mit −80 %-Tail. Der Ausstieg schützt — lässt aber nur das ~Null-Excess-Beta übrig.

### 5.2 Market Cap (aktueller Wert als Näherung — Vorbehalt: keine punktgenaue historische Aktienzahl)

| Tier | n | roh Ø | roh Median | Excess Ø (t) |
|---|---|---|---|---|
| < 500 Mio. | 65 | +7,58 % | **+1,51 %** | +5,74 % (1,5) |
| 500 Mio.–2 Mrd. | 41 | +1,43 % | +0,40 % | +0,23 % (0,1) |
| 2–10 Mrd. | 71 | +4,90 % | +4,27 % | +1,59 % (1,2) |
| > 10 Mrd. | 147 | +2,29 % | +1,81 % | −0,14 % (−0,2) |

Der Effekt konzentriert sich nominell in **Nano-/Micro-Caps (< 500 Mio.)**, aber: **Mittelwert +7,6 % vs. Median +1,5 %** → von wenigen extremen (teils Daten-artefakt-verdächtigen, illiquiden) Ausreißern getrieben, **nicht signifikant** (t = 1,5). Bei > 10 Mrd. (Big Pharma) ist der Excess **null** — erwartungsgemäß, da ein Medikament den Konzern kaum bewegt. **Interpretation:** „Edge" = Lotterieschein-Verhalten illiquider Kleinstwerte, kein verlässlicher, handelbarer Vorteil.

### 5.3 Marktumfeld / Regime

**(a) Innerhalb Kohorte P** (XBI-Trend 63 Tage, aber alles 2025–2026 → begrenzte Bandbreite): bear-Fenster Excess +2,40 %, bull +0,19 %, seitwärts +0,59 % — alle nicht signifikant, kein klares Muster (echte Struktur-Bärenmärkte fehlen im Sample).

**(b) Eigene Regime-Kohorte 2022–2023** (drugs.com, *nur Zulassungen = Gewinner-verzerrt = optimistischer Fall*, n = 33): roh **+2,40 %, Median +0,07 %, Hit 51,5 %, t = 0,92** — **nicht signifikant, Median praktisch null.** Aufgeschlüsselt: **2022 roh +1,53 %, Median −0,11 %, Hit 50 %** (praktisch flach); 2023 +3,05 %. Selbst im gewinner-verzerrten Optimalfall **keine Edge** im schwächeren Regime.

**(c) Externe Referenz** (pdufa.bio, 1.754 Events, T-120→T-1): **2020 +12,9 %, 2021 +7,3 %, 2022 −5,1 %, 2023 −3,8 %, 2024 +12,6 %, 2025 +13,0 %.** Der Run-up ist **stark regimeabhängig und in Bärenjahren negativ.** Das Original-Sample (2023–2025) fing zufällig überwiegend die Erholung.

**Fazit Regime:** Der Run-up ist **kein stabiles Phänomen, sondern Konjunktur des Sektors.** Er verstärkt sich im Bullenmarkt (weil = Beta) und **kehrt sich im Bärenmarkt um**.

### 5.4 Review-Typ (Priority/Standard) und Short Interest — ehrlich: **nicht belastbar verfügbar**

- **Review-Typ:** In keiner frei erreichbaren Quelle maschinell und flächendeckend vorhanden. Eine punktuelle Zuordnung wäre selektiv und nicht reproduzierbar → **nicht ausgewertet, als Datenlücke gekennzeichnet** (statt zu raten).
- **Short Interest (historisch):** Frei nicht flächendeckend verfügbar (Bi-Monats-Daten hinter Datenanbietern). **Nicht auswertbar — Datenlücke.** (Das Original hatte dasselbe Problem und hat es korrekt offengelassen.)

Diese zwei Filter kann ich mit den vorhandenen Mitteln **nicht wissenschaftlich sauber** liefern; ich erfinde dafür keine Werte.

---

## 6 · Statistik (Kohorte P, Variante A, handelbar n = 379, sofern nicht anders)

| Kennzahl | roh | **Excess (über XBI)** |
|---|---|---|
| Durchschnitt | +3,58 % | **+1,04 %** |
| Median | +2,68 % | **+0,04 %** |
| Trefferquote | 63,1 % | **50,4 %** |
| Profit Factor | 2,24 | ~1,1 |
| Std/Trade | 18,8 % | 18,3 % |
| Sharpe/Trade (rf = 0) | 0,19 | ~0,06 |
| Sortino/Trade | ~0,28 | ~0,08 |
| Erwartungswert/Trade | +3,58 % | **+1,04 %** |
| t-Statistik (vs. 0) | +5,03 | **+1,53** |
| 95 %-KI (Bootstrap, 10 k) | [+2,2 %, +5,0 %] | **[−0,3 %, +2,4 %]** |
| Sign-Test p | < 0,001 | **≈ 0,9 (n. s.)** |

**Signifikanz-Kernaussage:** Roh signifikant (t = 5), Excess **nicht** (t = 1,5, KI enthält null, Sign-Test nicht signifikant). **Vorbehalt zur Unabhängigkeit:** Events überlappen zeitlich und teilen Biotech-Beta; naive t-Tests **überschätzen** die Signifikanz. Die Excess-Berechnung entfernt das gemeinsame Beta teilweise — dass selbst dann die KI null enthält, macht die „Kein-Edge"-Aussage **robuster**, nicht schwächer.

---

## 7 · Robustheit

**(a) Timing ±5 Tage** (Ø roh / Ø Excess %):

| Einstieg\Ausstieg | −2 d | −7 d | −12 d |
|---|---|---|---|
| −25 d | +2,5 / −0,1 | +2,8 / +0,6 | +2,1 / +0,7 |
| −30 d | +3,2 / +0,3 | +3,4 / +1,0 | +2,6 / +1,0 |
| −35 d | +3,5 / +0,3 | +3,7 / +1,0 | +3,0 / +1,1 |
| −45 d | +4,0 / +0,2 | +4,1 / +0,8 | +3,3 / +0,9 |

Roh stabil positiv, **Excess über alle 12 Kombinationen −0,1 % bis +1,1 %** — durchweg klein und insignifikant. Das Ergebnis ist **nicht** ein Timing-Zufall; es ist robust *klein*.

**(b) Gebühren/Slippage/FX** (Ø roh/Trade, Basis +3,38 %):
- + Slippage 0,5 %/Seite → **+2,35 %** (−1,0 pp)
- + Slippage 1,5 %/Seite (realistisch für illiquide Small/Nano-Caps) → **+0,33 %** (−3,1 pp) — **rohes Signal praktisch weg**
- + USD/EUR (EUR-denominiert, echte EURUSD-Kurse) → +2,89 % (−0,5 pp), zusätzliche Streuung
- Gebühren verdoppeln (4 €/Trade): bei 1.500 € Kapital vernachlässigbar (~0,13 pp/Trade), bei Micro-Positionen relevanter.

**Da die einzige nominelle „Edge" in illiquiden < 500-Mio.-Namen sitzt, wo Slippage real > 1 %/Seite ist, frisst die Reibung genau dort das Roh-Signal auf.** Nach Beta-Adjustierung **und** Reibung bleibt nichts Handelbares.

---

## 8 · Fazit — die Kernfragen

**Existiert statistisch eine Pre-PDUFA-Edge?**
Ein **rohes** Run-up-Muster (~+3,4 %/Trade) existiert und ist auf 431 Events statistisch klar (t = 5). Eine **PDUFA-spezifische Edge** existiert **nicht belastbar**: beta-bereinigt +1,0 % (t = 1,1–1,5, KI enthält null, Median ≈ 0, Trefferquote ≈ 50 %). Der einzige grenzwertig-signifikante Wert (t ≈ 2 in einem Subset) überlebt keine Mehrfachtest-Korrektur.

**Wie groß ist sie wirklich?** Als *Punktschätzung* +1 % bis best-case +1,7 % beta-bereinigt/Trade — **ununterscheidbar von null** und **kleiner als realistische Transaktionskosten** in den einzigen Namen, wo sie überhaupt auftritt.

**Ist sie robust?** Nein. Sie ist (i) fast reines Sektor-Beta, (ii) **regimeabhängig** (in 2022–2023 flach bis negativ), (iii) auf illiquide Micro-Caps und wenige Ausreißer konzentriert, (iv) durch Slippage/FX aufgezehrt, (v) durch das CRL-Gap-Tail (−80 %) asymmetrisch nach unten.

**Was verstärkt sie (scheinbar)?** Bullenmarkt (= mehr Beta), Nähe zum Event halten (= mehr Event-/Beta-Exposure, nicht mehr Alpha), Micro-Caps (= mehr Ausreißer-Varianz), Gewinner-/Survivorship-Selektion, kleine Stichprobe.

**Was zerstört sie?** Beta-Adjustierung, große unverzerrte Stichprobe, Bären-/Seitwärtsmarkt, Transaktionskosten, Einbezug der CRLs, ehrliche Datenqualität (Nano-Cap-Filter).

**Wie sähe eine möglichst saubere Strategie aus?** Ehrlich: **Auf Basis dieser Evidenz gibt es keine wissenschaftlich tragfähige Long-Run-up-Strategie.** Das rohe Signal ist Biotech-Beta — das bekommt man über **XBI** direkt (+76,5 % im Sample, halber Drawdown, keine Gap-Gefahr). Falls man dennoch forschen will, wäre der einzig defensible Rahmen: **(1)** beta-neutral (long Einzelname / short XBI, um zu prüfen, ob überhaupt Rest-Alpha existiert — meine Zahlen sagen: kaum); **(2)** **fixe** kleine Positionsgröße (≤ 1–2 % je Trade), **niemals** All-in (Ruin-Tail); **(3)** harter Ausstieg vor dem Event (Gap-Schutz); **(4)** Ausschluss illiquider Nano-Caps und Reverse-Split-Namen; **(5)** Test über **≥ ein volles Bären-/Bullen-Zyklus** (2010–2026), nicht ein Regime. Vorhersage nach dieser Analyse: Auch das liefert netto keinen robusten, kostennach-positiven Vorteil.

---

## Grenzen dieser Analyse (explizit)

- **Zeitliche Konzentration:** Das saubere, dual-outcome-Kern-Sample ist **2025–2026** (Bullen-Regime). 2022–2023 nur als kleinere, gewinner-verzerrte Zulassungs-Kohorte + externe pdufa.bio-Referenz. Ein voll gleichwertiges, unverzerrtes 2010–2024-Sample war mit frei erreichbaren Quellen **nicht** rekonstruierbar (ex-ante-PDUFA-Kalender sind Paywall/egress-blockiert).
- **Market-Cap-Tier** = *aktueller* Wert als Näherung (keine punktgenaue historische Aktienzahl frei verfügbar).
- **Review-Typ & Short Interest:** Datenlücke, bewusst **nicht** geschätzt.
- **PDUFA-Datum ±wenige Tage** (v. a. „price-only"-Events): unsicher, aber durch die ±5-Tage-Robustheit abgedeckt.
- **Feed-Abdeckung:** „nicht verfügbar" ≠ nachgewiesenes Delisting.
- **Keine Anlageberatung.** Historische Muster sagen nichts über die Zukunft.

## Reproduktion

```bash
python3 src/parse_pdufa_bio.py       # PDUFA-Events aus gespeichertem HTML → CSV
python3 src/fetch_all_prices.py      # Yahoo-Kurse (gecacht in data/prices/)
python3 src/fetch_marketcap.py       # Market-Cap-Näherung
python3 src/run_all.py               # ALLE Kennzahlen → output/results.json
```

Datenquellen mit Abrufdatum in `data/raw/`. Kurse split-/dividendenbereinigt (Yahoo v8). Alle Zufallszahlen mit festem Seed.
