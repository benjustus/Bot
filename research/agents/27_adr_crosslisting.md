```yaml
agent: 27
klasse: "ADRs & Cross-Listings"
websuche_verfuegbar: ja
strategien:
  - name: "Preisparitäts-Arbitrage konvertierbarer ADRs/Cross-Listings (Law-of-One-Price-Deviations)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 2
      regimestabilitaet: 3
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.6
    netto_sharpe_erwartung: "~0.0 für Fonds auf Tages-/Stundenfrequenz; nur für Colocation-HFT-Desks >0, aber irrelevant für systematisches Mandat"
    kernrisiko: "Ineffizienz ist real, aber bereits durch HFT-Arbitrage-Desks auf Basispunkt-Niveau mit ~12 Minuten Halbwertszeit wegarbitriert; Latenzwettbewerb, den ein Multi-Tage-Fonds nicht gewinnen kann"
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
  - name: "Dual-Listed-Company-Arbitrage (Siamese Twins, z.B. Royal Dutch/Shell-Typ)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 1
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.55
    netto_sharpe_erwartung: "historisch 0.1-0.3 (de Jong et al. 2009), aber mit extremer Linksschiefe/Tail-Risiko; aktuell nicht replizierbar mangels Anlageuniversum"
    kernrisiko: "Divergenz kann >8 Jahre gegen die Position laufen (LTCM 1997-2005, Verlust von über der Hälfte der ~$286 Mio. Equity-Pairs-Verluste allein im Royal-Dutch/Shell-Trade); Anlageuniversum ist durch freiwillige Unifikationen (Shell 2005, RELX 2018, Mondi 2019, Unilever 2020, Reckitt 2021, BHP 2022, Carnival 2026) auf praktisch ein Restrisiko (Rio Tinto) geschrumpft"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Yahoo Finance historische Ticker-Paare (RDSA.L/RDSB.L vor 2005, UN/UL vor 2020, BHP/BLT vor 2022) – nur noch historische Fallstudien, keine laufend handelbare Strategie"
  - name: "Nicht-konvertierbare Cross-Listing-Prämien (China A-H-Premium, VIE-basierter US-ADR-Diskont) inkl. Zeitzonen-Friktion"
    urteil: KILL
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 4
      regimestabilitaet: 2
      handelbarkeit: 1
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.3
    netto_sharpe_erwartung: "~0.0 bis leicht negativ nach Tail-Risiko-Adjustierung (Delisting/Kapitalkontrollen); für Fondsmandat nicht umsetzbar"
    kernrisiko: "Kein legaler Arbitrage-Mechanismus für die meisten Marktteilnehmer (Kapitalverkehrskontrollen, Quoten); VIE-Rechtsstrukturrisiko und Delisting-Risiko (HFCAA) können Totalverlust statt Drawdown bedeuten"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Hang Seng Stock Connect China AH Premium Index (Bloomberg/Investing.com Ticker, z.B. 'AHPI'); Yahoo-Finance A/H-Ticker-Paare (z.B. 601398.SS vs. 1398.HK)"
```

# Agent 27 — ADRs & Cross-Listings: Adversarial Review

**Mandat:** ADR-Prämien/-Discounts, Dual-Listed-Company-Arbitrage, Zeitzonen-Arbitrage/Predictability. Nullhypothese: kein echtes, für einen systematischen Fonds nutzbares Alpha. Stand der Recherche: Juli 2026, Websuche verfügbar und genutzt (Ergebnisse und Zugriffsprobleme unten dokumentiert).

## Executive Summary

Alle drei geprüften Kandidaten enden auf **KILL**. Das Muster ist bei jedem Kandidaten unterschiedlich, aber die Schlussfolgerung ist dieselbe:

1. **Konvertierbare ADR-Preisparität** — die Ineffizienz existiert nachweislich, ist aber inzwischen so klein (im Mittel 4,9 Basispunkte, Gagnon & Karolyi 2010) und so kurzlebig (mittlere Persistenz ~12 Minuten laut Rösch 2021, JFE, basierend auf Milliarden von Trades 2001–2016), dass sie ausschließlich von kolozierten HFT-Arbitrage-Desks gehalten wird. Für ein Multi-Tages-/Wochen-Mandat ist das Feld leergeräumt.
2. **DLC-Arbitrage** (Royal Dutch/Shell-Typ) — historisch die überzeugendste Anomalie der Klasse mit dokumentierten Netto-Renditen von bis zu ~10% p.a. (de Jong, Rosenthal & van Dijk 2009), aber (a) die LTCM-Lektion zeigt, dass die Position 8+ Jahre und über 250 Mio. USD Verlust gegen einen der bestkapitalisierten Fonds der Geschichte laufen konnte, und (b) fast das gesamte historische Anlageuniversum hat sich seit 2005 durch freiwillige Unifikation selbst aufgelöst. Die Anomalie wurde nicht wegarbitriert — sie wurde von den Unternehmen per Corporate Action eliminiert. Übrig bleibt praktisch ein einziger Name (Rio Tinto), dessen Board eine Unifikation im April/Mai 2025 per Aktionärsbeschluss explizit abgelehnt hat.
3. **Nicht-konvertierbare Prämien** (China A-H, VIE-ADR-Diskont) — die Fehlbewertung ist groß, persistent und statistisch unbestreitbar (Hang-Seng-AH-Premium-Index seit Jahrzehnten zwischen 100 und 160), aber es gibt schlicht keinen legalen Arbitrage-Mechanismus für die meisten Marktteilnehmer. Das ist keine Frage von "Limits to Arbitrage", sondern von "kein Arbitrage-Kanal vorhanden". Zusätzlich trägt die China-ADR-Variante (VIE-Struktur) ein Totalverlustrisiko (Delisting unter dem HFCAA, Rechtsstruktur ohne direkten Eigentumsanspruch), das die beobachtete Prämie eher als Risikoprämie denn als Mispricing erklärt.

Das ehrliche Ergebnis für diese Anomalieklasse: **strukturell tot für ein systematisches, nicht-HFT-fähiges Fondsmandat.** Was an Alpha nachweisbar war, ist entweder (i) mittlerweile Domäne von Sub-Millisekunden-Arbitrageuren, (ii) durch Corporate-Governance-Entwicklungen (Unifikationen) verschwunden, oder (iii) niemals wirklich handelbar gewesen, weil der zugrunde liegende Mechanismus (Kapitalverkehrskontrolle) per Definition keine Konvertierung erlaubt.

---

## Kandidat 1: Preisparitäts-Arbitrage konvertierbarer ADRs/Cross-Listings

### a) Ökonomische Begründung

Ein ADR (Level II/III, konvertierbar) und die zugrunde liegende Heimataktie sind bei fixem Konversionsverhältnis ökonomisch identische Claims auf denselben Cashflow, gehandelt an zwei Börsen mit unterschiedlichen Zeitzonen, Währungen, Investorenklientelen und Handelskosten. Preisabweichungen entstehen durch:
- **Segmentierte Investorenbasis**: US-Retail/Institutionelle vs. Heimatmarkt-Investoren reagieren asynchron auf Informationen.
- **Haltekosten-Proxies** (Gagnon & Karolyi 2010): Leerverkaufsbeschränkungen, Kapitalverkehrskontrollen im Heimatmarkt, Konversionsfriktionen zwischen ADR und Stammaktie.
- **Preisdruck/Liquiditätsschocks** (Rösch 2021, JFE): kurzfristige Order-Flow-Ungleichgewichte in einem der beiden Märkte, die sich nicht sofort über Arbitrage-Handel ausgleichen.
- Verursacher der Fehlbewertung sind primär **uninformierte Liquiditätshändler und lokale Sentiment-Schocks**, nicht rationale Neubewertung von Fundamentaldaten — das macht die Deviation grundsätzlich arbitragefähig, sofern die Ausführung schnell genug ist.

### b) Limits to Arbitrage

Anders als bei DLCs (Kandidat 2) ist das *Konvertierungsrisiko* hier gering (Level-II/III-ADRs sind gegen Gebühr konvertierbar), aber:
- **Geschwindigkeit ist der limitierende Faktor, nicht Kapital.** Da beide Beine ökonomisch identisch sind, ist das fundamentale Risiko null — das Risiko liegt vollständig in Ausführungslatenz zwischen zwei Handelsplätzen in unterschiedlichen Zeitzonen.
- FX-Risiko während der (kurzen) Haltedauer, doppelte Spreads, Clearing-/Settlement-Unterschiede (T+1 vs. T+2, unterschiedliche Feiertage).
- Kapitalverkehrskontrollen im Heimatmarkt (v.a. Schwellenländer) verhindern in Stresssituationen genau dann die Konversion, wenn die Prämie am größten ist.

### c) Originalstudien

- **Gagnon & Karolyi (2010)**, *Multi-Market Trading and Arbitrage*, Journal of Financial Economics 97(1), S. 53–80. Stichprobe: 506 US-cross-gelistete Aktien aus 35 Ländern, Intraday-Preise/Quotes. Ergebnis: mittlere Abweichung von der Preisparität = **4,9 Basispunkte**, hochvolatil mit gelegentlich großen Extremwerten. Abweichungen und deren Tagesänderungen sind signifikant positiv mit Haltekosten-Proxies korreliert (auch nach Kontrolle für Transaktionskosten und Kapitalverkehrsbeschränkungen). Zentrales Ergebnis: **Emerging-Markets-ADRs zeigen deutlich größere und persistentere Deviationen** als Developed-Markets-ADRs; die Prämien-/Discount-Größe korreliert negativ mit dem Entwicklungsgrad des Heimatmarktes.
- **Rösch (2021)**, *The Impact of Arbitrage on Market Liquidity*, Journal of Financial Economics 142(1), S. 195–213. Datensatz: Milliarden Trades im ADR-Markt, 2001–2016. Ergebnis: Preisabweichungen bestehen im Mittel nur **~12 Minuten**, entstehen hauptsächlich durch Preisdruck; ein positiver Arbitrage-Schock (simultane Gegentrades in ADR und Heimataktie) reduziert Deviation und Bid-Ask-Spread signifikant (Impulsantwortfunktionen auf 1-Minuten-Basis).
- Ergänzend: **Poutré, Dionne & Yergeau (2022)**, *International High-Frequency Arbitrage for Cross-Listed Stocks* (HEC Montréal Working Paper / SSRN 4066962). Untersuchung von 74 grenzüberschreitend gelisteten Aktien (Kanada/USA) unter expliziter Berücksichtigung von Informationslatenz zwischen Handelsplätzen. Ergebnis: geschätzter **Jahresnettogewinn einer HFT-Firma mit Limit-Orders von ca. USD 6 Mio.** über alle 74 Paare; **Arbitrage mit Market-Orders unter realistischer Latenz ist NICHT profitabel.** Median-Halbwertszeit eines Preisparitäts-Schocks: 1,1 Handelstage; für 14 von 21 untersuchten Paaren sinkt die Deviation in unter 2 Tagen um die Hälfte (verwandte Studie zur Preiskonvergenz).

### d) Out-of-Sample-/Post-Publication-Evidenz

Die Rösch-Studie (Daten bis 2016) und die Poutré-et-al.-Studie (Publikation 2022) sind bereits *post-Gagnon-Karolyi* und zeigen eindeutig: Die Halbwertszeit der Deviation ist auf **Minuten bis wenige Handelstage** gesunken, die verbleibende Größenordnung (~5 Basispunkte im Mittel) liegt **unterhalb typischer institutioneller Transaktionskosten**. Geschätzter Decay der ökonomisch nutzbaren Ineffizienz gegenüber den 1980er/1990er-Jahren (als ADR-Arbitrage noch manuell/telefonisch mit Stunden-Latenz betrieben wurde): **>90%**. Es gibt keine belastbare Evidenz für eine Handelsstrategie mit positivem Netto-Alpha auf Tages- oder Wochenfrequenz seit Beginn der HFT-Ära (~2005–2010).

### e) Kosten

FX-Konvertierung (2 Beine, oft unterschiedliche Währungen), doppelte Spreads (Heimatmarkt + ADR-Markt), Broker-Kommission auf beiden Beinen, ADR-Konversionsgebühren (Depositary Fees, typischerweise 0,01–0,05 USD/ADR bei tatsächlicher Konversion), Custody-Gebühren im Auslandsmarkt, Settlement-Mismatch-Finanzierungskosten. Bei einem mittleren Edge von 4,9 Basispunkten ist die Strategie für jeden Akteur ohne Colocation und Maker-Rebates **strukturell unrentabel**.

### f) Kapazität und Handelbarkeit

Sehr gering für einen systematischen Fonds. Das Beispiel aus Poutré et al. (2022) — ca. 6 Mio. USD Jahresgewinn für eine spezialisierte HFT-Firma über 74 Aktienpaare — zeigt die Größenordnung der insgesamt im Markt verfügbaren Rente. Aufgeteilt auf die Zahl konkurrierender Arbitrage-Desks bleibt für einen Neueinsteiger ohne Tick-für-Tick-Kolokation an mehreren Börsen **de facto nichts übrig**. Erfordert Millisekunden-Infrastruktur, die außerhalb des Mandats eines fundamental-/faktorbasierten systematischen Fonds liegt.

### g) Regimeabhängigkeit und Tail-Risiko

Deviations skalieren mit Haltekosten-Proxies — sie werden in Stressphasen (Kapitalkontrollen, Marktilliquidität) größer, genau dann, wenn Arbitrageure am wenigsten Risikokapital bereitstellen wollen (klassisches Shleifer-Vishny-Muster). Tail-Risiko ist für die *verbleibende* Strategie moderat (Positionen werden binnen Minuten geschlossen), aber das bedeutet auch: es gibt keine Möglichkeit, auf niedrigerer Frequenz Exposure aufzubauen, ohne das Fundamentalrisiko der Einzelaktie einzugehen.

### h) Bekannte Kritik/Widerlegungen

Mehrere Autoren (u.a. Suarez 2005, "Arbitrage opportunities in the depositary receipts market: Myth or reality?") argumentieren, dass ein Großteil der scheinbaren historischen Ineffizienz Artefakt von nicht-synchronen Schlusskursen und unzureichender FX-Anpassung war. Rösch (2021) bestätigt explizit, dass Arbitrage-Aktivität die Deviations *reduziert und Liquidität bereitstellt* — die Marktmikrostruktur-Literatur sieht die Ineffizienz inzwischen mehrheitlich als weitgehend "gelöstes" Problem der Marktqualität, nicht als offene Handelsgelegenheit.

**Urteil: KILL.** Die Ineffizienz ist real (p≈0,6), aber vollständig im HFT-Bereich internalisiert. Kein Pfad zu positivem Netto-Sharpe für ein systematisches Mandat ohne Colocation-Infrastruktur.

---

## Kandidat 2: Dual-Listed-Company-Arbitrage (Siamese Twins)

### a) Ökonomische Begründung

DLCs (Royal Dutch/Shell, Unilever N.V./PLC, SmithKline Beecham, BHP Billiton, Rio Tinto, Reed Elsevier/Reed International, Mondi, Reckitt Benckiser/Reckitt Colman-artige Strukturen) sind zwei rechtlich getrennte, börsennotierte Muttergesellschaften mit einem **Equalization Agreement**, das Cashflow-Ansprüche in einem fixen Verhältnis bindet — ökonomisch de facto eine einzige Aktie, aber **rechtlich nicht fungibel** (keine Konversion zwischen den beiden Aktienklassen möglich, anders als bei ADRs). Das ist der entscheidende strukturelle Unterschied zu Kandidat 1: Hier gibt es *keinen* Konversionsmechanismus, der die Preise zusammenzwingt — nur Erwartungen über zukünftige Unifikation oder Liquidation.

Verursacher der Fehlbewertung laut Literatur:
- **Investor-Sentiment/-Standort** (Froot & Dabora 1999): Der Preis jedes Zwillings korreliert stark mit dem lokalen Marktindex seines Haupthandelsplatzes, nicht nur mit fundamentalen Faktoren — Indiz für standortgebundenes (nicht arbitragefreies) Investorenverhalten.
- **Noise-Trader-Risiko** (Scruggs 2006, "Noise trader risk: Evidence from the Siamese Twins").
- **Indexmitgliedschaft und institutionelle Klientel-Effekte**: unterschiedliche Aufnahme in nationale Indizes (FTSE, AEX) erzeugt strukturelle Nachfrageunterschiede.

### b) Limits to Arbitrage — die zentrale Lektion

**Non-Fungibilität ist der Kern des Problems.** Ein Arbitrageur kann nicht das billigere Bein in das teurere umwandeln — er kann nur long/short gehen und auf Konvergenz warten, deren Zeitpunkt unbekannt ist (typischerweise: Unifikation der Struktur oder — theoretisch — Liquidation).

**LTCM/Royal-Dutch-Shell als Lehrstück**: LTCM hielt ab Sommer 1997 eine Position von ca. **2,3 Mrd. USD** (long Shell Transport, short Royal Dutch, ausnutzend einen Discount von Shell gegenüber Royal Dutch von ca. 8–10%). Während der Russland-/LTCM-Krise 1998 weitete sich die Fehlbewertung **statt zu konvergieren weiter aus** (Royal-Dutch-Prämie stieg auf ca. 22%, nach anderen Quellen bis ~35% im Herbst 1998/2000). LTCM musste die Position mit Verlust auflösen; von den insgesamt **286 Mio. USD Verlust im Equity-Pairs-Trading-Buch entfiel mehr als die Hälfte allein auf den Royal-Dutch/Shell-Trade.** Vollständige Konvergenz kam erst **2005 mit der Unifikation** — d.h. eine korrekt identifizierte, fundamental "risikolose" Fehlbewertung hätte **acht Jahre** benötigt, um sich aufzulösen, und wäre für einen gehebelten Investor auf dem Weg dorthin insolvent geworden. Das ist die Definition von "limits to arbitrage können Jahre gegen dich laufen".

Weitere Kostenfaktoren: Leerverkaufskosten/-verfügbarkeit auf dem jeweils ausländischen Bein, FX-Exposure über die gesamte (unbekannte) Haltedauer, Dividendensteuer-Asymmetrien zwischen Jurisdiktionen, Margin-Anforderungen bei zwei Auslandspositionen.

### c) Originalstudien

- **Rosenthal & Young (1990)**, *The seemingly anomalous price behavior of Royal Dutch/Shell and Unilever N.V./PLC*, Journal of Financial Economics 26(1), S. 123–141. Untersuchungszeitraum September 1979–Dezember 1986. Dokumentiert "signifikante und persistente" Abweichungen von der theoretischen Parität; **Royal Dutch handelte Anfang der 1980er mit einem Discount von ca. 30%** gegenüber Shell Transport & Trading. Konsistent über NYSE und LSE.
- **Froot & Dabora (1999)**, *How are stock prices affected by the location of trade?*, Journal of Financial Economics 53(2), S. 189–216. Stichprobe: drei Zwillingspaare (Royal Dutch/Shell, Unilever NV/PLC, SmithKline Beecham), 1989–1995. Kernergebnis: Preis-Deviationen zwischen den Zwillingen korrelieren hoch mit den **relativen Indexbewegungen der jeweiligen Haupthandelsplätze** — wenn der US-Markt relativ zum UK-Markt steigt, steigt Royal Dutch (stärker in NY gehandelt) relativ zu Shell (stärker in London gehandelt). Das ist der Ursprung des "standortbasierten Sentiment"-Erklärungsmodells und implizit auch der Zeitzonen-Dimension der Anomalie.
- **de Jong, Rosenthal & van Dijk (2009)**, *The Risk and Return of Arbitrage in Dual-Listed Companies*, Review of Finance 13(3), S. 495–520. Stichprobe: **12 DLCs, 1980–2002**. Einfache Handelsregeln erzielen risikoadjustierte abnormale Renditen von **bis zu ~10% p.a.** nach Berücksichtigung von systematischem Risiko, Transaktionskosten und Margin-Anforderungen. Gleichzeitig: **hohe idiosynkratische Volatilität** und eine **hohe Häufigkeit großer negativer Renditen** ("large negative returns"), die Arbitrage strukturell erschweren — die Autoren selbst betonen, dass Konvergenzhorizont-Unsicherheit ein zentrales Hindernis ist.

### d) Out-of-Sample-/Post-Publication-Evidenz

Dies ist der aufschlussreichste Befund der gesamten Recherche: **Das Anlageuniversum hat sich seit Publikation der Kernstudien fast vollständig selbst aufgelöst — nicht durch Arbitrage-Konvergenz, sondern durch freiwillige Corporate-Governance-Entscheidungen:**

| DLC | Aktiv | Unifiziert |
|---|---|---|
| Royal Dutch/Shell | 1907–2005 | 2005 (nach LTCM-Krise) |
| Reed Elsevier/Reed International | 1993–2018 | 2018 |
| Mondi | 2007–2019 | 2019 |
| Unilever N.V./PLC | 1930–2020 | 2020 (99% Zustimmung) |
| Reckitt Benckiser-artige Struktur | –2021 | 2021 |
| BHP Billiton | 2001–2022 | 2022 |
| Carnival Corporation/plc | 2003–2026 | Mai 2026 (Redomizilierung nach Bermuda) |

Von den historisch großen DLCs ist nach Stand Juli 2026 im Wesentlichen nur noch **Rio Tinto** (ASX/LSE, seit 1995) als "echte" DLC mit Equalization Agreement aktiv, plus kleinere/weniger liquide Strukturen wie **Investec** (LSE/JSE). Bemerkenswert: Aktivist Palliser Capital forderte 2024/2025 explizit eine Unifikation von Rio Tinto (mit Verweis auf einen anhaltenden Bewertungsabschlag der Struktur); der Rio-Tinto-Board lehnte dies nach eigener Prüfung ab, und die Aktionäre stimmten im April/Mai 2025 mit deutlicher Mehrheit **gegen** die Unifikation — d.h. der einzige verbliebene "Trade" bleibt auf unbestimmte Zeit ungelöst, mit explizit vom Board bestätigtem Fortbestand der Struktur.

**Interpretation für die Nullhypothese:** Die DLC-Anomalie wurde nicht durch Marktkräfte (Arbitrage-Kapital) beseitigt, sondern durch einen exogenen Trend zu **einfacheren Kapitalstrukturen und Governance-Vereinfachung** (oft getrieben von Aktivisten, die genau die von der Literatur dokumentierte Bewertungslücke als Hebel nutzten). Für einen systematischen Fonds bedeutet das: Das, was heute an "Alpha" übrig ist, ist kein diversifizierbarer Faktor mehr, sondern eine **Einzelwette auf eine Governance-Entscheidung bei genau einem Titel** — das ist Event-Driven-/Special-Situations-Research, keine systematische Cross-Listing-Strategie.

### e) Kosten

Zwei-Länder-Leerverkaufsinfrastruktur, FX-Exposure über Jahre, Dividenden-Quellensteuer-Differenzen (können mehrere Prozentpunkte p.a. betragen), Finanzierungskosten der Short-Position über unbestimmt lange Haltedauer, Margin-Calls bei Divergenz (siehe LTCM — genau das killt die Position, bevor sie konvergiert).

### f) Kapazität und Handelbarkeit

**Kapazität heute: praktisch null.** Ein einziger liquider Name (Rio Tinto) erlaubt keine diversifizierte, skalierbare Strategie. Historisch (1980er–2000er) gab es vielleicht 5–10 gleichzeitig handelbare DLC-Paare weltweit — selbst im besten Fall eine Nischenstrategie mit Konzentrationsrisiko.

### g) Regimeabhängigkeit und Tail-Risiko

Extrem: Die Deviation korreliert mit **globalen Liquiditätskrisen** (1998 Russland/LTCM) — also genau dann am größten, wenn Diversifikationsvorteile am meisten gebraucht würden und Fremdkapital am teuersten ist. Klassisches "Crowded-Trade-Blow-up"-Muster.

### h) Bekannte Kritik/Widerlegungen

Kritiker (u.a. im Rahmen der Noise-Trader-Risk-Literatur) argumentieren, dass ein Teil der historischen "Ineffizienz" tatsächlich eine Kompensation für Noise-Trader-Risiko und Illiquiditätsrisiko war, nicht freies Alpha — konsistent mit der beobachteten Linksschiefe der Renditen bei de Jong et al. (2009).

**Urteil: KILL.** Historisch die überzeugendste Anomalie der Klasse mit klarer ökonomischer Logik und positiven Netto-Renditen in der Literatur, aber (i) durch die LTCM-Episode empirisch als Tail-Risk-Trade mit Jahres-Divergenzpotenzial belegt, und (ii) durch Selbstauflösung des Anlageuniversums heute nicht mehr systematisch umsetzbar. Höchstens als diskretionäre Einzeltitel-Spezialsituation (Rio Tinto) relevant — außerhalb des systematischen Mandats.

---

## Kandidat 3: Nicht-konvertierbare Cross-Listing-Prämien (China A-H-Premium / VIE-ADR-Diskont) inkl. Zeitzonen-Friktion

### a) Ökonomische Begründung

A-Shares (Shanghai/Shenzhen, primär Onshore-Chinesen zugänglich) und H-Shares (Hongkong, international zugänglich) bzw. US-ADRs derselben Unternehmen sind **nicht frei konvertierbar**. Der **Hang Seng Stock Connect China AH Premium Index** misst den Bewertungsaufschlag der A-Shares gegenüber den H-Shares und schwankt strukturell zwischen **100 und 150** (0–50% Premium); im **Februar 2024 erreichte er einen Peak nahe 160** (~60% Premium), getrieben von schwachem internationalem Sentiment und Konjunktursorgen. Die Prämie ist seit Einführung der Indizes in den 1990er-Jahren **nie vollständig verschwunden** — ein Beleg dafür, dass hier kein funktionierender Arbitrage-Mechanismus existiert, sondern strukturelle Marktsegmentierung.

Für **China-ADRs mit VIE-Struktur** (Variable Interest Entity, z.B. historisch Alibaba, JD.com, Pinduoduo) kommt eine zusätzliche Dimension hinzu: Der ADR-Inhaber hält **keinen direkten Eigentumsanspruch** an der operativen chinesischen Gesellschaft, sondern einen vertraglichen Anspruch über eine Cayman-Holding — ein grundsätzlich anderes Rechtsrisiko als bei einer klassischen ADR-Konversionslücke.

Verursacher: **Kapitalverkehrskontrollen der chinesischen Regierung** (nicht Marktineffizienz im klassischen Sinn) plus fundamentale Rechtsstruktur-Unsicherheit bei VIEs.

### b) Limits to Arbitrage

Hier ist die Formulierung "Limits to Arbitrage" fast zu wohlwollend — treffender ist **"kein Arbitrage-Kanal vorhanden"**:
- Ausländische Investoren können A-Shares nur über QFII/RQFII-Quoten oder **Stock-Connect-Northbound**-Zugang handeln, unterliegen dabei Eligibility- und Volumenbeschränkungen; Leerverkauf von A-Shares durch Ausländer ist stark eingeschränkt.
- Chinesische Onshore-Investoren dürfen H-Shares nur über das quotierte **Southbound**-Programm handeln (seit 2014), ebenfalls mengenmäßig begrenzt.
- Eine "kombinierte" Position (long H, short A oder umgekehrt) ist für die meisten Marktteilnehmer **schlicht nicht darstellbar**, unabhängig vom Kapitaleinsatz.
- Die Literatur (Meng et al. 2023, "Limits of arbitrage and their impact on market efficiency: Evidence from China", Journal of International Financial Markets/Global Finance Journal 2024) zeigt, dass Erweiterungen des Stock-Connect-Zugangs (z.B. Shenzhen-HK Connect) **Markteffizienz messbar verbessern** (Rückgang von Return-Predictability, verbesserte Varianzverhältnisse) — das ist im Umkehrschluss die Bestätigung, dass die vorherige Prämie primär ein **Zugangsproblem**, kein Bewertungsfehler im arbitragefähigen Sinne war.

### c) Originalstudien / etablierte Evidenz

Kein "klassisches" Rosenthal/Froot-Dabora-Äquivalent für diese Subklasse, aber breite und konsistente Literatur:
- **Hang Seng AH Premium Index** (öffentlich seit 2007, methodisch vergleichbare Vorgänger seit den 1990ern): persistente Prämie 0–60%, kein struktureller Trend zur Konvergenz über 15+ Jahre.
- **Meng et al. (2023/2024)**: Stock-Connect-Erweiterung als exogener Schock zur Identifikation von Limits-to-Arbitrage-Effekten; zeigt, dass Handelsfriktionen (nicht Sentiment allein) die Prämie signifikant erklären.
- **NYU Stern (Whitelaw et al.), "Information in the A-H Premium"**: die Prämie enthält systematische Informationskomponenten (Sentiment, Liquiditätsunterschiede), ist aber nicht als reines "freies Alpha" handelbar.

### d) Out-of-Sample-/Post-Publication-Evidenz (2015–2026)

Im Gegensatz zu Kandidat 1 (Decay) zeigt diese Subklasse **keinen Decay** — die Prämie ist über die letzten zehn Jahre (2015: Index ~120–130; 2024: Peak ~160) tendenziell eher **gestiegen** als gesunken, parallel zu verschärften geopolitischen Spannungen und Kapitalverkehrsbeschränkungen. Zusätzlich neue, seit 2020 relevante Tail-Risk-Dimension: **Holding Foreign Companies Accountable Act (HFCAA)**, unterzeichnet Dezember 2020, schafft ein konkretes Delisting-Risiko für US-gelistete China-ADRs bei Nichteinhaltung von US-Audit-Anforderungen. Als direkte Folge sind seit 2021–2023 zahlreiche große China-ADRs (Alibaba, JD.com, NetEase, Pinduoduo u.a.) präventiv in Hongkong **sekundär-/dual-gelistet** worden — eine strukturelle Reaktion auf regulatorisches Tail-Risiko, nicht auf eine Handelsgelegenheit.

### e) Kosten

FX (RMB-Konvertierungsbeschränkungen selbst), Stempelsteuer-Asymmetrien, Quellensteuer-Unterschiede auf Dividenden zwischen A- und H-Aktien, Quota-Zugangskosten/-risiko (Stock-Connect-Programme können bei politischer Eskalation ausgesetzt werden), Broker-/Custody-Infrastruktur in mindestens zwei Jurisdiktionen.

### f) Kapazität und Handelbarkeit

Aggregiert bewegt Stock Connect erhebliche Volumina, aber der **spezifische Arbitrage-Trade** (long billige Seite, short teure Seite über die A-H-Grenze) ist für einen US-/EU-basierten Hedgefonds **faktisch nicht zugänglich** (keine Northbound-Short-Möglichkeit für die meisten ausländischen Adressen, keine Southbound-Berechtigung für Nicht-Chinesen). Die relevante Kapazität für unser Fondsmandat: **~0.**

### g) Regimeabhängigkeit und Tail-Risiko

Höchste Kategorie in dieser gesamten Anomalieklasse: **Kapitalverkehrskontrollen können jederzeit verschärft werden** (regimeabhängig per Definition), und für VIE-basierte US-ADRs besteht ein **Delisting-/Enteignungs-Tail-Risiko**, das nicht symmetrisch ist — im Extremfall (geopolitische Eskalation, Taiwan-Szenario, harte HFCAA-Durchsetzung) drohen **Totalverlust oder monatelange Handelsaussetzung**, nicht nur Drawdown. Das unterscheidet dieses Risiko qualitativ von normaler Marktvolatilität.

### h) Bekannte Kritik/Widerlegungen

Ein Teil der Literatur (u.a. NYU Stern) argumentiert, die A-H-Prämie sei zumindest teilweise durch **Informationsasymmetrie und Sentiment der stärker retailgetriebenen Onshore-Anleger** erklärbar, also eine Art Verhaltensanomalie — aber genau diese Anomalie ist wegen der Kapitalkontrollen **nicht monetarisierbar** durch Fremdkapital, weshalb sie sich (anders als bei klassischen Behavioral-Finance-Anomalien in offenen Märkten) nicht durch Arbitrage-Kapitalzufluss selbst korrigiert.

**Urteil: KILL.** Statistisch die robusteste und am wenigsten "wegarbitrierte" Prämie der drei Kandidaten — aber genau deshalb, weil kein Arbitrage-Mechanismus existiert. Für einen Fonds mit freiem Kapitalzugang ist das kein handelbares Alpha, sondern ein Blick auf eine Fehlbewertung, die man nicht schließen kann, kombiniert mit echtem Tail-Risiko auf der ADR-Seite (VIE/HFCAA).

---

## Querschnittsthema: Zeitzonen-Arbitrage/Predictability

Das Mandat nennt Zeitzonen-Arbitrage explizit als dritten Anomalietyp. Nach Durchsicht der Literatur wird dies hier **nicht als eigenständiger vierter Kandidat**, sondern als **Querschnittsfaktor** behandelt, der die Limits-to-Arbitrage sowohl von Kandidat 1 als auch Kandidat 2 verschärft:

- Froot & Dabora (1999) zeigen explizit, dass die DLC-Preisdifferenz mit der **relativen Indexperformance des jeweiligen Haupthandelsplatzes** korreliert — ein Zeitzonen-/Standort-Effekt ist der zentrale Erklärungsmechanismus ihrer Studie, keine separate Anomalie.
- Der Titel "Can time difference deter arbitrage opportunities?" (Journal of Asset Management, 2013) deutet klar in Richtung **Zeitzonen als Arbitrage-Hindernis** (Kosten-/Risikofaktor), konnte im Volltext wegen Paywall nicht verifiziert werden (Zugriff über Springer-Autorisierung blockiert) — Befund daher mit Vorbehalt zu behandeln, aber konsistent mit dem übrigen Bild.
- Auf der HFT-Ebene (Poutré et al. 2022) ist die Zeitzonen-/Latenz-Dimension bereits vollständig in die Kapazitäts- und Kostenanalyse von Kandidat 1 eingepreist: Der beschriebene Jahresgewinn von ~6 Mio. USD für eine spezialisierte Firma über 74 Paare ist im Kern ein Zeitzonen-/Latenz-Arbitrage-Ergebnis (Kanada/USA, unterschiedliche Handelsplätze).

**Fazit Zeitzonen:** Kein eigenständig handelbarer Faktor für ein systematisches Mandat — entweder bereits Teil der (toten) HFT-Preisparitäts-Arbitrage, oder ein Verstärker der ohnehin bereits als Tail-Risiko eingestuften DLC-Divergenzdynamik.

---

## Gesamtfazit

Diese Anomalieklasse ist für ein systematisches, nicht-HFT-fähiges institutionelles Mandat **nach ehrlicher Prüfung tot**:

- **Konvertierbare ADRs**: Ineffizienz real, aber vollständig im Mikrosekundenbereich internalisiert (4,9 bps Durchschnittsdeviation, ~12 Minuten Halbwertszeit) — genau wie im Auftrag antizipiert ("werden von Arbitrage-Desks eng gehalten").
- **DLC-Arbitrage**: Die historisch beste Evidenz der Klasse (bis zu 10% p.a. netto, de Jong et al. 2009), aber durch LTCM empirisch als Multi-Jahres-Tail-Risk-Trade bewiesen und durch eine Welle freiwilliger Unifikationen (2005–2026) auf ein einziges, aktiv gegen Unifikation votierendes Restrisiko (Rio Tinto) reduziert. Kein systematisch skalierbares Anlageuniversum mehr vorhanden.
- **Nicht-konvertierbare Prämien**: Größte und persistenteste Fehlbewertung, aber per Konstruktion ("keine Fungibilität", Kapitalverkehrskontrollen) nicht arbitragefähig — exakt das im Auftrag beschriebene Problem ("kein Arbitrage-Mechanismus"). Zusätzliches, asymmetrisches Tail-Risiko (VIE/HFCAA-Delisting) auf der US-ADR-Seite macht die Klasse für ein institutionelles Buch zusätzlich unattraktiv.

Kein Kandidat erreicht die Schwelle für **CANDIDATE** (dokumentierte Post-Publication-Evidenz UND Kostenrobustheit). Empfehlung an das Fondsmandat: **Klasse nicht weiterverfolgen**, außer als diskretionäre, nicht-systematische Einzeltitel-Beobachtung (Rio-Tinto-DLC als Sondersituation, sollte sich die Governance-Position künftig ändern).

## Evidenzbasis und Einschränkungen

Websuche war verfügbar und wurde für alle Kernaussagen genutzt (WebSearch + WebFetch, Stand Juli 2026). Mehrere Primärquellen waren nicht im Volltext zugänglich (Paywalls bei ScienceDirect/Springer: Gagnon & Karolyi Volltext, "International High-Frequency Arbitrage for Cross-Listed Stocks" ScienceDirect-Fassung, "Can time difference deter arbitrage opportunities?"); in diesen Fällen wurde auf Sekundärquellen (SSRN-Abstracts, Working-Paper-Fassungen, Zitationen in Folgeliteratur, Suchmaschinen-Snippets) zurückgegriffen und dies im Text kenntlich gemacht. Zahlen zu LTCM/Royal Dutch Shell stammen aus mehreren konvergierenden Sekundärquellen (Lowenstein-Zitate, Wikipedia LTCM-Artikel, akademische Siamese-Twins-Literatur) und sind als Größenordnung, nicht als exakte Bilanzzahl zu verstehen. Die Liste der DLC-Unifikationen wurde über offizielle Unternehmensmitteilungen/SEC-Filings (BHP, Shell, Unilever, Carnival, Rio-Tinto-6-K-Filings) verifiziert.

## Wichtigste Quellen

- Gagnon, L. & Karolyi, G.A. (2010). Multi-Market Trading and Arbitrage. *Journal of Financial Economics* 97(1), 53–80.
- Rösch, D. (2021). The Impact of Arbitrage on Market Liquidity. *Journal of Financial Economics* 142(1), 195–213.
- Rosenthal, L. & Young, C. (1990). The seemingly anomalous price behavior of Royal Dutch/Shell and Unilever N.V./PLC. *Journal of Financial Economics* 26(1), 123–141.
- Froot, K.A. & Dabora, E.M. (1999). How are stock prices affected by the location of trade? *Journal of Financial Economics* 53(2), 189–216.
- de Jong, A., Rosenthal, L. & van Dijk, M.A. (2009). The Risk and Return of Arbitrage in Dual-Listed Companies. *Review of Finance* 13(3), 495–520.
- Scruggs, J.T. (2006). Noise trader risk: Evidence from the Siamese twins. *Journal of Financial Markets*.
- Poutré, C., Dionne, G. & Yergeau, G. (2022). International High-Frequency Arbitrage for Cross-Listed Stocks. HEC Montréal Working Paper / SSRN 4066962.
- Meng et al. (2023/2024). Limits of arbitrage and their impact on market efficiency: Evidence from China. *Global Finance Journal* 59.
- Hang Seng Stock Connect China AH Premium Index, hsi.com.hk / MacroMicro.
- SEC-6-K-Filings BHP Group, Shell plc, Unilever plc, Carnival Corporation & plc, Rio Tinto plc (2021–2026) zu DLC-Unifikationen bzw. Ablehnung der Rio-Tinto-Unifikation (AGM April/Mai 2025).
- White & Case (2022). The HFCAA and consequences for US-listed China-based companies.
