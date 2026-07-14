```yaml
agent: 05
klasse: "Index-Aufnahmen & -Ausschlüsse"
websuche_verfuegbar: ja
strategien:
  - name: "S&P-500-Inklusionseffekt (Additions long)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 1
      regimestabilitaet: 1
      handelbarkeit: 3
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.05
    netto_sharpe_erwartung: "~0.0 (seit ca. 2010 statistisch nicht von Null unterscheidbar, brutto)"
    kernrisiko: "Sekulärer, monoton verlaufender Decay bis zur Bedeutungslosigkeit (7,6% -> 0,8% AR); jede verbleibende Kante wird von Bank-Programmhandelsdesks in Millisekunden abgeschöpft, bevor ein Fonds mit T+1-Ausführung reagieren kann."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Öffentliche S&P-500-Änderungsliste (Wikipedia 'List of S&P 500 companies'/S&P-Pressemitteilungen) + Yahoo Finance/Stooq Kursdaten"
  - name: "S&P-500-Exklusionseffekt (Deletions short)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 1
      regimestabilitaet: 1
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.05
    netto_sharpe_erwartung: "~0.0 bis leicht negativ nach Leihkosten (brutto AR 2010er nur -0,6%, insignifikant)"
    kernrisiko: "Deletion-Kandidaten sind überwiegend fundamental angeschlagene Small-/Micro-Caps (Distress); verbleibendes Signal ist eher Distress-/Illiquiditätsprämie als Index-Effekt; Borrow oft teuer oder unmöglich exakt im Handlungsfenster."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Öffentliche S&P-500-Änderungsliste + Yahoo Finance/Stooq Kursdaten"
  - name: "Russell-Rekonstitution (Anticipatory Trading / Reconstitution-Arbitrage, Additions & Deletions)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0.1-0.3 brutto geschätzt; nach Crowding/Kosten/Wettbewerb realistisch 0.0-0.15, hohe Schätzunsicherheit (nur 1-2 Events p.a.)"
    kernrisiko: "Extrem niedrige Eventfrequenz (Konzentrationsrisiko, kein Diversifikationseffekt innerhalb eines Jahres), starkes Crowding durch dedizierte Index-Arb-/Programmhandelsdesks, aktive Methodik-Änderungen von FTSE Russell (Banding, Diskussion Semi-Annual-Rekonstitution) als laufendes Strukturrisiko."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
```

# Agent 05 — Index-Aufnahmen und Index-Ausschlüsse: Adversariale Prüfung

## Zusammenfassung des Urteils

Die Anomalieklasse "Index-Rekonstitution" ist in ihrer bekanntesten Form — dem S&P-500-Inklusions-/Exklusionseffekt — **akademisch belegt tot**. Die Originaleffekte der 1980er/1990er-Jahre (3,4–7,6% abnormale Rendite bei Aufnahme, -4,6% bis -16,1% bei Ausschluss) sind laut der bislang gründlichsten Post-Publication-Studie (Greenwood & Sammon, *Journal of Finance* 2025, ursprünglich NBER WP 30748, Dez. 2022) in den 2010er-Jahren auf statistisch insignifikante 0,8% (Additions) bzw. -0,6% (Deletions) geschrumpft — **trotz** einer Vervielfachung des indexierten Vermögens (S&P-DJI-getrackte Assets: ca. 13 Bio. USD, Stand Ende 2023). Das ist der Lehrbuchfall einer durch Publikation wegarbitrierten Anomalie.

Die einzige Teilklasse mit belastbarer, jüngerer (2012–2021) Evidenz für eine fortbestehende mechanische Ineffizienz ist die **Russell-Rekonstitution**. Dort gibt es dokumentierte, nicht verschwundene Kosten für Indexfonds (7,5 Basispunkte/Jahr, ca. 11 Mrd. USD p.a. Verlust für Investoren, Preisverzerrung von >4% in den 20 Handelstagen vor Rekonstitution mit anschließender Reversal von ca. -5,7% im Folgemonat). Das ist jedoch (a) kein sauber peer-reviewter Befund erster Güte für die jüngste Dekade, (b) eine Kostenaussage für Indexfonds, nicht automatisch ein Netto-Alpha für einen dritten Marktteilnehmer, und (c) nachweislich gecrowded (Micheli & Neuman 2020/2022). Urteil: WEAK, nicht CANDIDATE.

**Kein Kandidat dieser Klasse erreicht die Schwelle für CANDIDATE.**

---

## Kandidat 1: S&P-500-Inklusionseffekt (Additions)

### a) Ökonomische Begründung
Zwei konkurrierende, seit 1986 nie vollständig aufgelöste Erklärungen:

1. **Price-Pressure-Hypothese** (Harris & Gurel 1986): Kurzfristige Nachfrageverschiebung durch Indexfonds, die mechanisch kaufen müssen, trifft auf eine im kurzen Fenster unelastische Angebotskurve. Die Fehlbewertung ist temporär und wird durch Arbitrageure/Market-Maker korrigiert, die dafür eine Liquiditätsprämie verlangen.
2. **Downward-Sloping-Demand-Curve-Hypothese** (Shleifer 1986): Aktien sind keine perfekten Substitute; ein permanenter Nachfrageschub durch Indexierung erzeugt einen permanenten Preisanstieg. Verursacher: strukturell gezwungene Käufer (Indexfonds mit Tracking-Error-Mandat), die preisunelastisch sind — kein klassischer "irrationaler" Bias, sondern eine strukturelle Friktion (Zwang zur Indexnachbildung).
3. **Investor-Recognition-Hypothese** (Merton 1987, angewandt von Chen/Noronha/Singal 2004): Aufnahme erhöht dauerhaft die Zahl informierter/aufmerksamer Investoren, senkt "Shadow Costs" unvollständiger Diversifikation, erklärt insbesondere die **Asymmetrie** zwischen Aufnahme (permanent) und Ausschluss (nicht symmetrisch permanent negativ).

Verursacher der Fehlbewertung: strukturell gebundene Indexfonds/ETFs, die de facto ohne Preiselastizität kaufen müssen, sobald ein Ticker im Index ist. Kein klassischer Behavioral Bias bei diskretionären Investoren — die Friktion ist regelbasierter Zwang.

### b) Limits to Arbitrage
Historisch (1980er/90er): Arbitragekapital war klein, S&P-Ankündigungen kamen überraschend (kein systematisches Vorhersagemodell), Shortpositionen zur Vorwegnahme von Deletions waren teuer/schwer zu konstruieren. Diese Grenzen sind heute weitgehend gefallen: (1) Ankündigungen erfolgen mit mehrtägigem Vorlauf zwischen Bekanntgabe und Wirksamkeit, (2) spezialisierte Event-Driven-/Index-Arb-Desks mit erheblichem Kapital stehen bereit, um Aktien vor der Aufnahme aufzukaufen und Indexfonds am Umsetzungstag zu beliefern (Greenwood & Sammon nennen dies explizit als Erklärung: "Arrangements where other institutions stood ready to sell to indexers upon inclusions").

### c) Originalstudien
- **Harris & Gurel (1986)**, *Journal of Finance* 41(4), S. 815–829: Preisanstieg von >3% unmittelbar nach Ankündigung, binnen 2 Wochen nahezu vollständig reversiert → Price-Pressure.
- **Shleifer (1986)**, *Journal of Finance* 41(3), S. 579–590: signifikant positive abnormale Rendite bei Ankündigung, kein Reversal binnen mindestens 10 Tagen, Rendite korreliert mit Ausmaß des Indexfonds-Kaufvolumens → permanenter Effekt, downward-sloping demand.
- **Chen, Noronha & Singal (2004)**, *Journal of Finance* 59, S. 1901–1930: dokumentieren die Asymmetrie explizit über einen langen Sample-Zeitraum (Additions permanent positiv, Deletions nicht symmetrisch permanent negativ) und führen dies auf Investor-Recognition zurück, nicht auf reine Preisdruck-Mechanik.

### d) Out-of-Sample-/Post-Publication-Evidenz (zentraler Befund)
**Greenwood & Sammon, "The Disappearing Index Effect"** (NBER WP 30748, Dez. 2022; *Journal of Finance* 2025, Vol. 80(2), S. 657–698):
- Additions: 3,4% (1980er) → 7,6% (1990er) → 5,21% (2000er) → **0,8% (2010er, statistisch insignifikant)**.
- Deletions: -4,6% (1980er) → -16,1% (1990er) → -12,4% (2000er) → **-0,6% (2010er, statistisch insignifikant)**.
- Das geschieht trotz massiv gestiegenem indexiertem Vermögen — ein Effizienz-Paradox, das die Autoren mit drei Faktoren erklären: (1) zunehmender Anteil der Änderungen sind Migrationen aus dem S&P MidCap 400 (dadurch vorhersagbarer, geringere Überraschung), (2) bessere Antizipation/Vorhersagemodelle für Aufnahmekandidaten, (3) Aufbau von dediziertem "Bereitschaftskapital", das strukturell bereit steht, Indexfonds zu beliefern und damit den Preisdruck vorab absorbiert, statt ihn am Ereignistag zu materialisieren.
- Frühere Vorläuferbefunde in dieselbe Richtung: Bennett et al. (2020) für 1997–2017, Preston & Soe (2021) (S&P Dow Jones Indices selbst) ab 1995 — der Decay ist also nicht nur ein Artefakt einer einzelnen Studie, sondern mehrfach unabhängig repliziert.

### e) Kosten
Selbst wenn ein Restsignal existierte: Petajisto (2011, *Journal of Empirical Finance* 18(2), S. 271–288) zeigt, dass der "Index-Turnover-Cost" — die strukturelle Belastung, die mechanische Indexer durch Kauf-mit-Premium/Verkauf-ohne-Premium erleiden — sich für S&P-500-Investoren 1990–2005 auf **21–28 Basispunkte p.a.** belief, bei einem durchschnittlichen Preisimpact von 8,8% bei Aufnahme. Das war die Größenordnung, als der Effekt noch signifikant war. Bei einem Bruttosignal von 0,8% (2010er) und typischen Market-Impact-/Spread-Kosten für die Umsetzung eines Large-Cap-Trades im engen Ankündigungsfenster ist die Nettorendite nach Kosten bestenfalls neutral, wahrscheinlicher leicht negativ.

### f) Kapazität und Handelbarkeit
Die zugrunde liegenden Titel sind hochliquide Large Caps (per Definition S&P-500-fähig), Handelbarkeit technisch kein Problem. Kapazitätsfrage ist jedoch irrelevant, da kein robustes Netto-Alpha mehr vorhanden ist, das skaliert werden könnte.

### g) Regimeabhängigkeit und Tail-Risiko
Der Effekt zeigt eine klare, monotone säkulare Verfallskurve über vier Jahrzehnte — das Gegenteil von Regimestabilität. Tail-Risiko besteht darin, dass die historische "Kante" in Backtests (die vor 2010 endende Perioden einschließen) massiv überschätzt wird, wenn nicht explizit auf die letzte Dekade beschränkt wird — ein klassisches Beispiel für Look-Ahead-verzerrte Strategieentwicklung.

### h) Bekannte Kritik/Widerlegungen
- Die S&P-500-Komiteeentscheidung ist **nicht rein mechanisch**, sondern diskretionär (S&P-Ausschuss wählt Kandidaten u.a. nach Rentabilität/Liquidität aus). Das erzeugt einen möglichen Information-Content-Kanal (Denis, McConnell, Ovtchinnikov & Yu 2003 zeigen positive Analysten-EPS-Revisionen nach Aufnahme) — ein Teil des historischen Effekts könnte fundamentale Information statt reiner Nachfrageschock gewesen sein, was die "reine Preisdruck"-Interpretation schwächt.
- Ein aktuelles methodisches Papier (*"Causal Inference in Financial Event Studies"*, Nov. 2025, arXiv 2511.15123) argumentiert, dass Standard-Faktormodell-Eventstudien bei Index-Inklusion fehlspezifiziert sein können und dass ein Teil des dokumentierten Pre-Announcement-Drifts bei Synthetic-Control-Schätzung nahezu verschwindet — ein Hinweis auf Selection-on-Unobservables statt echtem Antizipationshandel. Das ist eine Warnung, dass auch die verbleibenden 0,8%/-0,6% möglicherweise noch nach oben verzerrt sind.
- Die ursprüngliche Harris-&-Gurel- vs. Shleifer-Kontroverse (temporär vs. permanent) wurde nie sauber aufgelöst — die Literatur stritt sich 20+ Jahre über die korrekte ökonomische Interpretation, bevor der Effekt selbst verschwand.

**Urteil: KILL.** Post-Publication-Decay ist mehrfach unabhängig repliziert (Greenwood/Sammon, Bennett et al., S&P DJI eigene Studie), der Effekt ist in der relevanten (aktuellen) Dekade statistisch nicht von Null zu unterscheiden, und selbst historische Bruttoeffekte hätten realistische Umsetzungskosten kaum überlebt.

---

## Kandidat 2: S&P-500-Exklusionseffekt (Deletions)

Getrennt von Additions behandelt, da Chen/Noronha/Singal (2004) explizit eine **Asymmetrie** dokumentieren: Aufnahme erzeugt (historisch) einen permanenten Effekt, Ausschluss keinen symmetrischen permanenten Effekt — mit der Investor-Recognition-Hypothese als Erklärung (Investoren "vergessen" ein Unternehmen nach Ausschluss nicht in gleichem Maße, wie sie es nach Aufnahme neu wahrnehmen).

### a) Ökonomische Begründung
Gleiche strukturelle Friktion wie bei Additions (mechanischer Zwangsverkauf durch Indexfonds), aber asymmetrische Erwartung: kein spiegelbildlicher Recognition-Effekt. Zusätzlich: Deletion-Kandidaten sind selektiert (meist Small-/Micro-Caps, oft nach fundamentalem Abstieg — Bankrott, Übernahme, Delisting-Nähe), sodass ein Teil der historisch gemessenen negativen Rendite schlicht fortgesetzte fundamentale Schwäche ist, nicht Indexmechanik.

### b) Limits to Arbitrage
Leerverkauf von Deletion-Kandidaten ist strukturell schwieriger: geringe Marktkapitalisierung, dünne Liquidität, potenziell hohe/unmögliche Leihkosten genau im Handlungsfenster (viele Deletion-Kandidaten sind bereits "hard to borrow", weil sie fundamental unter Druck stehen). Das ist eine echte, strukturelle Arbitragegrenze — aber sie schützt die Anomalie nicht vor Erosion, sie verhindert nur, dass verbleibende Reste sauber captured werden können.

### c) Originalstudie
Chen, Noronha & Singal (2004), s.o. — zentrale Quelle für die asymmetrische Struktur dieses Sub-Effekts.

### d) Out-of-Sample-Evidenz
Identisch zu Additions: Greenwood & Sammon (2025) zeigen den Deletion-Effekt fällt von -16,1% (1990er) auf **-0,6% (2010er), statistisch insignifikant**. Damit ist auch die historisch dokumentierte Asymmetrie in der Praxis irrelevant geworden — beide Seiten sind auf ökonomisch vernachlässigbare Größenordnung geschrumpft.

### e) Kosten
Leerverkaufskosten (Borrow Fee, potenzieller Squeeze-Risiko) kommen zusätzlich zu den generischen Marktimpact-/Spread-Kosten hinzu. Bei einem Bruttosignal von -0,6% (insignifikant) ist die Nettorendite nach Shortkosten mit hoher Wahrscheinlichkeit negativ.

### f) Kapazität und Handelbarkeit
Gering. Deletion-Kandidaten sind per Definition kleinere, illiquidere Titel als der S&P-500-Durchschnitt; Shortability oft eingeschränkt.

### g) Regimeabhängigkeit und Tail-Risiko
Gleiches Bild wie Additions: monotoner Decay über 4 Dekaden. Zusätzliches Tail-Risiko: Short-Squeeze-Gefahr bei Deletion-Kandidaten, die gleichzeitig von Meme-/Retail-Flows betroffen sein können (strukturell nicht in den klassischen Studien erfasst, aber ein bekanntes Phänomen der 2020er-Jahre bei kleinkapitalisierten, stark geshorteten Titeln).

### h) Bekannte Kritik/Widerlegungen
Gleiche methodische Vorbehalte wie bei Additions (Selection Bias durch S&P-Komitee, potenzielle Fehlspezifikation von Faktormodellen in Event-Studien). Zusätzlich: ein Teil der historisch gemessenen negativen Rendite dürfte schlicht eine Distress-/Value-Risikoprämie sein, die mit dem Indexausschluss koinzidiert, aber nicht kausal durch ihn verursacht wird (reverse causality: Unternehmen werden ausgeschlossen, WEIL sie fundamental abgestürzt sind, nicht nur wegen mechanischem Verkaufsdruck).

**Urteil: KILL.** Wie Additions: Effekt in der relevanten Dekade insignifikant, zusätzlich strukturell schlechter handelbar (Shorting-Kosten) und stärker durch Selection-Bias/Fundamentaldistress kontaminiert als die Long-Seite.

---

## Kandidat 3: Russell-Rekonstitution (Anticipatory Trading / Reconstitution-Arbitrage)

### a) Ökonomische Begründung
Die jährliche (Ende Juni) Russell-1000/2000/3000-Rekonstitution ist **regelbasiert und transparent** (Ranking nach Marktkapitalisierung zum Stichtag Ende Mai, mit 5%-Banding zur Turnover-Reduktion seit 2007). Genau diese Transparenz erzeugt die Ineffizienz: Weil der Stichtag und die Methodik öffentlich bekannt sind, können Marktteilnehmer die Zusammensetzung Wochen im Voraus mit hoher Genauigkeit vorhersagen (vgl. akademisches Vorhersagemodell, veröffentlicht in *Journal of Finance*, "An Improved Method to Predict Assignment of Stocks into Russell Indexes"). Verursacher der Fehlbewertung: Indexfonds/ETFs, die aus Tracking-Error-Gründen gezwungen sind, exakt am Rekonstitutionstag (historisch: letzter Freitag im Juni, ein einzelner Handelstag mit extrem konzentriertem Volumen) zu handeln, unabhängig vom Preis. 2019 wurden an diesem einen Tag 1,2 Mrd. Aktien im Wert von 42,6 Mrd. USD in 1,14 Sekunden abgewickelt; das gesamte jährliche Rekonstitutions-Handelsvolumen liegt seit 2019 bei über 100 Mrd. USD.

Eine zusätzliche, sauber identifizierte kausale Quelle (nicht nur Eventstudie mit Kontrollgruppenproblem): **Chang, Hong & Liskovich (2015)**, *Review of Financial Studies* 28(1), S. 212–246 (NBER WP 19290), nutzen die Regression-Discontinuity-Eigenschaft an der Russell-1000/2000-Cutoff-Grenze — durch die wertgewichtete Konstruktion bekommen die kleinsten Russell-1000-Titel strukturell WENIGER passives Geld zugewiesen als die größten Russell-2000-Titel knapp unterhalb des Cutoffs, obwohl beide nahezu identische Marktkapitalisierung haben. Diese "künstliche" Diskontinuität in der Indexfonds-Nachfrage bei nahezu identischer Fundamentaldatenlage liefert einen der methodisch saubersten Kausalitätsbeweise der gesamten Indexeffekt-Literatur: mehr Indexgeld → höherer Preis, sauber getrennt von Fundamentaldaten.

### b) Limits to Arbitrage
Kapitalbedarf zur Vorpositionierung über Wochen, Prognoserisiko (Marktkapitalisierungs-Ranking kann sich bis zum Stichtag noch verschieben), Liquiditätsrisiko bei Small-/Micro-Caps (Russell 2000/Microcap-Segment), Shortability-Einschränkungen bei Deletion-Kandidaten. Zusätzlich: die eigentliche Preisverzerrung konzentriert sich auf ein extrem enges Zeitfenster (Sekunden bis Minuten am Rekonstitutionstag selbst) — ein Fonds ohne spezialisierte Ausführungsinfrastruktur (Program-Trading-Desk, Zugang zum "MOC"/Auktionsvolumen) kann hier strukturell nicht konkurrieren.

### c) Originalstudien
- **Madhavan (2003)**, *Financial Analysts Journal*, "The Russell Reconstitution Effect", S. 51–64: dokumentiert kumulative Überrenditen von Russell-1000-Additions von ca. 10,9% im Fenster um den Stichtag und Verluste von Russell-2000-Growth-Deletions von ca. -6,6% — die klassische, meistzitierte Referenz.
- **Chang, Hong & Liskovich (2015)**, s.o. — sauberste kausale Identifikation via RD-Design.

### d) Out-of-Sample-/Post-Publication-Evidenz
Im Gegensatz zu S&P 500 gibt es für Russell **keine gleichwertig belastbare "Disappearing Effect"-Studie** aus einem Top-Journal für die 2010er/2020er-Jahre. Stattdessen:
- **Micheli & Neuman (2020/2022)**, "Evidence of Crowding on Russell 3000 Reconstitution Events" (*Market Microstructure and Liquidity*, arXiv 2006.07456): zeigen mittels rekonstruierter CRSP-basierter Indexmitgliedschaft 1989–2019, dass jährlich rebalancierte Portfolios entlang des Russell-3000-Indexes **stärker gecrowded** sind als quartalsweise rebalancierte — ein direkter Hinweis, dass die Konzentration von Kapital auf den einen Rekonstitutionstag selbst zum Crowding-Problem für Arbitrageure wird, nicht nur für Indexfonds.
- Eine jüngere (nicht in einem Top-Journal, sondern als Masterarbeit/Aalto-Universität veröffentlichte) Untersuchung des Russell-1000-Rebalancing 2012–2021 findet einen anhaltenden "hidden cost" von 7,5 Basispunkten p.a., entsprechend ca. 11 Mrd. USD Verlust für Indexinvestoren pro Jahr, mit Preisverzerrungen von über 4% in den 20 Handelstagen vor Rekonstitution und einer Reversal-Bewegung von ca. -5,7% im Folgemonat. **Wichtige Einschränkung**: diese Quelle ist nicht peer-reviewed auf dem Niveau der S&P-Literatur; sie wird hier als Hinweis, nicht als belastbarer Beweis gewertet.
- FTSE Russell selbst reagiert aktiv auf die Kritik am Preisimpact: Banding-Regeln seit 2007 zur Turnover-Reduktion, und laufende Konsultationen (Stand jüngerer Marktberichte) über eine mögliche Umstellung auf **semi-annual** statt jährlicher Rekonstitution, explizit begründet mit dem gewachsenen Handelsvolumen von über 100 Mrd. USD am Rekonstitutionstag. Das zeigt: der Effekt existiert nach Einschätzung des Indexanbieters selbst noch, ABER die Struktur, auf der jede Strategie hier aufsetzen würde, ist in aktiver regulatorischer/methodischer Veränderung — ein Regimerisiko für jede kalibrierte Backtest-Strategie.

### e) Kosten
Petajisto (2011) beziffert den Index-Turnover-Cost für Russell-2000-Investoren (1990–2005) auf **38–77 Basispunkte p.a.** — deutlich höher als bei S&P 500 (21–28 Bp), was auf strukturell höhere Friktion im Small-Cap-Segment hindeutet, aber auch auf höhere Umsetzungskosten für jeden, der versucht, diese Ineffizienz zu erfassen (breitere Spreads, höherer Market Impact bei kleineren Titeln).

### f) Kapazität und Handelbarkeit
Das aggregierte Handelsvolumen ist hoch (>100 Mrd. USD am Rekonstitutionstag), aber die tatsächlich ausnutzbare Ineffizienz konzentriert sich auf eine begrenzte Zahl von Grenzfällen nahe den Cutoff-Punkten und ist bereits stark von spezialisierten Bank-Programmhandelsdesks und Index-Arb-Funds dominiert. Geschätzte realistische Kapazität für einen neuen, nicht-etablierten Marktteilnehmer: niedrig- bis mittel-zweistelliger Millionenbereich USD, bevor Eigen-Impact die Rendite auffrisst — deutlich unterhalb dessen, was die aggregierten 11 Mrd. USD/Jahr an Gesamtkosten suggerieren, da dieser Betrag auf viele konkurrierende Akteure verteilt bzw. von diesen bereits eingepreist wird.

### g) Regimeabhängigkeit und Tail-Risiko
Nur 1–2 messbare Hauptevents pro Jahr (Russell-Rekonstitution im Juni, ggf. IPO-bedingte Quartalsergänzungen) → geringe statistische Power pro Jahr, hohe Ergebnisvarianz zwischen einzelnen Jahren, kein Diversifikationseffekt innerhalb eines Kalenderjahres. Tail-Risiko: eine Methodikänderung (Semi-Annual-Umstellung, veränderte Banding-Regeln, veränderte Ankündigungsfenster) kann die historische Kalibrierung einer Strategie über Nacht entwerten.

### h) Bekannte Kritik/Widerlegungen
- Der historisch meistzitierte Madhavan-(2003)-Effekt stammt aus einer Periode mit deutlich geringerem Konkurrenzkapital; eine direkte Reproduktion mit heutigen Daten in einem Top-Journal fehlt.
- Micheli & Neuman zeigen explizit, dass genau der Umstand, der die Ineffizienz erzeugt (konzentriertes, vorhersagbares Handelsvolumen an einem Tag), auch die Konkurrenz unter Arbitrageuren maximiert — das strukturelle Argument für die Existenz der Ineffizienz ist zugleich das Argument für ihr Crowding.
- Chang/Hong/Liskovich (2015) zeigen zwar sauber kausal einen Preiseffekt aus Indexnachfrage, das ist aber ein Beleg für die generelle Downward-Sloping-Demand-These, nicht direkt ein Beweis für ein profitables, netto-kostenrobustes Handelssignal für Dritte.

**Urteil: WEAK.** Einzige Teilklasse mit dokumentierter, nicht eindeutig verschwundener struktureller Ineffizienz auch in jüngerer Zeit (2012–2021), aber: geringe Eventfrequenz, hohes Crowding, methodisch schwächere/weniger top-tier-abgesicherte jüngste Evidenzbasis, aktives regulatorisches Änderungsrisiko durch den Indexanbieter selbst. Erreicht nicht die Schwelle für CANDIDATE, da die Post-Publication-Evidenz nicht aus einem Top-Journal mit klarer Kostenrobustheits-Analyse für einen Drittanbieter stammt.

---

## Übergreifende Einschätzung der Klasse

**Nullhypothese nicht verworfen für die Hauptvariante (S&P 500).** Die Klasse "Index-Aufnahmen/-Ausschlüsse" ist ein Lehrbuchbeispiel für eine publizierte, danach systematisch wegarbitrierte Anomalie: Je bekannter und "lehrbuchhafter" ein Indexeffekt wurde (S&P 500 ist der meistzitierte Fall in jedem Lehrbuch zur Marktmikrostruktur), desto mehr strukturelles Arbitragekapital wurde aufgebaut, um genau diesen Effekt zu monetarisieren — mit dem Ergebnis, dass der Effekt selbst dadurch verschwand. Das ist konsistent mit McLean & Pontiff (2016)-artigen Post-Publication-Decay-Befunden für Anomalien generell, hier aber besonders drastisch und mehrfach unabhängig repliziert (Greenwood/Sammon 2025, Bennett et al. 2020, Preston & Soe 2021/S&P DJI selbst).

Russell-Rekonstitution ist die einzige Teilklasse, die eine ehrliche "WEAK" statt "KILL" verdient — nicht weil die Evidenz stark ist, sondern weil sie nicht eindeutig widerlegt ist und eine strukturelle, mechanische Ursache hat, die (im Gegensatz zu S&P 500) noch nicht durch eine gleichwertig belastbare Top-Journal-Studie für Netto-Verschwinden in der jüngsten Dekade dokumentiert wurde. Das rechtfertigt aber keine Kapitalallokation ohne eigene, aktuelle (Post-2022) Verifikation, insbesondere angesichts der laufenden Methodikdiskussion bei FTSE Russell.

**Empfehlung für das Portfolio-Komitee:** Diese Klasse insgesamt nicht für eine eigenständige Strategieallokation freigeben. Falls überhaupt eine Restoption verfolgt wird, dann ausschließlich die Russell-Rekonstitution mit (1) expliziter Kapazitätsobergrenze im niedrigen zweistelligen Millionenbereich, (2) laufender Neuvalidierung nach jeder FTSE-Russell-Methodikänderung, (3) Behandlung als Satellit-/Diversifikations-Sleeve, nicht als tragende Ertragsquelle, gegeben die extrem niedrige Eventfrequenz.

---

## Quellen (Auswahl, alle per Websuche Juli 2026 verifiziert)

- Harris, L. & Gurel, E. (1986). "Price and Volume Effects Associated with Changes in the S&P 500 List." *Journal of Finance* 41(4), 815–829.
- Shleifer, A. (1986). "Do Demand Curves for Stocks Slope Down?" *Journal of Finance* 41(3), 579–590.
- Chen, H., Noronha, G. & Singal, V. (2004). "The Price Response to S&P 500 Index Additions and Deletions: Evidence of Asymmetry and a New Explanation." *Journal of Finance* 59, 1901–1930.
- Greenwood, R. & Sammon, M. (2022/2025). "The Disappearing Index Effect." NBER WP 30748; *Journal of Finance* 80(2), 657–698. https://www.nber.org/papers/w30748
- Petajisto, A. (2011). "The Index Premium and Its Hidden Cost for Index Funds." *Journal of Empirical Finance* 18(2), 271–288.
- Madhavan, A. (2003). "The Russell Reconstitution Effect." *Financial Analysts Journal* 59(4), 51–64.
- Chang, Y.-C., Hong, H. & Liskovich, I. (2015). "Regression Discontinuity and the Price Effects of Stock Market Indexing." *Review of Financial Studies* 28(1), 212–246. NBER WP 19290.
- Micheli, A. & Neuman, E. (2020/2022). "Evidence of Crowding on Russell 3000 Reconstitution Events." *Market Microstructure and Liquidity*. arXiv:2006.07456.
- Denis, D., McConnell, J., Ovtchinnikov, A. & Yu, Y. (2003). "S&P 500 Index Additions and Earnings Expectations." *Journal of Finance* 58, 1821–1840.
- "Causal Inference in Financial Event Studies" (Nov. 2025). arXiv:2511.15123 — methodische Kritik an Eventstudien-Standardansätzen inkl. Index-Inklusion.
- FTSE Russell: "Four Decades of Russell US Indexes Reconstitution" sowie Marktkommentare zu Diskussion Semi-Annual-Rekonstitution (LSEG, 2023–2026).

Evidenzbasis: Websuche funktionierte während der Recherche (Juli 2026); Kernaussagen stützen sich auf direkt abgerufene Abstracts/Zusammenfassungen von NBER-, SSRN-, RFS- und JF-Quellen. Ein PDF-Volltextabruf (arXiv 2006.07456) schlug technisch fehl (nicht extrahierbarer Binärinhalt); die entsprechenden Aussagen stützen sich auf Suchergebnis-Snippets und Abstract-Seiten, nicht auf eigene Volltextprüfung — moderate Restunsicherheit bei Detailzahlen aus dieser einen Quelle.
