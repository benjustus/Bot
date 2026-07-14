```yaml
agent: 07
klasse: "Secondary Offerings / Net Share Issuance"
websuche_verfuegbar: ja
strategien:
  - name: "SEO Event-Study Langfrist-Underperformance (Buy-and-Hold, 3-5 Jahre nach Emission)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 1
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "~0.0 (statistisch nicht von Null unterscheidbar nach Kalenderzeit-Korrektur)"
    kernrisiko: "Methodenartefakt: naive Buy-and-Hold-Abnormal-Return-Tests sind statistisch invalide (Mitchell & Stafford 2000); Effekt verschwindet in Kalenderzeit-3-Faktor-Regressionen und ist nicht von Size-/BM-Faktorexposure unterscheidbar (Brav, Geczy & Gompers 2000)."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
  - name: "Net Share Issuance (NSI) – Cross-sectional Signal, monatlich rebalanciert"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 3
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.45
    netto_sharpe_erwartung: "0.15-0.30 long-short institutionell; nach Crowding/Borrow-Kosten eher unteres Ende"
    kernrisiko: "Alpha schrumpft auf Grenzsignifikanz nach Risikoadjustierung mit Investment-Faktor (Hou/Xue/Zhang 2020: q-Faktor-Alpha t=-1.85 vs. Rohspanne t=-3.16); rational-erklärbar via q-Theorie (Li/Livdan/Zhang 2009), nicht eindeutig Mispricing; Short-Bein konzentriert in schwer/teuer leihbaren Small-/Microcap-Emittenten."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Open Source Asset Pricing (Chen & Zimmermann, openassetpricing.com) Portfolio-Returns 'NetEquityFinance'/'ChNetIssue' (kostenlos); kein exaktes Ken-French-Pendant, CMA-Faktor (FF5) nur grobe Proxy"
  - name: "Composite Equity Issuance (CEI) – Intangible-Return-Signal"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 3
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.4
    netto_sharpe_erwartung: "0.10-0.30"
    kernrisiko: "Hohe Korrelation mit NSI und Asset Growth (gemeinsame Ladung auf Stambaugh-Yuan MGMT-Mispricing-Cluster) -> kaum inkrementelle Diversifikation zu Candidate 2 und zu bereits verbreiteten Quality/Investment-Faktoren; behaviorale 'Overreaction-to-Intangible-Information'-Interpretation konkurriert mit rationaler q-Theorie-Erklärung."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Open Source Asset Pricing (Chen & Zimmermann) Portfolio-Returns 'CompEquIss' (kostenlos)"
```

# Agent 07 – Anomalieklasse: Secondary Offerings / Net Share Issuance

## Executive Summary

Die Klasse "Aktienemissionen / Verwässerung" ist akademisch eine der am besten dokumentierten Anomalien überhaupt – aber mit deutlichem Bruch zwischen der ursprünglichen, spektakulären Ereignisstudien-Literatur der 1990er (Kandidat 1) und der saubereren, aber deutlich schwächeren Cross-Sectional-Faktor-Literatur (Kandidaten 2 und 3). Mein Urteil nach adversarialer Prüfung:

- **Kandidat 1 (SEO-Langfrist-Underperformance, Event-Study):** **KILL.** Der ursprüngliche Effekt (Loughran & Ritter 1995; Spiess & Affleck-Graves 1995) ist ein methodisches Artefakt langfristiger Buy-and-Hold-Tests. Mitchell & Stafford (2000) zeigen, dass die verwendeten t-Statistiken wegen Querschnittskorrelation überlappender Event-Fenster ungültig sind; Brav, Geczy & Gompers (2000) zeigen, dass der Effekt in einer sauberen Kalenderzeit-3-Faktor-Regression verschwindet und nicht von bekannter Size-/Value-Faktorexposure zu unterscheiden ist.
- **Kandidat 2 (Net Share Issuance, Pontiff & Woodgate 2008 / Fama & French 2008):** **WEAK.** Real, robust über Size-Gruppen und international repliziert, aber die Interpretation als Mispricing ist fragil: Hou/Xue/Zhang (2020) zeigen, dass nach Risikoadjustierung mit einem Investment-Faktor die Signifikanz auf Grenzniveau (t≈-1.85) fällt, und Li/Livdan/Zhang (2009) liefern eine vollständig rationale q-Theorie-Erklärung ohne Mispricing.
- **Kandidat 3 (Composite Equity Issuance, Daniel & Titman 2006):** **WEAK.** Ähnliches Profil wie Kandidat 2, stark korreliert mit diesem und mit Asset Growth (gemeinsamer Stambaugh-Yuan "MGMT"-Mispricing-Cluster) – wenig inkrementeller Wert für ein Portfolio, das bereits Quality-/Investment-Faktoren hält.

Keiner der drei Kandidaten erfüllt die Doppelbedingung für CANDIDATE (dokumentierte Post-Publication-Persistenz **und** Kostenrobustheit). Die ökonomisch reinste Formulierung der Klasse (NSI/CEI) ist eher ein "Grenzfall-Faktor", der in modernen Multi-Faktor-Modellen weitgehend vom Investment-/Quality-Faktor absorbiert wird – kein eigenständiges, klar handelbares Alpha mehr.

**Evidenzbasis:** Websuche war in dieser Session funktionsfähig und wurde für alle Kernaussagen genutzt (siehe Quellenverzeichnis). Einzelne quantitative Detailwerte (v.a. exakte Pontiff-Woodgate-Regressionskoeffizienten aus dem Volltext hinter der Wiley-Paywall) konnten nicht direkt verifiziert werden; diese sind explizit als "aus Sekundärquellen/Erinnerung, nicht volltext-verifiziert" gekennzeichnet.

---

## Kandidat 1: SEO Event-Study Langfrist-Underperformance
**(Loughran & Ritter 1995 "The New Issues Puzzle"; Spiess & Affleck-Graves 1995 "Underperformance in Long-Run Stock Returns Following Seasoned Equity Offerings")**

### a) Ökonomische Begründung
Behavioral-Timing-These: Manager verfügen über bessere Informationen über den fundamentalen Wert ihrer Firma als der Markt und emittieren opportunistisch Aktien, wenn die Firma überbewertet ist ("windows of opportunity"). Investoren extrapolieren naiv die jüngste positive operative/Kurs-Performance vor der Emission (Overextrapolation-Bias) und unterschätzen systematisch die Signalwirkung der Emissionsentscheidung selbst. Verursacher der Fehlbewertung: retail-lastige, sentimentgetriebene Käufer der Neuemission plus Analysten mit strukturell zu optimistischen Wachstumsschätzungen für frisch emittierende Wachstumsfirmen.

### b) Limits to Arbitrage
Lange Haltedauer (3-5 Jahre) bindet Kapital und Risikobudget; Shortpositionen in Emittenten sind wegen Borrow-Kosten, Squeeze-Risiko und der Notwendigkeit, über Jahre gegen einen möglichen fortgesetzten positiven Sentiment-Trend zu halten, teuer; Idiosynkratisches Risiko bei kleinen Wachstumsfirmen ist hoch und schreckt risikoaverse Arbitrageure ab (klassisches Shleifer-Vishny-Argument).

### c) Originalstudie(n)
- **Loughran & Ritter (1995), Journal of Finance, Stichprobe 1970-1990 (US-IPOs und -SEOs).** Kernergebnis: Über 5 Jahre nach der Emission erzielen SEO-Firmen eine durchschnittliche Jahresrendite von nur ~7% p.a. (IPO-Firmen ~5% p.a.), verglichen mit deutlich höheren Renditen size-gematchter Nicht-Emittenten; ein Investor hätte ~44% mehr Kapital in Emittenten investieren müssen, um nach 5 Jahren dasselbe Endvermögen wie mit Nicht-Emittenten zu erzielen ("wealth relative" < 1). Buch-Marktwert-Effekte erklären laut den Autoren nur einen kleinen Teil des Effekts.
- **Spiess & Affleck-Graves (1995), Journal of Financial Economics, Stichprobe 1975-1989 (US-SEOs).** Medianrendite von SEO-Firmen über 5 Jahre ~10% vs. ~42.3% für size-/branchengematchte Nicht-Emittenten – eine der größten dokumentierten Lücken in der Anomalie-Literatur überhaupt. Robust gegenüber Handelssystem, Emissionsgröße, Firmenalter und Buch-Marktwert-Kontrolle (im Rahmen der damaligen Methodik).

### d) Out-of-Sample-/Post-Publication-Evidenz
Dies ist der entscheidende Schwachpunkt: Die Folgeliteratur hat den Effekt nicht bestätigt, sondern methodisch zerlegt:
- **Brav, Geczy & Gompers (2000, JFE), "Is the Abnormal Return Following Equity Issuances Anomalous?"**: Underperformance konzentriert sich fast ausschließlich auf kleine Emittenten mit niedrigem Buch-Marktwert-Verhältnis. Die Zeitreihenrenditen der "underperformierenden" SEO-Firmen kovariieren fast vollständig mit Faktorrenditen, die aus Nicht-Emittenten konstruiert wurden. Im Kalenderzeit-3-Faktor-Modell (Markt, Size, B/M) verschwindet die Anomalie – der Effekt ist keine eigenständige Emissions-Anomalie, sondern ein Artefakt der Size-/Value-Faktorexposure junger Wachstumsfirmen.
- **Mitchell & Stafford (2000)**: Zeigen allgemein für Langfrist-Ereignisstudien, dass überlappende Event-Firmen-Renditen im Kalenderzeitraum querschnittlich positiv korreliert sind; die in L&R/Spiess-Affleck-Graves verwendeten Standardfehler unterschätzen daher die wahre Varianz massiv, was die berichteten t-Statistiken ungültig macht.
- **Eckbo, Masulis & Norli (2000), "Seasoned Public Offerings: Resolution of the 'New Issues Puzzle'"**: Liefern eine rationale Risiko-Erklärung – Emittenten reduzieren durch die Kapitalerhöhung ihren Leverage und ihr systematisches Risiko, wodurch niedrigere erwartete Renditen nach der Emission ökonomisch konsistent (nicht anomal) sind.
- **Barber & Lyon (1997) / Lyon, Barber & Tsai (1999), Kothari & Warner**: Dokumentieren drei generische Verzerrungen in BHAR-Langfriststudien (New-Listing-Bias, Rebalancing-Bias, Skewness-Bias), die unabhängig vom SEO-Kontext zu falsch-positiven Ergebnissen führen.

Decay-Schätzung: Nicht sinnvoll quantifizierbar als "%", weil der Effekt in korrekt spezifizierten Tests bereits im Ursprungszeitraum nicht robust signifikant von Null verschieden ist – es handelt sich nicht um Decay eines echten Effekts, sondern um Nichtreplikation aufgrund von Fehlspezifikation.

### e) Kosten
Turnover niedrig (Halteperiode 3-5 Jahre), aber die Positionsgröße pro Titel ist klein (viele kleine SEO-Emittenten), was Marktzugangskosten und Rebalancing-Aufwand bei fortlaufendem Eventfluss erhöht. Da der Effekt ohnehin nicht robust nachweisbar ist, sind Netto-Kostenschätzungen akademisch nicht sinnvoll – jede Bruttorendite ist bereits zweifelhaft.

### f) Kapazität und Handelbarkeit
Sehr eingeschränkt: SEO-Emittenten sind überproportional Small-/Microcaps; volle Umsetzung (Long Nicht-Emittenten, Short Emittenten über 5 Jahre) erfordert kontinuierliches Event-Sourcing (SDC Platinum/Refinitiv – kostenpflichtig) und laufendes Rebalancing eines Portfolios mit Hunderten kleiner Illiquide Positionen. Geschätzte Kapazität < USD 100-200 Mio. bei institutioneller Umsetzung, bevor Market Impact dominiert.

### g) Regimeabhängigkeit und Tail-Risiko
SEO-Volumen ist prozyklisch – Emissionsfenster schließen sich in Stressphasen (2008/09, März 2020), sodass gerade in Crashphasen kaum neue Long-Signale (Nicht-Emittenten) und die bestehenden Short-Positionen (Emittenten) zusätzlichem Squeeze-Risiko durch Flucht in Qualität/Erholungsrallyes ausgesetzt sind. Erzwungene ("distressed") Kapitalerhöhungen (z.B. Bankenrekapitalisierungen 2008/09) verhalten sich fundamental anders als opportunistische Wachstumsemissionen und verwässern das Signal zusätzlich.

### h) Bekannte Kritik/Widerlegungen
Siehe (d): Brav/Geczy/Gompers 2000 und Mitchell/Stafford 2000 sind direkte, im Kern vernichtende methodische Widerlegungen. Zusätzlich: Selection-Bias in den Originalstichproben (nur erfolgreich abgeschlossene, in CRSP/Compustat sauber verlinkbare Emissionen; kleine, teils handkuratierte Samples der 1990er-Jahre-Ära).

### Urteil: **KILL**
Als eigenständige, handelbare Ereignisstrategie ist dieser Kandidat widerlegt. Er überlebt nur als Beschreibung eines Size-/Value-/Leverage-Faktor-Zusammenhangs, der bereits durch Standardfaktoren abgedeckt ist.

---

## Kandidat 2: Net Share Issuance (NSI) – Cross-Sectional Signal
**(Pontiff & Woodgate 2008 "Share Issuance and Cross-Sectional Returns"; Fama & French 2008 "Dissecting Anomalies"; international: McLean, Pontiff & Watanabe 2009)**

### a) Ökonomische Begründung
Behavioral/strukturell gemischt: (i) Behavioral – Investoren reagieren zu langsam/unvollständig auf das Signal des Netto-Aktienangebots als Proxy für Managementeinschätzung der Überbewertung; (ii) strukturell – Indexfonds und passive Vehikel müssen bei Aktienemissionen mechanisch Aktien nachkaufen (unabhängig vom Preis), was kurzfristigen Kaufdruck erzeugt, der sich mittelfristig umkehrt; (iii) rationale Alternative (siehe d): Netto-Emission korreliert mechanisch mit Investitionsausgaben – Firmen mit hohem Investment haben laut q-Theorie niedrigere erwartete Renditen (kein Mispricing nötig).

### b) Limits to Arbitrage
Die stärkste Ausprägung des Signals liegt bei kleinen/mittleren Emittenten mit erhöhten Leihkosten und Squeeze-Risiko auf der Short-Seite; institutionelle Halter (die für den Verkaufsdruck/die Emissionsabwicklung nötig sind) agieren oft mit langem Horizont und Index-Constraints, sodass kurzfristige Preisineffizienz nicht sofort geschlossen wird.

### c) Originalstudie(n)
- **Pontiff & Woodgate (2008), Journal of Finance.** Zeigen für US-Aktien (NYSE/AMEX ab ~1970, NASDAQ-Teilstichprobe ab den 1980ern), dass Aktienemission (log-Veränderung der ausstehenden, split-bereinigten Aktienzahl) eine "starke Fähigkeit hat, Renditen im Querschnitt vorherzusagen" – laut Originalabstract statistisch signifikanter als die individuelle Vorhersagekraft von Size, Buch-Marktwert oder Momentum. *(Hinweis: exakte Koeffizienten/t-Statistiken der Fama-MacBeth-Regressionen konnten über die frei zugängliche Websuche nicht aus dem Volltext verifiziert werden – Wiley-Paywall; Sekundärquellen bestätigen jedoch die qualitative Kernaussage der überlegenen statistischen Signifikanz.)*
- **Fama & French (2008), Journal of Finance, "Dissecting Anomalies", Stichprobe 1963-2005, breite US-Aktien.** Net Stock Issues zeigen anomale Renditen, die – anders als z.B. Asset Growth (nur Microcaps) – **in allen Size-Gruppen** (Micro, Small, Big) sowohl in Sortierungen als auch in Cross-Section-Regressionen auftreten. Dies ist der stärkste Robustheitsnachweis des Signals und unterscheidet es positiv von vielen anderen "Zoo"-Anomalien.
- **McLean, Pontiff & Watanabe (2009), Journal of Financial Economics, 41-Länder-Stichprobe.** Emission sagt Renditen außerhalb der USA vorher, mit statistischer Signifikanz vergleichbar mit Buch-Marktwert und stärker als Size/Momentum; robust in kleinen und großen Firmen. Wichtig: außerhalb der USA wird der Effekt stärker von negativen Renditen nach Aktienschaffung als von positiven Renditen nach Rückkäufen getrieben, und die Stärke steigt mit Emissionsaktivität, Marktentwicklung und Anlegerschutz des jeweiligen Landes.

### d) Out-of-Sample-/Post-Publication-Evidenz
- **Hou, Xue & Zhang (2020), Review of Financial Studies, "Replicating Anomalies"**: Für den eng verwandten Composite-Equity-Issuance-Sort (Cei, siehe Kandidat 3, methodisch nahezu identisch zu NSI) beträgt die rohe High-minus-Low-Dezilrendite -0.56%/Monat (t = -3.16), die q-Faktor-Alpha (inkl. Investmentfaktor) jedoch nur noch -0.24%/Monat (t = -1.85) – **Grenzsignifikanz**. Die Autoren zeigen explizit, dass der Investmentfaktor der Haupttreiber der verbleibenden Erklärungskraft ist, d.h. ein Großteil dessen, was als "Issuance-Anomalie" firmiert, ist eigentlich Investment-/Asset-Growth-Exposure.
- **Li, Livdan & Zhang (2009), Review of Financial Studies, "Anomalies"**: Ein reines q-Theorie-Investitionsmodell (ohne jegliches Mispricing) reproduziert qualitativ und quantitativ prozyklische Emissionswellen, die negative Investment-Rendite-Beziehung, die Langfrist-Underperformance nach Emissionen und den positiven Drift nach Ausschüttungen. Dies ist eine vollständige rationale Alternativerklärung zur Behavioral-These.
- **McLean & Pontiff (2016), Journal of Finance**: Über 97 publizierte Renditeprädiktoren hinweg sinken Portfolio-Renditen im Schnitt um 26% out-of-sample (obere Schranke für Data-Mining) und um 58% post-Publikation (davon ~32 Prozentpunkte durch publikationsinduzierten Arbitragehandel zurechenbar). *Wichtiger Hinweis zur Präzision:* Eine anomalie-spezifische Zahl für "Net Share Issuance" konnte über die Websuche nicht isoliert verifiziert werden; die 26%/58%-Zahlen sind Stichprobendurchschnitte über alle 97 Prädiktoren, nicht spezifisch für NSI. Es wäre spekulativ, sie 1:1 auf NSI zu übertragen – als Orientierungsgröße aber plausibel, da NSI/Issuance ein bekannter, viel zitierter Prädiktor mit hoher öffentlicher Sichtbarkeit seit den 1990ern ist (also eher überdurchschnittlicher Decay zu erwarten).
- **Stambaugh & Yuan (2017), Review of Financial Studies, "Mispricing Factors"**: Net Share Issuance und Composite Issuance sind zwei von elf Anomalien, die im "MGMT"-Mispricing-Cluster (gemeinsam mit Asset Growth, Accruals, Net Operating Assets) zusammengefasst werden – das bedeutet hohe Kovarianz mit bereits breit gehandelten Multi-Anomalie-Faktoren, was für Crowding-Risiko spricht.
- **Stambaugh, Yu & Yuan (2012), JFE, "The Short of It: Investor Sentiment and Anomalies"**: Anomalierenditen (inkl. issuance-artiger Signale) sind nach Phasen hohen Investorsentiments deutlich stärker, und zwar **spezifisch getrieben durch das Short-Bein**, während das Long-Bein keine Sentiment-Abhängigkeit zeigt. Konsistent mit der Story, dass Überbewertung wegen Shortsale-Beschränkungen nicht sofort wegarbitriert wird – aber auch ein Hinweis, dass die Profitabilität der Strategie regimeabhängig und auf die am schwersten leihbaren Titel konzentriert ist.

Netto-Einschätzung Decay: Substanziell – von "hoch signifikant und ökonomisch groß" in den Originalstudien zu "statistisch grenzwertig" nach moderner Risikoadjustierung (HXZ). Größenordnung des Rückgangs der risikoadjustierten Signifikanz: t-Statistik fällt um ca. 40% (von t≈-3.2 roh auf t≈-1.85 risikobereinigt, konkret am CEI-Beispiel gezeigt).

### e) Kosten
Niedriger Turnover (Signal basiert auf Jahresdaten/Aktienzahl-Änderungen, typischerweise jährlich/quartalsweise aktualisiert) – laut **Novy-Marx & Velikov (2016), RFS, "A Taxonomy of Anomalies and Their Trading Costs"** erzielen die meisten Anomalien mit <50% monatlichem Turnover signifikante Netto-Spreads nach Kostenoptimierung (Buy/Hold-Spread-Technik); Ausführungskosten für mittel-turnover Anomalien liegen bei 20-57 Basispunkten. NSI dürfte in diese "eher kostenrobuste" Kategorie fallen – **aber** dies gilt für Standard-TAQ-basierte Spread-/Impact-Schätzungen und berücksichtigt nicht die tatsächlichen Leihkosten für die konzentriert kleinkapitalisierten Short-Ziele, die in Stresszeiten stark steigen können.

### f) Kapazität und Handelbarkeit
Moderat. Long-Bein (Vermeiden/Untergewichten von Emittenten, Übergewichten von Rückkäufern) ist gut handelbar und in praktisch unbegrenzter Kapazität als Tilt implementierbar. Short-Bein ist der Flaschenhals: konzentriert in kleineren/mittleren Emittenten mit periodisch angespanntem Borrow-Markt (insbesondere kurz nach SEO-Ankündigung, siehe Safieddine & Wilhelm 1996, Henry & Koski 2010 zu Short-Selling-Regulierung rund um SEOs, SEC Rule 105). Geschätzte Kapazität eines dedizierten Long-Short-Programms: **USD 300 Mio. – 1 Mrd.**, primär limitiert durch Leihbarkeit/Liquidität des Short-Buchs, nicht durch das Long-Buch.

### g) Regimeabhängigkeit und Tail-Risiko
Sentiment-abhängig (Stambaugh/Yu/Yuan 2012): Strategie ist am profitabelsten nach Hochsentiment-Phasen (Blasenbildung), aber genau dann trägt das Short-Bein das größte Squeeze-/Crash-Risiko (Short-Overpriced-Growth-Stocks ist strukturell verwandt mit dem Momentum-Crash-Muster von Daniel & Moskowitz 2016 sowie den Meme-Stock-Short-Squeezes 2021, die überproportional stark emittierende Small-Caps trafen). Negative Skewness auf der Short-Seite ist ein reales Tail-Risiko-Merkmal dieser Klasse.

### h) Bekannte Kritik/Widerlegungen
Konfundierung mit Investmentfaktor (HXZ 2020); rationale q-Theorie-Alternative (Li/Livdan/Zhang 2009) reduziert Vertrauen in "echtes Mispricing"; hohe Kovarianz mit bereits etablierten Multi-Anomalie-Composite-Faktoren (Stambaugh & Yuan 2017) spricht für Crowding und geringe inkrementelle Diversifikation für einen Fonds, der bereits Quality-/Investment-Faktoren hält.

### Urteil: **WEAK**
Real und international repliziert, aber nach moderner Risikoadjustierung grenzwertig signifikant, teils rational erklärbar, und praktisch stark durch die Short-Bein-Kostenstruktur begrenzt.

---

## Kandidat 3: Composite Equity Issuance (CEI)
**(Daniel & Titman 2006, "Market Reactions to Tangible and Intangible Information")**

### a) Ökonomische Begründung
Behavioral: Daniel & Titman zerlegen die Aktienrendite in eine "tangible" (fundamentalbasierte) und eine "intangible" Komponente. CEI misst die Gesamtheit der Eigenkapitalfinanzierungsaktivität (SEOs, aktienbasierte Akquisitionen erhöhen CEI; Rückkäufe/Dividenden senken CEI) relativ zur Marktkapitalisierungsveränderung, die nicht durch thesaurierte Gewinne erklärt wird. These: Investoren legen zu viel Gewicht auf den "intangible"-Anteil vergangener Renditen (der stark mit CEI korreliert) und überreagieren, was zu Overpricing bei Hoch-CEI-Firmen und nachfolgender Korrektur führt.

### b) Limits to Arbitrage
Analog zu Kandidat 2 – zusätzlich erschwert durch die Komplexität des Signals selbst (kombiniert mehrere Bilanz-/Marktwert-Komponenten), was die praktische Nachbildung außerhalb akademischer Datenbanken (Compustat/CRSP) erschwert und Modellrisiko bei der exakten Signalkonstruktion einführt.

### c) Originalstudie(n)
**Daniel & Titman (2006), Journal of Finance.** Firmen mit hoher CEI zeigen in der Folge signifikant schlechtere Renditen; die intangible Return-Komponente ist stark negativ mit zukünftigen Renditen assoziiert, während sie unkorreliert mit vergangener Rechnungslegungs-Performance ist – dies wird als Beleg für Überreaktion auf "weiche" Informationen (M&A-Ankündigungen, Aktienemissionen) interpretiert statt auf harte Fundamentaldaten.

### d) Out-of-Sample-/Post-Publication-Evidenz
- **Hou, Xue & Zhang (2020)**: Wie oben – Cei-Dezilspread roh -0.56%/Monat (t=-3.16), q-Faktor-Alpha nur -0.24%/Monat (t=-1.85). Damit ist CEI der direkt am gründlichsten aus 2020er-Sicht getestete der drei Kandidaten, und das Ergebnis ist ernüchternd: signifikant in Rohform, grenzwertig nach moderner Risikoadjustierung.
- **Stambaugh & Yuan (2017)**: CEI ist Teil desselben "MGMT"-Clusters wie NSI – hohe Kovarianz, geringe inkrementelle Information gegenüber Kandidat 2.
- **Aktuelle Kritik (2024), "Why isn't composite equity issuance favored by the stock market? A risk-based explanation for the anomaly" (ScienceDirect/Int. Review of Financial Analysis)**: Existenz einer neueren (2024) Arbeit, die explizit eine risikobasierte (nicht-behaviorale) Erklärung für die CEI-Anomalie vorschlägt – ein weiteres Indiz, dass die akademische Debatte 2015-2026 in Richtung "eher Risikofaktor als reines Mispricing" tendiert, nicht in Richtung Bestätigung robusten Alphas. *(Titel/Kernthese aus Suchergebnis verifiziert, Volltext-Effektgrößen nicht abrufbar.)*

### e) Kosten
Wie Kandidat 2 – niedriger Turnover, daher tendenziell in Novy-Marx & Velikovs "kostenrobuster" Kategorie, mit denselben Einschränkungen bezüglich Short-Leihkosten.

### f) Kapazität und Handelbarkeit
Vergleichbar mit Kandidat 2, tendenziell noch etwas geringer, da die Signalkonstruktion granularere/seltener aktualisierte Bilanzdaten erfordert und die praktische Portfolioüberlappung mit NSI hoch ist (faktisch dasselbe Exposure mit anderer Gewichtung). Geschätzte eigenständige Zusatzkapazität über ein bestehendes NSI-Buch hinaus: gering.

### g) Regimeabhängigkeit und Tail-Risiko
Im Wesentlichen identisch zu Kandidat 2 (hohe Korrelation der Signale, gemeinsamer Cluster).

### h) Bekannte Kritik/Widerlegungen
Siehe (d). Zusätzlich: Weil CEI M&A-getriebene Aktienemissionen (Stock-Deals) explizit einschließt, ist das Signal in Phasen hoher M&A-Aktivität (späte Bullenmärkte) besonders "voll", was prozyklisches Crowding-Risiko mit Kandidat 1 (SEO-Fenster) und dem generellen Marktzyklus teilt.

### Urteil: **WEAK**
Eigenständig kaum zusätzlicher Wert gegenüber Kandidat 2; dieselben Kernschwächen (Investment-Faktor-Konfundierung, Grenzsignifikanz nach Risikoadjustierung, aufkommende risikobasierte Gegenerklärungen).

---

## Klassenweites Gesamturteil

Die Nullhypothese ("kein echtes Alpha in dieser Klasse") lässt sich **nicht vollständig verwerfen, aber auch nicht überzeugend zurückweisen**. Ergebnis einer dreistufigen Betrachtung:

1. Die historisch größte und "verkäuflichste" Version der Anomalie (Langfrist-SEO-Underperformance als Ereignisstrategie) ist methodisch widerlegt und sollte als Klasse **nicht** gehandelt werden (KILL).
2. Die saubereren, cross-sektional/monatlich rebalancierten Versionen (Net Share Issuance, Composite Equity Issuance) sind akademisch die robustesten Vertreter der gesamten "Anomalie-Zoo"-Literatur – sie überleben Fama & French (2008) Size-Sortierungen und internationale Replikation (McLean/Pontiff/Watanabe 2009) besser als die meisten anderen 300+ publizierten Prädiktoren. Das ist ein echtes Pluspunkt gegenüber vielen anderen Klassen.
3. Aber: Sobald man mit einem modernen Multi-Faktor-Modell (q-Faktor, Hou/Xue/Zhang 2020) risikoadjustiert, schrumpft die Signifikanz auf Grenzniveau (t≈-1.85), es existiert eine vollständige rationale Alternativerklärung (Li/Livdan/Zhang 2009 q-Theorie sowie Eckbo/Masulis/Norli 2000 Risikoreduktion), und das Signal ist stark mit bereits weit verbreiteten Multi-Anomalie-Composite-Faktoren korreliert (Stambaugh & Yuan 2017 MGMT-Cluster) – ein klares Crowding-Signal.

**Fazit für einen institutionellen Allokator:** Diese Klasse verdient keinen dedizierten Sleeve mit signifikantem Risikobudget. Als **Tilt/Overlay** innerhalb eines bestehenden Quality-/Investment-Faktor-Portfolios (Long: Nicht-Emittenten/Rückkäufer, kein separates Short-Buch) ist ein kleiner positiver Erwartungswert plausibel (p≈0.4-0.45 für "reale, aber grenzwertige Ineffizienz"), aber die inkrementelle risikoadjustierte Rendite über bereits gehaltene Standardfaktoren hinaus dürfte nahe Null liegen. Ein eigenständiges Long-Short-Programm ist wegen Short-Bein-Kosten, Crowding und Konfundierung mit Investment-Risiko nicht zu empfehlen.

---

## Quellenverzeichnis (mit Verifikationsstatus über Websuche, Juli 2026)

- Loughran, T. & Ritter, J. (1995). "The New Issues Puzzle." *Journal of Finance* 50(1), 23-51. — Kernzahlen (7%/5% p.a., 44% Wealth-Relative-Lücke) via Websuche verifiziert.
- Spiess, D.K. & Affleck-Graves, J. (1995). "Underperformance in Long-Run Stock Returns Following Seasoned Equity Offerings." *JFE* 38(3). — Median-10%-vs-42.3%-Zahl via Websuche verifiziert.
- Brav, A., Geczy, C. & Gompers, P. (2000). "Is the Abnormal Return Following Equity Issuances Anomalous?" *JFE* 56(2), 209-249. — Kernaussage (3-Faktor-Modell absorbiert Effekt) via Websuche verifiziert.
- Mitchell, M. & Stafford, E. (2000). Methodenkritik Langfrist-Ereignisstudien. — Kernaussage via Websuche verifiziert.
- Eckbo, B.E., Masulis, R. & Norli, Ø. (2000). "Seasoned Public Offerings: Resolution of the 'New Issues Puzzle'." *JFE*. — Existenz/Titel via Websuche bestätigt, Risiko-Argument aus Fachkenntnis ergänzt.
- Pontiff, J. & Woodgate, A. (2008). "Share Issuance and Cross-Sectional Returns." *Journal of Finance* 63(2), 921-945. — Qualitative Kernaussage via Websuche (Abstract) verifiziert; exakte t-Statistiken nicht volltextverifiziert (Paywall).
- Fama, E.F. & French, K.R. (2008). "Dissecting Anomalies." *Journal of Finance* 63(4), 1653-1678. — Robustheit über Size-Gruppen via Websuche verifiziert.
- McLean, R.D., Pontiff, J. & Watanabe, A. (2009). "Share Issuance and Cross-Sectional Returns: International Evidence." *JFE* 94(1), 1-17. — Kernaussagen via Websuche verifiziert.
- Daniel, K. & Titman, S. (2006). "Market Reactions to Tangible and Intangible Information." *Journal of Finance* 61(4), 1605-1643. — Kernkonzept CEI via Websuche verifiziert.
- Li, E.X.N., Livdan, D. & Zhang, L. (2009). "Anomalies." *Review of Financial Studies* 22(11), 4301-4334. — q-Theorie-Erklärung via Websuche verifiziert.
- Hou, K., Xue, C. & Zhang, L. (2020). "Replicating Anomalies." *Review of Financial Studies* 33(5), 2019-2133. — Cei-Zahlen (-0.56%, t=-3.16 roh; -0.24%, t=-1.85 q-Faktor) via Websuche direkt verifiziert.
- McLean, R.D. & Pontiff, J. (2016). "Does Academic Research Destroy Stock Return Predictability?" *Journal of Finance* 71(1), 5-32. — 26%/58%-Decay-Zahlen (Stichprobendurchschnitt über 97 Prädiktoren) via Websuche verifiziert; NICHT anomalie-spezifisch für NSI verifizierbar.
- Novy-Marx, R. & Velikov, M. (2016). "A Taxonomy of Anomalies and Their Trading Costs." *Review of Financial Studies* 29(1), 104-147. — Kostenspannen (20-57bp) und Turnover-Kostenrobustheits-Aussage via Websuche verifiziert.
- Stambaugh, R.F., Yu, J. & Yuan, Y. (2012). "The Short of It: Investor Sentiment and Anomalies." *JFE* 104(2), 288-302. — Sentiment-/Short-Bein-Ergebnis via Websuche verifiziert.
- Stambaugh, R.F. & Yuan, Y. (2017). "Mispricing Factors." *Review of Financial Studies* 30(4), 1270-1315. — MGMT-Cluster-Zusammensetzung (inkl. Net Share Issuance und Composite Issuance) via Websuche verifiziert.
- Chen, A.Y. & Zimmermann, T. "Open Source Cross-Sectional Asset Pricing." *Critical Finance Review*, sowie openassetpricing.com. — Existenz/Umfang (319 Charakteristika, 98% Replikationsrate bei t>1.96) via Websuche verifiziert; exakte Feldnamen "NetEquityFinance"/"CompEquIss" aus Fachkenntnis, nicht einzeln volltextverifiziert.
- Safieddine, A. & Wilhelm, W. (1996); Henry, T. & Koski, J. (2010). Short-Selling rund um SEOs, SEC Rule 105. — Kernaussagen via Websuche verifiziert.
- ATM-Offering-Strukturwandel (SEC-Reform 2008, geringere Discount-Magnitude ~1.5-3% vs. ~7% bei traditionellen Follow-ons). — Via Websuche verifiziert (Stand ~2012-Daten).
- Aktuelle (2024) risikobasierte CEI-Gegenerklärung (ScienceDirect/Int. Review of Financial Analysis). — Titel/Existenz via Websuche verifiziert, Effektgrößen nicht abrufbar.
