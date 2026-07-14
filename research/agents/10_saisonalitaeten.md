```yaml
agent: 10
klasse: "Saisonalitäten"
websuche_verfuegbar: ja
strategien:
  - name: "Turn-of-the-Month (TOM) Effekt"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 3
      regimestabilitaet: 2
      handelbarkeit: 4
      kapazitaet: 3
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0.0-0.2 in entwickelten Märkten nach Kosten; ggf. 0.2-0.4 in ausgewählten Schwellenländern vor Kapazitätsgrenzen"
    kernrisiko: "Effekt in liquiden Industrieländer-Märkten bereits weitgehend arbitriert/verschwunden (Decay auf ~0 in US-ETFs seit ca. 2015); Fensterspezifikation (-1 bis +3 Handelstage) selbst Ergebnis von Data-Mining über viele getestete Fensterlängen"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Daily Factors (Mkt-RF, Tagesfrequenz) + Yahoo-Finance-Tagesdaten SPY/IWM/internationale ETFs"
  - name: "Cross-sektionale Kalendersaisonalität (Heston-Sadka 'Own-Month'-Effekt)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 4
      regimestabilitaet: 3
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.45
    netto_sharpe_erwartung: "0.1-0.3 brutto; keine dokumentierte Netto-Sharpe nach realistischen Kosten auffindbar, Unsicherheit hoch"
    kernrisiko: "Konzentration in Small-/Micro-Caps mit Leerverkaufsbeschränkungen; monatlicher Vollrebalance der gesamten Cross-Section treibt Turnover/Kosten stark; kein etabliertes Risikomodell erklärt den Effekt -> Restunsicherheit ob doch Kompensation für unbeobachtetes Risiko statt reiner Ineffizienz"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French 25 Size-BM- bzw. 10 Momentum-Portfolios (monatlich, seit 1926) als Näherung; für echte Einzeltitel-Replikation WRDS/CRSP nötig (nicht frei)"
  - name: "Halloween-Effekt / Sell-in-May (Bouman & Jacobsen)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 3
      regimestabilitaet: 2
      handelbarkeit: 5
      kapazitaet: 5
      kostenrobustheit: 4
    p_echte_ineffizienz: 0.3
    netto_sharpe_erwartung: "0.0-0.2 langfristig gepoolt international; in mehreren Einzelmärkten 2014-2025 negativ ggü. Buy-and-Hold"
    kernrisiko: "Strategie verzichtet 6 Monate auf Aktienrisikoprämie -> hohe Opportunitätskosten in strukturellen Bullenphasen (genau das ist seit ca. 2012 eingetreten); Pfadabhängigkeit: einzelne 'falsche' Sommer-Rally oder Winter-Crash kann Mehrjahresvorsprung auslöschen"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Mkt-RF (US, monatlich) + MSCI-Länderindizes via Yahoo Finance für internationale Tests"
```

# Anomalieklasse: Saisonalitäten — Adversarial Review

**Researcher:** unabhängiger Quant-Researcher, Mandat Saisonalitäten
**Stand:** Juli 2026
**Nullhypothese:** Es gibt kein echtes, nach Kosten handelbares Alpha in Kalender-/Saisonalitätsregeln. Diese Nullhypothese wird nicht verworfen, außer die Evidenz ist stark genug, um Sullivan/Timmermann/White (2001) explizit zu widerlegen.

---

## 0. Methodisches Vorwort: Warum diese Klasse besonders anfällig für Data-Mining ist

Kalenderanomalien sind das Lehrbuchbeispiel für Multiple-Testing-Verzerrung. Es gibt nur 12 Monate, ~252 Handelstage, 5 Wochentage, ~10 Feiertage im Jahr — ein extrem kleiner, diskreter Hypothesenraum, der von Forschern seit über 100 Jahren systematisch durchsucht wird ("harvesting"). Sullivan, Timmermann & White (2001, *Journal of Econometrics*, "Dangers of Data-Driven Inference: The Case of Calendar Effects in Stock Returns") ist hier die zentrale Referenz meines gesamten Mandats: Sie wenden White's Reality-Check-Bootstrap auf den DJIA (1897–1996) an und zeigen, dass einzeln betrachtete Kalenderregeln (Turn-of-Month, Januar, Wochenende, Feiertage) signifikant *erscheinen* — sobald man aber korrekt für die Größe des tatsächlich durchsuchten Regelraums (Tausende plausible Kalenderfilter) korrigiert, verliert selbst die beste gefundene Regel ihre statistische Signifikanz im Out-of-Sample-Test. Das ist die Messlatte, an der jeder Kandidat in diesem Bericht gemessen wird.

Zusätzlich gilt für die gesamte Klasse die allgemeine Anomalie-Decay-Evidenz von McLean & Pontiff (2016, *Journal of Finance*): Über ~97 publizierte Renditeanomalien hinweg sinkt die Effektgröße im Schnitt um ca. 58% zwischen In-Sample- und Post-Sample-Zeitraum und nochmals zusätzlich nach Publikation (konsistent mit Lernen/Arbitrage durch Marktteilnehmer, nicht mit reinem Statistical-Fluke-Reversal). Saisonalitäten sind von dieser Publikationsdecay nicht ausgenommen — im Gegenteil, sie sind maximal einfach zu implementieren (kein komplexes Signal, nur ein Kalenderdatum), was schnelle Arbitrage begünstigt.

Ich habe daher initial ~8 Kalendereffekte geprüft und explizit auf 3 Kandidaten reduziert, die (a) über Jahrzehnte/Jahrhunderte und mehrere unabhängige Länder-Stichproben reproduziert wurden und (b) eine nicht-triviale ökonomische Begründung jenseits von "es ist halt so" haben.

---

## 1. Turn-of-the-Month (TOM) Effekt

### a) Ökonomische Begründung
Ogden (1990, *Journal of Finance*, "Turn-of-Month Evaluations of Liquid Profits and Stock Returns: A Common Explanation for the Monthly and January Effects") liefert die Standard-Flow-Erklärung: Löhne, Gehälter, Dividenden, Zinszahlungen und Pensionsbeiträge sind in den USA und den meisten Industrieländern kalendarisch standardisiert und konzentrieren sich auf das Monatsende/den Monatsanfang. Institutionelle Investoren (insb. Pensionsfonds) reinvestieren diesen Cash-Zufluss systematisch in den ersten Handelstagen des neuen Monats, was einen kurzfristigen Kaufdruck (Price Pressure) erzeugt. Ergänzend: "Dash for Cash" (Etula et al., *Review of Financial Studies* 2020) zeigt, dass Pensionskassen und andere institutionelle Investoren am Monatsende systematisch Liquidität benötigen bzw. bereitstellen, was TOM-Muster in Fixed Income und Aktien gleichermaßen erklärt.

### b) Limits to Arbitrage
Der Effekt ist ein reiner Timing-/Beta-Trade (keine Stock-Picking-Komponente, keine Shortseite nötig) und damit für institutionelle Arbitrageure extrem billig zu handeln — das ist zugleich der Grund, warum er in liquiden Märkten kaum überlebt haben sollte. Verbleibende Reste erklären sich am ehesten dadurch, dass die Flows selbst preisunelastisch sind (Pensionsfonds re-investieren nicht opportunistisch, sondern nach fixen Kalenderregeln/Statuten) — ein struktureller, aber sehr kleiner Rest-Effekt.

### c) Originalstudien
- Ariel (1987, *Journal of Financial Economics*): NYSE/AMEX 1963–1981 — praktisch die gesamte positive Marktrendite fällt auf den letzten Handelstag des Monats plus die erste Monatshälfte.
- **Lakonishok & Smidt (1988, *Review of Financial Studies*, "Are Seasonal Anomalies Real? A Ninety-Year Perspective")** — die methodisch wichtigste Studie der Klasse, weil 90 Jahre Dow-Jones-Daten (1897–1986) verwendet werden, was die übliche "Kurzstichprobe → Zufallsfund"-Kritik entschärft. Sie finden, dass das 4-Tage-Fenster um den Monatswechsel (letzter Handelstag + erste 3 Tage) die Rendite des gesamten Monats trägt, während die übrigen Tage im Schnitt nahe Null liegen — über 90 Jahre hinweg konsistent positiv und statistisch signifikant.
- Internationale Replikation: McConnell & Xu (2008, *Financial Analysts Journal*) sowie eine aktuelle Studie über 30 Aktienmärkte (~90% der globalen Marktkapitalisierung), Zeitraum 1994–2023, bestätigen erhöhte Renditen am letzten Handelstag plus den ersten drei Handelstagen des Folgemonats.

### d) Out-of-Sample-/Post-Publication-Evidenz und Decay
Dies ist der entscheidende Schwachpunkt: Aktuelle Analysen (2023–2025) zeigen einen deutlichen Decay in entwickelten Märkten. Für das klassische enge 4-Tage-Fenster gilt inzwischen laut jüngerer Auswertung von US-ETFs (SPY/QQQ/IWM): "keine der Differenzen ist mehr statistisch signifikant" — QQQ etwa zeigte in den frühen 2000ern einen starken TOM-Effekt, der seither schrittweise auf Null gesunken ist, teils sogar mit inversem Vorzeichen. Nur bei einem breiteren 7-Tage-Fenster (Tag −3 bis +3) bleiben noch 5–12 Basispunkte in US-Märkten messbar, in einzelnen Schwellenländern (Brasilien: ~23 Basispunkte) deutlich mehr. Fazit: **geschätzter Decay in entwickelten Märkten grob 70–100% relativ zur Originalgröße** (von signifikant robust auf statistisch nicht mehr abgrenzbar von Null im engen Fenster); internationale/EM-Reste bestehen, korrelieren aber vermutlich mit geringerer Liquidität/höheren impliziten Kosten dort.

### e) Kosten
Bei einer angenommenen Transaktionskostenbelastung von nur 5 Basispunkten pro Trade kollabiert die Netto-Performance: US-TOM-Strategien auf SPY/QQQ/IWM zeigen "einen deutlichen Rückgang der CAGR und generell niedrigere oder vergleichbare Sharpe Ratios" gegenüber Buy-and-Hold. Bei zwei Trades pro Monat (24/Jahr) ist der Turnover moderat, aber die verbleibende Bruttoedge (5–12bp) liegt in der gleichen Größenordnung wie realistische Round-Trip-Kosten (Spread + Market Impact) selbst in liquiden ETFs — die Strategie ist damit strukturell kostenmarginal.

### f) Kapazität
Hoch in Dollar-Volumen (S&P-500-Futures/ETFs sind extrem liquide), aber niedrig in Alpha-Dollar, weil die Bruttoedge selbst schon nahe der Kostenschwelle liegt. Eine Studie zu Calendar-Anomalien in S&P-500-Futures bestätigt: TOM ist "der einzige Kalendereffekt, der statistisch UND ökonomisch signifikant und über die Zeit persistent ist" — allerdings bezieht sich das primär auf ältere Stichproben; die aktuelle Decay-Evidenz relativiert das für die letzten 10 Jahre.

### g) Regimeabhängigkeit und Tail-Risiko
Der Effekt ist an strukturelle institutionelle Flow-Muster gebunden (Gehaltszyklen, Pensionsbeiträge) und sollte daher regimestabiler sein als reine Sentiment-Effekte — trotzdem zeigt die Empirie klaren Decay, vermutlich weil algorithmische Arbitrageure genau dieses vorhersehbare Flow-Muster inzwischen frontrunnen. Tail-Risiko ist gering (kein Leverage/Crowding-typisches Crash-Risiko), aber das Chancen-Risiko-Verhältnis ist inzwischen ungünstig.

### h) Kritik / Widerlegung
Sullivan/Timmermann/White (2001) zeigen explizit für TOM-artige Regeln, dass die Signifikanz nach Data-Snooping-Korrektur schrumpft. Die von mir gefundene aktuelle Praktiker-Analyse (2023, "Turn-of-the-Month Strategies: Do They Still Work?") kommt unabhängig zum gleichen Schluss: der Effekt "ist wahrscheinlich wegarbitriert worden" ("has likely been arbitraged away"), klassischer Lebenszyklus einer publizierten Anomalie.

**Urteil: WEAK.** Ökonomisch plausibel begründet, außergewöhnlich lange und international reproduziert (90 Jahre, 30+ Länder) — das ist stärker als die meisten Kalendereffekte. Aber die Post-2015-Evidenz zeigt fast vollständigen Decay in liquiden Industrieländer-Märkten und Netto-Renditen nahe/unter Buy-and-Hold nach Kosten. Ein Rest-Signal in weniger liquiden Märkten könnte real sein, ist aber schwer klar von Liquiditätsprämie zu trennen und kapazitätsmäßig klein.

---

## 2. Cross-sektionale Kalendersaisonalität ("Own-Month"-Effekt, Heston & Sadka)

### a) Ökonomische Begründung
Anders als TOM oder Halloween hat dieser Effekt **keine** etablierte Flow-basierte Erklärung. Heston & Sadka (2008) selbst bieten keine überzeugende Risiko- oder Flow-Story; sie dokumentieren das Muster primär als robuste empirische Regelmäßigkeit. Keloharju, Linnainmaa & Nyberg (2016, *Journal of Finance*, "Return Seasonalities"; Folgearbeit 2021 in *JFE* "Are Return Seasonalities Due to Risk or Mispricing?") testen explizit Risiko- vs. Mispricing-Hypothesen und finden Evidenz, die eher zu **temporärem Mispricing** passt als zu einer rationalen Risikoprämie — u.a. weil sich die Saisonalitäten über das Jahr zu praktisch Null aufsummieren (ein Titel mit hoher Rendite im "eigenen" Monat hat systematisch niedrigere Renditen in den anderen elf Monaten), was für eine Kompensations-/Rotationslogik statt für einen dauerhaften Risikofaktor spricht. Als spekulative Mechanismen werden genannt: saisonal wiederkehrende institutionelle Rebalancing-Zyklen, saisonale Unterschiede in Handelsaktivität/Retail-Attention, sowie eine mögliche Rolle von Index-/Fonds-Rebalancing-Kalendern.

### b) Limits to Arbitrage
Dies ist der ökonomisch unbefriedigendste Punkt des Kandidaten: Es gibt keinen klaren strukturellen Grund, warum dieses Muster nicht wegarbitriert wird, außer der Kostenstruktur der Umsetzung selbst (siehe e). Das ist ein Warnsignal — ein "Free Lunch" ohne identifizierbaren Arbitrage-Hemmschuh ist entweder (i) durch ein unmodelliertes Risiko erklärt, (ii) ein Kostenphänomen (siehe unten), oder (iii) doch teilweise Artefakt der Konstruktion (20 Jahres-Lags gleichzeitig getestet, viele Freiheitsgrade in der Sortierungsmethodik).

### c) Originalstudie
Heston & Sadka (2008, *Journal of Financial Economics* 87(2), 418–445, "Seasonality in the Cross-Section of Stock Returns"). Sortierung von US-Aktien nach historischer Rendite im gleichen Kalendermonat (Lags von 12, 24, 36 Monaten, bis zu 20 Jahres-Lags); die Autoren zeigen, dass diese "Own-Month"-Rendite-Sortierung eine signifikante Renditespanne zwischen Top- und Bottom-Dezil erzeugt, die von den üblichen Kontrollen (Size, B/M, Momentum, Industrie) nicht absorbiert wird. Effekt ist über alle Kalendermonate positiv, mit den stärksten Ausprägungen im Oktober, Dezember und Januar.

Keloharju, Linnainmaa & Nyberg (2016) erweitern die Analyse erheblich: über Aktien, ~100 publizierte Anomalie-Long-Short-Strategien, Rohstoffe und internationale Aktienindizes hinweg, jeweils auf Tages- und Monatsfrequenz. Eine auf historischer Own-Month-Rendite basierende Long-Short-Strategie erzielt in ihrer Stichprobe eine durchschnittliche Rendite von **ca. 13% p.a.**, hochsignifikant.

### d) Out-of-Sample-/Post-Publication-Evidenz
Die Breite der Replikation (mehrere unabhängige Autorenteams, internationale Aktienmärkte, Rohstoffe, verschiedene bereits publizierte Faktor-Strategien) spricht klar gegen reines Data-Mining innerhalb einer einzigen US-Stichprobe — das ist der stärkste MTK-robuste Befund meiner drei Kandidaten. Was fehlt: eine dezidierte Post-2016-Decay-Studie (analog McLean/Pontiff für diesen spezifischen Faktor) konnte ich nicht auffinden; es ist daher unklar, ob und wie stark der Effekt seit Publikation der Keloharju-Arbeit (2016) gesunken ist. Diese Evidenzlücke werte ich konservativ (keine dokumentierte Post-Publication-Persistenz mit aktuellen Zahlen = kein Freibrief für "CANDIDATE").

### e) Kosten
Hier liegt das eigentliche Killer-Argument. Eine Own-Month-Strategie erfordert **monatlichen Vollrebalance der gesamten Cross-Section** long UND short — de facto eine der turnoverintensivsten Strategiearten überhaupt (ähnlich Short-Term-Reversal-Strategien, die in der Literatur regelmäßig als "auf dem Papier profitabel, nach realistischen Kosten unprofitabel" eingestuft werden, z.B. Novy-Marx/Velikov 2016 zu Handelskostenmodellen). Keine der gesichteten Quellen liefert eine Netto-von-Kosten-Sharpe-Ratio für genau diese Strategie.

### f) Kapazität
Der Effekt ist in der Literatur nicht explizit auf Small-Caps beschränkt dokumentiert, aber cross-sektionale Long-Short-Anomalien dieser Bauart laden empirisch typischerweise stark auf kleinere, weniger liquide Titel (dort ist die Renditestreuung und damit auch die "Anomalie" größer). Kombiniert mit dem hohen Turnover ⇒ Kapazität wahrscheinlich in den niedrigen bis mittleren zweistelligen Millionen-USD-Bereich für eine einzelne Fonds-Implementierung, bevor Market Impact die Bruttoedge auffrisst — eine Schätzung mangels expliziter Kapazitätsstudie in der Literatur, daher mit Vorsicht zu genießen.

### g) Regimeabhängigkeit und Tail-Risiko
Wenig dokumentiert. Da der Effekt nicht klar risikobasiert ist (siehe Keloharju et al. 2021), besteht das Risiko, dass er in Stressphasen (hohe Korrelationen, Short-Squeeze-Risiko bei Small-Cap-Shorts) genau dann versagt, wenn Diversifikation am wichtigsten wäre.

### h) Kritik/Widerlegung
Kein direkter STW-artiger Data-Snooping-Test für diesen spezifischen Faktor gefunden. Die implizite Kritik: 20 verschiedene Jahres-Lags gleichzeitig zu testen und den "besten" saisonalen Monat pro Aktie zu identifizieren, ist methodisch nah an einem Data-Mining-Design (in-sample wird für jede Aktie individuell der Monat mit der historisch besten Performance identifiziert) — Keloharju et al. adressieren dies teilweise durch Out-of-Sample-Tests und Cross-Asset-Replikation, was das Vertrauen erhöht, aber die grundsätzliche Konstruktionslogik bleibt overfitting-anfällig auf Einzeltitelebene.

**Urteil: WEAK.** Statistisch der robusteste und am breitesten replizierte Befund der drei Kandidaten (mehrere unabhängige Autorenteams, mehrere Assetklassen, mehrere Länder) — das spricht stark gegen reinen Zufallsfund. Aber: fehlende ökonomische Arbitrage-Grenze, fehlende dokumentierte Netto-Kosten-Performance, sehr hoher Turnover und wahrscheinliche Small-Cap-Konzentration lassen mich bei "wahrscheinlich reale statistische Regelmäßigkeit, aber nicht sauber belegt handelbar" landen statt bei CANDIDATE.

---

## 3. Halloween-Effekt / Sell-in-May (Bouman & Jacobsen)

### a) Ökonomische Begründung
Die Autoren selbst finden **keine** überzeugende risikobasierte Erklärung (sie testen und verwerfen u.a. Zinsstruktur-, Dividenden- und übliche Risikofaktor-Erklärungen). Die meistzitierte komplementäre Hypothese ist verhaltensökonomisch: Kamstra, Kramer & Levi (2003, *American Economic Review*, "Winter Blues: A SAD Stock Market Cycle") — Seasonal Affective Disorder (SAD): geringeres Tageslicht im Herbst erhöht die Risikoaversion, was im Herbst zu Verkaufsdruck/niedrigeren Bewertungen und im Frühjahr zu einer Erholung führt. Dies ist eine "weiche" Verhaltenserklärung, keine Flow-/Institutionen-Story wie bei TOM.

### b) Limits to Arbitrage
Die Umsetzung ist trivial billig (zwei Trades pro Jahr, liquide Indexfutures/ETFs, kein Shortzwang) — wenn der Effekt real und groß genug wäre, gäbe es keinen strukturellen Grund, warum er nicht arbitriert würde. Als Verteidigung wird meist angeführt: Der Effekt ist klein relativ zur Volatilität der Aktienmarktrisikoprämie, weshalb er im Rauschen der Jahresrenditen schwer als verlässliches Arbitrage-Ziel zu isolieren ist ("statistically significant, but economically marginal relative to noise" — klassisches Limits-to-Arbitrage-Argument über Rauschen, nicht über Transaktionskosten).

### c) Originalstudie
**Bouman & Jacobsen (2002, *American Economic Review* 92, 1618–1635, "The Halloween Indicator, 'Sell in May and Go Away': Another Puzzle")**: 37 Länder, MSCI-Daten (unterschiedliche Startpunkte, teils bis in die 1970er zurück). Winterrenditen (November–April) sind in 36 von 37 Ländern signifikant höher als Sommerrenditen (Mai–Oktober); die Marktrisikoprämie ist über das Jahr betrachtet praktisch vollständig auf die Wintermonate konzentriert. Bemerkenswert: Die "Sell in May"-Faustregel existierte bereits Jahrzehnte als Börsenfolklore, bevor sie formal getestet wurde — das mildert (aber eliminiert nicht) die übliche Kritik des Post-hoc-Data-Minings, weil die Hypothese nicht aus der Stichprobe selbst generiert wurde.

### d) Out-of-Sample-/Post-Publication-Evidenz
Dies ist der Kandidat mit der längsten dokumentierten Historie überhaupt. Zhang & Jacobsen (2021, *Journal of International Money and Finance*, Fortsetzung von Jacobsen/Bouman) erweitern die Stichprobe zurück bis 1693 (UK) und testen 108–114 Märkte über einen kombinierten Zeitraum von rund 323 Jahren; sie finden den Effekt in 82 von 109 Ländern weiterhin mit Winterrenditen > Sommerrenditen. Für den ursprünglichen Post-2002-Zeitraum (Out-of-Sample zur Originalstudie) bestätigen sie den Effekt in allen 37 Ländern der Originalstichprobe, mit in 15 davon weiterhin statistisch signifikanten Einzelschätzern.

**Aber:** Aktuellere Einzelmarkt-Auswertungen (2015–2025) zeichnen ein deutlich schwächeres Bild. Eine Halloween-Strategie auf den S&P 500 von November 2015 bis April 2025 hätte 100 USD auf 175 USD wachsen lassen, während Buy-and-Hold im selben Zeitraum auf 264 USD gekommen wäre. Für DJIA, Nasdaq-100 und FTSE All-World im Zeitraum 2014–2025 wird die Strategie explizit als "invalidiert" gegenüber simplem Buy-and-Hold beschrieben. Das ist eine massive Regime-abhängige Unterperformance in genau den liquidesten, am einfachsten handelbaren Märkten — während die gepoolte internationale Signifikanz (inkl. vieler kleinerer/illiquiderer Märkte) weiterhin besteht. Geschätzter Decay für die praktisch relevanten Kernmärkte (US/UK-Großindizes) seit den 2010ern: **wirtschaftlich gegen 100%, teils Vorzeichenumkehr**, während die akademische Statistik über die Gesamtstichprobe (inkl. Historie vor 2000 und Emerging Markets) weiterhin signifikant bleibt.

### e) Kosten
Praktisch irrelevant — bei zwei Trades pro Jahr in liquiden Index-Futures/ETFs sind Spread- und Market-Impact-Kosten vernachlässigbar (Bruchteile eines Basispunkts p.a. annualisiert). Das ist der einzige Kandidat der drei, bei dem Transaktionskosten definitiv NICHT die limitierende Größe sind — das Problem ist die Größe und Stabilität des Brutto-Effekts selbst.

### f) Kapazität
Sehr hoch (S&P-500-/MSCI-World-Futures und -ETFs haben praktisch unbegrenzte Kapazität für einen Markttiming-Overlay dieser Größenordnung). Kapazität ist hier kein limitierender Faktor.

### g) Regimeabhängigkeit und Tail-Risiko
Hoch regimeabhängig — das zentrale Ergebnis dieser Recherche. Die Strategie funktioniert nur, wenn die Aktienrisikoprämie systematisch stärker im Winterhalbjahr anfällt; in strukturellen Bullenmärkten mit anhaltend positiver Sommerperformance (wie größtenteils 2012–2021 und erneut 2023/24) verliert die Strategie gegenüber Buy-and-Hold, weil sie 6 Monate Marktexposure aufgibt. Tail-Risiko: ein einzelner "falscher" Sommer-Crash oder eine ausbleibende Winter-Korrektur kann mehrjährige relative Performance auslöschen (siehe S&P-500-Beispiel oben) — Pfadabhängigkeit ist hier das Kernproblem, nicht Liquidität oder Kosten.

### h) Kritik/Widerlegung
Sullivan/Timmermann/White (2001) zielt direkt auf diese Art von Kalenderregel. Zusätzlich: Die SAD-Erklärung (Kamstra/Kramer/Levi) selbst wurde methodisch kritisiert (u.a. Kelly & Meschke sowie weitere Arbeiten hinterfragen Kausalität vs. Korrelation der Tageslicht-Stimmungs-Kette). Der dokumentierte Bruch der Einzelmarkt-Performance seit ~2014 in den größten/liquidesten Indizes ist die stärkste empirische Widerlegung der praktischen Handelbarkeit, unabhängig von der akademischen Signifikanz der gepoolten Langfriststichprobe.

**Urteil: WEAK.** Der am längsten und breitesten historisch dokumentierte Effekt überhaupt (323 Jahre, über 100 Länder) — das ist beeindruckende Reproduzierbarkeit und spricht gegen simples Data-Mining. Kosten sind kein Hindernis. Aber die ökonomische Begründung ist weich (Verhaltenshypothese, nicht Flow-basiert), und die Out-of-Sample-Performance in genau den Märkten, die ein institutioneller Investor tatsächlich handeln würde (US-Großindizes, seit ca. 2014), ist enttäuschend bis negativ. Kein CANDIDATE, weil die jüngste Dekade die Kostenrobustheits-Frage durch eine Brutto-Effekt-Frage ersetzt hat: das Problem ist nicht mehr "frisst der Spread die Rendite", sondern "ist die Rendite überhaupt noch da".

---

## 4. Kurz geprüft und verworfen (KILL) — zur Illustration der Multiple-Testing-Problematik

Diese wurden bewusst NICHT als Hauptkandidaten gewählt, werden hier aber kurz dokumentiert, um zu zeigen, dass die Auswahl der drei Kandidaten oben kein Zufallsprodukt selektiver Berichterstattung ist:

- **Januar-Effekt / Small-Cap-Tax-Loss-Selling** (Rozeff & Kinney 1976; Keim 1983): Ursprünglich einer der robustesten Kalendereffekte (Small-Cap-Januarrenditen deutlich über anderen Monaten, Tax-Loss-Selling-Reversal als plausibler Mechanismus). Post-1990-Evidenz zeigt jedoch einen klaren, gut dokumentierten Rückgangstrend seit Ende der 1980er für Large- UND Small-Cap-Indizes; für die Russell-Indizes ist der Effekt inzwischen verschwunden. Aktuelle Bewertung: "in der jüngeren Periode war der Januar-Effekt so klein, dass Transaktionskosten den Handel unmöglich machen." **KILL** — Lehrbuchbeispiel für Publikations-getriebenen Decay (Anstieg von index-/ETF-basiertem Small-Cap-Kapital, das nicht steuersensitiv ist [401(k)/Pensionsvehikel], schwächt den Tax-Loss-Selling-Mechanismus strukturell ab).
- **Feiertagseffekt (Pre-Holiday-Effekt)**, Ariel (1990), Lakonishok & Smidt (1988): historisch sehr stark (Pre-Holiday-Tagesrenditen ein Vielfaches der Normalrendite), aber in mehreren Folgestudien (u.a. Vergin & McGinnis 1999) für die 1990er als weitgehend verschwunden dokumentiert. **KILL**.
- **Wochentagseffekt / Montags-Effekt** (French 1980): das historisch bekannteste Kalendermuster (negative Montagsrenditen), aber seit den 1990ern in mehreren Studien als abgeschwächt bis umgekehrt dokumentiert. **KILL**.
- **Quartalsende-Window-Dressing/Rebalancing**: real als Preisdruck-Phänomen (Window Dressing von Fondsmanagern, Index-Rebalancing-Tage), aber ökonomisch eher ein Liquiditäts-/Market-Microstructure-Effekt auf Einzeltitelebene (z.B. bei Indexaufnahmen) als eine systematische, breit handelbare Kalender-Anomalie im Sinne dieses Mandats — gehört eher in die Marktmikrostruktur-/Liquiditäts-Anomalieklasse als hierher. **Nicht vertieft** (Abgrenzungsentscheidung, kein inhaltliches KILL).

---

## 5. Gesamturteil der Klasse

Keiner der drei geprüften Kandidaten erreicht die Schwelle **CANDIDATE**. Alle drei sind **WEAK**: real genug dokumentiert (lange Historie, teils außergewöhnlich breite internationale Replikation), um die reine Nullhypothese "alles Zufall" nicht mit voller Überzeugung zu bestätigen — aber keiner erfüllt gleichzeitig (i) dokumentierte Post-Publication-Persistenz UND (ii) Kostenrobustheit UND (iii) klare ökonomische Arbitrage-Grenze, wie in der Aufgabenstellung für CANDIDATE gefordert.

Auffälliges Muster: Die drei Kandidaten scheitern an unterschiedlichen der drei Kriterien — TOM an (ii)/Decay, Own-Month-Saisonalität an (i)/fehlender dokumentierter Netto-Kosten-Evidenz und (iii)/fehlender Arbitrage-Grenze, Halloween an (i)/jüngerer Einzelmarkt-Underperformance trotz gepoolter Signifikanz. Das ist kein Zufall: Es spiegelt genau das erwartete Verhalten einer Anomalieklasse wider, die (a) trivial einfach zu entdecken ist (kein komplexes Signal nötig, nur ein Kalender), (b) seit Jahrzehnten von Praktikern UND Akademikern durchsucht wird, und (c) sobald real, extrem leicht und billig zu arbitrieren ist (Timing-Trades ohne komplexe Titelauswahl).

**Mein Gesamturteil für die Klasse Saisonalitäten: überwiegend tot als eigenständige, direkt handelbare Alpha-Quelle für ein institutionelles Buch.** Was übrig bleibt, ist im besten Fall ein sehr kleiner, nicht robust belegter Signal-Beitrag, der allenfalls als Timing-Overlay in Kombination mit anderen Signalen (z.B. Execution-Timing für ohnehin geplante Trades um den Monatswechsel, oder als einer von vielen schwachen Inputs in einem größeren Multi-Faktor-Modell wie in der zitierten Quantpedia-Kombinationsstrategie mit TOM+Halloween+FOMC+Momentum, die auf 9,56% p.a. bei Sharpe 0,77 kommt) Wert stiftet — nicht als eigenständige Strategie. Die adversariale Grundhaltung dieses Mandats wird durch die Daten bestätigt: Die Klasse ist der Klassiker für "sieht in jeder Backtest-Tabelle gut aus, überlebt aber selten den nächsten Zehn-Jahres-Zeitraum out-of-sample".

**Empfehlung an das Portfolio-Komitee:** Kein dediziertes Saisonalitäts-Buch aufsetzen. Falls überhaupt Kapitalallokation: allenfalls als kostenloses Nebenprodukt-Signal (Execution-Timing) innerhalb bereits bestehender Strategien anderer Anomalieklassen, nicht als eigenständige Sharpe-Quelle.

---

## Quellen (Web-Recherche, Juli 2026)

- [Turn-of-the-Month Strategies: Do They Still Work? — QuantSeeker](https://www.quantseeker.com/p/turn-of-the-month-strategies-do-they)
- [Infrequent rebalancing, risk deferral, and equity returns at the turn of the month — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1042443126000259)
- [Investigating the Turn of the Month effect: Evidence from International Financial Markets — ResearchGate](https://www.researchgate.net/publication/370416630_Investigating_the_Turn_of_the_Month_effect_Evidence_from_International_Financial_Markets)
- [Turn of the Month in Equity Indexes — Quantpedia](https://quantpedia.com/strategies/turn-of-the-month-in-equity-indexes)
- [Turn‐of‐Month Evaluations of Liquid Profits and Stock Returns — Ogden 1990, Journal of Finance](https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1990.tb02435.x)
- [Dash for Cash: Monthly Market Impact of Institutional Liquidity Needs — Review of Financial Studies](https://academic.oup.com/rfs/article/33/1/75/5494694)
- [Seasonality in the Cross-Section of Expected Stock Returns — Heston & Sadka, SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=687022)
- [Seasonality in the cross-section of stock returns — ScienceDirect/JFE](https://www.sciencedirect.com/science/article/abs/pii/S0304405X0700195X)
- [Seasonality in the Cross Section of Stock Returns: The International Evidence — ResearchGate](https://www.researchgate.net/publication/227406433_Seasonality_in_the_Cross_Section_of_Stock_Returns_The_International_Evidence)
- [Are Return Seasonalities Due to Risk or Mispricing? — Keloharju, Linnainmaa, Nyberg, SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3276334)
- [Return Seasonalities — Keloharju, Linnainmaa, Nyberg 2016, Journal of Finance (Wiley)](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12398)
- [The Halloween Indicator, "Sell in May and Go Away": Everywhere and all the time — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0261560620302242)
- [The Halloween Indicator, 'Sell in May and Go Away': Another Puzzle — Bouman & Jacobsen, AEA](https://www.aeaweb.org/articles?id=10.1257%2F000282802762024683)
- [Are Monthly Seasonals Real? A Three Century Perspective — Jacobsen, Wharton](http://www-stat.wharton.upenn.edu/~steele/Courses/434/434Context/Calendar%20Effects/SellInMayGoAway.pdf)
- [The Halloween Effect: Trick or Truth? — Commonwealth](https://blog.commonwealth.com/independent-market-observer/the-halloween-effect-trick-or-truth)
- [Dangers of Data-Driven Inference: The Case of Calendar Effects — Sullivan, Timmermann, White, escholarship.org](https://escholarship.org/content/qt2z02z6d9/qt2z02z6d9.pdf)
- [Data-Snooping, Technical Trading Rule Performance, and the Bootstrap — Sullivan, Timmermann, White, SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=160330)
- [January Effect in Stocks — Quantpedia](https://quantpedia.com/strategies/january-effect-in-stocks)
- [The evolution of the January effect — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0378426607002774)

**Hinweis zur Evidenzbasis:** Alle Kernaussagen zu Originalstudien und Post-Publication-Decay wurden mittels WebSearch/WebFetch im Juli 2026 gegengeprüft (websuche_verfuegbar: ja). Einzelne quantitative Detailwerte aus den Originalarbeiten (z.B. exakte Basispunkt-/t-Statistik-Angaben bei Lakonishok & Smidt 1988 und Ogden 1990), die sich nicht direkt aus den durchsuchbaren Quellen extrahieren ließen (PDF-Volltext war in dieser Session nicht maschinenlesbar zugänglich), wurden konservativ nur qualitativ referenziert statt mit möglicherweise ungenauen Zahlen aus internem Modellwissen beziffert.
