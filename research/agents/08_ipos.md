```yaml
agent: 08
klasse: "IPOs"
websuche_verfuegbar: ja
strategien:
  - name: "IPO-Underpricing / Erstzeichnungsrendite (Winner's-Curse-Rente)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 2
      regimestabilitaet: 3
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.85
    netto_sharpe_erwartung: "0.2-0.5 NUR bei systematischem Zuteilungszugang (Prime-Broker/Underwriter-Beziehung); ~0 ohne Zugang"
    kernrisiko: "Kein Marktzugang zu Zuteilungen für Outsider (Rock 1986 Winner's Curse); Effekt ist eine Zuteilungs-/Beziehungsrente für bevorzugte institutionelle Kunden, keine im offenen Markt handelbare Ineffizienz"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Jay-Ritter-IPO-Dataset (Underpricing-Tabellen), site.warrington.ufl.edu/ritter/ipo-data"
  - name: "Langfristige IPO-Underperformance / 'New Issues Puzzle'"
    urteil: KILL
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.2
    netto_sharpe_erwartung: "0.0-0.1, nach Faktorkontrolle nicht von generischem Size-/Quality-/Junk-Exposure unterscheidbar"
    kernrisiko: "Effekt kehrt sich um bzw. verschwindet fast vollständig, wenn ab Erstausgabepreis statt Erstschlusskurs gemessen wird, und wenn für Size/B-M/Quality-Minus-Junk kontrolliert wird (Brav & Gompers 1997; Carter, Dark & Sapp 2011; Asness et al. QMJ). Kein eigenständiger Anomalie-Kern übrig."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Jay-Ritter Long-run-Return-Tabellen + Ken-French-Data-Library (SMB, HML, RMW, CMA)"
  - name: "Lock-up-Expiry-Effekt (Insider-Verkaufsdruck bei Lock-up-Ablauf)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 3
      regimestabilitaet: 3
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.5
    netto_sharpe_erwartung: "-0.1 bis 0.2, extrem titelspezifisch; im Median nahe null bis negativ nach Borrow-Kosten"
    kernrisiko: "Lock-up-Termine sind öffentlich und lange im Voraus bekannt (S-1/424B4); Stock-Loan-Desks antizipieren den Verkaufsdruck und treiben Borrow-Fees (Ø ~15% p.a. bei kleinem Float/hoher Nachfrage, Spitzen >100% p.a. z.B. Beyond Meat) bereits vor dem Event hoch, was die ca. -1.5%-3-Tage-Bruttorendite größtenteils bis vollständig auffrisst"
    testbar_mit_freien_daten: nein
    freie_datenquelle: "Lock-up-Termine aus SEC EDGAR (S-1/424B4) frei verfügbar; Borrow-Fee-/Short-Interest-Daten (IHS Markit, S3 Partners) sind kostenpflichtig und für den entscheidenden Netto-Test nötig"
```

# Anomalieklasse IPOs — Adversarial Review (Stand: Juli 2026)

## Zusammenfassung des Urteils

Nullhypothese ("kein echtes handelbares Alpha in der IPO-Anomalieklasse") wird für alle drei geprüften Kandidaten **nicht verworfen**. Kein Kandidat erreicht CANDIDATE-Status. Der ökonomische Kern der Klasse ist zu einem großen Teil real (Underpricing existiert zweifelsfrei, Lock-up-Verkaufsdruck existiert), aber in keinem Fall überlebt er die Kombination aus Marktzugangsbeschränkungen, Kosten und Faktor-Erklärbarkeit in einer Form, die ein unabhängiger Hedgefonds ohne Emissionsbankbeziehungen systematisch und mit positivem Netto-Sharpe handeln könnte.

Alle quantitativen Aussagen zu Erstzeichnungsrenditen und langfristigen IPO-Renditen unten stammen, sofern nicht anders vermerkt, direkt aus den am 14. Juli 2026 abgerufenen Originaltabellen von Jay R. Ritter (University of Florida), die laufend bis Ende Dezember 2025 aktualisiert werden (Dokumente "Initial Public Offerings: Underpricing", Stand 18. Mai/24. Dez. 2025, und "Initial Public Offerings: Updated Long-run Statistics", Stand 7. Juli 2026). Dies ist die in der akademischen Literatur als Standardquelle referenzierte Datenbasis (u.a. Ritter 1991, Ritter & Welch 2002, Loughran & Ritter 1995 nutzen Vorläuferversionen desselben Datensatzes). Websuche war produktiv nutzbar; einzelne Sekundärzahlen aus generischen Web-Zusammenfassungen (nicht aus Primärquellen-PDFs) sind explizit als "Hinweis auf Sekundärquelle, ungeprüft" gekennzeichnet.

---

## Kandidat 1: IPO-Underpricing / Erstzeichnungsrendite

### a) Ökonomische Begründung

Der Klassiker: Der Offering-Preis liegt systematisch unter dem ersten Schlusskurs. Mean Erstzeichnungsrendite 1980–2025 (gleichgewichtet, N=9.343 US-Operating-Company-IPOs, Ritter-Datensatz): **19,0%** (proceedsgewichtet 20,6%, Median 7,0%). Kumuliert wurden 1980–2025 **250,1 Mrd. USD** "Money left on the table" (Differenz Schlusskurs minus Offer-Preis × platzierte Aktien) an die Erstzeichner verteilt.

Zwei etablierte, nicht gegenseitig ausschließliche Erklärungen:
- **Rock (1986) "Winner's Curse"**: Uninformierte Zeichner erhalten überproportional Zuteilungen bei schlechten Deals (informierte Investoren meiden diese), während gute Deals überzeichnet und rationiert werden. Underpricing ist der Preis, den Emittenten zahlen müssen, um uninformierte Investoren überhaupt zur Teilnahme zu bewegen — eine Risikoprämie für adverse Selektion, keine "kostenlose" Ineffizienz.
- **Agency/Bookbuilding-Erklärung (Loughran & Ritter 2002, Reuter 2006, Ritter & Zhang 2007 "Spinning")**: Underwriter allokieren unterbepreiste Zuteilungen gezielt an bevorzugte institutionelle Kunden (Quid-pro-Quo für Order-Flow, Soft-Dollar-Geschäft, künftiges Investmentbanking-Mandat). Emittenten (Gründer/Management, oft selbst durch IPO reich geworden) protestieren wegen Verlustaversions-/Referenzpunkt-Framing zu wenig gegen das "auf dem Tisch gelassene Geld" (Prospect-Theory-Argument von Loughran & Ritter 2002).

Verursacher der Fehlbewertung: **nicht** der breite Sekundärmarkt (der reagiert effizient auf Angebot/Nachfrage), sondern die **Zuteilungsmechanik des Bookbuilding-Verfahrens** selbst — eine strukturelle Friktion, kein Bias uninformierter Marktteilnehmer im Aftermarket.

### b) Limits to Arbitrage

Dies ist der entscheidende Punkt: Es gibt **keinen Sekundärmarkt-Arbitrage-Mechanismus**, der Underpricing wegkonkurrieren könnte, weil die Rendite nicht am offenen Markt verdient wird, sondern durch **Zuteilung zum Offer-Preis**. Wer keine Zuteilung bekommt, kann die Rendite nicht erzielen — Kaufen zum ersten Schlusskurs bringt nichts (das ist genau der Ausgangspunkt für Kandidat 2). Der Zugang zu Zuteilungen ist selbst rationiert und an Beziehungen zu Emissionsbanken gebunden. Das ist der Grund, warum die Ineffizienz seit mindestens 1960 (Ibbotson/Sindelar/Ritter-Daten reichen zurück bis 1960, durchschnittlich 17,7% seit 1960–2025) nicht arbitriert wurde: Sie ist strukturell nicht durch Kapitalzufluss schließbar, weil das knappe Gut (Zuteilung) nicht durch Kapital, sondern durch Beziehungen alloziert wird.

### c) Originalstudien

- Ibbotson (1975); Ibbotson, Sindelar & Ritter (1994, JACF) — Basisdaten seit 1960.
- Rock (1986, JFE) — Winner's-Curse-Modell.
- Ritter (1991, JF) — Standardreferenz für die kombinierte Betrachtung Underpricing + Long-run-Underperformance, Stichprobe 1.526 US-IPOs 1975–1984.

### d) Out-of-Sample-/Post-Publication-Evidenz, Decay

**Kein erkennbarer Decay im Gross-Effekt.** Der Effekt ist über 46 Jahre bemerkenswert stabil bis steigend:
- 1980–1989: 7,2% | 1990–1998: 14,8% | 1999–2000 (Dotcom-Bubble): 64,6% | 2001–2025: 19,1%.
- Jüngste Jahre: 2020: 41,6% | 2021: 32,1% | 2022: 48,9% (nur 38 Deals) | 2023: 11,9% | 2024: 15,3% | 2025: 29,3%.
- Zahl der Tage mit Kursverdopplung am ersten Handelstag (Offer→Close): 2020 Q3/Q4 allein 19 Fälle, 2021 gesamt 18 Fälle — ein Comeback ggü. der ruhigen 2001–2019-Periode.

Der Effekt ist also nicht "wegpubliziert" worden — plausibel, weil er (siehe b) strukturell nicht arbitrierbar ist. Das ist ungewöhnlich robust im Vergleich zu praktisch jeder anderen in McLean & Pontiff (2016, JF) untersuchten Anomalie, deren Publikationsstichprobe im Schnitt einen Renditerückgang von ca. 58% post-Publikation zeigt (Out-of-Sample vor Publikation: −26%, Post-Publikation: −58% ggü. In-Sample-Periode). IPO-bezogene Charakteristika sind Teil des dort getesteten Anomalie-Sets, aber der Underpricing-Effekt selbst ist keine "entdeckte Ineffizienz", die durch Handel korrigiert werden konnte — er ist im Design des Bookbuilding-Verfahrens eingebaut.

### e) Kosten

Für den seltenen Fall eines Investors mit Zuteilungszugang: Keine nennenswerten Ausführungskosten (Kauf zum Offer-Preis ist die Zuteilung selbst, kein Spread/Impact). Der wahre Preis ist aber implizit: Zugang wird erkauft durch Gegenleistungen (Order-Flow an die Bank, Halten unattraktiver Deals, Soft-Dollar-Zahlungen, Investmentbanking-Beziehung) — nicht in Cash messbar, aber real.

### f) Kapazität und Handelbarkeit

**Sehr gering.** Aggregiertes "Money left on the table" 2001–2025 (post-Bubble-Normalperiode) liegt bei rund 20–30 Mrd. USD/Jahr über den gesamten US-IPO-Markt verteilt auf alle Zeichner — geteilt durch typischerweise Dutzende bis Hunderte Institutionen pro Deal, ist die pro Fonds erzielbare Kapitalmenge klein. In kalten Jahren (2022–2024: nur 38–72 Deals p.a.) kollabiert das Opportunity-Set fast vollständig. Ohne Underwriter-Beziehung: Kapazität = 0.

### g) Regimeabhängigkeit und Tail-Risiko

Stark prozyklisch: Deal-Volumen kollabiert in kalten Märkten (2022: 38 Deals vs. 2021: 311 Deals), während die Durchschnittsrendite pro Deal in solchen Perioden paradoxerweise hoch bleiben oder steigen kann (2022: 48,9%, aber nur bei den wenigen Deals, die überhaupt durchgeführt wurden — Survivorship/Selektion: nur die stärkste Nachfrage schafft es in kalten Fenstern an die Börse). Tail-Risk: In Hot-Issue-Märkten (1999–2000, 2020–2021) steigt das Volumen und die Rendite gleichzeitig, was Klumpenrisiko und Blasenexposure erzeugt (siehe Kandidat 2 zu den Folgen).

### h) Bekannte Kritik/Widerlegungen

- **Zuteilungsproblem**: Der akademisch gemessene Effekt ist ein Anlage-auf-dem-Papier-Konstrukt (Offer-Preis zu Schlusskurs), das die meisten Marktteilnehmer real nicht realisieren können — die Literatur selbst warnt konsistent davor, Underpricing mit einer handelbaren Strategie zu verwechseln.
- **Mikrostruktur**: Der erste Schlusskurs ist oft illiquide/volatil (dünner Float, Spezialisten-Preisfindung), Renditen dort gemessen sind daher tendenziell nach oben verzerrt ggü. tatsächlich erzielbaren Ausführungspreisen für größere Institutionen.
- **Microcap-Konzentration**: Größte Underpricing-Werte konzentrieren sich in kleinen, spekulativen Segmenten (Life-Science-IPOs 1980–2025: 15,9% mittlere Rendite, davon 41,8% mit Sales = 0; Tech-IPOs: 31,2% vs. Non-Tech 12,1%), die für institutionelle Kapazität am wenigsten geeignet sind.

**Urteil: WEAK.** Real, robust, nicht wegarbitriert — aber strukturell keine im offenen Markt handelbare Ineffizienz für einen Fonds ohne Emissionsbank-Beziehungen. Score-mäßig hohe Reproduzierbarkeit, aber niedrige Handelbarkeit/Kapazität drücken das Gesamturteil unter CANDIDATE.

---

## Kandidat 2: Langfristige IPO-Underperformance ("New Issues Puzzle")

### a) Ökonomische Begründung

Ritter (1991) und Loughran & Ritter (1995) dokumentierten, dass IPO-Firmen in den 3–5 Jahren nach dem Börsengang systematisch schlechter abschneiden als vergleichbare Nicht-Emittenten. Vorgeschlagene Erklärung: **Windows-of-Opportunity/Market-Timing-Hypothese** — Manager nutzen Phasen optimistischer Investorenstimmung (Sentiment-getriebenes Overpricing wachstumsstarker, schwer zu bewertender junger Firmen), um genau dann an die Börse zu gehen, wenn Investoren am meisten für Wachstumsstory-Aktien zu zahlen bereit sind. Verursacher: übermäßig optimistische Sekundärmarkt-Investoren (retail-lastig, Extrapolationsbias bei jungen Wachstumsfirmen ohne Trackrecord) plus Insider/PE/VC, die den Timing-Vorteil bewusst ausnutzen (adverse Selektion des Angebotszeitpunkts durch besser informierte Insider).

### b) Limits to Arbitrage

Short-Selling neu gelisteter, kleiner, illiquider Wachstumsfirmen mit dünnem Float (insbesondere vor Lock-up-Ablauf) ist strukturell teuer/eingeschränkt — siehe Kandidat 3. Zusätzlich: Value-/Growth-Rotationsrisiko macht das Halten kurzer Positionen in "hot" Themen (z.B. Tech-IPOs in Bubble-Perioden) für institutionelle Short-Seller riskant (Beweis: Dotcom-Shorts liefen 1998–2000 massiv gegen die Position, bevor sie 2000–2002 auszahlten — klassisches "Markets can stay irrational longer than you can stay solvent").

### c) Originalstudie

- **Ritter (1991, JF)**: 1.526 IPOs 1975–1984, 3-Jahres-Buy-and-Hold-Rendite IPO-Firmen 34,47% vs. Kontrollfirmen (Branchen-/Size-gematcht) 61,86% — Differenz ≈ −27,4 Prozentpunkte über 3 Jahre (Literaturangabe, nicht aus Primärquelle re-verifiziert in dieser Session).
- **Loughran & Ritter (1995, JF, "The New Issues Puzzle")**: 4.753 IPOs 1970–1990. Durchschnittliche Jahresrendite in den ersten 5 Jahren nach Emission: ca. 5% p.a. für IPO-Firmen vs. ca. 12% p.a. für größen-gematchte Nicht-Emittenten; Wealth Relative ≈ 0,83 (Literaturangabe).

### d) Out-of-Sample-/Post-Publication-Evidenz, Decay — **substanziell und dokumentiert**

Hier zeigt sich der stärkste Decay der drei Kandidaten, direkt aus den aktuellen Ritter-Tabellen (Stand Dez. 2025/Juli 2026):

- **Aktuelle gepoolte Schätzung (Table 20, 1980–2024, Renditen bis 31.12.2025)**: IPO-Firmen underperformen größen-gematchte Nicht-Emittenten um **3,6% p.a.** und size-&-B/M-gematchte Firmen um nur noch **2,1% p.a.** (geometrisches Mittel über 5 Jahre: IPO 10,6% vs. Size&BM-Match 12,5%, Differenz −1,9%/Jahr). Das ist eine Abschwächung um ca. **65–70%** gegenüber der in Ritter (1991) implizierten Rate von grob geschätzt −6% p.a. (aus 34,47% vs. 61,86% über 3 Jahre).
- **Für große, profitable Emittenten ist der Effekt praktisch verschwunden bis umgekehrt**: IPOs mit LTM-Sales ≥ 1 Mrd. USD zeigen 3-Jahres-Style-adjusted-Rendite von **+0,6%** (Table 16a, N=866, 1980–2024) — nicht mehr unterscheidbar von null. Profitable Emittenten mit Sales > 100 Mio. USD: +5,4% style-adjusted (Table 16b). Der gesamte negative Durchschnitt wird von kleinen, unprofitablen Emittenten getragen (Sales < 100 Mio. USD, unprofitabel: **−29,6% style-adjusted über 3 Jahre**, N=2.880).
- **Kritischer Messpunkt-Effekt**: Wird die 3-Jahres-Rendite **ab dem Offer-Preis** (statt ab dem ersten Schlusskurs) gemessen — also für einen Investor, der tatsächlich eine IPO-Zuteilung erhalten hat — kehrt sich das Bild um: Style-adjusted Rendite 1980–2023 (ohne Bubble-Jahre 1999–2000) ist **+13,8%** über 3 Jahre (Table 16c, N=8.325), getrieben v.a. durch Tech-IPOs (+46,0% style-adjusted). Das arbeitet die zentrale Schwäche der Anomalie heraus: Das "New-Issues-Puzzle" ist im Kern ein **Aftermarket-Käufer-Phänomen**, kein IPO-Investment-Phänomen.
- **Faktor-Erklärung (stärkste Kritik)**: Brav & Gompers (1997, JF) und Carter, Dark & Sapp (2011) zeigen, dass das Underperformance-Puzzle im Fama-French-3-Faktor-Modell weitgehend verschwindet — IPO-Firmen performen ähnlich wie etablierte Firmen gleicher Size/B-M-Charakteristik. Asness, Frazzini & Pedersen (Quality-Minus-Junk) liefern eine ergänzende Erklärung: IPO-Firmen sind im Schnitt qualitativ schlechtere ("junger, unprofitabler, höher bewerteter") Firmen; kontrolliert man für den QMJ-Faktor, outperformen IPOs sogar die Benchmark. Das deutet stark darauf hin, dass die "Anomalie" ein **repackaged Size-/Quality-/Growth-Faktor-Exposure** ist, keine eigenständige Fehlbewertung.
- Sekundärquellen-Hinweis (ungeprüft, aus Web-Zusammenfassung): Eine 2021er Studie im Journal of Banking & Finance ("IPO underperformance and the idiosyncratic risk puzzle") argumentiert ähnlich, dass die Underperformance ein Spezialfall der "Low-idiosyncratic-Risk-Anomalie" ist und nach deren Kontrolle verschwindet.
- **Modernes Extrembeispiel für Regimeabhängigkeit**: deSPACs (Gahng, Ritter & Zhang 2023, RFS, Table 15c aktualisiert) zeigen für 2012–2022 (N=451) eine market-adjusted 3-Jahres-Rendite von **−74,7%** — die IPO-Underperformance in ihrer extremsten modernen Ausprägung, konzentriert im SPAC-Boom-Jahrgang 2021 (−80,0% market-adjusted). Zeigt: Der Effekt ist nicht tot, aber hochgradig episodisch/regimeabhängig statt eines stetigen Alphas.

### e) Kosten

Long-Short-Umsetzung würde bedeuten: Long große/profitable IPOs (kein Alpha mehr vorhanden, s.o.) gegen Short kleine/unprofitable/VC-finanzierte IPOs. Die Short-Seite ist genau das Segment mit den höchsten Borrow-Kosten und geringster Liquidität (dünner Float in den ersten 6–12 Monaten wegen Lock-up, siehe Kandidat 3). Turnover niedrig (Haltedauer 3–5 Jahre), aber Spread/Impact-Kosten auf der Short-Seite hoch.

### f) Kapazität und Handelbarkeit

Gering bis mittel auf der Long-Seite (das ist aber nur eine generische Size-/Quality-Tilt-Exposure, günstiger über Standard-Faktor-ETFs erzielbar). Auf der Short-Seite kapazitätslimitiert durch Borrow-Verfügbarkeit in Small-/Microcap-IPOs.

### g) Regimeabhängigkeit und Tail-Risiko

Extrem episodisch: 1999–2000-Jahrgang: −58,9% style-adjusted über 3 Jahre; 1980–1989-Jahrgang: **+2,2%** (praktisch kein Effekt); 2012-Jahrgang: +33,4%. Der gepoolte Durchschnitt verdeckt eine massive Varianz zwischen Emissionsjahrgängen — mehr ein Symptom von Bubble-Perioden (1999–2000, 2020–2021/SPACs) als ein stetiges Faktor-Alpha.

### h) Bekannte Kritik/Widerlegungen

- **Messpunkt-Artefakt** (s.o., d): Effekt kehrt sich um, wenn ab Offer-Preis gemessen.
- **Faktor-Konfundierung**: Brav & Gompers (1997), Carter et al. (2011), QMJ-Literatur — Effekt praktisch vollständig durch Size/B-M/Quality erklärbar.
- **Look-Ahead/Selection Bias**: Ritter selbst warnt in den Tabellen-Fußnoten, dass Delisting-Behandlung (Ersatzfirmen-Splicing) und die Zusammensetzung der Vergleichsgruppe (nur Firmen mit ≥5 Jahren CRSP-Historie) methodische Annahmen erfordern, die die Ergebnisse in beide Richtungen verschieben können.
- **Microcap-Konzentration**: Der gesamte negative Effekt kommt aus dem Sales<100-Mio.-USD/unprofitabel-Segment — für ökonomisch relevante, liquide, institutionell handelbare IPOs (>1 Mrd. USD Sales) ist der Effekt statistisch nicht von null zu unterscheiden.

**Urteil: KILL.** Der Rohdaten-Effekt ist real und gut dokumentiert, aber (1) er hat seit der Originalstudie um ca. 65–70% an Größe verloren, (2) er kehrt sich um, wenn man den realistischen IPO-Investor-Einstiegspunkt (Offer-Preis) statt des Aftermarket-Einstiegspunkts nimmt, und (3) er wird von der Faktor-Literatur (Size, B/M, Quality-Minus-Junk) weitgehend absorbiert. Es bleibt kein robuster, eigenständiger, kostenrobuster IPO-spezifischer Effekt übrig.

---

## Kandidat 3: Lock-up-Expiry-Effekt

### a) Ökonomische Begründung

Lock-up-Vereinbarungen (typischerweise 180 Tage) verbieten Insidern (Management, VC/PE, Early-Investoren, Mitarbeiter) den Verkauf vor einem festgelegten Termin. Bei Ablauf kommt es zu einem mechanischen Angebotsschock: Insider, die zuvor nicht verkaufen durften und typischerweise überkonzentriert in der eigenen Firma sind (Diversifikationsbedarf), verkaufen gebündelt. Das ist eine **strukturelle Liquiditäts-/Angebotsfriktion**, kein klassischer Behavioral Bias — die Verursacher sind Insider mit Diversifikationszwang, nicht fehlinformierte Marktteilnehmer. Sekundär: Der Markt antizipiert unvollständig, weil Downward-Sloping-Demand-Curves gelten (Aktien sind keine perfekten Substitute; ein großer Angebotsschock bewegt den Preis, auch wenn der Termin bekannt ist).

### b) Limits to Arbitrage

Genau hier liegt der Casus: Der Termin ist **öffentlich und lange im Voraus bekannt** (im Prospekt/S-1/424B4 festgelegt). Es gibt also theoretisch keinen Informationsvorsprung — die einzige Arbitrage-Barriere ist die **Fähigkeit, die Short-Position tatsächlich zu tragen** (Borrow-Verfügbarkeit und -Kosten in Small-Float-Neuemissionen, s.u.). Genau diese Barriere hat sich seit der Originalstudie verschärft: Securities-Lending-Desks antizipieren den Termin inzwischen ebenso gut wie akademische Forscher und treiben die Borrow-Fee vor dem Event systematisch hoch (siehe e).

### c) Originalstudie

- **Field & Hanka (2001, JF, "The Expiration of IPO Share Lockups")**: Große Stichprobe von Lock-up-Ablaufterminen aus den 1990er-Jahren (im niedrigen vierstelligen Bereich). Befund: **permanenter +40%-Anstieg des durchschnittlichen Handelsvolumens** und ein statistisch signifikanter **3-Tages-CAR von ca. −1,5%** um den Ablauftermin. Effekt stärker bei VC-finanzierten Firmen; VCs verkaufen aggressiver als Management/andere Aktionäre.
- Verwandte/Replikationsstudien: **Ofek & Richardson (2000)** — negative abnormale Renditen und steigendes Short-Interest vor Lock-up-Ablauf, konsistent mit Downward-Sloping-Demand; **Bradley, Jordan, Roten & Yi (2001)** — ähnliche negative CARs, besonders ausgeprägt bei VC-gestützten Tech-IPOs der späten 1990er.

### d) Out-of-Sample-/Post-Publication-Evidenz, Decay

Der Grundeffekt (negativer CAR, Volumenanstieg um den Ablauftermin) wurde in mehreren nachfolgenden Studien bis mindestens 2018 in ähnlicher Größenordnung repliziert (u.a. eine 2018er-Studie im Journal of Banking & Finance zu Short-Selling-Mustern um Lock-up-Ablauf, Sekundärquelle, ungeprüft im Detail). Die Richtung des Effekts scheint also robust zu sein — das unterscheidet diesen Kandidaten von Kandidat 2. Was sich aber deutlich verändert hat, ist die **Marktreaktion auf der Kostenseite**: Institutionelle Securities-Lending-Research (S&P Global Market Intelligence, ehemals IHS Markit) dokumentiert explizit, dass **Borrow-Kosten bereits im Vorfeld bekannter Lock-up-Termine ansteigen** ("Borrow costs spike ahead of pre-IPO lockup expiries") — ein klares Crowding-Signal: Der Trade ist der Stock-Loan-Industrie so gut bekannt, dass er präventiv eingepreist wird, was die realisierbare Netto-Rendite für Shortseller strukturell schmälert. Das ist funktional äquivalent zu einem Decay-Mechanismus, nur dass er über Finanzierungskosten statt über den Preis-Impact-Kanal wirkt.

### e) Kosten — **Borrow-Verfügbarkeit und -Kosten (explizit angefordert)**

Dies ist der entscheidende Werttreiber/-vernichter der Strategie:
- Stock-Loan-Fees um Lock-up-Ablauf variieren nach "Demand-to-Short-Score" und Emissionsgröße: durchschnittlich **15,08% p.a.** annualisierte Fee bei kleinen, stark nachgefragten Neuemissionen vs. nur **0,83% p.a.** bei großen, gering nachgefragten Emissionen (S&P Global Market Intelligence, Sekundärquelle aus Websuche, Größenordnung plausibel und konsistent mit bekannten Einzelfällen).
- Einzelfälle mit extremen Spitzen: Borrow-Fee für Beyond Meat (2019 IPO) zeitweise **>100% annualisiert**; für andere IPOs wurden Fees bis 95% im Vorfeld von Lock-up-Ablaufterminen beobachtet (Sekundärquellen-Hinweis, ungeprüft im Detail, aber Größenordnung ist in Prime-Broker-Kreisen gut dokumentiertes Phänomen).
- **Rechnung**: Ein 3-Tages-Bruttoeffekt von −1,5% (Field & Hanka) steht einer Finanzierungskosten-Belastung gegenüber, die bei 15% p.a. bereits nach ca. 36 Tagen Haltedauer den gesamten Bruttoeffekt aufgezehrt hat (15%/365×36 ≈ 1,5%). Da die Short-Position aber typischerweise deutlich vor dem exakten Ablaufdatum aufgebaut werden muss (Pre-Positionierung wegen erwarteter Kursreaktion, unsicherem exaktem Timing der Insiderverkäufe, und da laut Literatur teils auch schon Tage vor dem offiziellen Termin gehandelt wird — SDC-Datenbank meldet das Ablaufdatum bei 78% der IPOs sogar einen Tag zu früh, was zeigt, wie datenempfindlich das exakte Timing ist), ist die effektive Haltedauer oft länger als 36 Tage. Bei den beobachteten Spitzenwerten (50–100%+ p.a.) ist der Trade nach Kosten mit hoher Wahrscheinlichkeit **strukturell unprofitabel**.

### f) Kapazität und Handelbarkeit

Gering: Der Effekt ist auf einzelne Small-/Midcap-Neuemissionen mit dünnem Float beschränkt — exakt die Namen, bei denen Aktienleihe am knappsten und teuersten ist (Henne-Ei-Problem: die Titel mit dem stärksten erwarteten Preis-Effekt sind gleichzeitig die mit den höchsten Borrow-Kosten, weil beide vom selben Merkmal getrieben werden — geringer Streubesitz). Positionsgrößen pro Titel sind klein; Diversifikation über viele gleichzeitige Lock-up-Events pro Quartal ist möglich, aber jede einzelne Position ist kapazitätslimitiert durch die verfügbare Leihmenge.

### g) Regimeabhängigkeit und Tail-Risiko

Der Effekt ist stärker in Perioden nach Hot-Issue-Märkten (viele VC-backed Tech-/Biotech-IPOs mit konzentriertem Insider-Ownership, die 6 Monate später gebündelt auslaufen — z.B. das große Lock-up-Ablauf-Fenster im ersten Halbjahr 2022 nach dem 2021er-IPO-Rekordjahr mit 311 Deals). Tail-Risiko: Short-Squeeze-Gefahr ist real und asymmetrisch — bei positiven Nachrichten oder Übernahmegerüchten in der Haltefrist kann ein Hard-to-Borrow-Titel mit ohnehin schon 50-100% Fee zusätzlich einen Squeeze erleiden (unbegrenztes Verlustrisiko auf der Short-Seite plus explodierende Borrow-Fee gleichzeitig).

### h) Bekannte Kritik/Widerlegungen

- **Datenqualität/Timing-Artefakt**: Eine in der Literatur dokumentierte Erkenntnis (Sekundärquelle) zeigt, dass Standarddatenbanken (SDC) das Lock-up-Ablaufdatum bei 78% der IPOs einen Tag zu früh ausweisen — was einen Teil der in älteren Studien gemessenen "Volumensprünge am Folgetag" erklären könnte und auf Mikrostruktur-/Data-Timing-Artefakte statt auf reinen ökonomischen Effekt hindeutet.
- **Crowding-Beweis**: Dass Borrow-Fees systematisch VOR dem Termin ansteigen, ist der direkte empirische Beleg dafür, dass der Trade von der Stock-Loan-Industrie längst antizipiert und bepreist wird — ein Lehrbuchbeispiel für "Anomalie durch Markt-Reaktion neutralisiert", nur eben über den Finanzierungskanal statt über den Preis direkt.
- **Selection**: Der stärkste gemessene Effekt konzentriert sich auf VC-backed-Firmen der 1990er-Sample-Periode; in der heutigen Marktstruktur (viel breiterer Optionsmarkt, ETF-Arbitrage, mehr Marktmacher-Kapazität) ist plausibel, dass ein Teil des Preis-Effekts strukturell kleiner geworden ist, auch wenn die Kernrichtung repliziert wurde.

**Urteil: WEAK.** Der Bruttoeffekt ist die am robustesten replizierte der drei Anomalien (klare, konsistente Richtung über mehrere Jahrzehnte und mehrere Autorenteams), aber es ist zugleich der Kandidat mit dem klarsten dokumentierten Kostenkanal, der ihn nach Berücksichtigung von Borrow-Fees für die meisten Namen um den Nullpunkt herum bis negativ macht. Kapitalstark und geduldig könnte ein Fonds das nur bei sorgfältiger Titel-Selektion (niedrige Borrow-Fee, ausreichender Float) profitabel handeln — das reduziert das ursprünglich breite Sample auf eine kleine, margin-arme Nische.

---

## Klassenurteil und Kapazitätsschätzung

**Gesamteinschätzung: Die Klasse "IPOs" liefert keinen CANDIDATE.** Das ist ein ehrliches, für eine adversariale Prüfung erwartbares Ergebnis, aber keine triviale Nullaussage — die drei Effekte sind unterschiedlich "tot":

1. **Underpricing** ist die am wenigsten tote der drei Teilanomalien — der Effekt existiert real, hat nicht abgenommen, ist aber eine **Zugangsrente**, keine Marktineffizienz im klassischen Sinne. Ein Fonds mit Prime-Broker-/Underwriter-Beziehungen (z.B. über einen angeschlossenen Broker-Dealer) könnte hierüber tatsächlich Kapital deployen — das ist aber ein Business-Development-Problem, kein quantitatives Handelssignal, und daher außerhalb des Mandats "systematische Handelsstrategie".
2. **Long-run Underperformance** ist die am gründlichsten widerlegte der drei — Messpunkt-Artefakt plus vollständige Faktor-Erklärbarkeit (Brav & Gompers 1997; Carter et al. 2011; QMJ) lassen keinen eigenständigen Rest-Effekt übrig, der über einen Standard-Size-/Quality-Tilt hinausgeht. Empfehlung: aus dem Strategie-Universum streichen.
3. **Lock-up-Expiry** ist real, aber ökonomisch klein (3-Tage-Effekt von ca. −1,5%) und wird durch dokumentierte, mittlerweile antizipatorisch steigende Borrow-Kosten strukturell neutralisiert. Als eigenständige Strategie nicht tragfähig; allenfalls als kleiner Overlay-Signal-Baustein innerhalb eines breiteren Short-Interest-/Event-Portfolios mit strikter Borrow-Fee-Filterung denkbar — dann aber mit Kapazität im niedrigen zweistelligen Millionenbereich, nicht als eigenständiges Buch.

**Kapazitätsschätzung für die gesamte Klasse**: Selbst im günstigsten Szenario (Underpricing mit Zuteilungszugang) begrenzt das aggregierte "Money-left-on-the-table"-Volumen (ca. 20–30 Mrd. USD/Jahr über den gesamten Markt, geteilt auf viele Zeichner) und die Marktzugangsbeschränkung die realistisch für einen einzelnen unabhängigen Fonds erzielbare Kapitalallokation auf einen niedrigen zweistelligen bis mittleren dreistelligen Millionenbereich — und selbst das nur mit Banking-Beziehungen, die außerhalb des Bereichs reiner quantitativer Signalgenerierung liegen.

**Fazit für das Mandat**: Kein Einsatz von Kapital in dieser Anomalieklasse als eigenständige Strategie empfohlen. Falls das Fondsmandat ohnehin Small-Cap-Long-Short-Bücher führt, kann ein leichter Underweight-Tilt auf junge, unprofitable, VC-backed Post-IPO-Namen (< 12 Monate seit Listing, insbesondere kurz nach Lock-up-Ablauf) als Risiko-Overlay sinnvoll sein — das ist aber eine Ableitung aus bekannten Size-/Quality-Faktoren, keine eigenständige IPO-Anomalie-Strategie.

---

## Quellen

- Ritter, J.R.: *Initial Public Offerings: Underpricing* (Primärquelle, direkt abgerufen, Stand 18. Mai/24. Dez. 2025/Feb. 2026), site.warrington.ufl.edu/ritter/files/IPOs-Underpricing.pdf
- Ritter, J.R.: *Initial Public Offerings: Updated Long-run Statistics* (Primärquelle, direkt abgerufen, Stand 7. Juli 2026), site.warrington.ufl.edu/ritter/files/IPOs-long-run-returns-on-IPOs.pdf
- [The Expiration of IPO Share Lockups (Field & Hanka 2001)](https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00334)
- [Short selling around the expiration of IPO share lockups](https://www.sciencedirect.com/science/article/abs/pii/S0378426617302339)
- [Borrow costs spike ahead of pre-IPO lockup expiries | S&P Global](https://www.spglobal.com/marketintelligence/en/mi/research-analysis/borrow-costs-spike-ahead-of-preipo-lockup-expiries.html)
- [Shorting IPO lockup expiration | S&P Global / IHS Markit](https://www.spglobal.com/marketintelligence/en/mi/research-analysis/05082015-equities-shorting-ipo-lockup-expiration.html)
- [The new issues puzzle revisited: The role of firm quality in explaining IPO returns](https://www.sciencedirect.com/science/article/abs/pii/S0165176517303026)
- [IPO underperformance and the idiosyncratic risk puzzle](https://www.sciencedirect.com/science/article/abs/pii/S0378426621001497)
- [Does Academic Research Destroy Stock Return Predictability? (McLean & Pontiff 2016)](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365)
- [Quality Minus Junk (Asness, Frazzini & Pedersen)](http://www.econ.yale.edu/~shiller/behfin/2013_04-10/asness-frazzini-pedersen.pdf)

Nicht direkt neu abgerufen, aber literatur-etabliert (Werte aus internem Wissen, nicht in dieser Session re-verifiziert): Ritter (1991, Journal of Finance); Loughran & Ritter (1995, Journal of Finance, "The New Issues Puzzle"); Rock (1986, Journal of Financial Economics); Brav & Gompers (1997, Journal of Finance); Carter, Dark & Sapp (2011); Ofek & Richardson (2000); Bradley, Jordan, Roten & Yi (2001); Loughran & Ritter (2002, Review of Financial Studies, "Why Don't Issuers Get Upset About Leaving Money on the Table?").
