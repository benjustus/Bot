```yaml
agent: 03
klasse: "Insiderkäufe"
websuche_verfuegbar: ja
strategien:
  - name: "Opportunistische (non-routine) Insider-Käufe vs. Routine-Käufe"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 3
      regimestabilitaet: 3
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.55
    netto_sharpe_erwartung: "0.1-0.3"
    kernrisiko: "Alpha konzentriert sich in kleinen, illiquiden, lokal/schlecht-governance-geprägten Titeln; Kosten und realistische Positionsgrößen fressen den Großteil der Bruttorendite auf"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "SEC EDGAR Form 4 / SEC DERA 'Insider Transactions' Structured Data Sets (kostenlos, kein Ken-French-Datensatz)"
  - name: "Cluster-Käufe mehrerer Insider/Executives (koordiniertes Kaufsignal)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.4
    netto_sharpe_erwartung: "0.0-0.2"
    kernrisiko: "Dünne akademische Evidenzbasis (im Kern 1-2 Studien), Cluster-Events sind selten und noch stärker auf Microcaps konzentriert als das Basissignal -> Kapazität praktisch null"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "SEC EDGAR Form 4 (Multi-Insider-Aggregation pro CIK/Ticker selbst konstruiert)"
  - name: "Klassisches aggregiertes Insider-Kauf-Signal (Insider-Sentiment, Lakonishok/Lee-Typ)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "0.0-0.1"
    kernrisiko: "Seit Sarbanes-Oxley (2-Tage-Meldepflicht ab 2002) und massiver Kommerzialisierung des Signals (Retail-Apps, Insider-Tracker) strukturell arbitriert; internationale Replikation (UK) findet netto negative Renditen"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "SEC EDGAR Form 4 / OpenInsider (Scraping, kostenlos, inoffiziell)"
```

# Anomalieklasse: Insiderkäufe (Form-4-Filings) — Adversarial Review

**Agent 03 | Juli 2026 | Nullhypothese: Es gibt kein echtes, netto handelbares Alpha in dieser Klasse, bis das Gegenteil mit harten Zahlen bewiesen ist.**

Evidenzbasis: Websuche verfügbar und genutzt (siehe Quellen am Ende). Für einzelne Detailzahlen (insb. exakte t-Statistiken aus Originaltabellen, die nicht im Volltext zugänglich waren) wird explizit auf internes Wissen mit Unsicherheitsmarkierung zurückgegriffen — diese Stellen sind gekennzeichnet.

---

## Zusammenfassung des Urteils

Von drei geprüften Kandidaten erreicht **keiner** den Status CANDIDATE. Zwei sind WEAK (real, aber nur in sehr kleinem Maßstab und mit erheblicher Unsicherheit handelbar), einer ist KILL. Der ökonomische Kern der Klasse — Insider haben private Information und handeln teilweise darauf — ist nicht ernsthaft bestritten. Das Problem der Klasse ist fast durchgängig: **Was Outsider aus öffentlich gewordenen Form-4-Daten netto extrahieren können, ist nach Kosten, Kapazitätsgrenzen und Post-2002/Post-2012-Krautung sehr klein bis nicht mehr vorhanden.** Die einzige Teilmenge mit belastbarer Persistenz (opportunistische/non-routine Käufe) ist strukturell auf Small-/Microcaps beschränkt und daher institutionell kaum skalierbar.

---

## Kandidat 1: Opportunistische (non-routine) Insider-Käufe vs. Routine-Käufe

### a) Ökonomische Begründung

Kein Risikoprämien-Argument — dies ist eine reine **Informationsasymmetrie-Anomalie**. Bestimmte Insider (v.a. nicht-exekutive Insider, geografisch nahe am Firmensitz, in Firmen mit schwacher Governance) handeln diskretionär und unregelmäßig ("opportunistisch"), im Gegensatz zu "Routine"-Insidern, die zu vorhersehbaren, kalendergetriebenen Zeitpunkten handeln (10b5-1-Pläne, Optionsausübungszyklen, steuerlich motivierte Verkäufe). Die Fehlbewertung entsteht, weil:
- Außenstehende (Retail, aber auch viele Institutionelle) die riesige Masse an Form-4-Filings nicht in "informativ" vs. "uninformativ" trennen — das erfordert eine mehrjährige Handelshistorie pro Insider, um "Routine" zu identifizieren (genau die Methode von Cohen/Malloy/Pomorski, kurz CMP).
- Die Verursacher der Fehlbewertung sind somit **uninformierte/unaufmerksame Marktteilnehmer**, die entweder das Signal gar nicht verarbeiten (limitierte Aufmerksamkeit, Form-4-Filings sind technisch, massenhaft, unstrukturiert) oder es fälschlich mit dem "Grundrauschen" der Routine-Trades vermengen und dadurch verwässern.
- Zusatzmechanismus: schwache Unternehmens-Governance und geografische Nähe der Insider zum Headquarter korrelieren mit Informationsvorsprung — ein struktureller (nicht rein verhaltensbedingter) Kanal.

### b) Limits to Arbitrage

- **Informationsverarbeitungskosten**: Die Trennung Routine/Opportunistisch erfordert individuelle Handelshistorien über mehrere Jahre und ein Klassifikationsmodell — ein Fixkosten-Eintrittsbarriere, die kleine Arbitrageure abschreckt.
- **Idiosynkratisches Risiko / Illiquidität**: Die informativsten Trades stammen aus kleinen, lokal konzentrierten, schlecht kontrollierten Firmen — genau das Marktsegment, in dem laut Pontiff (2006) "Costly Arbitrage" idiosynkratisches Risiko Arbitrage am stärksten behindert.
- **Größenmismatch**: Für große Adressen ist die Opportunity zu klein (Positionsgrößen in Microcaps bewegen den Preis), für kleine Adressen ist die nötige Dateninfrastruktur (Bulk-EDGAR-Parsing, Insider-Klassifikation, Corporate-Governance-Scores) zu aufwendig — eine klassische "zu groß für die Kleinen, zu klein für die Großen"-Lücke.
- Keine relevante Short-Constraint, da die Strategie primär long (Opportunistisch-Kauf) gegen long (Routine-Kauf) bzw. gegen Marktindex gestellt wird.

### c) Originalstudie

**Cohen, Malloy, Pomorski (2012), "Decoding Inside Information", Journal of Finance, Vol. 67(3), S. 1009-1043** (NBER WP 16454, 2010). Stichprobe: US-Insider-Form-4-Daten über ca. zwei Jahrzehnte (1986-2007-Bereich, Thomson-Reuters-Insider-Filings). Kernresultat:
- Value-weighted abnormale Rendite einer Strategie, die ausschließlich auf **opportunistische** Insider setzt: **82 Basispunkte/Monat** (≈ 10% p.a.), hochsignifikant.
- Equal-weighted Variante: **180 Basispunkte/Monat**.
- Abnormale Renditen der **Routine-Trader sind statistisch nicht von Null verschieden**.
- Opportunistische Insider sagen zusätzlich zukünftige Firmen-News, Analysten-/Management-Prognose-Überraschungen und Gewinnankündigungs-Renditen voraus — ein zusätzlicher Kanal jenseits reiner Preisreaktion.
- *Hinweis zur Präzision*: Die exakten t-Statistiken der Originaltabellen (Vier-Faktor-Modell) liegen laut Sekundärquellen im hochsignifikanten Bereich (p<0.01); ein exakter t-Wert konnte aus den zugänglichen Quellen nicht zweifelsfrei verifiziert werden und wird hier bewusst nicht erfunden.

### d) Out-of-Sample-/Post-Publication-Evidenz

- **Ali & Hirshleifer (2017), "Opportunism as a Firm and Managerial Trait", Journal of Financial Economics 126(3), S. 490-515**: unabhängige, methodisch andere Operationalisierung von "Opportunismus" (Profitabilität vor Quartalsgewinnmeldungen statt Routine/Non-Routine-Klassifikation). Ergebnis: value-weighted Vier-Faktor-Alpha **>1%/Monat**, signifikant auch auf der Short-Seite. Das ist eine **echte methodische Replikation mit unabhängigem Maß**, kein bloßes Sample-Update — stärkt die Reproduzierbarkeit deutlich.
- Ein 2025er MDPI-Paper ("Herding Insider Traders: The Case of Opportunistic Insiders") zeigt, dass das Thema bis heute aktiv beforscht wird, was auf anhaltende (nicht widerlegte) Relevanz hindeutet, aber auch, dass die einfache Grundstrategie längst bekannt und potenziell gecrowded ist.
- **Keine dedizierte, mir zugängliche Studie** quantifiziert den spezifischen Post-2012-Decay von CMP direkt (kein "CMP-Faktor" im Stil eines Fama-French-Portfolios ist öffentlich fortlaufend gepflegt). Als Analogie-Anker dient **McLean & Pontiff (2016, JF)**: über 97 publizierte Renditeprädiktoren im Schnitt **-26% Out-of-Sample-Rückgang** und **-58% Post-Publication-Rückgang** gegenüber der In-Sample-Rendite. Es gibt keinen Grund anzunehmen, dass CMP dieser Regel entgeht — eher im Gegenteil, da das Signal seit 2012 kommerzialisiert wurde (Verity/2iq, InsiderScore/FactSet, Barchart-Cluster-Alerts etc.).
- Internationale Evidenz (UK, siehe Kandidat 3) zeigt für das *nicht* nach Opportunismus getrennte Basissignal bereits eine deutliche Abschwächung — ein Warnsignal auch für die verfeinerte Variante außerhalb der USA.

### e) Kosten

- Ein aktuelles (2026, nicht peer-reviewed) Arbeitspapier ("Insider Purchase Signals in Microcap Equities: Gradient Boosting Detection of Abnormal Returns", arXiv 2602.06198) findet: abnormale Renditen sind für kurze Haltedauern positiv, **verschwinden aber und werden teils negativ, sobald der handelbare Dollarbetrag pro Signal auf realistische Größen begrenzt wird**; die Renditen sind **negativ mit der Aktienliquidität korreliert** — d.h. gerade die profitabelsten Signale stecken in den am schwersten handelbaren Titeln.
- Für die UK-Replikation (FTSE-350, siehe Kandidat 3) werden Round-Trip-Kosten von 2.9% (FTSE-350) bis 6.2% (alle UK-Aktien) bzw. 8.1%/11.3% (hohe/niedrige Accruals-Stocks) dokumentiert — Größenordnungen, die die dokumentierten Brutto-Alphas von 1-2%/Monat schnell aufzehren, sobald Turnover monatlich/mehrmonatlich ist.
- Kein mir zugängliches Netto-Rendite-Papier im Stil Novy-Marx & Velikov (2016) oder Frazzini/Israel/Moskowitz (2018) wurde spezifisch für den CMP-Opportunismus-Faktor gefunden — dies ist selbst eine Erkenntnis: **die Literatur hat diesen Faktor nie einer strengen Netto-Kosten-Prüfung im Stil der etablierten Faktor-Kostenliteratur unterzogen.** Das ist ein Warnsignal, kein Freispruch.

### f) Kapazität und Handelbarkeit

- Konzentriert in kleinen, lokal verankerten, schlecht kontrollierten Firmen — genau das Gegenteil eines kapazitätsfreundlichen Faktors.
- Grobe Kapazitätsschätzung: **niedrig dreistelliger Millionenbereich (geschätzt < 300-500 Mio. USD AUM)**, bevor Market Impact und Liquiditätsengpässe die Nettorendite signifikant erodieren. Diese Schätzung ist eine Analogie aus der allgemeinen Microcap-/Illiquiditäts-Kapazitätsliteratur, keine dedizierte Studie für diesen Faktor.
- Handelbarkeit: technisch machbar (Form 4 muss laut Sarbanes-Oxley seit 2002 binnen 2 Geschäftstagen gemeldet werden, Daten sind über SEC EDGAR frei verfügbar), aber Ausführung in dünn gehandelten Titeln erfordert sorgfältiges Order-Slicing.
- Short-Seite kaum relevant/sinnvoll konstruierbar (Short-Availability in Microcaps oft schlecht, Borrow-Kosten hoch) — die Strategie ist de facto long-only bzw. long-short gegen den Markt statt Einzeltitel-Shorts.

### g) Regimeabhängigkeit und Tail-Risiko

- Kein dediziertes Krisenperioden-Backtest (2008, März 2020) für den CMP-Faktor spezifisch gefunden. Plausibilitätsargument: Insider könnten in Crashs verstärkt (contrarian) kaufen — Lakonishok & Lee (2001) zeigen, dass Insider aggregiert Contrarian-Investoren sind und Marktbewegungen besser vorhersagen als simple Contrarian-Strategien. Das deutet darauf hin, dass das Signal in Abschwungphasen eher zusätzliche (nicht reduzierte) Information trägt.
- Gleichzeitig: Small-/Microcap-Exposure bedeutet strukturelle Korrelation mit Liquiditäts- und Size-Faktor-Crashs — in Liquiditätskrisen (2008, März 2020) leiden gerade diese Titel überproportional, unabhängig vom Insider-Signal. Das Portfolio dürfte daher **linksschiefe Tail-Exposure** gegenüber allgemeinen Liquiditätsschocks haben, auch wenn das Insider-Timing selbst in der Tendenz "richtig" liegt (Insider kaufen die Bodenbildung, aber der Investor, der ihnen folgt, durchlebt den Drawdown vorher mit).

### h) Bekannte Kritik / Widerlegungen

- **Klassifikationsrauschen**: Die Routine/Non-Routine-Trennung nach CMP basiert auf einer Heuristik (mind. 3 aufeinanderfolgende Jahre gleicher Kalendermonat-Trades = Routine); Fehlklassifikationen sind plausibel und könnten einen Teil des Effekts erklären.
- **Konfundierung mit bekannten Faktoren**: Opportunistische Käufe könnten schlicht ein Proxy für Size-, Value- oder Illiquiditätsprämien sein (Insider kaufen nach Kursrückgängen = Value-/Contrarian-Tilt), die bereits anderweitig bekannt und teils selbst fragwürdig kapazitätsarm sind.
- **Fehlende dedizierte Netto-Kosten-Studie** (s.o.) ist selbst ein Kritikpunkt — die akademische Literatur hat primär Brutto-Alphas dokumentiert.
- **Kommerzialisierung**: Zahlreiche Fintech-Produkte (Verity/FactSet InsiderScore, 2iQ Research, Barchart, OpenInsider) verkaufen inzwischen genau dieses "smart insider"-Signal an Retail- und institutionelle Kunden — ein starkes Crowding-Indiz, auch ohne direkte akademische Decay-Studie.

**Urteil: WEAK.** Der informationsökonomische Kern ist glaubwürdig und methodisch unabhängig repliziert (Ali & Hirshleifer 2017), aber die Kombination aus Microcap-Konzentration, fehlender dedizierter Netto-Kosten-Studie und wahrscheinlichem Post-2012-Crowding verfehlt die CANDIDATE-Schwelle (dokumentierte Post-Publication-Evidenz UND Kostenrobustheit — Letzteres ist nicht belastbar dokumentiert, eher gegenteilig indiziert).

---

## Kandidat 2: Cluster-Käufe mehrerer Insider/Executives

### a) Ökonomische Begründung

Wenn mehrere Insider unabhängig voneinander (oder informationsvernetzt) innerhalb eines kurzen Fensters kaufen, sinkt die Wahrscheinlichkeit, dass es sich um idiosynkratische Liquiditäts-/Diversifikationsmotive handelt, und steigt die Wahrscheinlichkeit einer gemeinsamen, werthaltigen privaten Information. Der Fehlbewertungsmechanismus: Außenstehende beobachten typischerweise Einzel-Filings, nicht das Aggregationsmuster über mehrere Insider und Tage hinweg — eine weitere Spielart limitierter Aufmerksamkeit/Verarbeitungskosten.

**Zusatzbefund (Alldredge & Blank 2019)**: Insider clustern ihre Trades besonders um Kollegen, mit denen sie eng zusammenarbeiten, und dies verstärkt sich in Phasen niedriger Investor-Aufmerksamkeit, hoher Unsicherheit und hoher Informationsasymmetrie — was für einen echten Informationsweitergabe-Kanal (nicht nur Zufall) spricht.

### b) Limits to Arbitrage

Dieselben Kanäle wie Kandidat 1, plus zusätzlich: Cluster-Ereignisse (≥2-3 Insider innerhalb von z.B. 15 Tagen) sind selten und damit noch schwerer systematisch mit ausreichendem Turnover zu handeln. Die Notwendigkeit, Insider-zu-Insider-Netzwerke (Kollegenbeziehungen) zu rekonstruieren, ist ein zusätzlicher Datenaufwand, der kleine Arbitrageure abschreckt.

### c) Originalstudie

**Alldredge, D. M. & Blank, B. (2019), "Do Insiders Cluster Trades with Colleagues? Evidence from Daily Insider Trading", Journal of Financial Research, 42(2), S. 331-360.** Kernbefund: geclusterte Insider-Käufe werden von abnormalen Renditen **>2% im Folgemonat** begleitet. Ergänzend liefert **Ravina & Sapienza (2010), "What Do Independent Directors Know? Evidence from Their Trading", Review of Financial Studies 23(3), S. 962-1003** Evidenz, dass bestimmte Insider-Subgruppen (unabhängige Direktoren, insbesondere im Audit Committee) überdurchschnittlich informierte Käufer sind — das stützt die Cluster-/Subgruppen-Logik, ohne selbst eine Cluster-Studie zu sein.

Weitere in Praktiker-/Aggregator-Quellen zitierte Zahlen (z.B. "cluster purchases: 3.8% abnormale Rendite über 21 Handelstage vs. 2.0% für Nicht-Cluster-Käufe, Gap steigt auf 2.5 Prozentpunkte über 90 Tage") stammen aus Branchen-Whitepapers (2iQ Research u.ä.), **nicht aus peer-reviewten Journalen** — diese Zahlen werden hier explizit als weniger belastbar gekennzeichnet und nicht als akademische Evidenz gewertet.

### d) Out-of-Sample-/Post-Publication-Evidenz

Sehr dünn. Die akademische Literatur zu Cluster-Trading spezifisch ist im Wesentlichen auf 1-2 Kernstudien plus tangentiale Unterstützung (Ravina/Sapienza zu Subgruppen-Informiertheit) begrenzt. Es gibt keine mir bekannte unabhängige Zweitstudie, die exakt denselben Cluster-Mechanismus mit unabhängigen Daten/Zeiträumen repliziert, und keine dedizierte Decay-Schätzung. Das 2025er MDPI-Herding-Paper deutet zumindest fortlaufendes akademisches Interesse an, liefert aber keine robuste Netto-Kosten- oder Decay-Quantifizierung.

### e) Kosten

Keine dedizierte Netto-Kosten-Studie gefunden. Da Cluster-Ereignisse tendenziell in denselben (kleinen, illiquiden) Firmen auftreten wie Kandidat 1 — eher noch konzentrierter, weil das Cluster-Kriterium die Grundmenge weiter einschränkt — ist zu erwarten, dass die Kostenproblematik mindestens so gravierend ist wie bei Kandidat 1, eher schlimmer wegen der geringeren Ereignisanzahl (schlechtere Diversifikation über Zeit/Titel, höhere Idiosynkrasie im Portfolio).

### f) Kapazität und Handelbarkeit

Sehr gering. Cluster-Ereignisse sind selten, das investierbare Universum zu jedem Zeitpunkt ist klein (typischerweise eine Handvoll Namen gleichzeitig), was Diversifikation und damit auch Kapazität stark einschränkt. Realistische Kapazitätsschätzung: **niedriger zweistelliger bis niedriger dreistelliger Millionenbereich**, eher eine Nischenstrategie für einen kleinen spezialisierten Pool als eine Kernallokation.

### g) Regimeabhängigkeit und Tail-Risiko

Nicht dokumentiert in den gefundenen Quellen. Analog zu Kandidat 1 zu erwarten: verstärktes Signal in Unsicherheitsphasen (laut Alldredge & Blank clustern Insider gerade dann verstärkt), aber gleichzeitig erhöhte Liquiditäts-/Crash-Exposure durch die Small-Cap-Konzentration.

### h) Bekannte Kritik / Widerlegungen

- Geringe Stichprobengröße/Ereigniszahl erhöht das Risiko von Data-Mining bzw. Zufallsfunden in der ursprünglichen Studie.
- Viele der im Internet kursierenden "Cluster-Buy"-Erfolgszahlen (3.8%/21 Tage etc.) stammen aus nicht-akademischen, potenziell selektiv berichteten Quellen (Anbieter von Insider-Tracking-Produkten haben ein kommerzielles Interesse, die Wirksamkeit ihres Signals zu betonen) — klassisches Publication-/Selection-Bias-Risiko außerhalb des Peer-Review-Prozesses.
- Keine belastbare internationale Replikation gefunden.

**Urteil: WEAK.** Plausibler Informationsmechanismus mit seriöser (wenn auch dünner) akademischer Stütze, aber zu wenig unabhängige Replikation, keine Kosten-/Kapazitätsstudie, und die ökonomisch sinnvolle Handelsmenge dürfte für ein institutionelles Mandat zu klein sein, um mehr als eine Nischen-Beimischung zu rechtfertigen.

---

## Kandidat 3: Klassisches aggregiertes Insider-Kauf-Signal (Insider-Sentiment / Lakonishok-Lee-Typ)

Dies ist die "Urform" der Anomalie und dient hier explizit als **Kontrastfolie**: Sie zeigt, wohin die Klasse ohne die Verfeinerungen aus Kandidat 1/2 tendiert.

### a) Ökonomische Begründung

Gleiche Grundlogik wie oben (Informationsasymmetrie), aber ohne Unterscheidung Routine/Opportunistisch bzw. Cluster — schlicht "aggregierte Netto-Insider-Käufe pro Firma sagen zukünftige Renditen voraus". Der Fehlbewertungs-Kanal ist historisch v.a. die **Meldeverzögerung**: vor Sarbanes-Oxley (2002) hatten Insider bis zu 40 Tage Zeit, ihre Trades zu melden, was Außenstehenden Information erst mit erheblicher Verzögerung zugänglich machte.

### b) Limits to Arbitrage

Historisch: Meldeverzögerung selbst war die Arbitragegrenze — wer die Verzögerung nicht überbrücken konnte (kein Zugriff/Prozess für rechtzeitige Nachbildung), konnte nicht handeln. Diese strukturelle Friktion ist seit 2002 (2-Tage-Meldepflicht) weitgehend beseitigt — was das Signal für Outsider theoretisch handelbarer, aber auch schneller arbitrierbar gemacht hat.

### c) Originalstudie

**Lakonishok, J. & Lee, I. (2001), "Are Insider Trades Informative?", Review of Financial Studies 14(1), S. 79-111.** Stichprobe: NYSE/AMEX/Nasdaq, 1975-1995. Kernbefunde: Käufe sind informativ, Verkäufe nicht; die Vorhersagekraft für Renditen ist auf kleinere Firmen konzentriert; Insider sind aggregiert Contrarians, sagen aber Marktbewegungen besser vorher als simple Contrarian-Strategien.

**Jeng, Metrick & Zeckhauser (2003), "Estimating the Returns to Insider Trading: A Performance-Evaluation Perspective", Review of Economics and Statistics, Mai 2003.** Performance-Evaluations-Methodik (statt Event-Study): Insider-Käufe erzielen abnormale Renditen von **>6% p.a.**, Verkäufe sind nicht signifikant. Zusätzlich schätzen die Autoren die Kosten des Insiderhandels für Außenstehende als sehr klein (~10 Cent pro 10.000-USD-Transaktion) — ein Hinweis darauf, dass auch das Nachbildungspotenzial für Outsider strukturell begrenzt ist.

Grundlegende Vorarbeit: **Seyhun, N. (1986), "Insiders' Profits, Costs of Trading, and Market Efficiency", Journal of Financial Economics 16(2)**, zeigt bereits, dass Insider Nettogewinne erzielen, Außenstehende mit Meldeverzögerung aber nach Kosten kaum profitieren.

### d) Out-of-Sample-/Post-Publication-Evidenz

**Testing the Insider Trading Anomaly in FTSE-350 (2022, Frontiers)**: UK-Replikation mit granularen Insider-Daten über ein Jahrzehnt. Ergebnis: **deutlich niedrigere abnormale Renditen als in der US-Literatur dokumentiert**; markt-modell-adjustierte Renditen nach Verkäufen sogar signifikant **negativ (-0.752%)**; Käufe liefern negative bzw. (je nach Test) insignifikante abnormale Renditen. Die Autoren betonen, dass diese mageren Brutto-Effekte die dokumentierten Round-Trip-Kosten (2.9% FTSE-350, bis 6.2%/8.1%/11.3% je nach Segment) **nicht annähernd kompensieren** — Fazit der Autoren: Markteffizienz ist für diese Größensegmente stärker intakt als frühere Studien suggerieren.

Dies liefert eine der wenigen echten **internationalen Post-Publication-Tests** in dieser gesamten Klasse und fällt klar negativ aus für das undifferenzierte Basissignal.

Zusätzlich: Die generelle McLean-&-Pontiff-Decay-Rate (-58% post-publication im Schnitt über 97 Anomalien) ist als Analogie-Prior anzuwenden — mit der Besonderheit, dass Insiderkäufe zusätzlich durch die 2002er Regulierungsänderung strukturell "vorzeitig" arbitriert wurden, weil die Kern-Friktion (Meldeverzug) direkt beseitigt wurde.

### e) Kosten

Wie oben: FTSE-350-Studie zeigt Netto-Effekt negativ. In den USA sind keine mir bekannten aktuellen (post-2015) Studien vorhanden, die für das undifferenzierte Signal eine positive Netto-Rendite nach realistischen Kosten dokumentieren — die moderne Literatur hat sich fast vollständig auf die verfeinerten Varianten (Kandidat 1/2) verlagert, weil das Grundsignal als "ausgereizt" gilt.

### f) Kapazität und Handelbarkeit

Technisch das am leichtesten handelbare Signal (einfachste Regel, breiteste Datenverfügbarkeit über kostenlose Aggregatoren wie OpenInsider), aber gerade deshalb am stärksten kommerzialisiert/gecrowded: zahlreiche Retail-Apps und Newsletter verkaufen "folge den Insidern"-Signale seit Jahren.

### g) Regimeabhängigkeit und Tail-Risiko

Wie Kandidat 1, ohne die Präzisierung durch Opportunismus-Filter vermutlich mit noch mehr Grundrauschen (viele "Käufe" sind de facto Routine/steuerlich motiviert und tragen kein Signal), was die Tail-Charakteristik nicht verbessert, aber die durchschnittliche Signalqualität verschlechtert.

### h) Bekannte Kritik / Widerlegungen

- **Strukturelle Obsoleszenz durch Regulierung**: Die zentrale Friktion (40-Tage-Meldeverzug), die den Originaleffekt trug, existiert seit 2002 nicht mehr in der Form.
- **Microcap-Konzentration**: Lakonishok & Lee selbst zeigen, dass die Vorhersagekraft auf kleinere Firmen beschränkt ist — bekanntes Muster für spätere Kosten-Ernüchterung (vgl. Fama & French 2008 "Dissecting Anomalies": viele Anomalien sind Microcap-getrieben und ökonomisch nach Kosten irrelevant).
- **Internationale Widerlegung**: FTSE-350-Studie mit negativer Netto-Evidenz ist ein starkes Gegenargument gegen universelle Gültigkeit.
- **Redundanz**: Das gesamte ökonomisch werthaltige Signal dieser Klasse scheint in der Literatur inzwischen fast vollständig in der Opportunistisch/Routine-Unterscheidung (Kandidat 1) aufzugehen — das undifferenzierte Signal ist im Kern eine verwässerte Version davon.

**Urteil: KILL.** Als eigenständige, undifferenzierte Handelsstrategie für Outsider ist dieses Signal strukturell arbitriert (Regulierung + Kommerzialisierung), international nicht robust repliziert, und nach Kosten in der direktesten verfügbaren Post-Publication-Studie (UK) sogar negativ.

---

## Gesamtfazit für die Klasse "Insiderkäufe"

1. **Die Klasse ist nicht komplett tot, aber sie ist auf eine sehr schmale, kapazitätsarme Nische geschrumpft.** Der einzige Teil mit belastbarer, methodisch unabhängiger Post-Publication-Bestätigung (Ali & Hirshleifer 2017 als Replikation von Cohen/Malloy/Pomorski 2012) bleibt strukturell auf Small-/Microcaps beschränkt, ohne dokumentierte Netto-Kosten-Robustheit.
2. **Kein Kandidat erreicht CANDIDATE.** Der limitierende Faktor ist in allen drei Fällen derselbe: Kostenrobustheit ist entweder negativ dokumentiert (Kandidat 3, UK-Studie) oder schlicht nicht belastbar untersucht (Kandidat 1, 2) — und wo sie indirekt geprüft wurde (Microcap-arXiv-Preprint 2026), deutet die Evidenz auf Erosion bei realistischer Positionsgröße hin.
3. **Kapazität ist der strukturelle Deckel der gesamten Klasse.** Selbst die glaubwürdigste Variante (opportunistische Käufe) dürfte kaum über den niedrigen dreistelligen Millionenbereich hinaus skalierbar sein, bevor Market Impact die Nettorendite auf null drückt.
4. **Regulatorische Entwicklung wirkt gegen die Klasse**: Die 2002er Verkürzung der Meldefrist auf 2 Tage hat die zentrale historische Friktion bereits strukturell reduziert; jede weitere Erhöhung der Transparenz/Geschwindigkeit von Form-4-Daten (z.B. durch bessere EDGAR-APIs, wie seit einigen Jahren verfügbar) wirkt tendenziell weiter anomalie-mindernd.
5. **Ehrliche Einordnung für das Mandat**: Wer diese Klasse dennoch handeln will, sollte es als kleine, hochspezialisierte Satellitenstrategie mit Fokus auf die opportunistisch/nicht-routine-Filterung tun, mit strengem Kapazitätslimit, expliziter Small-Cap-Liquiditätsprämien-Kontrolle (um zu prüfen, ob nach Kontrolle für Size/Illiquidität überhaupt noch Alpha übrig bleibt) und einer dedizierten Netto-Kosten-Validierung vor Kapitaleinsatz — diese Validierung existiert in der akademischen Literatur bislang nicht in ausreichender Tiefe.

---

## Quellen (aus Websuche, Juli 2026)

- [Decoding Inside Information — Cohen, Malloy, Pomorski (2012), Journal of Finance](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2012.01740.x)
- [Decoding Inside Information — NBER Working Paper 16454](https://www.nber.org/papers/w16454)
- [Opportunism as a Firm and Managerial Trait — Ali & Hirshleifer (2017), JFE](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2635257)
- [Do Insiders Cluster Trades with Colleagues? — Alldredge & Blank (2019), Journal of Financial Research](https://onlinelibrary.wiley.com/doi/abs/10.1111/jfir.12172)
- [What Do Independent Directors Know? — Ravina & Sapienza (2010), RFS](https://papers.ssrn.com/abstract=951921)
- [Estimating the Returns to Insider Trading — Jeng, Metrick, Zeckhauser (2003)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=146029)
- [Are Insider Trades Informative? — Lakonishok & Lee (2001), RFS](https://academic.oup.com/rfs/article-abstract/14/1/79/1587398)
- [Testing the Insider Trading Anomaly in FTSE-350 (2022, Frontiers/PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8886886/)
- [Does Academic Research Destroy Stock Return Predictability? — McLean & Pontiff (2016), JF](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365)
- [Open Source Cross-Sectional Asset Pricing — Chen & Zimmermann](https://www.openassetpricing.com/)
- [Insider Purchase Signals in Microcap Equities (arXiv 2602.06198, 2026, nicht peer-reviewed)](https://arxiv.org/pdf/2602.06198)
- [Herding Insider Traders: The Case of Opportunistic Insiders (MDPI, 2025)](https://www.mdpi.com/1911-8074/18/11/629)
