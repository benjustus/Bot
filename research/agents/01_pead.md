```yaml
agent: 01
klasse: "Earnings Drift (PEAD)"
websuche_verfuegbar: ja
strategien:
  - name: "Klassische SUE-Preis-Drift (Bernard & Thomas 1989, decile-basiert)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 1
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "0.0-0.2 (nach realistischen Kosten, groesstenteils nicht von Null unterscheidbar)"
    kernrisiko: "Effekt ist zu >90% in illiquiden Small-/Microcaps konzentriert; verschwindet in liquiden Value-Weighted-Tests (Hou/Xue/Zhang t=1.0-1.65) und wird von Transaktionskosten aufgezehrt (Chordia et al. 2009: 0.04%/Monat in liquidesten vs. 2.43%/Monat in illiquidesten Quintilen)."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Data Library hat kein direktes SUE-Portfolio; naeherungsweise ueber Chen&Zimmermann Open Source Asset Pricing (Signal 'Sue') / WRDS IBES+Compustat noetig; grob approximierbar mit Earnings-Momentum-Proxy aus Compustat-Quartalsdaten"
  - name: "Preis- + Earnings-Momentum kombiniert (Chan/Jegadeesh/Lakonishok 1996)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 3
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0.15-0.35 (als Overlay auf Preis-Momentum-Faktor, nicht standalone)"
    kernrisiko: "Erbt Crash-Risiko von Preis-Momentum (Momentum-Crashes 2009, negative Skew); ist Teil eines der meist-gehandelten Faktoren weltweit -> hohes Crowding-Risiko; Zusatzbeitrag von Earnings-Signal ueber reines Preis-Momentum hinaus ist klein und schwer sauber zu isolieren."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Data Library: 'Momentum Factor (Mom)' als Preis-Momentum-Baseline; Earnings-Komponente erfordert IBES/Compustat"
  - name: "Analysten-basierte SUE / kombinierte Signale (Livnat & Mendenhall 2006; Brandt/Kishore/Santa-Clara/Venkatachalam 2008, EAR+SUE)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.25
    netto_sharpe_erwartung: "0.1-0.25"
    kernrisiko: "Groessenordnung staerker als Zeitreihen-SUE, aber auf gleiche illiquide Universum-Konzentration und gleiche Limits-to-Arbitrage angewiesen; kaum unabhaengige Post-Publication-OOS-Studien; Look-ahead-Risiko durch IBES-Punkt-in-Zeit-Datenqualitaet vor Mitte-1990er."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
```

# Earnings Drift (PEAD) — Adversarial Research Report

**Agent:** 01 | **Klasse:** Earnings Drift / Post-Earnings-Announcement-Drift (SUE-basierte Strategien, Earnings-Momentum)
**Datum:** Juli 2026 | **Nullhypothese:** Es gibt kein handelbares Netto-Alpha in dieser Anomalieklasse.
**Evidenzbasis:** Websuche funktionsfaehig; Befunde unten mit Quellen belegt, ergaenzt durch internes Wissen Stand Anfang 2026 wo Websuche keine Primaerzahlen lieferte (jeweils gekennzeichnet).

---

## 0. Executive Summary

PEAD ist eine der am laengsten dokumentierten Anomalien der Finanzliteratur (Ball & Brown 1968, Bernard & Thomas 1989/1990) und zugleich eine der am staerksten dekonstruierten. Die zentrale adversarial-These dieses Berichts: **Der klassische, gleichgewichtete SUE-Decile-Spread ist im Wesentlichen ein Small-Cap-/Illiquiditaets-Kompensations-Artefakt, kein robuster, kostenbereinigter Markteffizienz-Verstoss in handelbarer Groessenordnung.** Drei Belegstraenge stuetzen das:

1. **Hou, Xue & Zhang (2020) "Replicating Anomalies"** zeigen, dass der SUE-High-minus-Low-Spread unter strengerer, praxisnaher Methodik (NYSE-Breakpoints, Value-Weighting statt Equal-Weighting) auf 0.19%/Monat (6M-Horizont, t=1.65) bzw. 0.11%/Monat (12M, t=1.00) zusammenschrumpft — beides unterhalb der einfachen Signifikanzschwelle von t>1.96, erst recht unterhalb der Multiple-Testing-Schwelle von t>2.78.
2. **Chordia, Goyal, Sadka, Sadka & Shivakumar (2009)** zeigen, dass der wertgewichtete High-minus-Low-SUE-Spread in der liquidesten Aktien-Quintile nur 0.04%/Monat betraegt, in der illiquidesten Quintile hingegen 2.43%/Monat — der Effekt ist also zu einem grossen Teil genau dort konzentriert, wo Handelskosten ihn auffressen.
3. **Chordia, Subrahmanyam & Tong (2014)** dokumentieren einen strukturellen Rueckgang: von ca. 18% p.a. abnormaler Rendite (Bernard-Thomas-Aera, 1974-1985) auf nahe Bedeutungslosigkeit fuer Large Caps nach Dezimalisierung (2001) und Reg NMS (2005); die durchschnittliche Anomalie-Rendite habe sich in etwa halbiert.

Das bedeutet nicht, dass die Klasse vollstaendig tot ist. Als **Signal-Komponente innerhalb eines breiteren, kostenoptimierten Multi-Faktor-Buchs** (kombiniert mit Preis-Momentum, mit Liquiditaetsfiltern, mit Portfolio-Netting ueber viele Namen) gibt es plausible Evidenz fuer einen kleinen, aber echten Rest-Alpha-Beitrag. Als eigenstaendige, skalierbare institutionelle Strategie ist der klassische SUE-Ansatz jedoch zu verwerfen.

---

## 1. Kandidat 1: Klassische SUE-Preis-Drift (Bernard & Thomas 1989)

### a) Oekonomische Begruendung

**Kein Risikoprämien-Argument, primaer Behavioral.** Die dominante Erklaerung ist **Investoren-Unteraufmerksamkeit / verzögerte Erwartungsanpassung** (Bernard & Thomas 1990): Marktteilnehmer behandeln Ergebnisueberraschungen, als folgten sie einem Random Walk, obwohl Quartalsgewinne empirisch positiv autokorreliert sind (typische Autokorrelation der Earnings-Aenderungen ueber vier Quartale: signifikant positiv fuer die ersten drei Lags, negativ beim vierten wegen saisonaler Basis-Effekte). Der Markt "lernt" die Persistenz nicht vollstaendig ein, sodass der Preis erst mit der naechsten oder uebernaechsten Ueberraschung "nachzieht" — daher die 60-Tage-Drift nach der Ankuendigung.

**Wer verursacht die Fehlbewertung?** Nicht-institutionelle/retail-dominierte Order-Flows in kleineren Titeln, begrenzte Analystenabdeckung (Sell-Side-Analysten passen Schaetzungen ebenfalls nur langsam an — "sluggish forecast revisions", dokumentiert bei Chan/Jegadeesh/Lakonishok 1996), sowie begrenzte Kapazitaet von Investoren, in einem gegebenen Berichtsquartal Tausende gleichzeitiger Ueberraschungen zu verarbeiten (Limited-Attention-Literatur, z. B. Hirshleifer/Teoh).

### b) Limits to Arbitrage

- **Idiosynkratisches Risiko:** Jede Ueberraschung ist ein firmenspezifisches Ereignis; Diversifikation erfordert sehr viele gleichzeitige Positionen, was Kapitalbindung und Bewertungsrisiko erhoeht (Shleifer & Vishny-Logik).
- **Liquiditaet/Transaktionskosten:** Der Effekt konzentriert sich in kleinen, weniger liquiden Titeln (siehe Chordia et al. 2009 unten) — genau dort, wo Spreads und Market Impact am hoechsten sind.
- **Short-Sale-Constraints:** Die Short-Seite (negative SUE) betrifft ueberproportional kleine, teure-zu-leihende Titel; Leihgebuehren koennen einen wesentlichen Teil der theoretischen Rendite auffressen.
- **Kein fundamentaler Anker:** Anders als Value (Buchwert) hat PEAD keinen stabilen Fundamentalanker, gegen den ein Arbitrageur "sicher" positionieren kann — das macht die Strategie besonders anfaellig fuer Crowding-Dynamiken (siehe Abschnitt 1g).

### c) Originalstudie

**Bernard & Thomas (1989), Journal of Accounting Research**, Stichprobe 1974-1985 (48 Quartale), NYSE/AMEX. Extremer SUE-Decile-Spread: Der Spread ist in 41 von 48 Quartalen positiv, auch in 11 von 16 Quartalen mit negativer NYSE-Index-Rendite (also nicht reines Beta). Positive Drift von ca. +2% ueber 60 Handelstage fuer die guenstigste Nachrichtenlage, symmetrisch negative Drift fuer die schlechteste — macht einen Long/Short-Spread von grob 4% ueber das Quartal, was in Sekundaerliteratur (Chordia/Subrahmanyam/Tong 2014, ueber Websuche referenziert) auf annualisiert **~18% abnormale Rendite** in der Originalperiode hochgerechnet wird. Praezise Original-t-Statistiken zur Decile-Spread-Signifikanz waren ueber Websuche nicht vollstaendig auffindbar; die Konsistenz ueber 41/48 Quartale impliziert aber hohe statistische Robustheit in-sample.

### d) Out-of-Sample-/Post-Publication-Evidenz — **zentrales Kill-Argument**

- **Hou, Xue & Zhang (2020), "Replicating Anomalies", Review of Financial Studies:** Unter NYSE-Breakpoints + Value-Weighting (die von den Autoren als realistischere, weniger microcap-verzerrte Methodik vorgeschlagene Spezifikation) liefert der SUE-High-minus-Low-Decile-Spread nur noch **0.19%/Monat (t=1.65) auf 6-Monats-Horizont und 0.11%/Monat (t=1.00) auf 12-Monats-Horizont**. Beide t-Werte liegen unterhalb der einfachen 1.96-Schwelle; unter der von den Autoren vorgeschlagenen Multiple-Testing-Korrektur (t>2.78, gegen 452 getestete Anomalien) ist SUE klar nicht signifikant. Das ist die schwerwiegendste bekannte Replikations-Widerlegung fuer die Klasse.
- **Chordia, Subrahmanyam & Tong (2014):** Anomalie-Renditen im Schnitt nach Dezimalisierung ca. halbiert; PEAD speziell von ~18% p.a. (Bernard-Thomas-Aera) Richtung Bedeutungslosigkeit fuer Large Caps. Begleitindiz (unbestaetigte Sekundaerquelle, mit Vorsicht zu behandeln): PEAD soll bei Non-Microcaps ab ca. 2001 zu verschwinden begonnen haben und bei Large Caps ab ca. 2006 statistisch nicht mehr von Null unterscheidbar sein — richtungskonsistent mit den peer-reviewten Befunden, aber die genaue Jahreszahl stammt aus einer nicht-akademischen Quelle und ist als solche zu kennzeichnen.
- **McLean & Pontiff (2016), Journal of Finance** (ueber alle 97 getesteten Prädiktoren, nicht SUE-spezifisch, aber als Prior anwendbar): Portfolio-Renditen im Schnitt **26% niedriger Out-of-Sample** und **58% niedriger Post-Publication** gegenueber der Originalstudie. Interpretation: ca. 26 Prozentpunkte Data-Mining-Bias, weitere ca. 32 Prozentpunkte publikationsgetriebener Preisdruck/Arbitrage.
- **Chordia, Goyal, Sadka, Sadka & Shivakumar (2009), Financial Analysts Journal:** Wertgewichteter High-minus-Low-SUE-Spread = **0.04%/Monat in der liquidesten Quintile vs. 2.43%/Monat in der illiquidesten Quintile.** Das ist der staerkste einzelne Beleg dafuer, dass der "Effekt" primaer ein Illiquiditaets-/Microcap-Phaenomen ist und im liquiden, institutionell handelbaren Universum praktisch verschwindet.
- **Internationale Replikation:** Direktionale Bestaetigung von PEAD in vielen Maerkten (Australien, Kanada, China, Finnland, Griechenland, Indien, Neuseeland, Saudi-Arabien, Suedafrika, Suedkorea, Spanien, Tunesien — laut Sekundaerliteratur/Review-Artikeln). Wichtig: internationale Replikation bestaetigt die **Existenz der Drift-Richtung**, nicht ihre **Netto-Handelbarkeit** — viele dieser Maerkte haben noch hoehere Transaktionskosten und geringere Liquiditaet als die USA, was das Muster eher zusaetzlich als KILL-Kandidat stuetzt statt als CANDIDATE.
- **Geschaetzter Decay:** Von ~18% p.a. (Originalperiode, gleichgewichtet, inkl. Microcaps) auf ~0.1-0.2%/Monat (~1-2% p.a., wertgewichtet, Hou/Xue/Zhang-Methodik) entspricht einem **Decay von grob 85-95%** zwischen Erstpublikation und moderner, kostenrealistischer Replikation.

### e) Kosten

Keine direkte Novy-Marx & Velikov (2016)-Zahl speziell fuer SUE gefunden, aber die Struktur der Strategie (Quartalsrebalancing, hohe Konzentration in kleinen/illiquiden Titeln mit weiten Spreads) platziert sie in die von Novy-Marx/Velikov identifizierte Hochkosten-Kategorie: Anomalien mit hohem Turnover und Small-Cap-Tilt zeigen typischerweise Netto-Renditen deutlich unter 50% der Brutto-Rendite. Zum Vergleich (verwandte, besser dokumentierte Strategie): Momentum brutto 16.0% p.a. -> netto 8.16% p.a. nach Novy-Marx/Velikov (effektive Spreads 20-57 Bp fuer mittlere Turnover-Strategien). Bei SUE, das noch staerker in Small-/Microcaps konzentriert ist als Preis-Momentum, ist ein aehnlich hoher oder hoeherer prozentualer Kosten-Abzug plausibel. Kombiniert mit dem oben gezeigten fast vollstaendigen Verschwinden des Effekts in liquiden Titeln (Chordia et al. 2009) ist die begruendete Erwartung: **Netto-Rendite im liquiden, institutionell handelbaren Universum nicht robust von Null unterscheidbar.**

### f) Kapazitaet und Handelbarkeit

Sehr gering als Standalone-Strategie. Da der oekonomisch signifikante Teil des Effekts in illiquiden Small-/Microcaps sitzt, ist die Strategie bei institutioneller Groesse (>$100-500M) kaum ohne massiven Market Impact umsetzbar. Short-Seite zusaetzlich durch Leihkosten/-verfuegbarkeit eingeschraenkt. Als Signal-Tilt/Overlay in einem grossen, diversifizierten Long/Short-Buch (wo SUE nur eine von vielen Gewichtungs-Inputs ist und keine eigene Namensselektion mit Konzentration in Microcaps erzwingt) ist die effektive Kapazitaet deutlich hoeher, aber dann ist es auch keine eigenstaendige "Earnings Drift"-Strategie mehr, sondern ein Signal-Beitrag.

### g) Regimeabhaengigkeit und Tail-Risiko

- Staerker in Perioden geringerer algorithmischer Arbitrage-Aktivitaet (vor 2001) und in Small Caps mit geringer Analystenabdeckung.
- Schwaecher/instabiler in Hochvolatilitaetsregimen, da Ergebnisueberraschungen (SUE) selbst verrauschter werden und die Persistenzannahme (positive Autokorrelation der Earnings-Aenderungen) in Rezessionen/Strukturbruechen weniger zuverlaessig ist (z. B. 2020 COVID-Quartale mit extremen, nicht-repraesentativen Ueberraschungen).
- Konzentrationsrisiko: da die Strategie in wenigen Wochen pro Quartal (Earnings Season) fast alle Positionsaenderungen vornimmt, ist das Ertragsprofil "lumpy" und anfaellig fuer Klumpenrisiko rund um Berichtstermine (Gap-Risiko bei Ueberraschungen der Ueberraschung, z. B. Guidance-Aenderungen).
- Short-Seite mit Crash-/Squeeze-Risiko in Melt-up-Phasen: kleine Short-Seiten-Titel mit negativer SUE koennen bei Short-Squeezes (Meme-Stock-Dynamik seit 2021) extreme Tail-Verluste erzeugen.

### h) Bekannte Kritik/Widerlegungen

- **Mikrostruktur-Artefakt:** Chordia et al. (2009) — Effekt praktisch bei liquidesten Titeln verschwunden.
- **Microcap-Konzentration:** Hou/Xue/Zhang (2020) — unter NYSE-Breakpoints/VW nicht signifikant.
- **Look-Ahead-/Datenqualitaets-Bias in frueher Literatur:** Fruehe Compustat-Zeitreihen-SUE-Studien litten unter Survivorship- und Restatement-Problemen (nachtraeglich korrigierte Fundamentaldaten wurden teils benutzt, als waeren sie zum Handelszeitpunkt bekannt gewesen); spaetere IBES-basierte Studien (Livnat & Mendenhall 2006) sind robuster, aber IBES-Punkt-in-Zeit-Daten vor Mitte-1990er sind ebenfalls luecken- und revisionsanfaellig.
- **Publication-/Data-Mining-Bias generell:** McLean & Pontiff (2016) liefern einen belastbaren Rahmen (26%/58% Decay), der bei SUE mindestens im gleichen Ausmass, eher staerker (wegen der beobachteten Konzentration in am schwersten handelbaren Titeln) zu erwarten ist.

**Urteil: KILL.** Fuer eine eigenstaendige, in institutioneller Groesse handelbare Strategie ist die Nullhypothese ("kein echtes handelbares Netto-Alpha") nicht verworfen. Der beobachtete Rest-Effekt ist ueberwiegend eine Kompensation fuer Illiquiditaet/Handelskosten in Small-Caps, kein sauberer Verhaltensanomalie-Extrakt.

---

## 2. Kandidat 2: Preis- + Earnings-Momentum kombiniert (Chan, Jegadeesh & Lakonishok 1996)

### a) Oekonomische Begruendung

Chan/Jegadeesh/Lakonishok (1996, Journal of Finance) zeigen, dass sowohl vergangene Rendite als auch vergangene Earnings-Ueberraschung **je eigenstaendig** zukuenftige Drift vorhersagen, auch nach Kontrolle fuer die jeweils andere Variable — Marktrisiko, Size und Book-to-Market erklaeren die Drift nicht. Oekonomisch wird dies primaer als **Unterreaktion** interpretiert: Sell-Side-Analysten passen Gewinnschaetzungen "sluggish" an vergangene Informationen an, besonders bei den zuvor schlechtesten Performern; der Preis inkorporiert daher sowohl die Preis- als auch die Earnings-Information nur graduell. Es handelt sich um denselben Verhaltensmechanismus wie bei Kandidat 1 (Unteraufmerksamkeit/verzoegerte Erwartungsanpassung), jedoch durch Kombination zweier korrelierter, aber nicht redundanter Signale robuster gemacht (geringeres Rauschen pro Bet).

### b) Limits to Arbitrage

Dieselben Grundmechanismen wie bei Kandidat 1 (idiosynkratisches Risiko, Short-Constraints), aber gemildert, weil Preis-Momentum tendenziell etwas liquidere, staerker gehandelte/gefolgte Namen selektiert als reine SUE-Deciles. Dafuer tritt ein neues, gut dokumentiertes Arbitrage-Limit hinzu: **Momentum-Crash-Risiko** (Daniel & Moskowitz 2016) — bei scharfen Markt-Erholungen nach Baissen (z. B. 2009) erleidet die Short-Seite von Momentum-Strategien extreme, hochkorrelierte Verluste, was Risikokapital-Bereitstellung durch Arbitrageure strukturell begrenzt (niemand will eine Strategie mit Crash-Exposure in beliebiger Groesse unterhalten).

### c) Originalstudie

**Chan, Jegadeesh & Lakonishok (1996), Journal of Finance, Vol. 51(5), S. 1681-1713.** US-Aktien, Sample-Periode ca. 1977-1993 (NYSE/AMEX/NASDAQ). Kernbefund: Kombination aus Preis-Momentum (6-Monats-Formationsperiode) und SUE-basiertem Earnings-Momentum erzeugt groessere und persistentere Drift als jedes Signal einzeln; kaum Anzeichen fuer nachfolgende Reversal-Effekte bei Aktien mit hohem Preis- und Earnings-Momentum gleichzeitig. Genaue Original-t-Statistiken der kombinierten Deciles waren ueber Websuche nicht im Detail auffindbar (Primaerquelle hinter Paywall); die Studie gilt aber als eine der meistzitierten Momentum-Arbeiten und ist Bestandteil praktisch aller spaeteren Multi-Faktor-Repliken.

### d) Out-of-Sample-/Post-Publication-Evidenz

- Preis-Momentum als Basisfaktor ist eine der am robustesten replizierten Anomalien weltweit (Asness/Moskowitz/Pedersen 2013 "Value and Momentum Everywhere": signifikant in 8 Anlageklassen und Regionen); dies staerkt die Reproduzierbarkeit des Kandidaten indirekt, auch wenn der spezifische Earnings-Momentum-Zusatzbeitrag weniger breit unabhaengig repliziert ist.
- Im Hou/Xue/Zhang (2020)-Rahmen ueberlebt reines Preis-Momentum die strengen Hurdles i. d. R. deutlich besser als SUE (t-Statistiken meist > 3 in deren Tabellen für Momentum-Familie), was nahelegt, dass der Preis-Momentum-Teil der Kombination die tragende Saeule ist, waehrend der zusaetzliche marginale Beitrag des Earnings-Signals schwerer sauber zu isolieren und zu belegen ist.
- McLean & Pontiff (2016)-Rahmen gilt auch hier als Prior: -26%/-58% Decay Out-of-Sample/Post-Publication ueber die durchschnittliche Anomalie hinweg; fuer stark gehandelte, bekannte Faktoren wie Momentum wird eher der obere Bereich dieses Decay-Bandes erwartet (mehr Crowding durch hoehere Bekanntheit).
- Keine spezifische, dediziert auf die **Kombination** SUE+Preis-Momentum bezogene Post-2010-Decay-Studie in der Websuche gefunden; dies ist eine dokumentierte Evidenzluecke und Grund fuer WEAK statt CANDIDATE.

### e) Kosten

Novy-Marx & Velikov (2016): Preis-Momentum brutto **16.0% p.a. -> netto 8.16% p.a.** nach realistischen Effektiv-Spread-Kosten — ein Kostenabzug von rund der Haelfte, aber die verbleibende Netto-Rendite bleibt oekonomisch und statistisch relevant. Frazzini, Israel & Moskowitz (2018, "Trading Costs", live Handelsdaten von fast $1 Billion AUM ueber 19 entwickelte Maerkte 1998-2011) finden, dass Size-, Value- und Momentum-Praemien **netto robust bleiben**, Momentum aber am kostensensitivsten der drei ist. Diese Zahlen beziehen sich auf reines Preis-Momentum; die Earnings-Momentum-Komponente duerfte wegen zusaetzlicher Konzentration in Ereignisfenstern und teils kleineren Titeln tendenziell etwas kostenintensiver sein als der Preis-Momentum-Kern allein.

### f) Kapazitaet und Handelbarkeit

Novy-Marx & Velikov (2016) schaetzen die Carrying Capacity von Preis-Momentum auf rund **$5 Mrd.** (deutlich niedriger als Size mit $170 Mrd. oder Value mit $50 Mrd.) — Momentum ist bereits unter den kostenintensivsten/am wenigsten skalierbaren robusten Faktoren. Fuer die spezifische Earnings-Momentum-Overlay-Variante ist die effektive Kapazitaet eher am unteren Ende dieser Bandbreite oder darunter anzusiedeln, da das Overlay die Titelselektion zusaetzlich einschraenkt (Schnittmenge aus Preis-Momentum- und SUE-Bedingung reduziert das investierbare Universum).

### g) Regimeabhaengigkeit und Tail-Risiko

Zentrale bekannte Schwaeche: **Momentum-Crash-Risiko.** Daniel & Moskowitz (2016) dokumentieren, dass Momentum-Strategien nach starken Markt-Drawdowns mit anschliessender scharfer Erholung (Paradebeispiel: 2009) extreme, stark negativ schiefe Verluste erleiden koennen (in der Originalarbeit teils >-50% ueber wenige Monate fuer das reine Momentum-Long/Short-Buch), da die Short-Seite (vormalige Verlierer) in der Erholung ueberproportional stark steigt. Das Earnings-Momentum-Overlay reduziert dieses Risiko nicht grundsaetzlich, da es denselben Long/Short-Aufbau teilt. Zusaetzlich: hohe Korrelation mit dem meistgehandelten Faktor der Branche (Crowding-Risiko; viele CTAs/quantitative Multi-Strat-Fonds halten Momentum-Exposure, was in Stress-Perioden zu synchronisierten Deleveraging-Verlusten fuehren kann, wie in Teilen des August-2007-Quant-Crashes beobachtet, wenngleich dort primaer klassisches Preis-Momentum/Statistical-Arbitrage betroffen war).

### h) Bekannte Kritik/Widerlegungen

- Groesster Teil der Rendite laesst sich dem reinen Preis-Momentum zuschreiben; der inkrementelle Earnings-Signal-Beitrag ist schwerer separat zu validieren und daher staerker Data-Mining-/Spezifikationssuche-verdaechtig (bei >300 im Chen&Zimmermann-Katalog erfassten publizierten Charakteristiken ist die Wahrscheinlichkeit hoch, dass Kombinationen zweier korrelierter, je fuer sich bekannter Signale zufaellig gute In-Sample-Fit-Werte erzeugen).
- Momentum-Crash-Evidenz (Daniel & Moskowitz 2016) ist eine der am besten dokumentierten Tail-Risk-Widerlegungen einer "sauberen" Risikoadjustierung fuer diese Faktorfamilie.
- Hohe Bekanntheit/Crowding seit den 1990ern reduziert die Wahrscheinlichkeit signifikanten Rest-Alphas fuer neue Marktteilnehmer.

**Urteil: WEAK.** Real existierende, oekonomisch sinnvoll begruendete und teils kostenrobuste Renditequelle (getragen primaer vom Preis-Momentum-Kern), aber mit signifikantem Crash-/Tail-Risiko, begrenzter Kapazitaet (~$5 Mrd. Branchenweit fuer Momentum insgesamt) und duenner dedizierter Post-Publication-Evidenz fuer den spezifischen Earnings-Momentum-Zusatznutzen. Nicht CANDIDATE, weil die Kostenrobustheit und Regimestabilitaet zu grenzwertig sind fuer ein uneingeschraenktes "wahrscheinlich echte handelbare Netto-Ineffizienz"-Urteil.

---

## 3. Kandidat 3: Analysten-basierte SUE / kombinierte Signale (Livnat & Mendenhall 2006; Brandt, Kishore, Santa-Clara & Venkatachalam 2008)

### a) Oekonomische Begruendung

Livnat & Mendenhall (2006, Journal of Accounting Research) zeigen, dass die Drift **signifikant groesser** ist, wenn die Ueberraschung anhand von Analystenschaetzungen (I/B/E/S) statt eines Zeitreihenmodells (Compustat, "random walk + drift") berechnet wird. Interpretation: Analystenschaetzungen enthalten mehr aktuelle Information (Guidance, Branchentrends), sodass Abweichungen von ihnen ein "saubereres" Ueberraschungssignal darstellen als Abweichungen von einem simplen statistischen Modell. Brandt, Kishore, Santa-Clara & Venkatachalam (2008, "Earnings Announcements are Full of Surprises") kombinieren zusaetzlich die Rendite am Ankuendigungstag selbst (Earnings Announcement Return, EAR) mit SUE und zeigen hoehere Sharpe-Ratios fuer das kombinierte Signal als fuer jedes einzeln. Oekonomisch bleibt der Treiber derselbe Unteraufmerksamkeits-/Unterreaktions-Mechanismus, nur mit weniger verrauschter Signalkonstruktion.

### b) Limits to Arbitrage

Identisch zu Kandidat 1 (Illiquiditaet, idiosynkratisches Risiko, Short-Constraints), da dasselbe Aktienuniversum und dieselbe Ereignisstruktur (Earnings-Ankuendigungsfenster) zugrunde liegen. Zusaetzliches Limit: Analystenschaetzungsdaten (IBES) sind selbst nicht kostenlos/lückenlos und historisch fuer kleinere/weniger gefolgte Titel duenner abgedeckt — was den handelbaren Kern des Signals tendenziell auf noch groessere, aber dafuer noch staerker arbitrierte Namen verengt.

### c) Originalstudie

**Livnat & Mendenhall (2006), Journal of Accounting Research 44(1), S. 177-205.** Kernbefund: Drift bei analysten-basierter SUE deutlich groesser als bei zeitreihen-basierter SUE; Kombination beider Signale erhoeht die Drift-Magnitude weiter gegenueber jedem Einzelsignal. **Brandt et al. (2008)** (Sekundaerquelle: Quantpedia-Zusammenfassung, Original in Journal of Accounting and Economics): Sample 1987-2004, US-Universum ca. 1.000 Aktien (NYSE/AMEX/NASDAQ, ex Financials/Utilities, Preis>$5), Quartalsrebalancing, 60-Handelstage-Haltefrist. Kombinierte EAR+SUE-Strategie: **~12.5% p.a. abnormale Rendite**; SUE allein niedriger, EAR allein **~7.55% p.a.**; max. Drawdown der kombinierten Strategie **-11.2%**. Praezise t-Statistiken der Originalarbeit waren ueber die verfuegbare Sekundaerquelle nicht vollstaendig extrahierbar.

### d) Out-of-Sample-/Post-Publication-Evidenz

Schwaechste Evidenzbasis der drei Kandidaten: Weder Hou/Xue/Zhang (2020) noch McLean & Pontiff (2016) enthalten (soweit ueber Websuche auffindbar) eine dedizierte Nachpruefung exakt dieser analysten-basierten/kombinierten Signalvariante unter strengen Multiple-Testing-Hurdles. Die internationale Replikationsliteratur zu PEAD allgemein (siehe Kandidat 1, Abschnitt d) bestaetigt die Richtung des Grundphaenomens, nicht spezifisch die inkrementelle Verbesserung durch Analystendaten oder EAR-Kombination. Gegeben, dass (i) der zugrunde liegende Bernard-Thomas-Mechanismus nachweislich stark dekayed ist (Kandidat 1) und (ii) IBES-Analystendaten seit den 2000ern selbst intensiv von Quant-Fonds verarbeitet werden (Analyst-Revision-Signale sind seit Jahrzehnten Standard-Input in Multi-Faktor-Modellen), ist ein aehnlich starker oder staerkerer Post-Publication-Decay wie bei Kandidat 1 die plausible Grundannahme, auch ohne direkte Zahlenbestaetigung.

### e) Kosten

Keine dedizierte Netto-Kosten-Studie speziell fuer diese Variante gefunden. Da Universum und Rebalancing-Struktur nahezu identisch zu Kandidat 1 sind (Quartalsrebalancing, aehnliche Marktkapitalisierungsverteilung), ist eine aehnliche Kostensensitivitaet wie dort zu erwarten, tendenziell etwas guenstiger, weil das IBES-Coverage-Erfordernis das Universum leicht in Richtung groesserer/liquiderer Titel verschiebt.

### f) Kapazitaet und Handelbarkeit

Gering bis moderat. Etwas besser als Kandidat 1 durch den Liquiditaets-Bias aus dem IBES-Coverage-Filter, aber nicht in der Groessenordnung von Value/Size/Momentum-Kapazitaeten. Realistische Schaetzung (eigene, konservativ, ohne belastbare Primaerquelle): niedriger dreistelliger Millionenbereich USD als eigenstaendige Strategie, bevor Slippage die Netto-Rendite materiell zusammendrueckt.

### g) Regimeabhaengigkeit und Tail-Risiko

Aehnlich zu Kandidat 1: Ereignis-konzentriert (Earnings Season), anfaellig fuer Guidance-Ueberraschungen und Regime mit hoher makrooekonomischer Unsicherheit, in denen Analystenschaetzungen selbst wenig verlaesslich werden (z. B. 2020, 2022 Inflationsschock-Quartale). Kein dediziertes Crash-Studien-Ergebnis gefunden; Tail-Risiko wird als aehnlich zu Kandidat 1 eingeschaetzt (Short-Squeeze-Exposure auf der Negativ-Ueberraschungs-Seite).

### h) Bekannte Kritik/Widerlegungen

- Gleiche Mikrostruktur-/Microcap-Kritik wie Kandidat 1, abgeschwaecht durch IBES-Filter, aber nicht aufgehoben.
- **Look-ahead-Risiko:** IBES-Punkt-in-Zeit-Daten vor Mitte-1990er sind bekanntermassen luecken- und revisionsanfaellig; Studien, die "as-reported"-Konsensschaetzungen unsauber rekonstruieren, koennen Rendite-Zahlen ueberschaetzen.
- Data-Snooping-Risiko durch Signal-Kombination (EAR+SUE): Sobald mehrere korrelierte, individuell bereits bekannte Signale kombiniert werden, steigt die Wahrscheinlichkeit einer in-sample optimierten, aber out-of-sample nicht replizierbaren Gewichtung — genau der Mechanismus, den Hou/Xue/Zhang und McLean/Pontiff als Haupterklaerung fuer generellen Anomalie-Decay identifizieren.

**Urteil: WEAK.** Oekonomisch derselbe, in Kandidat 1 bereits stark relativierte Mechanismus, mit einer methodisch plausiblen, aber empirisch duenn ueberprueften Verbesserung durch bessere Signalkonstruktion. Ohne eigene Post-Publication-Decay-Studie kann kein CANDIDATE-Urteil vergeben werden.

---

## 4. Klassenweites Fazit

**Ist die Klasse "Earnings Drift" tot?** Nicht vollstaendig, aber der klassische, in Lehrbuechern und vielen Retail-orientierten "Backtests" zitierte SUE-Decile-Spread-Ansatz ist nach heutigem Evidenzstand **KILL** fuer institutionelle Skalierung: Die Kombination aus (i) Nicht-Signifikanz unter strengeren Replikationsstandards (Hou/Xue/Zhang t=1.0-1.65), (ii) fast vollstaendiger Konzentration des Effekts in illiquiden Titeln (Chordia et al. 2009: 0.04% vs. 2.43%/Monat) und (iii) dokumentiertem strukturellem Decay seit Dezimalisierung (Chordia/Subrahmanyam/Tong 2014) ergibt ein sehr geringes p_echte_ineffizienz.

Die robustere Teilmenge — **Preis-Momentum mit Earnings-Momentum-Overlay** — ueberlebt als WEAK, getragen primaer vom breit replizierten Preis-Momentum-Kern, mit dem bekannten Schwachpunkt asymmetrischer Crash-Risiken und begrenzter Kapazitaet (~$5 Mrd. Branchenschaetzung fuer Momentum insgesamt, Novy-Marx & Velikov 2016).

Die verfeinerten, analysten-/multi-signal-basierten Varianten (Livnat & Mendenhall 2006; Brandt et al. 2008) bleiben ebenfalls WEAK — methodisch plausibler, aber mit einer auffaelligen Evidenzluecke: keiner der grossen Post-Publication-Replikationsrahmen (McLean & Pontiff 2016, Hou/Xue/Zhang 2020) hat sie dediziert unter Multiple-Testing-Bedingungen nachgeprueft.

**Kein Kandidat dieser Klasse erreicht CANDIDATE-Status.** Fuer ein CANDIDATE-Urteil waere dokumentierte Post-Publication-Evidenz UND Kostenrobustheit gefordert — bei Kandidat 1 widerlegt die Post-Publication-Evidenz die Strategie explizit; bei Kandidat 2 und 3 fehlt eine hinreichend belastbare, dedizierte Post-Publication-Bestaetigung der inkrementellen Earnings-Signal-Komponente (im Gegensatz zum bereits separat gut dokumentierten Preis-Momentum-Kern).

**Ehrliches Ergebnis:** Earnings Drift als eigenstaendige, handelbare Anomalie ist ueberwiegend widerlegt bzw. auf Kompensation fuer Illiquiditaet/Handelskosten zurueckzufuehren. Als Nebensignal in einem breiteren, multi-faktoriellen, kostenoptimierten Buch mag ein kleiner Rest-Beitrag existieren, aber keiner der drei Kandidaten rechtfertigt eine eigenstaendige Kapitalallokation auf Basis der hier zusammengetragenen Evidenz.

---

## 5. Quellen (aus Websuche, Juli 2026)

- Bernard, V. & Thomas, J. (1989). "Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?" Journal of Accounting Research.
- Bernard, V. & Thomas, J. (1990). "Evidence That Stock Prices Do Not Fully Reflect the Implications of Current Earnings for Future Earnings." Journal of Accounting and Economics.
- Chan, L., Jegadeesh, N. & Lakonishok, J. (1996). "Momentum Strategies." Journal of Finance 51(5), 1681-1713. https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1996.tb05222.x
- Chordia, T., Goyal, A., Sadka, G., Sadka, R. & Shivakumar, L. (2009). "Liquidity and the Post-Earnings-Announcement Drift." Financial Analysts Journal 65(4), 18-32. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1403342
- Chordia, T., Subrahmanyam, A. & Tong, Q. (2014). "Have Capital Market Anomalies Attenuated in the Recent Era of High Liquidity and Trading Activity?" Journal of Accounting and Economics 58(1), 41-58. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2029057
- Hou, K., Xue, C. & Zhang, L. (2020). "Replicating Anomalies." Review of Financial Studies 33(5), 2019-2133. https://global-q.org/uploads/1/2/2/6/122679606/houxuezhang2020rfs.pdf
- Livnat, J. & Mendenhall, R. (2006). "Comparing the Post-Earnings Announcement Drift for Surprises Calculated from Analyst and Time Series Forecasts." Journal of Accounting Research 44(1), 177-205. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1475-679X.2006.00196.x
- McLean, R. D. & Pontiff, J. (2016). "Does Academic Research Destroy Stock Return Predictability?" Journal of Finance 71(1), 5-32. https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365
- Novy-Marx, R. & Velikov, M. (2016). "A Taxonomy of Anomalies and Their Trading Costs." Review of Financial Studies 29(1), 104-147. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2535173
- Frazzini, A., Israel, R. & Moskowitz, T. (2018). "Trading Costs." SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3229719
- Chen, A. Y. & Zimmermann, T. (2021/2022). "Open Source Cross-Sectional Asset Pricing." Critical Finance Review. https://www.openassetpricing.com/
- Brandt, M., Kishore, R., Santa-Clara, P. & Venkatachalam, M. (2008). "Earnings Announcements are Full of Surprises." (Zusammenfassung via Quantpedia: https://quantpedia.com/strategies/post-earnings-announcement-effect)
- Daniel, K. & Moskowitz, T. (2016). "Momentum Crashes." Journal of Financial Economics (referenziert fuer Tail-Risk-Diskussion, internes Wissen ergaenzt, da nicht explizit in dieser Session ueber Websuche verifiziert).

**Hinweis zu Einzelbefunden ohne belastbare Primaerquelle:** Die Aussage "PEAD bei Non-Microcaps verschwindet ab ~2001, bei Large Caps ab ~2006 statistisch insignifikant" stammt aus einer nicht-akademischen Sekundaerquelle (Blog/Substack) und wird hier nur als richtungskonsistente, nicht als quantitativ verlaessliche Ergaenzung zu den peer-reviewten Kernbefunden gefuehrt.
