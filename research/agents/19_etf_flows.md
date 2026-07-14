```yaml
agent: 19
klasse: "ETF-Flows"
websuche_verfuegbar: ja
strategien:
  - name: "Leveraged-ETF-Rebalancing Front-Running (End-of-Day)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 1
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.25
    netto_sharpe_erwartung: "0.0-0.3 (regimeabhaengig, meist ~0 im Normalregime, temporaer hoeher in Krisen-Clustern)"
    kernrisiko: "Effekt existiert fast ausschliesslich in kurzen Stress-Clustern (Okt/Nov 2008); im Normalregime statistisch/oekonomisch insignifikant laut 2024-Survey; Crowding durch bekannte Deterministik seit >15 Jahren"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Yahoo/Stooq Intraday-Kurse SSO/SDS/TQQQ/SQQQ + SPX Tagesdaten; kein Ken-French-Datensatz einschlaegig"

  - name: "ETF-Premium/Discount NAV-Arbitrage (Nicht-AP-Perspektive)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 3
      handelbarkeit: 1
      kapazitaet: 2
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "~0.0-0.1 fuer Nicht-APs nach Kosten; AP-Segment nicht zugaenglich/nicht Teil des Mandats"
    kernrisiko: "Geschaeftsmodell strukturell APs/Market-Makern mit Realzeit-Creation/Redemption vorbehalten; Restopportunitaet (Petajisto) konzentriert in illiquiden/internationalen ETFs mit hohen Handelskosten, die die 7% Brutto-Abnormal-Return auffressen"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "-"

  - name: "Monatsende-Rebalancing-Flows / Turn-of-the-Month (Multi-Asset- und Indexfonds)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.25
    netto_sharpe_erwartung: "0.1-0.3 brutto, ~0.0-0.15 netto nach Transaktionskosten und Crowding"
    kernrisiko: "Kausalmechanismus (Flow-getrieben) durch eigene Originalstudien widerlegt bzw. nicht durch Fondsflows erklaerbar; Alternativerklaerung (Risk-Deferral) ist keine reine ETF-Flow-Anomalie und daher ausserhalb des engen Mandats"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Daily/Monthly Factors (Mkt-RF) fuer Turn-of-Month Replikation"
```

# ETF-Flows: Adversarial Review (Agent 19)

## Zusammenfassung des Urteils

Die Klasse "ETF-Flows" liefert **keinen robusten CANDIDATE**. Alle drei geprüften Strategiekandidaten bleiben unter der Schwelle für ein CANDIDATE-Urteil (dokumentierte Post-Publication-Evidenz UND Kostenrobustheit). Der glaubwürdigste Kandidat — Leveraged-ETF-Rebalancing-Front-Running — hat einen sauberen ökonomischen Mechanismus (deterministisches Rebalancing), aber die empirische Evidenz zeigt: (a) Effekt ist statistisch nachweisbar, aber ökonomisch nach Kosten meist insignifikant, (b) er konzentriert sich fast ausschließlich auf kurze Stresscluster (Herbst 2008), (c) eine aktuelle Literatur-Survey (2024) kommt zum Schluss, dass der Markt ausreichend Liquidität bereitstellt, um Rebalancing-Bedarf ohne signifikante Marktqualitätsverschlechterung zu absorbieren. NAV-Arbitrage ist per Konstruktion das Geschäft der Authorized Participants (AP) — was für Nicht-APs übrig bleibt, ist eine Restopportunität in illiquiden/internationalen ETFs, die nach Kosten kaum tragfähig ist. Monatsende-Rebalancing-Flows sind real und robust nachweisbar über Jahrzehnte/Länder hinweg, aber die Originalstudien selbst widerlegen den Flow-Kausalmechanismus als Haupterklärung — das schwächt die Zuordnung zur Klasse "ETF-Flows" im engen Sinn.

---

## Kandidat 1: Leveraged-ETF-Rebalancing Front-Running (End-of-Day)

### a) Ökonomische Begründung

Leveraged/Inverse-ETFs (LETFs, z.B. SSO/SDS 2x, TQQQ/SQQQ 3x) müssen täglich ihr Exposure zurücksetzen, um konstante Hebelfaktoren gegenüber dem NAV zu halten. Das ist **mechanisch deterministisch**: Bei einem positiven Tagesreturn des Referenzindex muss ein Long-2x-Fonds zusätzliche Exposure kaufen (weil das Dollar-Exposure überproportional zum NAV gestiegen ist), ein Short-Fonds muss ebenfalls in Richtung Marktbewegung handeln (covering bei Marktanstieg). Diese Flows sind Betrag und Richtung nach aus dem Tagesreturn bis ca. 15:30/15:45 Uhr NY-Zeit approximierbar, bevor der Handel typischerweise nahe dem Closing-Auktion/4pm-Fixing stattfindet. Cheng & Madhavan (2009) formalisieren dies als eingebettete pfadabhängige Option: Bei Kursanstieg "buy high", bei Kursverlust "sell low" — ein prozyklischer, nicht-fundamentaler Flow, der in der Theorie Volatilität gegen Handelsschluss verstärkt, besonders bei extremen Tagesbewegungen (Multiplikator-Effekt: Rebalancing-Bedarf ≈ (Hebel² − Hebel) × Tagesreturn × Fondsvermögen).

### b) Limits to Arbitrage

- **Zeitfenster-Kompression**: Die profitabelste Ausführung liegt nahe am 4pm-Closing-Fixing; institutionelle Akteure (inkl. der ETF-Anbieter selbst über Swap-Kontrahenten) haben Preisvorteile durch VWAP/TWAP-Algorithmen und direkten Marktzugang.
- **Informationsvorsprung ist öffentlich**: Der Mechanismus ist seit >15 Jahren bekannt (Cheng/Madhavan 2009 publiziert), jeder quantitative Marktteilnehmer kann den erwarteten Flow aus AUM-Daten (öffentlich, täglich) und Tagesreturn approximieren — daher strukturell crowding-anfällig.
- **Gegenläufige Liquiditätsbereitstellung**: Wenn Rebalancing-Bedarf antizipierbar ist, haben Market-Maker einen Anreiz, dagegen Liquidität bereitzustellen (genau das findet Brøgger 2021 für VIX-Produkte, siehe unten) — das drückt die Preiswirkung und damit die Profitabilität des Front-Runnings.
- **Basisrisiko**: Wetten auf Rebalancing-Richtung sind faktisch Wetten auf Fortsetzung der Tagesbewegung in die Closing-Auktion — bei Reversal-Tagen (nicht selten) verliert die Strategie.

### c) Originalstudien

**Cheng & Madhavan (2009)**, "The Dynamics of Leveraged and Inverse Exchange-Traded Funds", Journal of Investment Management. Theoretischer/deskriptiver Rahmen (keine Handelsstrategie mit Sharpe-Zahlen), zeigt: tägliches Re-Leveraging erzeugt Mikrostruktur-Effekte, verstärkt Volatilität zum Handelsschluss; bei hoher Volatilität erodiert der Median-Investor langfristig Wert (Volatility Decay).

**Shum, Hejazi, Haryanto, Rodier (2012)**, "Intraday Share Price Volatility and Leveraged ETF Rebalancing" — die zentrale quantitative Originalstudie:
- Stichprobe: Juni 2006 – Juli 2011, 346 großkapitalisierte US-Aktien, SSO/SDS, Intraday-Daten in 15-Minuten-Intervallen.
- Strategie 1 (Kauf SSO/Verkauf SDS um 14:45 Uhr bei ≥2% Marktbewegung, Glattstellung zum Close): Ø Brutto-Return/Trade 0,60%, kumulierter Brutto-Return 104% über 5 Jahre, 128 Trades, davon 34% Verlusttrades.
- Strategie 2 (Signal um 14:30 Uhr + Rebalancing-Magnitude): Ø 0,66%/Trade, kumuliert 119%, 127 Trades, 35% Verlusttrades.
- **Kritischer Befund zur Konzentration**: Gewinne konzentrieren sich zu ~80%+ auf einen Zeitraum von 2,5 Monaten in Q4 2008 (Finanzkrise); die Strategie handelt in den Jahren 2006, 2007 und 2011 gar nicht oder kaum (keine Signale ausgelöst).
- Aggregiertes Rebalancing erklärt geschätzt ~ein Drittel der Late-Day-Renditevolatilität im Schnitt, an Extremtagen (≥3% Bewegung bis 15:30) über 50%.
- Die Autoren selbst nennen die Breakeven-Handelsfriktion bei ~0,60% — d.h. die durchschnittliche Bruttorendite pro Trade liegt praktisch AUF der Kostenschwelle, nicht darüber hinaus.

### d) Out-of-Sample-/Post-Publication-Evidenz und Decay

Die stärkste verfügbare Evidenz stammt aus einer **direkt vergleichbaren, methodisch saubereren Studie zu einem strukturgleichen Produkt**: Brøgger (2021), "The Market Impact of Predictable Flows: Evidence from Leveraged VIX Products", Journal of Banking & Finance. Kernbefunde:
- Leveraged-VIX-ETPs erzeugen tägliche Rebalancing-Flows mit bekannter Größe, Vorzeichen und Timing — strukturell identisch zum LETF-Aktienfall, aber mit saubereren Daten (VIX-Futures-Markt).
- Tägliches Rebalancing verursacht messbare implizite Kosten für die ETP-Investoren selbst.
- **Aber**: Größere und vorhersagbarere Flows haben KLEINERE Preiswirkungskoeffizienten (Gegenteil der "Predatory Trading"-Hypothese) — Liquiditätsanbieter positionieren sich antizipatorisch und dämpfen den Preisdruck.
- **Front-Running ist nach Transaktionskosten nicht profitabel.** Dies ist eine explizite, direkte Widerlegung der Handelsstrategie-Implikation von Shum et al. (2012) in einem strukturell verwandten, aber jüngeren Produktsegment.
- Öffentliche Offenlegung des Rebalancing-Bedarfs fördert zusätzliche Liquiditätsbereitstellung, die die Marktwirkung weiter mindert — ein sich selbst korrigierender Mechanismus.

Zusätzlich: Eine **2024-Literatur-Survey** ("The market impact of leveraged ETFs: A Survey of the literature", AIMS Press, Quantitative Finance and Economics) fasst die gesamte Literatur seit Cheng/Madhavan zusammen:
- Statistisch signifikante Assoziationen zwischen LETF-Rebalancing-Bedarf und Late-Day-Returns/Volatilität sind in vielen Studien nachweisbar, ABER die **ökonomischen Assoziationen erweisen sich als insignifikant**, sobald methodische Probleme (u.a. Endogenität, Look-Ahead in der Signalkonstruktion) korrigiert werden.
- "Die breitere Literatur legt nahe, dass der Markt genug Liquidität bereitstellt, um LETF-Rebalancing-Nachfrage mit insignifikanter Verschlechterung der Marktqualität zu absorbieren."
- Klare Diskrepanz zwischen regulatorischer/politischer Besorgnis (SEC, Fed) und der empirischen Evidenz — Sorgen sind nicht durch die Gesamtevidenz gestützt.

**Decay-Schätzung**: Die einzige robuste Profitabilitätsperiode (Q4 2008) fällt mit einem AUM- und Volatilitätsregime zusammen, das seither in dieser Form (VIX-Spikes >60-80, tagelang anhaltend) selten wiederkehrte (am ehesten März 2020, kurzzeitig). Bei ruhigen/normalen Regimen (der überwiegende Teil der Zeit seit 2011) ist die Strategie inaktiv oder verlustträchtig. Insofern ist "Decay" hier eher ein **Regime-Konzentrations-Artefakt** als klassischer post-Publikations-Alpha-Zerfall: Es gab nie ein robustes Alpha außerhalb von Tail-Events — das 2008-Ergebnis war vermutlich zu großen Teilen datamining-getrieben (die Autoren selbst räumen Data-Snooping-Bias ein) plus echtes, aber sehr seltenes Tail-Phänomen.

### e) Kosten: Intraday-Handel nötig — Nettorendite-Realität

- Erfordert Intraday-Marktzugang, Echtzeit-AUM/NAV-Daten der LETFs (kostenpflichtig/verzögert bei Retail-Feeds), präzises Timing um 14:30-15:45 Uhr NY-Zeit.
- Slippage/Market Impact beim eigenen Trade ist in der Originalstudie nicht enthalten (nur Geld-Brief-unbereinigte Kassakurse) — bei 0,60% durchschnittlichem Bruttoertrag pro Trade frisst realistischer Slippage (Aktien mit erhöhtem Handelsvolumen exakt in der Phase, in der auch alle anderen antizipatorisch handeln) einen erheblichen Teil auf.
- Brøgger (2021) zeigt explizit: netto nach Kosten nicht profitabel für das strukturell verwandte VIX-Produktsegment.
- Given Crowding (jeder kennt die AUM-Zahlen und die Formel), ist die realistische Erwartung: Bruttorendite nahe Kostenschwelle, Nettorendite ≈ 0 im Normalfall, ggf. leicht positiv in extremen, seltenen Tail-Events (aber dort auch höheres Ausführungsrisiko/Liquiditätslücken).

### f) Kapazität und Handelbarkeit

- US-Leveraged-ETF-Markt erreichte 2026 ein Rekordvolumen von ca. USD 198 Mrd. AUM (von ~USD 170 Mrd. sechs Monate zuvor, +ca. 16%), TQQQ allein USD 30-40 Mrd., tägliches Handelsvolumen der liquidesten LETFs branchenweit ca. USD 45 Mrd./Tag.
- Auf den ersten Blick suggeriert das große absolute Kapazität. Aber: Der antizipierbare **Rebalancing-Bedarf** (nicht das Handelsvolumen) skaliert nur mit der Tagesbewegung und ist typischerweise eine kleine Größenordnung relativ zum gesamten Marktvolumen der zugrundeliegenden Basiswerte (S&P 500, Nasdaq-100) — bei ~3-8 Mrd. USD taeglichem Rebalancing-Bedarf gegen ein Vielfaches an Marktliquidität in den Basiswerten. Die verfügbare "Opportunity" pro Tag ist klein; verteilt auf die vielen bekannten/systematischen Akteure, die dasselbe Signal beobachten, bleibt pro Akteur nur ein Bruchteil.
- Kapazität der Strategie selbst (nicht des Produktmarkts) wird auf niedrig eingeschätzt (Score 1/5): das handelbare Alpha ist auf wenige Extremtage im Jahr konzentriert, mit begrenzter Positionsgröße bevor der eigene Handel den erwarteten Effekt selbst auffrisst (Marktwirkung linear/konvex mit Ordergröße in der Schlussauktion).

### g) Regimeabhängigkeit und Tail-Risiko

- Strategie ist **extrem regimeabhängig**: nur profitabel (wenn überhaupt) an Tagen mit Marktbewegung ≥2-3% — d.h. faktisch eine Wette auf/mit hoher Realized Volatility, korreliert mit Tail-Risk-Regimen (Krisen, Crashes).
- Adverse Selektion: An genau den Tagen, an denen das Signal am stärksten ist (z.B. Flash-Crash-artige Bewegungen), ist auch die Ausführungsqualität am schlechtesten (breite Spreads, Liquiditätslücken, Handelsunterbrechungen) — die Strategie ist daher am unzuverlässigsten genau dann, wenn sie am nötigsten wäre.
- Tail-Risiko: Bei Fehleinschätzung der Richtung (z.B. Intraday-Reversal nach starker Anfangsbewegung, wie es an vielen Crash-Tagen vorkommt) sind Verluste asymmetrisch groß, weil Positionsgrößen genau in Hochvolatilitätsphasen aufgebaut werden.

### h) Bekannte Kritik/Widerlegungen

- Shum et al. (2012) selbst: Data-Snooking-Warnung, keine Kontrolle für realistische Ausführungskosten, keine Out-of-Sample-Validierung nach 2011.
- Brøgger (2021): direkte, methodisch stärkere Widerlegung der Profitabilität-nach-Kosten-These im strukturell verwandten Produktsegment (VIX statt Aktienindex, aber gleicher Mechanismus).
- AIMS-Press-Survey (2024): Meta-Kritik an der gesamten Literatur — viele Studien mit "potenziell schwerwiegenden methodischen Fehlern"; ökonomische Signifikanz verschwindet nach Korrektur.
- Regulatorische Bedenken (SEC-Kommentare zu Leveraged-ETF-Regeln, z.B. Rule 6c-11/18f-4-Diskussion) sind vorhanden, aber die Survey-Literatur stützt diese Bedenken nicht empirisch.

**Urteil: WEAK.** Der Mechanismus ist real und deterministisch, aber die dokumentierte historische Profitabilität ist auf ein extremes Tail-Event (2008) konzentriert, eine methodisch stärkere Nachfolgestudie zu einem strukturell identischen Produkt widerlegt Netto-Profitabilität explizit, und eine aktuelle Survey (2024) bestätigt fehlende ökonomische Signifikanz nach Kontrolle für Methodik. Kein CANDIDATE, da keine robuste, kostenrobuste Post-Publication-Evidenz vorliegt — im Gegenteil, die beste verfügbare Post-Publication-Evidenz spricht dagegen.

---

## Kandidat 2: ETF-Premium/Discount NAV-Arbitrage (aus Nicht-AP-Perspektive)

### a) Ökonomische Begründung

ETFs sollten durch den Creation/Redemption-Mechanismus nahe am NAV handeln. Abweichungen (Premium/Discount) entstehen durch: Stale Pricing der zugrunde liegenden Basiswerte (unterschiedliche Handelszeiten, z.B. internationale ETFs während US-Handelszeiten), Liquiditätsengpässe, temporäre Angebots-/Nachfrageungleichgewichte, oder AP-Inventar-Constraints.

### b) Limits to Arbitrage — hier der entscheidende Punkt für das Mandat

Der Kern-Arbitragemechanismus (Creation/Redemption zum NAV) ist **strukturell APs und designierten Market-Makern vorbehalten**: Diese haben (i) direkten, gebührenfreien/-günstigen Zugang zum Creation/Redemption-Prozess, (ii) Echtzeit-Fair-Value-Modelle für die Basiswerte, (iii) Bilanzkapazität, um Inventar zu halten, (iv) Kolokation/Latenzvorteile. Für Nicht-APs (auch institutionelle, aber ohne AP-Status) verbleibt nur die sekundärmarktliche Wette auf Konvergenz von Preis zu NAV — mit denselben Kostennachteilen wie jeder andere Marktteilnehmer.

### c) Originalstudien

**Petajisto (2017)**, "Inefficiencies in the Pricing of Exchange-Traded Funds", Financial Analysts Journal (Graham & Dodd Award 2017):
- Methodik: Kontrolle für Stale-NAV-Pricing mittels Querschnitts-Ansatz über Gruppen ähnlicher ETFs.
- Durchschnittliches Pricing-Band: ~100-200 Basispunkte (roh ~200bp, nach Stale-Pricing-Korrektur ~100bp, ökonomisch weiterhin signifikant).
- Größte Fehlbepreisungen bei internationalen und illiquiden-Basiswert-ETFs.
- Aktive Handelsstrategien, die diese Ineffizienzen ausnutzen, erzeugen **~7% abnormale Bruttorendite** (vor Transaktionskosten) — Gewinne konzentriert in internationalen und illiquiden-Segment-ETFs — also exakt dort, wo Handelskosten am höchsten sind.

### d) Out-of-Sample-Evidenz

Post-2017-Literatur (u.a. ESRB Working Paper 2017 zu "ETF arbitrage under..." sowie diverse Studien zu AP-Verhalten während Marktstress, z.B. "dash for cash" 2020) zeigt: Der Arbitragemechanismus kann sich verzerren, wenn APs Creation/Redemption strategisch nach eigenem Inventar statt reiner Mispricing-Korrektur einsetzen — das kann größere, nicht kleinere relative Fehlbepreisungen erzeugen, besonders in Stressphasen (Corporate-Bond-ETFs im März 2020 zeigten Discounts von mehreren Prozentpunkten). Das ist aber überwiegend AP/Dealer-Geschäft (Pan & Zeng 2019, u.a. zu Bond-ETF-APs als gleichzeitige Bond-Dealer) — für externe Arbitrageure bleibt selbst in Stressphasen der Zugang zum tatsächlichen Creation/Redemption-Schritt verschlossen, sie können höchstens sekundärmarktlich (ETF-Aktie gegen Futures/Basket-Proxy) hedgen, was Basisrisiko und Finanzierungskosten mit sich bringt.

### e) Kosten

Für Nicht-APs: Keine Möglichkeit, den NAV-Konvergenz-Mechanismus direkt zu erzwingen (kein Creation/Redemption-Zugang) — Position muss über Sekundärmarkt-Reversal warten, mit Haltekosten, Basisrisiko und ohne institutionelle Kostenvorteile. Die 7%-Bruttorendite bei Petajisto konzentriert sich in genau den Segmenten (international, illiquide) mit den höchsten Bid-Ask-Spreads und Finanzierungskosten für Leerverkäufe/Hedges.

### f) Kapazität und Handelbarkeit

Sehr gering für Nicht-APs. AP-Segment selbst ist mandatsseitig ausgeschlossen ("was bleibt für andere?" laut Auftrag). Score entsprechend niedrig vergeben.

### g) Regimeabhängigkeit

Größte Opportunitäten just in Stressphasen — aber genau dort auch am schwersten sekundärmarktlich zu monetarisieren ohne AP-Zugang (Finanzierungs-/Repo-Stress, Shortability-Probleme).

### h) Bekannte Kritik

Marktkonsens (Invesco-institutionelle Publikationen, akademische Übersichten): Der Arbitragemechanismus funktioniert in der überwiegenden Mehrheit der Zeit gut genug, dass verbleibende Ineffizienzen klein und für Marktteilnehmer ohne AP-Status kaum profitabel handelbar sind — die Petajisto-Ergebnisse selbst werden im Feld primär als Beleg für die Grenzen (nicht die Breite) der Opportunität zitiert.

**Urteil: KILL.** Die These aus dem Mandat bestätigt sich direkt: Was an NAV-Arbitrage-Alpha existiert, ist strukturell AP-Territorium. Der dokumentierte Rest (Petajisto) ist auf die kostenintensivsten Marktsegmente konzentriert und für Nicht-APs nach realistischen Kosten kaum tragfähig.

---

## Kandidat 3: Monatsende-Rebalancing-Flows / Turn-of-the-Month-Effekt

### a) Ökonomische Begründung

Multi-Asset-Fonds (Pensionsfonds, Mischfonds, viele auch ETF-basiert) rebalancieren häufig zu Kalendermonatswechseln auf Ziel-Allokationen zurück; zusätzlich fallen Gehaltseinzahlungen in Sparpläne/401(k)-äquivalente Programme meist auf Monatsanfang. Das sollte laut Hypothese systematischen Kaufdruck um den Monatswechsel erzeugen.

### b) Limits to Arbitrage
Falls der Effekt real und antizipierbar ist: Kalenderdaten sind öffentlich bekannt, jeder kann vorab positionieren, was den Effekt selbstkorrigierend macht — Erwartung wäre Crowding und Vorverlagerung des Preisdrucks (was auch teilweise beobachtet wird: Käufe schon vor dem eigentlichen Monatswechsel).

### c) Originalstudien
McConnell & Xu (2008), "Equity Returns at the Turn of the Month", Financial Analysts Journal: Effekt so stark (1926-2005), dass Marktrisikoprämie fast ausschließlich an Monatswechseln verdient wird; robust in 31 von 35 untersuchten Ländern.

### d) Kritischer eigener Befund der Literatur (adversarial-relevant)
**Entscheidend**: Dieselbe Literatur findet, dass der Effekt **nicht durch tatsächliche Monatsende-Kaufvolumina oder Netto-Fondsflows erklärt wird** — die naheliegendste Flow-basierte Kausalkette ist empirisch NICHT bestätigt (das ist ein seit Jahren offenes Rätsel, "puzzle in search of an answer"). Eine alternative, neuere Erklärung (Risk-Deferral/infrequentes Rebalancing durch langsames institutionelles Kapital an diskreten Kalenderpunkten, stärker nach Marktturbulenzen) ist plausibler, aber auch das ist kein direkter, mechanischer ETF-Flow-Kausalmechanismus im engen Sinn des Mandats. Eine 15-Jahres-Mutual-Fund-Studie (2005-2020, inkl. Finanzkrise und COVID) bestätigt den TOM-Effekt nur für 23 von 40 untersuchten Fonds als statistisch signifikant — keine Universalität.

### e)-h) Kosten, Kapazität, Regime, Kritik
Handelbar ohne Intraday-Zwang (im Gegensatz zu Kandidat 1), daher potenziell kostengünstiger umsetzbar (Ausführung über mehrere Tage um den Monatswechsel). Aber: Da der Kausalmechanismus selbst umstritten ist und explizit NICHT auf nachweisbaren ETF-/Fonds-Flows beruht, ist die Zuordnung zur Klasse "ETF-Flows" schwach — es handelt sich eher um eine allgemeine Kalender-Anomalie mit unklarem, möglicherweise nicht-flow-basiertem Ursprung. Für das enge Mandat (ETF-Flows spezifisch) ist dies bestenfalls ein Randkandidat.

**Urteil: WEAK.** Effekt robust dokumentiert über Jahrzehnte und Länder, aber (i) Kausalmechanismus explizit NICHT durch ETF-/Fondsflows bestätigt (Gegenteil in Originalstudien dokumentiert), (ii) nur partielle Signifikanz in jüngerer Fondsstichprobe (23/40), (iii) fällt eng ausgelegt kaum unter "ETF-Flows"-Mandat.

---

## Gesamtfazit

Die Nullhypothese hält sich robust: **Kein dokumentiertes, kostenrobustes Post-Publication-Alpha in der Klasse ETF-Flows.** Der einzige Kandidat mit sauberem, deterministischem Preisdruckmechanismus (Leveraged-ETF-Rebalancing) zeigt in der methodisch stärksten verfügbaren Folgestudie (Brøgger 2021, strukturell identisches VIX-Produktsegment) explizit **keine Netto-Profitabilität nach Kosten**, und eine aktuelle Survey (2024) bestätigt: statistisch signifikant, ökonomisch insignifikant, Markt absorbiert den Rebalancing-Bedarf ausreichend. NAV-Arbitrage bestätigt die im Mandat vorweggenommene These direkt: Es ist AP-Geschäft, der Rest ist für externe Akteure nach Kosten kaum tragfähig. Monatsende-Flows sind real, aber ihr Kausalmechanismus ist explizit NICHT als ETF-/Fonds-Flow-getrieben bestätigt.

**Empfehlung für das Gesamtportfolio der Studie**: ETF-Flows als eigenständige Alpha-Klasse für ein institutionelles Mandat ohne AP-Status ist mit hoher Wahrscheinlichkeit tot oder bestenfalls ein Nebenprodukt-Signal (z.B. als Risikofaktor/Timing-Overlay in Extremvolatilitätsregimen), nicht als eigenständige handelbare Strategie mit belastbarer positiver Netto-Sharpe-Ratio.

## Quellen (Auswahl, per Websuche verifiziert Juli 2026)

- Ben-David, Franzoni, Moussawi (2018), "Do ETFs Increase Volatility?", Journal of Finance 73(6): 2471-2535. https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12727
- Cheng, Madhavan (2009), "The Dynamics of Leveraged and Inverse Exchange-Traded Funds", Journal of Investment Management. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1393995
- Shum, Hejazi, Haryanto, Rodier (2012), "Intraday Share Price Volatility and Leveraged ETF Rebalancing". Zusammenfassung: https://www.cxoadvisory.com/volatility-effects/front-running-leveraged-etfs-at-the-end-of-the-day/
- Brøgger (2021), "The Market Impact of Predictable Flows: Evidence from Leveraged VIX Products", Journal of Banking & Finance 133. https://www.sciencedirect.com/science/article/abs/pii/S0378426621002363
- AIMS Press (2024), "The market impact of leveraged ETFs: A Survey of the literature", Quantitative Finance and Economics. https://www.aimspress.com/article/doi/10.3934/QFE.2024031
- Petajisto (2017), "Inefficiencies in the Pricing of Exchange-Traded Funds", Financial Analysts Journal 73(1): 24-54. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2000336
- Greenwood, Sammon (2022/2025), "The Disappearing Index Effect", NBER WP 30748, Journal of Finance 80(2): 657-698. https://www.nber.org/papers/w30748
- McConnell, Xu (2008), "Equity Returns at the Turn of the Month", Financial Analysts Journal 64(2). https://www.tandfonline.com/doi/abs/10.2469/faj.v64.n2.11
- Jain, Mishra, Pagano, Rodriguez (2024), "Of Seesaws and Swings: The Market-wide Impact of Levered ETF Rebalancing During Stressful Times", EFMA/SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5371016
- Cryptobriefing (2026), "US leveraged ETFs reach record $198B in assets as TQQQ and SOXL lead the charge" (Marktdaten, Juli 2026). https://cryptobriefing.com/leveraged-etfs-record-198b-aum/

Evidenzbasis: Websuche verfügbar und genutzt (Stand Juli 2026); zusätzlich internes Wissen zur Einordnung der Mechanismen.
