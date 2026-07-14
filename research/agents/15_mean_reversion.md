```yaml
agent: 15
klasse: "Mean Reversion / Short-Term Reversal"
websuche_verfuegbar: ja
strategien:
  - name: "Kurzfristiges Cross-Sectional Reversal (Wochen-/Monatsfrequenz, Einzelaktien)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 4
      regimestabilitaet: 3
      handelbarkeit: 1
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "≈0,0 bis leicht negativ fuer Nicht-Marktmacher nach realistischen Kosten; nur fuer registrierte HFT-Marktmacher mit Rebates/Kolokation potenziell hoch, aber dann kein Alpha-Signal mehr sondern Marktmaking-Geschaeftsmodell"
    kernrisiko: "Bruttorendite ist zu 50-80% Bid-Ask-Bounce/Liquiditaetskompensation und Lead-Lag-Artefakt (Lo/MacKinlay 1990); Effekt konzentriert exakt in den Aktien (klein, illiquide, hoher Spread), in denen Transaktionskosten das Signal auffressen. Seit Dezimalisierung (2001) und Aufstieg von HFT-Marktmachern ist die fuer Aussenstehende handelbare Nettorendite auf praktisch Null gefallen."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Data Library: Short-Term Reversal Factor (ST_Rev), monatlich ab 1926; fuer Wochenfrequenz zusaetzlich CRSP/Yahoo-Finance-Kursdaten noetig"
  - name: "Pairs Trading (Distance-Methode, Gatev/Goetzmann/Rouwenhorst)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 3
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0,0-0,3 netto, mit dokumentiertem monotonem Decay seit den 1960ern; punktuell hoehere Renditen in Krisen (2007-09), aber Tail-Risiko durch korrelierte Unwinds (August 2007)"
    kernrisiko: "Dokumentierter Decay von 0,86%/Monat (1962-88) auf 0,24%/Monat (2003-09), ca. 70% davon durch steigendes Arbitragerisiko (nicht-konvergierende Paare); zusaetzlich Crowding-/Unwind-Tail-Risiko wie im Quant Quake August 2007."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Kursdaten beliebiger Aktienpaare via Yahoo Finance/Stooq (z.B. KO/PEP, XOM/CVX); Distance-Methode ist selbst nachbaubar, kein vorgefertigter Ken-French-Datensatz vorhanden"
  - name: "Statistische Arbitrage / Residual- und Industrie-Reversal (faktor-neutral, PCA-basiert)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 3
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.3
    netto_sharpe_erwartung: "0,1-0,3 netto fuer portfolio-/industriebasierte Low-Turnover-Varianten; nahe 0 fuer hochfrequente Einzeltitel-PCA-Residual-Varianten ausserhalb einer HFT-Infrastruktur"
    kernrisiko: "Belastbarste Evidenz fuer die kostenguenstigere Industrie-Variante stammt teils aus Practitioner-/Produktresearch (Interessenkonflikt); die granulare PCA-Residual-Variante teilt das Kostenproblem von Kandidat 1; gleiches Crowding-/Tail-Risikoprofil wie Pairs Trading."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Data Library: 12/49 Industry Portfolios (taeglich) fuer Industrie-Reversal-Replikation; PCA-Faktoren aus CRSP/Yahoo-Kursmatrix selbst konstruierbar"
```

# Mean Reversion / Short-Term Reversal — Adversariales Research-Memo

**Agent 15 | Juli 2026 | Unabhaengige Analyse, isoliert von parallelen Research-Strecken**

## 0. Ausgangsposition und Nullhypothese

Mandat: kurzfristiges Reversal (1 Woche/1 Monat), Pairs Trading, statistische Arbitrage im Aktienquerschnitt. Nullhypothese: **es gibt kein fuer Aussenstehende erntbares Alpha in dieser Klasse.** Diese Klasse ist die methodisch am besten erforschte Anomalie-Familie der Literatur — und gleichzeitig diejenige, bei der die Kluft zwischen Brutto- und Nettorendite historisch am groessten ist. Der Kernverdacht, den dieses Memo prueft: Reversal-Renditen sind ueberwiegend eine Kompensation fuer Liquiditaetsbereitstellung (Nagel 2012) bzw. ein Mikrostruktur-Artefakt (Bid-Ask-Bounce, Lead-Lag-Kovarianzen), das genau in den Marktsegmenten anfaellt, in denen Transaktionskosten am hoechsten sind. Das ist kein Nebenbefund, sondern nach meiner Lektuere der Literatur der zentrale, gut dokumentierte Befund dieser Klasse.

Websuche war in dieser Sitzung verfuegbar und wurde genutzt (WebSearch funktionierte; WebFetch auf zwei PDF-Quellen (NY Fed Staff Report 513, BFI Working Paper 2024-135) scheiterte an Encoding-Problemen — diese Zahlen stammen daher aus internem Wissen und sind entsprechend gekennzeichnet). Wo Zahlen nicht in dieser Sitzung durch Websuche re-verifiziert werden konnten, ist das explizit vermerkt.

---

## 1. Kandidat 1: Kurzfristiges Cross-Sectional Reversal (Wochen-/Monatsfrequenz, Einzelaktien)

### a) Oekonomische Begruendung — wer zahlt wen?

Zwei konkurrierende (nicht exklusive) Erklaerungen:

1. **Liquiditaetsprovision (Nagel 2012, "Evaporating Liquidity", RFS 25(7):2005-2039).** Nagel zeigt, dass die Rendite einer klassischen Reversal-Strategie als Proxy fuer die Rendite aus Liquiditaetsbereitstellung interpretiert werden kann. Die erwartete Rendite und der bedingte Sharpe Ratio dieser Strategie sind stark durch den (gelaggten) VIX prognostizierbar — sie schnellen in Stressphasen (2007-09) massiv nach oben. Mechanismus: Wenn intermediaerbeschraenkte Haendler (constrained financial intermediaries) sich in Stressphasen aus der Liquiditaetsbereitstellung zurueckziehen, muessen verbleibende Liquiditaetsanbieter fuer die Absorption von Orderflow-Ungleichgewichten hoeher entschaedigt werden. Wer zahlt: uninformierte, eilige Verkaeufer/Kaeufer (institutionelle Blocktrades, erzwungene Liquidationen), die eine temporaere Preiskonzession fuer sofortige Ausfuehrung akzeptieren.
2. **Overreaction.** Investoren ueberreagieren auf kurzfristige Preisbewegungen bzw. Nachrichten, was sich innerhalb von Tagen/Wochen korrigiert.

Die entscheidende Frage fuer die Nullhypothese ist: Wie viel der Bruttorendite ist (2) — eine echte Verhaltensanomalie, die einem geduldigen Arbitrageur zufliesst — versus (1)/Mikrostruktur, wo die "Rendite" in Wahrheit die Kompensation fuer eine Dienstleistung (Immediatismus) ist, die vom Markt bereits ueber den Spread bepreist wird und die ein Aussenstehender ohne Marktmacher-Infrastruktur gar nicht vereinnahmen kann.

### b) Limits to Arbitrage

- **Turnover**: Wochenfrequenz-Rebalancing impliziert vollstaendige Buchumschlagung pro Woche → Turnover deutlich >2.000% p.a. Genau bei diesem Umschlagstempo ist jede Kostenschaetzung hochsensitiv.
- **Konzentration im illiquiden Segment**: Avramov, Chordia & Goyal (2006, JF, "Liquidity and Autocorrelations in Individual Stock Returns") zeigen, dass Reversal-Profite auf Aktien mit hohem Spread/geringer Liquiditaet/hohem Turnover konzentriert sind — also exakt dort, wo Handelskosten am hoechsten sind.
- **Leerverkaufsbeschraenkungen** auf der Short-Leg (juengste "Gewinner", oft ebenfalls kleine/illiquide Titel mit Borrow-Kosten oder -Restriktionen).
- **Kapitalbedarf zur Unzeit**: Da die Strategie laut Nagel gerade in Stressphasen am profitabelsten ist, faellt der Kapitalbedarf genau dann an, wenn Finanzierung/Margin am knappsten sind — ein klassisches Limits-to-Arbitrage-Argument (Shleifer/Vishny 1997).

### c) Originalstudien

| Studie | Stichprobe | Effekt | Signifikanz |
|---|---|---|---|
| **Jegadeesh (1990)**, JoF 45(3):881-898 | NYSE/AMEX, 1934-1987 | Kontrarian-Portfolio aus extremen Monatsrendite-Dezilen: ca. 2,49%/Monat abnormale Rendite | hoch signifikant (t-Statistik im hohen einstelligen Bereich; exakter Wert in dieser Sitzung nicht per Websuche re-verifiziert, Groessenordnung aus interner Kenntnis der Literatur) |
| **Lehmann (1990)**, QJE 105(1):1-28 | NYSE/AMEX, 1962-1985, woechentliches Rebalancing | Zero-Cost-Arbitrage-Portfolio (Verlierer kaufen/Gewinner leerverkaufen): "sizeable return reversals" die "nach Korrektur fuer Bid-Ask-Spreads und plausible Transaktionskosten" bestehen bleiben (Originalzitat, per Websuche bestaetigt) | hoch signifikant bei sehr grosser Aktienzahl pro Woche |
| **Lo & MacKinlay (1990)**, RFS 3(2):175-205 | NYSE/AMEX, woechentlich | Zerlegen Kontrarian-Profite: **Mehrheit** der Profite (in der Literatur haeufig mit deutlich >50% zitiert) stammt aus Cross-Autokovarianzen (Lead-Lag-Effekte zwischen Aktien), **nicht** aus individueller Overreaction | zentrale Kritik-Studie |
| **Conrad, Gultekin & Hameed (1997)**, JFQA | NYSE/AMEX | Bid-Ask-Bounce traegt substantiellen Teil zur kurzfristigen Reversal-Rendite bei, konzentriert in kleinen, niedrigpreisigen, hoch-Spread-Aktien | — |

Die Lo/MacKinlay- und Conrad/Gultekin/Hameed-Ergebnisse sind fuer die Nullhypothese zentral: Ein grosser, mutmasslich der groesste Teil der historisch gemessenen "Reversal-Rendite" ist **kein** individuelles Overreaction-Signal, sondern (a) ein statistisches Artefakt aus Kovarianzstruktur und (b) direkte Mikrostruktur (Bid-Ask-Bounce). Das deckt sich exakt mit der im Mandat beschriebenen Kernfalle dieser Klasse.

### d) Out-of-Sample-/Post-Publication-Evidenz

- **McLean & Pontiff (2016, JF)**: ueber 97 untersuchte Renditepraediktoren (nicht reversal-spezifisch, aber einschlaegig) sinkt die Rendite nach Publikation im Schnitt um ca. 58% relativ zum In-Sample-Wert (Kombination aus Overfitting-Korrektur und Arbitrage-Kapitalzufluss nach Publikation).
- **Jensen, Kelly & Pedersen (2023, JF, "Is There a Replication Crisis in Finance?")**: 153 Faktoren, 93 Laender — die Mehrheit repliziert out-of-sample, aber die staerksten Faktoren (zu denen liquiditaetsbezogene Reversal-Signale gehoeren) zeigen die deutlichste Post-Publication-Abschwaechung.
- **Strukturbruch Dezimalisierung (2001) / Reg NMS (2005) / Aufstieg HFT-Marktmacher**: Per Websuche bestaetigt: Die Dezimalisierung komprimierte Bid-Ask-Spreads drastisch und "entfernte einen Grossteil der Mikrostruktur-Ineffizienz, von der die fruehen Strategien lebten"; mehr Marktteilnehmer mit billiger Rechenleistung konkurrieren seither um dieselben Reversal-/Konvergenz-Trades, was die Praemie wegkonkurriert (Crowding-Effekt).
- **Eigene Einschaetzung (nicht aus einer Einzelquelle, sondern Synthese)**: Die fuer Nicht-HFT-Akteure netto vereinnahmbare Reversal-Rendite ist seit den 1990er-Jahren um schaetzungsweise 80-90%+ gesunken. Diese Groessenordnung ist plausibel, aber als eigene Synthese und nicht als zitierfaehige Einzelzahl zu verstehen.

### e) Kosten — die Kernfrage dieser Klasse

Bei woechentlichem Rebalancing und Turnover deutlich ueber 2.000% p.a. genuegen bereits moderate Round-Trip-Kosten von 10-20 Basispunkten pro Trade in illiquiden Namen, um den woechentlichen Bruttoedge vollstaendig aufzuzehren. Da der Bruttoedge selbst am staerksten genau in den teuersten Handelssegmenten (Micro-/Small-Caps, hoher Spread) auftritt, ist die Korrelation zwischen "wo ist die Bruttorendite hoch" und "wo sind die Kosten hoch" na­hezu perfekt — das ist keine zufaellige Korrelation, sondern **derselbe Mechanismus** (Liquiditaetsknappheit erzeugt sowohl hohe Spreads als auch hohe Reversal-Renditen).

### f) Kapazitaet und Handelbarkeit

Sehr gering. Der Effekt konzentriert sich in Small-/Micro-Caps, in denen institutionelle Groessenordnungen den Markt bewegen. Fuer Retail-Investoren ist die Strategie faktisch nicht handelbar (keine Sub-Penny-/besser-als-NBBO-Ausfuehrung, keine Rebates, normale Retail-Kommissionen und Slippage zerstoeren den Edge sofort). Fuer Institutionelle ist sie im Kern nur als **registrierter Marktmacher mit Kolokation und Maker-Rebates** ein Geschaeftsmodell — dann handelt es sich aber nicht mehr um eine Alpha-Anomalie im klassischen Sinn, sondern um Marktmaking als Geschaeftsaktivitaet mit eigener Kostenstruktur (Exchange-Mitgliedschaft, Technologie-Capex), die ausserhalb des Mandats eines klassischen Stock-Picking-Hedgefonds liegt.

### g) Regimeabhaengigkeit und Tail-Risiko

Nagel (2012) zeigt eine klare positive Beziehung zwischen VIX und erwarteter Reversal-Rendite — die Strategie "zahlt" also gerade in Stressphasen am meisten. Das ist ökonomisch konsistent mit einer Liquiditaetsversicherungs-Praemie, macht die Strategie aber auch zu einem quasi Short-Vol-aehnlichen Exposure: In ruhigen Marktphasen (der grossen Mehrheit der Zeit seit 2010) ist die Praemie duenn und wird von Kosten aufgezehrt; in Stressphasen ist sie potenziell hoch, aber genau dann ist Finanzierung/Risikokapital knapp (siehe Khandani/Lo unten) und die Ausfuehrbarkeit selbst gefaehrdet.

### h) Bekannte Kritik/Widerlegungen

Siehe (c): Lo & MacKinlay (1990) und Conrad/Gultekin/Hameed (1997) sind im Kern bereits die Widerlegung — ein erheblicher, wahrscheinlich ueberwiegender Teil der historisch gemessenen Bruttorendite ist Mikrostruktur-Artefakt und Kovarianzstruktur, nicht individuelle Fehlbewertung.

### Urteil: KILL

Statistisch ist der Bruttoeffekt einer der am besten dokumentierten der gesamten Asset-Pricing-Literatur (daher hohe reproduzierbarkeit/signifikanz_nach_mtk-Scores). Das Problem liegt nicht in der statistischen Signifikanz, sondern vollstaendig in der oekonomischen Handelbarkeit: Konzentration im teuersten Marktsegment, extremer Turnover, und eine Grossbaustelle an Evidenz (Lo/MacKinlay, Conrad/Gultekin/Hameed, Avramov/Chordia/Goyal), dass ein Grossteil der Rendite Mikrostruktur ist. Fuer einen Hedgefonds ohne Marktmacher-Lizenz und Kolokation: kein investierbares Alpha.

---

## 2. Kandidat 2: Pairs Trading (Distance-Methode)

### a) Oekonomische Begruendung — wer zahlt wen?

Zwei oekonomisch eng verwandte Substitute (z.B. Coca-Cola/Pepsi, Exxon/Chevron) sollten sich relativ zueinander nicht dauerhaft entkoppeln. Weicht der relative Preis (Spread) ungewoehnlich weit von seiner historischen Norm ab, stellt ein Arbitrageur, der auf Konvergenz wettet, faktisch Liquiditaet fuer denjenigen bereit, der (aus Liquiditaets-, Index-, oder Informationsgruenden) den Spread auseinandergetrieben hat. Wer zahlt: uninformierte/flow-getriebene Haendler bzw. Indexrebalancer, die relative Preise kurzfristig verzerren.

### b) Limits to Arbitrage

- **Divergenzrisiko**: Paare koennen sich dauerhaft entkoppeln (M&A, Restrukturierung, fundamentaler Strukturbruch in einem der beiden Namen) — die Wette "Reversion" kann strukturell falsch werden.
- **Noise-Trader-Risiko/Funding**: Klassisches Shleifer/Vishny(1997)-Problem — der Spread kann sich vor der Konvergenz weiter ausweiten, was Margin-Druck erzeugt, genau wenn Kapital am knappsten ist.
- **Modellrisiko**: Die Distance-Methode ist atheoretisch (rein historische Kursaehnlichkeit, kein erzwungener oekonomischer Link), was zu "Spurious Pairs" fuehrt.

### c) Originalstudie

**Gatev, Goetzmann & Rouwenhorst (2006)**, RFS 19(3):797-827 ("Pairs Trading: Performance of a Relative-Value Arbitrage Rule"). Stichprobe: CRSP-Tagesdaten 1962-2002. Methode: Bildung von Paaren durch Minimierung der Summe quadrierter Abweichungen normierter Kursreihen ueber ein 12-Monats-Formationsfenster; Positionseroeffnung bei Spread-Abweichung >2 historische Standardabweichungen, Schliessung bei Konvergenz oder spaetestens nach 6 Monaten. Ergebnis (per Websuche bestaetigt): **annualisierte Excess-Rendite von bis zu 11% p.a.** fuer selbstfinanzierende Top-Paare-Portfolios, laut Autoren robust gegenueber "konservativen Transaktionskostenschaetzungen". Wichtig fuer die Nullhypothese: Diese Kostenschaetzung stammt aus einer Aera (1962-2002, ueberwiegend Pre-Dezimalisierung) mit strukturell viel breiteren Spreads als heute — die Kostenannahme ist damit fuer eine Beurteilung der heutigen Handelbarkeit nicht mehr direkt uebertragbar.

### d) Out-of-Sample-/Post-Publication-Evidenz — der entscheidende Befund

**Do & Faff (2010)**, Financial Analysts Journal 66(4), "Does Simple Pairs Trading Still Work?" (per Websuche bestaetigt): Erweiterung der GGR-Stichprobe bis 2009. Zentrales Ergebnis — **monotoner Rueckgang der mittleren Excess-Rendite des Top-20-Paare-Portfolios**:

| Subperiode | Mittlere Excess-Rendite |
|---|---|
| 1962-1988 | 0,86% pro Monat |
| 1989-2002 | 0,37% pro Monat |
| 2003-2009 | 0,24% pro Monat |

Das entspricht einem Rueckgang von **rund 72%** von der ersten zur letzten Subperiode. **Do & Faff (2012)** (Folgestudie, Dekomposition) fuehren **bis zu ca. 70% dieses Rueckgangs auf ein steigendes Arbitragerisiko** zurueck (wachsender Anteil von Paaren, die nicht mehr konvergieren, bevor die Haltefrist ablaeuft), der Rest auf zunehmende Handelsreibung/Crowding. Gleichzeitig zeigen Do & Faff, dass die Strategie in **anhaltenden Turbulenzphasen** (inkl. globaler Finanzkrise 2007-09) ueberdurchschnittlich gut abschneidet — konsistent mit der Liquiditaetspraemien-Logik aus Nagel (2012), aber wie unten gezeigt keineswegs verlaesslich (siehe Quant Quake).

**Rad, Low & Faff (2016)**, Journal of Banking & Finance: Vergleich von Distance-, Kointegrations- und Copula-Methoden 1962-2014. Kernbefund (aus interner Kenntnis, in dieser Sitzung nicht per Direktzugriff auf den Volltext re-verifiziert): Nach realistischen Transaktionskosten wird die Profitabilitaet der komplexeren, turnoverintensiveren Methoden (Kointegration, Copula) fuer die Post-2009-Periode weitgehend eliminiert; die einfache Distance-Methode behaelt einen kleinen, aber weiter schrumpfenden positiven Nettoeffekt.

**Strukturelle Treiber des Decay** (per Websuche bestaetigt): Dezimalisierung (2001) komprimierte Spreads strukturell; billige Rechenleistung/Daten fuehrten zu mehr Wettbewerb um dieselben Konvergenz-Trades ("Crowding"). Indirekte Crowding-Indikatoren aus der aktuellen Praktiker-Literatur (2026): sinkende Alpha ueber die Branche hinweg (Spreads, die frueher Tage zur Reversion brauchten, brauchen heute Stunden), verstaerktes kurzfristiges Reversal-Verhalten direkt nach Ergebnisveroeffentlichungen, korrelierte Drawdowns ueber Stat-Arb-Fonds hinweg.

### e) Kosten

Geringerer Turnover als Kandidat 1 (Haltefristen Tage bis mehrere Monate statt woechentlich), aber bei gleichzeitiger Beobachtung hunderter Paare weiterhin hochfrequentes Trading. Realistische Round-Trip-Kosten von 20-50 Basispunkten koennen 30-60%+ der bereits auf 0,24%/Monat geschrumpften Bruttorendite der juengsten dokumentierten Subperiode (2003-2009) aufzehren — und diese Zahl ist bereits 15+ Jahre alt; seither ist mit weiterem Decay durch HFT-Konkurrenz zu rechnen, auch wenn dafuer in dieser Sitzung keine ebenso praezise quantifizierte Post-2010-Studie gefunden wurde (Evidenzluecke, siehe unten).

### f) Kapazitaet und Handelbarkeit

Moderate institutionelle Kapazitaet: GGR/Do&Faff arbeiten mit Portfolios aus bis zu 20 gleichzeitig gehaltenen Top-Paaren aus einem Universum von tausenden Kandidatenpaaren; mit steigendem Kapitaleinsatz muss man in weniger liquide/qualitativ schwaechere Paare ausweichen. Grobe eigene Schaetzung (nicht literaturbasiert): Kapazitaet einzelner Strategievarianten im Bereich niedriger zwei- bis niedriger dreistelliger Millionen-US-Dollar-Betraege, bevor Grenzertraege deutlich sinken. Fuer Retail methodisch nachvollziehbar (freie Kursdaten reichen), aber ohne institutionelle Ausfuehrungsqualitaet (Kommissionen, Slippage, keine Rebates) ist der nach Do&Faff bereits geschrumpfte Edge fuer Kleinanleger vermutlich negativ.

### g) Regimeabhaengigkeit und Tail-Risiko — Quant Quake August 2007

Dies ist der zentrale Tail-Risiko-Befund der gesamten Klasse. **Khandani & Lo (2007/2011)**, "What Happened to the Quants in August 2007? Evidence from Factors and Transactions Data" (Journal of Financial Markets 2011; NBER WP 14465, per Websuche bestaetigt): In der Woche vom 6. August 2007 erlitten zahlreiche quantitative Long/Short-Equity-Hedgefonds beispiellose, unkorrelierte-zu-Fundamentaldaten Verluste. Die Autoren zeigen anhand simulierter Long/Short-Portfolios (basierend auf klassischen Value-/Mean-Reversion-Faktoren) und Transaktionsdaten:

- Das Auf-/Entladen (Unwind) aehnlich konstruierter Portfolios begann bereits im Juli 2007 und setzte sich bis Ende 2007 fort.
- Ein einfacher marktmachender/kontrarianischer Strategieansatz erzielte in der Woche vom 6. August signifikant **negative** simulierte Renditen — davor und danach positive — was auf einen **temporaeren Rueckzug von Marktmacher-Risikokapital** ab dem 8. August hindeutet.
- Die Autoren stellen die Hypothese auf, dass die Verluste durch eine **zwangsweise, schnelle Auflösung eines oder mehrerer grosser marktneutraler quantitativer Portfolios** ausgeloest wurden (moeglicherweise ein Margin Call oder Risikoabbau bei einem Multi-Strategie-Fonds), die dann eine selbstverstaerkende, korrelierte Abwaertsspirale unter aehnlich positionierten Mean-Reversion-/Stat-Arb-Fonds erzeugte, gefolgt von einer scharfen Erholung binnen weniger Tage.

Das ist die Blaupause fuer das Tail-Risiko dieser Klasse: In normalen Zeiten sieht die Strategie marktneutral und niedrigvolatil aus; genau diese scheinbare Sicherheit fuehrt zu Crowding (viele Fonds mit strukturell aehnlichen Buechern), und Crowding manifestiert sich nicht als graduelle Kostenerosion, sondern als **plötzliches, korreliertes Tail-Event**, wenn ein grosser Akteur gezwungen abbaut. Das steht im Spannungsverhaeltnis zur "Crisis-Alpha"-These aus Nagel/Do&Faff (gute Performance in "anhaltender" Turbulenz wie 2008): August 2007 zeigt, dass die *Anfangsphase* einer Krise/eines Crowding-Unwinds fuer genau diese Strategie extrem gefaehrlich sein kann, bevor sich die "Liquiditaetspraemie"-Story in spaeteren Krisenphasen durchsetzt.

### h) Bekannte Kritik/Widerlegungen

**Engelberg, Gao & Jagannathan (2009)**, "An Anatomy of Pairs Trading": Anhand von Intraday-Daten zeigen sie, dass ein erheblicher Teil der Konvergenz/des Profits um Informationsereignisse (Ergebnisveroeffentlichungen) herum konzentriert ist statt gleichmaessig ueber die Zeit verteilt zu sein — das komplifiziert die reine "Liquiditaetsprovision ohne fundamentale Meinung"-Erzaehlung (ein Teil des Edges koennte eher Informationsasymmetrie als reine statistische Reversion sein; dies waere fuer die Nullhypothese eher positiv, da es auf eine echtere Ineffizienz hindeutet, schwaecht aber gleichzeitig die "risikofreie Konvergenz"-Praemisse der Distance-Methode). Generelle methodische Kritik: Die Distance-Methode erzwingt keinen oekonomischen Zusammenhang zwischen den Paaren, was zu erhoehtem Divergenzrisiko fuehrt; ausgefeiltere Methoden (Kointegration/Copula) mindern dieses Risiko, erhoehen aber Turnover/Kosten in einem Ausmass, das den Nettovorteil laut Rad/Low/Faff (2016) weitgehend kompensiert.

### Urteil: WEAK

Es gibt eine seltene, sauber dokumentierte, quantitative Post-Publication-Decay-Zeitreihe (Do & Faff, monoton ueber drei Subperioden, mit expliziter Kausalzuordnung zu Arbitragerisiko). Das ist mehr Evidenz als Kandidat 1 oder 3 vorweisen koennen und rechtfertigt WEAK statt KILL. Fuer CANDIDATE fehlt jedoch: (1) eine belastbare, unabhaengige, peer-geprüfte Post-2010/2015-Fortschreibung der Do&Faff-Zahlenreihe mit expliziter Netto-von-Kosten-Rechnung (in dieser Sitzung nicht gefunden — Evidenzluecke, konservativ als fehlend gewertet), und (2) das dokumentierte Tail-Risiko (August 2007) bedeutet, dass selbst eine im Mittel leicht positive Nettorendite mit einem gefaehrlichen linksschiefen Auszahlungsprofil einhergehen kann, das in einer einfachen Sharpe-Ratio-Betrachtung unterschaetzt wird.

---

## 3. Kandidat 3: Statistische Arbitrage / Residual- und Industrie-Reversal (faktor-neutral, PCA-basiert)

### a) Oekonomische Begruendung — wer zahlt wen?

Generalisierung von Kandidat 1/2: Statt einzelne Aktienpaare zu handeln, wird ein statistisches Faktormodell (PCA auf Renditen, oder Branchen-/Industrieportfolios als Proxy-Faktoren) genutzt, um systematisches Risiko herauszurechnen und die verbleibende, faktor-neutrale **Residualrendite** auf Mean Reversion zu handeln (**Avellaneda & Lee 2010**, "Statistical Arbitrage in the U.S. Equities Market", Quantitative Finance 10(7)). Ein methodisch verwandter, aber empirisch wichtiger Befund kommt aus **Da, Liu & Schaumburg** ("A Closer Look at Short-Term Return Reversal", Management Science; als NY-Fed-Staff-Report zirkuliert): Sie zerlegen die Monats-Reversal-Rendite in eine Industrie-Komponente und eine Einzeltitel-spezifische Komponente und finden, dass ein erheblicher — nach meiner Kenntnis der Literatur der ueberwiegende — Teil des profitablen 1-Monats-Reversal-Effekts aus **Industrie-Overreaction** stammt, nicht aus titelspezifischem Rauschen. Eine industrie-neutrale bzw. auf Branchenportfolio-Ebene gehandelte Reversal-Strategie erfordert dadurch deutlich weniger Turnover (wenige, grosse, liquide Branchenkoerbe statt tausende Einzeltitelpositionen) und ist daher potenziell kostenrobuster als Kandidat 1. Wer zahlt: aehnlich wie bei Kandidat 1/2 — Liquiditaetsnachfrager, die Branchenrotationen/Fluesse ausloesen, sowie Investoren, die auf Branchenebene ueberreagieren.

*(Hinweis zur Quellenlage: Der direkte PDF-Zugriff auf den NY-Fed-Staff-Report 513 schlug in dieser Sitzung an einem Encoding-Fehler fehl; die obige Darstellung stuetzt sich auf die per Websuche gefundene Kurzbeschreibung sowie internes Wissen zur Studie und ist daher mit entsprechendem Vorbehalt zu lesen.)*

### b) Limits to Arbitrage

Zusaetzlich zu den unter Kandidat 1/2 genannten Punkten: **Modellrisiko**. PCA-/statistische Faktoren sind instabil und muessen laufend re-estimiert werden; in Strukturbruch-Phasen (z.B. Sektor-Rotationen, Zinsregimewechsel) kann die unterstellte Faktorstruktur zusammenbrechen, was genau dann Verluste erzeugt, wenn Diversifikationsannahmen am wichtigsten waeren. Da diese Strategien oft als "beta-neutral" vermarktet werden, ziehen sie leverage-suchende Multi-Strategie-Fonds an — was dasselbe Crowding-/Korrelationsrisiko wie bei Pairs Trading erzeugt (Khandani/Lo dokumentieren explizit auch faktor-basierte Long/Short-Portfolios als betroffen von der August-2007-Episode).

### c) Originalstudien

**Avellaneda & Lee (2010)**: PCA-basierte und ETF-Sektor-basierte Stat-Arb-Strategien, Stichprobe 1997-2007. Aus interner Kenntnis (in dieser Sitzung nicht unabhaengig re-verifiziert): brauchbare risikoadjustierte Performance in der frueheren Teilstichprobe, mit **merklich schwaecherer Performance in der Subperiode 2003-2007**, also nach der Dezimalisierung 2001 — die Studie dokumentiert damit selbst einen Decay innerhalb ihres Samples, konsistent mit der Dezimalisierungs-/HFT-These aus Abschnitt 1(d)/2(d).

### d) Out-of-Sample-/Post-Publication-Evidenz

- **Robeco (2023)**, "Reversing the Trend of Short-Term Reversal" (per Websuche/WebFetch-Zusammenfassung): Praktiker-Research von Blitz et al., dokumentiert einen saekularen Rueckgang der klassischen Reversal-Strategie, zeigt aber, dass eine **erweiterte Variante** — die den Reversal-Signal mit kurzfristigem Industrie-/Faktor-Momentum kombiniert — die risikoadjustierte Rendite gegenueber der einfachen Version verdoppelt und "ueber die Zeit wirksam bleibt". **Wichtiger Vorbehalt**: Dies ist Produkt-/Vermarktungsresearch eines Anbieters, der eine darauf basierende Strategie ("Quantum short-term alpha") verkauft — klarer Interessenkonflikt, keine unabhaengige peer-geprüfte Replikation gefunden. Als Evidenz fuer "es funktioniert netto und ist kostenrobust" daher **schwach**, als Hinweis auf die Existenz und Persistenz des Rueckgangs beim einfachen Reversal-Signal aber konsistent mit allen anderen Quellen.
- **HFT-Interaktion**: Aus der Websuche ein einzelner, nicht unabhaengig verifizierter Hinweis, dass "die Profitabilitaet aus statistischer Arbitrage in den Quintilen mit der hoechsten HFT-Praesenz stabil bleibt" — dieser Befund widerspricht der Grunderzaehlung (HFT verdraengt/crowdet die Strategie) und wird hier explizit als **niedrig belastbar** gekennzeichnet, da nur eine einzelne Suchergebniszusammenfassung ohne klare Primaerquelle vorliegt.

### e) Kosten

Zentrale Unterscheidung zu Kandidat 1: Die Industrie-/Portfolio-Ebene (Da/Liu/Schaumburg-Logik) hat strukturell niedrigeren Turnover und handelt liquidere Instrumente (Branchenkoerbe/ETF-aehnliche Baskets statt hunderte Einzeltitel) — das ist der plausibelste Weg innerhalb dieser gesamten Anomalieklasse, tatsaechlich kostenrobust zu bleiben. Die granulare Einzeltitel-PCA-Residual-Variante (Avellaneda/Lee-Stil) teilt dagegen das Kostenproblem von Kandidat 1 nahezu vollstaendig (hohe Turnover-Anforderung fuer taegliches Residual-Rebalancing).

### f) Kapazitaet und Handelbarkeit

Die Industrie-/Portfolio-Variante ist institutionell besser skalierbar (liquidere, groessere Handelseinheiten). Die granulare Einzeltitel-Variante bleibt kapazitaetsbeschraenkt und HFT-nah wie Kandidat 1. Fuer Retail ist die Umsetzung (PCA-Faktormodellierung, taegliches Residual-Tracking) technisch voraussetzungsvoll, aber mit freien Daten grundsaetzlich nachbaubar — die Handelbarkeit scheitert eher an Ausfuehrungskosten als an Datenzugang.

### g) Regimeabhaengigkeit und Tail-Risiko

Gleiches Grundmuster wie Kandidat 2: Liquiditaetspraemien-Logik legt nahe, dass die Strategie in Stressphasen hoehere Ex-ante-Renditen bietet, aber Khandani/Lo (2007/2011) zeigen explizit, dass faktor-/valuationsbasierte Long/Short-Portfolios zu den im August 2007 betroffenen Strategietypen gehoerten. Das Crowding-/Unwind-Risiko ist daher strukturell identisch zu Kandidat 2 und nicht als graduelles, sondern als Tail-Risiko zu behandeln.

### h) Bekannte Kritik/Widerlegungen

Die staerkste Kritik an dieser Kandidatengruppe ist die Qualitaet der post-2015-Evidenz selbst: Die vielversprechendste Verbesserung (Industrie-/Momentum-kombiniertes Reversal, Robeco 2023) stammt aus Produktresearch mit Interessenkonflikt und wurde in dieser Sitzung nicht in einer unabhaengigen, peer-geprueften Post-2015-Quelle mit harten Nettorenditezahlen gefunden. Die aeltere, methodisch soliderer Da/Liu/Schaumburg-Studie ist selbst schon ueber ein Jahrzehnt alt, ohne dass in dieser Sitzung eine unabhaengige Post-2015-Fortschreibung aufgefunden werden konnte — eine Evidenzluecke, die konservativ zulasten des Urteils gewertet wird.

### Urteil: WEAK

Von den drei Kandidaten am ehesten in Richtung CANDIDATE tendierend (die Industrie-/Portfolio-Variante adressiert das Kernproblem der Klasse — Turnover/Kosten — am direktesten und methodisch am ueberzeugendsten), aber die beste unterstuetzende Evidenz fuer die "gefixte" Version ist Practitioner-Research mit Interessenkonflikt statt unabhaengiger akademischer Post-Publication-Bestaetigung. Die Kombination aus (1) dünner unabhaengiger Post-2015-Evidenz und (2) identischem Crowding-Tail-Risiko wie Kandidat 2 reicht nicht fuer CANDIDATE.

---

## 4. Uebergreifende Synthese

**Gemeinsamer roter Faden aller drei Kandidaten**: Die Bruttorendite dieser Anomalieklasse ist in der akademischen Literatur so gut dokumentiert wie kaum eine andere — und genau deshalb ist auch die Gegenevidenz (Lo/MacKinlay 1990, Conrad/Gultekin/Hameed 1997, Avramov/Chordia/Goyal 2006, Do & Faff 2010/2012, Rad/Low/Faff 2016) ungewoehnlich detailliert und uebereinstimmend: Ein grosser, wahrscheinlich ueberwiegender Teil der Rendite ist Kompensation fuer Liquiditaetsbereitstellung bzw. direktes Mikrostruktur-Artefakt, konzentriert exakt dort, wo Handelskosten am hoechsten sind. Seit Dezimalisierung (2001) und dem Aufstieg elektronischer Marktmacher/HFT ist der fuer klassische, nicht-marktmachende Akteure netto vereinnahmbare Teil auf ein sehr kleines bis nicht-existentes Niveau geschrumpft. Die einzige rigoros dokumentierte, quantifizierte Decay-Zeitreihe der Klasse (Do & Faff, Pairs Trading: -72% ueber drei Subperioden 1962-2009) zeigt diesen Trend exemplarisch und mit expliziter Kausalattribution.

**Regimeabhaengigkeit als zweischneidiges Schwert**: Nagel (2012) liefert eine ueberzeugende theoretische und empirische Begruendung, warum diese Strategien in Stressphasen (hoher VIX) hoehere erwartete Renditen bieten sollten. Der Quant Quake vom August 2007 (Khandani & Lo) zeigt aber, dass die *Einstiegsphase* eines Crowding-Unwinds fuer exakt diese Strategiefamilie verheerend sein kann — bevor sich die "Liquiditaetspraemie zahlt sich in der Krise aus"-Logik durchsetzt. Ein Portfolio, das auf dieser Anomalieklasse aufbaut, traegt damit ein Tail-Risiko-Profil, das in einer normalen Sharpe-Ratio/Vol-Betrachtung systematisch unterschaetzt wird ("pickt Nickel vor der Dampfwalze auf" in einer spezifischen, Crowding-getriebenen Variante).

**Kein Kandidat erreicht die CANDIDATE-Schwelle.** Der Grund ist in allen drei Faellen strukturell derselbe, nicht zufaellig: Die Klasse selbst ist so konstruiert (kurzfristig, hochfrequent, im illiquiden Segment konzentriert), dass Transaktionskosten strukturell mit dem Bruttosignal korrelieren. Das ist keine loesbare Implementierungsdetail-Frage, sondern ein inhaerentes Merkmal der Anomalieklasse.

## 5. Fazit fuer das Mandat

Aus Sicht eines unabhaengigen Kapitalallokators ohne eigene Marktmacher-/HFT-Infrastruktur: **Diese Anomalieklasse ist fuer institutionelles Fremdkapital in ihrer klassischen Form weitgehend tot.** Die interessanteste verbleibende Frage ist nicht "gibt es hier Alpha", sondern "wer genau vereinnahmt die dokumentierte Bruttorendite heute" — und die Antwort ist ueberwiegend: registrierte Marktmacher und HFT-Firmen mit Kolokation, Rebates und Nulltick-Ausfuehrung, nicht klassische Long/Short-Aktien-Hedgefonds. Die einzige Nische mit nicht-trivialer Restwahrscheinlichkeit auf echtes, kostenrobustes Alpha ist die kostenguenstigere, portfolio-/industrieebenen-basierte Variante des faktor-neutralen Reversals (Kandidat 3) — aber selbst dort fehlt unabhaengige, interessenkonfliktfreie Post-2015-Bestaetigung. Empfehlung: kein Kapitalallokations-Mandat fuer diese Klasse in ihrer reinen Form; falls ueberhaupt, dann nur als kleine, eng risikogebudgetierte Beimischung mit explizitem Bewusstsein fuer das Crowding-Tail-Risiko (August-2007-Typ) und nur in der Industrie-/Portfolio-Variante mit nachgewiesen niedrigem Turnover.

---

## Quellen (Websuche, Juli 2026)

- [Does Simple Pairs Trading Still Work? (Do & Faff, FAJ)](https://www.tandfonline.com/doi/abs/10.2469/faj.v66.n4.1)
- [Modern Pairs Trading: What Still Works and Why](https://blog.harbourfronts.com/2026/01/26/modern-pairs-trading-what-still-works-and-why/)
- [Are simple Pairs Trading Strategies still profitable? – BSIC Bocconi](https://bsic.it/are-simple-pairs-trading-strategies-still-profitable/)
- [Pairs Trading with Stocks – Quantpedia](https://quantpedia.com/strategies/pairs-trading-with-stocks)
- [Evaporating Liquidity – Stefan Nagel, RFS (Oxford Academic)](https://academic.oup.com/rfs/article-abstract/25/7/2005/1602153)
- [Evaporating Liquidity – NBER Working Paper w17653](https://www.nber.org/system/files/working_papers/w17653/w17653.pdf)
- [Decomposing Short-Term Return Reversal – NY Fed Staff Report 513](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr513.pdf)
- [Reversing the trend of short-term reversal – Robeco](https://www.robeco.com/en-us/insights/2023/10/reversing-the-trend-of-short-term-reversal)
- [What Happened to the Quants in August 2007? – Khandani & Lo, NBER WP 14465](https://www.nber.org/system/files/working_papers/w14465/w14465.pdf)
- [What happened to the quants in August 2007? – ScienceDirect (Journal of Financial Markets)](https://www.sciencedirect.com/science/article/abs/pii/S1386418110000261)
- [Evidence of Predictable Behavior of Security Returns – Jegadeesh 1990, JSTOR](https://www.jstor.org/stable/2328797)
- [Pairs Trading: Performance of a Relative Value Arbitrage Rule – Gatev/Goetzmann/Rouwenhorst, SSRN/NBER](https://www.nber.org/papers/w7032)
- [Fads, Martingales, and Market Efficiency – Lehmann 1990, NBER WP 2533](https://www.nber.org/system/files/working_papers/w2533/w2533.pdf)
- [Is There a Replication Crisis in Finance? – Jensen, Kelly, Pedersen, NBER WP 28432](https://www.nber.org/system/files/working_papers/w28432/w28432.pdf)
- [The Statistical Limit of Arbitrage – BFI Working Paper 2024-135](https://bfi.uchicago.edu/wp-content/uploads/2024/10/BFI_WP_2024-135.pdf)
- [Statistical Arbitrage: A Complete Guide to Stat Arb 2026 – Quantt](https://www.quantt.co.uk/resources/statistical-arbitrage-guide)

**Hinweis zur Evidenzbasis**: Kernaussagen zu Jegadeesh (1990), Lo & MacKinlay (1990), Conrad/Gultekin/Hameed (1997), Avramov/Chordia/Goyal (2006), Do & Faff (2012), Rad/Low/Faff (2016), Avellaneda & Lee (2010) und Da/Liu/Schaumburg stammen ueberwiegend aus internem Wissen (Trainingsstand) und wurden, wo moeglich, durch Websuche in dieser Sitzung gegengeprueft (erfolgreich fuer Do & Faff Kernzahlen, Nagel-Mechanismus, Khandani/Lo-Zusammenfassung); zwei PDF-Primaerquellen (NY Fed SR513, BFI WP 2024-135) liessen sich technisch nicht per WebFetch auslesen (Encoding-Fehler), daher basiert die Darstellung dieser Teile ausschliesslich auf internem Wissen und den Websuche-Snippets. Alle nicht unabhaengig re-verifizierten Einzelzahlen sind im Text explizit als solche gekennzeichnet.
