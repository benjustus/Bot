```yaml
agent: 02
klasse: "Analystenrevisionen"
websuche_verfuegbar: ja
strategien:
  - name: "Analysten-Empfehlungsrevisionen (Konsensus-Recommendation Upgrades/Downgrades)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 3
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0.0-0.2"
    kernrisiko: "Barber/Lehavy/McNichols/Trueman (2001) zeigen explizit: tägliches Rebalancing noetig fuer Bruttoalpha >4%/Jahr, Nettorendite nach Kosten 'not reliably greater than zero'. Zusaetzlich Short-Squeeze-/Crowding-Risiko auf der Downgrade-Short-Seite in Melt-up-Regimen."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
  - name: "Analysten-EPS-Prognoserevisionen (Consensus Earnings Forecast Revisions / 'dEf', 'Re')"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 4
      regimestabilitaet: 3
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.45
    netto_sharpe_erwartung: "0.1-0.3"
    kernrisiko: "Hoher Portfolio-Turnover durch haeufige Konsensus-Updates; Konzentration in Small/Mid Caps mit geringer Coverage begrenzt Kapazitaet; substanzielle Ueberlappung mit Preis-/Earnings-Momentum erschwert Nachweis von inkrementellem Signal nach Kosten."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Open Source Asset Pricing (Chen & Zimmermann, openassetpricing.com) - Signal 'REV6'/'ChgEarnings'/'dEf' Portfolio-Returns (Signal-Rohdaten stammen aus IBES, aber prozessierte Faktor-Returns sind frei abrufbar)"
  - name: "Kursziel-Revisionen (Analyst Target Price Changes)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "0.0-0.1 (vermutlich ~0)"
    kernrisiko: "Analysten-Overoptimism-Bias (im Schnitt implizieren 12-Monats-Kursziele ~28% Kurssteigerung, die selten erreicht wird) verzerrt das Level-Signal; die Revisions-Komponente ist stark kollinear mit Recommendation- und EPS-Revisionen, daher fraglich ob eigenstaendiger inkrementeller Wert; duenne unabhaengige Post-Publication-Replikationsbasis als Standalone-Faktor."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
```

# Anomalieklasse: Analystenrevisionen — Adversarial Review

**Agent 02 | Stand: Juli 2026 | Evidenzbasis: Web-Recherche (WebSearch verfuegbar) + internes Wissen**

## Executive Summary

Die Nullhypothese lautet: Es gibt kein handelbares Netto-Alpha in Analystenrevisionen. Nach Durchsicht der Kernliteratur wird diese Nullhypothese **nicht vollstaendig bestaetigt, aber auch nicht widerlegt**. Es existiert ein robuster, jahrzehntelang repliziertes *Brutto*-Informationseffekt: Aenderungen in Analystenmeinungen (Empfehlungen, EPS-Schaetzungen, Kursziele) sagen Renditen der Folgeperiode voraus, und die Effekte ueberleben grob den klassischen "ist es nur Data-Mining"-Test (Hou/Xue/Zhang 2020 bestaetigen z.B. die EPS-Revisionsvariable als eine der Minderheit von Anomalien, die den strengen NYSE-Breakpoint/Value-Weight/|t|>1.96-Test besteht). Das Problem liegt nicht primaer in der Statistik, sondern in **Kosten und Kapazitaet**: Die direkteste und methodisch sauberste Nettorendite-Studie der Klasse (Barber, Lehavy, McNichols, Trueman 2001, JF) kommt zu dem expliziten Ergebnis, dass die fuer die Bruttorendite noetige taegliche Portfolioumschichtung die Nettorendite auf "nicht zuverlaessig groesser als null" druecht. Das ist eine seltene, sehr direkte Falsifikation einer ganzen Anomalie-Unterklasse durch die Originalautoren-Tradition selbst (nicht durch spaetere Kritiker).

Ergebnis: **Keine der drei geprueften Strategien erreicht den CANDIDATE-Status.** Zwei werden als WEAK eingestuft (realer Effekt, aber Kosten-/Kapazitaetsgrenzen ungeklaert bzw. nachweislich prohibitiv in der einfachsten Umsetzung), eine wird als KILL eingestuft (Kursziel-Revisionen: zu duenne unabhaengige Evidenz, hohe Kollinearitaet mit den anderen beiden, dokumentierter struktureller Bias).

---

## Kandidat 1: Analysten-Empfehlungsrevisionen (Recommendation Upgrades/Downgrades)

### a) Oekonomische Begruendung

Mechanismus: **Graduelle Informationsdiffusion / Unteraktion (underreaction)** in Kombination mit der Rolle von Sell-Side-Analysten als Informationsintermediäre. Analysten aggregieren private Kanalcheckerkenntnisse, Branchenexpertise und Managementkontakte in ein diskretes Signal (Upgrade/Downgrade). Der Markt – insbesondere weniger aufmerksame/kapazitaetsbeschraenkte Investoren (Retail, kleinere Institutionelle) – verarbeitet dieses Signal nicht sofort vollstaendig; es entsteht Post-Event-Drift. Das ist konsistent mit Hong & Stein (1999)-artiger gradueller Informationsdiffusion und mit begrenzter Aufmerksamkeit (limited attention) der Marktteilnehmer. Verursacher der Fehlbewertung: primaer Retail-/langsame Institutionelle, die Downgrades (unangenehme, verkaufsgetriebene Information) langsamer einpreisen als Upgrades.

Eine zweite, konkurrierende Erklaerung: Es handelt sich teils um eine **Kompensation fuer Informationsproduktionskosten** der Analysten/deren Kunden (kein "freies" Alpha für Aussenstehende, sondern Rente für den, der zuerst reagiert) – das erklaert, warum Nettoeffekte fuer normale Investoren nahe null liegen (siehe c/e).

### b) Limits to Arbitrage

- **Asymmetrische Short-Constraints**: Womack (1996) findet fuer Sell-Empfehlungen einen 6-monatigen Post-Drift von -9.1% gegenueber nur +2.4% (kurzlebig) fuer Buy-Empfehlungen — konsistent mit Short-Sale-Beschraenkungen, die das Wegarbitrieren der negativen Seite erschweren.
- **Turnover-Zwang**: Um die Bruttorendite zu erfassen, ist nach BLMT (2001) taegliches Rebalancing bei zeitnaher Reaktion auf Revisionen notwendig — das treibt Spread-/Market-Impact-Kosten in genau die Groessenordnung der Bruttoanomalie.
- **Small-/Mid-Cap-Konzentration**: Effekt ist in weniger liquiden, weniger gut gecoverten Titeln staerker, wo Spreads und Impact am hoechsten sind.
- **Herding der Analysten** (Analysten grosser Broker, Analysten mit geringer Abweichung vom Konsens, seltene Revidierer herden staerker) daempft die Informationshaltigkeit einzelner Revisionen und macht Signal-Extraktion noisy.

### c) Originalstudien

- **Womack (1996)**, *"Do Brokerage Analysts' Recommendations Have Investment Value?"*, JF 51(1), 137-167. Stichprobe: >1.500 Empfehlungsaenderungen von 14 US-Brokern (1989-1991). Effektgroesse: Buy-Empfehlung → +3.0% groessenbereinigte Kursreaktion; Sell-Empfehlung → -4.7%. Post-Event-Drift: Buy +2.4% (kurzlebig), Sell -9.1% ueber 6 Monate.
- **Barber, Lehavy, McNichols, Trueman (2001)**, *"Can Investors Profit from the Prophets?"*, JF 56(2), 531-563. Long-Short auf Konsensusempfehlungsniveau/-aenderungen mit taeglichem Rebalancing: Bruttoabnormalrendite >4%/Jahr, aber Nettorendite nach realistischen Transaktionskosten "not reliably greater than zero".
- **Jegadeesh, Kim, Krische, Lee (2004)**, *"Analyzing the Analysts: When Do Recommendations Add Value?"*, JF 59(3), 1083-1124. Zentrales Ergebnis: Die *quartalsweise Aenderung* der Konsensusempfehlung ist ein robuster Praediktor mit Information orthogonal zu einer breiten Reihe anderer Praediktoren (Value, Momentum etc.) — das Level allein ist deutlich schwaecher und teils kontraproduktiv bei "Glamour"-Aktien.

### d) Out-of-Sample-/Post-Publication-Evidenz

- **Hou/Xue/Zhang (2020)**, "Replicating Anomalies", RFS 33(5): In ihrer Bibliothek von 452 Anomalien ueberleben unter strengen Bedingungen (NYSE-Breakpoints, Value-Weighting, |t|>1.96) nur 35%; 96% der "Trading Frictions"-Kategorie fallen durch. Empfehlungs-/Revisions-nahe Variablen liegen tendenziell in den robusteren Clustern (Momentum-verwandt), aber ich habe keine belastbare, spezifische Post-2010-Netto-Zahl fuer die reine Empfehlungsrevision gefunden — Vorsicht vor Ueberinterpretation.
- **McLean & Pontiff (2016)**, JF 71(1): Portfolios auf Basis von 97 publizierten Praediktoren zeigen 26% niedrigere Renditen out-of-sample und 58% niedrigere Renditen post-publication. Wichtige Einschraenkung fuer unsere Klasse: Deren Stichprobe stammt ueberwiegend aus CRSP/Compustat-berechenbaren Characteristics; IBES-basierte Analysten-Variablen sind darin nicht prominent vertreten. Die MP-Decay-Zahlen sind daher **nicht direkt uebertragbar** — ich zitiere sie als generelles Precedent fuer Publikations-Decay, nicht als spezifischen Beleg fuer diese Strategie.
- **Strukturbruch-Argument (qualitativ, kein hartes Decay-%)**: Reg FD (2000) und der Global Analyst Research Settlement (2003) veraenderten das Informationsumfeld fundamental (Verbot selektiver Guidance, Trennung Research/Investment-Banking). Seit den 2000ern ist Recommendation-Revision-Information ausserdem via Bloomberg/Refinitiv/StarMine in Echtzeit kommerzialisiert und in quantitative Screens/Barra-artige Risikomodelle eingebettet — das ist ein plausibler, aber nicht mit harter Zahl belegter Crowding-Kanal.

### e) Kosten

BLMT (2001) ist hier die Schluesselstudie: Bei realistischer Umsetzung (taegliches Rebalancing zur zeitnahen Erfassung von Revisionen) frisst der Spread/Market-Impact **den gesamten Bruttoeffekt** auf. Novy-Marx & Velikov (2016, RFS, "A Taxonomy of Anomalies and Their Trading Costs") ordnen Hochumschlags-Anomalien (>50%/Monat Turnover) generell in die Kategorie "nach Kosten meist nicht signifikant" ein — Empfehlungsrevisionen mit ihrem ereignisgetriebenen, hochfrequenten Charakter fallen tendenziell in dieses Muster, auch wenn Cost-Mitigation-Techniken (Buffering, geringere Rebalancing-Frequenz) einen Teil retten koennten.

### f) Kapazitaet und Handelbarkeit

IBES-gecoverte US-Titel: ca. 3.000-4.000, aber zu einem Zeitpunkt mit *materieller* Revision typischerweise nur 50-150 Titel/Monat, konzentriert in Small/Mid Caps mit ADV oft <20 Mio. USD/Tag. Geschaetzte Bruttokapazitaet niedriger einstelliger Milliarden-Bereich, netto (nach Impact bei institutioneller Groessenordnung) eher **<300-500 Mio. USD**, bevor Alpha durch Slippage merklich erodiert. Shortability der Downgrade-Seite ist in Small Caps oft eingeschraenkt (Borrow-Kosten, Hard-to-Borrow-Listen).

### g) Regimeabhaengigkeit und Tail-Risiko

Ausgepraegte Asymmetrie: Downgrade/Sell-Signal ist staerker und langlebiger als Upgrade/Buy-Signal — das deutet auf strukturell hoehere Fragilitaet der Short-Seite in Regimen mit Short-Squeeze-Dynamik (z.B. Meme-Stock-Episoden 2020/2021 als Extrembeispiel; generell in Melt-up-/Low-Vol-Bullenmaerkten mit hohem Retail-Anteil). In solchen Regimen kann die Short-Seite der Strategie linksschief werden (Crash-Risiko), waehrend die Long-Seite (Upgrades) tendenziell in Bullenmaerkten ohnehin wenig Zusatzalpha liefert (kurzlebiger Drift).

### h) Bekannte Kritik/Widerlegungen

- BLMT (2001) selbst ist die staerkste "Widerlegung" der Netto-Handelbarkeit.
- Analysten-Overoptimism/Interessenkonflikt (Investment-Banking-Beziehungen) verzerrt v.a. das *Level* der Empfehlung nach oben (Lin & McNichols 1998, Michaely & Womack 1999) — Revisionen sind robuster als Level, aber nicht immun.
- Ueberlappung mit klassischem Preis-Momentum: ein Teil des Effekts koennte doppelt gezaehlt sein, auch wenn JKKL (2004) Orthogonalitaet zeigen.
- Herding-Literatur (u.a. Studien zu Analysten grosser Broker und Konsensnaehe) relativiert den Informationsgehalt einzelner Revisionen.

---

## Kandidat 2: Analysten-EPS-Prognoserevisionen (Consensus Earnings Forecast Revisions)

### a) Oekonomische Begruendung

Analog zu Kandidat 1, aber auf der praeziseren, kontinuierlichen Groesse "Aenderung der Konsensus-EPS-Schaetzung" (statt diskreter Empfehlungsstufen). Mechanismus: **Unteraktion des Marktes auf neue fundamentale Information**, die in Analystenschaetzungen frueher erscheint als im Kurs — sogenannter "Post-Forecast-Revision Drift". Gleason & Lee (2003, *The Accounting Review* 78(1), 193-225) zeigen, dass der Markt nicht ausreichend zwischen "High-Innovation"-Revisionen (neue Information) und "Low-Innovation"-Revisionen (blosse Annaeherung an den Konsens) unterscheidet, und dass die Preisanpassung schneller/vollstaendiger ist bei Star-Analysten (Institutional Investor All-Stars) und bei Titeln mit hoeherer Coverage — d.h. die Fehlbewertung konzentriert sich systematisch bei obskureren Analysten und geringerer Coverage (dort, wo Informationsfriktion am groessten ist). Verursacher: wiederum primaer Investoren mit begrenzter Aufmerksamkeit/Verarbeitungskapazitaet, die Konsensverschiebungen erst mit Verzoegerung einpreisen.

### b) Limits to Arbitrage

- **Hohe Turnover-Anforderung**: Konsensrevisionen aktualisieren sich quasi-kontinuierlich (jedes Mal, wenn ein einzelner Analyst seine Schaetzung aendert, bewegt sich der Konsens leicht) — ein sauberer Trading-Trigger erfordert haeufiges Rebalancing.
- **Coverage-Bias**: Der Effekt ist am staerksten bei geringer Coverage/obskuren Analysten — genau dort, wo Liquiditaet/Spreads am ungünstigsten sind.
- **Ueberlappung mit Momentum**: Chan/Jegadeesh/Lakonishok (1996) zeigen, dass Revisionen mit Preis-Momentum korrelieren (aber nicht identisch sind) — professionelle Arbitrageure, die bereits Momentum handeln, absorbieren einen Teil des Signals indirekt, was die inkrementelle Opportunitaet fuer Dritte verkleinert.

### c) Originalstudien

- **Elton, Gruber, Grossman (1986)**, *"Discrete Expectational Data and Portfolio Performance"*, JF 41(3), 699-713. Fruehe Grundlagenarbeit: Portfolios sortiert nach Analystenschaetzungsrevisionen zeigen signifikante Performanceunterschiede ueber nachfolgende Perioden.
- **Stickel (1991)**, *"Common Stock Returns Surrounding Earnings Forecast Revisions: More Puzzling Evidence"*, JAR/Accounting Review-Familie: Kursreaktionen um Revisionsereignisse plus mehrmonatiger Drift.
- **Gleason & Lee (2003)**, s.o.: Grossangelegte Zerlegung des Post-Revisions-Drifts nach Innovationsgehalt und Analystenreputation.

### d) Out-of-Sample-/Post-Publication-Evidenz

- **Hou/Xue/Zhang (2020)** testen explizit "Revisions in analysts' earnings forecasts" (Re) und "Change in analysts' earnings forecasts" (dEf) in ihrer 452-Anomalien-Bibliothek. Bemerkenswert: dEf zeigt laut Suchergebnissen **grosse q-Faktor-Alphas in den High-minus-Low-Dezilen** und gehoert damit zur Minderheit, die den strengen Test (NYSE-Breakpoints, Value-Weighted, |t|>1.96) uebersteht — das ist eine der staerksten Post-Publication-Bestaetigungen, die ich fuer die gesamte Analystenrevisions-Klasse finden konnte.
- **Chen & Zimmermann, Open Source Asset Pricing** (openassetpricing.com): Fuehren analystenbasierte Signale (u.a. Revisionsmasse) in ihrer 300+-Signal-Bibliothek und liefern direkt herunterladbare Portfolio-Renditen — das erlaubt eigene Robustheitschecks (Decay seit 2000er-Jahre, Sample 1980-2024).
- Kein spezifisch fuer diese Variable dediziertes, mir bekanntes Nettorenditen-Papier (Novy-Marx/Velikov- oder Frazzini/Israel/Moskowitz-Stil) gefunden — das ist die zentrale Luecke, die CANDIDATE-Status verhindert.

### e) Kosten

Keine dedizierte Netto-Kostenstudie speziell fuer diese Variable identifiziert. Qualitativ: Turnover duerfte aehnlich hoch sein wie bei Empfehlungsrevisionen (haeufige Konsens-Updates), aber die Variable ist kontinuierlich (nicht diskret gestuft) und laesst sich potenziell mit Momentum-typischen Kostenminderungstechniken (Signal-Glaettung, No-Trade-Buffer, monatliche statt taegliche Rebalancing) besser handhaben als das diskrete Empfehlungssignal. Das ist jedoch eine Vermutung, keine belegte Zahl — daher konservative Einstufung "kostenrobustheit: 2".

### f) Kapazitaet und Handelbarkeit

Aehnliche Groessenordnung wie Kandidat 1: Konzentration in Small-/Mid-Caps mit geringerer Coverage begrenzt Kapazitaet auf wohl niedrige einstellige Milliarden brutto, deutlich weniger netto bei institutioneller Umsetzung. In Large-Cap-Universen ist der Effekt gemaess Gleason/Lee schwaecher (schnellere/vollstaendigere Preisanpassung bei hoher Coverage) — ein klassischer Zielkonflikt zwischen Signalstaerke und Liquiditaet.

### g) Regimeabhaengigkeit und Tail-Risiko

Vermutlich weniger extrem asymmetrisch als reine Empfehlungsrevisionen (kontinuierliches statt diskretes Signal daempft Tail-Ereignisse etwas), aber die Ueberlappung mit Momentum importiert tendenziell das bekannte Momentum-Crash-Risiko (Daniel & Moskowitz 2016: scharfe Verluste bei Markt-Rebounds nach Baerenmaerkten) fuer die Short-Seite in Erholungsphasen.

### h) Bekannte Kritik/Widerlegungen

- Kollinearitaet mit Preis-Momentum und mit "Standardized Unexpected Earnings" (SUE)/Post-Earnings-Announcement-Drift erschwert die Isolierung eines wirklich inkrementellen Analystenrevisions-Effekts.
- IBES-Konsensdaten sind bekannt fuer Staleness-Probleme (nicht jeder Analyst aktualisiert taeglich; "alte" Schaetzungen bleiben im Konsens, bis der Analyst reagiert) — das erzeugt Rauschen und potenzielle Look-Ahead-Fallen bei naiver Datenverwendung (Timing der tatsaechlichen Verfuegbarkeit vs. Report-Datum).
- Zunehmendes "Forecast Clustering" (Analysten schaetzen naeher am Konsens, teils wegen steigender Arbeitslast) ist in juengerer Literatur (2020er) dokumentiert und koennte die Informationshaltigkeit einzelner Revisionen im Zeitverlauf verwaessern — ein plausibler, aber nicht quantitativ belegter Decay-Kanal.

---

## Kandidat 3: Kursziel-Revisionen (Analyst Target Price Changes)

### a) Oekonomische Begruendung

Gleicher Grundmechanismus (Informationsintermediation, Unteraktion), aber Kursziele sind die "weichste" der drei Analysten-Outputgroessen — sie sind qualitativ nicht standardisiert (kein einheitliches Modell, Zeithorizont oft "12 Monate" aber uneinheitlich definiert) und praesentieren nachweislich einen systematischen Optimism-Bias.

### b) Limits to Arbitrage

Aehnlich wie Kandidaten 1/2, plus ein zusaetzliches Problem: Kursziele werden meist **gleichzeitig** mit Empfehlungsaenderungen und/oder EPS-Revisionen veroeffentlicht, was die Isolierung eines eigenstaendigen handelbaren Signals erschwert (Multikollinearitaet auf Ereignisebene).

### c) Originalstudien

- **Brav & Lehavy (2003)**, *"An Empirical Analysis of Analysts' Target Prices"*, JF: Im Schnitt impliziert das 1-Jahres-Kursziel eine Kurssteigerung von **28%** gegenueber dem aktuellen Kurs — deutlich mehr, als historisch realisiert wird. Das dokumentiert primaer einen Bias, nicht sauber ein handelbares Revisions-Alpha.
- **Asquith, Mikhail, Au (2005)**, JAE: Kurszieländerungen enthalten inkrementellen Informationsgehalt zusaetzlich zu Empfehlung und EPS-Prognose, aber die Studie ist duenner repliziert als Womack/BLMT/JKKL.

### d) Out-of-Sample-/Post-Publication-Evidenz

Ich konnte **keine** dedizierte grossangelegte Post-2010-Replikation oder Decay-Schaetzung spezifisch fuer Kurszielrevisionen als Standalone-Handelssignal finden (im Unterschied zu Empfehlungsrevisionen und EPS-Revisionen, die beide in Hou/Xue/Zhang 2020 bzw. der breiteren Anomalie-Bibliothek explizit vorkommen). Das ist selbst ein Warnsignal: Die Variable wird in der Praxis meist als Zusatzkomponente in kommerziellen Analysten-Composite-Scores (z.B. StarMine) verwendet, nicht als eigenstaendig in Top-Journals immer wieder unabhaengig validierter Faktor.

### e) Kosten

Keine dedizierte Netto-Kostenstudie gefunden. Angesichts der Ueberlappung mit den anderen beiden Signalen ist zu erwarten, dass ein reines Kurszielrevisions-Portfolio aehnliche oder schlechtere Kosteneigenschaften hat wie Kandidat 1 (BLMT-Analogieschluss), ohne dass eine eigene Studie das explizit zeigt.

### f) Kapazitaet und Handelbarkeit

Aehnliche strukturelle Grenzen wie Kandidaten 1/2, aber ohne eigene belastbare Kapazitaetsstudie – Einstufung uebernimmt konservativ die Werte der verwandten Signale.

### g) Regimeabhaengigkeit und Tail-Risiko

Kein eigenstaendiger Befund; der dokumentierte systematische Optimism-Bias (28%-Praemie) duerfte sich in Bullenmaerkten verstaerken (Analysten extrapolieren Kursstaerke) und die Netto-Information des Signals in genau den Phasen am meisten verwaessern, in denen viele Marktteilnehmer ohnehin bereits bullish sind – ein prozyklisches, wenig differenzierendes Signal in Trendphasen.

### h) Bekannte Kritik/Widerlegungen

- Der dokumentierte 28%-Optimism-Bias (Brav & Lehavy 2003) ist ein handfester Beleg gegen die Verwendung des *Levels*; fuer die *Revision* fehlt eine ebenso robuste, unabhaengig replizierte Evidenzbasis.
- Hohe Kollinearitaet mit Empfehlungs- und EPS-Revisionen wirft die Frage auf, ob ein eigenstaendiges "Kurszielrevisions-Alpha" ueberhaupt existiert oder ob gefundene Effekte in fruehen Studien schlicht die anderen beiden Signale mit-erfassen (Omitted-Variable-Problem in die andere Richtung).
- Kein/kaum konsequent aktualisierter Präsenz in modernen Open-Source-Anomalie-Bibliotheken (im Unterschied zu dEf/Re) gefunden — deutet auf geringere Reife/Konsens in der akademischen Literatur hin.

---

## Uebergreifende Einordnung

| Kriterium | Empfehlungsrevisionen | EPS-Revisionen | Kurszielrevisionen |
|---|---|---|---|
| Bruttosignal robust ueber Jahrzehnte repliziert | Ja | Ja (bestaetigt in HXZ 2020) | Schwach belegt |
| Explizite Nettokosten-Widerlegung vorhanden | Ja (BLMT 2001) | Nein explizit, aber Turnover-Analogie | Nein, keine Studie gefunden |
| Unabhaengig von Momentum/SUE nachgewiesen | Teilweise (JKKL 2004: orthogonal) | Unklar, hohe Korrelation vermutet | Unklar |
| Strukturelle Bias-Dokumentation | Ja (IB-Konflikte) | Geringer | Ja (28%-Zielkurs-Bias) |
| Freie Datenquelle fuer eigene Tests | Nein | Ja (OSAP) | Nein |

**Gesamturteil zur Klasse "Analystenrevisionen":** Die Klasse ist nicht tot im Sinne von "reines Data-Mining-Artefakt" — der zugrundeliegende Unteraktions-/Informationsdiffusions-Mechanismus ist oekonomisch plausibel, gut dokumentiert und in mehreren unabhaengigen Datensaetzen (US, international, ueber Jahrzehnte) repliziert. Sie ist aber auch kein sauberer CANDIDATE: Die einzige Studie, die explizit realistische Handelskosten gegen die Bruttoanomalie stellt (BLMT 2001), findet **keine verlaessliche Nettorendite**. Fuer die EPS-Revisionsvariante existiert bessere Post-Publication-Bestaetigung (HXZ 2020), aber keine ebenso direkte Kostenwiderlegung *oder* Kostenbestaetigung — die Evidenzluecke bleibt offen, weshalb hier konservativ WEAK statt CANDIDATE vergeben wird. Kurszielrevisionen faellt mangels eigenstaendiger, unabhaengig replizierter Evidenz und wegen dokumentierten Levels-Bias durch.

**Fuer ein institutionelles Mandat bedeutet das:** Falls diese Klasse ueberhaupt eingesetzt wird, dann nur (1) als Overlay/Tie-Breaker innerhalb eines ohnehin gehandelten Momentum-/Quality-Faktors (um marginale Turnover-Kosten zu vermeiden, da das Buch bereits gehandelt wird), nicht als eigenstaendige Strategie mit eigenem Turnover-Budget; (2) mit reduzierter Rebalancing-Frequenz (monatlich statt taeglich) und Signal-Buffering, wohl wissend, dass das gemaess BLMT einen Grossteil der Bruttorendite kostet; (3) mit Fokus auf die EPS-Revisionsvariante (bessere Post-Publication-Bestaetigung) statt auf diskrete Empfehlungsstufen oder Kursziele.

## Quellen (Web-Recherche Juli 2026)

- [Does Academic Research Destroy Stock Return Predictability? (McLean & Pontiff 2016)](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365)
- [A Taxonomy of Anomalies and Their Trading Costs (Novy-Marx & Velikov)](https://academic.oup.com/rfs/article-abstract/29/1/104/1844518)
- [Open Source Asset Pricing (Chen & Zimmermann)](https://www.openassetpricing.com/)
- [Analyzing the Analysts: When Do Recommendations Add Value? (Jegadeesh, Kim, Krische, Lee 2004)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2004.00657.x)
- [Do Brokerage Analysts' Recommendations Have Investment Value? (Womack 1996)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1996.tb05205.x)
- [Can Investors Profit from the Prophets? (Barber, Lehavy, McNichols, Trueman 2001)](https://onlinelibrary.wiley.com/doi/abs/10.1111/0022-1082.00336)
- [Replicating Anomalies (Hou, Xue, Zhang 2020)](https://academic.oup.com/rfs/article-abstract/33/5/2019/5236964)
- [Discrete Expectational Data and Portfolio Performance (Elton, Gruber, Grossman 1986)](https://www.jstor.org/stable/2328502)
- [An Empirical Analysis of Analysts' Target Prices (Brav & Lehavy 2003)](https://onlinelibrary.wiley.com/doi/10.1111/1540-6261.00593)
- [Analyst Forecast Revisions and Market Price Discovery (Gleason & Lee 2003)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=370425)
- [Is Herding Spurious or Intentional? Evidence from Analyst Recommendation Revisions and Sentiment](https://www.sciencedirect.com/science/article/abs/pii/S1057521920301836)
