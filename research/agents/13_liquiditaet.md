```yaml
agent: 13
klasse: "Liquiditätsanomalien"
websuche_verfuegbar: ja
strategien:
  - name: "Amihud-Illiquiditätsprämie (charakteristikbasiert, ILLIQ-Sortierung)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 1
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "0.0-0.15 nach realistischen Kosten in institutioneller Größe"
    kernrisiko: "Prämie ist überwiegend unrealisierte Handelskostenkompensation; nach Slippage/Market Impact in genau den Titeln, die die Prämie erzeugen, verschwindet der Netto-Effekt"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Eigenkonstruktion ILLIQ = |Rendite|/Dollarvolumen aus Yahoo Finance/Stooq Tagesdaten; keine offizielle Ken-French-Reihe"
  - name: "Pastor-Stambaugh systematischer Liquiditätsrisikofaktor (LIQ, Beta-Sortierung)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.25
    netto_sharpe_erwartung: "0.1-0.3 brutto; ca. 0.0-0.15 netto nach Crowding/Kosten"
    kernrisiko: "Post-Publication-Replikation (Pontiff & Singla 2019) zeigt fragile Identifikation; Prämie lädt konzentriert auf Krisenperioden (2008), genau wenn Liquiditätsspiralen Diversifikation zerstören"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Pastor-Stambaugh Liquidity Factor (frei auf L. Pástors Faculty-Website, monatliche Reihe seit 1962), ergänzend Ken-French 5-Faktoren + Momentum"
  - name: "Liquiditätsprovision / Market-Making-Renditen (kurzfristige Reversal als Proxy, Nagel 2012)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 1
      handelbarkeit: 1
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.2
    netto_sharpe_erwartung: "<0 nach Kosten für Nicht-HFT-Akteure ohne Speed-/Rebate-Vorteil; für Mandat nicht als Faktor-Anomalie handelbar"
    kernrisiko: "Ist strukturell kein Alpha-Faktor sondern ein Infrastruktur-/Geschwindigkeitsgeschäft (Kolokation, Maker-Rebates); für Fonds ohne diese Infrastruktur ist die 'Prämie' reiner Bid-Ask-Bounce, der beim Ausführen verschwindet"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken-French Short-Term-Reversal-Faktor (ST_Rev) als grobe Näherung, keine echte Market-Making-P&L-Reihe frei verfügbar"
```

# Agent 13 — Anomalieklasse: Liquiditätsanomalien
**Unabhängiger Quant-Research-Bericht, Juli 2026**

Evidenzbasis: Websuche verfügbar und genutzt (WebSearch/WebFetch funktionierten für die meisten Quellen; zwei Original-PDFs — Amihud 2002 und Pontiff & Singla 2019 — waren technisch nicht extrahierbar und wurden über Sekundärquellen/Abstracts sowie internes Wissen ergänzt und als solches gekennzeichnet). Nullhypothese für die gesamte Klasse: Es gibt kein durch Außenstehende ernte­bares Alpha in Liquiditätsanomalien. Diese Nullhypothese wird durch die Evidenz weitgehend bestätigt.

---

## Executive Summary

Liquiditätsanomalien sind die Anomalieklasse, bei der sich Bruttoeffekt und Nettoeffekt am stärksten unterscheiden — per Konstruktion. Jede der drei geprüften Strategievarianten leidet an derselben Grundpathologie: Der gemessene Effekt korreliert fast perfekt mit den Handelskosten, die nötig sind, um ihn zu ernten. Dazu kommt scharfe Post-Publication-Evidenz:

- **Hou, Xue & Zhang (2020, "Replicating Anomalies", Review of Financial Studies)**: Von 102 getesteten Liquiditätsvariablen sind bei wertgewichteten Portfolios mit NYSE-Breakpoints **95 (93%) insignifikant** auf dem 5%-Niveau. Die Autoren bezeichnen die Liquiditätsliteratur explizit als "the biggest casualty" ihrer Replikationsstudie.
- **Pontiff & Singla (2019, Critical Finance Review, "Liquidity Risk?")**: Der Pástor-Stambaugh-Liquiditätsfaktor repliziert zwar in der Originalstichprobe (1962/66–1999), aber schon moderate methodische Variationen der Konstruktion drücken die Signifikanz der Prämie; Prä-Stichproden-Renditen sind niedriger, Post-Stichproben-Renditen höher als in der Originalstichprobe — ein klassisches Warnsignal für Data-Mining/Regime-Zufall statt stabiler Risikokompensation.
- **Ben-Rephael, Kadan & Wohl (2015, JFQA, "The Diminishing Liquidity Premium")**: Die Illiquiditätsprämie war bis Mitte der 1980er groß und robust, ist seither aber "small and second order" geworden und bei NYSE/AMEX-Titeln praktisch verschwunden; Restevidenz konzentriert sich nur noch auf sehr kleine Titel.
- **Nagel (2012, RFS, "Evaporating Liquidity")**: Erträge aus Liquiditätsbereitstellung (kurzfristige Reversal-Strategien als Proxy) sind extrem prozyklisch mit dem VIX — am höchsten genau in Krisen, wenn Kapital knapp und Ausführung am teuersten ist. Das ist keine handelbare Prämie für einen typischen Fonds, sondern eine Kompensation für ein Risiko, das strukturell mit dem übrigen Portfolio korreliert ist.
- **Aktuelle Marktstruktur-Evidenz (Sommer 2025, MSCI-Analyse)**: Liquiditätsfaktor-Exposures waren zentraler Treiber eines Quant-Crowding-Unwinds (Juni–Juli 2025, geschätzte ca. -4,2% Verlust bei Long-Short-Aktienfonds laut Goldman-Sachs-Prime-Services-Schätzung), der zeigt, dass Liquiditätsfaktoren heute überwiegend durch Crowding-Dynamik und nicht durch eine stabile Risikoprämie getrieben werden.

Fazit vorweg: Diese Anomalieklasse ist für ein Mandat mit realistischen institutionellen Kosten weitgehend **tot bzw. nicht profitabel handelbar**. Der einzige Kandidat mit einem WEAK-Urteil (Pástor-Stambaugh-Faktor) überlebt nur, weil er auf liquiden Blue-Chip-Titeln beruht (Beta-Sortierung statt Halten illiquider Titel) — nicht weil die zugrunde liegende Risikokompensation überzeugend repliziert.

---

## Kandidat 1: Amihud-Illiquiditätsprämie (charakteristikbasiert)

### a) Ökonomische Begründung — wer zahlt die Prämie und warum?

Die Kernidee (Amihud & Mendelson 1986, empirisch operationalisiert in Amihud 2002): Investoren verlangen eine Kompensation dafür, illiquide Titel zu halten, weil sie beim Kauf und Verkauf hohe Preiswirkungskosten (Market Impact) tragen. Illiquidität wird über das ILLIQ-Maß operationalisiert: der Jahresdurchschnitt des täglichen Verhältnisses von absoluter Rendite zu Dollarvolumen — ein Proxy für Preiswirkung pro gehandeltem Dollar.

Ökonomisch zahlt die Prämie, wer aus strukturellen Gründen (Small-Cap-Indexfonds, passive Anleger, Privatanleger ohne Wahl) gezwungen ist, illiquide Titel zu halten oder zu handeln, ohne die Kosten einzupreisen — die Prämie fließt an geduldige, langfristig orientierte Kapitalgeber (Buy-and-Hold-Investoren), die die Liquiditätsdienstleistung "Halten ohne baldigen Verkauf" erbringen. Das ist ökonomisch plausibel als Kompensation für ein reales Risiko (Liquidationskosten), nicht per se eine Ineffizienz.

### b) Limits to Arbitrage

Der zentrale Widerspruch dieser Anomalie: Um die Prämie zu ernten, muss man genau die Titel kaufen, deren Kauf/Verkauf am teuersten ist. Arbitrageure, die versuchen, den Effekt "wegzuhandeln", erhöhen selbst die Handelskosten, die sie kompensieren wollen — ein sich selbst limitierender Mechanismus. Zusätzlich: kleine, illiquide Titel haben oft geringe Marktkapitalisierung und Institutionelle unterliegen regulatorischen/mandatsbedingten Beschränkungen (Positionsgrößenlimits relativ zum Tagesvolumen, Diversifikationsvorgaben), die verhindern, dass genug Kapital zur Arbitrage bereitgestellt wird. Das begrenzt zwar theoretisch die Selbstzerstörung der Prämie – bedeutet aber gleichzeitig, dass ein Fonds, der sie ernten will, ebenfalls klein bleiben muss.

### c) Originalstudie: Amihud (2002)

Amihud, Y. (2002), "Illiquidity and stock returns: cross-section and time-series effects", Journal of Financial Markets 5, 31–56. Stichprobe: NYSE-Titel, 1963/1964–1997. Kernbefund: erwartete (marktweite bzw. titelspezifische) Illiquidität ist positiv mit erwarteten Überschussrenditen assoziiert (kompatibel mit einer Illiquiditätsprämie), während unerwartete Illiquiditätsschocks Aktienpreise kontemporär senken (Liquiditäts-Risikokanal). Amihud selbst dokumentiert bereits im Originalpaper, dass der geschätzte Effekt in der zweiten Hälfte der Stichprobe schwächer ist als in der ersten — ein früher Hinweis auf Decay, der in der Folgeliteratur bestätigt wurde.

*Hinweis Evidenzbasis*: Die Original-PDF-Regressionskoeffizienten/exakte t-Statistiken konnten technisch nicht extrahiert werden (korrupte PDF-Wiedergabe bei WebFetch); die oben genannten qualitativen Kernaussagen sind über Sekundärquellen (u.a. Lou & Shu, "Why is the Amihud Illiquidity Measure Priced?"; Amihuds eigene Revisit-Studie) bestätigt sowie durch internes Wissen ergänzt. Größenordnung aus der Literatur bekannt: die rohe (unkontrollierte) Renditespanne zwischen den illiquidesten und liquidesten Dezilen liegt historisch bei mehreren Prozentpunkten pro Jahr, schrumpft aber nach Size-Kontrolle massiv, da ILLIQ stark mit Marktkapitalisierung korreliert ist (Multikollinearitätsproblem — siehe Kritik unten).

### d) Out-of-Sample-/Post-Publication-Evidenz

- **Ben-Rephael, Kadan & Wohl (2015, JFQA)**: "The Diminishing Liquidity Premium" — bis Mitte der 1980er groß und robust, seither "small and second-order"; bei NYSE/AMEX-Titeln über 1997–2008 praktisch verschwunden; Rest-Effekt nur noch bei sehr kleinen Titeln nachweisbar. Erklärung der Autoren: strukturell gesunkene Transaktionskosten (Dezimalisierung, elektronischer Handel) haben die ökonomische Notwendigkeit einer Kompensation verringert.
- **Amihud selbst, "Illiquidity and Stock Returns: A Revisit"** (Critical Finance Review-Reihe, ca. 2020): erneute Prüfung des eigenen Maßes über einen erweiterten Zeitraum; bestätigt grundsätzlich einen Restpreis-Effekt, aber mit deutlich geschwächter und zeitlich instabiler Ausprägung.
- **Drienko et al. (2018), Harris & Amato (2018)**: unabhängig dokumentierte Abschwächung des Effekts über Zeit (laut Sekundärquellen-Zusammenfassung konsistent mit Ben-Rephael et al.).
- **Hou, Xue & Zhang (2020, RFS)**: In der bislang umfassendsten systematischen Replikationsstudie (447 Anomalien, davon 102 Liquiditätsvariablen) sind bei value-weighted Portfolios mit NYSE-Breakpoints **95 von 102 Liquiditätsvariablen (93%) insignifikant** auf 5%-Niveau — der höchste Ausfallanteil aller getesteten Anomalie-Kategorien. Die Autoren nennen die Liquiditätsliteratur explizit "the biggest casualty" ihrer Studie. Das ist der schärfste verfügbare Beleg dafür, dass ein Großteil der publizierten Liquiditätscharakteristik-Effekte auf Small-Cap-/Equal-Weight-Artefakte und unzureichende Microcap-Kontrolle zurückzuführen ist.
- **Decay-Schätzung (konservativ, aus Kombination der Quellen)**: Wird der ursprüngliche (grobe, unkontrollierte) Effekt als 100% Basis gesetzt, deutet die Literatur auf einen Decay von grob **70–90%** der rohen Renditespanne, sobald (i) Size sauber kontrolliert, (ii) value-weighted statt equal-weighted gerechnet und (iii) Post-2000-Daten verwendet werden.

### e) Kosten — die zentrale Frage dieser Klasse

Dies ist der entscheidende Testpunkt. Die Amihud-Illiquiditätsprämie ist per Definition am stärksten in genau den Titeln, in denen Slippage und Market Impact am größten sind (niedriges Dollarvolumen, große Preisbewegung pro gehandeltem Dollar — das ist praktisch die Umkehrung der ILLIQ-Formel). Novy-Marx & Velikov (2016, RFS, "A Taxonomy of Anomalies and their Trading Costs") zeigen allgemein: Strategien mit hohem Turnover und Fokus auf kleine/illiquide Titel verlieren nach realistischen Kosten den Großteil oder die gesamte Signifikanz; nur Strategien mit unter ca. 50% Monatsturnover und expliziten Halte-Kosten-Puffern (Buy/Hold-Spread-Konstruktion) generieren robuste Netto-Spreads. Eine naive Illiquiditäts-Sortierstrategie hat i.d.R. sowohl hohen Turnover (illiquide Titel wechseln häufig Dezile) als auch strukturell hohe Pro-Trade-Kosten. Kombiniert mit dem Ben-Rephael-Befund, dass der Bruttoeffekt seit den 1980ern ohnehin auf "second order" geschrumpft ist, bedeutet das: **die Nettorendite nach realistischen institutionellen Kosten (Market Impact, Spread, Opportunitätskosten aus langsamer Ausführung) liegt für die meisten plausiblen Implementierungen nahe null oder negativ.** Es gibt in der Literatur keine überzeugende Studie, die eine robuste, netto-positive, institutionell skalierbare Illiquiditätsprämie nach vollständigen Kosten zeigt.

### f) Kapazität und Handelbarkeit

Sehr gering. Per Konstruktion sind die attraktivsten Titel (höchstes ILLIQ) diejenigen mit dem geringsten Dollarvolumen — ein institutioneller Fonds kann nur einen kleinen Bruchteil des Tagesvolumens ohne signifikanten Market Impact handeln. Realistische Kapazitätsschätzung: niedriger zweistelliger bis niedriger dreistelliger Millionenbereich USD für ein diversifiziertes Long-Short-Buch, bevor Grenzkosten den Grenzertrag übersteigen — für einen institutionellen Hedgefonds im Milliarden-AUM-Bereich irrelevant klein.

### g) Regimeabhängigkeit und Tail-Risiko

Illiquiditätsprämien sind konzeptionell prozyklisch invers: In Stressphasen (2008, März 2020) steigt Illiquidität sprunghaft (Amihud selbst zeigt in der kontemporären Zeitreihenkomponente, dass unerwartete Illiquiditätsschocks Preise fallen lassen), das heißt genau dann, wenn die Prämie "fällig" würde, entstehen gleichzeitig große Mark-to-Market-Verluste und Liquidationsschwierigkeiten (siehe Brunnermeier & Pedersen 2009, "Market Liquidity and Funding Liquidity", RFS: destabilisierende Margin-Spiralen zwischen Markt- und Funding-Liquidität — Händler müssen in Stresszeiten Positionen abbauen, unabhängig vom Fundamentalwert, was Marktliquidität weiter austrocknet). Das ist der Kernwiderspruch der gesamten Klasse: Die Prämie wird am ehesten genau in den Momenten "verdient", in denen man am wenigsten in der Lage ist, sie tatsächlich zu realisieren.

### h) Bekannte Kritik/Widerlegungen

- **Bid-Ask-Bounce/Mikrostruktur-Artefakte**: Kurzfristige "Umkehrrenditen", die aus Geld-Brief-Spanne-Oszillationen entstehen (Roll 1984), können in täglichen Renditedaten fälschlich als ökonomische Prämie erscheinen, obwohl sie reines Ausführungsrauschen sind. Das ILLIQ-Maß selbst mischt echten Preisimpact mit Spread-bedingtem Rauschen.
- **Size-Kollinearität**: ILLIQ korreliert extrem stark (negativ) mit Marktkapitalisierung. Ein Großteil der scheinbaren "Illiquiditätsprämie" in unkontrollierten Sortierungen ist schlicht die Size-Prämie in anderem Gewand (die selbst seit den 1980ern stark geschwächt ist).
- **Lou & Shu ("Why is the Amihud Illiquidity Measure Priced?")**: zerlegen ILLIQ und zeigen, dass primär die Volumenkomponente (nicht die "echte" Preiswirkungskomponente) den Preiseffekt trägt — ein Hinweis, dass ILLIQ eher ein Turnover-/Aufmerksamkeits-Proxy als ein reines Liquiditätsrisikomaß ist.
- **Down-Day-Konzentration**: Weitere Zerlegungsstudien zeigen, dass die Prämie überwiegend aus der "Down-Day"-Komponente stammt — kompatibel mit einer Crash-Risikoprämie statt einer reinen Liquiditätsprämie.

**Urteil: KILL.** Die Kombination aus (i) dokumentiertem strukturellem Decay seit den 1980ern, (ii) der Hou-Xue-Zhang-Befund, dass 93% der Liquiditätsvariablen bei sauberer Methodik insignifikant werden, und (iii) der Tatsache, dass der Effekt am stärksten genau dort ist, wo Handelskosten ihn auffressen, ergibt keine belastbare, netto-positive, institutionell umsetzbare Prämie.

---

## Kandidat 2: Pástor-Stambaugh systematischer Liquiditätsrisikofaktor (LIQ)

### a) Ökonomische Begründung — wer zahlt die Prämie und warum?

Anders als die Amihud-Charakteristik ist dies ein **systematisches Risikofaktor-Argument**: Aktien, deren Renditen stark mit marktweiten (unerwarteten) Liquiditätsschocks kovariieren (hohe "Liquiditätsbeta"), sollten eine Risikoprämie tragen, weil Investoren eine Kompensation dafür verlangen, in genau den Momenten Verluste zu erleiden, in denen Liquidität marktweit austrocknet (schlechter Diversifikationszeitpunkt, analog zu CAPM-Logik, aber mit Liquidität statt Marktrendite als Preisfaktor). Wer zahlt: Investoren mit geringer Flexibilität, die Liquiditätsschocks nicht aussitzen können (gehebelte, margin-constrained Marktteilnehmer), zahlen implizit die Prämie an weniger constrained, geduldige Kapitalgeber, die bereit sind, das Liquiditätsrisiko zu tragen.

### b) Limits to Arbitrage

Der Faktor wird zwar aus liquiden Titeln konstruiert (Beta-Sortierung, nicht Level-Sortierung nach Illiquidität), was das Handelbarkeitsproblem gegenüber Kandidat 1 entschärft. Dennoch: Wenn die Prämie eine echte Risikokompensation für Liquiditätsspiralen ist, dann ist sie per Definition am stärksten in Krisen ausgeprägt — und genau dann sind Arbitrageure selbst funding-constrained (Brunnermeier & Pedersen 2009) und können die Prämie nicht beliebig wegarbitrieren. Das ist ökonomisch konsistent mit einer stabilen Risikoprämie, macht die Strategie aber gleichzeitig zu einem schlechten Diversifikationsbaustein für ein Multi-Strategie-Buch, da sie in genau den Momenten verliert, in denen andere Strategien ebenfalls unter Druck stehen.

### c) Originalstudie: Pástor & Stambaugh (2003)

Pástor, L. & Stambaugh, R.F. (2003), "Liquidity Risk and Expected Stock Returns", Journal of Political Economy 111(3), 642–685. Stichprobe: NYSE/AMEX-Titel, 1966–1999. Kernbefund: Aktien mit hoher historischer Sensitivität (Beta) gegenüber einem marktweiten Liquiditätsmaß (basierend auf volumen-induzierten Return-Reversal-Effekten) erzielen eine um **7,5% p.a.** höhere durchschnittliche Rendite als Aktien mit niedriger Sensitivität — adjustiert für Markt-, Size-, Value- und Momentum-Exposure (10-1-Spread-Portfolio, LIQ-Faktor). Das ist eine der größten dokumentierten Faktorprämien der Asset-Pricing-Literatur und war seit Publikation Standardbestandteil vieler Multifaktor-Modelle.

### d) Out-of-Sample-/Post-Publication-Evidenz

Dies ist der Kern der adversarialen Prüfung, und die Evidenz ist gemischt bis kritisch:

- **Pontiff & Singla (2019, Critical Finance Review, "Liquidity Risk?")**: Replizieren die Faktorkonstruktion erfolgreich in der Originalstichprobe. Aber: Out-of-Sample-Analyse zeigt Prä-Stichproben-Renditen niedriger und Post-Stichproben-Renditen höher als in der Originalperiode — ein Muster, das eher zu Zufall/Regimespezifität als zu einer stabilen strukturellen Risikoprämie passt. Kritischer: bereits **moderate Variationen der Indexkonstruktion** (leicht andere Gewichtungs- oder Aggregationsmethoden desselben zugrunde liegenden Konzepts) drücken die Signifikanz der Gamma-Prämie erheblich — ein klassisches Fragilitätssignal, das nahelegt, dass die publizierte Spezifikation (mit-)selektiert wurde, um Signifikanz zu erzielen ("garden of forking paths").
- **Li et al. (unabhängige Replikationsstudie, zitiert in Pástor & Stambaugh 2020 "Liquidity Risk After 20 Years")**: bestätigen grundsätzlich das Liquiditätsmaß und scharfe Einbrüche während der Finanzkrise 2008, was für die *deskriptive* Validität des zugrunde liegenden Liquiditätsmaßes spricht — aber nicht zwingend für eine stabil geprice­te Risikoprämie in der Cross-Section.
- **Pástor & Stambaugh selbst (2020, "Liquidity Risk After 20 Years", J. Finance/NBER w25774)**: verteidigen ihren Faktor gegen die Pontiff-Singla-Kritik, bestätigen aber implizit die Existenz eines Robustheitsproblems, sonst wäre keine Verteidigungsschrift nötig gewesen — die akademische Kontroverse selbst ist Evidenz für eine keineswegs unstrittige Prämie.
- **Hou, Xue & Zhang (2020, RFS)**: Im breiten Anomalie-Replikationstest gehört die Liquiditätsfaktor-Familie (inkl. verwandter LIQ-Beta-Konstruktionen) zu den am stärksten von Insignifikanz betroffenen Kategorien bei sauberer (value-weighted, NYSE-Breakpoint) Methodik.
- **Decay-Schätzung**: Konservativ geschätzt hat sich die statistische Robustheit (t-Statistik-Stabilität über Subperioden und Spezifikationsvarianten) seit 2003 um schätzungsweise **40–60%** verschlechtert, gemessen an der Bandbreite publizierter Replikationsergebnisse — mit erheblicher Unsicherheit, da Punktschätzungen der Prämie je nach Methodik stark streuen (teils sogar über 7,5% hinaus, teils nahe null).

### e) Kosten

Deutlich weniger problematisch als bei Kandidat 1, da der Faktor überwiegend aus liquiden, großkapitalisierten Titeln konstruiert wird (Beta-Sortierung statt Level-Illiquidität). Dennoch bleiben reale Kosten: monatliches Rebalancing der Beta-Schätzungen erzeugt Turnover, und in Krisenzeiten — wenn der Faktor am meisten "zahlt" — sind selbst großkapitalisierte Titel mit erhöhten Spreads und Market Impact konfrontiert (Liquidität ist prozyklisch für praktisch alle Titel, nicht nur Small Caps). Netto-Sharpe-Schätzung nach realistischen institutionellen Kosten und unter Berücksichtigung von Crowding: geschätzt 0,0–0,15, gegenüber brutto ca. 0,1–0,3.

### f) Kapazität und Handelbarkeit

Höher als Kandidat 1 (liquide Basiswerte), aber real begrenzt durch zwei Faktoren: (i) die Prämie ist im Kern eine Krisenrisikoprämie — ihre "wahre" Kapazität ist die Fähigkeit, in Krisen zusätzliches Risiko zu tragen, was für die meisten institutionellen Mandate (Drawdown-Limits, Risikobudgets) genau in diesen Momenten eingeschränkt ist; (ii) die jüngste Crowding-Evidenz (siehe g) zeigt, dass der Faktor mittlerweile signifikante Krypto-artige Unwind-Dynamik durch andere Quant-Fonds erlebt, was die effektive Kapazität für neue Kapitalallokation weiter reduziert.

### g) Regimeabhängigkeit und Tail-Risiko

Dies ist der kritischste Punkt für diesen Kandidaten. Konzeptionell und empirisch ist die Prämie stark auf Krisenperioden konzentriert (2008 als Paradebeispiel). Aktuelle Evidenz von **Sommer 2025**: Laut MSCI-Analyse (Blogpost "Unraveling Summer 2025's Quant Fund Wobble") erlitten Long-Short-Aktien-Quant-Fonds von Juni bis Ende Juli 2025 kumulierte Verluste von geschätzt **ca. -4,2%** (Goldman-Sachs-Prime-Services-Schätzung), getrieben primär durch ein Crowding-Unwind, bei dem **hoch-Beta- und liquiditätsfaktor-exponierte Short-Positionen** systematisch gegen die Fondspositionierung liefen. Unter den am stärksten leerverkauften Titeln wiesen 84% hohe Exposure gegenüber "problematischen" Faktoren (residuale Volatilität, Liquidität, Beta, geringe Profitabilität) auf — ein Beleg dafür, dass Liquiditätsfaktor-Exposures heute maßgeblich durch korrelierte Positionierung anderer Quant-Akteure getrieben werden, nicht durch eine fundamentale, stabile Risikoprämie. Das ist strukturell dieselbe Liquiditätsspiralen-Dynamik, die Brunnermeier & Pedersen (2009) theoretisch beschreiben: Wenn Kapital knapp wird, müssen gehebelte Akteure Positionen abbauen, was Preise weiter gegen sie bewegt — unabhängig vom fundamentalen Wert des Liquiditätsrisikos selbst.

### h) Bekannte Kritik/Widerlegungen

- Pontiff & Singla (2019) argumentieren explizit, dass die publizierte Spezifikation nicht robust gegenüber plausiblen alternativen Konstruktionen ist — ein starkes Signal für Data-Mining bzw. selektive Publikation der besten von vielen getesteten Varianten.
- Die auffällige Diskrepanz zwischen In-Sample- (7,5% p.a.) und variierenden Out-of-Sample-Schätzungen (teils höher, teils insignifikant je nach Studie/Methodik) ist unvereinbar mit einem stabilen, gut verstandenen Risikopreis-Mechanismus.
- Alternative Erklärung: Ein Großteil der historisch gemessenen Prämie könnte eine Kompensation für Krisenkorrelation/Tail-Risiko sein, die eher als Crash-Risikoprämie (verwandt mit Betting-against-Beta- oder Tail-Risk-Faktoren) denn als eigenständiges "Liquiditätsrisiko" zu interpretieren ist — schwer sauber zu trennen.

**Urteil: WEAK.** Kein KILL, weil (i) die Faktorkonstruktion auf liquiden Titeln beruht (Kostenproblem entschärft) und (ii) eine ökonomisch kohärente Geschichte (Liquiditätsspiralen, Brunnermeier-Pedersen) sowie eine bis heute laufende akademische Verteidigung (Pástor & Stambaugh 2020) existieren. Aber auch kein CANDIDATE, weil die geforderte Kombination aus dokumentierter Post-Publication-Robustheit UND Kostenrobustheit nicht erfüllt ist — Pontiff & Singla (2019) und Hou/Xue/Zhang (2020) liefern beide unabhängig belastende Evidenz gegen die Robustheit der Prämie, und die 2025er Crowding-Episode zeigt, dass der Faktor heute stärker durch Positionierungs-Dynamik als durch fundamentale Preisbildung getrieben wird.

---

## Kandidat 3: Liquiditätsprovision / Market-Making-Renditen (kurzfristige Reversal als Proxy)

### a) Ökonomische Begründung — wer zahlt die Prämie und warum?

Market Maker/Liquiditätsanbieter stellen kontinuierlich Kauf- und Verkaufskurse und verdienen im Erwartungswert die Geld-Brief-Spanne als Kompensation für (i) Bestandsrisiko (Inventory Risk) und (ii) Adverse-Selection-Risiko (das Risiko, gegen besser informierte Marktteilnehmer zu handeln). Nagel (2012, "Evaporating Liquidity", RFS) verwendet kurzfristige Kontrarian-/Reversal-Strategien als ökonomischen Proxy für die Renditen aus Liquiditätsbereitstellung: Wer nach kurzfristigen Preisbewegungen dagegenhält (kauft nach Rückgängen, verkauft nach Anstiegen), übernimmt implizit die Rolle eines Liquiditätsanbieters und wird von ungeduldigen, liquiditätsnachfragenden Händlern (die sofortige Ausführung wollen) kompensiert. Zahler der Prämie: Akteure mit dringendem Liquiditätsbedarf (z.B. gezwungene Verkäufer, Index-Rebalancer, in Not geratene gehebelte Fonds).

### b) Limits to Arbitrage

Extrem: Die Bereitstellung dieser Liquidität erfordert entweder (i) technologische Geschwindigkeit (Kolokation, Niedrig-Latenz-Infrastruktur, direkter Marktzugang), um vor anderen Marktteilnehmern zu reagieren, oder (ii) speziellen regulatorischen Status (eingetragene Market Maker mit Rebate-Vorteilen, Verpflichtungen aber auch Privilegien). Für einen "normalen" Quant-Hedgefonds ohne diese Infrastruktur ist der ökonomische Kern der Strategie nicht zugänglich — jeder Versuch, den akademisch gemessenen Reversal-Effekt in Tagesdaten ohne Intraday-Ausführungsvorteil zu handeln, kollidiert direkt mit denselben Kosten, die die Strategie kompensieren soll.

### c) Referenzstudien

Nagel, S. (2012), "Evaporating Liquidity", Review of Financial Studies 25(7), 2005–2039. Kernbefund: Erwartete Renditen aus Liquiditätsbereitstellung (approximiert durch kurzfristige Reversal-Strategien) sind stark zeitvariabel und gut durch den VIX-Index prognostizierbar; erwartete Renditen und bedingte Sharpe Ratios steigen mit dem VIX massiv an, insbesondere während der Finanzkrise 2007–09. Das Austrocknen der Liquiditätsbereitstellung durch kapitalbeschränkte Intermediäre wird als Haupttreiber der Liquiditäts-Evaporation in Krisen identifiziert. Ergänzend: Chordia, Roll & Subrahmanyam (2000) zeigen "Commonality in Liquidity" — Liquidität ist selbst ein systematischer, marktweiter Faktor, kein rein idiosynkratisches Titelmerkmal, was die Marktweite von Liquiditätskrisen erklärt.

### d) Out-of-Sample-/Post-Publication-Evidenz, Marktstruktur-Wandel

Der Marktstruktur-Wandel seit Dezimalisierung (2001) und Regulation NMS (2007) hat das gesamte ökonomische Umfeld für diese Strategieklasse verändert: Market-Making wird heute überwiegend von spezialisierten HFT-Firmen mit direktem Kolokations- und Rebate-Zugang dominiert. Das bedeutet nicht, dass die zugrunde liegende ökonomische Rente verschwunden ist (Market Making bleibt profitabel — sonst gäbe es keine HFT-Industrie), sondern dass sie fast vollständig an Akteure mit Geschwindigkeitsvorteil transferiert wurde und für traditionelle "Faktor"-Fonds strukturell nicht mehr zugänglich ist. Dies ist keine klassische Alpha-Decay-Geschichte (der Effekt "verschwindet" nicht), sondern eine Marktzugangs-/Kapazitätsgeschichte: die Rente existiert, ist aber vollständig von einer Handvoll technologisch führender Akteure eingehegt.

### e) Kosten — die zentrale Frage dieser Klasse

Ohne Geschwindigkeits-/Rebate-Vorteil ist die "Prämie" aus akademischen Reversal-Backtests größtenteils bzw. vollständig **Bid-Ask-Bounce-Artefakt** (Roll 1984): Beobachtete kurzfristige negative Autokorrelation in Tagesrenditen entsteht mechanisch durch das Oszillieren von Transaktionspreisen zwischen Geld- und Briefkurs, nicht durch eine ökonomisch reale Umkehrbewegung. Ein Backtest, der zu Schlusskursen handelt, überschätzt daher die real erzielbare Rendite systematisch. Sobald realistische Spreads, Marktimpact und Ausführungsverzögerung (selbst wenige Sekunden) berücksichtigt werden, wird die Nettorendite für Nicht-HFT-Akteure regelmäßig negativ — dies ist ein in der Marktmikrostruktur-Literatur gut etablierter Befund und keine neue Erkenntnis dieser Analyse, sondern Konsens.

### f) Kapazität und Handelbarkeit

Für Außenstehende (Nicht-Market-Maker) praktisch null. Die reale Kapazität dieser Ertragsquelle liegt bei den etablierten HFT-/Market-Making-Firmen selbst und ist für ein Hedgefonds-Mandat, das über Standardbroker-Infrastruktur ohne Kolokation handelt, nicht erschließbar.

### g) Regimeabhängigkeit und Tail-Risiko

Dies ist die am stärksten prozyklische Strategie der gesamten Klasse: Nagel (2012) zeigt explizit, dass die erwartete Rendite aus Liquiditätsbereitstellung mit dem VIX steigt — sie ist am höchsten in Krisen. Für einen Akteur, der tatsächlich in der Lage ist, in Krisen Liquidität bereitzustellen (ausreichend Kapitalpuffer, keine Zwangsverkäufer), ist das eine attraktive Diversifikationseigenschaft. Für die meisten institutionellen Mandate ist es das Gegenteil: gerade in Krisen sind Risikobudgets am knappsten, Margin-Anforderungen steigen, und die Fähigkeit, zusätzliches Kapital für Liquiditätsbereitstellung zu mobilisieren, ist am geringsten (Brunnermeier & Pedersen 2009 Spiralen-Logik) — die Strategie verlangt genau dann Kapitaleinsatz, wenn Kapital am knappsten und teuersten ist.

### h) Bekannte Kritik/Widerlegungen

- Klassischer Einwand: Akademische kurzfristige Reversal-Renditen in CRSP-Tagesdaten sind zu einem erheblichen Teil Bid-Ask-Bounce, keine reale handelbare Rendite (Roll 1984; breiter Konsens in der Mikrostrukturliteratur).
- Die Strategie ist kein "Faktor" im Sinne einer Cross-Sectional-Anomalie, die durch Screening/Sortierung handelbar wäre, sondern ein Infrastruktur-/Geschäftsmodell — die Vermischung mit klassischen Faktor-Anomalien in Teilen der akademischen Literatur ist irreführend für die Frage der praktischen Handelbarkeit durch einen Fundamental-/Quant-Hedgefonds ohne HFT-Arm.

**Urteil: KILL** (für das vorliegende Mandat — ein institutioneller Quant-Fonds ohne HFT-/Kolokations-Infrastruktur). Die ökonomische Rente ist vermutlich real (sonst gäbe es keine profitable HFT-Industrie), aber für dieses Mandat nicht zugänglich und in akademischen Standard-Backtests weitgehend ein Bid-Ask-Bounce-Artefakt ohne reale Handelbarkeit.

---

## Klassenurteil / Fazit

**Alle drei geprüften Kandidaten scheitern an mindestens einem harten Kriterium des Mandats.** Die Anomalieklasse "Liquiditätsanomalien" bestätigt die eingangs formulierte Falle in aller Deutlichkeit: Die Illiquiditätsprämie (Kandidat 1) frisst sich durch genau die Handelskosten auf, die sie kompensieren soll — das ist keine Vermutung, sondern durch die Kombination aus dokumentiertem strukturellem Decay (Ben-Rephael et al. 2015) und der harten Hou-Xue-Zhang-Replikationsstatistik (93% Insignifikanz) hinreichend belegt. Der systematische Pástor-Stambaugh-Risikofaktor (Kandidat 2) entgeht dem reinen Kostenproblem, leidet aber an fragiler statistischer Identifikation (Pontiff & Singla 2019) und an einer Tail-Risiko-Struktur, die durch die aktuelle Crowding-Episode 2025 in Echtzeit bestätigt wurde: Der Faktor verliert am meisten genau dann, wenn ein diversifiziertes Portfolio ihn am wenigsten gebrauchen kann. Die Market-Making-/Liquiditätsprovisions-Rente (Kandidat 3) ist am ehesten "echt", aber strukturell kein Faktor-Alpha, sondern ein durch Geschwindigkeit und Infrastruktur monopolisiertes Geschäftsmodell, das für ein klassisches Hedgefonds-Mandat nicht zugänglich ist.

**Einziges tragfähiges Signal für weitere Beobachtung**: der Pástor-Stambaugh-Faktor als Risikokontrollvariable (nicht als eigenständige Alpha-Quelle) — d.h. Kenntnis der eigenen Liquiditätsbeta-Exposure kann nützlich sein, um unbeabsichtigte Krisenkorrelation in einem Multi-Strategie-Buch zu vermeiden, auch wenn man die Prämie nicht aktiv als Ertragsquelle handelt.

Ein ehrliches Ergebnis dieser Untersuchung: **Diese Anomalieklasse liefert kein robustes, kostenrobustes, aus akademischer Literatur ableitbares Alpha für ein institutionelles Mandat.** Die Klasse sollte nicht als eigenständiger Strategiebaustein budgetiert werden.

---

## Quellen (Auswahl, per Websuche verifiziert bzw. ergänzt durch internes Wissen wie gekennzeichnet)

- Amihud, Y. (2002), "Illiquidity and stock returns: cross-section and time-series effects", Journal of Financial Markets 5, 31–56.
- Pástor, L. & Stambaugh, R.F. (2003), "Liquidity Risk and Expected Stock Returns", Journal of Political Economy 111(3), 642–685.
- Pontiff, J. & Singla, R. (2019), "Liquidity Risk?", Critical Finance Review 8(1-2), 257–276.
- Pástor, L. & Stambaugh, R.F. (2020), "Liquidity Risk After 20 Years", NBER Working Paper 25774 / Critical Finance Review.
- Hou, K., Xue, C. & Zhang, L. (2020), "Replicating Anomalies", Review of Financial Studies 33(5), 2019–2133.
- Ben-Rephael, A., Kadan, O. & Wohl, A. (2015), "The Diminishing Liquidity Premium", Journal of Financial and Quantitative Analysis.
- Nagel, S. (2012), "Evaporating Liquidity", Review of Financial Studies 25(7), 2005–2039.
- Brunnermeier, M.K. & Pedersen, L.H. (2009), "Market Liquidity and Funding Liquidity", Review of Financial Studies 22(6), 2201–2238.
- Novy-Marx, R. & Velikov, M. (2016), "A Taxonomy of Anomalies and their Trading Costs", Review of Financial Studies 29(1), 104–147.
- Chordia, T., Roll, R. & Subrahmanyam, A. (2000), "Commonality in Liquidity", Journal of Financial Economics.
- Roll, R. (1984), "A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market", Journal of Finance.
- Lou, X. & Shu, T. (2016), "Why is the Amihud (2002) Illiquidity Measure Priced?".
- MSCI Research Blog (2025), "Unraveling Summer 2025's Quant Fund Wobble" (aktuelle Marktstruktur-/Crowding-Evidenz, per Websuche verifiziert).

*Hinweis zur Evidenzqualität*: Zwei Original-PDFs (Amihud 2002, Pontiff & Singla 2019) konnten technisch nicht vollständig als Text extrahiert werden; die entsprechenden quantitativen Aussagen stützen sich auf Sekundärquellen, Abstracts und internes Wissen (Stand Anfang 2026), ergänzt durch die per Websuche verifizierten qualitativen Kernaussagen dieser Studien. Alle übrigen zitierten Zahlen (7,5% p.a. Pástor-Stambaugh-Prämie; 93% Insignifikanz bei Hou/Xue/Zhang; -4,2% Quant-Verlust Sommer 2025; 84%-Faktor-Exposure-Statistik) wurden direkt per Websuche aus den jeweiligen Quellen bzw. Sekundärzusammenfassungen bestätigt.
