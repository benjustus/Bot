```yaml
agent: 12
klasse: "Volatilitätsanomalien (Low-Vol/BAB/IVOL)"
websuche_verfuegbar: ja
strategien:
  - name: "Betting Against Beta (BAB) – gehebelte Long-Low-Beta/Short-High-Beta-Faktorstrategie"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.30
    netto_sharpe_erwartung: "0.0-0.2 (institutionell umsetzbar, gehebelt, nach Fundingkosten/Shortkosten)"
    kernrisiko: "Konstruktionsartefakt: Rank-Weighting erzeugt de-facto Gleichgewichtung mit massivem Microcap-Tilt (Novy-Marx & Velikov 2022: ~1,05 USD je investiertem Dollar in unterstes 1% Marktkap.-Perzentil); Alpha weitgehend durch Profitability-/Investment-Exposure erklärbar; Sensitivität ggü. Fundingkosten/Zinsregime"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "AQR 'Betting Against Beta: Equity Factors' (monthly/daily, offen abrufbar); ergänzend CRSP-Beta-Dezile / Ken-French-Beta-Portfolios als Näherung"
  - name: "Low-Volatility / Minimum-Variance Long-Only Aktienstrategie"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 4
      kapazitaet: 4
      kostenrobustheit: 4
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0.1-0.3 absolut; kaum inkrementell ggü. Quality/Value-Sleeve"
    kernrisiko: "Novy-Marx (2014) 'Understanding Defensive Equity': Effekt weitgehend Repackaging von Profitability- und Value-Exposure ohne eigenständiges Alpha; strukturelle Underperformance in Growth-/Momentum-Bullenmärkten (2020, 2023-2024); Crowding durch >100 Mrd. USD Low-Vol-ETF-AUM seit 2011"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French '10 Portfolios Formed on Variance' bzw. Beta-sortierte Portfolios; Tickerproxy USMV/SPLV/XMLV"
  - name: "Idiosynkratische Volatilität (IVOL) – Ang, Hodrick, Xing, Zhang (2006)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 1
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.20
    netto_sharpe_erwartung: "~0.0 nach Kosten, ggf. negativ auf der Short-Seite"
    kernrisiko: "Effekt konzentriert in kleinen, illiquiden, schwer/teuer shortbaren 'Lottery'-Aktien; durch MAX-Faktor (Bali/Cakici/Whitelaw 2011) und 1-Monats-Reversal/Mikrostruktur (Huang et al. 2010) größtenteils subsumiert bzw. erklärt; Vorzeichenrichtung methodenabhängig (Fu 2009 EGARCH-Kontroverse)"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "- (kein direkter Ken-French-Datensatz; selbst konstruierbar aus FF3/FF5-Residuen auf CRSP-Basis)"
```

# Volatilitätsanomalien im Aktienquerschnitt: Adversarial Review (Low-Vol / BAB / IVOL)

**Mandat:** Agent 12, unabhängige Prüfung. Nullhypothese: kein echtes Alpha. Websuche war während dieser Recherche verfügbar und wurde für Primärquellen (SSRN/NBER/JFE-Abstracts, AQR-Datensatzseiten, aktuelle ETF-Daten Stand ca. Q1/Q2 2026) genutzt. Wo Zahlen aus internem Wissen (Trainingsstand Anfang 2026) stammen und nicht per Websuche verifiziert werden konnten, ist dies explizit vermerkt.

---

## Executive Summary

Die "Volatilitätsanomalie" ist keine einzelne Anomalie, sondern mindestens drei unterschiedlich robuste Phänomene, die in der Praxis oft vermischt werden:

1. **BAB (Betting Against Beta)** – gehebelte Long-Short-Strategie auf Beta-Rang (Frazzini & Pedersen 2014).
2. **Low-Vol/Minimum-Variance long-only** – Sortierung nach realisierter Volatilität, meist ohne Hebel (Haugen & Baker 1991/1996; Blitz & van Vliet 2007; Baker/Bradley/Wurgler 2011).
3. **IVOL-Anomalie** – negativer Zusammenhang zwischen idiosynkratischer Volatilität (FF3-Residuen) und Folgerenditen (Ang et al. 2006, 2009).

Alle drei haben in den letzten zehn Jahren erhebliche akademische Gegenkritik erfahren, die über simples "Publikations-Decay" hinausgeht: Es handelt sich nicht nur um schwächere Renditen nach 2012–2014, sondern um **Konstruktionskritik**, die zeigt, dass ein erheblicher Teil der ursprünglich berichteten Effektgröße ein Artefakt der Portfoliokonstruktion (Rank-/Equal-Weighting, Microcap-Tilt, kurzfristige Reversal-Kontamination) war. Das ist qualitativ ein stärkerer Befund gegen die Klasse als reines Decay, weil es nahelegt, dass ein Teil des "Alpha" in der Originalstudie nie ökonomisch real war.

Mein Gesamturteil: **Kein Kandidat erreicht CANDIDATE.** BAB und Low-Vol long-only landen bei **WEAK** (es gibt eine plausible strukturelle Erklärung – Leverage-Constraints bzw. Benchmarking – aber die dokumentierte Netto-Alpha nach Kosten/Konstruktionskorrektur ist klein bis fraglich, und Crowding seit 2011–2014 ist real und beobachtbar). IVOL als eigenständige handelbare Long-Short-Strategie erhält **KILL** (das Phänomen existiert statistisch, ist aber in der Praxis nicht profitabel handelbar und größtenteils durch andere, besser verstandene Effekte erklärt).

---

## Kandidat 1: Betting Against Beta (BAB)

### a) Ökonomische Begründung

Frazzini & Pedersen (2014, JFE) bauen ein Modell mit heterogenen Leverage-Constraints: Anleger, die nicht (kostenfrei) hebeln dürfen (viele Privatanleger, manche institutionelle Mandate mit Leverage-Verbot), erreichen höhere erwartete Renditen nur durch Übergewichtung von High-Beta-Aktien statt durch Hebel auf Low-Beta-Aktien. Das drückt die Preise von High-Beta-Aktien relativ zu ihrem Risiko nach oben (Security Market Line wird "zu flach") und erzeugt einen Alpha-Unterschied zwischen Low- und High-Beta-Segment. BAB longt (gehebelt) Low-Beta-Aktien und shortet High-Beta-Aktien, jeweils beta-neutral skaliert.

Konkurrierende Erklärungen für den gleichen Querschnitt:
- **Lottery Demand** (Bali, Cakici, Whitelaw 2011, JFE, MAX-Effekt): Anleger mit Präferenz für schiefe, lotterieartige Payoffs zahlen eine Prämie für Aktien mit hohen extremen Tagesrenditen (MAX). Der MAX-Effekt korreliert stark mit hohem Beta und hoher idiosynkratischer Volatilität und **kehrt** in ihrer Studie das Vorzeichen der ursprünglichen IVOL-Anomalie um, wenn MAX kontrolliert wird – das heißt, ein signifikanter Teil dessen, was als "Beta-Anomalie" oder "IVOL-Anomalie" firmiert, könnte in Wahrheit ein Lottery-Demand-Effekt sein.
- **Benchmarking-Zwang** (Baker, Bradley, Wurgler 2011, FAJ): Institutionelle Manager, die an einem kapitalisierungsgewichteten Benchmark mit Tracking-Error-Budget gemessen werden (nicht am Sharpe Ratio), meiden systematisch Low-Beta-Aktien, weil deren erwartete Outperformance klein, aber ihr Tracking Error hoch ist relativ zum Benchmark. Das ist eine eigenständige, von Frazzini/Pedersen unabhängige Mikrofundierung mit ähnlicher Vorhersage.

Welche Erklärung "hält"? Adversarial betrachtet: Beide sind plausibel und schließen sich nicht aus, aber Novy-Marx & Velikov (2022, s.u.) zeigen, dass ein großer Teil des BAB-Alphas in der Originalkonstruktion **kein sauberes Beta-Alpha ist**, sondern über eine Rank-basierte Portfoliokonstruktion in eine Profitability-/Investment-Prämie (q-Faktor-Sprache) übersetzt wird. Das untergräbt die Frazzini-Pedersen-Erklärung empirisch, ohne sie theoretisch zu widerlegen.

### b) Limits to Arbitrage

- **Leverage-Aversion/-Restriktionen**: Genau der Mechanismus, der die Anomalie laut Theorie erzeugt (viele Investoren können/dürfen nicht hebeln), verhindert auch deren Arbitrage – ein internes konsistentes Argument, aber zugleich zirkulär: Wer BAB handeln will, muss selbst hebeln (Low-Beta-Seite typischerweise 1,5–3x gehebelt, um Beta-Neutralität zu erzeugen), was Fundingkosten, Margin-Calls und Prime-Broker-Abhängigkeit einführt.
- **Benchmarking** verhindert Arbitrage durch die größte Kapitalbasis (aktive Long-only-Manager, deren Alpha an TE gemessen wird) strukturell – dieses Argument ist zeitlich stabil, solange Manager-Evaluierung benchmark-relativ bleibt.
- **Shortkosten der High-Beta-Seite**: High-Beta-Aktien sind tendenziell kleiner, volatiler, wachstumsstärker – tendenziell teurer zu shorten (Borrow Fees), was die Short-Seite der Strategie strukturell verteuert.

### c) Originalstudie: Zahlen

Frazzini & Pedersen (2014, JFE 111(1), 1–25): US-Aktien 1926–März 2012. Berichteter Sharpe Ratio des BAB-Faktors für US-Aktien: **0,78** – etwa doppelt so hoch wie der Sharpe Ratio des Aktienmarktes im gleichen Zeitraum. International wird die Beta-Anomalie in 20 weiteren Aktienmärkten sowie in Treasuries, Credit-Märkten und Futures repliziert (Cross-Asset-Konsistenz als Robustheitsargument der Autoren). Der exakte t-Stat für den US-Equity-BAB-Faktor ließ sich in dieser Recherche nicht letztgültig aus Primärquellen verifizieren; er wird in Sekundärquellen als hochsignifikant (deutlich > 5) beschrieben – dieser Punkt wird hier **konservativ mit Unsicherheit gekennzeichnet**, da ich ihn nicht direkt aus dem Paper-PDF extrahieren konnte.

Zum Vergleich die IVOL-Originalstudie (Ang, Hodrick, Xing, Zhang 2006, Journal of Finance 61, 259–299): Spread zwischen Quintil 1 (niedrigste IVOL) und Quintil 5 (höchste IVOL) über 1% pro Monat (Value-weighted, FF3-risikoadjustiert), robust gegenüber Size-, Book-to-Market-, Momentum- und Liquiditätskontrollen. Bestätigt international in Ang et al. (2009) für 23 entwickelte Märkte.

Haugen & Baker (1991, 1996): eher praktikerorientierte Studien ohne die heute übliche formale Faktor-Regressionsapparatur; zeigen empirisch, dass Portfolios mit niedrigster historischer Varianz über 1929–1990er (US) sowohl absolut als auch risikoadjustiert Portfolios mit hoher Varianz outperformen – der historische Ursprung der Low-Vol-Beobachtung, aber methodisch schwächer (kein sauberes Multi-Faktor-Alpha, geringere statistische Strenge nach heutigem Standard).

### d) Out-of-Sample-/Post-Publication-Evidenz (2015–2026)

Dies ist der entscheidende Abschnitt für die Nullhypothese.

**Novy-Marx & Velikov (2022), Journal of Financial Economics 143(1), 80–106, "Betting Against Betting Against Beta"** – zentrale Kritik, die 2024 in aktualisierter Fassung erneut diskutiert wurde (arXiv:2409.00416, "Betting Against (Bad) Beta", ebenfalls Novy-Marx/Velikov, publiziert 2025 in Quantitative Finance):
- BAB verwendet eine **rank-basierte (nicht kapitalisierungsgewichtete) Portfoliokonstruktion**, die faktisch eine annähernde Gleichgewichtung erzeugt.
- Für jeden investierten Dollar in BAB werden im Schnitt **1,05 USD in Aktien des untersten 1%-Marktkapitalisierungs-Perzentils** committed – ein massiver, nicht transparent gemachter Microcap-Tilt.
- Nach Korrektur der Konstruktion (kapitalisierungsgewichtet bzw. mit realistischen Liquiditäts-/Investierbarkeitsfiltern) und nach Kontrolle auf Profitability- und Investment-Faktoren (q-Faktor-Modell) verbleibt zwar eine positive Netto-Rendite nach Transaktionskosten, aber sie ist überwiegend durch **Quality-artige Exposure** (Profitability, konservative Investitionspolitik) erklärbar – nicht durch eine eigenständige "Beta"-Prämie im Sinne der ursprünglichen Leverage-Constraint-Theorie.
- Fazit dieser Kritik: Ein Großteil der "astonishing performance" des Originalfaktors ist ein Konstruktionsartefakt, kein sauberes Test der Frazzini-Pedersen-Theorie.

**Baltussen, van Vliet et al. (Robeco-Autorenkreis, ca. 2019–2021, "Betting Against Beta or Demand for Lottery")**: ähnliche Stoßrichtung – zeigt, dass der BAB-Effekt stark mit Lottery-Demand-/kleinen-Aktien-Segmenten konzentriert ist, konsistent mit Bali/Cakici/Whitelaw statt mit einer reinen Leverage-Constraint-Geschichte.

**Live-/Fundingkosten-Sensitivität**: Nach Aussagen mehrerer Sekundärquellen (u.a. Marktkommentare zu AQRs BAB-Produkten) hat die Strategie seit ca. 2018–2023 in einem Umfeld steigender Zinsen (höhere Fundingkosten für die gehebelte Long-Low-Beta-Seite) und komprimierter Beta-Dispersion schwächer performt als im Backtest 1926–2012. AQR selbst unterhält zwei unterschiedliche Datenserien: die "Original Paper Data" (endet März 2012) und eine laufend aktualisierte "BAB Equity Factors"-Serie; die monatliche Korrelation zwischen beiden ist mit 96,2% zwar hoch, aber die Originalserie weist einen **signifikant höheren** Sharpe Ratio auf als die fortlaufend gepflegte Serie – ein Hinweis auf Overfitting/Snooping in der ursprünglichen Spezifikation oder auf echtes Post-Publication-Decay (beide Interpretationen sind mit den Daten vereinbar, und die Websuche konnte sie nicht sauber trennen).

**McLean & Pontiff (2016, Journal of Finance)**: Im breiteren Kontext von Post-Publication-Decay über ~100 dokumentierte Anomalien finden sie im Schnitt **58% Rückgang** der In-Sample-Effektgröße out-of-sample sowie einen weiteren Rückgang **nach** Publikation (~26% zusätzlich, Interpretation als Trading-getriebenes Decay). Volatilitätsbezogene Anomalien liegen in ihrer Stichprobe im Bereich dieses Durchschnitts, nicht auffällig robuster als der Median.

**Barroso ("Managing the risk of the betting-against-beta anomaly", Lancaster/FoFi-Konferenzpapier)**: zeigt, dass BAB-Renditen zeitvariable, mit Volatilität des Faktors selbst korrelierte Risikoprämien aufweisen ("Volatility Managed"-Literatur) – Risikomanagement kann Sharpe verbessern, ändert aber nichts an der grundsätzlichen Konstruktionskritik.

### e) Kosten

- **Turnover**: BAB wird monatlich (teils häufiger) auf Basis rollierender Beta-Schätzungen (typischerweise 1–5 Jahre Historie, teils mit Shrinkage) reformiert. Durch den Rang-Gewichtungsmechanismus und die Microcap-Konzentration (siehe Novy-Marx/Velikov) ist der Turnover in der Small-/Microcap-Seite hoch.
- **Spreads/Market Impact**: Gerade der von Novy-Marx & Velikov identifizierte Bottom-1%-Marktkapitalisierungs-Tilt bedeutet strukturell hohe Bid-Ask-Spreads und Market-Impact-Kosten – Aktien in diesem Segment sind typischerweise il liquide, teils Penny-Stock-nah.
- **Shortkosten High-Beta-Seite**: High-Beta-Aktien sind im Schnitt kleiner/wachstumsstärker/spekulativer und daher am Aktienleihemarkt tendenziell teurer zu shorten als der Marktdurchschnitt.
- **Hebelkosten**: Die Long-Low-Beta-Seite benötigt Fremdkapital (Rebalancing-Leverage), was in Hochzinsphasen (2022–2024/25) die Netto-Rendite spürbar schmälert – ein struktureller Nachteil gegenüber unlevered Faktoren.
- **Novy-Marx & Velikov (2022) selbst**: Nach Transaktionskosten bleibt eine positive Rendite, aber die Autoren attributieren sie größtenteils auf Profitability-/Investment-Exposure, nicht auf "Beta" – ökonomisch ist das dann eher eine (bereits bekannte) Quality-Prämie in neuem Gewand, kein zusätzliches Alpha.

### f) Kapazität und Handelbarkeit

Kapazität ist durch den Microcap-Tilt strukturell **klein bis mittel** für die Originalkonstruktion – die von der Kritik aufgedeckte Konzentration im untersten 1%-Marktkapitalisierungs-Segment ist per Definition kapazitätsarm; ein institutionelles Multi-Milliarden-Mandat kann diese Version nicht sauber replizieren, ohne den Marktimpact selbst zur dominanten Kostenkomponente zu machen. Eine kapitalisierungsgewichtete, liquiditätsgefilterte "praktikable" BAB-Variante (wie sie AQR in Produkten umsetzt) hat höhere Kapazität, aber laut Konstruktionskritik proportional geringeres Alpha. Long-Short mit Hebel ist zudem nur für institutionelle/professionelle Anleger mit Prime-Brokerage-Zugang praktikabel – keine Retail-Umsetzung ohne Derivate/gehebelte Produkte.

### g) Regimeabhängigkeit und Tail-Risiko

BAB ist strukturell zinssensitiv (Fundingkosten der Hebelseite) und daher in Phasen steigender Realzinsen (2022–2023) im Nachteil. Zusätzlich ist die Strategie durch die Kombination "Long gehebelt / Short ungehebelt" in Crash-Szenarien mit Deleveraging-Spiralen (Margin Calls, Prime-Broker-Rückzug) exponiert – genau das von Frazzini/Pedersen selbst beschriebene Leverage-Constraint-Regime kann sich in Stressphasen gegen den Anwender wenden (prozyklische Verschärfung von Margin-Anforderungen).

### h) Bekannte Kritik/Widerlegungen

Novy-Marx & Velikov (2022, 2025) ist die zentrale, technisch fundierte Widerlegung der Konstruktions-Reinheit des Originaleffekts. AQR/Frazzini/Pedersen haben in Reaktionsartikeln die praktische Relevanz und Cross-Asset-Konsistenz verteidigt, aber die Microcap-Tilt-Kritik nicht grundsätzlich entkräftet, sondern eher relativiert (z.B. mit Verweis auf liquiditätsgefilterte Produktversionen). Baltussen et al. liefern eine unabhängige, konvergente Kritik über den Lottery-Demand-Kanal.

**Fazit BAB: WEAK.** Eine ökonomisch kohärente Theorie (Leverage-Constraints, unterstützt durch Cross-Asset-Evidenz) trifft auf eine handwerklich fundierte, post-publikative Konstruktionskritik, die zeigt, dass die spektakuläre Originalgröße größtenteils ein Artefakt ist. Was übrig bleibt, überlappt stark mit der bereits bekannten Profitability-/Quality-Prämie. Realistische Netto-Sharpe-Erwartung nach Kosten/Hebel: niedrig (0,0–0,2 inkrementell), nicht null, aber kein eigenständiges robustes Alpha in der Größenordnung des Originalpapiers.

---

## Kandidat 2: Low-Volatility / Minimum-Variance Long-Only

### a) Ökonomische Begründung

Die long-only-Variante (Sortierung nach trailing realisierter Volatilität oder Beta, kein Hebel, keine strukturelle Short-Seite) wird primär durch **Baker, Bradley & Wurgler (2011, FAJ 67(1), 40–54)** fundiert: Benchmark-gebundene institutionelle Manager (gemessen an Information Ratio relativ zu einem kapitalisierungsgewichteten Index, ohne Hebeloption) meiden systematisch Low-Beta/Low-Vol-Aktien, weil deren Tracking Error zum Benchmark hoch, ihr erwarteter Alpha-Beitrag aber (unter Standardannahmen) klein erscheint. Das erzeugt eine strukturelle Nachfragelücke, die Low-Vol-Aktien unterbewertet lässt. Diese Erklärung ist unabhängig von Frazzini/Pedersens Leverage-Argument und erklärt speziell, warum die Anomalie **auch ohne Hebel** in long-only-Portfolios sichtbar ist.

### b) Limits to Arbitrage

Institutionelles Mandat-Design (Benchmarking) ist der zentrale Arbitragehemmnis-Kanal: Ein Manager, der stark von einem Cap-Weighted-Index abweicht, um Low-Vol-Aktien überzugewichten, nimmt Career-/Tracking-Error-Risiko auf sich, selbst wenn die erwartete risikoadjustierte Rendite höher ist. Dieser Mechanismus ist strukturell/institutionell und ändert sich nur langsam (Compensation-Strukturen, Consultant-Benchmarks) – potenziell **persistenter** als reine statistische Marktineffizienz.

### c) Originalstudien: Zahlen

Haugen & Baker (1991, "The Efficient Market Inefficiency of Capitalization-Weighted Stock Portfolios", Journal of Portfolio Management) sowie Haugen & Baker (1996): früheste systematische Dokumentation, dass die niedrigste-Varianz-Dezile über lange US-Stichproben (ab ca. 1929) höhere risikoadjustierte und teils sogar höhere absolute Renditen als die höchste-Varianz-Dezile erzielt – ohne moderne Multifaktor-Kontrolle, daher aus heutiger Sicht methodisch schwächer.

Blitz & van Vliet (2007, "The Volatility Effect", Journal of Portfolio Management, Robeco): globale Stichprobe, dokumentieren einen "Volatility Effect" mit deutlichem Renditespread zwischen niedrigster und höchster Volatilitätsdezile bei gleichzeitig geringerem realisiertem Risiko im Low-Vol-Portfolio.

Baker/Bradley/Wurgler (2011) liefern primär die Benchmarking-Erklärung, nicht primär neue Effektgrößenschätzungen – ihr Beitrag ist konzeptionell/erklärend.

### d) Out-of-Sample-/Post-Publication-Evidenz

**Novy-Marx (2014), "Understanding Defensive Equity"** (NBER WP 20591, SSRN 2513151) ist die zentrale Gegenkritik: Er zeigt, dass Defensive-Equity-/Low-Vol-Strategien ihre abnormale Performance größtenteils aus einem **Tilt zu profitablen, günstig bewerteten (teils kleineren Growth-)Aktien** ziehen. Profitability ist der stärkste Einzelprädiktor für niedrige Volatilität – stärker als Marktkapitalisierung. Kontrolliert man auf Size, Profitability und relative Bewertung, verschwindet die Low-Vol-Performance weitgehend; die Umkehrung gilt nicht (Value-/Profitability-Strategien lassen sich nicht durch Low-Vol-Exposure erklären). Novy-Marx' Schlussfolgerung: **Es wäre effizienter, Profitability und Value direkt zu targetieren, statt über den Umweg "niedrige Volatilität" zu gehen** – exakt die im Auftrag genannte Kritik "Low-Vol = teuer+Junk-Short" (hier: Low-Vol = indirektes/ineffizientes Profitability-Value-Proxy).

**Crowding/ETF-Evidenz (Websuche, Stand ca. Anfang/Mitte 2026)**: iShares MSCI USA Min Vol Factor ETF (USMV, aufgelegt 2011) verwaltet aktuell rund **23 Mrd. USD** (mehrere konsistente Quellen: 23,3–23,9 Mrd. USD). Zusammen mit SPLV, XMLV und globalen Pendants ergibt sich eine geschätzte Gesamtkapazität im Low-Vol-ETF-Segment im hohen zweistelligen bis niedrigen dreistelligen Milliarden-USD-Bereich (grobe eigene Schätzung, nicht durch eine einzelne Quelle belegt) – ein deutliches Crowding-Signal seit dem Produktlaunch-Boom ab 2011.

**Regimeabhängige Performance seit 2015**: 10-Jahres-annualisierte Rendite USMV ca. **10,4%**, SPLV ca. **8,7%** (Stand der Websuche-Ergebnisse, ca. November 2025) – SPLV (reiner Low-Vol/defensiver Sektor-Tilt: ~25% Utilities, ~21% Financials, ~18% Real Estate) underperformt gegenüber USMV (dessen Indexkonstruktion durch Optimierungsverfahren ca. 33% Tech-Exposure zulässt, näher am Cap-Weighted-Markt bleibt). Das ist selbst ein Beleg für die Novy-Marx-These: Je "reiner" die Volatilitäts-Sortierung (SPLV), desto schwächer die Rendite relativ zu einer Version, die durch Optimierungsrestriktionen näher an Marktfaktoren bleibt (USMV).

**2020-Evidenz (interne Kenntnis, nicht separat verifiziert)**: Im extremen Growth-/Tech-getriebenen Bullenmarkt 2020 haben Low-Vol-Strategien (insbesondere reine Varianten wie SPLV) deutlich hinter dem Cap-Weighted-Markt zurückgelegen (zweistellige Prozentpunkt-Differenz zum S&P 500 über das Jahr), weil Low-Vol-Sortierungen strukturell wachstumsstarke, hochbewertete Mega-Cap-Tech-Aktien untergewichten. Umgekehrt zeigten Low-Vol-ETFs im 2022er-Bärenmarkt und im 2025er "Bear Market" laut Websuche-Ergebnissen deutlich geringere Drawdowns (**ca. 9% vs. ca. 18%** beim S&P 500) – das defensive Profil ("weniger Verlust in Abschwüngen") ist empirisch robuster belegt als das Alpha-Profil ("mehr Rendite über einen vollen Zyklus").

### e) Kosten

Long-only Low-Vol/Min-Var-Portfolios haben moderaten Turnover (typischerweise vierteljährliches oder halbjährliches Rebalancing bei ETF-Indizes, ca. 20–40% p.a. Turnover je nach Methodik), sind primär in liquiden Large-/Mid-Caps investiert (geringe Spreads, geringer Market Impact) und benötigen keinen Hebel und keine Short-Seite. Dies ist die mit Abstand **kostengünstigste** und am einfachsten institutionell/retail-umsetzbare der drei hier untersuchten Strategien.

### f) Kapazität und Handelbarkeit

Hoch: Bereits heute Multi-Milliarden-USD-AUM in liquiden ETF-Wrappern gehandelt (USMV: ~23 Mrd. USD), ohne dass diese Produkte über Liquiditätsprobleme berichten. Long-only-Umsetzung ist Standard und retail-zugänglich. Das ist zugleich das Kapazitäts-Todesurteil aus Ineffizienz-Sicht: Ein Faktor mit derart hoher, seit 15 Jahren nachweisbarer Kapitalaufnahme sollte, wenn er ein echtes, begrenztes Ineffizienz-Alpha wäre, längst arbitriert worden sein. Dass die Produkte weiterhin Nettomittelzuflüsse verzeichnen und die Renditen (siehe oben) im Rahmen liegen, spricht eher für "strukturelle Beta-Variante mit Diversifikationsnutzen" als für "verstecktes Alpha".

### g) Regimeabhängigkeit und Tail-Risiko

Klar prozyklisch invers: Outperformance in Bärenmärkten/Korrekturen (Value-of-Defensiveness), Underperformance in scharfen, breiten, wachstumsgetriebenen Bullenmärkten (2020, 2023–2024, Mega-Cap-Tech-Rallye). Zinssensitivität indirekt über den Utilities-/Sektor-Tilt (bei reinen Low-Vol-Varianten wie SPLV): Diese Sektoren reagieren empfindlich auf Zinsänderungen (Bond-Proxy-Charakter), was in Hochzinsphasen zusätzliche Belastung bedeutet.

### h) Bekannte Kritik/Widerlegungen

Novy-Marx (2014) ist die zentrale akademische Widerlegung des "eigenständigen Alpha"-Anspruchs. Ergänzend: Der Verweis im Auftrag auf "Low-Vol = teuer+Junk-Short" (im Sinne von: die Short-Seite von Low-Vol-Long-Short-Konstruktionen besteht aus teuren, spekulativen "Junk"-Aktien) korrespondiert mit den BAB-Kritikpunkten aus Kandidat 1 (High-Beta/High-Vol-Seite = kleine, unprofitable, teure Growth-Aktien) sowie mit Novy-Marx' Befund, dass Aggressive-/High-Vol-Aktien überproportional "small, unprofitable, and growth firms" sind, was ihre schwache absolute Performance erklärt, ohne dass ein neuer Risikofaktor "Volatilität" nötig wäre.

**Fazit Low-Vol long-only: WEAK.** Robuste, gut reproduzierbare, kostengünstige und liquide Strategie mit dokumentiertem Diversifikations-/Drawdown-Reduktionsnutzen – aber die akademische Evidenz (Novy-Marx 2014) spricht stark dafür, dass das "Alpha" bereits vollständig durch Profitability und Value erklärt wird und kein inkrementeller Ineffizienz-Beitrag der Volatilitäts-Dimension selbst verbleibt. Für ein Portfolio, das bereits Quality/Value-Faktoren hält, ist der Zusatznutzen einer separaten Low-Vol-Sleeve fraglich. Als eigenständige "neue" Ineffizienz für dieses Mandat: nicht überzeugend.

---

## Kandidat 3: Idiosynkratische Volatilität (IVOL) – Ang et al. (2006)

### a) Ökonomische Begründung

Ang, Hodrick, Xing, Zhang (2006, Journal of Finance) dokumentieren, dass Aktien mit hoher idiosynkratischer Volatilität relativ zum FF3-Modell **abnorm niedrige** Folgerenditen aufweisen – ein Rätsel, weil idiosynkratisches Risiko nach Standardtheorie (CAPM/diversifiziertes Portfolio) nicht bepreist sein sollte, und wenn doch, dann mit **positivem** Vorzeichen (mehr Risiko = mehr erwartete Rendite), nicht negativem. Konkurrierende Erklärungsansätze:
- **Lottery Demand** (Bali/Cakici/Whitelaw 2011): Der MAX-Effekt (höchste tägliche Rendite im Vormonat) erklärt/kehrt den IVOL-Effekt um – Anleger zahlen für lotterieartige Schiefe, IVOL ist teilweise nur ein Proxy für MAX.
- **Arbitrage-Asymmetrie** (Stambaugh, Yu, Yuan 2015, Journal of Finance, "Arbitrage Asymmetry and the Idiosyncratic Volatility Puzzle"): Der IVOL-Effekt ist **negativ** unter überbewerteten/short-sale-constrained Aktien und **positiv** (!) unter unterbewerteten Aktien – die aggregierte Nettobeziehung erscheint negativ nur, weil Überbewertung/Leerverkaufsbeschränkung in der Praxis dominiert. Das ist eine genuine Mispricing-Geschichte, aber mit der unangenehmen Implikation, dass der ausnutzbare Teil primär auf der **Short-Seite überbewerteter, schwer leerverkaufbarer** Aktien liegt.

### b) Limits to Arbitrage

Genau hier liegt das Kernproblem: Der Effekt ist laut Stambaugh/Yu/Yuan am stärksten in genau dem Segment, das am teuersten/schwersten zu shorten ist (kleine, illiquide, hohe Borrow-Fees, manche gar nicht leihbar). Das ist ein Lehrbuchbeispiel für "Anomalie ökonomisch real, aber nicht handelbar": Das Vorhandensein des Effekts erklärt sich gerade dadurch, dass ihn niemand wegarbitrieren kann.

### c) Originalstudie: Zahlen

Ang et al. (2006): Spread zwischen niedrigstem und höchstem IVOL-Quintil (value-weighted, FF3-risikoadjustiert) **> 1% pro Monat**, robust gegenüber Size-, B/M-, Momentum- und Liquiditätskontrollen. International bestätigt in Ang et al. (2009, JFE) über 23 entwickelte Märkte hinweg (G7-ex-US-Spread laut interner Erinnerung ca. -1,3% pro Monat, hier nicht separat über Websuche verifiziert – mit Unsicherheit gekennzeichnet).

### d) Out-of-Sample-/Post-Publication-Evidenz

**Fu (2009)**: Mit einer EGARCH-basierten bedingten (statt realisierten) IVOL-Schätzung findet Fu einen **positiven** Zusammenhang zwischen IVOL und Folgerenditen – direkter Widerspruch zu Ang et al. Später zeigte sich (Guo/Savickas u.a., in der Literatur breit diskutiert), dass Fus Ergebnis stark durch **Look-ahead-Bias** in der EGARCH-Parameterschätzung (In-Sample-Parameter werden zur Konstruktion von Out-of-Sample-Signalen verwendet) getrieben war – nach Korrektur bricht der positive Zusammenhang weitgehend zusammen. Netto-Implikation: Vorzeichen und Robustheit des IVOL-Effekts sind **methodenabhängig**, was für eine Nullhypothese-freundliche Interpretation spricht (fragile Ergebnisse, hohe Spezifikationssensitivität).

**Huang, Liu, Rhee, Zhang (2010)**: Zeigen, dass ein wesentlicher Teil des IVOL-Effekts durch **kurzfristige Return-Reversal** (1-Monats-Mikrostruktur-/Bid-Ask-Bounce-Effekte) getrieben wird, nicht durch eine eigenständige Volatilitäts-Prämie. Kontrolliert man sauber auf Short-Term-Reversal, schwächt sich der IVOL-Effekt deutlich ab.

**Bali/Cakici/Whitelaw (2011)**: Ausdrücklich: "Including MAX reverses the puzzling negative relation between returns and idiosyncratic volatility." Das ist eine der schärfsten verfügbaren Widerlegungen – nicht nur Abschwächung, sondern **Vorzeichenumkehr** nach Kontrolle auf einen eng verwandten Faktor.

**McLean & Pontiff (2016)**: IVOL-artige Anomalien liegen im Bereich des Anomalie-Durchschnitts von ca. 58% In-Sample-zu-Out-of-Sample-Decay plus zusätzlichem Post-Publication-Rückgang – nicht auffällig robuster als der Median der über 90 getesteten Anomalien.

In Summe: IVOL ist von allen drei Kandidaten am stärksten durch die post-2006-Literatur **relativiert bis dekonstruiert** worden (Vorzeichenumkehr bei MAX-Kontrolle, Reversal-Kontamination, EGARCH-Spezifikationsfragilität).

### e) Kosten

Eine reine IVOL-Long-Short-Strategie erfordert Shorts im Hochvolatilitäts-Quintil – genau dem Segment mit den höchsten Spreads, höchsten Borrow-Fees und größtem Market Impact. In Kombination mit der Erkenntnis, dass ein signifikanter Teil des Effekts ohnehin Kurzfrist-Reversal-Rauschen ist (das bei monatlichem Rebalancing teilweise schon wieder verschwunden ist, wenn ein reales Portfolio tatsächlich handelt), ist die Kostenrobustheit dieser Anomalie die schwächste der drei Kandidaten.

### f) Kapazität und Handelbarkeit

Sehr gering. Der ausnutzbare Kern des Effekts (laut Stambaugh/Yu/Yuan) liegt in schwer leerverkaufbaren, kleinen, überbewerteten Aktien – das ist per Definition kapazitätsarm und für institutionelle Multi-Milliarden-Mandate nicht sauber skalierbar. Long-only-Umsetzung (nur die Long-Seite: niedrige IVOL kaufen) ist technisch möglich, verliert aber die Hälfte des theoretischen Effekts und überschneidet sich stark mit Kandidat 2 (Low-Vol long-only) und dessen Novy-Marx-Kritik.

### g) Regimeabhängigkeit und Tail-Risiko

Wie bei den anderen Kandidaten: prozyklisch invers zu spekulativen Bullenmärkten (hohe IVOL-Aktien = oft spekulative Growth-/Meme-artige Titel, die in Risk-on-Phasen outperformen), was die Short-Seite in genau solchen Phasen (z.B. 2020–2021 Retail-Trading-Boom, "Meme-Stock"-Episoden) mit erheblichem Tail-Risiko belastet – Short-Squeezes in stark long-vol-nachgefragten Titeln sind ein bekanntes, teils existenzbedrohendes Risiko für Short-IVOL-Bücher.

### h) Bekannte Kritik/Widerlegungen

Fu (2009) vs. Guo/Savickas-Kritik an Fu; Huang et al. (2010) Reversal-Kritik; Bali/Cakici/Whitelaw (2011) MAX-Vorzeichenumkehr; Stambaugh/Yu/Yuan (2015) Arbitrage-Asymmetrie (bestätigt den Effekt, lokalisiert ihn aber in nicht handelbarem Terrain). Insgesamt eine der am intensivsten "zerlegten" Anomalien der Faktorliteratur.

**Fazit IVOL: KILL.** Das statistische Phänomen ist real und international repliziert, aber (1) methodisch fragil (vorzeichenabhängig von Spezifikation), (2) größtenteils durch MAX/Lottery-Demand und Mikrostruktur-Reversal erklärbar, (3) in seinem "sauberen" verbleibenden Kern (Stambaugh/Yu/Yuan) gerade in dem Segment lokalisiert, das am wenigsten handelbar ist. Als eigenständige handelbare Strategie für ein institutionelles Mandat: nicht empfehlenswert.

---

## Übergreifende Synthese

**Gemeinsamer roter Faden aller drei Kandidaten**: Volatilität/Beta ist im Aktienquerschnitt kein eigenständiger, sauberer Preisfaktor, sondern in hohem Maße ein **Proxy-Bündel** aus Size, Profitability/Quality, Value und Lottery-Demand-Charakteristika. Jede der drei Originalstudien wurde durch spätere Arbeiten (Novy-Marx 2014 für Low-Vol/Defensive Equity, Novy-Marx & Velikov 2022/2025 für BAB, Bali/Cakici/Whitelaw 2011 + Fu 2009 + Huang et al. 2010 für IVOL) so weit seziert, dass der jeweils verbleibende "reine" Volatilitätsbeitrag klein bis nicht mehr nachweisbar ist.

**Kostenrobustheit** ist umgekehrt proportional zur "Reinheit" des jeweiligen Signals: Je näher eine Konstruktion am ursprünglichen akademischen Signal bleibt (kleine, illiquide, extreme Beta-/IVOL-Aktien; gehebelte Long-Short-Bücher), desto teurer und weniger kapazitätsstark ist sie – und genau dort sitzt der größte Teil des ursprünglich berichteten Alphas. Sobald man auf liquide, kapazitätsstarke, kostengünstige Umsetzung (z.B. USMV-Stil) filtert, nähert sich die Nettorendite dem an, was durch Quality/Value ohnehin erklärt wird.

**Crowding ist beobachtbar und quantifizierbar**: USMV allein verwaltet ca. 23 Mrd. USD (Stand der Websuche-Ergebnisse, ca. 2025/26), Low-Vol-ETFs insgesamt ein Vielfaches davon, seit dem Produktlaunch-Zyklus ab 2011 (unmittelbar nach/parallel zu Baker/Bradley/Wurgler 2011 und kurz vor Frazzini/Pedersen 2014). Das ist ein Lehrbuchfall für "Publikation → Kapitalzufluss → Crowding-getriebene Renditekompression", konsistent mit McLean/Pontiff (2016).

**Regimeabhängigkeit ist der praktisch bedeutsamste Befund für ein Fund-Mandat**: Alle drei Kandidaten liefern ihren Nutzen überwiegend als **Drawdown-Reduktion in Bärenmärkten**, nicht als robuste Outperformance über den vollen Zyklus. 2020 (Tech-Bullenmarkt) und 2023–2024 (KI-/Mega-Cap-Rallye) waren ausgeprägte Underperformance-Perioden für reine Low-Vol-Strategien; 2022 und der im Websuche-Material referenzierte "2025er Bärenmarkt" (S&P 500 ca. -18%, Low-Vol-Drawdown ca. -9%) waren Outperformance-Perioden. Das ist ökonomisch plausibel (defensive Charakteristik, Put-artiges Profil), aber es ist **Risikoprämie für Skew/Beta, nicht Alpha** im engeren Sinne – und die Frage, ob dafür eine positive Sharpe-Ratio-Prämie über den Zyklus bezahlt wird, bleibt nach der Konstruktionskritik unklar.

## Gesamturteil

Für das Mandat "Volatilitätsanomalien" komme ich zu einem überwiegend negativen, aber nicht vollständig nihilistischen Ergebnis:

- **BAB: WEAK.** Theoretisch am elegantesten fundiert (Leverage-Constraints, Cross-Asset-Evidenz), aber die Novy-Marx & Velikov (2022/2025)-Konstruktionskritik ist schwerwiegend und zeigt, dass ein Großteil der Originalgröße Artefakt ist. Was bleibt, überschneidet sich mit Quality.
- **Low-Vol long-only: WEAK.** Robust reproduzierbar, günstig, liquide, aber laut Novy-Marx (2014) im Kern ein indirektes Profitability-/Value-Proxy ohne inkrementelles Alpha; zusätzlich klar crowded (>20 Mrd. USD allein in USMV) und stark regimeabhängig (Underperformance in starken Bullenmärkten).
- **IVOL: KILL.** Statistisch real, aber methodisch fragil, größtenteils durch MAX/Lottery-Demand und Mikrostruktur-Reversal erklärt, und im verbleibenden "sauberen" Kern in nicht handelbarem Terrain (kleine, schwer leerverkaufbare Aktien) lokalisiert.

Diese Klasse liefert für ein institutionelles Alpha-Mandat kein überzeugendes CANDIDATE. Sie liefert am ehesten Argumente für eine **Risikomanagement-/Diversifikations-Sleeve** (Low-Vol long-only als Baustein neben Quality/Value, mit expliziter Erwartung von Zyklen-Underperformance in starken Bullenmärkten), nicht für eine eigenständige Alpha-Quelle. "Diese spezifische Erzählung (reine Volatilität als Preisfaktor) ist weitgehend widerlegt" ist meines Erachtens die ehrlichste Zusammenfassung – das im Auftrag angesprochene "diese Klasse ist tot"-Ergebnis trifft hier in abgeschwächter Form zu: nicht die zugrundeliegenden empirischen Renditemuster (die existieren), sondern die Interpretation als eigenständiges, handelbares "Volatilitäts-Alpha" jenseits von Quality/Value/Lottery-Demand.

---

### Quellenhinweise (über Websuche verifiziert bzw. referenziert)

- Novy-Marx, R. & Velikov, M. (2022). "Betting Against Betting Against Beta." *Journal of Financial Economics* 143(1), 80–106. Aktualisierte Fassung: "Betting Against (Bad) Beta" (2024/2025, *Quantitative Finance*, arXiv:2409.00416).
- Frazzini, A. & Pedersen, L.H. (2014). "Betting Against Beta." *Journal of Financial Economics* 111(1), 1–25. (Sharpe Ratio US-Equity-BAB 0,78, Stichprobe 1926–März 2012, via AQR/NBER-Quellen bestätigt.)
- Baker, M., Bradley, B. & Wurgler, J. (2011). "Benchmarks as Limits to Arbitrage: Understanding the Low-Volatility Anomaly." *Financial Analysts Journal* 67(1), 40–54.
- Novy-Marx, R. (2014). "Understanding Defensive Equity." NBER Working Paper 20591 / SSRN 2513151.
- Ang, A., Hodrick, R.J., Xing, Y. & Zhang, X. (2006). "The Cross-Section of Volatility and Expected Returns." *Journal of Finance* 61(1), 259–299.
- Ang, A., Hodrick, R.J., Xing, Y. & Zhang, X. (2009). "High Idiosyncratic Volatility and Low Returns: International and Further U.S. Evidence." *Journal of Financial Economics*.
- Bali, T.G., Cakici, N. & Whitelaw, R.F. (2011). "Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns." *Journal of Financial Economics* 99(2), 427–446.
- Stambaugh, R.F., Yu, J. & Yuan, Y. (2015). "Arbitrage Asymmetry and the Idiosyncratic Volatility Puzzle." *Journal of Finance*.
- McLean, R.D. & Pontiff, J. (2016). "Does Academic Research Destroy Stock Return Predictability?" *Journal of Finance*.
- Aktuelle ETF-Daten (USMV/SPLV AUM, 10-Jahres-Renditen, Drawdown-Vergleich 2025er Bärenmarkt): über Websuche im Juli 2026 erhoben, Sekundärquellen (TradingView, Mezzi, diverse ETF-Datenaggregatoren) — Einzelwerte nicht durch Primärquelle (Fondsprospekt/SEC-Filing) gegengeprüft, daher mit moderater Unsicherheit zu behandeln.
- Fu, F. (2009); Huang, W., Liu, Q., Rhee, S.G. & Zhang, L. (2010); Haugen, R.A. & Baker, N.L. (1991, 1996); Blitz, D. & van Vliet, P. (2007); Baltussen, G., van Vliet, P. et al. (Lottery-Demand-Kritik an BAB): Zahlen/Befunde aus internem Wissen (Trainingsstand Anfang 2026), nicht in dieser Sitzung einzeln über Websuche gegengeprüft — Evidenzbasis für diese spezifischen Punkte: **internes Wissen, Stand Anfang 2026**.
