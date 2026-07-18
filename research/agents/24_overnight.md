```yaml
agent: 24
klasse: "Overnight-Effekt"
websuche_verfuegbar: ja
strategien:
  - name: "Naiver Close-to-Open Overnight-Drift (Index/Futures/ETF, Cliff/Cooper/Gulen 2008; Boyarchenko/Larsen/Whelan 2020)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 1
      handelbarkeit: 2
      kapazitaet: 4
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.12
    netto_sharpe_erwartung: "~0.0, netto seit 2021 eher leicht negativ"
    kernrisiko: "Effekt ist gemäss Post-Publication-Studie der Originalautoren (NY Fed, Juli 2026) seit 2021 auf effektiv null kollabiert; selbst brutto reichten historische ~3.6-3.7%/Jahr nicht, um realistische Handelskosten von ~5%/Jahr (252 Round-Trips) zu decken; unkompensiertes Gap-/Tail-Risiko in Krisen (Marz 2020, Circuit Breaker)"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "SPY/^GSPC/ES-Futures OHLC via Yahoo Finance (Open vs. Vortages-Close); kein Ken-French-Datensatz verfuegbar (Ken French fuehrt keine Overnight/Intraday-Zerlegung)"
  - name: "Cross-sektionaler Overnight/Intraday Tug-of-War (Momentum-Zerlegung, Lou/Polk/Skouras 2019; Akbas/Boehmer/Jiang/Koch 2022)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 3
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.30
    netto_sharpe_erwartung: "0.1-0.3 brutto vor Kosten; nahe 0 fuer eigenstaendige Standalone-Strategie netto"
    kernrisiko: "Kosten der Cross-Sektions-Strategie werden in den Originalstudien nicht quantifiziert; Signal ueberlappt stark mit bekanntem Momentum-/Reversal-Faktor (fragliche inkrementelle Kapazitaet); Post-2019-Evidenz stammt aus verwandten, nicht identischen Replikationsstudien"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Taegliche OHLC-Kurse breiter Aktienuniversen (Yahoo Finance/Stooq) zur groben Open/Close-Zerlegung; fuer saubere Replikation waeren CRSP/TAQ-Intraday-Daten noetig; kein Ken-French-Datensatz"
```

# Agent 24 — Anomalieklasse "Overnight-Effekt"

## Zusammenfassung des Urteils

Diese Klasse ist im Kern **tot** oder zumindest **klinisch fast tot**. Der Haupteffekt — dass die gesamte Aktienrisikopraemie ueber Nacht anfaellt — war real, gut dokumentiert und oekonomisch erklaerbar (Inventar-Risiko von Market-Makern). Aber genau die aktuellste verfuegbare Evidenz, die im Rahmen dieser Recherche gefunden wurde (ein Fed-Papier vom **Juli 2026**, also aus diesem Monat), zeigt: der Effekt ist seit 2021 auf praktisch null gefallen. Ein realer Praxistest bestaetigt das: Die "NightShares"-ETFs (NSPY, NIWM), die genau diesen Effekt 2022 kommerzialisieren wollten, mussten nach 14 Monaten mangels Performance liquidiert werden. Das ist eines der saubersten "Beweis durch gescheitertes Produkt"-Ergebnisse, die man sich fuer eine Faktor-Anomalie wuenschen kann.

Ein zweiter, subtilerer Kandidat (cross-sektionale Overnight/Intraday-Zerlegung als Signal fuer Momentum/Reversal-Strategien) entgeht der "zweimal taeglich handeln"-Falle, weil er nicht auf taeglichem Round-Trip beruht, sondern die Overnight/Intraday-Aufteilung als Prognose-Signal fuer normal-frequente Portfolio-Rebalancings nutzt. Er ist aber schlecht kostenvalidiert und ueberlappt stark mit bekannten Faktoren — daher WEAK, nicht CANDIDATE.

**websuche_verfuegbar: ja.** Alle unten zitierten Quellen wurden per WebSearch/WebFetch in dieser Sitzung (Juli 2026) abgerufen; einige PDFs waren technisch nicht extrahierbar (korrupte Kodierung beim Fetch), dort wird auf Sekundaerquellen/Abstracts verwiesen und das entsprechend gekennzeichnet.

---

## Kandidat 1: Naiver Close-to-Open Overnight-Drift (Index/ETF/Futures)

### a) Oekonomische Begruendung

Der Mechanismus ist Marktmikrostruktur, nicht Fundamentaldaten:

- **Inventar-Aversion von Market-Makern**: Haendler/Dealer, die am Handelsschluss Netto-Verkaufsdruck absorbieren muessen, sitzen ueber Nacht auf einem Lagerbestand ("Inventory"), den sie nicht risikofrei absichern koennen. Sie verlangen dafuer eine Kompensation, die sich als positive Overnight-Rendite manifestiert (Boyarchenko/Larsen/Whelan 2020, NY Fed Staff Report 917: "The Overnight Drift").
- **Retail-Marktorders und Optionshedging**: Ein Grossteil der Retail-Kaeufe (Market-Orders, die ueber Nacht "geparkt" und zur Eroeffnung ausgefuehrt werden) sowie Delta-Hedging-Fluesse von Optionshaendlern konzentrieren sich um die Eroeffnung.
- **Informationsankunft ueber Nacht**: Ein grosser Teil relevanter Nachrichten (Earnings nach US-Handelsschluss, europaeische/asiatische Makrodaten, geopolitische Ereignisse) trifft ausserhalb der regulaeren US-Handelszeit ein und wird erst zur naechsten Eroeffnung eingepreist.
- **Konkreter Kanal identifiziert**: Boyarchenko et al. zeigen, dass fast die **gesamte** US-Aktienrisikopraemie in einem einzigen Zeitfenster von **2:00-3:00 Uhr ET** (Eroeffnung der europaeischen Boersen) anfaellt — im Sample 1998-2019/2020 durchschnittlich **~3.6-3.7% p.a.** annualisiert, bei einer Gesamt-Jahresrendite des Futures-Kontrakts von **~5.9%** (Close-to-Close) — also **>60% der Gesamtrendite in 1 von 24 Stunden**. Der Kanal ist eng an das Order-Ungleichgewicht ("Order Imbalance") zum vorherigen US-Handelsschluss gekoppelt und asymmetrisch: nach Ausverkaeufen ist die Overnight-Erholung stark positiv, nach Rallyes ist die Umkehr deutlich schwaecher.

### b) Limits to Arbitrage

Die strukturelle Erklaerung, warum ein Marktmacher-Kompensationseffekt nicht sofort wegarbitriert wird: Nur Akteure mit privilegiertem Zugang zu den Eroeffnungs-/Schlussauktionen (Designated Market Maker-Status, Maker-Rebates, Kolokation) koennen den Spread/die Kosten so weit druecken, dass ein struktureller Inventar-Risikoaufschlag als Ertrag uebrig bleibt. Fuer alle anderen Marktteilnehmer ist der Bruttoeffekt durch Spread und Slippage bereits mehr als aufgezehrt (siehe Punkt e). Das ist die klassische "Limits to Arbitrage"-Situation: der Effekt bleibt bestehen, weil nur eine kleine Gruppe (Market-Maker/HFT mit Rebates) ihn tatsaechlich netto vereinnahmen kann — fuer den Rest ist er ein Buchhaltungs-Artefakt der Renditezerlegung, kein handelbarer Gewinn.

### c) Originalstudien

- **Cooper, Cliff & Gulen (2008)**, "Return Differences between Trading and Non-Trading Hours: Like Night and Day" (SSRN Working Paper; spaeter u.a. als "Returns in Trading versus Non-Trading Hours: The Difference is Day and Night", Journal of Asset Management, 2011). Sample: S&P-500-Einzelwerte, ca. 1993-2006. Laut Sekundaerquellen (Originalpaper technisch nicht vollstaendig extrahierbar) liegt die durchschnittliche Overnight-Rendite bei ca. **+0.028% bis +0.048% pro Tag**, die Intraday-Rendite bei ca. **-0.028% bis +0.002% pro Tag** — die gesamte Aktienpraemie also faktisch ueber Nacht. Der Effekt ist robust ueber NYSE und Nasdaq, Einzelwerte, Indizes und Futures. Bemerkenswert und wichtig fuer die Robustheitsbewertung: Die eigenen Erklaerungsmodelle der Autoren (Liquiditaet, Bid-Ask-Bounce, Risikofaktoren) erklaeren laut zitierenden Sekundaerquellen nur **ca. 8-10% der Varianz** der Day/Night-Renditen — der Effekt ist also empirisch sehr robust, aber strukturell schlecht verstanden, was ihn anfaellig fuer Data-Mining-Kritik macht.
- **Boyarchenko, Larsen & Whelan (2020, rev. 2022)**, "The Overnight Drift", NY Fed Staff Report Nr. 917. Sample: US-Aktienindex-Futures, 1998-2019/2020 (5.691 Handelstage). Kernresultat: 2-3 Uhr ET-Fenster liefert ~3.6-3.7% p.a., >60% der Jahresrendite, statistisch und oekonomisch signifikant, robust an Inventar-Risiko-Modell gekoppelt.

### d) Out-of-Sample-/Post-Publication-Evidenz — der entscheidende Fund

Dies ist der wichtigste Befund dieser Recherche: **"The Disappearing Overnight Drift"**, Liberty Street Economics, **Juli 2026** (vermutlich dieselben/verwandte Fed-Autoren, direkte Fortsetzung von Staff Report 917). Es handelt sich um einen echten Post-Publication-Out-of-Sample-Test:

- Sample-Split: **1998-2020** (5.691 Tage, "in-sample"/Originalperiode) vs. **2021-2025** (1.245 Tage, "out-of-sample").
- Ergebnis: Das 2-3-Uhr-ET-Fenster, das 1998-2020 **~3.7% p.a.** brachte, lieferte 2021-2025 im Schnitt **~0%**.
- Ursachenzerlegung (Modell: Erwartete Overnight-Rendite ∝ Order-Ungleichgewicht × Renditevarianz / Risikotragfaehigkeit der Liquiditaetsanbieter):
  - **Order-Ungleichgewicht-Streuung** (Standardabweichung des signierten Handelsvolumens zum Schluss) fiel von **6.5% auf 2.9%** — eine Kompression um **~55%**. Dies ist laut den Autoren der **einzige** Kanal, der sich signifikant veraendert hat, und damit der Haupttreiber des Verschwindens.
  - Renditevarianz (VIX-Mittelwert 20.4 vs. 19.4) — praktisch unveraendert.
  - Risikotragfaehigkeit/Overnight-Volumenanteil (15% vs. 16%) — praktisch unveraendert.
  - Die Korrelation zwischen Schluss-Ungleichgewicht und Overnight-Rendite (das Kernprognose-Signal) hat sich drastisch abgeschwaecht.
- **Realer Praxistest**: NightShares brachte im Juni 2022 zwei ETFs (NSPY auf den S&P 500, NIWM auf den Russell 2000) auf den Markt, die explizit nur die Overnight-Rendite vereinnahmen wollten (Cash/Treasuries tagsueber, Aktienexposure nur over-night). Die Fonds wurden **im August 2023 nach nur ca. 14 Monaten liquidiert** — NSPY verwaltete nur $3.7 Mio., NIWM $1.4 Mio.; NSPY verlor **-6.9%** seit Auflage, waehrend der S&P 500 im selben Zeitraum **+22%** zulegte. Das ist ein selten sauberes Beispiel dafuer, dass eine akademisch dokumentierte Anomalie genau in dem Moment kommerzialisiert wurde, als sie bereits verschwunden war — ein Lehrbuchfall von Post-Publication-Decay.
- Internationale Evidenz: Der Overnight-Effekt wurde in Europa, Asien und Nordamerika repliziert (z.B. Hua & Sanhaji 2015 zur Tag/Nacht-Informationsuebertragung zwischen Boersenzeitzonen); die Staerke und Interpretierbarkeit variiert aber je nach Region — Studien zu China (z.B. "Overnight returns, daytime reversals: Is China different?") deuten auf abweichende Mechanismen hin, und eine Untersuchung zur internationalen Sentiment-Interpretation von Overnight-Renditen fand, dass Overnight-Rendite ausserhalb der USA **kein verlaesslicher Sentiment-Proxy** ist — ein Hinweis, dass der US-Mechanismus nicht 1:1 uebertragbar ist.
- Eine 2025 erschienene Studie ("Does Overnight News Explain Overnight Returns?", arXiv 2507.04481, S&P-500-Sample 1996-2022 mit 2.4 Mio. Nachrichtenartikeln) findet einen Overnight-Overhang von ca. **2.75 Basispunkten/Tag (~7.2% p.a.)**, der in der Teilperiode 2011-2022 qualitativ aehnlich bleibt — dies widerspricht dem obigen Fed-Befund fuer das enge 2-3-Uhr-Fenster nicht direkt (andere Definition/Fenster, andere Attribution: nachrichtengetrieben statt reines Inventar-Risiko), zeigt aber, dass **ein Teil** des Overnight-Overhangs bei Einzelwerten weiterhin messbar ist, sofern er auf vorhersagbare, nachrichtengetriebene Teilmengen von Aktien eingeschraenkt wird (wenn Aktien mit prognostizierten "guten" Overnight-News entfernt werden, verschwindet der Effekt laut dieser Studie weitgehend). Das ist eher ein Hinweis auf einen selektiven, informationsbasierten Rest-Effekt als auf einen weiterhin breit handelbaren Index-Overnight-Trade.

**Fazit d)**: Fuer den reinen, unselektiven Index-/Futures-Overnight-Trade ist die Post-Publication-Evidenz eindeutig negativ: Decay auf ~0% seit 2021, bestaetigt durch gescheiterten Produktlaunch.

### e) Kosten — die Kernfrage

Ein naiver Overnight-Trade bedeutet: Kauf zum Schluss, Verkauf zur Eroeffnung, **252 Round-Trips pro Jahr**, zusaetzlich zu jedem regulaeren Rebalancing.

- Bei einem sehr liquiden Instrument (SPY, ES-Futures) mit institutionellem Ein-Weg-Spread von grob 0.5-1 Basispunkt ergibt allein der Spread **252 × ~1-2 Basispunkte ≈ 2.5-5% p.a.** Kostenaufwand — bei einem Bruttoeffekt, der selbst historisch nur **~3.6-3.7% p.a.** betrug und seit 2021 bei ~0% liegt. Das Ergebnis ist strukturell negativ, nicht erst am Rande unprofitabel.
- Fuer die verwandte Einzelaktien-Version (Long-short-Overnight-minus-Intraday-Portfolio) zeigt eine ausfuehrliche Kostenanalyse (Elm Wealth, "Night Moves", 1995-2022, S&P-500-Sample): brutto **~38% p.a.** annualisierte Rendite bei sehr hohem Sharpe Ratio — aber: **1 Basispunkt Round-Trip-Kosten je Seite reduziert die Rendite bereits um ~5%/Jahr**; eine **1%ige Leihgebuehr fuer Shorts kostet weitere ~1%/Jahr**; Preisimpact von **~40 Basispunkten** beim Handel von 1% des Tagesvolumens in typischen Einzelwerten; historische (1990er) Kommissionen von 10 Basispunkten haetten die Strategie um **~100% p.a.** belastet; selbst bei modernen institutionellen Kommissionen von nur 1 Basispunkt wird die Profitabilitaet in den letzten Jahren eliminiert.
- Eine weitere zitierte Kostenanalyse (Alpha Architect, mit Bezug auf Barber & Odean 2001) verwendet realistischere Retail-Kosten von **~1% Spread + 1.4% Kommission pro Round-Trip** — bei diesen Annahmen ist die Strategie fuer Retail-Investoren komplett aussichtslos.
- Eine begleitende Beobachtung: An nur **~53% der Handelstage** (von rund 6.800 untersuchten Tagen in einer der zitierten Studien) war die Overnight-Rendite tatsaechlich hoeher als die Intraday-Rendite — der "Effekt" ist also stark von wenigen extremen Tagen/dem Verteilungs-Skew getrieben, nicht von einer konsistenten taeglichen Edge. Das erhoeht das Timing-/Ausfuehrungsrisiko realer Umsetzung zusaetzlich.

**Wer koennte trotzdem profitieren?** Ausschliesslich Marktmacher/HFT-Firmen mit (a) Maker-Rebates an den Eroeffnungs-/Schlussauktionen, (b) Kolokation und quasi-Null-Grenzkosten pro Order, und (c) der Faehigkeit, das Overnight-Exposure durch Auktions-Order-Flow-Internalisierung statt durch tatsaechliches Halten der Position zu vereinnahmen. Fuer einen institutionellen Fonds ohne Market-Maker-Status ist dieser Trade nicht profitabel handelbar — weder brutto (seit 2021 ohnehin ~0%) noch erst recht nicht netto.

### f) Kapazitaet und Handelbarkeit

Waere der Effekt intakt, waere die Kapazitaet sehr hoch (SPY/ES-Futures handeln taeglich zweistellige Milliardenbetraege, mechanisch einfach ueber MOC-/MOO-Orders umsetzbar). Das ist aber irrelevant, weil der Bruttoeffekt nicht mehr vorhanden ist. Handelbarkeit an sich (Orderausfuehrung) ist trivial — das Problem liegt nicht in der Umsetzung, sondern darin, dass es nichts mehr umzusetzen gibt.

### g) Regimeabhaengigkeit und Tail-Risiko

Der Overnight-Effekt ist stark regimeabhaengig und mit erheblichem, strukturell unkompensierbarem Tail-Risiko verbunden:

- Overnight-Gap-Risiko konzentriert sich in Krisenperioden: Im Maerz 2020 (COVID-Crash) oeffneten mehrere Handelstage mit Gaps von ueber 5% nach unten; **binnen 10 Tagen wurden viermal Level-1-Circuit-Breaker (7%-Schwelle) ausgeloest** (9., 12., 16., 18. Maerz 2020). 2022 (Zinserhoehungs-Baermarkt) traten wiederholt grosse Gap-downs bei Ausverkaeufen auf.
- Eine Studie zur systematischen Risikoveraenderung bei Marktschluss findet, dass die Sensitivitaet von US-Aktien gegenueber Marktschliessungen seit COVID-19 zugenommen hat.
- Dies bestaetigt direkt die in der Aufgabenstellung genannte Kernfalle: Ein Teil der historischen Overnight-Praemie ist schlicht **Kompensation fuer das Unvermoegen, bei einem Overnight-Schock auszusteigen** (keine Liquiditaet, moegliche Limit-up/Limit-down-Handelsunterbrechungen) — kein "freies" Alpha, sondern ein Risikoaufschlag fuer getragenes Gap-Risiko. Wer diesen Trade systematisch faehrt, sammelt in ruhigen Regimen kleine Praemien ein und ist in Tail-Events (Crash-Nacht) einem asymmetrischen Verlustrisiko ausgesetzt — ein klassisches "Picking up nickels in front of a steamroller"-Profil, zusaetzlich zur bereits negativen Kosten-Bruttoeffekt-Bilanz.

### h) Bekannte Kritik/Widerlegungen

- **Knuteson (2020)**, "Strikingly Suspicious Overnight and Intraday Returns" (arXiv 2010.01727 / SSRN 3705017): argumentiert, dass die Konsistenz des Musters (durchgehend positive Overnight-, durchgehend negative/neutrale Intraday-Renditen ueber Jahrzehnte) zu "sauber" sei, um sich zwanglos mit Standard-Risikokompensationsmodellen zu erklaeren, und postuliert als "einzig plausible Erklaerung" eine Art systematisches "Hold-and-Pump"-Verhalten grosser Akteure (eine eher fringe-artige, in der akademischen Mainstream-Literatur nicht breit akzeptierte manipulationsnahe These, die ~1 Mrd. USD Kapital voraussetzen wuerde). Unabhaengig davon, ob man dieser spezifischen These folgt, ist der Kernpunkt fuer unsere Bewertung wichtig: Selbst die Originalautoren (Cooper/Cliff/Gulen) koennen mit Standardmodellen nur 8-10% der Varianz erklaeren — das strukturelle Verstaendnis des Effekts war immer duenn, was Datamining-/Spezifikations-Kritik Tuer und Tor oeffnet.
- Die generelle Kostenkritik (Elm Wealth, Alpha Architect) ist selbst die schaerfste Waffe gegen die Strategie: mehrere unabhaengige Kostenanalysen kommen unabhaengig voneinander zum selben Schluss, dass realistische Handelskosten den Bruttoeffekt vollstaendig aufzehren.
- Die "Disappearing Overnight Drift"-Studie ist selbst die staerkste verfuegbare Widerlegung: Die Originalautoren des Overnight-Drift-Papers widerlegen faktisch ihren eigenen frueheren Befund fuer die Post-2020-Periode.

### Urteil: KILL

Der Effekt war real (starke oekonomische Fundierung durch Inventar-Risiko, robuste Replikation ueber Jahrzehnte und Maerkte), ist aber (1) seit 2021 auf ~0% dezimiert — bestaetigt durch die Originalautoren selbst und durch einen gescheiterten kommerziellen ETF-Launch — und war (2) selbst in seiner Bluetezeit nach realistischen Handelskosten fuer Nicht-Market-Maker kaum bis gar nicht profitabel. Beide von der Aufgabenstellung genannten Fallen (Kosten der zweimal-taeglich-Handelsfrequenz; Kompensation fuer nicht aussteigbares Overnight-Risiko) greifen hier voll.

---

## Kandidat 2: Cross-sektionaler Overnight/Intraday "Tug-of-War" als Prognosesignal

### a) Oekonomische Begruendung

Anders als Kandidat 1 geht es hier nicht um "kaufe Index zum Schluss, verkaufe zur Eroeffnung", sondern um eine **Renditezerlegung als Prognosesignal**: Man zerlegt die Rendite jeder Aktie in einen Overnight- und einen Intraday-Anteil und nutzt das Verhaeltnis/die relative Intensitaet dieser beiden Komponenten, um zukuenftige (normal-frequente, z.B. monatliche) Renditen vorherzusagen.

- **Lou, Polk & Skouras (2019)**, "A Tug of War: Overnight versus Intraday Expected Returns", Journal of Financial Economics 134(1), S. 192-213. Kernbefund ueber 14 untersuchte Handelsstrategien: Gewinne werden entweder fast vollstaendig ueber Nacht (Reversal- und diverse Momentum-Strategien) oder fast vollstaendig intraday erzielt — mit haeufig entgegengesetztem Vorzeichen der beiden Komponenten. Insbesondere wird praktisch das **gesamte Alpha von Momentum-Strategien ueber Nacht generiert** — konsistent mit institutionellem Trendfolgeverhalten (Fonds, die zur Eroeffnung in die Richtung des juengsten Trends handeln), waehrend Value-, Profitabilitaets- und Investment-Anomalien ihre Praemie tagsueber verdienen.
- Das "TugOfWar"-Signal (die geglaettete Differenz zwischen Overnight- und Intraday-Rendite-Komponente einer Strategie) **prognostiziert die zukuenftige Close-to-Close-Performance** dieser Strategie: eine Erhoehung um eine Standardabweichung entspricht ca. **+1% hoeherer Rendite im Folgemonat**, was rund **18% der monatlichen Renditevolatilitaet** der jeweiligen Strategie entspricht — ein oekonomisch relevanter, aber nicht extrem grosser Effekt.
- Momentum-Overnight-Renditen selbst zeigen einen **Reversal-Verlauf**: sie sind ueber die ersten ~12 Monate stark positiv, beginnen ab ca. Monat 18 umzukehren, und **nach 2 Jahren ist rund 30% des ursprnglichen Overnight-Momentum-Gewinns wieder verschwunden ("reverted")**.
- **Akbas, Boehmer, Jiang & Koch (2022)**, "Overnight returns, daytime reversals, and future stock returns", Journal of Financial Economics 145(3), S. 850-875, liefern eine unabhaengige, methodisch andere Bestaetigung: eine hoehere Intensitaet des taeglichen "Tug of War" (positive Overnight-Rendite gefolgt von negativer Intraday-Umkehr) sagt hoehere zukuenftige Renditen im Querschnitt voraus. Interpretation: Overnight-Kaeufer sind primaer Noise-Trader (Retail), waehrend Intraday-Arbitrageure am Folgetag tendenziell **ueberkorrigieren**, weil sie die Wahrscheinlichkeit echter positiver Nachrichten unterschaetzen — dies erzeugt eine handelbare Fehlbepreisung.

### b) Limits to Arbitrage

Die Erklaerung, warum dieser Effekt nicht wegarbitriert wird, liegt in der **Klientel-Heterogenitaet**: Retail-/Noise-Trader-Fluesse zur Eroeffnung sind strukturell (Verhaltens-bedingt, nicht durch einfache Arbitrage eliminierbar), waehrend die Arbitrageure, die tagsueber korrigieren, selbst begrenztem Kapital und Risikoaversion unterliegen und daher nicht vollstaendig korrigieren (klassisches Noise-Trader-Risiko a la DeLong/Shleifer/Summers/Waldmann). Da diese Fehlbepreisung sich erst mit Verzoegerung (naechster Monat) aufloest, ist sie fuer schnelle High-Frequency-Arbitrage schwerer zugaenglich als der reine Overnight-Spread-Kanal aus Kandidat 1.

### c) Originalstudien — Effektgroessen und Signifikanz

Siehe a) fuer Effektgroessen. Praezise t-Statistiken waren aus den verfuegbaren (teils technisch nicht extrahierbaren) PDF-Quellen nicht zuverlaessig zu extrahieren; die Abstracts/Sekundaerquellen berichten die Effekte durchgehend als "hoch signifikant" innerhalb des jeweiligen Papers, jedoch ohne dass diese Recherche die exakten t-Werte verifizieren konnte — das wird hier transparent als Evidenzluecke gekennzeichnet statt einer erfundenen Zahl.

### d) Out-of-Sample-/Post-Publication-Evidenz

- Die Akbas et al. (2022)-Studie ist selbst bereits eine Post-2019-Bestaetigung des grundlegenden Phaenomens (wenn auch mit anderer Modellierung/Mechanik, nicht als direkte Replikation derselben exakten Strategie).
- China-spezifische Studien (u.a. "Overnight momentum, informational shocks, and late informed trading in China"; "Overnight returns, daytime reversals, and future stock returns: Is China different?") deuten auf eine gewisse internationale Uebertragbarkeit hin, aber mit abweichenden Mechanismen (andere Marktstruktur, hoher Retail-Anteil in China).
- Die 2025er "Does Overnight News Explain Overnight Returns?"-Studie (arXiv 2507.04481, Sample bis 2022) unterstuetzt indirekt, dass Teile der Overnight/Intraday-Renditeaufteilung bei Einzelwerten bis mindestens 2022 messbar blieben, auch wenn dort primaer Nachrichtenflusstiming statt reines Tug-of-War-Momentum untersucht wird.
- Es wurde in dieser Recherche **keine dedizierte, direkte Out-of-Sample-Replikation exakt der Lou/Polk/Skouras-TugOfWar-Strategie fuer 2019-2026** gefunden. Die Post-Publication-Evidenz ist also indirekt/verwandt, nicht direkt — eine wichtige Einschraenkung.

### e) Kosten

Der entscheidende Vorteil gegenueber Kandidat 1: Diese Strategie erfordert **kein taegliches Round-Trip-Handeln derselben Position**. Das TugOfWar-Signal wird eher als **Timing-/Gewichtungsinput** fuer ohnehin monatlich (oder aehnlich) rebalancierte Momentum-/Reversal-Portfolios verwendet — die inkrementellen Transaktionskosten gegenueber einer bereits gehaltenen Momentum-Strategie sind also deutlich geringer als bei Kandidat 1. Allerdings: Keine der gefundenen Quellen liefert eine explizite, quantifizierte Netto-Kostenanalyse fuer diese spezifische Cross-Sektions-Strategie — eine der Suchergebnis-Quellen merkt explizit an, dass "die Kosten von Overnight-Strategien in aktuellen Arbeiten generell nicht quantifiziert werden". Das ist ein Warnsignal, kein Freibrief: unquantifizierte Kosten sind in der Quant-Praxis erfahrungsgemaess meist schlechter als erhofft, insbesondere weil die Strategie auf denselben Aktien wie klassisches Momentum aufsetzt, das selbst fuer hohe Turnover-Kosten bekannt ist.

### f) Kapazitaet und Handelbarkeit

Begrenzter als Kandidat 1: Die Strategie erfordert Positionen in einem breiten Aktien-Querschnitt (inkl. kleinerer, weniger liquider Namen, wo Overnight/Intraday-Verzerrungen typischerweise staerker sind), was Kapazitaet und Ausfuehrungskosten stark einschraenkt. Realistisch eher im Bereich niedriger bis mittlerer zweistelliger bis niedriger dreistelliger Millionenbetraege AUM, bevor Market Impact die Grenzrendite auffrisst — nicht auf Milliarden-Ebene skalierbar wie ein reiner Indexeffekt.

### g) Regimeabhaengigkeit und Tail-Risiko

Da die Strategie eng mit klassischem Momentum verwandt ist (das Overnight-Alpha momentumartiger Strategien ist der Kernbefund), erbt sie tendenziell das bekannte Tail-Risiko-Profil von Momentum: Crash-Risiko bei abrupten Markt-Umkehrungen ("Momentum Crashes", z.B. 2009, Maerz/April 2020), wo Overnight-Gap-Bewegungen die zugrunde liegende Positionierung besonders hart treffen koennen, weil Overnight-Exposure per Definition nicht intraday abgesichert werden kann.

### h) Bekannte Kritik/Widerlegungen

- Die generelle Kostenkritik an Overnight-Strategien (siehe Kandidat 1e) gilt grundsaetzlich auch hier, auch wenn in abgeschwaechter Form.
- Die enge mechanische Verwandtschaft zum klassischen Momentum-Faktor wirft die Frage auf, wie viel **inkrementelles** Alpha das TugOfWar-Signal tatsaechlich liefert, das nicht bereits durch Standard-Momentum-/Reversal-Faktor-Exposure erklaert wird — keine der gefundenen Quellen lieferte eine überzeugende Netto-von-bekannten-Faktoren-Attribution.

### Urteil: WEAK

Die oekonomische Fundierung (Noise-Trader/Arbitrageur-Klientel-Heterogenitaet) ist plausibler und weniger "schwarze Box" als bei Kandidat 1, und die Strategie umgeht geschickt die Zweimal-taeglich-Handelsfalle. Sie scheitert aber an der strikten Vorgabe "CANDIDATE nur bei dokumentierter Post-Publication-Evidenz UND Kostenrobustheit": Die Post-Publication-Evidenz ist nur indirekt/verwandt (keine direkte Replikation derselben Strategie 2019-2026 gefunden), und Kostenrobustheit ist in der Literatur explizit nicht quantifiziert. Beides zusammen mit der starken Ueberlappung zu bekanntem Momentum fuehrt zu WEAK statt CANDIDATE.

---

## Gesamtfazit fuer die Anomalieklasse "Overnight-Effekt"

1. **Der historisch beruehmteste Befund dieser Klasse — "die gesamte Aktienpraemie faellt ueber Nacht an" — ist als naiv handelbare Strategie tot.** Die eigenen Urheber der wichtigsten modernen Version (Boyarchenko/Larsen/Whelan) veroeffentlichten just in diesem Monat (Juli 2026) eine Fortsetzungsstudie, die den Zerfall des Effekts auf ~0% seit 2021 dokumentiert und mechanistisch erklaert (Kompression der Order-Ungleichgewicht-Streuung um 55%). Ein kommerzieller ETF-Versuch (NightShares, 2022-2023) bestaetigt dies als realen Praxis-Fehlschlag.
2. **Selbst wenn der Bruttoeffekt intakt waere**, zeigen mehrere unabhaengige Kostenanalysen, dass realistische Spread-/Impact-/Kommissionskosten bei 252 taeglichen Round-Trips den Bruttoeffekt komplett aufzehren — die von der Aufgabenstellung benannte Kernfalle greift hier lehrbuchartig.
3. **Ein Teil des historischen Effekts war ohnehin Risikokompensation, kein freies Alpha**: Overnight-Positionen koennen bei Gap-Events (COVID-Crash Maerz 2020, Circuit Breaker) nicht ausgestiegen werden — die zweite von der Aufgabenstellung benannte Kernfalle greift ebenfalls.
4. **Der subtilere, cross-sektionale Signalansatz (Tug-of-War als Momentum-Overlay)** entkommt der Handelsfrequenz-Falle, bleibt aber wegen unzureichend dokumentierter Kostenrobustheit und starker Faktor-Ueberlappung nur WEAK.
5. Insgesamt: **Diese Anomalieklasse sollte fuer ein institutionelles Portfolio nicht mit eigenstaendigem Kapital allokiert werden.** Ehrliches Ergebnis im Sinne der Aufgabenstellung: diese Klasse ist im Kern tot; das einzig verbliebene, schwach positive Signal ist ein Nebenprodukt-Overlay fuer ohnehin gehaltene Momentum-Strategien, nicht eine eigenstaendige Strategie.

---

## Quellen (per WebSearch/WebFetch abgerufen, Juli 2026)

- [Return Differences between Trading and Non-Trading Hours: Like Night and Day (Cooper, Cliff, Gulen, SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1004081)
- [Returns in Trading versus Non-Trading Hours: The Difference is Day and Night (ResearchGate)](https://www.researchgate.net/publication/233589349_Returns_in_Trading_versus_Non-Trading_Hours_The_Difference_is_Day_and_Night)
- [One Weird Regularity of the Stock Market: Intraday vs Overnight Returns (FastML)](https://fastml.com/one-weird-regularity-of-the-stock-market-intraday-vs-overnight-returns/)
- [A Tug of War: Overnight versus Intraday Expected Returns (Lou, Polk, Skouras, LSE)](https://personal.lse.ac.uk/polk/research/LouPolkSkouras.pdf)
- [A tug of war: Overnight versus intraday expected returns (ScienceDirect/JFE)](https://www.sciencedirect.com/science/article/abs/pii/S0304405X19300650)
- [A tug of war: overnight versus intraday expected returns (LSE Research Online)](https://researchonline.lse.ac.uk/id/eprint/87481/)
- [Overnight returns, daytime reversals, and future stock returns (Akbas, Boehmer, Jiang, Koch, JFE)](https://ideas.repec.org/a/eee/jfinec/v145y2022i3p850-875.html)
- [The Overnight Drift (Boyarchenko, Larsen, Whelan, NY Fed Staff Report 917)](https://www.newyorkfed.org/research/staff_reports/sr917)
- [The Overnight Drift in U.S. Equity Returns (Liberty Street Economics, 2021)](https://libertystreeteconomics.newyorkfed.org/2021/05/the-overnight-drift-in-us-equity-returns/)
- [The Disappearing Overnight Drift (Liberty Street Economics, Juli 2026)](https://libertystreeteconomics.newyorkfed.org/2026/07/the-disappearing-overnight-drift/)
- [Does Overnight News Explain Overnight Returns? (arXiv 2507.04481)](https://arxiv.org/pdf/2507.04481)
- [Night Moves: Is the Overnight Drift the Grandmother of All Market Anomalies? (Elm Wealth)](https://elmwealth.com/night-moves-overnight-drift/)
- [Night Moves (Advisor Perspectives Re-Publikation)](https://www.advisorperspectives.com/articles/2022/06/24/night-moves-is-the-overnight-drift-the-grandmother-of-all-market-anomalies)
- [Trading Costs Wipe Out the Overnight Return Anomaly (Alpha Architect)](https://alphaarchitect.com/2020/06/trading-costs-wipe-out-the-overnight-return-anomaly/)
- [2 NightShares ETFs Close After Struggling to Gain Traction (etf.com)](https://www.etf.com/sections/news/2-nightshares-etfs-close-after-struggling-gain-traction)
- ['Night Effect' ETFs to Shut Down With Overnight Stock Returns Elusive (WealthManagement.com)](https://www.wealthmanagement.com/etfs/-night-effect-etfs-to-shut-down-with-overnight-stock-returns-elusive)
- [Strikingly Suspicious Overnight and Intraday Returns (Knuteson, arXiv 2010.01727)](https://arxiv.org/abs/2010.01727)
- [Night trading: Lower risk but higher returns? (Lachance, 2023, Review of Financial Economics)](https://onlinelibrary.wiley.com/doi/full/10.1002/rfe.1180)
- [Can overnight return really serve as a proxy for firm-specific investor sentiment? Cross-country evidence (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1042443119304822)
- [Does systematic risk change when markets close? An analysis using stocks' beta (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0264999322000281)

## Methodische Anmerkung

Mehrere PDF-Originaldokumente (u.a. Lou/Polk/Skouras Volltext, Cooper/Cliff/Gulen SSRN, Knuteson arXiv) liessen sich technisch nicht sauber per WebFetch extrahieren (korrupte/binaere PDF-Kodierung im Fetch-Prozess) oder waren durch Paywalls (SSRN, Wiley) blockiert. In diesen Faellen wurde auf Abstracts, Sekundaerzitate und journalistische/praxisnahe Aufbereitungen (Elm Wealth, Alpha Architect, Liberty Street Economics) zurueckgegriffen, die die zentralen Zahlen konsistent wiedergeben. Wo Zahlen nur aus Sekundaerquellen stammen und nicht am Original verifiziert werden konnten, ist dies im Text explizit vermerkt ("laut Sekundaerquellen"). Keine Zahl wurde erfunden; wo praezise t-Statistiken nicht auffindbar waren, wurde dies als Evidenzluecke benannt statt eine Zahl zu approximieren.
