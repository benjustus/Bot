```yaml
agent: 04
klasse: "Spin-offs & Abspaltungen"
websuche_verfuegbar: ja
strategien:
  - name: "Post-Spin-off Kursdrift der abgespaltenen Tochtergesellschaft (Spinoff Subsidiary Drift)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.30
    netto_sharpe_erwartung: "0.0-0.2"
    kernrisiko: "Rechtsschiefe Renditeverteilung (Median bei 36 Monaten negativ trotz positivem Mittelwert); negatives Crash-Beta (2008: ETF -55.2%, Subsidiary-Basket -41.1% vs. Markt -38.1%); reales investierbares Vehikel (CSD-ETF) zeigt seit ca. 2013 Konvergenz auf Marktrendite netto Kosten"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "CSD (Invesco/Guggenheim S&P Spin-Off ETF, Kurshistorie z.B. Yahoo Finance) als investierbarer Proxy; Ken-French 25 Size-B/M-Portfolios als Benchmark"
  - name: "Post-Spin-off Kursdrift des Mutterkonzerns (Parent Drift)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 1
      signifikanz_nach_mtk: 1
      regimestabilitaet: 2
      handelbarkeit: 4
      kapazitaet: 4
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.05
    netto_sharpe_erwartung: "~0.0"
    kernrisiko: "Kein robuster Effekt außerhalb der Originalstichprobe; Originalergebnis nachweislich durch einen einzelnen Extremausreißer getrieben (McConnell/Ovtchinnikov 2004); in jeder Out-of-Sample-Replikation seit 2001 statistisch insignifikant bzw. sogar negativ im Punktschätzer (t=-0.48 bis 0.72)"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken-French 25 Size-B/M-Portfolios + manuell erhobene Parent-Ticker via SEC EDGAR (Form 10 / 8-K); CRSP-Distributionsdatei selbst nicht frei verfügbar"
```

# Agent 04 — Spin-offs & Abspaltungen: Adversarial Review

**Nullhypothese:** Es gibt kein handelbares Netto-Alpha in der Klasse "Spin-offs". Ziel dieses Berichts ist die Falsifikation dieser Nullhypothese anhand der akademischen Literatur, nicht deren Bestätigung.

**Evidenzbasis:** Websuche funktionierte (WebSearch/WebFetch verfügbar) und wurde für alle zentralen Aussagen genutzt, inkl. Volltext-Extraktion aus dem Originalpapier McConnell/Sibley/Xu (2015). Wo Primärquellen nicht direkt zugänglich waren (z.B. Cusatis/Miles/Woolridge 1993 Volltext, Desai/Jain 1999 Volltext hinter Paywall), stützt sich die Darstellung auf Sekundärzitate aus mehreren unabhängigen Treffern plus internes Wissen; das ist explizit gekennzeichnet.

---

## Kandidat 1: Post-Spin-off Kursdrift der abgespaltenen Tochtergesellschaft ("Subsidiary Drift")

### a) Ökonomische Begründung

Drei sich ergänzende Erklärungen werden in der Literatur genannt:

1. **Forced Selling / struktureller Zwang durch Indexfonds und Mandatsrestriktionen.** Wenn ein Mutterkonzern (z.B. ein S&P-500-Mitglied) eine Tochter abspaltet, erhalten Aktionäre pro rata Aktien der neuen, meist deutlich kleineren Einheit. Diese neue Aktie ist zunächst in keinem relevanten Index enthalten. Index-gebundene Fonds und viele Mandate mit Marktkapitalisierungs- oder Index-Restriktionen (Großraum-Fonds, die nur S&P-500-Titel halten dürfen) sind gezwungen, die neuen Spin-off-Aktien unmittelbar und größenunabhängig vom Preis zu verkaufen — ein klassischer "urteilsfreier", nicht-informationsbasierter Verkaufsdruck.
2. **Neglected-Firm-Hypothese / Informationsasymmetrie.** Die Tochter hat keine eigene Analysten-Coverage, keine mehrjährige öffentliche Finanzhistorie, keinen Gewinnkonsens. Institutionelle, auf Coverage angewiesene Investoren meiden die Position, wodurch sich Fehlbewertung langsamer korrigiert.
3. **Anreiz-/Fokus-Realignment.** Management der neuen, unabhängigen Einheit ist ökonomisch direkter an den eigenen Aktienkurs gekoppelt (Optionen, Boni), was tatsächliche operative Verbesserungen auslösen kann (Desai & Jain 1999 zeigen dies primär für "focus-increasing" Spin-offs).

Verursacher der Fehlbewertung sind also primär **gezwungene, nicht-preissensitive Verkäufer** (Indexfonds, Mandats-gebundene Fonds) auf der Angebotsseite, denen auf der Nachfrageseite zu wenig informierte Käufer gegenüberstehen, weil die neue Aktie noch nicht "auf dem Radar" von Analysten und Index-Aufnahmen ist.

### b) Limits to Arbitrage

- **Fehlende Shortbarkeit als Hedge:** Arbitrageure, die die Fehlbewertung durch Long-Spinoff/Short-Markt-Positionen ausnutzen wollen, finden in den ersten Wochen oft keinen liquiden Leihmarkt für die neue, dünn gehandelte Aktie — sie können also die Position kaum sauber hedgen, sondern tragen implizit Marktrisiko.
- **Informationskosten:** Fehlende Historie/Coverage macht systematische (quantitative) Bewertung teuer; das begrenzt, wie schnell informierte Arbitrageure Kapital allozieren.
- **Kleine Opportunity-Menge:** Nur ca. 10-20 relevante US-Spin-offs pro Jahr (siehe Kapazitätsabschnitt) — zu wenig Dealflow, um einen großen dedizierten Fonds zu tragen. Das begrenzt sowohl die Größe als auch die Geschwindigkeit des Kapitals, das die Ineffizienz eliminieren könnte.
- **Index-Aufnahme-Lag:** Institutionelles, indexgebundenes Kapital kann strukturell (Mandat) monatelang nicht kaufen, selbst wenn es die Unterbewertung erkennt — die "natürlichen" Käufer sind vorübergehend ausgeschlossen.

Diese Reibungen erklären plausibel, warum der Effekt ursprünglich bestand — sie erklären aber nicht, warum er trotz jahrzehntelanger Bekanntheit (dedizierte Spin-off-Hedgefonds, ein öffentlicher Spin-off-ETF seit 2006, Greenblatts "You Can Be a Stock Market Genius" seit 1997 als Blaupause) nicht binnen weniger Jahre wegarbitriert wurde — bzw. genau das ist, was die Post-Publication-Daten (Abschnitt d) nahelegen: Er wurde inzwischen weitgehend wegarbitriert.

### c) Originalstudien

- **Cusatis, Miles & Woolridge (1993, Journal of Financial Economics 33)**, "Restructuring Through Spinoffs: The Stock Market Evidence": 24-Monats-Überrendite ggü. Vergleichsunternehmen von **26.7% (t=2.55)** für Mutterkonzerne und **25.0% (t=2.43)** für Tochtergesellschaften. Ein großer Teil dieser Überrendite wird in der Literatur später auf nachfolgende Übernahmeaktivität der Spinoff-Einheiten zurückgeführt (siehe Allen, Lummer, McConnell & Reed 1995, "Can Takeover [Premia] Explain Spin-off Gains?").
- **Desai & Jain (1999, JFE 54)**, "Firm Performance and Focus": Stichprobe von **155 Spin-offs, 1975-1991**. Fokus-erhöhende Spin-offs zeigen signifikant größere Überrenditen (Ankündigungs- und Langfristfenster) als nicht-fokuserhöhende; genaue Drei-Jahres-Prozentwerte/t-Statistiken konnten in dieser Session nicht aus dem Volltext verifiziert werden (Paywall) — Sekundärzitate bestätigen aber Richtung und Signifikanzstruktur konsistent mit Cusatis et al.
- **McConnell & Ovtchinnikov (2004, Journal of Investment Management 2)**, "Predictability of Long-Term Spinoff Returns": umfassende Stichprobe **1965-2000**. Tochtergesellschaften schlagen die Benchmark über die ersten 22 Monate, danach Gleichlauf. Mutterkonzerne schlagen die Benchmark scheinbar über 15 Monate — **aber: die Autoren zeigen selbst, dass diese Überrendite fast vollständig auf einen einzigen Extremausreißer zurückgeht; ohne diesen ist die kumulierte Überrendite der Mutterkonzerne gleich der Benchmark.**

### d) Out-of-Sample / Post-Publication-Evidenz und Decay

Dies ist der entscheidende Abschnitt für die Falsifikation:

- **McConnell, Ozbilgin & Wahal (2001, Journal of Business 74)**, "Spinoffs, Ex Ante": explizit als Ex-ante-/Out-of-Sample-Test der Cusatis-et-al.-Strategie konzipiert, Stichprobe **1989-1995**. Ergebnis: **nur begrenzte Evidenz für Überperformance, insignifikant positive langfristige Überrenditen.** Das ist faktisch eine frühe, publikationsnahe Nicht-Replikation — nur acht Jahre nach der Originalstudie.
- **McConnell, Sibley & Xu (2015, Journal of Portfolio Management 42)**, "The Stock Price Performance of Spin-Off Subsidiaries, Their Parents, and the Spin-Off ETF, 2001–2013" (Volltext ausgewertet). Zentrale Zahlen, Stichprobe **146 Spin-off-Events, 153 Tochtergesellschaften, 139 Mutterkonzerne, 2001-2012**:
  - Tochtergesellschaften: Überrendite ggü. Size/B-M-Benchmark bei 6 Monaten **4.83% (t=1.69)**, 12 Monaten **8.50% (t=1.96)**, 22 Monaten **17.06% (t=2.16)**, 27 Monaten (Maximum) **29.20% (t=2.78)**, 36 Monaten **26.53% (t=2.40)**.
  - **Aber:** Die Verteilung ist stark rechtsschief. Bei 36 Monaten liegt der **Median der Überrendite bei -6.79%**, das 25. Perzentil bei **-39.44%**. D.h. der positive Mittelwert wird von wenigen extremen Gewinnern getragen ("Max" bei 36 Monaten: 775.95%!); **mehr als die Hälfte der Einzeltitel schneidet nach 36 Monaten schlechter ab als die Benchmark.**
  - Mutterkonzerne: Überrendite bei 15 Monaten (Höhepunkt-Fenster) **3.70% (t=0.66)**, bei 19 Monaten **4.79% (t=0.72)**, bei 36 Monaten **-2.70% (t=-0.48)** — **in keinem Horizont statistisch signifikant.**
  - **Reales, investierbares Vehikel:** Der Guggenheim/Invesco S&P Spin-Off ETF (Ticker **CSD**, Start Dezember 2006) schlug den Markt deutlich bis 2013 (kumulierte Rendite Dez. 2006–Dez. 2013: ETF +92.9% vs. CRSP-Value-Weighted-Markt +52.2%). **Aktuellere Daten (Stand der Websuche, 2026) zeigen jedoch: seit Auflage liegt CSD kumuliert bei ca. +74.6% gegenüber +76.9% für SPY** — d.h. netto Gebühren (0.65% p.a.) hat sich die 2013 noch sichtbare Outperformance über die folgenden gut zehn Jahre vollständig zurückgebildet und ins Negative gedreht. Das ist die stärkste verfügbare Netto-/Post-Publication-Evidenz: **ein reales, seit fast 20 Jahren laufendes Handelsvehikel liefert netto keine Outperformance mehr.**
  - Geschätzter Decay: Vergleicht man die Rohgrößenordnung der Originalstudien (24-36-Monats-Überrendite von 25-30%, hoch signifikant) mit dem Punktschätzer der 2001-2012-Stichprobe (nominell noch 17-27%, aber Median negativ) und dem investierbaren Ergebnis seit 2013 (~0% bis leicht negativ netto), ergibt sich ein **Decay von grob geschätzt 80-100% in Netto-/Praxistermen**, obwohl der akademische Bruttopunktschätzer wegen der Rechtsschiefe formal "noch signifikant" bleibt.
- **Strukturelle Lücke in den großen Replikationsstudien:** Der Spin-off-Effekt taucht **nicht** in den Standard-Meta-Studien (McLean & Pontiff 2016, 97 Anomalien; Hou/Xue/Zhang 2020 "Replicating Anomalies", 452 Charakteristika; Chen & Zimmermann Open Source Asset Pricing) auf, weil er kein kontinuierliches Querschnitts-Charakteristikum ist, sondern ein seltenes, binäres Corporate-Event. Das ist **kein Beleg für Robustheit**, sondern zeigt, dass diese Anomalie nie durch die harten Multiple-Testing-Hürden (t>2.78 bei Hou/Xue/Zhang) dieser Literatur gefiltert wurde — eine methodische Lücke, kein Gütesiegel.
- **Nicht-peer-reviewte Gegenevidenz:** Eine 2022er Copenhagen-Business-School-Masterarbeit ("Spin-off Performance: An Unrelenting Anomaly", 609 Spin-offs, Westeuropa/Nordamerika, 2000-2022) behauptet Fortbestand des Effekts. Das steht in **direktem Widerspruch** zur Netto-ETF-Evidenz oben. Da es sich um keine peer-reviewte Publikation handelt (Methodik/Robustheit nicht unabhängig begutachtet), wird dies hier **nicht** als belastbare Pro-Evidenz gewertet, sondern als Illustration der Kluft zwischen brutto-akademischer Event-Study-Methodik und netto-investierbarer Realität.
- **Mechanismus-Ebene:** Die verwandte "Index Effect"-Literatur (Greenwood & Sammon, NBER Working Paper 30748, "The Disappearing Index Effect") zeigt, dass die allgemeine Preiswirkung von index-getriebenem Forced Buying/Selling seit den 1990ern durch wachsendes Arbitragekapital systematisch abgenommen hat. Das stützt die Decay-These strukturell: der zugrundeliegende Verkaufsdruck-Mechanismus, der Spin-off-Fehlbewertung antreibt, ist selbst schwächer geworden.

### e) Kosten

Eine dedizierte Netto-Kosten-Studie im Stil Novy-Marx & Velikov (2016) oder Frazzini/Israel/Moskowitz (2018) **existiert für die Spin-off-Anomalie nicht** (kein Treffer in der Recherche) — das Fehlen einer solchen Studie ist selbst ein Warnsignal, da echte, institutionell interessante Anomalien inzwischen praktisch alle einer solchen Prüfung unterzogen wurden.

Indirekte Kostenindikatoren:
- Tochtergesellschaften sind in den ersten Monaten überwiegend Small-/Microcaps (mittlere Marktkapitalisierung in der McConnell/Sibley/Xu-Stichprobe je nach Jahr zwischen **$0.69 Mrd. und $15.1 Mrd.**, viele deutlich unter $1 Mrd.). Microcap-Literatur zeigt typische Geld-Brief-Spannen von **>2-3%** und hohe Market-Impact-Kosten bei institutionellen Tickets.
- Turnover ist moderat (Halteperiode von ca. 22 Monaten pro Position), das Kostenproblem liegt primär im **Einstieg**: Genau in den ersten Handelstagen/-wochen, wenn der Forced-Selling-Druck am größten und damit die Ineffizienz am größten ist, sind Spreads und Volatilität ebenfalls am höchsten — die attraktivste Phase ist zugleich die teuerste.

### f) Kapazität und Handelbarkeit

- Aggregiertes jährliches Marktwert-Volumen der US-Spin-off-Töchter (2001-2012-Stichprobe): zwischen **$9.8 Mrd. (2003)** und **$145.4 Mrd. (2008)**, bei typischerweise **10-19 Events/Jahr**; zwei Branchen (Telekom/TV-Übertragung und Konsumgüter-Nichtdurables) allein repräsentieren **49.3%** des aggregierten Marktwerts — starke Konzentration.
- Realistische Kapazitätsschätzung für eine disziplinierte, diversifizierte systematische Umsetzung (Positionsgrößenlimit ~5-10% des Tagesvolumens, Diversifikation über die parallel gehaltene Kohorte von typischerweise 15-30 Positionen): grob **USD 200 Mio. bis 1.5 Mrd.** an dediziertem Kapital, bevor Slippage und erzwungene Konzentration auf wenige Large-Cap-Spinoffs den Edge weiter verwässern. Das ist eine **Nischen-Kapazität**, klein im Vergleich zu klassischen Faktorprämien (Value, Momentum, Quality), die zweistellige Milliardenbeträge aufnehmen können.
- Shortbarkeit: schlecht in den ersten Wochen (dünner Leihmarkt), was sowohl das Hedging als auch reine Short-Strategien (z.B. auf überteuerte Tech-Spinoffs Ende der 1990er, siehe Recherchehinweis zu "arbitrage would have been possible in a frictionless market, but short positions were very difficult to establish") strukturell erschwert.

### g) Regimeabhängigkeit und Tail-Risiko

- **2008-Finanzkrise:** All-Subsidiary-Portfolio **-41.1%**, Spin-off-ETF **-55.2%**, gegenüber Gesamtmarkt **-38.1%**. Die Strategie fällt in der Krise **stärker** als der Markt — das Gegenteil einer Versicherungsprämie. Das deutet auf verdecktes Small-Cap-/Liquiditäts-/Qualitäts-Beta hin, das genau dann reißt, wenn Diversifikation am wichtigsten wäre.
- **Prozyklisches Dealflow-Muster:** Spin-off-Aktivität selbst ist stark prozyklisch (Höhepunkte 2002 und 2008 in der Stichprobe, Tiefpunkte 2003 und 2009) — die Opportunity-Menge konzentriert sich strukturell in Spätzyklus-/Euphoriephasen, was Timing-/Konzentrationsrisiko erhöht.
- **Rechtsschiefe auf Einzeltitelebene** (Mittelwert ≫ Median, s.o.) bedeutet: jeder real konzentrierte (nicht voll diversifizierte) Investor hat eine deutlich höhere Wahrscheinlichkeit, die Benchmark zu unterbieten, als der akademische Mittelwert suggeriert.

### h) Bekannte Kritik / Widerlegungen

- **Überlappende, nicht unabhängige Stichproben:** Cusatis et al. (1993), Desai & Jain (1999) und McConnell & Ovtchinnikov (2004) beziehen sich alle auf denselben zugrunde liegenden CRSP-Spin-off-Datenbestand 1965-2000 mit überlappenden Zeiträumen — das sind keine drei unabhängigen Bestätigungen, sondern überlappende Schnitte eines einzigen Datensatzes. Echte Out-of-Sample-Tests sind nur McConnell/Ozbilgin/Wahal (2001, schwach/insignifikant) und McConnell/Sibley/Xu (2015, signifikant im Mittelwert, aber schief/median-negativ).
- **Ausreißer-Artefakt bei Mutterkonzernen:** Das ursprünglich beeindruckende Mutterkonzern-Ergebnis (Cusatis et al., t=2.55) wird von den Autoren selbst (McConnell & Ovtchinnikov 2004) auf einen einzelnen Extremausreißer zurückgeführt — Lehrbuchbeispiel für einen Small-Sample-/Data-Mining-Artefakt.
- **M&A-Konfundierung:** Allen, Lummer, McConnell & Reed (1995) fragen explizit, ob Übernahmeprämien (nicht Spin-off-spezifische Fehlbewertung) einen wesentlichen Teil der ursprünglich gemessenen Überrendite erklären — viele Spin-off-Einheiten und Mutterkonzerne der 1980er/90er-Stichprobe wurden anschließend selbst übernommen.
- **Microcap-/Rechtsschiefe-Artefakt:** Die statistische Signifikanz in allen Studien beruht auf Mittelwerttests, die von wenigen Extremgewinnern getragen werden; der Median ist in der aktuellsten Stichprobe (2001-2012) bei 36 Monaten **negativ**. Das ist exakt das Muster, das durch Value-Weighting/NYSE-Breakpoint-Methodik (Hou/Xue/Zhang) typischerweise als nicht robust entlarvt wird — auch wenn Spin-offs nie durch diesen spezifischen Test liefen.
- **Selektions-/Survivorship-Effekte:** Studien schließen Mutterkonzerne aus, die "at or near the ex date" übernommen wurden (McConnell/Sibley/Xu, Fußnote 3) — eine Datenbereinigung, die die überlebende Stichprobe potenziell in Richtung "ruhigerer" Kursverläufe verzerrt.
- **Widerspruch akademisch vs. investierbar:** Die 2022er Masterarbeit behauptet Fortbestand bis 2022, während das reale ETF-Vehikel netto Kosten seit ~2013 keine Outperformance mehr zeigt. Dieser Widerspruch selbst ist der aussagekräftigste Befund: Brutto-Event-Study-Renditen und Netto-investierbare Renditen sind auseinandergelaufen — genau das Muster einer wegarbitrierten Anomalie.

---

## Kandidat 2: Post-Spin-off Kursdrift des Mutterkonzerns ("Parent Drift")

Wird separat bewertet, da die ökonomische Logik (Fokus-Realignment, Wegfall der "Konglomeratsabschlags"-Diversifikationskosten) eigenständig ist und in der Praxis oft als eigene Strategie ("kaufe den Mutterkonzern nach Spin-off-Ankündigung") vermarktet wird.

### a) Ökonomische Begründung (behauptet)
Wegfall des Konglomeratsabschlags, klarere Kapitalallokation, freigesetztes Managementfokus. Diese Story ist ökonomisch plausibel für die **Ankündigungsrendite** (kurzfristiger CAR, siehe unten), aber die Frage hier ist die **langfristige Kursdrift danach**.

### b) Limits to Arbitrage
Nicht relevant/diskutierbar, da kein robuster Effekt nachweisbar ist (siehe unten) — bei Mutterkonzernen (typischerweise weiterhin Large-Cap, liquide, mit Analysten-Coverage) gäbe es ohnehin kaum strukturelle Arbitragehindernisse. Genau das spricht gegen die Existenz eines echten, lang anhaltenden Mispricings: liquides Large-Cap-Kapital hätte einen echten Effekt sehr schnell eliminiert.

### c) Originalstudie
Cusatis et al. (1993): 24-Monats-Überrendite Mutterkonzerne **26.7% (t=2.55)** — s.o.

Kurzfristiger Ankündigungseffekt (nicht dieselbe Frage, aber Kontext): Veld & Veld-Merkoulova (2004, Journal of Banking & Finance 28), europäische Stichprobe von **156 Spin-offs aus 15 Ländern, 1987-2000**: 3-Tages-CAR um Ankündigung **2.62%** (signifikant), bei fokuserhöhenden Spin-offs **3.57%**, bei nicht-fokuserhöhenden nur **0.76%**. Das ist ein **Ankündigungseffekt**, kein handelbares Drift-Signal (man kennt die Ankündigung nicht im Voraus) und daher keine eigenständige systematische Strategie, sondern nur Kontext zur Fokus-Story.

### d) Out-of-Sample-Evidenz
- McConnell, Ozbilgin & Wahal (2001): insignifikante Ergebnisse in der 1989-1995-Out-of-Sample-Stichprobe.
- McConnell & Ovtchinnikov (2004): Mutterkonzern-Überrendite bei umfassender 1965-2000-Stichprobe **nachweislich durch einen einzigen Ausreißer getrieben**; ohne ihn: keine Überrendite.
- McConnell, Sibley & Xu (2015), 2001-2012: Mutterkonzern-Überrendite in **keinem** der getesteten Horizonte (6/12/15/19/36 Monate) statistisch signifikant (t-Werte zwischen **-0.55 und +0.72**); bei 36 Monaten sogar **negativer** Punktschätzer (-2.70%, t=-0.48).

Fazit: Der Effekt repliziert in keiner der drei unabhängigen Nachfolgestudien robust. Er sieht wie ein Small-Sample-Artefakt der Originalstichprobe aus.

### e)-g) Kosten/Kapazität/Regime
Nicht relevant zu vertiefen — es gibt keinen dokumentierten Netto-Effekt, den man kostenseitig oder kapazitätsseitig absichern müsste.

### h) Kritik
Siehe oben (Ausreißer-Artefakt, M&A-Konfundierung). Dies ist ein Lehrbuchfall für eine Anomalie, die bei der ersten unabhängigen Out-of-Sample-Prüfung (2001, nur 8 Jahre nach Publikation) bereits nicht mehr nachweisbar war.

---

## Gesamturteil zur Klasse "Spin-offs & Abspaltungen"

**Diese Anomalieklasse ist überwiegend tot, mit einem Teilaspekt (Subsidiary Drift), der brutto/akademisch noch schwache Spuren zeigt, aber netto/investierbar nicht mehr belastbar ist.**

Zusammenfassung der Belastungslinie gegen die Nullhypothese "kein Alpha":
1. Es gibt eine plausible, gut identifizierte ökonomische Mechanik (Forced Selling durch Indexfonds/Mandate + Neglect), die ursprünglich (1965-2000) mit soliden t-Statistiken (2.4-2.8) für Tochtergesellschaften dokumentiert ist.
2. Diese Mechanik ist Teil einer breiteren, ebenfalls dokumentierten Decay-Familie (Index-Effekt-Literatur, Greenwood & Sammon 2023): Der zugrunde liegende Verkaufsdruck-Mechanismus wird seit Jahrzehnten schwächer.
3. Das einzige reale, seit fast 20 Jahren existierende investierbare Vehikel (CSD-ETF) zeigt, dass die 2013 noch sichtbare Netto-Outperformance seither vollständig verschwunden ist.
4. Die Renditeverteilung ist so schief, dass der Median-Spin-off in der jüngsten Stichprobe (2001-2012) bei 36 Monaten die Benchmark **unterbietet** — der Mittelwert-Effekt ist ein Artefakt weniger Ausreißer, nicht ein breit verteilter Edge.
5. Der Mutterkonzern-Teil der Anomalie ist bereits in der ersten Out-of-Sample-Studie (2001) nicht mehr nachweisbar und in der jüngsten (2015) klar insignifikant — ein klassischer Small-Sample-/Data-Mining-Fall.
6. Es existiert keine einzige dedizierte Netto-Kosten-Studie (Novy-Marx/Velikov- oder Frazzini/Israel/Moskowitz-Stil) für diese Klasse — bemerkenswert für eine seit 1993 bekannte Anomalie, und selbst ein Warnsignal.

Damit erfüllt **kein** Kandidat die Bar für CANDIDATE ("dokumentierte Post-Publication-Evidenz UND Kostenrobustheit"). Subsidiary Drift wird als **WEAK** eingestuft (realer, aber mittlerweile weitgehend arbitrierter, klein-kapazitiver, schief verteilter und kostenintensiver Effekt mit schlechtem Krisenverhalten). Parent Drift wird als **KILL** eingestuft (nie robust repliziert, Ausreißer-Artefakt).

Für ein institutionelles Mandat mit echtem Kapital: Diese Klasse eignet sich allenfalls als **kleine, ereignisgetriebene Satellitenposition** innerhalb eines Special-Situations-/Event-Driven-Buckets (Kapazität grob USD 200 Mio.-1.5 Mrd.), nicht als eigenständige, skalierbare Faktorstrategie. Ein diszipliniertes Backtesting mit freien Daten (CSD-ETF-Kurshistorie seit 2006 vs. SPY, plus Ken-French-Size/B-M-Portfolios als Benchmark) ist möglich und wird empfohlen, bevor überhaupt über Kapitalallokation nachgedacht wird — die erwartete Antwort auf Basis der hier zusammengetragenen Evidenz ist allerdings, dass sich seit ca. 2013 kein signifikanter Netto-Edge mehr zeigen lässt.

---

## Quellen (Websuche, Juli 2026)

- [Restructuring Through Spinoffs: The Stock Market Evidence — Cusatis, Miles & Woolridge (1993), ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/0304405X9390009Z)
- [Firm performance and focus: long-run stock market performance following spinoffs — Desai & Jain (1999), ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0304405X9900032X)
- [Spin-offs, Ex Ante — McConnell, Ozbilgin & Wahal (2001), JSTOR](https://www.jstor.org/stable/10.1086/209672)
- [Predictability of Long-Term Spin-Off Returns — McConnell & Ovtchinnikov (2004), ResearchGate](https://www.researchgate.net/publication/228289308_Predictability_of_Long-Term_Spin-Off_Returns)
- [The Stock Price Performance of Spin-Off Subsidiaries, Their Parents, and the Spin-Off ETF, 2001–2013 — McConnell, Sibley & Xu (2015), Journal of Portfolio Management, Purdue University (Volltext ausgewertet)](https://business.purdue.edu/faculty/mcconnell/publications/The%20Stock%20Price...2013%20jpm.2015.42.1.143.pdf)
- [Do Spin-Offs Really Create Value? The European Case — Veld & Veld-Merkoulova (2004), SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=296092)
- [Value Creation Through Spin-offs: A Review of the Empirical Evidence — Veld & Veld-Merkoulova (2009), SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=905137)
- [Spin-off performance: An unrelenting anomaly — CBS Masterarbeit (2022, nicht peer-reviewed)](https://research.cbs.dk/en/studentProjects/spin-off-performance-an-unrelenting-anomaly)
- [Replicating Anomalies — Hou, Xue & Zhang (2020), NBER Working Paper 23394](https://www.nber.org/system/files/working_papers/w23394/w23394.pdf)
- [Open Source Cross-Sectional Asset Pricing — Chen & Zimmermann (2021), Federal Reserve Board](https://www.federalreserve.gov/econres/feds/files/2021-037pap.pdf)
- [The Disappearing Index Effect — Greenwood & Sammon, NBER Working Paper 30748](https://www.nber.org/system/files/working_papers/w30748/w30748.pdf)
- [Guggenheim/Invesco S&P Spin-Off ETF (CSD) — ETF-Übersicht, etfdb.com](https://etfdb.com/etf/CSD/)
- [CSD ETF Kurshistorie — Investing.com](https://www.investing.com/etfs/guggenheim-spin-off-historical-data)
- [Predictability of Long-Term Spin-Off Returns / Corporate Divestitures: Spin-Offs vs. Sell-Offs — Prezas et al., EFMA](https://www.efmaefm.org/0efmameetings/efma%20annual%20meetings/2013-Reading/papers/EFMA2013_0059_fullpaper.pdf)
- [Capital Market Implications of Spinoffs — S&P Quantamental Research (2017, praktikernahe Sekundärquelle, Zugriff verweigert/nur Titel verifiziert)](https://www.spglobal.com/content/dam/spglobal/mi/en/documents/general/Capital-Market-Implications-Of-Spinoffs.pdf)
