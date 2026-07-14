```yaml
agent: 06
klasse: "Aktienrückkäufe"
websuche_verfuegbar: ja
strategien:
  - name: "Open-Market-Buyback-Ankündigungs-Drift (Long-Run BHAR, Value-Subsample)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0.1-0.3"
    kernrisiko: "Prozyklizität: Buyback-intensive Firmen sind bei Kredit-/Liquiditätsschocks überproportional exponiert, weil Managements Rückkäufe genau dann aussetzen, wenn die Value-Stütze am nötigsten wäre (2008, 2020). Zusätzlich uneinheitliche Post-2000-Evidenz: Fu & Huang (2016) finden die Anomalie für 2003-2012 verschwunden, Peyer & Vermaelen (2009) finden sie bis 2001 intakt; internationale Evidenz (Manconi/Peyer/Vermaelen 2019) stützt Persistenz außerhalb der USA."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "SEC EDGAR Volltextsuche (8-K Item 8.01, 10-Q Item 703) - nur ab ca. 2001 vollständig, keine kuratierte Ken-French-Reihe verfügbar; für Vollreplikation wird SDC Platinum/WRDS (kostenpflichtig) benötigt"

  - name: "Net Share Issuance / Net Payout Yield (Composite Issuance)"
    urteil: CANDIDATE
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 4
      regimestabilitaet: 3
      handelbarkeit: 4
      kapazitaet: 4
      kostenrobustheit: 4
    p_echte_ineffizienz: 0.55
    netto_sharpe_erwartung: "0.2-0.4"
    kernrisiko: "Der überwiegende Teil des Alphas stammt aus der Short-/Untergewichtungs-Seite (Vermeidung von Emittenten/SEO-Firmen), nicht aus reinem Long-Exposure auf Rückkäufer. Als 'reine Buyback-Strategie' isoliert schwächer als das kombinierte Netto-Payout-Signal. Crowding seit ca. 2010 durch Verbreitung in Quality-/Investment-Faktorprodukten; vorbörslicher Struktur-Bruch 1970 (Signifikanz nur post-1970, konsistent mit SEC Rule 10b-18 von 1982 als Katalysator der modernen Buyback-Welle)."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Chen & Zimmermann Open Source Asset Pricing (GitHub OpenSourceAP/CrossSection) - Signale 'NetPayoutYield' und 'CompositeIssuance' als fertige Long-Short-Portfoliorenditen kostenlos abrufbar"

  - name: "Actual-Repurchase-Informativeness / Ist-Rückkauf-Signal (Buy-the-Dip via Quartalsdisclosure)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "0.0-0.15 (nach Kosten vermutlich ~0)"
    kernrisiko: "Strukturelle Informationsverzögerung: Ist-Rückkaufvolumina werden nur quartalsweise (10-Q Item 703) offengelegt; sobald der Datenpunkt öffentlich ist, hat der Markt längst reagiert. Die von der SEC 2023 beschlossene schnellere Offenlegungspflicht wurde im Dezember 2023 vom 5th Circuit annulliert - die Latenz bleibt strukturell hoch, keine Verbesserung in Sicht."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "SEC EDGAR Financial Statement Data Sets (XBRL, kostenlos, aber sehr aufwändige Rohdaten-Aufbereitung nötig) - '-'"
```

# Anomalieklasse: Aktienrückkäufe — Adversariale Bewertung

**Agent 06 | Mandat: Buyback-Ankündigungen, vollzogene Rückkäufe, Net Payout Yield | Stand: Juli 2026**

**Nullhypothese:** Es gibt kein handelbares Netto-Alpha in der Rückkauf-Anomalieklasse. Diese Analyse versucht, diese Hypothese zu widerlegen — nicht, die Klasse zu verkaufen.

**Websuche:** War in dieser Session verfügbar und wurde für alle Kernaussagen genutzt (Primärstudien, Replikationen, aktuelle Marktdaten 2023-2026). Einzelne quantitative Detailwerte (exakte t-Statistiken einiger Tabellenzeilen) konnten trotz Suche nicht verifiziert werden und sind entsprechend als Näherung/unsicher gekennzeichnet.

---

## Zusammenfassung des Urteils

Von drei geprüften Kandidaten ist **einer** ein CANDIDATE — und dieser ist eigentlich eine **Payout/Issuance-Strategie**, bei der Rückkäufe nur die Hälfte der Gleichung sind; der überwiegende Teil des dokumentierten Alphas stammt aus der Vermeidung von Aktienemittenten, nicht aus dem Long-Exposure auf Rückkäufer. Die "reine" klassische Buyback-Anomalie (Ikenberry/Lakonishok/Vermaelen 1995, Peyer/Vermaelen 2009) ist WEAK: real in der Originalperiode, aber mit dokumentiertem Verschwinden im US-Datensatz 2003-2012 (Fu & Huang 2016) und struktureller Prozyklizität, die genau in Stressphasen versagt. Ein drittes, mikrostrukturnahes Signal (Ist-Rückkauf-Informativität) wird als KILL eingestuft — ökonomisch plausibel, aber durch Offenlegungsverzögerung praktisch nicht vorlaufend handelbar, zumal die 2023 beschlossene SEC-Regel zur saison beschleunigten Offenlegung Ende 2023 gerichtlich kassiert wurde.

**Makro-Kontext Juli 2026:** S&P-500-Rückkäufe erreichten 2024 ein Rekordjahr von 942,5 Mrd. USD, Q1 2025 mit 293,5 Mrd. USD ein Rekordquartal, und die 12-Monats-Summe bis Q3 2025 lag bei rund 1,02 Billionen USD — trotz der seit 2023 geltenden 1%-Excise-Tax auf Rückkäufe (Inflation Reduction Act). Das bedeutet: Rückkäufe sind heute so allgegenwärtig wie nie zuvor. Ein Signal, das auf "Firma X kündigt Rückkauf an" beruht, hat dadurch strukturell an Diskriminierungskraft verloren — fast jede Large-Cap-Firma tut es.

---

## Kandidat 1: Open-Market-Buyback-Ankündigungs-Drift (Long-Run BHAR)

### a) Ökonomische Begründung

Die klassische Erklärung ist **Marktunterreaktion (Behavioral Bias)**: Manager verfügen über private Informationen zum inneren Wert der Firma und signalisieren Unterbewertung durch Rückkaufankündigungen. Der Markt reagiert bei Ankündigung nur unvollständig (limited attention / underreaction to information conveyed through the announcement), sodass sich die Korrektur über 1-4 Jahre fortsetzt. Verursacher der Fehlbewertung: uninformierte/passive Investoren und Analysten, die Rückkäufe nicht korrekt als Signal für Unterbewertung dekodieren — insbesondere bei Firmen, die zuvor von Analysten herabgestuft und deren langfristige Gewinnerwartungen übertrieben pessimistisch waren (Peyer & Vermaelen 2009: Rückkäufe als Reaktion auf Marktüberreaktion auf schlechte Nachrichten).

### b) Limits to Arbitrage

Peyer & Vermaelen (2009) liefern eine spezifische Erklärung für Tender-Offer-Fälle: Preise nach Tender-Offers werden gesetzt, als ob **alle** Aktionäre andienen würden; empirisch tun das aber nicht alle — der Marginal-Investor (nicht der Durchschnittsinvestor) bestimmt effektiv den Preis, wodurch eine strukturelle Lücke entsteht, die schwer zu arbitrieren ist, da man die Anteilseignerstruktur nicht beobachten kann. Für Open-Market-Rückkäufe: Der Effekt konzentriert sich auf **Value-Aktien** (kleinere, weniger liquide, höheres idiosynkratisches Risiko) — exakt das Marktsegment, das laut McLean & Pontiff (2016) generell höhere Post-Publikations-Renditen behält, weil Arbitrageure dort höhere Kosten und Risiken tragen. Zusätzlich ist die Strategie strukturell "long-only ohne natürliches Short-Pendant" (Glamour-Rückkäufer zeigen laut ILV 1995 keinen Drift), was das Aufbauen einer marktneutralen Arbitrageposition erschwert.

### c) Originalstudien

- **Ikenberry, Lakonishok, Vermaelen (1995)**, *Journal of Financial Economics* 39: 181-208. Stichprobe: Open-Market-Rückkaufankündigungen NYSE/AMEX 1980-1990. Ergebnis: durchschnittliche abnormale 4-Jahres-Buy-and-Hold-Rendite (BHAR) nach Ankündigung von **12,1%** (Gesamtstichprobe); für **Value-Aktien** (hohes B/M, am ehesten unterbewertungsgetrieben) **45,3%**; für **Glamour-Aktien** kein signifikanter Drift (Bootstrap-Mittelwert ca. **-4,3%**, nicht signifikant von Null verschieden). Wegen der bekannten Rechtsschiefe von BHAR-Verteilungen verwenden die Autoren Bootstrap-Verfahren statt klassischer t-Tests; die Value-Subsample-Ergebnisse sind auf dem 1%-Niveau signifikant, die Gesamtstichprobe schwächer (~2-3 Sigma-Bereich).
- **Comment & Jarrell (1991)**, *Journal of Finance* 46: 1243-1271, liefert den kurzfristigen Ankündigungseffekt als Kontext: 3-Tage-CAR bei Open-Market-Ankündigungen **2-4%**, bei Fixed-Price-Tender-Offers historisch **16-17%** (ältere Stichprobe 1960er/70er). Dieser sofortige Sprung ist informationseffizient und **nicht** ex ante handelbar — er ist Bestandteil der EMH-konformen Reaktion, keine Anomalie per se.
- **Peyer & Vermaelen (2009)**, *Review of Financial Studies* 22(4): 1693-1745. Stichprobe: 3.481 Open-Market-Rückkaufankündigungen 1991-2001 (Post-ILV-Periode, explizit als Robustheitstest konzipiert). Ergebnis: signifikante durchschnittliche monatliche abnormale Renditen von 0,52% / 0,50% / 0,45% / 0,44% über 12-/24-/36-/48-Monats-Fenster. Im höchsten B/M-Quintil (623 Firmen) kumulative 48-Monats-Überrendite von **28,9%** (p<0,1%). Kernaussage: Die Autoren **verwerfen explizit** die Hypothese, dass die Anomalie bis 2001 verschwunden sei.

### d) Out-of-Sample-/Post-Publication-Evidenz

Hier liegt der entscheidende Bruch in der Literatur:

- **Fu & Huang (2016)**, *Management Science* 62(4): 964-984: Für Rückkauf- **und** Emissionsereignisse **2003-2012** verschwinden die langfristigen abnormalen Renditen. Erklärung der Autoren: gestiegenes institutionelles Eigentum, gesunkene Handelskosten (Dezimalisierung 2001), verbesserte Liquidität und schärfere Offenlegungs-/Governance-Regulierung (Reg FD 2000) haben die Preisbildung effizienter gemacht; Firmen agieren seither weniger "opportunistisch" (weniger Timing von Unterbewertung, mehr operative Motive).
- **Manconi, Peyer, Vermaelen** ("Buybacks Around the World", *JFQA* 2019): 9.000+ Rückkaufankündigungen aus 31 Nicht-US-Ländern. Auch international signifikante kurz- und langfristige Überrenditen, CAR-Differenz zwischen hohem/niedrigem Unterbewertungs-Index von **13-17% über 48 Monate**. Wichtig: die Autoren finden **keine** Evidenz, dass diese internationalen Überrenditen im Zeitverlauf abnehmen oder reine Übernahmerisiko-Kompensation sind — im Gegensatz zu den US-Befunden von Fu & Huang.
- **McLean & Pontiff (2016)**, *Journal of Finance* 71: 5-32, allgemeiner Rahmen für 97 Anomalien: Portfoliorenditen im Schnitt **26% niedriger out-of-sample**, **58% niedriger post-Publikation**, davon rund **32 Prozentpunkte** durch publikationsinduziertes Handeln erklärbar. Rückkäufe sind in diesem breiten Sample enthalten, aber nicht separat ausgewiesen.
- **Jacobs & Müller** (241 Anomalien, 39 Länder): Nur der **US-Markt** zeigt einen verlässlichen Post-Publikations-Decay; internationale Märkte zeigen ihn nicht systematisch — konsistent mit dem US-spezifischen Fu-&-Huang-Befund.

**Decay-Schätzung (eigene Einordnung):** Für die reine US-Ankündigungs-Drift-Strategie liegt die Evidenz für einen Decay in der Größenordnung **50-100% seit 2002** vor (Fu & Huang zeigen praktisch vollständiges Verschwinden 2003-2012), während internationale/Value-Subsample-Varianten deutlich robuster erscheinen (Decay eher im 20-40%-Bereich, analog zum generischen McLean/Pontiff-Muster).

### e) Kosten

Long-only, Haltedauer 1-4 Jahre (Turnover ca. 25-100% p.a. je nach Rebalancing-Frequenz) — grundsätzlich kostenfreundliches Profil. Novy-Marx & Velikov (2016, *RFS* 29(1): 104-147) zeigen, dass Strategien mit <50% Monats-Turnover typischerweise signifikante Netto-Spreads nach Kosten erzielen; durchschnittliche Ausführungskosten liegen bei 20-57 Bp für mittel-turnover Anomalien. Problem: Der werthaltige Teil des Signals konzentriert sich auf kleinere Value-Firmen mit breiteren Spreads und höherem Market Impact als der Durchschnitt — die Kostenannahmen aus generischen Taxonomien sind hier optimistisch. Realistisch dürften 100-150 Bp p.a. an Umsetzungskosten anfallen, was einen Großteil der nach 2002 ohnehin geschrumpften Bruttoprämie auffrisst.

### f) Kapazität und Handelbarkeit

Moderat: Das investierbare Universum ist auf Firmen beschränkt, die tatsächlich Rückkäufe ankündigen UND einen Value-Tilt aufweisen — deutlich kleiner als der Gesamtmarkt. Kapazitätsschätzung: niedrige einstellige Milliarden-USD-Bereich, bevor Market Impact die Nettorendite signifikant erodiert (konservative Einordnung angesichts der Small-/Mid-Cap-Konzentration des werthaltigen Subsamples). Shortability ist irrelevant, da die Strategie long-only ist (kein belastbares Signal auf der Short-Seite, da Glamour-Rückkäufer keinen negativen Drift zeigen).

### g) Regimeabhängigkeit und Tail-Risiko

Dies ist die größte strukturelle Schwäche: **Aggregierte Rückkäufe sind hochgradig prozyklisch.** S&P-500-Rückkäufe stiegen 2003-2007 von 135 Mrd. auf 590 Mrd. USD mit Höhepunkt in Q3 2007 — unmittelbar vor der Finanzkrise — und brachen danach auf 25 Mrd. USD in Q2 2009 ein. Firmen timen den Gesamtmarkt schlecht: Rückkaufvolumen korreliert positiv mit vorangegangenen Kursanstiegen und ist prozyklisch mit dem Marktzyklus verknüpft, nicht kontrazyklisch. Für die Einzeltitel-Anomalie bedeutet das: genau in Crash-Phasen (2008, März 2020), wenn der "Value-Support" durch Rückkäufe am nötigsten wäre, setzen die Firmen ihre Programme aus — die Strategie verliert ihre Verteidigungslinie exakt im Tail-Risiko-Szenario. Zusätzlich sind rückkaufintensive Firmen tendenziell stärker fremdfinanziert (Rückkäufe teilweise schuldenfinanziert), was die Beta-Exponierung gegenüber Credit-Spread-Schocks erhöht. Erwartete Skewness: negativ, mit Crash-Clustering-Risiko.

### h) Bekannte Kritik/Widerlegungen

- **Selection/Look-Ahead-Bias der Originalstudie:** ILV 1995 nutzt eine Post-hoc-Selektion in Value/Glamour-Quintile, die erst nach Beobachtung der Ergebnisse plausibilisiert wurde — klassisches Risiko von Data-Snooping bei mehrfacher Sample-Teilung.
- **Regimewechsel-Kritik:** Fu & Huang (2016) argumentieren explizit, dass die Anomalie ein Artefakt geringerer Markteffizienz der 1980er/90er war (vor Dezimalisierung, vor breiter institutioneller Abdeckung) und in der modernen Marktstruktur strukturell nicht mehr vorhanden ist.
- **Microcap-Konzentration:** Der werthaltige Teil des Signals sitzt überproportional in kleineren, weniger liquiden Titeln — ein wiederkehrendes Muster bei praktisch allen "überlebenden" US-Anomalien post-2000 (McLean/Pontiff: höhere Persistenz bei hoher Idiosynkrasie/geringer Liquidität = höhere Umsetzungskosten).
- **Lebender Praxistest:** PKW (Invesco BuyBack Achievers ETF, seit 2006 an der Realität getestet, folgt dem NASDAQ US BuyBack Achievers Index) hat 2023 spürbar schlechter abgeschnitten als der kapitalisierungsgewichtete S&P 500 — ein Jahr, das von einer extremen Mega-Cap-Konzentration ("Magnificent 7") geprägt war, die das Buyback-Achievers-Universum strukturell untergewichtet. 2024/2025 näherte sich die Performance wieder an den Index an. Dies illustriert das Stilrisiko/Faktor-Rotationsrisiko der Strategie in der Praxis (exakte Jahreszahlen aus verfügbaren Quellen teils widersprüchlich, Richtung aber konsistent).

**Fazit Kandidat 1: WEAK.** Ökonomisch plausibel, in der Ursprungsperiode (1980-2001) mit klaren, replizierten Effektgrößen belegt, aber mit dokumentiertem (wenn auch umstrittenem) Verschwinden im US-Kernsample seit 2002 und struktureller Prozyklizität, die die Strategie in genau den Tail-Szenarien schwächt, in denen ein Value-/Contrarian-Signal am meisten bringen müsste.

---

## Kandidat 2: Net Share Issuance / Net Payout Yield (Composite Issuance)

### a) Ökonomische Begründung

Zwei sich ergänzende Mechanismen: (1) **Managerielles Markttiming** — Manager emittieren Aktien, wenn sie ihre Firma für überbewertet halten, und kaufen zurück, wenn sie sie für unterbewertet halten (asymmetrische Information zwischen Insidern und Markt). (2) **Investoren-Extrapolationsbias**: Anleger unterschätzen systematisch den Verwässerungseffekt von Emissionen bzw. den akkretiven Effekt von Rückkäufen auf Kennzahlen je Aktie und reagieren träge auf die im Aktienzahl-Wachstum enthaltene Information. Verursacher der Fehlbewertung: passive/quantitativ wenig sophistizierte Investoren, die Nettomittelfluss zwischen Firma und Aktionären (Dividenden + Rückkäufe − Emissionen) nicht vollständig einpreisen, obwohl er laut Boudoukh/Michaely/Richardson/Roberts (2007) deutlich mehr Prognosekraft besitzt als die traditionelle Dividendenrendite.

### b) Limits to Arbitrage

Der Großteil des Alphas sitzt auf der **Short-Seite** (Vermeidung/Leerverkauf von Emittenten — häufig kleine, wachstumsstarke, sentimentgetriebene Growth-/Glamour-Firmen mit hohen Leihkosten und Short-Sale-Constraints, klassische Nagel (2005)/Lamont-Stein-Konstellation). Das macht die vollständige Umsetzung der Bruttoprämie in der Praxis teurer als im Long-Only-Backtest sichtbar. Die Long-Seite (Netto-Rückkäufer, meist reifere, profitable Firmen) ist dagegen liquide und leicht zu halten — die Arbitragebarriere liegt also asymmetrisch auf einer Seite des Buchs.

### c) Originalstudien

- **Pontiff & Woodgate (2008)**, *Journal of Finance* 63(2): 921-945. Aktienemission (Composite Share Issuance) zeigt post-1970 eine cross-sektionale Prognosekraft, die statistisch **stärker** ist als die von Size, Book-to-Market oder Momentum einzeln. Vor 1970 keine signifikante Prognosekraft feststellbar — konsistent mit der Einführung von SEC Rule 10b-18 (1982), die den modernen "Safe Harbor" für Open-Market-Rückkäufe erst schuf und deren Volumen strukturell ermöglichte.
- **Boudoukh, Michaely, Richardson, Roberts (2007)**, *Journal of Finance* 62(2): 877-915. Payout- und Net-Payout-Yield (Dividenden + Rückkäufe [− Emissionen]) besitzen deutlich höhere Prognosekraft für aggregierte Marktrenditen als die klassische Dividendenrendite — die vielzitierte "verschwundene" Prognosekraft der Dividendenrendite ist laut den Autoren größtenteils ein Messfehler-Artefakt, weil Rückkäufe seit den 1980ern einen wachsenden Anteil des Payouts ausmachen. Wichtig: dies ist primär ein **Zeitreihen-Markttiming-Befund**, kein reiner Cross-Sektions-Stock-Picking-Befund wie Pontiff & Woodgate.

### d) Out-of-Sample-/Post-Publication-Evidenz

- **Chen & Zimmermann, "Open Source Cross-Sectional Asset Pricing"** (2020/2022, *Critical Finance Review*): Von 161 in Originalstudien klar signifikanten Prädiktoren replizieren **98%** einen |t|>1,96 in unabhängiger Nachbildung; Regression reproduzierter auf Original-t-Statistiken ergibt Slope 0,88, R²=82%. Issuance-/Payout-bezogene Signale (u.a. CompositeIssuance, NetPayoutYield) gehören zu den am robustesten replizierten Charakteristika im gesamten Katalog von 319 getesteten Variablen und bleiben im Chen/Zimmermann-(2022)-Update bei 5%-Signifikanz erhalten.
- **Hou, Xue, Zhang, "Replicating Anomalies"**: Issuance-/Investment-verwandte Anomalien werden im q-Faktor-Rahmen weitgehend durch den Investment-Faktor erklärt — das heißt, ein Teil der Prognosekraft ist nicht "zusätzliches Alpha", sondern durch etablierte Investment-/Quality-Faktor-Exposures abgedeckt. Das reduziert die inkrementelle Signifikanz für einen Investor, der bereits auf Standardfaktoren exponiert ist.
- **Internationale Evidenz**: Pontiff & Woodgate sowie Folgestudien (u.a. McLean, Pontiff & Watanabe zu internationaler Issuance-Anomalie) finden das Muster auch außerhalb der USA, wenn auch mit geringerer Effektstärke in weniger entwickelten Märkten (konsistent mit Arbitragekapital-Knappheit als Erklärung für Persistenz).

**Decay-Schätzung:** Im Rahmen des allgemeinen McLean/Pontiff-Musters (26% out-of-sample, 58% post-Publikation) liegt Net-Payout-/Issuance vermutlich am unteren Ende des Decay-Spektrums, da es zu den am robustesten replizierten Signalen zählt — grobe eigene Einordnung: 20-35% Decay seit Erstveröffentlichung, deutlich weniger als bei fragilen Small-Sample-Anomalien.

### e) Kosten

Niedriger Turnover (typischerweise jährliches oder halbjährliches Rebalancing basierend auf Jahresabschlussdaten zur Aktienzahl), breites Anlageuniversum über alle Marktkapitalisierungssegmente. Laut Novy-Marx & Velikov (2016) gehören genau solche Value-/Investment-artigen Low-Turnover-Signale zu den Strategien mit der **größten Kapazität zur Aufnahme neuen Kapitals** und den robustesten Netto-Spreads nach Kosten. Haupt-Kostentreiber bleibt die Short-Seite (siehe b), wo Leihgebühren und Hard-to-Borrow-Aufschläge bei kleinen Wachstumsemittenten die Netto-Sharpe-Ratio gegenüber dem Brutto-Backtest spürbar drücken.

### f) Kapazität und Handelbarkeit

Deutlich höher als Kandidat 1: Das Signal ist für praktisch das gesamte Compustat/CRSP-Universum berechenbar (jede Firma hat eine beobachtbare Aktienzahl-Änderung), nicht nur für Firmen mit expliziten Rückkaufankündigungen. Grobe Kapazitätsschätzung: niedriger bis mittlerer zweistelliger Milliarden-USD-Bereich für die Long-Seite; die Short-Seite ist durch Leihkapazität bei kleinen Emittenten begrenzter.

### g) Regimeabhängigkeit und Tail-Risiko

Diversifizierter als Kandidat 1, da über das gesamte Marktkapitalisierungsspektrum gestreut, aber nicht immun: Netto-Rückkäufer-Portfolios tragen ein gewisses Klumpenrisiko in Richtung reifer, teils fremdfinanzierter Firmen (ähnliche Kredit-Exponierung wie Kandidat 1, jedoch abgefedert durch die Short-Seite gegen wachstumsstarke, in Abschwüngen oft noch stärker fallende Emittenten — das Long-Short-Konstrukt bietet damit einen gewissen natürlichen Hedge gegen breite Marktabschwünge, den Kandidat 1 als Long-only-Strategie nicht hat).

### h) Bekannte Kritik/Widerlegungen

Wichtigster Kritikpunkt für das spezifische Mandat "Buybacks": Das Signal ist **kein reines Rückkaufsignal**, sondern ein kombiniertes Payout-/Kapitalstruktur-Signal, bei dem der dokumentierte Effekt überwiegend aus der Emissions-Seite (Short) stammt. Wer nur long auf Rückkäufer setzt und die Short-Seite weglässt, fängt historisch nur einen Bruchteil der ausgewiesenen Faktorprämie ein. Zudem überschneidet sich das Signal konzeptionell stark mit Investment-/Asset-Growth-Faktoren (Hou-Xue-Zhang, Fama-French 6-Faktor-INV), sodass ein Teil der "Buyback-Prämie" in Wahrheit bereits über Standard-Faktor-Exposures eingepreist/gecrowded ist.

**Fazit Kandidat 2: CANDIDATE — mit wesentlichem Vorbehalt.** Dies ist die robusteste, am besten replizierte Strategie der drei Kandidaten, gehört im engeren Sinne aber eher in die Klasse "Payout/Kapitalstruktur-Anomalien" als in eine reine "Buyback"-Klasse. Als CANDIDATE eingestuft, weil (i) dokumentierte Post-Publication-Robustheit (Chen/Zimmermann-Replikation, internationale Evidenz) und (ii) Kostenrobustheit (Novy-Marx/Velikov: Low-Turnover-Kapazitätsvorteil) beide erfüllt sind — die beiden vom Mandat geforderten Bedingungen für CANDIDATE.

---

## Kandidat 3: Actual-Repurchase-Informativeness ("Buy-the-Dip"-Signal aus Ist-Rückkaufdaten)

### a) Ökonomische Begründung

Firmen, die tatsächlich (nicht nur angekündigt) Aktien zurückkaufen, tun dies laut Ben-Rephael, Oded & Wohl ("Do Firms Buy Their Stock at Bargain Prices? Evidence from Actual Stock Repurchase Disclosures", *Review of Finance* 18, 2014, EFA-2015-Best-Paper-Investments-Award) informiert — sie kaufen überproportional in Phasen kurzfristiger Unterbewertung. Der ökonomische Mechanismus ist derselbe Informationsvorsprung des Managements wie bei Kandidat 1, aber granularer gemessen (tatsächliche Käufe statt bloße Ankündigung/Autorisierung, die oft nie vollständig ausgeschöpft wird).

### b) Limits to Arbitrage

Firmen mit Unterbewertungsmotiv kaufen empirisch **weniger** Aktien zurück und haben eine **niedrigere Programm-Vollzugsquote** als Firmen mit anderen Motiven (Ben-Rephael et al.) — die Vollzugsquote sinkt zusätzlich mit den Geld-Brief-Spannen (Adverse-Selection-Kosten). Empirische Vollzugsquoten von Rückkaufprogrammen liegen typischerweise bei rund 70-80% des autorisierten Volumens. Das bedeutet: genau das informativste Signal (kleine, aber gezielte Käufe bei echter Unterbewertung) ist am schwersten von außen zu beobachten und zu timen.

### c) Originalstudie

Ben-Rephael, Oded, Wohl (2014), *Review of Finance* 18(4). Datenbasis: tatsächliche, in Quartalsberichten offengelegte Rückkaufvolumina (nicht Ankündigungen). Kernbefund: informierte (unterbewertungsmotivierte) Firmen erzielen eine signifikant positivere Kursreaktion, wenn ihre Ist-Käufe bekannt werden, kaufen aber gleichzeitig weniger und langsamer.

### d) Out-of-Sample-/Post-Publication-Evidenz

Die Replikationsbasis ist dünn im Vergleich zu Kandidat 1 und 2: vereinzelte internationale Übertragungen (z.B. eine 2025 publizierte Studie zu Chinas reformiertem Open-Market-Rückkaufprogramm, Crash-Risk-Fokus statt Renditefokus) und einige australische/asiatische Marktreaktionsstudien zu Ist-Rückkäufen, aber keine systematische McLean/Pontiff-artige Decay-Analyse spezifisch für dieses Signal auffindbar. Evidenzbasis insgesamt schwächer und fragmentierter als bei den ersten beiden Kandidaten.

### e) Kosten

Das Signal erfordert die Verarbeitung von 10-Q-Daten (Item 703) mit inhärentem Veröffentlichungsverzug von bis zu einem Quartal. Jede Umsetzungsstrategie, die auf diesen historischen Daten aufbaut, kauft de facto "alten" Fakten hinterher — der eigentliche Informationsvorsprung des Managements ist zum Zeitpunkt der Offenlegung bereits ausgenutzt bzw. das kurzfristige Kursmuster (Wochen bis wenige Monate) längst abgeschlossen. Hochfrequente/Ereignisstudien-Investoren, die 8-K- und 10-Q-Filings automatisiert überwachen, haben diesen Datenpunkt schon lange in ihre Modelle integriert.

### f) Kapazität und Handelbarkeit

Gering: Das Signal wirkt kurzfristig und ist auf eine enge Zeitspanne um die (verzögerte) Offenlegung konzentriert — schlecht skalierbar, hohe Konkurrenz durch bereits etablierte quantitative Monitore von SEC-Filings.

### g) Regimeabhängigkeit und Tail-Risiko

Ähnlich prozyklisch wie Kandidat 1 (Ist-Käufe fallen in Stressphasen mit Ankündigungen zusammen weg), zusätzlich anfällig für regulatorische Verschiebungen der Offenlegungsfristen.

### h) Bekannte Kritik/Widerlegungen

Die SEC hatte 2023 eine Regel zur monatlichen, zeitnaheren Offenlegung von Ist-Rückkäufen verabschiedet (Share Repurchase Disclosure Modernization) — was das Signal potenziell handelbarer gemacht hätte. Diese Regel wurde jedoch am 19. Dezember 2023 vom 5th U.S. Circuit Court of Appeals wegen Verstoßes gegen den Administrative Procedure Act **vollständig annulliert** (fehlende Kosten-Nutzen-Analyse); Stand 2025/2026 gilt weiterhin die alte, langsamere Quartalsoffenlegung nach Item 703, ohne erkennbare neue SEC-Initiative. Diese regulatorische Sackgasse zementiert die strukturelle Latenz des Signals und spricht gegen eine baldige Verbesserung der Handelbarkeit.

**Fazit Kandidat 3: KILL.** Ökonomisch nachvollziehbare Informationsasymmetrie, aber durch Offenlegungsverzögerung strukturell nicht in ein vorlaufendes, handelbares Signal überführbar; dünne Replikationsbasis; regulatorischer Rückschritt 2023/2024 verschlechtert die Aussichten zusätzlich.

---

## Klassenübergreifendes Fazit

Die Anomalieklasse "Aktienrückkäufe" ist **nicht tot, aber stark ausgedünnt und teilweise umbenannt**. Die einzige Variante mit belastbarer Post-Publikations-Robustheit und Kostenrobustheit (Kandidat 2, Net Payout Yield/Composite Issuance) ist im Kern kein reines Rückkaufsignal, sondern ein Payout-/Kapitalstruktur-Signal, dessen stärkste Beinarbeit auf der Vermeidung von Aktienemittenten beruht. Die "originale", auf Ikenberry/Lakonishok/Vermaelen zurückgehende Ankündigungs-Drift-Anomalie hat im US-Kernmarkt seit den frühen 2000ern dokumentiert an Kraft verloren (Fu & Huang 2016), bleibt aber international und im engen Value-Subsegment nicht vollständig widerlegt — daher WEAK statt KILL. Ein granulareres, auf Ist-Käufen statt Ankündigungen basierendes Signal scheitert an strukturellen Offenlegungsverzögerungen, die durch die gerichtliche Kassierung der SEC-Modernisierungsregel 2023/2024 eher verschärft als gelindert wurden.

Ein zusätzlicher, hier nicht als eigener Kandidat geführter, aber relevanter Befund für das Gesamtbild: **Auf Marktebene sind aggregierte Rückkäufe ein verlässlich schlechter Market-Timing-Indikator des Corporate-Sektors selbst** (Rekordvolumina 2007 vor der Finanzkrise, Einbruch 2009; ähnliches Muster 2020) — das im Juli 2026 laufende Rekordtempo von rund 1 Billion USD/Jahr an Rückkäufen sollte als Warnsignal für spätzyklisches Verhalten gelesen werden, nicht als Bestätigung der Einzeltitel-Anomalie. Für ein institutionelles Buyback-Long-Buch bedeutet das ein eingebautes, historisch wiederkehrendes Tail-Risiko genau dann, wenn Diversifikationsschutz am wichtigsten wäre.

**Handlungsempfehlung für das Gesamtportfolio-Komitee:** Falls Kapital in diese Klasse allokiert wird, ausschließlich über Kandidat 2 (Net Payout Yield, long-short, diversifiziert über Marktkapitalisierung) und explizit **nicht** über reine Buyback-Ankündigungs-long-only-Produkte (Kandidat 1) oder Ist-Rückkauf-Timing-Signale (Kandidat 3). Erwartete Netto-Sharpe-Ratio realistisch im Bereich 0,2-0,4 für Kandidat 2, mit signifikantem Vorbehalt bezüglich Überschneidung mit bereits im Portfolio vorhandenen Investment-/Quality-Faktor-Exposures (Doppelzählungsrisiko).
