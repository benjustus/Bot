```yaml
agent: 11
klasse: "Faktorprämien (Value/Profitability/Investment/Quality)"
websuche_verfuegbar: ja
strategien:
  - name: "Value-Prämie (HML / Book-to-Market, inkl. moderner Value-Varianten)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 5
      kapazitaet: 5
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.3
    netto_sharpe_erwartung: "0.1-0.3"
    kernrisiko: "Mehrjähriger, potenziell jahrzehntelanger Drawdown bei strukturellem Regimewechsel (Intangibles-Ökonomie, tiefe Realzinsen, KI-Mega-Cap-Konzentration); FF5 macht HML statistisch redundant; >100 Mrd. USD Smart-Beta-Crowding"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Data Library: HML (Value) Factor, monatlich/täglich, seit 1926, plus 'Portfolios Formed on Book-to-Market'"

  - name: "Profitabilitäts-/Qualitätsprämie (Gross Profitability RMW / QMJ)"
    urteil: CANDIDATE
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 3
      regimestabilitaet: 3
      handelbarkeit: 5
      kapazitaet: 5
      kostenrobustheit: 4
    p_echte_ineffizienz: 0.4
    netto_sharpe_erwartung: "0.2-0.4"
    kernrisiko: "Mehrjährige Underperformance in spekulativen 'Junk-Rallyes' (2020/21 Reopening-Trade, 2024/25 KI-Boom bei unprofitablen Wachstumswerten); hohe Faktorüberlappung mit Value/Low-Vol; Grenzfall ob echte Ineffizienz oder Leverage-Constraint-Risikoprämie (BAB-Logik)"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Data Library: RMW (Robust Minus Weak); AQR 'Quality Minus Junk' Factors Monthly (aqr.com, kostenlos, seit 1957 bzw. global seit 1986)"

  - name: "Investment-Prämie (CMA / Asset Growth)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.25
    netto_sharpe_erwartung: "0.0-0.2"
    kernrisiko: "Weitgehend redundant zu Value/Profitability (Korrelation zu HML ≈0.7 in FF2015); Signal eng an Kapitalmaßnahmen (SEOs/Buybacks) gekoppelt → höhere Handelskosten bei kleineren/illiquideren Emittenten; hohe Ausfallrate bei Multiple-Testing-Korrektur (Hou/Xue/Zhang 2020)"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Data Library: CMA (Conservative Minus Aggressive)"
```

# Faktorprämien: Value, Profitability, Investment, Quality — Adversarial Review

**Evidenzbasis:** Websuche war verfügbar und wurde für aktuelle Daten (2015–2026), Originalstudien-Kennzahlen und Kritikliteratur genutzt (siehe Quellenangaben je Abschnitt). Für Detailzahlen aus Originalpapieren, die nicht per Volltext-Fetch verifiziert werden konnten (u.a. exakte FF1992/1993/2015-Koeffizienten), wird dies explizit als "Größenordnung aus etabliertem Lehrbuchwissen, nicht Zeile-für-Zeile verifiziert" gekennzeichnet.

## Vorbemerkung: Ist eine Risikoprämie überhaupt "Alpha"?

Das ist die zentrale Vorfrage dieses Mandats und ich beantworte sie explizit **negativ im Regelfall**: Eine Risikoprämie ist kein Alpha. Alpha im engeren Sinn ist eine risikoadjustierte Überrendite, die nicht durch Exposure zu einem systematischen, ökonomisch erklärbaren Risikofaktor erklärt wird — sie ist eine Ineffizienz, die verschwindet, sobald genug Kapital sie entdeckt und arbitriert. Eine echte Risikoprämie dagegen ist strukturell persistent, weil sie Kompensation für getragenes Risiko ist; sie verschwindet nicht durch Arbitrage, weil "Arbitrage" hier bedeutet, dass jemand das Risiko trägt und der Preis dafür sich einpendelt, nicht dass die Prämie wegkonkurriert wird. Wenn Value/Profitability/Investment-Prämien überwiegend rational-risikobasiert sind (Fama-French selbst vertreten diese Position: HML/RMW/CMA als ICAPM-State-Variablen, Zhang 2005 q-Theorie: Value-Firmen haben schwerer reversible Kapitalstöcke → höheres Risiko in Rezessionen), dann ist die "Prämie" strenggenommen **Beta, nicht Alpha** — und sie ist heute für jeden Retail-Anleger für 5-15 Basispunkte p.a. über Vanguard/iShares/DFA-ETFs erhältlich. Das allein disqualifiziert sie nicht als Kandidat für einen systematischen Hedgefonds, aber es verschiebt die Messlatte: Der Fonds müsste entweder (a) eine überlegene Implementierung liefern, die die reine ETF-Rendite schlägt, oder (b) nachweisen, dass ein substanzieller Anteil der Prämie tatsächlich Fehlbepreisung (Behavioral) und nicht Risikokompensation ist. Meine Einschätzung pro Kandidat unten adressiert genau das über `p_echte_ineffizienz`.

---

## Kandidat 1: Value-Prämie (HML)

### a) Ökonomische Begründung: Risikoprämie vs. Behavioral

**Risikobasiertes Lager (Fama & French):** Value-Firmen sind "relativ distressed" — sie haben strukturell schlechtere Wachstumsaussichten, höhere Fixkostenlast und tragen ein systematisches Konjunkturrisiko, das im Marktbeta nicht vollständig erfasst wird. Zhang (2005, "The Value Premium", *Journal of Finance*) liefert die einflussreichste rationale Fundierung: Value-Firmen halten mehr "unproduktives" Kapital, das in Rezessionen schwer abzubauen ist (costly reversibility), plus prozyklischer Risikopreis → Value ist in schlechten Zeiten riskanter, genau wenn Risikoaversion hoch ist.

**Behavioral-Lager (Gegenseite):** Lakonishok, Shleifer & Vishny (1994, "Contrarian Investment, Extrapolation, and Risk", *Journal of Finance*) zeigen, dass Value-Aktien in ihren Standardrisikomaßen (Beta, Renditevolatilität in schlechten Makrozuständen) *nicht* systematisch riskanter sind als Glamour-Aktien — die Prämie sei Kompensation für keine zusätzliche Risikoexposition, sondern Ergebnis von naiver Extrapolation vergangenen Wachstums durch Investoren (Glamour wird überteuert, Value unterbewertet). Daniel & Titman (1997) verschärfen den Konflikt: Sie zeigen, dass *Charakteristika* (B/M-Ratio selbst) Renditen vorhersagen, nicht *Kovarianzen* (Faktor-Loadings) — das widerspricht direkt jeder rationalen ICAPM/APT-Logik, die verlangt, dass nur Kovarianz-Risiko kompensiert wird.

**Stand der Debatte 2026:** Ungelöst. Beide Lager haben seit 30+ Jahren Gegenevidenz produziert, ohne Konsens. Die praktische Konsequenz: Selbst Asness (AQR, klar im "moderate risk + moderate behavioral"-Lager) argumentiert inzwischen, dass ein Großteil der Post-2007-Underperformance auf einen **Bewertungs-Fehler in der Messung** zurückgeht (Buchwert erfasst immaterielle Vermögenswerte nicht) — das ist ein drittes Argument, das weder rein Risiko noch rein Behavioral ist, sondern **Konstruktionsartefakt** (siehe Punkt h).

### b) Limits to Arbitrage

Value ist das Lehrbuchbeispiel für "es kann jahrzehntelang gegen dich laufen, bevor es sich auszahlt" (Shleifer & Vishny 1997, "The Limits of Arbitrage"). Konkrete Reibungen: (1) Karriererisiko für institutionelle Value-Manager — massive AUM-Abflüsse 2017-2020 bei Value-Häusern (u.a. bei Smart-Beta-ETFs, siehe Punkt g); (2) "Value-Traps" — billige Aktien sind oft billig aus gutem Grund (Distress-Risiko real, Noise-Trader-Risiko), was Short-Selling der Glamour-Seite riskant macht; (3) Leerverkaufskosten auf der Growth/Glamour-Seite sind bei stark gehypten Mega-Caps (z.B. AI-Werten 2023-2025) hoch und das Timing des Reversals unvorhersehbar.

### c) Originalstudie

Fama & French (1992, "The Cross-Section of Expected Stock Returns", *Journal of Finance*): NYSE/AMEX/NASDAQ-Nichtfinanzfirmen 1963-1990, Book-to-Market als stärkster Einzelprädiktor, dominiert Beta und Size in Fama-MacBeth-Regressionen. Fama & French (1993, "Common Risk Factors in the Returns on Stocks and Bonds", *JFE*) formalisieren HML als Long-Short-Faktor (unabhängige 2×3-Sortierung nach Size/B-M), Stichprobe Juli 1963–Dez 1991. Historisch zitierte Größenordnung: HML-Durchschnittsrendite ca. 0,4-0,5%/Monat, t-Statistik im Bereich 2,8-3,0 (Größenordnung aus Lehrbuchwissen, nicht zeilengenau verifiziert). Nach der Harvey/Liu/Zhu-Hürde (t>3,0, s.u.) liegt der Originalbefund damit **am Rand der Signifikanz** — nicht klar darüber.

### d) Out-of-Sample-/Post-Publication-Evidenz

Das ist der entscheidende Befund gegen Value: **Drawdown 2007–Mitte 2020 von ca. 55%** relativ zu Growth, 13,3 Jahre Underperformance — der längste und tiefste Drawdown seit Beginn der Zeitreihe 1963 (Quelle: Two Sigma "Diagnosing the Recent Decade of Drawdown in Value"; Research Affiliates "Reports of Value's Death May Be Greatly Exaggerated", Arnott et al. 2020, *Financial Analysts Journal*). Arnott et al. zerlegen den Drawdown: Die *Revaluation* (Bewertungsspread zwischen Value und Growth) erklärt praktisch den gesamten Drawdown, nicht ein Zusammenbruch der fundamentalen Value-Rendite. Wenn man Buchwerte um immaterielle Vermögenswerte korrigiert, verkürzt sich der Drawdown von 13,5 auf ca. 3,5 Jahre und die durchschnittliche Jahresrendite wäre ca. 2,2 Prozentpunkte höher gewesen — ein starkes Indiz, dass die klassische HML-Konstruktion (Buchwert/Marktwert) in der heutigen Intangibles-Ökonomie strukturell fehlerhaft ist, nicht dass die Value-Idee an sich tot ist.

**Comeback-Versuch 2021-2022:** Bei steigenden Zinsen/Inflation 2022 outperformte HML den Markt um ca. 8% über 12 Monate — teilweise Erholung. **Aber 2023 kippte es wieder brutal:** MSCI World Value +8,9% vs. MSCI World Growth +36% — eine der größten Renditelücken der Messgeschichte (KI-Mega-Cap-Rally). 2024 erneut Growth-Dominanz, mit kurzen Value-Rotationsphasen (Q4 2024, Q1 2025, Q4 2025, Anfang 2026 leicht Value-Führung laut Marktkommentaren). **Fazit: kein sauberes, robustes Comeback — ein volatiles Hin und Her, kein struktureller Regimewechsel zurück zu Value.**

International: Value-Prämie ist außerhalb der USA (v.a. Europa, Japan, Emerging Markets) über lange Zeiträume robuster dokumentiert, aber auch dort seit 2010 abgeschwächt. Fama & French (2015, "A Five-Factor Asset Pricing Model", *JFE*, US-Stichprobe 1963-2013) finden, dass **HML redundant wird**, sobald RMW und CMA im Modell sind — die Korrelation von HML mit CMA liegt bei ca. 0,7. Das ist strukturell beunruhigend für "Value als eigenständige Ineffizienz", weil es nahelegt, dass HML im Kern nur eine verrauschte Kombination aus Profitability- und Investment-Information ist (Caveat: Fama & French 2017 zeigen, dass diese Redundanz stichprobenabhängig ist und nicht überall gilt).

McLean & Pontiff (2016, "Does Academic Research Destroy Stock Return Predictability?", *Journal of Finance*): über alle 97 untersuchten Anomalien im Schnitt **-26% Rendite out-of-sample, -58% post-publication**. HML ist seit 1992 publiziert (über 30 Jahre alt, extrem breit gehandelt) — konsistent mit einem Faktor, der strukturell am oberen Ende des Decay-Spektrums liegt.

### e) Kosten

Novy-Marx & Velikov (2016, "A Taxonomy of Anomalies and Their Trading Costs", *RFS*): geschätzte Handelskosten 20-57 Bp für Mid-Turnover-Anomalien wie Value; Value fällt eher in die mittlere Kostenklasse. Gegenläufig: Frazzini, Israel & Moskowitz (AQR, "Trading Costs of Asset Pricing Anomalies") nutzen proprietäre Handelsdaten und finden deutlich niedrigere reale Kosten (Value+Momentum-Live-Fonds ca. 23 Bp/Jahr für Momentum-ähnliche Turnoverklassen) — es gibt eine **echte Forschungskontroverse** über die Kostenhöhe, kein Konsens. Bei annualisiertem Turnover von grob 15-30% (Standard-Jahres-Rebalancing) ist Value moderat kostenrobust, aber nicht kostenlos.

### f) Kapazität

Sehr hoch bei Large-/Mid-Cap-Implementierung (Hunderte Milliarden USD in Value-ETFs/Fonds weltweit im Umlauf, DFA/AQR/Vanguard/iShares), aber die erwartete Bruttoprämie ist bei dieser Kapazität auch am niedrigsten. Höhere erwartete Rendite bei Small-/Micro-Cap-Value, aber dort massiv geringere Kapazität und höhere Kosten.

### g) Regimeabhängigkeit und Tail-Risiko

Value verhält sich wie eine "kurze Duration"-Wette: outperformt bei steigenden Zinsen/Inflation (2022), underperformt strukturell in tiefen-Zins-/QE-Regimen und in Phasen extremer Wachstumskonzentration (2010-2020, 2023-2025 KI-Boom). Faktor-Crowding ist real: Value ist seit 1992 öffentlich, milliardenschwer in Smart-Beta-ETFs repliziert; Value+Momentum litten im "Quant Quake" August 2007 gemeinsam unter massivem, korreliertem Deleveraging quantitativer Fonds — ein Beispiel für Crowding-getriebenes Tail-Risiko, das nichts mit der fundamentalen Story zu tun hat.

### h) Bekannte Kritik

Faktor-Zoo (Harvey/Liu/Zhu 2016 dokumentieren 316+ publizierte Faktoren, fordern t>3,0 statt t>2,0 als Hürde für neue Faktoren — HML läge bei ursprünglicher t≈2,8-3,0 knapp an der Grenze); Konstruktionsartefakt-Kritik (Buchwert/Marktwert erfasst Intangibles nicht, s.o.); Redundanz mit RMW/CMA in FF5 (s.o.); Hou/Xue/Zhang (2020, "Replicating Anomalies", *RFS*) zeigen, dass von 452 getesteten Anomalien 65% die einfache |t|≥1,96-Hürde nicht bestehen und 52% bei Multiple-Testing-Korrektur scheitern — HML selbst gilt in ihrem q-Faktor-Modell-Rahmen als eher schwach eigenständig erklärend, da Investment/Profitability den Großteil der Information abdecken.

**Urteil: WEAK.** Kein KILL, weil die ökonomische Logik (ob Risiko oder Verhalten) nicht widerlegt ist und internationale/historische Evidenz über sehr lange Horizonte real ist. Aber kein CANDIDATE, weil (1) die Post-Publication-Evidenz seit 2007 gemischt bis negativ ist mit nur kurzen, unvollständigen Erholungsphasen, (2) HML in modernen Multifaktor-Modellen redundant wird, (3) die Konstruktion nachweislich unter einem strukturellen Messfehler leidet, der bislang nicht sauber in einem breit zugänglichen, kostengünstigen Signal korrigiert wurde. `p_echte_ineffizienz = 0,3` — ich gewichte die Risikoprämien-Erklärung leicht stärker als die Behavioral-Erklärung, gerade weil die Prämie systematisch mit Makro-Regimes (Zinsen, Rezessionsrisiko) korreliert, was für eine State-Variable-Kompensation statt reiner Fehlbepreisung spricht.

---

## Kandidat 2: Profitabilitäts-/Qualitätsprämie (Gross Profitability, RMW, QMJ)

### a) Ökonomische Begründung: Risikoprämie vs. Behavioral

Dies ist der theoretisch interessanteste Fall, weil er der reinen Risikostory am stärksten widerspricht: Profitablere, "sicherere" Firmen haben *höhere*, nicht niedrigere erwartete Renditen als unprofitable, riskantere Firmen. Ein simples Risiko-Rendite-Trade-off-Argument (mehr Risiko = mehr erwartete Rendite) sagt das Gegenteil voraus. Novy-Marx (2013, "The Other Side of Value: The Gross Profitability Premium", *JFE*) argumentiert explizit, dass Profitability eher eine **Value-Signal-Korrektur** ist: billige UND profitable Firmen sind die eigentlichen "Value"-Gewinner, während klassisches B/M-Value fälschlich auch billige-weil-unprofitable ("Value-Traps") mit einschließt.

**Rationales Lager:** Fama & French selbst integrieren RMW über eine Dividend-Discount-Modell-Logik (höhere erwartete Profitabilität bei gegebenem Buchwert/Preis impliziert höhere erwartete Rendite — eine rein rechnerische Konsequenz der Bewertungsgleichung, kein separates Risikofaktum per se). Asness/Frazzini/Pedersen (QMJ) argumentieren, Qualität sei eine Art "Versicherung" (defensiv, geringere Drawdowns in Krisen) und die Prämie sei Kompensation dafür, dass leverage-beschränkte Investoren (institutionell wie Privatanleger) systematisch "Junk"/Lotterie-Aktien überkaufen, um über Beta-Hebel Renditechancen zu erhöhen (Frazzini & Pedersen 2014, "Betting Against Beta"-Logik) — das drückt Junk-Preise hoch und Quality-Preise relativ runter. Das ist eine **Limits-to-Arbitrage-/Friktions-Erklärung**, nicht reines Makro-Risiko.

**Behavioral-Lager:** Kumar (2009) und andere zeigen eine robuste Retail-Präferenz für "Lottery Stocks" (hohe Skewness, spekulative Junk-Aktien) — das treibt Junk-Überbewertung strukturell und lässt sich nur schwer arbitrieren (s.u.), weil institutionelle Arbitrageure Junk nicht beliebig leerverkaufen können/wollen.

**Stand der Debatte:** Der Konsens tendiert stärker als bei Value dazu, dass ein substanzieller Teil der Prämie **friktions-/verhaltensbedingt** ist, weil die reine Risikostory (safe=low return) hier eigentlich das falsche Vorzeichen vorhersagen würde. Das ist der Hauptgrund für die höhere `p_echte_ineffizienz` in meiner Bewertung.

### b) Limits to Arbitrage

Die Short-Seite (Junk) ist das Problem: schwer und teuer zu leerverkaufende Small-/Micro-Cap-Distressed-Aktien mit hohen Leihgebühren und Squeeze-Risiko (Meme-Stock-Phänomen 2021 als Extrembeispiel). Zusätzlich begrenzen Leverage-Constraints (institutionelle Investoren mit Leverage-Limits kompensieren fehlenden Hebel durch Übergewichtung riskanterer/"junk"-artiger Aktien statt gehebelter sicherer Aktien) strukturell, wie schnell diese Fehlbepreisung korrigiert werden kann.

### c) Originalstudie

Novy-Marx (2013, *JFE*): NYSE-Aktien, Juli 1963–Dez 2010, Quintil-Sortierung nach Gross Profits/Assets. Höchstes minus niedrigstes Quintil: **0,31% Monatsrendite, t-Statistik 2,49** — unterhalb der Harvey/Liu/Zhu-3,0-Hürde, aber vergleichbar in Größenordnung mit B/M-Value selbst. Novy-Marx zeigt zusätzlich, dass eine Value-Strategie, die zusätzlich nach Profitability konditioniert (HML-GP), die Rendite auf 0,54%/Monat bei t=5,01 steigert — die Kombination ist deutlich robuster als jede Einzelkomponente.

Asness, Frazzini & Pedersen (Working Paper 2013, publiziert 2019 in *Review of Accounting Studies* als "Quality Minus Junk"): QMJ signifikant profitabel in den USA und 23 von 24 untersuchten Ländern (Spanne 0,20%/Monat Spanien bis 1,02-1,06%/Monat Hongkong/Griechenland), Information Ratio USA ca. 1,46 — außergewöhnlich hoch für einen Aktienfaktor. Langfristige Kennzahl (1964-2023, laut aktuellerer AQR-Aufbereitung): ca. 4,7% p.a. Prämie, Volatilität ca. 9,9%, Sharpe Ratio ca. 0,47.

### d) Out-of-Sample-/Post-Publication-Evidenz

Positiv: Breiteste internationale Replikation aller hier untersuchten Faktoren (23/24 Länder signifikant) — das ist eine der saubersten Out-of-Sample-Bestätigungen im gesamten Faktor-Zoo, weil die internationalen Stichproben zum Publikationszeitpunkt (2013) noch nicht ausführlich vorab durchsucht waren. Profitability ist zudem einer der zentralen Bausteine des Hou/Xue/Zhang q-Faktor-Modells (ROE-Faktor), das eigenständig und nicht aus der FF-Tradition entwickelt wurde und trotzdem zu einem sehr ähnlichen Schluss kommt — Konvergenz zweier unabhängiger Modellfamilien ist ein starkes Robustheitsindiz.

Negativ/nuanciert: Hou/Xue/Zhang (2020) zeigen, dass viele *einzelne* Profitability-Anomalie-Varianten (z.B. F-Score-Deciles) unter strengem q-Faktor-Alpha-Test nicht signifikant sind (t-Werte z.B. 0,58/0,86/0,49 für verschiedene Horizonte in ihrer Tabelle) — die *breite* Profitability-Prämie ist robuster als viele ihrer *spezifischen* Umsetzungsvarianten, ein klassisches Zeichen von Data-Mining bei den Detailvarianten.

Aktuelle Performance ist keineswegs euphorisch: Marktkommentare (Oakmark 4Q2025) beschreiben 2024 und v.a. **2025 als "awful year" für Quality**, da im KI-getriebenen Boom unprofitable/spekulative Wachstumswerte outperformten — ein Beleg dafür, dass Quality/QMJ genau wie Value in Phasen exzessiver Risikofreude ("Junk-Rallye") strukturell hinterherhinkt. Kein sauberer, unterbrechungsfreier Track Record seit Publikation.

### e) Kosten

Charakteristika (Profitabilität, ROE, Bilanzqualität) ändern sich langsamer als Preis-Kennzahlen → tendenziell niedrigerer Turnover als Value (grob 20-40% p.a.), fällt in Novy-Marx & Velikovs Taxonomie eher in die Low-/Mid-Turnover-Klasse mit besserer Netto-Rendite-Überlebensrate nach Kosten. QMJ übergewichtet zudem tendenziell bereits große, liquide, profitable Blue Chips (nicht Small-Cap-Distressed wie bei reinem Value) — das senkt Market-Impact-Kosten strukturell.

### f) Kapazität

Sehr hoch — vermutlich die höchste Kapazität aller drei Kandidaten, weil Qualität/Profitabilität mit Unternehmensgröße positiv korreliert (die profitabelsten Firmen sind oft Mega-Caps wie Apple, Microsoft), während Value und v.a. Investment eher in kleinere/illiquidere Segmente tendieren.

### g) Regimeabhängigkeit und Tail-Risiko

Defensiv in klassischen Abschwüngen/Flight-to-Quality (negative/niedrige Beta-Charakteristik in Crashs), aber verwundbar in spekulativen Blasenphasen mit breiter Risikoüberzeugung (2020/21 Reopening-/Meme-Rallye, 2023-2025 KI-Boom bei unprofitablen Wachstumsfirmen). Tail-Risiko ist also spiegelbildlich zu Value: schmerzt am meisten, wenn "Storytelling" statt Fundamentaldaten den Markt treibt.

### h) Bekannte Kritik

Faktor-Zoo/Publication-Bias-Kritik gilt genauso wie für Value; zusätzlich Kritik, dass "Quality" ein Sammelbegriff ohne einheitliche Definition ist (Profitabilität, Sicherheit, Wachstum, Payout — je nach Anbieter unterschiedlich gewichtet), was Data-Mining-Spielraum bei der Signalkonstruktion eröffnet (viele "Quality"-Indizes mit deutlich unterschiedlicher Performance trotz gleichem Etikett). Hohe Korrelation/Redundanz mit Low-Volatility- und teilweise mit Value-Faktoren (nicht Gegenstand dieses Mandats, aber relevant für Portfolio-Diversifikationsnutzen).

**Urteil: CANDIDATE.** Bester Kandidat der Klasse: breiteste unabhängige internationale Out-of-Sample-Bestätigung, bessere Kostenrobustheit, höhere Kapazität, und eine ökonomische Logik, die schwerer rein risikobasiert zu erklären ist (was für einen höheren Ineffizienz-Anteil spricht) als bei Value. Aber explizit **kein High-Confidence-CANDIDATE**: schwache/negative Performance 2024-2025, Uneinheitlichkeit der Definition, und die "Sicherheit als Versicherungsprämie"-Erklärung bleibt eine legitime Risikoprämien-Alternative zur Fehlbepreisungs-These. `p_echte_ineffizienz = 0,4` — bewusst unter 0,5, weil ich trotz besserer Ausgangslage nicht von einer mehrheitlich verhaltensbedingten Erklärung überzeugt bin.

---

## Kandidat 3: Investment-Prämie (CMA / Asset Growth)

### a) Ökonomische Begründung

**Risikobasiert (q-Theorie, Zhang und Koautoren):** Im Investment-basierten CAPM (q-Theorie) implizieren niedrige erwartete Renditen bei hohen Investitionsraten einfach niedrige Kapitalkosten im Gleichgewicht — Firmen investieren mehr, wenn ihr Diskontsatz (=erwartete Rendite für Investoren) niedrig ist. Das ist eine rein rationale, tautologische Beziehung zwischen Investition und erwarteter Rendite, kein Verhaltensfehler.

**Behavioral (Gegenseite):** Titman, Wei & Xie (2004) und Cooper, Gulen & Schill (2008, "Asset Growth and the Cross-Section of Stock Returns", *JF*) interpretieren dieselbe Beziehung als Überinvestitions-/Agency-Kosten-Problem: Manager bauen Empires, wenn günstiges Kapital verfügbar ist (oft nach Aktienemissionen), Investoren reagieren zu langsam/unteradäquat auf die impliziten negativen NPV-Signale, was zu systematisch enttäuschenden Folgerenditen führt — eine klassische Extrapolations-/Unteraktions-Fehlbepreisung, verstärkt durch Marktsentiment bei Kapitalerhöhungen (SEO-Underperformance-Literatur, Loughran & Ritter 1995 als verwandte Evidenz).

**Stand der Debatte:** Es gibt keinen klaren Sieger; das Signal wird in der Literatur häufiger als "am wenigsten eigenständig" der drei diskutiert, weil es in fast jedem Multifaktor-Modell (FF5, q-Factor) primär als Ergänzung zur Profitability-Dimension auftaucht, nicht als unabhängige Erklärungsgröße.

### b) Limits to Arbitrage

Eng an diskrete Corporate-Actions gekoppelt (Kapitalerhöhungen, M&A-finanzierte Bilanzsummenausweitung, Buybacks als Gegenpol) — Arbitrage würde bedeuten, systematisch gegen Emittenten zu wetten, was bei volatilen, sentimentgetriebenen Emissionsphasen (z.B. SPAC-/Growth-Emissionswellen 2020-2021) riskant und teuer ist.

### c) Originalstudie

Fama & French (2015, *JFE*, US-Stichprobe 1963-2013) definieren CMA formal im Fünf-Faktor-Modell; historisch zitierte Größenordnung ca. 0,2-0,3%/Monat, deutlich kleinere und weniger robuste Prämie als HML/RMW (Größenordnung aus Lehrbuchwissen). Cooper/Gulen/Schill (2008) zeigen für Asset-Growth-Deciles größere Spreads (bis zu ca. 20%/Jahr zwischen Top-/Bottom-Decile in bestimmten Subperioden), aber diese Zahlen sind stark size-/liquiditätsabhängig (Mikro-Cap-getrieben) und schrumpfen deutlich bei Value-Weighting.

### d) Out-of-Sample-/Post-Publication-Evidenz

Am schwächsten der drei Kandidaten: In FF2015 selbst bereits die kleinste, am wenigsten robuste der neuen Faktoren; hohe Korrelation zu HML (~0,7) deutet auf geringe eigenständige Information hin. Hou/Xue/Zhang (2020) zeigen, dass ein Großteil der "Investment-Zoo"-Varianten (Asset Growth, Net Share Issuance, Investment-to-Assets in diversen Definitionen) bei strenger Multiple-Testing-Korrektur die Signifikanz verliert — von 452 getesteten Variablen bestehen nur 35% überhaupt die einfache |t|≥1,96-Hürde, und Investment-nahe Variablen sind unter den anfälligsten Gruppen. Keine belastbare, dokumentierte "Comeback"-Story wie bei Value; auch keine breite unabhängige internationale Replikationsevidenz vergleichbar mit QMJ.

### e) Kosten

Höherer Turnover als Profitability, da Signal von diskreten Bilanz-/Kapitalmaßnahmen-Events getrieben wird (jährliche Neueinstufung kann sprunghaft sein); Emittenten-nahe Aktien (nach SEOs) sind tendenziell kleiner/illiquider mit breiteren Spreads. Fällt in Novy-Marx/Velikov eher in höhere Kostenklassen, mit spürbarer Netto-Renditeerosion.

### f) Kapazität

Moderat — kleiner-Cap-Tilt begrenzt Kapazität stärker als bei Value oder Quality.

### g) Regimeabhängigkeit und Tail-Risiko

An Kredit-/Investitionszyklus gekoppelt (hohe Investitionsraten korrelieren mit Kreditverfügbarkeit/Niedrigzinsphasen) — wenig eigenständig untersuchte Regimestabilität, tendenziell prozyklisch ähnlich wie ein verwässertes Value-Signal.

### h) Bekannte Kritik

Redundanz-Kritik am schärfsten hier: CMA wird in mehreren Multifaktor-Studien primär als "Model-Faktor" behandelt, der hilft, andere Anomalien statistisch zu erklären, nicht als eigenständig handelbare Ineffizienz. Publication-Bias und Faktor-Zoo-Kritik (Harvey/Liu/Zhu) treffen hier am härtesten, da Investment/Asset-Growth-Varianten einen der größten Cluster im "Zoo" bilden (viele leicht unterschiedliche Definitionen — Asset Growth, Investment-to-Assets, Net Operating Assets, Net Share Issuance — mit hoher gegenseitiger Korrelation, was auf Data-Mining/Redundanz statt unabhängiger Entdeckungen hindeutet).

**Urteil: KILL.** Als eigenständige, tradbare Strategie für diesen Fonds nicht überzeugend: schwache eigenständige Signifikanz nach Multiple-Testing-Korrektur, hohe Redundanz mit den anderen (ohnehin schon fragwürdigen) Faktoren, schwächste Kostenrobustheit, keine dokumentierte robuste Post-Publication-Comeback-Story. Bleibt höchstens als Nebenkomponente in einem kombinierten Value/Quality-Modell relevant, nicht als eigenständiges Alpha-Signal.

---

## Zusammenfassendes Urteil zur Klasse

Die Klasse "klassische Faktorprämien" ist **nicht tot, aber auch kein überzeugendes Alpha-Jagdgebiet mehr** für einen Hedgefonds, der über passive Beta-Exposition hinausgehen will. Drei Kernprobleme ziehen sich durch alle Kandidaten:

1. **Die Risikoprämien-vs.-Ineffizienz-Frage bleibt strukturell ungelöst** — nach über 30 Jahren akademischer Debatte gibt es keinen Konsens, was gegen "einfaches, robustes Alpha" spricht. Bei echtem, unstrittigem Alpha würde man erwarten, dass die Erklärung nach Jahrzehnten Forschung klarer geworden wäre statt weiterhin 50/50 verteilt zu sein.
2. **Das Timing-Problem ist real:** Value hatte einen 13-Jahre-Drawdown (2007-2020) und ein nur unvollständiges, volatiles Comeback seither (2022 gut, 2023 wieder schlecht, 2024-2026 uneinheitlich). Quality/Profitability litt 2024-2025 unter dem KI-Boom. Diese Prämien sind über Dekaden hinweg zu volatil und regimeabhängig, um verlässlich in ein Multi-Strategie-Portfolio mit stabilem Sharpe-Beitrag eingebaut zu werden.
3. **Kapazität ist strukturell hoch, aber genau deshalb ist Crowding real:** Hunderte Milliarden USD an Smart-Beta-AUM verfolgen dieselben Signale seit über 30 Jahren öffentlicher Publikation — McLean/Pontiffs Decay-Zahlen (-26% OOS, -58% post-Publikation im Durchschnitt über alle Anomalien) sind für diese besonders alten, besonders bekannten Faktoren eher eine untere Grenze als eine Übertreibung.

**Einziger Kandidat mit CANDIDATE-Status:** Profitability/Quality (Novy-Marx GP, QMJ) — wegen der breitesten internationalen Out-of-Sample-Bestätigung (23/24 Länder), besserer Kostenstruktur und einer ökonomischen Logik, die der reinen Risikoprämien-Erklärung tendenziell widerspricht (sicher+profitabel mit höherer statt niedrigerer Rendite ist kein einfaches Risiko-Rendite-Trade-off). Aber selbst hier: `p_echte_ineffizienz = 0,4`, keine Euphorie, und die jüngste (2024-2025) Schwächephase mahnt zur Vorsicht.

**Value (WEAK) und Investment (KILL)** sind für dieses Mandat nicht überzeugend genug: Value, weil die Post-2007-Evidenz zu gemischt ist und die Konstruktion einen dokumentierten strukturellen Fehler (Intangibles) aufweist; Investment, weil es überwiegend redundant zu den anderen beiden ist und die eigenständige Signifikanz bei sauberer Multiple-Testing-Korrektur nicht robust übersteht.

**Ehrliches Fazit:** Wenn dieses Mandat "echte, vom Risiko unabhängige Ineffizienz" verlangt, ist die Ausbeute aus der klassischen Faktorprämien-Literatur mager — ein einziger vorsichtiger CANDIDATE, keine starken Kauf-Empfehlungen. Das deckt sich mit der Selbsteinschätzung führender Praktiker (AQR, Research Affiliates) seit ca. 2018-2020, dass die "einfachen" Faktorprämien von den 1990er/2000er-Jahren zu einem "Basis-Beta-Baustein" degradiert sind, während echtes Alpha in dieser Klasse (falls vorhanden) heute eher aus überlegener Implementierung (Kostenoptimierung, Timing, Signal-Kombination, Behandlung von Konstruktionsfehlern wie Intangibles) als aus dem reinen Rohsignal selbst kommen müsste — und das ist per Definition schwerer, skalierbarer Edge, kein simples "kaufe billig/profitabel"-Signal mehr.

---

## Quellen (aus Websuche, Juli 2026)

- Two Sigma: "Diagnosing the Recent Decade of Drawdown in Value" — https://www.twosigma.com/articles/diagnosing-the-recent-decade-of-drawdown-in-value/
- Research Affiliates / Arnott et al.: "Reports of Value's Death May Be Greatly Exaggerated" (2020, FAJ) — https://www.tandfonline.com/doi/full/10.1080/0015198X.2020.1842704
- Alpha Architect: "Resurrecting the Value Premium" — https://alphaarchitect.com/resurrecting-the-value-premium/
- AQR: "Quality Minus Junk" Datasets & Working Paper — https://www.aqr.com/Insights/Datasets/Quality-Minus-Junk-Factors-Monthly, https://www.aqr.com/Insights/Research/Working-Paper/Quality-Minus-Junk
- Oakmark Funds: "Much ado about quality" (4Q2025 Commentary) — https://oakmark.com/news-insights/much-ado-about-quality-international-equity-market-commentary-4q-2025/
- Novy-Marx (2013), "The Other Side of Value: The Gross Profitability Premium" — https://mysimon.rochester.edu/novy-marx/research/OSoV.pdf
- McLean & Pontiff (2016), "Does Academic Research Destroy Stock Return Predictability?" — https://onlinelibrary.wiley.com/doi/10.1111/jofi.12365
- Harvey, Liu & Zhu (2016), "…and the Cross-Section of Expected Returns" — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2249314
- Hou, Xue & Zhang (2020), "Replicating Anomalies" — https://www.nber.org/system/files/working_papers/w23394/w23394.pdf
- Novy-Marx & Velikov (2016), "A Taxonomy of Anomalies and Their Trading Costs" — https://ideas.repec.org/a/oup/rfinst/v29y2016i1p104-147..html
- Frazzini, Israel & Moskowitz, "Trading Costs of Asset Pricing Anomalies" (AQR) — referenziert über Alpha Architect: https://alphaarchitect.com/wp-content/uploads/2021/08/Factor_Investing_and_Trading_Costs.pdf
- ETF Stream: "Value's underperformance highlights systemic problem with smart beta" — https://www.etfstream.com/articles/values-underperformance-highlights-systemic-problem-with-smart-beta
- Tacita Capital: "2024 Global Factor Round Up" — https://tacitacapital.com/insights/commentary/2024-global-factor-round-up/
- Wisdomtree: "Growth vs. Value: An Unfinished Debate" — https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/market-insights/wisdomtree-commentary/growth-vs-value-unfinished-debate.pdf

Ergänzend Lehrbuchwissen (interne Wissensbasis, Stand Anfang 2026) für: Fama & French (1992, 1993, 2015) Originalzahlen (Größenordnungen, nicht zeilengenau aus Primärquelle verifiziert), Zhang (2005) q-Theorie, Lakonishok/Shleifer/Vishny (1994), Daniel & Titman (1997), Cooper/Gulen/Schill (2008), Frazzini & Pedersen (2014) Betting-Against-Beta-Logik, Kumar (2009) Lottery-Preference-Literatur.
