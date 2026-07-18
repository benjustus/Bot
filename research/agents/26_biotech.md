```yaml
agent: 26
klasse: "Biotech-Katalysatoren"
websuche_verfuegbar: ja
strategien:
  - name: "Pre-Event-Run-up / informationsgetriebene Vorpositionierung vor PDUFA- und Advisory-Committee-Terminen"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0.0-0.2 fuer Outsider-Replikation nach Kosten; deutlich hoeher nur fuer die informierten Erstpositionierer selbst"
    kernrisiko: "Wer dem dokumentierten 'informed flow' hinterherhandelt, wird strukturell zur Gegenpartei der eigentlich informierten Trader zum ungünstigsten Zeitpunkt (adverse selection) und traegt gleichzeitig das volle binaere Gap-Risiko (-80%/+300%)."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "PDUFA-/AdCom-Kalender: FDA.gov 'Drugs@FDA' (frei); Kurse: Yahoo Finance/Stooq (frei). Options-IV/-Volumen-Signale (Kern der Originalstudien) NICHT frei verfuegbar (OptionMetrics/CBOE LiveVol kostenpflichtig)."
  - name: "Optionspraemien-Verkauf / 'IV-Crush'-Harvesting um binaere FDA-Events (Short Straddle/Strangle)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 1
      signifikanz_nach_mtk: 1
      regimestabilitaet: 1
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "unklar/vermutlich <=0 nach Tail-Risiko-Adjustierung (Brutto-Trackrekords ohne Tail-Jahre sind survivorship-verzerrt)"
    kernrisiko: "Katastrophales, geclustertes Tail-Risiko ('picking up nickels in front of a steamroller'); ein einzelnes -85%- oder +300%-Gap-Event kann Jahre an aufgelaufenen Praemieneinnahmen ausloeschen. Keine belastbare akademische Quantifizierung gefunden - Evidenzbasis ist Trading-Blog-Folklore."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
  - name: "Post-Event-Drift nach FDA-Entscheid ('Sell-the-News' vs. Momentum-Fortsetzung)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 1
      signifikanz_nach_mtk: 1
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "~0.0, kein robuster Nachweis eines Vorzeichens"
    kernrisiko: "Literatur und Praktiker-Quellen widersprechen sich ueber das Vorzeichen des Effekts (Drift vs. Sell-the-News) fuer dieselbe Ereignisklasse - ein klassisches Warnsignal fuer Post-hoc-Narrativ statt robustem Effekt."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "FDA.gov PDUFA-Kalender (frei) + Yahoo Finance/Stooq Kurshistorien (frei)"
```

# Agent 26 — Anomalieklasse "Biotech-Katalysatoren" (FDA/PDUFA-Events, Phase-Uebergaenge, Run-up/Drift)

## Zusammenfassung fuer Eilige

Die akademische Literatur zu Biotech-Katalysator-Events ist **duenn, jung und ueberwiegend deskriptiv statt strategie-validierend**. Es existieren real begutachtete Fachartikel (JNCI, Journal of Business Finance & Accounting, Journal of Corporate Finance), die **Informationslecks/informierten Handel vor FDA-Entscheidungen** robust dokumentieren — das ist mehr als reine Folklore. Aber: keine dieser Studien liefert einen Netto-nach-Kosten-Backtest einer handelbaren Strategie fuer Aussenstehende, keine liefert Out-of-Sample-Decay-Evidenz nach Publikation, und die Kosten (Borrow-Fees 15-30%+ p.a. in Small-Cap-Biotech, Options-Spreads von 10-30% der Praemie in illiquiden Namen) sitzen exakt dort, wo die Effekte am groessten sind. Die zweite Praktiker-Lieblingsstrategie (Vol-Verkauf/"IV-Crush"-Harvesting) hat **keine belastbare akademische Grundlage** — nur Trading-Blog-Content ohne Stichprobe, ohne t-Statistik, ohne Tail-Risiko-adjustierte Performance. Die dritte Kandidatin (Post-Event-Drift) scheitert an sich selbst widersprechenden Befunden.

**Gesamturteil der Klasse: Kein CANDIDATE. Die Nullhypothese (kein systematisch handelbares Alpha) wird nicht widerlegt.** Die Klasse eignet sich bestenfalls fuer sehr kleine, opportunistische, fundamental-informierte Einzelwetten mit Optionsstruktur (kein systematischer Faktor), nicht fuer eine skalierbare quantitative Strategie eines institutionellen Fonds.

---

## Methodischer Hinweis

Websuche war verfuegbar und wurde genutzt (Stand: Juli 2026, Abfragezeitraum der Quellen 2011-2026). Ergaenzend fliesst internes Wissensstand-Anfang-2026-Vorwissen zur Einordnung ein, wo Websuche keine belastbaren Primärquellen lieferte (insbesondere Kandidat 2). Die durchsuchte Literatur ist tatsaechlich klein — im Gegensatz zu PEAD, Momentum oder Value gibt es fuer "Biotech-Katalysatoren" **keine etablierte, mehrfach replizierte Kernstudie mit Konsens-Effektgroesse**. Das ist selbst ein Befund und wird im Urteil entsprechend streng gespiegelt.

---

## Kandidat 1: Pre-Event-Run-up / informierter Optionshandel vor FDA-Entscheidungen

### a) Oekonomische Begruendung

Drei sich ueberlagernde Kanaele werden in der Literatur diskutiert:

1. **Informationsasymmetrie / Leckage**: An FDA-Advisory-Committee-Sitzungen sind Dutzende Personen beteiligt (Ausschussmitglieder, klinische Pruefer an Studienstandorten, Data-Safety-Monitoring-Boards, Sell-Side-Analysten mit Experten-Netzwerken, Unternehmensinsider). Bei kleinen Single-Asset-Biotechs ist der "information float" extrem eng, was Leckage vor der offiziellen Bekanntgabe beguenstigt.
2. **Retail-Lottery-Demand**: Kleinanleger kaufen vor Katalysator-Terminen bevorzugt kurzlaufende, weit aus dem Geld liegende Calls (positiv schiefe, lotterieartige Auszahlungsprofile, konsistent mit der Boyer/Vorkink-Praeferenz fuer Skewness) — das erzeugt Rauschen, aber auch Volumen, in dem sich echte Informationstrader tarnen koennen.
3. **Institutionelles De-Risking**: Manche institutionelle Halter reduzieren Positionen vor binaeren Events aus Risikomanagement-/Karrieregruenden unabhaengig vom Erwartungswert (Benchmark-Tracking-Angst vor extremen Einzeltitel-Ausschlaegen), was systematische Pre-Event-Verkaufsstroeme erzeugen kann, die nicht informationsbasiert sind.

### b) Limits to Arbitrage

- **Borrow-Kosten**: Fuer Small-Cap-Biotech-Aktien (<100 Mio. USD Marktkapitalisierung) liegen durchschnittliche Leihgebuehren Berichten zufolge bei >30% p.a.; auch bei mittleren Namen sind 15-25% p.a. keine Seltenheit, gegenueber ~80 Basispunkten im breiten Marktdurchschnitt (wertgewichtet). Wer den Run-up leerverkaufen oder gegen ein negatives Advisory-Ergebnis positionieren will, zahlt diese Praemie — oft genau in den Namen, in denen der akademisch dokumentierte Effekt am staerksten ist (kleine, governance-schwache Firmen).
- **Optionsmarkt-Illiquiditaet**: Kleine Biotech-Namen haben duenne Options-Orderbuecher; nur wenige Strikes/Laufzeiten mit nennenswertem Open Interest. Wer versucht, dieselben kurzlaufenden OTM-Calls zu kaufen, die die Literatur als Signaltraeger identifiziert, bewegt IV und Preis gegen sich selbst und zahlt breite Spreads.
- **Kapitalkosten fuer Optionspositionen**: Prime-Broker-Margin-Anforderungen fuer Positionen in Namen mit bevorstehenden binaeren Events sind erhoeht.

### c) Originalstudien (Stichprobe, Effektgroesse, Signifikanz)

- **Rothenstein, Tomlinson, Tannock, Detsky (2011)**, *"Company Stock Prices Before and After Public Announcements Related to Oncology Drugs"*, Journal of the National Cancer Institute 103(20):1507-1512. Untersucht Aktienkursbewegungen von Onkologie-Wirkstoffentwicklern vor und nach oeffentlicher Bekanntgabe von Phase-III-Ergebnissen/FDA-Entscheidungen; findet Kursbewegungen bereits vor der offiziellen Bekanntgabe, die mit dem letztendlichen Ergebnis korrelieren — konsistent mit Informationsleckage. Kleine, auf Onkologie beschraenkte Stichprobe.
- **Aeltere indirekte Evidenz** (PubMed-ID 10736971, "Biotechnology stock prices before public announcements: evidence of insider trading?", ca. 2000): Berichtet eine Differenz der kumulierten Kursbewegung im Fenster -120 bis -3 Tage vor Bekanntgabe zwischen ex-post "Gewinnern" (~+27%) und "Verlierern" (~-4%) klinischer Studien/FDA-Entscheidungen. **Methodische Warnung**: Die Gewinner/Verlierer-Klassifikation erfolgt ex post — das ist ein Blick-nach-vorn-Bias-Risiko (Look-ahead-Bias), der die Effektgroesse mechanisch aufblaeht, wenn er nicht sauber aus einer echten Handelsregel heraus konstruiert wird. Als Beleg fuer "Leckage existiert" brauchbar, als Beleg fuer eine handelbare Strategie nicht.
- **Bohmann & Patel (2022)**, *"Informed options trading prior to FDA announcements"*, Journal of Business Finance & Accounting 49(7-8):1211-1236. 21-Jahres-Stichprobe. Optionsvolumen, Implied-Volatility-Spreads und Order-Imbalance sind in den 5 Handelstagen vor der FDA-Entscheidung abnormal erhoeht und sagen die Aktienrendite am Entscheidungstag signifikant vorher; Effekt konzentriert sich auf kleinere Firmen und Firmen mit schwaecherer Corporate Governance.
- **Wu, Borochin, Golec (2024)**, *"Informed options trading before FDA drug advisory meetings"*, Journal of Corporate Finance 84. Rund 32% der Advisory-Committee-Sitzungen zeigen statistisch signifikantes abnormales Optionsvolumen vor dem Sitzungstermin, konzentriert in kurzlaufenden, weit aus dem Geld liegenden Kontrakten; mehr Call- vor Zulassungen, mehr Put-Kaeufe vor Ablehnungen — die Optionspositionierung sagt die Post-Meeting-Rendite vorher.
- Ergaenzend: eine 2022 auf arXiv erschienene Arbeit (*"New drugs and stock market: how to predict pharma market reaction to clinical trial announcements"*) nutzt Machine-Learning-Ansaetze zur Vorhersage der Marktreaktion auf Studienankuendigungen — methodisch interessant, aber eine Prognose-/Klassifikationsstudie, keine kostenbereinigte Handelsstrategie-Validierung.

**Einordnung**: Dies ist die staerkste Teilliteratur der gesamten Klasse — drei unabhaengige, in angesehenen Fachzeitschriften begutachtete Arbeiten ueber gut zwei Jahrzehnte kommen qualitativ zum selben Schluss (Informationsasymmetrie vor FDA-Events ist messbar). Das ist mehr Konvergenz, als man in vielen anderen "Nischen-Anomalien" findet.

### d) Out-of-Sample-/Post-Publication-Evidenz und Decay

Hier wird die Evidenz duenn: Es existiert **keine mir bekannte Studie, die die Bohmann/Patel- oder Wu/Borochin/Golec-Signale nach Publikation (2022 bzw. 2024) auf Decay oder auf Netto-Rendite fuer einen Nachbildner testet**. Die Rothenstein-Arbeit (2011) ist alt genug, dass ein Decay-Test grundsaetzlich moeglich waere, wurde aber in der durchsuchten Literatur nicht gefunden. Der generelle akademische Befund zu Anomalie-Decay (McLean/Pontiff-Stil: durchschnittlich 26-58% Renditerueckgang nach Publikation ueber viele Anomalien hinweg) ist die einzig verfuegbare Referenzgroesse — es gibt keine biotech-spezifische Messung. Das Fehlen jeglicher Post-Publication-Decay-Studie fuer eine so junge, kleine Literatur ist an sich ein Signal: Diese Papers wurden bislang primaer als **Marktmikrostruktur-/Regulierungsbefund** (moegliches Insider-Trading, SEC-Ueberwachungsluecke) rezipiert, nicht als Grundlage fuer institutionelle Strategieentwicklung.

### e) Kosten

- Bid-Ask-Spreads in Small-Cap-Biotech-Aktien: mehrere Prozent des Kurses bei Nebenwerten.
- Options-Spreads: in den relevanten (kleinen, illiquiden) Namen haeufig 10-30% der Mitte, gerade bei den kurzlaufenden OTM-Kontrakten, die laut Studien das Signal tragen.
- Borrow-Fees: 15-30%+ p.a. fuer die relevanten Small-Cap-Namen (Quellen: S3 Partners/Marktdaten-Aggregatoren, Stand 2023-2024).
- Marktimpact: Bereits kleine Kauforders in den duennen Optionsketten bewegen IV messbar.

### f) Kapazitaet und Handelbarkeit

Sehr klein. Pro Quartal gibt es realistischerweise nur eine Handvoll PDUFA-/AdCom-Termine mit ausreichend liquiden Optionsmaerkten, um eine Position ueberhaupt ohne prohibitive Slippage aufzubauen. Geschaetzte Gesamtkapazitaet ueber alle handelbaren Events eines Jahres: eher im niedrigen zweistelligen Millionenbereich (USD) als hoeher, wenn Kosten- und Marktimpact-Disziplin eingehalten werden sollen. Fuer einen institutionellen Fonds mit relevanter AUM ist das ein Rundungsfehler, kein Portfoliobaustein.

### g) Regimeabhaengigkeit und Tail-Risiko

FDA-Regulierungsregime sind nicht stationaer: beschleunigte Zulassungswege (Breakthrough Therapy, Priority Review), COVID-Ausnahmeregelungen (EUA), und politische Unsicherheit rund um FDA-Fuehrung/-Philosophie (2025/2026 ist ein Beispielzeitraum mit erhoehter politischer Aufmerksamkeit auf die FDA-Leitung) veraendern die Grundverteilung der Ereignisse laufend. Binaere Gaps von -80% bis +300% an einem einzigen Handelstag sind gut dokumentiert und historisch wiederkehrend (z. B. bei gescheiterten Phase-III-Studien oder ueberraschenden Ablehnungen bzw. Zulassungen kleiner Single-Asset-Biotechs). Ein Signal-Follower traegt das volle Gap-Risiko, hat aber (per Definition, da er dem informierten Flow hinterherlaeuft) einen zeitlichen Nachteil gegenueber den urspruenglich informierten Akteuren.

### h) Kritik/Widerlegungen

- **Adverse Selection fuer Nachahmer**: Wenn ein Teil der Optionsbewegung vor FDA-Events tatsaechlich informiert ist (wie die Studien nahelegen), dann ist ein Aussenstehender, der diesem Flow hinterherhandelt, strukturell die Gegenpartei mit dem Informationsnachteil — er kauft/verkauft, nachdem die eigentliche Information bereits eingepreist wird, und traegt das Restrisiko.
- **Look-ahead-Bias** in der aeltesten Studie (ex-post Gewinner/Verlierer-Klassifikation).
- **Kleine Stichproben**: Alle referenzierten Arbeiten arbeiten mit Ereigniszahlen im niedrigen drei- bis vierstelligen Bereich ueber lange Zeitraeume (teils 21 Jahre) — das entspricht wenigen Dutzend bis wenigen Hundert unabhaengigen "Events pro Jahr", was die statistische Power fuer robuste Multiple-Testing-Korrektur einschraenkt.
- **Deskriptiv, nicht strategisch**: Keine der Studien liefert eine Netto-Kosten-Sharpe-Ratio fuer eine implementierbare Strategie. Sie beantworten "existiert informierter Handel?", nicht "kann ein Fonds X damit nach Kosten Geld verdienen?".
- **Regulatorische Grauzone**: Ein Teil der dokumentierten Musters ist explizit als potenzielles (illegales) Insider-Trading interpretiert (vgl. CLS Blue Sky Blog-Kommentare zu den Studien) — das ist fuer einen legitimen institutionellen Fonds ohnehin kein Fundament fuer eine Strategie, sondern hoechstens eine Warnung, in welchen Namen man selbst nicht unwissentlich gegen informierte Flows handelt.

**Urteil: WEAK.** Die zugrunde liegende Informationsasymmetrie ist die akademisch am besten abgesicherte Beobachtung der gesamten Klasse (drei unabhaengige, begutachtete Studien, qualitativ konsistent ueber 20+ Jahre). Aber: keine dokumentierte Post-Publication-Netto-Strategie-Evidenz, keine Kostenrobustheit (Kosten sitzen exakt dort, wo der Effekt am staerksten ist), extrem kleine Kapazitaet, und ein struktureller Adverse-Selection-Nachteil fuer jeden Nachahmer. Das erfuellt nicht die CANDIDATE-Schwelle ("dokumentierte Post-Publication-Evidenz UND Kostenrobustheit"), ist aber auch nicht reine Folklore — daher WEAK statt KILL.

---

## Kandidat 2: Optionspraemien-Verkauf um binaere FDA-Events ("IV-Crush"-Harvesting)

### a) Oekonomische Begruendung

Die These: Implizite Volatilitaet vor binaeren FDA-Events wird durch strukturelle Lottery-Demand (Kleinanleger kaufen bevorzugt billige, weit aus dem Geld liegende Calls fuer asymmetrische Auszahlungsprofile) systematisch ueber den fairen Wert hinaus aufgeblaeht (IV teils 150-300%+ in der letzten Woche vor der Entscheidung, fallend auf 30-50% danach). Analog zur gut dokumentierten Volatilitaetsrisikopraemie bei Aktienindizes und, mit duennerer Evidenz, bei Ergebnisankuendigungen (Earnings), sollte ein systematischer Verkaeufer dieser Praemie im Erwartungswert verdienen.

### b) Limits to Arbitrage

- Extreme Optionsmarkt-Illiquiditaet in genau den kleinen Namen, wo die Praemien am hoechsten erscheinen; oft nur 1-2 Strikes mit nennenswertem Open Interest.
- Margin-/Kapitalanforderungen fuer ungedeckte oder teilgedeckte Short-Vol-Positionen vor binaeren Events sind bei Primebrokern deutlich erhoeht bis prohibitiv.
- Market Maker bepreisen genau dieses Ereignisrisiko bewusst mit breiten Spreads (10-30% der Mitte) — die vermeintliche Praemie wird zu einem erheblichen Teil beim Ein- und Ausstieg wieder abgegeben.

### c) Originalstudien

**Hier ist die Literaturbasis am duennsten der gesamten Klasse.** Trotz gezielter Suche wurde **keine einzige begutachtete akademische Arbeit** gefunden, die eine biotech-FDA-event-spezifische Volatilitaetsrisikopraemie mit Stichprobe, Effektgroesse und t-Statistik quantifiziert. Alle gefundenen Quellen (SpotGamma, JournalPlus, QuantStrategy.io, BullishBears, MenthorQ, etrade-Kommentar) sind Trading-Blogs/Broker-Content ohne Peer-Review, ohne Stichprobenangabe, ohne Signifikanztest. Sie beschreiben die Mechanik plausibel (IV-Niveaus, Crush-Groessenordnung), liefern aber **keine** rigorose Backtest-Performance-Kennzahl. Die naeheste verwandte akademische Literatur (Dubinsky/Johannes 2006 zu Earnings-Announcement-Optionspreisen; generelle Index-VRP-Literatur) ist nicht biotech-spezifisch und ueberträgt sich wegen der viel extremeren, bidirektionalen Tail-Verteilung bei FDA-Events nur eingeschraenkt.

Dies deckt sich exakt mit der Warnung des Auftrags: **"vieles ist Praktiker-Folklore."**

### d) Out-of-Sample-/Post-Publication-Evidenz und Decay

Nicht anwendbar mangels Originalstudie. Kein Post-Publication-Decay messbar, wenn es keine Publication mit Methodik/Stichprobe gibt, die dekayen koennte.

### e) Kosten

Options-Spreads von 10-30%+ der Praemie in den relevanten Namen; Margin-/Kapitalbindungskosten; potenzielle Pin-/Assignment-Risiken; bei ungedeckten Strukturen im Extremfall Nachschusspflichten.

### f) Kapazitaet und Handelbarkeit

Noch kleiner als Kandidat 1: praktisch nur in der Handvoll liquidesten Biotech-Namen mit tiefen Optionsketten ueberhaupt sinnvoll ausfuehrbar (die typischen von Retail-Options-Plattformen breit abgedeckten "grossen" Biotech-Ticker). Realistische Kapazitaet fuer eine systematische Version: niedriger einstelliger bis niedriger zweistelliger Millionenbereich (USD) Risikokapital, bevor Marktimpact/Verfuegbarkeit zum Problem wird.

### g) Regimeabhaengigkeit und Tail-Risiko

Das zentrale Problem der Strategie: Die Auszahlungsstruktur eines systematischen Short-Vol-Ansatzes um binaere Events ist per Konstruktion **linksschief mit fetten Enden** (viele kleine Gewinne, seltene aber katastrophale Verluste). Gap-Bewegungen von -80% bis +300% an einem Tag sind in Biotech historisch wiederholt aufgetreten und koennen selbst gut diversifizierte Portfolios treffen, wenn mehrere Events korreliert ausfallen (z. B. sektorweite regulatorische Schocks, correlated FDA-Politik-Aenderungen). Ohne belastbare Originalstudie laesst sich nicht einmal seriös beziffern, wie oft/schwer solche Clustering-Ereignisse historisch die kumulierte Praemieneinnahme ausgeloescht haben — das ist selbst ein Warnsignal.

### h) Kritik/Widerlegungen

- **Survivorship in Praktiker-Trackrekords**: Oeffentlich beworbene "Erfolgsgeschichten" von Options-Einkommens-Strategien um Biotech-Events stammen fast ausschliesslich aus Perioden ohne grosses Tail-Event im Portfolio — klassischer Survivorship-/Cherry-Picking-Bias. Ein Verweis in den Suchergebnissen auf eine angebliche "FDA Fast Track Designation"-Studie mit kumulierten abnormalen Renditen von +21,59% (5 Tage), +38,34% (30 Tage), +76,64% (1 Jahr) und +111,37% (3 Jahre) gegenueber dem XBI-Biotech-Index ist ein Lehrbuchbeispiel fuer genau dieses Problem: Solche Groessenordnungen ueber 1-3 Jahre reflektieren fast sicher generelles Biotech-Beta/Bullenmarkt-Timing und Small-Sample-/Survivorship-Effekte, nicht einen sauber isolierten Ereigniseffekt. Sie sollten als Warnbeispiel, nicht als Evidenz gelesen werden.
- **Selection Bias**: Wer im Nachhinein von profitablen Vol-Verkaeufer-Strategien berichtet, hat fast per Definition die Jahre mit Tail-Verlusten entweder noch nicht erlebt oder nicht oeffentlich gemacht.
- **Keine Multiple-Testing-Korrektur moeglich**, da keine formale Studie mit Testdesign vorliegt.
- Kandidat 1 untergraebt Kandidat 2 zusaetzlich inhaltlich: Wenn ein relevanter Teil der Options-Praemie vor FDA-Events durch **echte Information** (nicht nur Lottery-Noise) getrieben ist, wie Bohmann/Patel und Wu/Borochin/Golec zeigen, dann verkauft ein systematischer Vol-Seller nicht nur "overpriced noise", sondern teilweise gegen echten Informationsvorsprung — ein strukturell schlechterer Trade als die einfache Lottery-Demand-Geschichte suggeriert.

**Urteil: KILL.** Keine akademische Originalstudie mit Stichprobe/Effektgroesse/t-Statistik auffindbar; die gesamte Evidenzbasis ist Praktiker-Content ohne Signifikanztest; das Tail-Risiko-Profil ist bei so duenner Evidenzlage nicht verantwortbar in ein institutionelles Strategiemandat zu uebernehmen.

---

## Kandidat 3: Post-Event-Drift nach FDA-Entscheidung ("Sell-the-News" vs. Momentum-Fortsetzung)

### a) Oekonomische Begruendung

Zwei einander widersprechende Storylines kursieren parallel:
1. **Unterreaktions-/Drift-These** (analog PEAD): Anleger verarbeiten komplexe klinische/regulatorische Information nur langsam vollstaendig, sodass der Kurs nach einer positiven/negativen Entscheidung noch einige Wochen in dieselbe Richtung weiterlaeuft.
2. **"Sell-the-News"-These**: Wenn eine Zulassung weitgehend erwartet/eingepreist war, fuehrt die Bestaetigung selbst zu Gewinnmitnahmen und einer Drift **entgegen** der Nachrichtenrichtung.

### b) Limits to Arbitrage

Falls ein echter Drift-Effekt existiert, waere er in liquiden Post-Event-Namen grundsaetzlich guenstiger handelbar als Kandidat 1/2 (kein Optionsmarkt noetig, kein akutes binaeres Gap-Risiko mehr, da das Ereignis bereits eingetreten ist). Das einzige Handelbarkeitsproblem waere Borrow-Kosten fuer die Short-Seite bei negativer Drift-These in Small-Caps.

### c) Originalstudien

Die durchsuchte Literatur liefert **keine robuste, in sich konsistente Kernstudie speziell zu mittelfristiger (1-6 Monate) Kursdrift nach FDA-Entscheidungen**. Die einschlaegigen Event-Studien (Rothenstein 2011 JNCI; die PLOS-ONE-Arbeit "Stock Market Returns and Clinical Trial Results of Investigational Compounds" zu grossen Biopharma-Unternehmen; eine 2022 in PMC erschienene Arbeit "The reaction of sponsor stock prices to clinical trial outcomes") fokussieren fast ausschliesslich auf **kurze Ereignisfenster (0 bis +3/+5 Tage)**, nicht auf mittelfristige Drift. Ein 2025 auf ScienceDirect erschienener Titel ("Long-term market reactions to FDA Phase III clinical trials announcements") deutet auf eine neuere Arbeit zu genau dieser Frage hin, jedoch ohne dass Stichprobe/Effektgroesse aus der Suche extrahierbar waren — hier bleibt die Evidenzlage fuer diesen Bericht unklar und sollte vor jeder Kapitalallokation im Original gelesen werden.

### d) Out-of-Sample-/Post-Publication-Evidenz und Decay

Keine auffindbar.

### e) Kosten

Falls handelbar: moderate Spreads in liquideren Post-Event-Namen, aber weiterhin hohe Borrow-Fees fuer eine Short-Seite in Small-Cap-Biotech.

### f) Kapazitaet und Handelbarkeit

Potenziell hoeher als Kandidat 1/2 (kein Optionsmarkt-Flaschenhals), aber irrelevant, solange kein robustes Vorzeichen des Effekts feststeht.

### g) Regimeabhaengigkeit und Tail-Risiko

Geringeres akutes Gap-Risiko als bei den beiden anderen Kandidaten, da das Hauptereignis bereits eingepreist ist. Regimeabhaengigkeit besteht dennoch (Sektor-Sentiment, Zinsumfeld fuer unprofitable Biotechs, M&A-Aktivitaet als konkurrierender Kurstreiber nach Zulassung).

### h) Kritik/Widerlegungen

- **Sich widersprechende Storylines fuer dieselbe Ereignisklasse** (Drift-Fortsetzung vs. Sell-the-News) in denselben Praktiker-/Uebersichtsquellen sind ein klassisches Warnsignal: Wenn ein Phaenomen je nach Einzelfall und Erzaehler mal in die eine, mal in die andere Richtung "erklaert" wird, handelt es sich haeufig um Post-hoc-Rationalisierung von Einzelbeispielen statt um einen robusten, vorab spezifizierten Effekt.
- Keine unabhaengige Replikation mit konsistentem Vorzeichen gefunden.
- Vermischung mit allgemeinerer Small-Cap-Momentum-/PEAD-Literatur ist naheliegend, aber eine biotech-spezifische Praemie ueber die allgemeine PEAD-Praemie hinaus ist nicht belegt.

**Urteil: KILL.** Zu duenne, in sich widerspruechliche Evidenzlage fuer ein Vorzeichen, geschweige denn eine Effektgroesse.

---

## Uebergreifende Wuerdigung der Klasse

1. **Die Literatur ist tatsaechlich duenn**, wie in der Aufgabenstellung antizipiert. Ausserhalb der drei Optionsmarkt-Mikrostruktur-Arbeiten (Rothenstein 2011; Bohmann & Patel 2022; Wu, Borochin & Golec 2024) gibt es kaum peer-reviewte Finance-Literatur, die eine handelbare Strategie mit Stichprobe/Effektgroesse/t-Statistik fuer diese Anomalieklasse validiert. Vieles, was in der Praktiker-Welt als "PDUFA-Play" oder "IV-Crush-Strategie" kursiert, ist unbelegte Folklore.
2. **Wo Evidenz existiert, dokumentiert sie primaer Marktmikrostruktur/Informationsleckage — nicht validierte Handelsstrategien.** Das ist ein wichtiger Unterschied: "Informierter Handel existiert" ist nicht dasselbe wie "ein Aussenstehender kann diesen Handel nach Kosten profitabel nachbilden".
3. **Kosten und Kapazitaet sind in dieser Klasse besonders unguenstig konzentriert**: Borrow-Fees und Options-Spreads sind exakt in den kleinen, governance-schwachen Namen am hoechsten, in denen die akademisch dokumentierten Effekte am staerksten sind. Das ist keine zufaellige Korrelation, sondern strukturell: Illiquiditaet und Informationsasymmetrie bedingen sich gegenseitig.
4. **Binaeres Tail-Risiko dominiert jede Kosten-Ertrags-Rechnung.** Ohne belastbare Stichproben-Statistik zur Haeufigkeit und Clusterung von -80%/+300%-Gaps kann keine der drei Kandidatenstrategien seriös als kapitalallokationswuerdig eingestuft werden.
5. **Kein Kandidat erreicht die CANDIDATE-Schwelle** ("dokumentierte Post-Publication-Evidenz UND Kostenrobustheit"). Kandidat 1 kommt akademisch am naechsten heran, scheitert aber an fehlender Post-Publication-Netto-Kosten-Evidenz und an strukturell prohibitiven Kosten in genau den relevanten Namen.

**Ehrliches Fazit**: Diese Anomalieklasse ist fuer einen systematischen, skalierbaren institutionellen Ansatz **de facto tot** — nicht weil die zugrunde liegenden oekonomischen Mechanismen (Informationsasymmetrie, Lottery-Demand, De-Risking-Fluesse) unplausibel waeren, sondern weil (a) die akademische Evidenzbasis zu duenn und zu deskriptiv ist, um eine Netto-Strategie zu validieren, (b) Kosten und Kapazitaet strukturell genau dort am schlechtesten sind, wo die Effekte am staerksten scheinen, und (c) das binaere Tail-Risiko jede optisch attraktive Sharpe-Ratio-Schaetzung ohne lange, tail-inklusive Stichprobe unglaubwuerdig macht. Einzelne, klein dimensionierte, fundamental recherchierte Optionswetten auf spezifische Katalysatoren mögen fuer einen diskretionaeren Spezialisten mit echtem Informationsvorsprung (klinische Expertise, Expertennetzwerk) funktionieren — das ist aber Stock-Picking mit Spezialwissen, keine systematische, aus dieser Literatur ableitbare Faktor-/Anomalie-Strategie, und faellt damit ausserhalb des Mandats eines quantitativen, reproduzierbaren Forschungsprogramms.

---

## Quellen (aus Websuche, Juli 2026)

- Rothenstein, Tomlinson, Tannock, Detsky (2011), JNCI 103(20):1507-1512 — Company Stock Prices Before and After Public Announcements Related to Oncology Drugs (via Semantic Scholar / Oxford Academic).
- PubMed 10736971 — Biotechnology stock prices before public announcements: evidence of insider trading?
- Stock Market Returns and Clinical Trial Results of Investigational Compounds: An Event Study Analysis of Large Biopharmaceutical Companies, PLOS ONE (2013) / PMC3737210.
- The reaction of sponsor stock prices to clinical trial outcomes: An event study analysis, PMC9439234 (2022).
- Bohmann & Patel (2022), Journal of Business Finance & Accounting 49(7-8):1211-1236 — Informed options trading prior to FDA announcements.
- Wu, Borochin, Golec (2024), Journal of Corporate Finance 84 — Informed options trading before FDA drug advisory meetings (ScienceDirect/IDEAS-RePEc).
- New drugs and stock market: how to predict pharma market reaction to clinical trial announcements, arXiv:2208.07248 (2022).
- Long-term market reactions to FDA Phase III clinical trials announcements, ScienceDirect (2025) — Titel identifiziert, Inhalt nicht vollstaendig verifizierbar aus Suchausschnitt.
- S3 Partners — U.S. Stock Borrow Fees; diverse Marktdaten-Aggregatoren zu Borrow-Fee-Niveaus in Small-Cap-/Hard-to-Borrow-Aktien.
- Diverse Trading-/Options-Broker-Content-Quellen (SpotGamma, JournalPlus, QuantStrategy.io, BullishBears, MenthorQ) zu IV-Crush-Mechanik — explizit als nicht-akademische, unbelegte Praktiker-Quellen gekennzeichnet und entsprechend gewichtet.
