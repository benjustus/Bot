```yaml
agent: 22
klasse: "Rohstoffe & Futures"
websuche_verfuegbar: ja
strategien:
  - name: "Commodity Basis / Term-Structure Carry (Backwardation-minus-Contango)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 3
      regimestabilitaet: 2
      handelbarkeit: 4
      kapazitaet: 3
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.40
    netto_sharpe_erwartung: "0.15-0.35"
    kernrisiko: "Financialization + Crowding erodieren die Prämie strukturell; Tail-Risiko in Storage-/Lieferkrisen (WTI April 2020: -37,63 USD/Barrel); ökonomisch eher rationale Versicherungsprämie als Mispricing, schrumpft mit zuströmendem Risikokapital."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "CFTC Commitments of Traders (frei, seit 1986); AQR 'Value and Momentum Everywhere' Commodity-Value-Faktor (frei, monatlich); vollständige Terminkurve (F1 vs F2..Fn) nur über kostenpflichtige Anbieter (Bloomberg/CSI/Norgate/Quandl-CHRIS-Premium)."

  - name: "Cross-Sectional Commodity Momentum"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 4
      kapazitaet: 3
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0.05-0.25"
    kernrisiko: "Dokumentierter Crowding-Effekt (~8% p.a. Renditeeinbuße pro Std.-Abw. Crowding-Anstieg) frisst Bruttoprämie von 9-15% p.a. weitgehend auf; hoher Turnover, Momentum-Crash-Risiko bei abrupten Regimewechseln."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Yahoo Finance/Stooq Frontmonth-Futures (CL=F, GC=F, ZC=F, HG=F, NG=F etc.); AQR 'Value and Momentum Everywhere' Commodity-Momentum-Faktor (frei, monatlich)."

  - name: "Hedging-Pressure-Faktor (Commercial Hedging Pressure, Basu & Miffre 2013)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.25
    netto_sharpe_erwartung: "0.0-0.15"
    kernrisiko: "Starke Multikollinearität mit dem Basis-Faktor (kein robuster eigenständiger Signalgehalt); CFTC-Reklassifizierung 2009 (Legacy zu Disaggregated COT) bricht Zeitreihenkontinuität; 'Commercial'-Kategorie enthält zunehmend Swap-Dealer/Index-Investoren statt echter Produzenten-Hedger, was die Kern-Theorie verwässert."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "CFTC Commitments of Traders (Legacy seit 1986, Disaggregated seit 2006, frei, wöchentlich)"
```

# Anomalieklasse: Rohstoffe & Futures — Adversarial Review

**Agent 22 | Stand: Juli 2026 | Evidenzbasis: Websuche (WebSearch/WebFetch funktionsfähig) + internes Wissen**

## Executive Summary

Nullhypothese: Es gibt kein echtes, nach Kosten und Multiple-Testing-Korrektur robustes Alpha in der Anomalieklasse Rohstoffe & Futures. Diese Nullhypothese wird durch die Recherche **nicht verworfen**. Die drei geprüften Kandidaten — Basis/Carry, Cross-Sectional Momentum, Hedging-Pressure-Faktor — zeigen alle das gleiche Muster: robuste akademische In-Sample-Evidenz aus den 1990er/2000er-Jahren, gefolgt von dokumentierter Abschwächung nach der "Financialization" der Rohstoffmärkte (2004–2008) und strukturell mageren Ergebnissen 2010–2026. Keiner der drei Kandidaten erreicht das Urteil CANDIDATE. Zwei werden als WEAK eingestuft (Basis/Carry, Momentum), einer als KILL (Hedging-Pressure als eigenständiger Faktor).

Wichtiger konzeptioneller Punkt vorab: Anders als bei vielen Aktienanomalien (PEAD, Insiderkäufe etc.), die auf Verhaltens-Bias oder Informationsfriktionen beruhen, ist die klassische Rohstoff-Risikoprämie nach Keynes/Hicks explizit als **rationale Versicherungsprämie** konzipiert — Hedger zahlen Spekulanten für Risikotransfer. Das ist per Definition kein "Mispricing", sondern ein Preis für Risikotragung in einem segmentierten Markt. Das bedeutet: selbst wenn die Prämie historisch real war, ist sie (a) theoretisch nicht "arbitrierbar" im Sinne einer Ineffizienz, sondern eine Kompensation, die mit zuströmendem Risikokapital schrumpfen *muss*, und (b) empirisch schwer von einer echten Verhaltens-Ineffizienz zu unterscheiden. Genau das ist seit 2004 passiert.

---

## Kandidat 1: Commodity Basis / Term-Structure Carry (Backwardation-minus-Contango)

### a) Ökonomische Begründung

**Keynes' Theory of Normal Backwardation (1930):** Kommerzielle Produzenten (z.B. Ölförderer, Farmer) sind natürliche Long-Positionen im Cash-Markt und wollen ihr Preisrisiko durch Short-Futures hedgen. Um Spekulanten (Long-Futures) zur Übernahme dieses Risikos zu bewegen, muss der Futures-Preis unterhalb des erwarteten künftigen Spotpreises liegen ("Normal Backwardation") — die Differenz ist die Risikoprämie der Spekulanten. Hicks (1939) erweiterte dies zur allgemeineren Hedging-Pressure-Hypothese: Das Vorzeichen der Prämie hängt vom Netto-Hedging-Bedarf ab — dominieren Produzenten (Short-Hedger), resultiert Backwardation; dominieren Verarbeiter/Konsumenten (Long-Hedger, z.B. Fluggesellschaften bei Kerosin), resultiert Contango.

**Storage Theory (Kaldor 1939, Working 1949, Brennan 1958):** Die Basis (Futures minus Spot) spiegelt Lagerkosten minus Convenience Yield. Bei niedrigen Lagerbeständen ist der Convenience Yield (Optionswert der physischen Verfügbarkeit) hoch → Backwardation. Bei Lagerüberfluss/Glut dominieren Lagerkosten → Contango. Damit ist die Basis auch ein Knappheitssignal, nicht nur ein Hedging-Signal.

**Nicht-profitmaximierende Gegenseite:** Kommerzielle Hedger (Produzenten, Farmer, Ölkonzerne, Minenbetreiber) maximieren nicht den erwarteten Handelsgewinn, sondern minimieren Cashflow-Volatilität (Corporate-Hedging-Motiv: Kreditauflagen, Investitionsplanung, Management-Risikoaversion). Sie zahlen bewusst eine Versicherungsprämie — ökonomisch rational auf Unternehmensebene, aber "irrational" im reinen Erwartungswert-Sinn des Spekulanten. Das ist eine deutlich robustere Gegenseiten-Story als bei vielen Aktienanomalien, weil sie aus der Realwirtschaft (Corporate Finance) und nicht aus Behavioral Bias von Privatanlegern stammt.

### b) Limits to Arbitrage

- **Storage-Zwang:** Physische Arbitrage (Cash-and-Carry) erfordert tatsächliche Lagerhaltung — begrenzt durch Kapazität (z.B. Cushing, Oklahoma für WTI), Lagerkosten, Verderblichkeit (Agrar, Vieh).
- **Keine Short-Storage-Möglichkeit:** Reverse Cash-and-Carry (Verkauf von Spot, Kauf Futures bei Contango) ist bei den meisten Rohstoffen praktisch unmöglich, da man den physischen Rohstoff nicht "leerverkaufen" kann, den man nicht besitzt und lagern kann. Das begrenzt die Arbitrage-Kräfte in eine Richtung.
- **Regulatorische Eingriffe:** Der Onion Futures Act (1958) verbot nach einem Manipulationsskandal den Futures-Handel mit Zwiebeln in den USA bis heute — ein historisches Beispiel dafür, dass politische/regulatorische Grenzen die Arbitrage in Rohstoffmärkten strukturell einschränken können.
- **Positionslimits (siehe f):** CFTC-Speculative-Position-Limits begrenzen direkt, wie viel Kapital in einzelne Kontrakte fließen kann.

### c) Originalstudien

- **Gorton & Rouwenhorst (2006, "Facts and Fantasies about Commodity Futures", FAJ):** Stichprobe Juli 1959–Dezember 2004, gleichgewichteter Index aus bis zu 36 Rohstoff-Futures. Kernbefund: voll besicherte Rohstoff-Futures erzielten historisch Rendite und Sharpe Ratio ähnlich US-Aktien, bei negativer Korrelation zu Aktien/Anleihen und positiver Korrelation zu (unerwarteter) Inflation. Backwardation-Portfolios schlugen Contango-Portfolios signifikant. Publikationsbias-Risiko: Datensatz wurde von den Autoren selbst konstruiert (Rollmethodik, Gewichtung), was Replizierbarkeit durch Dritte erschwert.
- **Erb & Harvey (2006, "The Strategic and Tactical Value of Commodity Futures", FAJ):** Long-Short-Strategie: Kauf der 6 am stärksten backwardierten, Verkauf der 6 am stärksten contangoierten Rohstoffe (aus einem Universum von ~12), monatlich rebalanciert. Zentrale Erkenntnis der Autoren: Der durchschnittliche Excess Return einzelner Rohstoff-Futures ist über lange Zeiträume nahe Null — die gesamte historische Rendite eines Rohstoffindex stammt fast ausschließlich aus (1) der Rebalancing-/Diversifikations-Prämie und (2) dem Term-Structure-Signal, nicht aus einer generischen "Long Commodities"-Prämie. Das ist eine der schärfsten Kritiken an naivem Long-Only-Commodity-Investing und stützt indirekt die Basis-Strategie als den eigentlichen Renditetreiber.
- **Szymanowska, de Roon, Nijman & van den Goorbergh (2014, "An Anatomy of Commodity Futures Risk Premia", Journal of Finance):** Zerlegen Rohstoff-Futures-Renditen in Spot- und Term-Prämie. Sortierung nach Basis, Momentum, Volatilität, Inflation, Hedging Pressure, Liquidität ergibt Spot-Prämien von **5–14% p.a.** und Term-Prämien von **1–3% p.a.** Ein einziger Faktor (High-minus-Low-Basis-Portfolio) erklärt den Großteil der Querschnittsvarianz der Spot-Prämien — ein starkes Argument für Basis als dominantes Preisungsprinzip, aber auch ein Single-Factor-Modell mit begrenzter Robustheitsprüfung außerhalb der Autoren-Stichprobe.
- **Bakshi, Gao & Rossi (2019, "Understanding the Sources of Risk Underlying the Cross-Section of Commodity Returns", Management Science):** Drei-Faktor-Modell (Average-, Carry-, Momentum-Faktor) beschreibt den Querschnitt; einfachere Ein/Zwei-Faktor-Modelle mit nur Average/Carry werden statistisch verworfen. Wichtig: Innovationen in der globalen Aktienvolatilität bepreisen Carry-sortierte Portfolios — das deutet darauf hin, dass die Carry-Prämie eine **Kompensation für Exposure zu systemischem Vol-/Tail-Risiko** ist (nicht reine Ineffizienz), was die Interpretation als "rationale Risikoprämie" stützt.

### d) Out-of-Sample-/Post-Publication-Evidenz

**Financialization (2004–2008):** Institutionelles Kapital in Rohstoff-Indexprodukten stieg von rund 15 Mrd. USD (2003) auf über 200 Mrd. USD (2008), mit Spitzenwerten (verschiedene Schätzungen) im Bereich 300–450 Mrd. USD um 2011/2012. Dieser massive Kapitalzustrom veränderte die Marktstruktur fundamental: Long-only-Indexanleger (Pensionsfonds, Privatanleger via ETFs) traten als neue "nicht-hedgende Nachfrage" auf, die selbst keine Versicherungsprämie verlangt, sondern strukturell long ist — das drückt tendenziell auf die Backwardation-Prämie und verschiebt viele Kontrakte in häufigeren/tieferen Contango.

**Bhardwaj, Gorton & Rouwenhorst (2015, "Facts and Fantasies about Commodity Futures Ten Years Later"):** Erweiterung der Originalstudie bis 2014. Zentrale Botschaft der Autoren: In- und Out-of-Sample-Risikoprämien sind statistisch nicht signifikant verschieden, ebenso die Basis-Rendite-Beziehung — die Autoren selbst ziehen ein optimistisches Fazit ("hat sich repliziert"). Adversariale Einordnung: Diese Studie stammt von den Originalautoren selbst (Interessenkonflikt: Bestätigung der eigenen These), und der Beobachtungszeitraum 2005–2014 umfasst sowohl den Rohstoff-Superzyklus (2005–2008) als auch den Einbruch 2008 und die beginnende Baisse ab 2011 — eine Mittelung, die eine mögliche Verschlechterung nach 2011 verdecken kann.

**Performance des breiten Marktes 2010–2026:** Der Bloomberg Commodity Index (BCOM) erzielte über die letzten 10 Jahre (Trailing bis ca. 2024/25) nur **ca. 5,1% p.a.**, gegenüber 13,7% p.a. für den S&P 500 — ein Großteil dieser Underperformance ist auf **negativen Roll Yield** in strukturell contango-geprägten Märkten zurückzuführen (v.a. Energie und Edelmetalle in Teilperioden). Das betrifft zwar primär Long-Only-Indexprodukte und nicht direkt die marktneutrale Basis-Long-Short-Strategie, zeigt aber, dass die von Erb & Harvey postulierte "Term-Structure-Prämie" im Aggregat seit 2010 strukturell schwächer/negativer war als in der 1959–2004-Stichprobe.

**Decay-Schätzung (eigene, konservative Einordnung):** Basierend auf der Kombination aus (i) dokumentiertem Kapitalzustrom post-2004, (ii) Crowding-Literatur (siehe Momentum-Sektion, analog für Carry), und (iii) empirisch schwacher BCOM-Performance 2010–2025 wird die Brutto-Prämie der Basis-Strategie auf **30–50% Decay** gegenüber der 1959–2004-Referenzperiode geschätzt. Das ist eine interne Schätzung, keine direkt zitierte Studienzahl — sie ist mit erheblicher Unsicherheit behaftet, da öffentlich zugängliche, saubere Post-2010-Replikationen mit exakten t-Statistiken in der Recherche nicht auffindbar waren (Datenzugriffsproblem, siehe unten).

### e) Kosten

Roll-Kosten variieren stark nach Liquidität: In hochliquiden Kontrakten (WTI, Gold, Mais) liegen realistische Roll-/Spread-Kosten bei geschätzt 5–20 Basispunkten pro Roll; in illiquiden Kontrakten (Lean Hogs, Feeder Cattle, Orangensaft, Lumber, hintere Erdgas-Monate) können es 50–200+ Basispunkte sein. Da die Strategie ein diversifiziertes Universum von 20–30 Rohstoffen inklusive vieler dünn gehandelter Märkte benötigt, um überhaupt eine belastbare Cross-Section zu haben, ist die Kostenbelastung im Portfolio-Durchschnitt nicht vernachlässigbar. Monatliches Rebalancing plus die Notwendigkeit, jeden Kontrakt vor Fälligkeit zu rollen (nicht nur bei Signaländerung), erzeugt strukturellen Grund-Turnover unabhängig vom Signal selbst.

### f) Kapazität und Handelbarkeit

CFTC-Positionslimits (finale Regel 2020, 17 CFR Part 150) begrenzen spekulative Positionen typischerweise auf 10% des Open Interest für die ersten 50.000 Kontrakte, danach +2,5% pro weitere Einheit; im Spotmonat gelten schärfere Grenzen (üblicherweise ~25% der lieferbaren Menge). Für liquide Kontrakte (WTI, Gold, Mais, Sojabohnen) ist das für die meisten Hedgefonds-Größenordnungen kein bindendes Limit. Für kleinere Agrar-/Vieh-Märkte (Hafer, Orangensaft, Lean Hogs, Lumber) wird das Limit schnell bindend und begrenzt die Skalierbarkeit eines diversifizierten Multi-Commodity-Programms auf geschätzt niedrige einstellige Mrd.-USD-Bereiche, bevor Market Impact und Positionslimits gemeinsam die Grenzkosten stark ansteigen lassen. Ein auf die liquidesten 8–10 Rohstoffe konzentriertes Programm ist deutlich kapazitätsstärker, verliert aber Diversifikation und damit Signifikanz.

### g) Regimeabhängigkeit und Tail-Risiko

Die Strategie ist hochgradig regimeabhängig: In breiten, strukturellen Contango-Phasen (z.B. Energiemärkte nach Schiefergas-Boom 2014–2019, oder globale Lager-Gluts) tendieren viele Basis-Signale gleichzeitig in dieselbe Richtung, was Diversifikation innerhalb des Long-Short-Buckets reduziert. Das Extremrisiko materialisierte sich am **20. April 2020**: WTI-Front-Month-Futures (Mai-Kontrakt) fielen erstmals in der Geschichte auf negative Preise (bis zu **-40,32 USD/Barrel** intraday, Settlement ca. -37,63 USD/Barrel), weil Lagerkapazität in Cushing, Oklahoma praktisch erschöpft war und Kontraktinhaber kurz vor Fälligkeit Positionen um jeden Preis schließen mussten. Dies ist ein Paradebeispiel für Storage-Theory-Tail-Risiko: Cash-and-Carry-Trader, die auf Super-Contango gesetzt hatten (long Front, short Back, plus physische Lagerung), gerieten in eine Situation, in der die Lagerkapazität selbst zum bindenden, nicht-linearen Risikofaktor wurde — ein Risiko, das in keinem historischen Backtest vor 2020 vorkam und damit klassisches Tail-Risiko außerhalb der Stichprobe darstellt.

### h) Bekannte Kritik/Widerlegungen

- **Indexkonstruktion:** GSCI (produktionsgewichtet, energie-lastig) und BCOM/DJ-UBS (liquiditätsgewichtet, diversifizierter) liefern über identische Zeiträume deutlich unterschiedliche historische Renditen — die "Rohstoff-Prämie" ist damit teilweise ein Artefakt der Indexmethodik, nicht eine robuste, methodenunabhängige Konstante.
- **Multiple Testing:** Nach Harvey, Liu & Zhu (2016) sollten wegen der Vielzahl publizierter Faktoren t-Statistiken von >3,0 gefordert werden. Viele der zitierten Commodity-Basis-Portfolios liegen im Bereich t≈2–3, was nach adjustierten Schwellenwerten grenzwertig ist.
- **Datenqualität:** Frühe Rohstoff-Futures-Daten (vor 1980) sind lückenhaft; Backfill- und Survivorship-Effekte bei der Konstruktion 40+-jähriger Indizes (eingestellte Kontrakte, geänderte Kontraktspezifikationen) sind schwer vollständig zu kontrollieren.
- **Rationale-Risikoprämie-Einwand:** Wie oben erläutert ist die Basis-Prämie theoretisch eher eine kompensierte Risikoexposition (Bakshi/Gao/Rossi: Verknüpfung mit globaler Aktienvolatilität) als eine Verhaltens-Ineffizienz — das relativiert den Anomalie-Charakter grundsätzlich.

**Urteil: WEAK.** Die Basis-/Carry-Strategie hat die theoretisch überzeugendste ökonomische Fundierung aller drei Kandidaten (reale Gegenseite: Corporate Hedger), aber die dokumentierte Post-2004-Abschwächung, Crowding durch Financialization, Tail-Risiken (April 2020) und Kapazitätsgrenzen in illiquiden Kontrakten verhindern eine CANDIDATE-Einstufung. Es fehlt insbesondere eine überzeugende, unabhängige (nicht von den Originalautoren stammende) Post-2010-Studie mit robusten t-Statistiken netto Kosten.

---

## Kandidat 2: Cross-Sectional Commodity Momentum

### a) Ökonomische Begründung

Kein einheitliches Rational-Modell, sondern meist verhaltensbasiert (analog Aktienmomentum): graduelle Informationsdiffusion, Under-/Overreaction von Hedgern und Trend-Followern, Herding unter CTA-Strategien. Ein spezifisch rohstoff-relevanter Kanal (Bakshi/Gao/Rossi 2019): Momentum-Prämie korreliert mit einem Maß spekulativer Aktivität — d.h. Trendfolge-Kapital selbst (CTAs, Managed Futures) erzeugt einen Teil des Signals, was eher auf eine selbstverstärkende Flow-Dynamik als auf eine fundamentale Risikoprämie hindeutet. Miffre & Rallis (2007) zeigen zudem, dass Momentum-Portfolios strukturell backwardierte Kontrakte kaufen und contangoierte verkaufen — Commodity-Momentum ist damit teilweise ein verzögertes/rotierendes Signal auf denselben Basis-Mechanismus wie Kandidat 1, keine vollständig unabhängige Anomalie.

**Nicht-profitmaximierende Gegenseite:** schwächer identifizierbar als bei Basis/Hedging-Pressure. Am ehesten: Hedger, die aus operativen (nicht Rendite-) Gründen antizyklisch handeln, sowie träge institutionelle Rebalancer.

### b) Limits to Arbitrage

Momentum-Strategien erfordern hohen Turnover (monatliches oder häufigeres Rebalancing über Ranking-Perioden von 1–12 Monaten), was Transaktionskosten strukturell wichtiger macht als bei Carry. Zudem sind Momentum-Strategien anfällig für "Crowding" durch systematische CTA-/Trendfolge-Fonds, die ähnliche Signale zeitgleich handeln — das verstärkt Markt-Impact und erhöht Korrelation zwischen vermeintlich unabhängigen Wetten.

### c) Originalstudien

- **Miffre & Rallis (2007, "Momentum Strategies in Commodity Futures Markets", J. Banking & Finance):** identifizieren 13 profitable Momentum-Strategien mit durchschnittlich **9,38% p.a.** Rendite über verschiedene Formations-/Halteperioden (bis 12 Monate). Die profitabelste Variante (12-Monats-Formation, 1-Monats-Halteperiode) erzielt **~15% p.a.** brutto. Bestätigung: Long-Seite besteht überwiegend aus backwardierten, Short-Seite aus contangoierten Kontrakten — Konsistenz mit Basis-Story, aber auch Hinweis auf Redundanz zum Basis-Faktor.
- **Shen, Szakmary & Sharma (2007)** und weitere Re-Examinations bestätigen signifikante Profitabilität für Formations-/Halteperioden von 9–12 Monaten in ähnlichen Größenordnungen.
- **Bakshi, Gao & Rossi (2019):** Momentum als eigenständiger dritter Faktor neben Average- und Carry-Faktor notwendig, um Querschnitt zu erklären — Zwei-Faktor-Modelle ohne Momentum werden statistisch verworfen.

### d) Out-of-Sample-/Post-Publication-Evidenz

**Crowding-Evidenz (zentrales Ergebnis für dieses Urteil):** Eine Crowding-Kennzahl (Abweichung der Positionierung nicht-kommerzieller Trader vom langfristigen Mittel, skaliert am Open Interest) zeigt: **eine Standardabweichung Anstieg der Crowding-Kennzahl reduziert die annualisierte Momentum-Faktor-Rendite um rund 8 Prozentpunkte** — eine Größenordnung, die etwa der Hälfte bis zwei Dritteln der ursprünglich dokumentierten Brutto-Prämie (9–15% p.a.) entspricht. Die Studie liefert zudem eine explizite Erklärung, warum Commodity-Momentum-Renditen in jüngeren Jahren niedrig ausgefallen sind: Crowding sagt Momentum-Renditen auch nach Kontrolle für vergangene Exzess-Renditen und Investoren-Flows vorher.

**Marktbreite Trendfolge-Performance 2011–2026:** Der SG CTA Index (breiter, nicht rein-Commodity, aber stark rohstoffgetrieben) erzielte seit Januar 2000 eine Sharpe Ratio von **0,61** und über 2000–2021 eine Rendite von rund **4,5% p.a.** bei ~11% Vol. Die Periode 2011–2013 gilt in der Branche selbst als besonders schwach für Trendfolgemodelle ("verlorenes Jahrzehnt"), mit partieller Erholung erst in Einzeljahren wie 2014, 2019, 2022 (Energiekrise). Neuere Daten (Trailing bis Februar 2026) zeigen für den SG CTA Index nur **3,16% annualisiert**, was auf anhaltend gedämpfte Performance im aktuellen Regime hindeutet — allerdings ist dies ein Multi-Asset-Index (Aktien-, Zins-, Devisen- und Rohstoff-Futures gemeinsam), sodass die reine Rohstoff-Momentum-Komponente daraus nicht isoliert werden kann; die Zahl dient nur als grober Proxy für das Umfeld systematischer Futures-Trendfolge.

**Decay-Schätzung:** Kombiniert man die Crowding-Elastizität (~8 Prozentpunkte pro Std.-Abw.) mit der beobachteten strukturellen Zunahme von Managed-Futures-/Index-Kapital seit 2004, ist ein Decay von **50–70% der ursprünglichen Brutto-Prämie** plausibel — d.h. von ehemals 9–15% p.a. brutto auf geschätzt 3–6% p.a. brutto im Post-2010-Regime, vor Kosten.

### e) Kosten

Monatliches Rebalancing über 20–30 Rohstoffe mit Ranking-basierter Neugewichtung erzeugt deutlich höheren Turnover als eine reine Carry-Strategie. Realistische Kostenschätzungen (Bid-Ask plus Marktimpact) liegen – je nach Liquiditätsmix des Universums – im Bereich mehrerer Prozentpunkte p.a., was bei einer bereits durch Crowding auf 3–6% geschätzten Brutto-Prämie einen erheblichen Anteil der Rendite aufzehrt. Explizit dokumentiert: "Transaction costs erode the economic gains of momentum strategies due to high portfolio turnover" — ein in der Literatur wiederkehrender Befund.

### f) Kapazität und Handelbarkeit

Ähnlich Kandidat 1: CFTC-Positionslimits und Liquiditätsgrenzen in kleineren Agrar-/Vieh-Kontrakten begrenzen die Skalierbarkeit eines breit diversifizierten Momentum-Programms. Da Momentum zusätzlich höheren Turnover benötigt, ist die effektive Kapazität pro investiertem Dollar tendenziell niedriger als bei Carry (mehr Market Impact pro Signaländerung).

### g) Regimeabhängigkeit und Tail-Risiko

Klassisches "Momentum-Crash"-Risiko: abrupte V-förmige Preisumkehrungen (wie der Ölpreiskollaps Anfang 2020 und die anschließende extreme Erholung) können bestehende Trendpositionen abrupt gegen die Strategie laufen lassen. Rohstoff-Momentum ist zudem stark durch makroökonomische Schock-Cluster (Angebotsschocks, geopolitische Ereignisse, Zentralbankpolitik) getrieben, was zu Regime-Klumpenrisiko über mehrere Rohstoffe gleichzeitig führt (geringere effektive Diversifikation als die Kontraktzahl suggeriert).

### h) Bekannte Kritik/Widerlegungen

- **Redundanz zu Basis-Faktor:** Da Momentum-Long-Positionen überwiegend backwardierte Kontrakte sind, ist unklar, wie viel "echtes" inkrementelles Alpha Momentum gegenüber einer reinen Basis-Strategie liefert (Multikollinearität, s.o.).
- **Multiple Testing:** Miffre & Rallis testen 13+ Parameterkombinationen (Formations-/Halteperioden) und berichten die beste(n) als Hauptergebnis — ein klassisches Setup für Overfitting-Risiko trotz nachträglicher Robustheitschecks.
- **Crowding-Kritik ist selbstwidersprüchlich für die Kandidatur:** Die gleiche Literatur, die die Existenz des Faktors bestätigt, liefert auch den stärksten Beleg für dessen Erosion — ein seltener Fall, in dem Bestätigungs- und Widerlegungsevidenz aus derselben Quelle stammen.

**Urteil: WEAK.** Ökonomisch schwächer fundiert als Carry (keine klare nicht-profitmaximierende Gegenseite, teils Redundanz zum Basis-Signal), mit der am klarsten dokumentierten Decay-Evidenz (Crowding-Elastizität) aller drei Kandidaten. Nach realistischen Kosten ist eine positive Netto-Sharpe-Ratio nicht ausgeschlossen, aber unsicher und klein.

---

## Kandidat 3: Hedging-Pressure-Faktor (Commercial Hedging Pressure, Basu & Miffre 2013)

### a) Ökonomische Begründung

Direkteste Operationalisierung der Keynes/Hicks-Theorie: statt der Preis-Basis wird die tatsächliche Positionierung kommerzieller Hedger aus den CFTC Commitments-of-Traders-Daten (COT) verwendet, um Long-Short-Portfolios zu bilden (long Rohstoffe, in denen Hedger stark netto-short sind = hohe Insurance-Nachfrage = hohe erwartete Prämie für Spekulanten; short Rohstoffe mit gegenteiliger Positionierung). Theoretisch ist dies die "sauberste" Operationalisierung der ökonomischen Grundgeschichte, weil sie direkt am Mechanismus (Positionierung) statt an einem Preis-Proxy (Basis) ansetzt.

### b) Limits to Arbitrage

Wie Kandidat 1, plus: COT-Daten werden nur wöchentlich mit Verzögerung veröffentlicht (Reporting-Lag von mehreren Tagen), was Hochfrequenz-Ausnutzung ausschließt und Slippage zwischen Signal und Umsetzung erzeugt.

### c) Originalstudien

**Basu & Miffre (2013, "Capturing the Risk Premium of Commodity Futures: The Role of Hedging Pressure"):** konstruieren Faktor-mimicking-Portfolios basierend auf Commercial Hedging Pressure (CHP) als Proxy für Hedger-Nettopositionierung und zeigen eine signifikante Verbindung zwischen Hedging Pressure und Rohstoff-Risikoprämien in einer Teilstichprobe. Wichtig für die adversariale Bewertung: der von den Autoren selbst berichtete Effekt ist in späteren Teilperioden (nach Financialization) deutlich schwächer bzw. statistisch nicht mehr robust — ein in der Sekundärliteratur wiederholt aufgegriffener Befund, dass die Hedging-Pressure-Prämie ihre Signifikanz nach 2004 weitgehend verliert.

### d) Out-of-Sample-/Post-Publication-Evidenz

Zwei strukturelle Probleme verschärfen sich speziell für diesen Faktor seit 2009:

1. **CFTC-Reklassifizierung:** Mit Einführung der Disaggregated COT Reports (2009) wurden Marktteilnehmer neu klassifiziert (u.a. "Swap Dealers" als eigene Kategorie abgespalten). Das bricht die Zeitreihenkontinuität der "Commercial"-Kategorie, auf der die gesamte Hedging-Pressure-Logik beruht.
2. **Kontamination der "Commercial"-Kategorie durch Indexinvestoren:** Viele Swap-Dealer, die im Auftrag von Long-only-Indexanlegern (Pensionsfonds, ETFs) agieren, werden/wurden als "Commercial" statt "Non-Commercial" eingestuft, obwohl sie ökonomisch keine Produzenten-Hedger sind, sondern strukturelle, preisunsensitive Long-Nachfrage darstellen. Das verwässert genau die Unterscheidung (echter Hedger vs. Spekulant), auf der die Theorie beruht, und ist ein zentraler, in der Literatur zur Financialization breit diskutierter Kritikpunkt.

Konkrete, unabhängige (nicht-Autoren-) Post-2015-Replikationsstudien mit vergleichbaren t-Statistiken waren in der Recherche nicht auffindbar — ein Negativbefund, der für sich genommen bereits gegen eine CANDIDATE-Einstufung spricht (fehlende Reproduktion ist per Auftrag gleichbedeutend mit Nicht-Bestehen des Kriteriums).

### e) Kosten

Ähnlich Kandidat 1 (Basis), zusätzlich durch Reporting-Lag der COT-Daten leicht erhöhtes Timing-/Slippage-Risiko.

### f) Kapazität und Handelbarkeit

Vergleichbar Kandidat 1, aber praktisch geringere Handelbarkeit, weil das Signal nur wöchentlich aktualisiert wird und viele Marktteilnehmer bereits systematisch auf COT-Daten schauen (CFTC-Daten sind seit Jahrzehnten frei verfügbar und extrem bekannt in der Trading-Community) — das spricht gegen einen strukturellen Informationsvorteil und für frühzeitige Arbitrierung durch andere Marktteilnehmer.

### g) Regimeabhängigkeit und Tail-Risiko

Analog Kandidat 1 (Storage-/Lieferkrisen), zusätzlich verstärkt durch das Risiko, dass sich die COT-"Commercial"-Klassifizierung in Krisenzeiten (z.B. massive Indexfonds-Rebalancing-Flows) besonders stark von der ökonomischen Realität entkoppelt.

### h) Bekannte Kritik/Widerlegungen

- **Fehlende Eigenständigkeit:** Wie oben erläutert korreliert Hedging Pressure stark mit der Basis (beide sind Proxies für dieselbe zugrundeliegende Marktspannung), sodass der inkrementelle Erklärungsgehalt gegenüber einer reinen Basis-Strategie fraglich ist.
- **Datenqualitätsbruch 2009:** Die Reklassifizierung ist ein "Strukturbruch", der lange, konsistente Backtests über die Financialization-Periode hinweg methodisch erschwert.
- **Bekanntheitsgrad:** COT-Daten sind seit Jahrzehnten öffentlich und werden breit von der Trading-Community beobachtet (z.B. "COT-Report-Trading" als verbreitete Retail- und CTA-Praxis), was gegen persistentes Alpha aus einem so gut beobachteten Signal spricht.

**Urteil: KILL.** Kein robuster, von der Basis-Strategie unabhängiger Signalgehalt; strukturelle Datenqualitätsprobleme seit 2009; keine überzeugende unabhängige Post-Publication-Bestätigung auffindbar. Als eigenständiger handelbarer Faktor nicht empfehlenswert — höchstens als Diagnose-/Kontroll-Variable innerhalb einer Basis-Strategie sinnvoll, nicht als eigener Trade.

---

## Gesamtfazit und Einordnung

Die Anomalieklasse Rohstoffe & Futures zeigt ein für institutionelle Multi-Faktor-Forschung typisches Muster: **eine ökonomisch gut begründete, historisch signifikante Prämie (Basis/Carry), die durch massiven Kapitalzustrom (Financialization 2004–2008, dauerhaft erhöhte Index- und CTA-Assets seither) strukturell erodiert wurde.** Die beste verfügbare Evidenz (BCOM-Performance 5,1% p.a. über die letzten 10 Jahre vs. 13,7% p.a. S&P 500; SG-CTA-Sharpe 0,61 seit 2000, aber nur ~3,16% annualisiert zuletzt; dokumentierte Crowding-Elastizität von ~8 Prozentpunkten pro Std.-Abw. für Momentum) deutet auf eine Halbierung bis Zwei-Drittel-Reduktion der ursprünglich dokumentierten Bruttoprämien hin. Nach realistischen Rollkosten, Spreads in illiquiden Kontrakten und CFTC-Positionslimits, die die Kapazität in kleineren Märkten hart begrenzen, bleibt für Basis/Carry und Momentum jeweils bestenfalls eine **kleine positive Netto-Sharpe-Ratio im Bereich 0,1–0,35** übrig — plausibel als Diversifikations-Baustein in einem Multi-Strategie-Portfolio, aber kein eigenständig überzeugendes Alpha-Signal.

Der Hedging-Pressure-Faktor als direkte COT-basierte Operationalisierung der Theorie ist am schwächsten: zu stark redundant mit Basis, methodisch durch die CFTC-Reklassifizierung 2009 beschädigt, und ohne auffindbare unabhängige Post-2015-Bestätigung.

**Ehrliche Einordnung im Sinne des Mandats:** Diese Anomalieklasse ist nicht vollständig tot, aber sie ist **von einer "freien Mittagsmahlzeit" (Ineffizienz) zu einer knapp bezahlten, stark konkurrierten Risikoprämie geschrumpft.** Kein Kandidat erreicht die geforderte Kombination aus dokumentierter Post-Publication-Evidenz UND Kostenrobustheit, die für ein CANDIDATE-Urteil nötig wäre. Für ein institutionelles Mandat mit Nullhypothese "kein echtes Alpha" ist das Ergebnis: **die Nullhypothese kann für keinen der drei Kandidaten verworfen werden.**

### Hinweis zur Multiple-Testing-Problematik der Gesamtklasse

Die akademische Rohstoff-Futures-Literatur hat seit Erb & Harvey (2006) und Gorton & Rouwenhorst (2006) buchstäblich Dutzende Sortiervariablen getestet (Basis, Momentum, Hedging Pressure, Volatilität, Skewness, Liquidität, Open-Interest-Änderungen, Inflation-Beta, etc. — u.a. bei Szymanowska et al. 2014 und Bakshi/Gao/Rossi 2019 explizit als Multi-Signal-Sortierungen). Bei einem so breiten Signal-Universum und typischen Einzel-t-Statistiken im Bereich 2–3 ist nach Harvey/Liu/Zhu-Standards (t>3,0 gefordert) eine relevante Zahl der berichteten Ergebnisse als nicht robust gegenüber Multiple-Testing-Korrektur einzustufen. Das senkt die in den YAML-Scores vergebenen "signifikanz_nach_mtk"-Werte bewusst auf 2–3 statt 4–5.

### Datenzugriffs-Hinweis für Testbarkeit

Für eine unabhängige Prüfung mit frei zugänglichen Daten:
- **CFTC Commitments of Traders** (https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm): frei, wöchentlich, Legacy-Reports seit 1986, Disaggregated seit 2006 — geeignet für Hedging-Pressure-Proxy und als Crowding-Kontrollvariable.
- **AQR "Value and Momentum Everywhere" Datensatz** (aqr.com/Insights/Datasets): frei, monatlich, enthält Commodity-Value- (Basis-Proxy) und Commodity-Momentum-Faktorrenditen über mehrere Jahrzehnte, laufend aktualisiert — die derzeit beste frei zugängliche Möglichkeit, beide Kandidaten 1 und 2 grob nachzubilden, ohne selbst eine vollständige Terminkurve konstruieren zu müssen.
- **Yahoo Finance/Stooq Frontmonth-Continuous-Futures** (CL=F, GC=F, SI=F, HG=F, NG=F, ZC=F, ZW=F, ZS=F, KC=F, CT=F, SB=F, LE=F, HE=F etc.): frei, aber nur Front-Month-Continuous-Contracts mit Backadjustierungs-/Splicing-Artefakten — ausreichend für einfache Momentum-Backtests, ungeeignet für exakte Basis-Berechnung (dafür wird mindestens ein zweiter Kontraktmonat pro Rohstoff benötigt, was zuverlässig i.d.R. nur über kostenpflichtige Anbieter wie Bloomberg, CSI Data oder Norgate verfügbar ist).

Ein Ken-French-Dataset existiert für diese Klasse nicht (French deckt nur Aktien-/Anleihe-Faktoren ab); AQR ist hier der beste Ersatz.
