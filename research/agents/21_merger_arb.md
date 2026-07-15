```yaml
agent: 21
klasse: "Merger Arbitrage & Corporate Actions"
websuche_verfuegbar: ja
strategien:
  - name: "Cash-Merger-Arbitrage & Fixed-Price Tender Offers (Deal-Spread-Capture)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.25
    netto_sharpe_erwartung: "0.15-0.35 (systematisch, vor Fremdkapitalkostenschwankung)"
    kernrisiko: "Deal-Break-Klumpenrisiko korreliert mit Kredit-/Liquiditätskrisen (2008, 2020) und mit dem politischen Antitrust-Regime (2021-2024 vs. 2025-2026) - nicht diversifizierbares Makro-Tail-Risiko trotz Einzeldeal-Diversifikation"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "SEC EDGAR (8-K/DEFM14A-Ankündigungen, HSR-Fristen) + Yahoo Finance Kurse; kein Ken-French-Datensatz; Deal-Datenbanken (SDC Platinum/Refinitiv) kostenpflichtig"

  - name: "Stock-for-Stock Merger-Arbitrage (Exchange-Ratio-Arbitrage mit Akquirer-Short)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.2
    netto_sharpe_erwartung: "0.05-0.25"
    kernrisiko: "Leihkosten/Hard-to-Borrow auf Akquirer-Aktie, Recall-Risiko in Proxy-Saison, Repricing bei Exchange-Ratio-Änderungen; Short-Hedge selbst unter Stress (Squeeze) gefährdet"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "SEC EDGAR (S-4/DEFM14A fuer Exchange Ratios) + Yahoo Finance; Borrow-Fee-Daten nicht frei verfuegbar (groesste Datenluecke)"

  - name: "Ex-ante Deal-Risiko-Selektion / Completion-Probability-Overlay (Baker-Savasoglu-Faktor)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 1
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.1
    netto_sharpe_erwartung: "0.0-0.15 (inkrementell, kein eigenstaendiger Sharpe)"
    kernrisiko: "Kein eigenstaendiges Alpha - Signal (Deal-Groesse, Praemie, cash vs. stock, feindlich vs. freundlich) ist seit Jahrzehnten Marktstandard jedes Arb-Desks; echte Kante erfordert diskretionaere Rechts-/Regulierungseinschaetzung, nicht systematisch reproduzierbar"
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
```

# Agent 21 - Merger Arbitrage & sonstige Corporate Actions

**Evidenzbasis:** WebSearch/WebFetch waren in dieser Session verfuegbar und wurden genutzt (siehe Quellenliste am Ende). Einige Primaerquellen (z. B. HFRI-Rohdaten, Analysis-Group-PDF) waren nicht maschinenlesbar oder nur teilweise zugaenglich; entsprechende Luecken sind explizit als "internes Wissen / Sekundaerquelle" markiert.

## Nullhypothese und Kurzurteil

Merger-Arbitrage ist die vielleicht am besten erforschte "Alternative-Risk-Premium"-Strategie ueberhaupt - und genau deshalb ein Lehrbuchbeispiel dafuer, wie eine dokumentierte akademische Ineffizienz durch drei Jahrzehnte Kapitalzufluss zu einer schmalen, prozyklischen Versicherungspraemie zusammenschrumpft. Die Nullhypothese ("kein echtes Alpha") laesst sich fuer diese Klasse **nicht vollstaendig verwerfen, aber auch nicht vollstaendig bestaetigen**: Es gibt einen realen, robust nachweisbaren Excess-Return, der jedoch (a) ganz ueberwiegend Kompensation fuer nicht-diversifizierbares Tail-Risiko ist, (b) seit den Originalstudien um schaetzungsweise 35-70% (gross) geschrumpft ist, und (c) in der einzigen mir bekannten voll systematischen, investierbaren Umsetzung (IQ Merger Arbitrage ETF, "MNA") ueber die Lebensdauer des Fonds auf ein Niveau nahe Cash-Rendite gefallen ist. Das ist das Gegenteil eines "toten" Feldes - es ist ein **lebendiges, aber strukturell kompensiertes Risiko**, kein Free Lunch.

## Kandidat 1: Cash-Merger-Arbitrage & Fixed-Price Tender Offers

### a) Oekonomische Begruendung - wer verkauft unter dem Angebotspreis?

Nach Ankaendigung eines Cash-Deals springt der Zielaktienkurs typisch auf 90-98% des Angebotspreises; die Restluecke ("Deal-Spread") ist die Pramie fuer das verbleibende Risiko (Nicht-Zustandekommen, Zeitwert bis Closing, Finanzierungsrisiko). Verkaeufer unter dem fairen, risikoadjustierten Wert sind typischerweise:

- **Mandatsgebundene Halter**: Index- und Growth-/Quality-Fonds, die den Titel aus Benchmark-/Stilgruenden nicht mehr halten duerfen oder wollen, sobald er zu einer "Merger-Arb-Situation" mit event-getriebenem Risikoprofil wird (Rebalancing-Zwang, nicht Bewertungsurteil).
- **Ungeduldige/risikoaverse Long-Halter**: Sie ziehen einen sicheren, sofortigen Gewinn einem unsicheren, erst in 3-12 Monaten realisierten Gewinn vor (Diskontierung + Ambiguitaetsaversion), obwohl der erwartete Wert des Wartens hoeher waere.
- **Strukturelle Nichtteilnehmer**: Anleger ohne Leerverkaufs-/Derivateinfrastruktur, die Stock-Deals gar nicht halten koennen, sowie Halter, die aus Diversifikationsgruenden Klumpenrisiko in einem Einzeltitel abbauen wollen.

Auf der Kaeuferseite steht eine **strukturell kapitalbeschraenkte Gruppe von Arbitrageuren** (Baker & Savasoglu 2002 nennen sie explizit "thinly capitalized" bzw. Investoren mit begrenzter Risikotragfaehigkeit). Das ist der Kern der oekonomischen Geschichte: kein permanenter Bewertungsfehler des Marktes, sondern ein **Marktsegmentierungsmodell** - eine kleine Gruppe spezialisierter Kapitalgeber muss idiosynkratisches Abbruchrisiko absorbieren, das der breite Markt nicht tragen will/kann, und wird dafuer entlohnt.

### b) Limits to Arbitrage

- **Deal-Break-Klumpenrisiko**: Einzelne Deals sind fuer sich genommen idiosynkratisch, aber in Stressphasen brechen mehrere Deals gleichzeitig (Finanzierungsaustrocknung, generelle Risikoaversion) - das Portfolio ist scheinbar diversifiziert ueber viele unkorrelierte "Wetten", verhaelt sich in Krisen aber wie eine einzige grosse Short-Vola-Position.
- **Antitrust-/Regulierungsrisiko**: Nicht laenger rein idiosynkratisch, sondern **regimeabhaengig und damit korreliert**: Die politische Grosswetterlage der US-Kartellbehoerden (FTC/DOJ) und der EU-Kommission/UK-CMA verschiebt sich zwischen Administrationen und trifft dann viele Deals gleichzeitig.
- **Finanzierungsrisiko fuer den Kaeufer**: LBO-finanzierte Deals haengen von der Verfuegbarkeit von Fremdkapital ab; Kreditmarkt-Stress killt Deals unabhaengig vom strategischen Rational.
- **Kapitalbeschraenkung der Arbitrageure selbst**: Mitchell & Pulvino (2012, "Arbitrage Crashes and the Speed of Capital", JFE 104(3), 469-490) zeigen, dass waehrend der Finanzkrise 2008 nahezu identische Wertpapiere um bis zu 10% fehlbewertet blieben, weil Prime-Broker-Finanzierung fuer Hedgefonds abrupt schrumpfte - die Arbitrageure konnten die Spreads nicht schliessen, weil ihnen selbst das Kapital ausging (prozyklisch genau dann, wenn die Opportunity am groessten war).

### c) Originalstudien

**Mitchell & Pulvino (2001), "Characteristics of Risk and Return in Risk Arbitrage", Journal of Finance 56(6), 2135-2175.**
Stichprobe: 4.750 Fusionen/Uebernahmen, 1963-1998 (grosser Sample-Umfang ueber 35 Jahre). Kernresultat: Nach Transaktionskosten generiert Risk Arbitrage einen Excess Return von **ca. 4% p.a.** Wichtigstes Risikoresultat: Die Renditen korrelieren **positiv mit dem Aktienmarkt nur in stark fallenden Maerkten**, sind aber in seitwaerts/steigenden Maerkten praktisch unkorreliert - ein Payoff-Profil analog zum **Verkauf ungedeckter Index-Putoptionen**. Das ist die zentrale Risikoerklaerung der ganzen Anomalieklasse: eine schiefe (negativ skewed), konvexe Downside-Exponierung, die in normalen Zeiten wie "freies Alpha" aussieht, aber strukturell Versicherungspraemie ist.

**Baker & Savasoglu (2002), "Limited Arbitrage in Mergers and Acquisitions", Journal of Financial Economics 64(1), 91-115.**
Stichprobe: 1.901 Uebernahmeangebote, 1981-1996. Kernresultat: Ein diversifiziertes Risk-Arbitrage-Portfolio erzielt einen abnormalen Return von **0,6-0,9% pro Monat** (annualisiert ca. **9,36% p.a.**, vor Transaktionskosten). Das theoretische Kernmodell: Arbitrageure sind kapazitaetsbeschraenkt durch Abbruchrisiko und Positionsgroesse; die erwartete Rendite steigt **in einem ex-ante Mass fuer Abbruchrisiko und in der Zielgroesse**. Explizite Interpretation der Autoren: Merger-Aktien werden von einer kleinen Gruppe duennkapitalisierter Investoren gepreist, die Angebotsschocks absorbieren - das ist explizit ein **Risikopraemien-Modell**, keine reine Behavioral-Ineffizienz-These.

### d) Out-of-Sample-/Post-Publication-Evidenz (Decay)

- **Jetley & Ji (2010), "The Shrinking Merger Arbitrage Spread: Reasons and Implications", Financial Analysts Journal 66(2), 54-68.** Stichprobe: 2.182 US-Deals, 1990-2007. Ergebnis: Der Tag-1-Median-Spread ist seit 2002 um **ueber 400 Basispunkte** gesunken - "economically and statistically significant". Der mediane monatliche Hedgefonds-Return sank von **0,96% (1990-1995)** auf **0,51% (2002-2007)** - ein **Rueckgang von rund 47% im monatlichen Bruttoertrag**. Als Ursache identifizieren die Autoren Kapitalzufluss/Crowding: Das Verhaeltnis von Arb-Kapital (Angebot an Liquiditaet) zu aggregiertem Dealvolumen (Nachfrage) ist der Haupttreiber des Spread-Niveaus - klassische Crowding-Signatur.
- **IQ Merger Arbitrage ETF (Ticker MNA)**, aufgelegt November 2009, regelbasiert/systematisch, liquide, taeglich handelbar. Durchschnittliche annualisierte Rendite seit Auflegung: **rund 2,71% p.a.** ueber gut anderthalb Jahrzehnte inkl. der Nullzins-Dekade 2009-2021. Das ist die staerkste verfuegbare **Live-Evidenz fuer einen systematischen (nicht-diskretionaeren) Ansatz**: eine voll investierbare, kostentransparente Umsetzung liefert ueber den Zyklus eine Rendite, die grossteils der Cash-Verzinsung der Periode entspricht - fast keine nachweisbare Ueberrendite fuer einen regelbasierten Nachbau, sobald Fondskosten (ca. 75 Bp Expense Ratio), Slippage und Leihkosten realistisch eingepreist sind.
- **Antitrust-Aera 2021-2024**: DOJ/FTC klagten 2022 gegen **10 Deals** (Rekordwert seit Beginn der Dechert-Erhebung 2011) gegenueber 6 in 2021; **60% der signifikanten 2022er Pruefverfahren** endeten mit Blockade oder Abbruch. Konkrete Deal-Breaks in diesem Fenster:
  - **Adobe/Figma** ($20 Mrd., angekuendigt Sept. 2022): am 18. Dez. 2023 einvernehmlich abgebrochen, da "kein klarer Pfad" zur EU-/UK-CMA-Freigabe gesehen wurde. Adobe zahlte eine Reverse-Termination-Fee von **1 Mrd. USD** an Figma und trug zusaetzlich **97,9 Mio. USD** eigene Transaktionskosten.
  - **JetBlue/Spirit Airlines** ($3,8 Mrd.): Bundesrichter erliess im Januar 2024 eine dauerhafte Verfuegung gegen den Deal; Vertrag am 4. Maerz 2024 einvernehmlich beendet. JetBlue zahlte 69 Mio. USD an Spirit; JetBlues Nettoverlust stieg im Jahresvergleich um **524 Mio. USD**, primaer durch Abschreibung Spirit-bezogener Kosten.
  - **Penguin Random House/Simon & Schuster** ($2,2 Mrd.): am 31. Okt. 2022 gerichtlich blockiert, danach abgebrochen.
  - Microsoft/Activision ueberlebte zwar eine FTC-Klage (Juli 2023 abgelehnte einstweilige Verfuegung), aber die verlaengerte regulatorische Unsicherheit reduzierte die annualisierte IRR der Position ueber die Haltedauer erheblich (Zeitwert-Erosion trotz letztlich erfolgreichem Closing).
- **Regimewechsel 2025-2026**: Unter der Trump-Administration wurde die Fusionskontrolle spuerbar deregulierungsfreundlicher (mehr Vergleiche statt Litigation, z. B. HPE/Juniper Networks $14 Mrd. per Settlement statt Klage; schnellere HSR-Fristablaeufe). Ergebnis: Der HFRI Event Driven: Merger Arbitrage Index stieg **+8,2% in den ersten drei Quartalen 2025** - der staerkste 9-Monats-Start seit 2021 und der zweitstaerkste seit 2009. Goldman Sachs bezifferte im August 2025 den medianen annualisierten US-Spread auf **7,7%** (nur angekuendigte Deals), nach kurzzeitiger Ausweitung waehrend des Zoll-bedingten Stresses im April 2025.
- **Decay-Schaetzung (grob, gross vor Kosten)**: BS2002 (~9,36% p.a., 1981-96) -> Jetley/Ji (~6,1% p.a. aequivalent, 2002-07) entspricht einem Rueckgang von **rund 35%**; gegen die volle Kostenrealitaet eines systematischen ETF-Nachbaus (MNA, ~2,7% p.a. ueber 2009-2025+, groesstenteils Nullzinsjahre) entspricht das einer **Erosion von 70-100% der urspruenglichen Bruttopraemie** auf Netto-Cash-Niveau. Die Erholung 2025/26 zeigt jedoch, dass das Regime (Regulierungszyklus, Zinsniveau) den grossen Teil der Varianz erklaert, nicht ein linearer, permanenter Zerfall.

### e) Kosten und Umsetzbarkeit fuer einen systematischen Ansatz

- Eintritts-Slippage direkt nach Ankuendigung (oft duenne Liquiditaet, grosse Kursspruenge) und Exit-Gap-Risiko bei Abbruch (Rueckfall des Zielkurses typischerweise -15% bis -40% Richtung Vor-Ankuendigungsniveau).
- Notwendiges Monitoring von HSR-Fristen, EU-/UK-Fusionskontroll-Kalendern und Vertragsdetails (Termination-Fee-Struktur, MAC-Klauseln) - ein rein regelbasiertes System kann Standardfristen abbilden, aber die Einschaetzung der tatsaechlichen Abbruchwahrscheinlichkeit (das eigentliche Alpha bei Baker & Savasoglu) ist im Kern eine **juristisch-diskretionaere Einschaetzung**, die ein nicht-diskretionaeres System kaum reproduziert.
- Leverage (typisch 2-4x) ist noetig, um aus kleinen Spreads attraktive Renditen zu machen - die Finanzierungskosten dieses Hebels sind selbst prozyklisch und steigen/verschwinden (Prime-Broker-Deleveraging) genau dann, wenn Spreads ohnehin auseinanderlaufen (siehe Mitchell/Pulvino 2012).
- Steuerliche Behandlung (kurzfristige Halteperioden, in den meisten Jurisdiktionen kein Vorzugssatz) reduziert die Netto-Attraktivitaet zusaetzlich gegenueber Buy-and-Hold-Anomalien.

### f) Kapazitaet und Handelbarkeit

Das jaehrliche global angekuendigte M&A-Volumen liegt im Bereich mehrerer Billionen USD, aber das zu jedem Zeitpunkt **investierbare Spread-Kapital-Universum** ist deutlich kleiner. Bekannte dedizierte Vehikel: The Merger Fund (MERFX, ~3,9 Mrd. USD AUM), AQR Diversified Arbitrage (ADAIX, ~1,7 Mrd. USD), IQ Merger Arbitrage ETF (MNA, ~460 Mio. USD) plus diverse Multi-Strategy-Buecher (Paulson & Co., Farallon, Davidson Kempner u. a.). Insgesamt eine **Nische im niedrigen zweistelligen Milliardenbereich** innerhalb einer ~4-5 Billionen USD grossen Hedgefonds-Industrie. Das Verhaeltnis von Arb-Kapital-Angebot zu Deal-Nachfrage ist laut Literatur der Haupttreiber des Spread-Niveaus - zusaetzliches systematisches Kapital wuerde die Spreads tendenziell **selbstlimitierend weiter komprimieren**.

### g) Regimeabhaengigkeit und Tail-Risiko

- Bestaetigt **negativ skewed**: viele kleine positive Monate, gelegentliche grosse Verlust-Events bei Deal-Break.
- Mitchell & Pulvino (2001): Korrelation zum Aktienmarkt ist nahe null in normalen/guten Maerkten, steigt aber stark in schwer fallenden Maerkten - Payoff-Profil wie ein geschriebener Put auf systemische Liquiditaetskrisen.
- 2008: Prime-Broker-Deleveraging fuehrte zu Spread-Ausweitungen und bis zu 10% Fehlbewertung nahezu identischer Wertpapiere (Mitchell/Pulvino 2012).
- 2020 (COVID): Tiffany/LVMH-Spread weitete sich von 5% auf 18%, bevor der Deal im Oktober 2020 zu einem reduzierten Preis (135 -> 131,50 USD/Aktie) neu verhandelt statt gebrochen wurde - zeigt, dass Krisenrisiko nicht nur binaeres Scheitern, sondern auch Repricing-Risiko umfasst.
- 2021-2024: Ein **neues, systematisches Regulierungsrisiko** (Biden-Administration) traf viele Deals gleichzeitig - nicht mehr rein idiosynkratisch, sondern ein politischer Faktor, der 2025/26 unter der Folgeadministration wieder verschwand. Das bestaetigt empirisch, dass "Antitrust-Risiko" eher ein **Makro-/Politik-Faktor mit Regimewechseln** ist als ein durch Diversifikation wegmittelbares Idiosynkrasierisiko.

### h) Bekannte Kritik/Widerlegungen

- Die Originalautoren selbst (Baker & Savasoglu) interpretieren den Effekt explizit als **Risikopraemie fuer kapitalbeschraenkte Arbitrageure**, nicht als Marktineffizienz im Sinne von "billigem Geld auf der Strasse".
- CAIA-Kommentar "Merger Arbitrage: Arbitraged Away?" sowie Jetley/Ji argumentieren fuer strukturelle Spread-Kompression durch Kapitalzufluss ueber Jahrzehnte - klassisches Crowding-Signatur, konsistent mit "die Praemie wurde re-priced, nicht dass sie nie existierte".
- Die MNA-ETF-Realrendite (~2,7% p.a. seit 2009) ist selbst die staerkste Widerlegung eines "einfachen systematischen Alpha": Eine voll transparente, kostenguenstige, regelbasierte Umsetzung liefert ueber anderthalb Jahrzehnte im Wesentlichen Cash-aehnliche Rendite mit gelegentlichem Crash-Tail - exakt die Signatur einer fair bepreisten Versicherungspraemie, nicht einer Ineffizienz.

**Urteil: WEAK.** Die Klasse ist nicht tot (2025/26-Erholung, jahrzehntelange Robustheit des Grundmechanismus), aber fuer einen systematischen, nicht-diskretionaeren Ansatz ist die Netto-Ueberrendite nach realistischen Kosten duenn, stark regimeabhaengig (Antitrust-Zyklus, Zinsniveau, Kreditmarktstress) und die Tail-Risiken sind exakt dann am groessten, wenn Diversifikationsvorteile im Gesamtportfolio am wichtigsten waeren. Einordnung: **ueberwiegend Risikopraemie (Versicherung gegen Deal-Break/Liquiditaetskrisen), kein robustes systematisches Alpha.**

## Kandidat 2: Stock-for-Stock Merger-Arbitrage (Exchange-Ratio-Arbitrage)

### a-d) Kurzfassung (gleiche Grundmechanik wie Kandidat 1)

Oekonomisch identischer Verkaeufer-Mechanismus wie bei Cash-Deals, zusaetzlich verstaerkt durch Investoren, die aus Mandatsgruenden **keine Aktien des Akquirers halten koennen/wollen** (z. B. weil dieser aus einem anderen Sektor/Index stammt) und daher sofort verkaufen, statt die implizite Aktienposition zu halten. Die Strategie kauft die Zielaktie und verkauft den Akquirer im Exchange Ratio leer, um die Spread-Konvergenz marktneutral zu vereinnahmen. Empirisch in denselben Studien (MP2001, BS2002) enthalten, mit tendenziell aehnlichen, teils etwas hoeheren Bruttorenditen wegen zusaetzlicher Risikopraemie fuer das Akquirer-Beta-Exposure, das nicht perfekt hedgebar ist.

### e) Zusaetzliche Kosten/Limits gegenueber Kandidat 1

- **Leihkosten (Borrow Fee)** fuer die Akquirer-Short-Position koennen insbesondere bei kleineren/spekulativen Akquirern erheblich sein und einen relevanten Teil des Spreads auffressen; diese Daten sind zudem **nicht frei verfuegbar** (groesste Datenluecke fuer eine unabhaengige Nachbildung).
- **Recall-Risiko** (Aktien werden waehrend der Hauptversammlungssaison zurueckgerufen) kann die Hedge-Position zum ungewuenschten Zeitpunkt zwingen zu schliessen.
- **Repricing-Risiko**: Aendert sich das Exchange Ratio waehrend der Verhandlung (haeufiger als bei Cash-Deals, da beide Boersenkurse schwanken), muss die Hedge-Ratio laufend nachjustiert werden - operationell aufwendiger und fehleranfaelliger fuer ein rein systematisches System.
- In Stressphasen (2008, 2020) kann die Short-Seite selbst zum Risiko werden (Squeeze-Gefahr, Leihkosten-Spikes, Shortsell-Bans in einzelnen Jurisdiktionen wurden 2008 und 2020 zeitweise verhaengt und trafen Finanzwerte, die haeufig Akquirer in Bankfusionen waren).

### f-h) Kapazitaet, Regime, Kritik

Kapazitaet und Regimeabhaengigkeit sind im Kern identisch zu Kandidat 1 (gleiche Deal-Population, teils Ueberschneidung), aber die zusaetzliche Kostenschicht (Leihe, Squeeze-Risiko) macht die Strategie fuer eine rein systematische, nicht-diskretionaere Umsetzung **strukturell unterlegen** gegenueber der Cash-Variante. Ein wesentlicher Teil der oeffentlich zugaenglichen akademischen Evidenz (MP2001, BS2002) mischt beide Deal-Typen, ohne die Netto-Leihkosten separat und realistisch auszuweisen - das ist eine bekannte Schwachstelle der Originalstudien, die die tatsaechliche Netto-Rendite dieser Variante eher ueberschaetzt haben duerften.

**Urteil: WEAK, an der Grenze zu KILL.** Gleiche Grundpraemie wie Kandidat 1, aber durch Leihkosten/Squeeze-Risiko zusaetzlich geschwaecht und schwerer aus frei verfuegbaren Daten sauber zu reproduzieren (Borrow-Fee-Daten fehlen).

## Kandidat 3: Ex-ante Deal-Risiko-Selektion / Completion-Probability-Overlay

Baker & Savasoglu (2002) zeigen, dass die erwartete Rendite in ex-ante messbarem Abbruchrisiko und Zielgroesse steigt - theoretisch liesse sich daraus ein Overlay ableiten, das Positionen nach geschaetzter Completion-Probability gewichtet (grosse Deals, hohe Praemie, feindliche vs. freundliche Uebernahme, Cash vs. Stock, Sektor-Antitrust-Historie als Inputs).

**Warum das keine eigenstaendige, systematisch handelbare Strategie ist:**
- Das Signal ist **kein Geheimnis** - Deal-Groesse, Praemienhoehe und Cash/Stock-Struktur sind seit Jahrzehnten Standardkriterien jedes professionellen Arb-Desks; es handelt sich nicht um eine unentdeckte Ineffizienz, sondern um eine seit BS2002 (1996 endender Sample-Zeitraum, seit fast 30 Jahren publiziert) vollstaendig in die Preisbildung eingepreiste Erklaerungsvariable.
- Die **wirkliche** Kante bei der Einschaetzung von Abbruchwahrscheinlichkeit liegt heute in juristischer/regulatorischer Analyse (Einschaetzung von Kartellrechtsverfahren, Vergleichsbereitschaft der Behoerden, politischem Klima) - genau die Faehigkeit, die diskretionaere Spezialisten (ehemalige Kartellrechtsanwaelte, Regulierungsanalysten) bei Fonds wie Paulson oder Farallon einbringen, und die sich nicht in ein "nicht-diskretionaeres" quantitatives Regelwerk uebersetzen laesst, ohne den eigentlichen Vorteil zu verlieren.
- Es ist zudem keine eigenstaendig handelbare Strategie, sondern nur eine Gewichtungsregel **innerhalb** von Kandidat 1/2 - daher auch kein separater Kapazitaets- oder Kostenblock zu bewerten.

**Urteil: KILL** (als eigenstaendiger systematischer Strategiekandidat; als Risiko-Gewichtungsregel innerhalb eines diskretionaeren Merger-Arb-Buchs weiterhin sinnvoll, aber das ist ausserhalb des hier zu bewertenden Mandats fuer einen systematischen Ansatz).

## Fazit fuer die Anomalieklasse

Merger Arbitrage ist die Klasse mit der wohl saubersten akademischen "Risikopraemie vs. Ineffizienz"-Antwort im gesamten Anomalie-Zoo: **Beides trifft in Teilen zu, aber das Risikopraemien-Element dominiert eindeutig.** Es gibt einen kleinen, robusten, seit 60+ Jahren replizierbaren Mechanismus (mandatsgetriebene, ungeduldige Verkaeufer treffen auf kapitalbeschraenkte Arbitrageure), der eine reale Praemie generiert hat. Diese Praemie ist jedoch:

1. **Ueber Dekaden geschrumpft** (Spread-Kompression >400 Bp seit 2002, Bruttoreturn-Rueckgang ca. 35-50% zwischen BS2002 und Jetley/Ji 2010),
2. **In der voll systematischen, investierbaren Umsetzung nahe Cash-Niveau angekommen** (MNA-ETF ~2,7% p.a. seit 2009), und
3. **Stark regimeabhaengig** - schlechte Jahre fallen fast immer mit systemischen Liquiditaetskrisen (2008, 2020) oder aggressiven Antitrust-Zyklen (2021-2024) zusammen, waehrend gute Jahre (2025/26) mit deregulierungsfreundlichem Klima und hohem Zinsniveau (attraktiverer Cash-Ersatz-Charakter des Spreads) zusammenfallen.

Fuer einen **institutionellen Fonds mit Fokus auf systematisches (nicht diskretionaeres) Alpha** ist der ehrliche Befund: Diese Klasse liefert primaer eine **Diversifikations- und Carry-Komponente mit Put-artigem Tail-Risiko**, kein eigenstaendiges, kostenrobustes Alpha. Ein Einsatz waere allenfalls als kleine, stark risikobudgetierte Beimischung mit explizitem Bewusstsein fuer die negative Schiefe und die Korrelation zu Kredit-/Liquiditaetsstress zu rechtfertigen - nicht als Kernstrategie. Die Klasse ist damit **nicht tot, aber auch kein Alpha-Fund** - ein ehrliches "die grosse Praemie ist arbitriert, ein kleiner Risikoaufschlag bleibt" ist das wertvollere Ergebnis gegenueber einem uebertriebenen CANDIDATE-Urteil.

## Quellen (Web-Recherche Juli 2026)

- [Characteristics of Risk and Return in Risk Arbitrage - Mitchell & Pulvino (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=268144)
- [Characteristics of Risk and Return in Risk Arbitrage (Wiley/JoF)](https://onlinelibrary.wiley.com/doi/abs/10.1111/0022-1082.00401)
- [Limited Arbitrage in Mergers and Acquisitions - Baker & Savasoglu (HBS PDF)](https://www.hbs.edu/faculty/Pages/download.aspx?name=arbitrage.pdf)
- [Limited Arbitrage in Mergers and Acquisitions (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=315639)
- [The Shrinking Merger Arbitrage Spread - Jetley & Ji (Return Stacked Review)](https://www.returnstacked.com/academic-review/the-shrinking-merger-arbitrage-spread-reasons-and-implications/)
- [The Shrinking Merger Arbitrage Spread (Tandfonline/FAJ)](https://www.tandfonline.com/doi/abs/10.2469/faj.v66.n2.3)
- [Arbitrage Crashes and the Speed of Capital - Mitchell & Pulvino (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1628261)
- [Arbitrage crashes and the speed of capital (ScienceDirect/JFE)](https://www.sciencedirect.com/science/article/abs/pii/S0304405X11001991)
- [MNA - IQ Merger Arbitrage ETF: Performance & Analysis (PortfoliosLab)](https://portfolioslab.com/symbol/MNA)
- [Merger Arbitrage: Riding the Wave Into 2026 (AllianceBernstein)](https://www.alliancebernstein.com/americas/en/institutions/insights/investment-insights/merger-arbitrage-riding-the-wave-into-2026.html)
- [Merger Arbitrage - Return Stacked Portfolio Solutions](https://www.returnstacked.com/merger-arbitrage/)
- [What Is The Average Merger Arbitrage Spread? (Event Driven Daily)](https://www.eventdrivendaily.com/what-is-the-average-merger-arbitrage-spread/)
- [Termination of Adobe / Figma Merger (Gibson Dunn)](https://www.gibsondunn.com/termination-of-adobe-figma-merger/)
- [Adobe and Figma cancel acquisition deal over antitrust issues (Morning Brew)](https://www.morningbrew.com/stories/2023/12/19/-adobe-and-figma-call-it-quits)
- [JetBlue, Spirit end $3.8 billion merger agreement after losing antitrust suit (CNBC)](https://www.cnbc.com/2024/03/04/jetblue-spirit-airlines-merger-called-off.html)
- [JetBlue and Spirit abandon the decision to merge after it was blocked by a judge (NPR)](https://www.npr.org/2024/03/05/1235909629/jetblue-spirit-airlines-merger)
- [Biden antitrust enforcers block deals at record pace (CFO Dive)](https://www.cfodive.com/news/biden-antitrust-enforcers-block-deals-record-pace/641796/)
- [M&A Enforcement Easing Under The Trump Administration (Forbes)](https://www.forbes.com/sites/aldenabbott/2025/07/16/ma-enforcement-easing-under-the-trump-administration/)
- [FTC and DOJ Shift Merger Review Toward Settlements (National Law Review)](https://natlawreview.com/article/takeaways-dealmakers-us-antitrust-merger-enforcement-trends)
- [LVMH and Tiffany Merger: the reality of Covid-19 deals (The Student Lawyer)](https://thestudentlawyer.com/2020/07/08/lvmh-and-tiffany-merger-the-reality-of-covid-19-deals/)
- [Merger Arbitrage: Arbitraged Away? (CAIA) - abgerufen, HTTP 403 bei Volltextabruf, nur Titel/Kontext verwertbar](https://caia.org/blog/2020/04/30/merger-arbitrage-arbitraged-away)
