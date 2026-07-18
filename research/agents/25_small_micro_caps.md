```yaml
agent: 25
klasse: "Small Caps & Micro Caps"
websuche_verfuegbar: ja
strategien:
  - name: "Rohe Size-Praemie (SMB unkonditioniert, Small-minus-Big long/short oder long-only Small-Cap-Tilt)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 1
      regimestabilitaet: 1
      handelbarkeit: 3
      kapazitaet: 4
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.08
    netto_sharpe_erwartung: "0.0-0.05 (statistisch nicht von Null unterscheidbar seit 1982)"
    kernrisiko: "Kein dokumentierter Netto-Alpha nach 1981; Praemie ist Artefakt aus Delisting-/Survivorship-Bias und Januar-Saisonalitaet; prozyklisches Tail-Risiko (Rezession, Zinsanstieg, Liquiditaetskrisen); letztes Jahrzehnt (2010-2024) klar negativ (-3.6%/Jahr ggue. Large Caps)"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Data Library: 'Portfolios Formed on Size' (SMB-Faktor, Size-Dezile Lo10/Hi10)"

  - name: "Size + Quality/Junk-Kontrolle (Asness, Frazzini, Israel, Moskowitz, Pedersen 2018 - 'Size Matters, If You Control Your Junk')"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 3
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.40
    netto_sharpe_erwartung: "0.15-0.30 brutto (kleine, institutionell nicht relevante Kapazitaet); netto nach Leihgebuehren/Spreads auf der Short-Junk-Seite realistisch 0.0-0.15 bei jeder nennenswerten Kapitalgroesse"
    kernrisiko: "Short-Bein (junge/junky Microcaps) ist teuer und schwer leihbar; Crowded-Short-Squeeze-Risiko (Meme-Stock-Analogon Jan. 2021); QMJ-Faktor selbst in tiefster Drawdown-Phase seit 20 Jahren (2021-2025); Autoren sind AQR-Mitarbeiter mit kommerziellem QMJ/SMB-Produktinteresse (Promotion-Bias); Konstrukt 'Quality' hat viele Freiheitsgrade (Profitabilitaet/Safety/Payout/Growth-Definitionen), Data-Mining-Risiko"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "AQR 'Quality Minus Junk: Factors, Monthly' Datensatz + Ken French Size/Profitability doppelt sortierte Portfolios (Proxy)"

  - name: "Mikrocap-Illiquiditaetspraemie / praktische Umsetzung mit Geduld+Qualitaet+Liquiditaetsfilter (DFA/Avantis-Stil)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.30
    netto_sharpe_erwartung: "0.10-0.20, primaer Exekutions-/Geduld-Alpha statt reiner systematischer Faktor-Praemie"
    kernrisiko: "Akademische Illiquiditaetspraemie seit Mitte-1980er statistisch nicht mehr von Null unterscheidbar (Ben-Rephael/Kadan/Wohl 2015); beobachtete Outperformance einzelner Live-Fonds (DFA) wahrscheinlich Exekutions-/Zugangs-Alpha (Nischen-Infrastruktur, Geduld, Blockhandel-Netzwerk), schwer replizierbar; Gesamtkapazitaet der Anlageklasse extrem klein (aggregiertes taegliches Dollarvolumen aller US-Microcaps in der Groessenordnung von wenigen hundert Mio. USD)"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Size-Dezile (Lo10/'Micro') als Proxy; echte Amihud-ILLIQ-Reihen erfordern CRSP (kostenpflichtig); ersatzweise oeffentliche Kursreihen DFSCX/IWC/AVUV"
```

# Agent 25 — Small Caps & Micro Caps: Size-Praemie, Size+Quality, Mikrocap-Illiquiditaet

## 0. Executive Summary

Die Nullhypothese haelt sich ueberraschend gut. Die **rohe Size-Praemie ist tot** — nicht "schwach", sondern seit ca. 1982 im gepoolten US-Datensatz von Null statistisch nicht mehr unterscheidbar, konzentriert in einem einzigen Kalendermonat (Januar) und in ihrer historischen Form zu einem erheblichen Teil ein Artefakt von Delisting-Bias in CRSP. Die einzige akademisch ernstzunehmende Rettungslinie — **"Size Matters, If You Control Your Junk"** (Asness, Frazzini, Israel, Moskowitz, Pedersen, *Journal of Financial Economics* 2018) — repariert das In-Sample-Bild beeindruckend (Alpha-Vervielfachung, t-Statistiken um ~4), scheitert aber an drei Dingen, die fuer einen institutionellen Fonds zaehlen: (1) das Alpha sitzt fast vollstaendig im Short-Bein aus "junky" Microcaps, die teuer und teilweise gar nicht leihbar sind; (2) die investierbare Kapazitaet der gesamten Microcap-Anlageklasse ist so klein, dass ein einzelner institutioneller Fonds mit einigen hundert Millionen bis niedrigem einstelligem Milliardenbetrag bereits "der Markt" wird; (3) der Qualitaetsfaktor selbst, auf dem die Rettung beruht, befindet sich seit 2021 in der schlimmsten Drawdown-Phase seit 20 Jahren — ausgerechnet im Post-Publication-Fenster, das als Out-of-Sample-Test dienen sollte. Eine dritte Variante — die praktische Umsetzung ueber Geduld, Liquiditaets- und Qualitaetsfilter (DFA-/Avantis-Stil) — zeigt zumindest einen 40+-jaehrigen Live-Track-Record mit leicht positivem Netto-Alpha, aber die Fachliteratur zur Illiquiditaetspraemie selbst zeigt, dass genau dieser Kanal seit Mitte der 1980er Jahre statistisch verschwunden ist; was uebrig bleibt, ist wahrscheinlich Exekutions- und Zugangs-Alpha eines einzelnen Managers, keine systematisch replizierbare Marktineffizienz.

Fazit: **keine der drei Kandidaten erreicht die CANDIDATE-Schwelle**. Zwei WEAK, ein KILL. Diese Anomalieklasse ist fuer ein institutionelles Mandat mit nennenswerter Kapitalallokation im Wesentlichen nicht bespielbar — nicht weil die Ineffizienz zwingend inexistent waere, sondern weil Kapazitaet und Kosten jede realistische Implementierung auf ein Sharpe-Niveau druecken, das die Opportunitaetskosten des Research- und Handelsaufwands kaum rechtfertigt.

## 1. Mandat, Datenlage und Methodik

- Isolationsvorgabe eingehalten: keine Dateien unter `/home/user/Bot/research/` gelesen; ausschliesslich externe Web-Recherche und internes Modellwissen verwendet.
- `websuche_verfuegbar: ja` — WebSearch/WebFetch funktionierten fuer die meisten Anfragen; einige Primaerquellen (SSRN-PDF, Alpha Architect, Morningstar-Detailartikel) waren per WebFetch nicht zugaenglich (403/Encoding-Probleme). In diesen Faellen wurde auf Sekundaerquellen (Suchmaschinen-Snippets, Zitationen in anderen Papers) zurueckgegriffen und dies im Text explizit als "gemaess Sekundaerliteratur" markiert. Exakte Originalzahlen aus Banz (1981) konnten nicht direkt aus dem Primaertext verifiziert werden; die zitierten Groessenordnungen stammen aus konsistent wiederholten Sekundaerzitaten und meinem Vorwissen (Stand Anfang 2026) — entsprechend gekennzeichnet.
- Haltung: adversarial. Jede vermeintliche Rettung der Size-Praemie wird primaer danach gefragt, ob sie (a) Out-of-Sample seit ihrer Publikation haelt und (b) nach realistischen Microcap-Handelskosten ueberlebt.

## 2. Kandidat 1: Rohe Size-Praemie (SMB unkonditioniert)

### a) Oekonomische Begruendung; wer ist die Gegenseite?

Die klassische Erklaerung (Banz 1981, Fama/French 1992/1993) ist eine Risikopraemie: kleine Firmen haben hoehere Konkurs-/Distress-Risiken, schlechtere Informationslage (geringere Analysten-Coverage), hoehere Kapitalkosten und muessen deshalb hoehere erwartete Renditen bieten, um Kapital anzuziehen. Alternative Erklaerungen sind Liquiditaetsrisiko (kleine Firmen sind illiquider, Amihud/Mendelson 1986) und schlicht CAPM-Fehlspezifikation (Small Caps haben Betas, die das CAPM systematisch unterschaetzt).

Gegenseite/Warum bleibt sie ungehandelt: institutionelle Anleger (Pensionskassen, Versicherer, grosse Mutual Funds) meiden Small/Micro Caps aus Prudent-Man-Erwaegungen, Index-Constraints, Liquiditaetsanforderungen und schlicht weil die Positionsgroessen, die sie brauchen, den Markt bewegen wuerden. Analysten-Coverage ist duenn bis nicht vorhanden. Das ist die klassische "neglected firm"-Erzaehlung (Arbel/Strebel 1983) — aber sie erklaert genauso gut, warum eine etwaige Ineffizienz *nicht* arbitriert wird wie warum sie ueberhaupt bestehen sollte.

### b) Limits to Arbitrage: Erklaerung oder Problem?

Beides — und das ist der Kern der Adversarial-Pruefung. Wenn die Kapazitaetsbeschraenkung die *Erklaerung* fuer eine fortbestehende Ineffizienz waere, muesste die Praemie fuer denjenigen, der sie doch handeln kann (sehr kleines Kapital, lange Haltefristen, keine Skalierungszwaenge), robust nachweisbar sein. Das ist nach 1981 gerade *nicht* der Fall (siehe d). Die Kapazitaetsbeschraenkung erklaert also nicht das Fortbestehen einer echten Praemie, sondern schlicht, warum ein Nullresultat (oder ein sehr kleines, verrauschtes Resultat) in aggregierten Indizes ueberlebt, ohne durch Arbitrage wegkonkurriert zu werden — es gibt naemlich nichts Substanzielles wegzukonkurrieren. Fuer ein institutionelles Mandat ist die Kapazitaetsfrage in jedem Fall das **Problem**, nicht die Chance: selbst wenn ein Restsignal existiert, ist es nicht in institutioneller Groessenordnung realisierbar (quantifiziert unter f).

### c) Originalstudien

**Banz (1981)**, *The Relationship Between Return and Market Value of Common Stocks*, JFE 9: NYSE-Stichprobe, Kernperiode ca. 1936-1975 (Gesamtfenster bis 1926 fuer Teilanalysen). Befund: risikoadjustierte (CAPM-)Ueberrenditen kleiner Firmen gegenueber grossen, wobei der Effekt stark nichtlinear ist — er konzentriert sich fast vollstaendig in den kleinsten ~20% (kleinstes Quintil), waehrend zwischen mittleren und grossen Firmen kaum ein Unterschied besteht. Groessenordnung gemaess durchgaengig zitierter Sekundaerliteratur: abnormale Renditen des kleinsten Quintils in der Groessenordnung von grob 0,3-0,4%/Monat gegenueber CAPM-Vorhersage (nicht aus Primaertext verifizierbar, hier als Literaturkonsens gekennzeichnet). Banz selbst warnte bereits im Original, dass unklar sei, ob "size" ein eigener Risikofaktor oder Proxy fuer etwas anderes (Illiquiditaet, fehlende Coverage) ist — die Ambiguitaet ist also von Anfang an eingebaut.

**Asness, Frazzini, Israel, Moskowitz, Pedersen (2018)**, *Size Matters, If You Control Your Junk*, JFE 129(3): 479-509. Stichprobe: US-Aktien (NYSE/AMEX/NASDAQ, ueberwiegend 1957-2016) sowie 24 internationale Aequitymaerkte und 30 Industrien. Kernresultat: rohes SMB hat ein "weak historical record" und ist nach den ueblichen sieben Einwaenden (siehe unten) kaum robust. Nach Kontrolle fuer Qualitaet/Junk (QMJ-Score aus Profitabilitaet, Wachstum, Sicherheit, Payout) springt das SMB-Alpha deutlich: bei Profitabilitaets-Kontrolle auf **42 Basispunkte/Monat, ca. 4 Standardfehler von Null entfernt**; bei Safety- bzw. Payout-Kontrolle auf **35 bzw. 44 Basispunkte/Monat** mit aehnlicher Signifikanz; bei Growth-Kontrolle nur **20 Basispunkte/Monat, nur marginal signifikant** (schwaechste der vier Spezifikationen). Die Autoren zeigen den Effekt zusaetzlich robust in 30 Industrien und 24 internationalen Maerkten und behaupten Vergleichbarkeit mit Value/Momentum in oekonomischer Groessenordnung.

Kritischer Kommentar zur Robustheit: "Quality" ist ein mehrdimensionales Konstrukt (Profitabilitaet, Wachstum, Sicherheit, Payout — vier verschiedene, teils schwach korrelierte Definitionen mit sehr unterschiedlicher Signifikanz: 44 vs. 20 Basispunkte). Das ist ein klassisches Data-Mining-Warnsignal: bei vier Freiheitsgraden in der Konstruktion des Kontrollfaktors ist es beinahe garantiert, dass mindestens eine Spezifikation "funktioniert". Zudem sind alle fuenf Autoren AQR-Mitarbeiter (bzw. AQR-affiliiert), und AQR vertreibt kommerzielle QMJ- und Size-bezogene Produkte — ein struktureller Promotion-Bias, der bei der Bewertung der Ergebnisse mitgedacht werden muss.

### d) Out-of-Sample-/Post-Publication-Evidenz

Dies ist der entscheidende Abschnitt fuer die Nullhypothese.

- **Schwert (2003)**, *Anomalies and Market Efficiency* (NBER WP 9277): Zeigt, dass der Size-Effekt (ebenso Value, Weekend- und Dividend-Yield-Effekt) nach der akademischen Publikation systematisch schwaecher wurde oder verschwand. Der **Wendepunkt liegt am Beginn der 1980er Jahre** — praktisch zeitgleich mit Banz' Publikation. Seither ist die relative Performance von Small vs. Large im Durchschnitt deutlich kleiner, teils sogar negativ.
- **Keim (1983)**, *Size-Related Anomalies and Stock Return Seasonality*, JFE 12: fast **50% der durchschnittlichen Groesse des "Size-Effekts" 1963-1979 entfaellt auf den Januar allein**, ca. **25% auf die ersten fuenf Handelstage des Januar**. In den uebrigen elf Monaten ist praktisch kein Size-Effekt nachweisbar. Das ist verheerend fuer die Risikopraemien-Erzaehlung (ein Risikofaktor sollte nicht kalenderabhaengig sein) und stuetzt stattdessen mechanische Erklaerungen (Steuerverlust-Verkaeufe im Dezember, "Window Dressing").
- **Shumway/Warther (1999)**, *The Delisting Bias in CRSP's Nasdaq Data*: fehlende/verzerrte Delisting-Returns in CRSP fuehren zu einem substanziellen Aufwaertsbias fuer Small-Cap-Renditen. Korrektur der negativen Delisting-Returns **eliminiert den Size-Effekt vollstaendig bei NASDAQ-Titeln** (bei NYSE/AMEX bleibt ein Rest, aber deutlich reduziert).
- **Fama/French (2008)**, *Dissecting Anomalies*, und **Hou/Xue/Zhang (2020)**, *Replicating Anomalies* (Review of Financial Studies 33): beide Arbeiten zeigen systematisch, dass ein grosser Teil der in der Literatur dokumentierten Anomalien primaer in Microcaps lebt und bei Verwendung von wertgewichteten Portfolios bzw. NYSE-Breakpoints (statt gepoolter NYSE-AMEX-NASDAQ-Breakpoints, die von winzigen NASDAQ-Microcaps dominiert werden) drastisch schrumpft oder ganz verschwindet. Das ist ein methodischer Kritikpunkt, der praktisch die gesamte Small-Cap-Anomalie-Literatur betrifft: ein erheblicher Teil "funktioniert" nur, weil Tausende praktisch untradebarer Nanocap-Titel mit Gleichgewichtung mitgezaehlt werden.
- **Internationale Evidenz**: von den Asness-et-al.-Autoren selbst als einer von sieben Haupteinwaenden gegen die rohe Size-Praemie benannt — "is weak internationally". Erst nach Junk-Kontrolle wird ein internationaler Effekt behauptet (siehe Kandidat 2); ohne Kontrolle gilt: international praktisch kein robuster Size-Effekt.
- **Aktuelle Dekade (2010-2024)**: Over the decade through April 2024 lieferten Large Caps eine kumulierte Mehrrendite von rund **113% gegenueber Small Caps, entsprechend ca. 3,6% p.a.** (S&P 500 ca. 13,5% p.a. vs. Russell 2000 ca. 9,5% p.a.). In den letzten zehn Jahren gab es nur **zwei Kalenderjahre (2016 und 2020)**, in denen Small Caps Large Caps in den USA outperformten. Ein Teil (ca. 1,4 Prozentpunkte p.a.) ist auf die extreme "Magnificent Seven"-Konzentration in Large Caps zurueckzufuehren, aber selbst bereinigt bleibt eine klare Unterperformance von Small Caps.
- **Strukturelle Verschiebung**: ca. **45% der Russell-2000-Konstituenten weisen negative Ertraege aus** (unprofitabel) — ein historisch hoher und steigender Anteil, was die Grundthese von Asness et al. (dass "Junk" die rohe Size-Praemie kontaminiert) empirisch untermauert, aber auch zeigt, dass der Anteil an handelbarem "Nicht-Junk" innerhalb Small Caps strukturell schrumpft (Rueckgang der Boersennotierungen, laengeres Verbleiben im Private-Equity-/VC-Bereich vor IPO — Selektionseffekt: die heute oeffentlichen Small Caps sind im Schnitt qualitativ schwaecher als die Small Caps der Banz-Aera).

**Decay-Schaetzung**: von einer in-sample (vor-1982) Praemie in der Groessenordnung von geschaetzt 4-19% p.a. (grobe Literaturangaben, nicht primaerverifiziert) auf eine seit 1982 im gepoolten Datensatz nicht signifikant von Null verschiedene, im letzten Jahrzehnt klar negative Praemie (-3,6% p.a. relativ zu Large Caps 2010-2024) — das entspricht einem **Decay von schaetzungsweise 90-100%**, je nach genauer Referenzperiode sogar Vorzeichenumkehr.

### e) Kosten: Microcap-Spreads und Market Impact

Microcap-Spreads liegen gemaess Branchenanalysen (Factor-Investor/OSAM-Research) haeufig im Bereich von **2-10% des Aktienkurses oder mehr** bei illiquiden Titeln, gegenueber Ein-Cent-Spreads (faktisch Tick-Groesse) bei liquiden Large Caps. Fuer einen hypothetischen 10-Mio.-USD-Trade wird der Implementierungs-Kostenanstieg von **~5 Basispunkten bei den liquidesten Titeln auf bis zu ~220 Basispunkte bei den illiquidesten** beziffert (44-facher Anstieg). Diese Kosten fressen jede rohe Size-Praemie, die ohnehin nicht mehr signifikant von Null verschieden ist, vollstaendig auf.

### f) Kapazitaet und Handelbarkeit

Aggregiertes taegliches Dollarvolumen: Large-Cap-Dollarvolumen ist ca. **245-fach**, Small-Cap-Dollarvolumen ca. **43-fach** groesser als das der Microcaps (Branchenschaetzung, inflationsbereinigt ueber 20 Jahre, aggregiertes Microcap-Tagesvolumen in der Groessenordnung von **~420 Mio. USD** ueber das gesamte Microcap-Segment). Ein Microcap-Fonds "wird zum Markt", sobald er in die Groessenordnung von **~5 Mrd. USD AUM** kommt — de facto weit darunter, da bereits deutlich kleinere Positionsgroessen Preis-Impact erzeugen. Fuer eine breite, liquide, long-only Small-Cap-Indexumsetzung (z.B. Russell-2000-Tracker) ist die Kapazitaet dagegen hoch — aber genau dort ist kein belastbares Alpha vorhanden.

### g) Regimeabhaengigkeit und Tail-Risiko

Small/Micro Caps sind strukturell prozyklisch und zinssensitiv: hoehere durchschnittliche Verschuldung (variable Zinsen, kuerzere Laufzeiten), hoehere Distress-Wahrscheinlichkeit, staerkere Betroffenheit von Kreditverknappung. In Liquiditaetskrisen (2008, Maerz 2020) und in Zinsanstiegszyklen (2022-2023) leiden sie ueberproportional. Der Zusammenhang mit Rezessionen ist ebenfalls asymmetrisch: gerade in Abschwuengen, wenn Diversifikation am wichtigsten waere, korrelieren Small Caps staerker mit dem allgemeinen Marktrisiko (steigende Betas, "Distress-Beta"), liefern also keinen verlaesslichen Diversifikationsnutzen, sondern eher Tail-Risiko-Verstaerkung.

### h) Bekannte Kritik/Widerlegungen

Bereits vollstaendig oben eingearbeitet: Delisting-/Survivorship-Bias (Shumway/Warther 1999), Januar-Konzentration (Keim 1983), Verschwinden nach Publikation (Schwert 2003), Microcap-/Equal-Weighting-Artefakt (Fama/French 2008; Hou/Xue/Zhang 2020), Schwaeche international (von Asness et al. selbst eingeraeumt vor Junk-Kontrolle).

**Urteil: KILL.** Die rohe Size-Praemie ist das Lehrbuchbeispiel einer Anomalie, die nach Publikation verschwindet. Reproduzierbar ist lediglich das Nullresultat.

## 3. Kandidat 2: Size + Quality/Junk-Kontrolle (Asness et al. 2018)

### a) Oekonomische Begruendung; wer ist die Gegenseite?

Die These: die rohe Size-Praemie ist nicht per se falsch, sondern wird durch eine Untermenge kleiner, "junky" (unprofitabler, hochverschuldeter, wachstumsschwacher, ausschuettungsschwacher) Firmen verwaesert bzw. dominiert, die im Aggregat schlecht performen und hohe Varianz haben. Bereinigt man um diese Untermenge (bzw. kontrolliert man dafuer im Regressionssinn), zeigt sich ein saubereres, stabileres Size-Signal. Oekonomisch waere das konsistent mit einer Kombination aus Distress-Risikopraemie (fuer die verbleibenden soliden Small Caps) und einer Verhaltensanomalie auf der Gegenseite: Anleger mit "Lottery Preference" (Kumar 2009) und spekulative Retail-Investoren kaufen bevorzugt genau die junky, hochvolatilen Microcaps mit Lotterie-Charakter (hohe Skewness, kleine Wahrscheinlichkeit eines Vielfachen), was deren Bewertung ueberhoeht und ihre erwartete Rendite senkt/negativ macht — was wiederum die durchschnittliche rohe Size-Praemie nach unten zieht, obwohl die "guten" Small Caps weiterhin eine positive Praemie tragen.

Gegenseite: Retail-Spekulanten und "closet indexer"-Fonds, die aus Benchmark-Zwang (Russell-2000-Tracking) auch Junk-Microcaps halten muessen, sowie Wachstums-/Momentum-orientierte Anleger, die in Boomphasen (siehe 2020/21 Meme-Stock-/SPAC-Episode) gezielt unprofitable, hoch geshortete Small Caps kaufen.

### b) Limits to Arbitrage: Erklaerung oder Problem?

Hier zeigt sich das Problem besonders scharf, weil die Strategie strukturell **long-short** ist (lang gute, kurz schlechte kleine Firmen) und das Alpha ueberproportional aus dem **Short-Bein** stammt. Genau die Junk-Microcaps, die geshortet werden muessten, sind (a) am teuersten zu leihen (hohe Borrow-Fees, teils "hard to borrow" bzw. gar nicht verfuegbar), (b) am staerksten von Short-Squeeze-Risiko betroffen, und (c) am illiquidesten im Handel. Die Limits-to-Arbitrage-Erklaerung ist hier also **beides gleichzeitig**: Sie erklaert plausibel, warum ein reales Signal unarbitriert bleiben koennte (kein Marktteilnehmer kann es günstig genug shorten) — gleichzeitig ist genau das der Grund, warum ein institutioneller Fonds es nicht profitabel handeln kann. Der GameStop-/Meme-Stock-Schock vom Januar 2021 ist ein reales Stresstest-Beispiel: exakt das Segment "klein, unprofitabel, hoch geshortet", das eine QMJ-in-Smallcaps-Strategie strukturell short haelt, wurde binnen Tagen um mehrere hundert Prozent nach oben gezwungen — ein konkretes, nicht-hypothetisches Tail-Risiko fuer diese Strategieklasse.

### c) Originalstudien (siehe auch Abschnitt 2c fuer Details zu Asness et al. 2018)

Kernzahlen wiederholt: SMB-Alpha nach Profitabilitaets-Kontrolle **42 Bp/Monat, ~4 Standardfehler**; Safety **35 Bp**; Payout **44 Bp**; Growth nur **20 Bp, marginal signifikant**. Robustheit ueber 30 Industrien und 24 internationale Maerkte behauptet. Verwandte Arbeit: **Fitzgibbons/Friedman/Pomorski/Serban** bzw. **Asness/Israel/Moskowitz** *"Fact, Fiction, and the Size Effect"* (Journal of Portfolio Management, ca. 2018) bestaetigt aehnliche Befunde und betont, dass Kontrolle fuer Qualitaet "einen groesseren Size-Effekt in fast zwei Dutzend internationalen Aequitymaerkten aufdeckt, wo Size sonst notorisch schwach war".

### d) Out-of-Sample-/Post-Publication-Evidenz (2018-2026)

Dies ist das eigentliche Nadeloehr fuer das Urteil.

- **Small Caps allgemein 2019-2024**: gemaess Branchenresearch (Acadian) waren Small-Cap-Renditen in den meisten Regionen 2019-2023 niedriger als Large-Cap-Renditen (Ausnahme Emerging Markets). Das absolute Sharpe-Ratio von Small Caps blieb aber ueberraschend stabil: Russell-2000-Sharpe **0,38** ueber die Dekade April 2014-April 2024, gegenueber **0,40** in der "Hochphase" Sept. 1998-Aug. 2008 und **0,39** seit 1995 sowie **0,41** ueber ein fast einhundertjaehriges Sample fuer das unterste Marktkapitalisierungs-Drittel. Sprich: Small Caps sind nicht "kaputter" geworden in absoluten risikoadjustierten Terms — sie wurden nur relativ zu Large Caps schlechter, weil Large-Cap-Sharpe durch die Mega-Cap-/"Magnificent-Seven"-Konzentration um rund 30% ueber den historischen Schnitt gestiegen ist. Das ist ein wichtiges Differenzierungsargument: es spricht eher fuer einen Grossunternehmens-Konzentrationseffekt als fuer einen Zusammenbruch der Small-Cap-Fundamentaldaten.
- **Qualitaetsfilter wirkt teilweise, aber die Evidenz ist gemischt**: gemaess MSCI-Research haben Small Caps **"excluding those with the highest short interest and lowest quality"** seit 2007 "matched or outperformed" Large Caps — eine direkte Teilbestaetigung des Asness-Mechanismus. Gleichzeitig zeigt Acadian, dass "Quality" und "Short Interest" ueber die letzten 25 Jahre insgesamt die **groessten negativen Renditebeitraege** innerhalb der Small-Cap-Faktorattribution waren (waehrend "Size" und "Value" positive Treiber waren) — was fuer den Long-Junk/Short-Quality-Interpretationswechsel je nach Betrachtungsfenster unterschiedlich ausfaellt und methodisch nicht saubere, konsistente Bestaetigung liefert.
- **Der Qualitaetsfaktor selbst ist seit 2021 strukturell schwach** — und das ist der schaerfste Einwand: gemaess mehreren 2025/2026-Branchenanalysen (CFA Institute, Davy, Aberdeen) durchlebt "Quality" **eine der schwierigsten Perioden seit Jahrzehnten**, mit Unterperformance gegenueber dem Gesamtmarkt seit 2021 und dem **groessten Drawdown seit 20 Jahren im Jahr 2025** (>10% relative Unterperformance vor teilweiser Erholung). Ursachen: Zinsanstieg traf "long-duration"-Qualitaetstitel besonders hart (hohe Bewertungs-Multiples auf stabile, weit in der Zukunft liegende Cashflows), und die extrem lockere Geldpolitik 2020/21 befeuerte spekulatives Verhalten in genau den Junk-Titeln, die eine QMJ-Strategie shorten wuerde (Meme-Stocks, SPACs, unprofitable Wachstumstitel). Da Kandidat 2 strukturell auf einer funktionierenden Qualitaetspraemie aufbaut, ist eine Kernkomponente der Strategie im Post-Publication-Fenster selbst unter Druck geraten — ein sehr ungünstiges Timing fuer einen sauberen Out-of-Sample-Beweis.
- **Fazit OOS**: Es gibt **keine saubere, unabhaengig dokumentierte Sharpe-Ratio-Reihe** einer live gehandelten "Size+Junk-kontrolliert"-Strategie seit 2018, die eindeutig ein robustes positives Netto-Alpha nachweist. Die verfuegbare Evidenz ist bestenfalls gemischt: Teilbestaetigung des Mechanismus (MSCI), aber auch strukturelle Gegenwinde (Quality-Crash 2021-2025, generelle Small-Cap-Schwaeche, Meme-Stock-Tail-Event).

### e) Kosten

Die Long-Seite (hochqualitative, gesunde Small Caps) ist moderat handelbar mit Spreads im mittleren einstelligen Prozentbereich. Die Short-Seite (Junk-Microcaps) ist das Kostenproblem: hohe Borrow-Fees (oft mehrere Prozent p.a., in Spitzenzeiten zweistellig), begrenzte Leihbarkeit, hohe Spreads (2-10%+ wie unter Kandidat 1). Realistisch duerften Leih- und Handelskosten einen erheblichen Teil der gemeldeten 35-44 Bp/Monat Brutto-Alpha auffressen — eine seriöse Schaetzung ohne eigene Live-Track-Record-Daten liegt bei **50-80% Kostenerosion** bei institutioneller Ausfuehrungsgroesse.

### f) Kapazitaet und Handelbarkeit

Da die Strategie sowohl long als auch short im Microcap-Segment agiert (schlechteste Liquiditaet auf beiden Seiten, insbesondere short), ist die Kapazitaet noch enger als bei einer reinen Long-only-Umsetzung. Realistisch schaetzbare institutionelle Kapazitaetsgrenze: **niedriger einstelliger Milliardenbereich brutto (long+short kombiniert), praktisch eher deutlich darunter (100 Mio. bis wenige hundert Mio. USD)** fuer eine Umsetzung ohne signifikanten Alpha-Verlust durch Market Impact. Zum Vergleich: ein einzelner grosser Hedgefonds-Sleeve haette diese Strategie in wenigen Handelstagen "gesaettigt".

### g) Regimeabhaengigkeit und Tail-Risiko

Doppelt regimeabhaengig: (1) vom Small-vs-Large-Zyklus (Zinsen, Risikoappetit) und (2) vom Quality-vs-Junk-Zyklus (Liquiditaetsregime — in extrem lockeren Geldpolitikphasen rallyen Junk-Titel ueberproportional, siehe 2020/21). Zusaetzliches, sehr reales Tail-Risiko: Crowded-Short-Squeeze in genau dem Segment, das strukturell geshortet wird (GameStop Januar 2021 als Fallbeispiel — kein hypothetisches Szenario, sondern ein tatsaechlich eingetretenes Ereignis, das viele quantitative Long-Short-Small-Cap-Strategien im Januar 2021 zweistellige Prozent-Drawdowns kostete).

### h) Bekannte Kritik/Widerlegungen

- Data-Mining-Risiko durch Mehrdimensionalitaet des Qualitaetskonstrukts (vier verschiedene Definitionen mit stark unterschiedlicher Signifikanz: 20 bis 44 Bp).
- Autoren-Interessenkonflikt: AQR-Autorenschaft, kommerzielles QMJ-/Size-Produktinteresse.
- Der urspruengliche 7-Punkte-Einwandkatalog der Autoren selbst (schwacher historischer Track Record, Konzentration in Microcaps, Januar-Dominanz, Abwesenheit bei Nicht-Preis-basierten Size-Massen, internationale Schwaeche, Subsumption unter Illiquiditaets-Proxy) wird zwar von den Autoren als "widerlegt" dargestellt, ist aber im Kern eine Selbstbewertung derselben Autorengruppe, die die Rettungsstrategie entwickelt — unabhaengige Replikation durch nicht-AQR-affiliierte Forscher ist duenner gesaet, als der Publikationserfolg suggeriert.

**Urteil: WEAK.** Der Mechanismus ist oekonomisch plausibel und die In-Sample-Statistik beeindruckend, aber es fehlt die vom Auftrag geforderte Kombination aus dokumentierter Post-Publication-Evidenz UND Kostenrobustheit. Beides ist bestenfalls gemischt/unklar. Naeher an CANDIDATE als Kandidat 1, aber nicht dort.

## 4. Kandidat 3: Mikrocap-Illiquiditaetspraemie / praktische Umsetzung (DFA-/Avantis-Stil)

### a) Oekonomische Begruendung; wer ist die Gegenseite?

Amihud/Mendelson (1986)-Logik: illiquide Aktien muessen eine hoehere erwartete Rendite bieten, um Investoren fuer hoehere Transaktionskosten und Liquidationsrisiko zu kompensieren. Praktische Umsetzung (DFA seit 1981, spaeter Avantis/AQR) versucht, diese Praemie nicht durch aggressives Traden, sondern durch **Geduld** (limitierte Orders, Blockhandel-Netzwerke, Bereitschaft, Tage/Wochen auf Gegenparteien zu warten) sowie durch Qualitaets- und Profitabilitaets-Screens zu vereinnahmen, statt sie durch eigene Marktimpact-Kosten wieder zu verlieren. Gegenseite: Verkaeufer, die aus Liquiditaetsnot (Fondsredemptions, Indexrekonstitutionen, Nachlassabwicklungen) zu ungünstigen Preisen verkaufen muessen und keine Geduld haben.

### b) Limits to Arbitrage: Erklaerung oder Problem?

Auch hier beides. Die Praemie kann nur von Kapital vereinnahmt werden, das selbst illiquide sein darf (lange Lock-ups, kein taegliches Redemption-Risiko) — genau das ist bei den meisten institutionellen Mandaten (taegliche/monatliche Liquiditaet, Sharpe-Ratio-getriebene Performance-Reviews) nicht gegeben. Wer die Geduld hat, kann theoretisch die Praemie einsammeln; wer sie braucht, kann es strukturell nicht. Fuer ein Hedgefonds-Mandat mit ueblichen Liquiditaetsanforderungen ist dies erneut in erster Linie ein **Kapazitaets- und Strukturproblem**, keine ausnutzbare Opportunitaet.

### c) Empirische Basis / "Originalstudien"

Kein einzelnes Ursprungspapier wie bei Kandidat 1/2; die relevante akademische Linie ist Amihud (2002) *"Illiquidity and Stock Returns"* und Amihud/Hameed/Kang/Zhang (2015) *"The Illiquidity Premium: International Evidence"*. Als praktischer Beleg dient der **Live-Track-Record des DFA US Micro Cap Portfolio (DFSCX)**, aufgelegt 1981 (also praktisch zeitgleich mit Banz' Publikation) — mit gemaess Dimensional-eigenen Angaben **+1,5% p.a. Netto-Outperformance gegenueber dem Russell 2000 ueber gut 42 Jahre** (Endwert $1 → ca. $108 vs. ca. $59 im Russell-2000-Tracker). Das ist die einzige in dieser Untersuchung gefundene, wirklich langfristige, netto-of-fee dokumentierte positive Zahl in der gesamten Small/Micro-Cap-Klasse.

Wichtige Einschraenkung, da es sich um eine Herstellerangabe (Dimensional selbst) handelt, nicht um unabhaengige akademische Verifikation: nach Rolling-Perioden ist das Bild deutlich durchwachsener — DFSCX lag gemaess Fondsdaten in den letzten **1, 5 und 15 Jahren hinter dem Russell 2000** (z.B. 5-Jahres-Rendite 7,50% p.a. vs. 8,23% p.a. Russell 2000), aber **in den letzten 10 und 20 Jahren davor** (12,40% vs. 11,83% resp. 9,31% vs. 7,59% p.a.). Das Netto-Ergebnis ist also stark periodenabhaengig und keineswegs ein gleichmaessig positiver Alpha-Strom.

### d) Out-of-Sample-/Post-Publication-Evidenz

Der zentrale, fuer die Nullhypothese wichtigste Befund stammt aus **Ben-Rephael, Kadan, Wohl (2015)**, *The Diminishing Liquidity Premium*, Journal of Financial and Quantitative Analysis: unter Verwendung von NYSE-Daten ueber vier Jahrzehnte zeigen die Autoren, dass sowohl die Sensitivitaet von Renditen gegenueber Liquiditaetsmassen als auch die Liquiditaetspraemien selbst **seit Mitte der 1980er Jahre drastisch gesunken sind, auf ein Niveau, das statistisch nicht mehr von Null zu unterscheiden ist**. Handelsstrategien, die illiquide Aktien kaufen und liquide leerverkaufen (bzw. umgekehrt gewichten), sind gemaess dieser Studie **"virtually unprofitable"** geworden. Als plausible Erklaerung nennen die Autoren die Verbreitung von Indexfonds/ETFs, die generell Liquiditaet in vormals illiquiden Marktsegmenten erhoeht haben. Das ist eine fast wortgleiche Bestaetigung des allgemeinen Verschwindungs-Musters wie bei der rohen Size-Praemie (Kandidat 1) — nur mit anderem Mechanismus (Liquiditaet statt Groesse als Sortierkriterium).

Damit steht die einzige belastbare positive Live-Zahl (DFA +1,5% p.a. seit 1981) in direktem Spannungsverhaeltnis zur akademischen Literatur, die den zugrunde liegenden Kanal (Illiquiditaetspraemie) als seit Mitte der 1980er verschwunden einordnet. Die plausibelste Aufloesung: DFA's Outperformance ist **weniger eine systematische Faktorpraemie als Exekutions-Alpha** — ein struktureller Vorteil aus 40+ Jahren Blockhandel-Beziehungen, Skaleneffekten in der Orderausfuehrung und einem im Zeitverlauf mehrfach angepassten ("geglätteten") Microcap-Universumsbegriff, der die reinste (und damit kapazitaetsschwaechste) Definition von "Microcap" zugunsten von Handelbarkeit verwaessert. Das ist ein durchaus reales, aber **manager-spezifisches, nicht ohne Weiteres replizierbares** Alpha — kein systematischer Faktor, den ein neu eintretender Fonds ohne vergleichbare Infrastruktur einfach kopieren koennte.

### e) Kosten

Identisch zu Kandidat 1/2 (2-10%+ Spreads, bis zu 220 Bp Market Impact bei 10-Mio.-USD-Trades in den illiquidesten Namen). Der einzige Weg, diese Kosten zu vermeiden, ist genau die "Geduld"-Strategie von DFA — was aber bedeutet, dass die Kosten nicht eliminiert, sondern in Form von Opportunitaetskosten/Tracking-Error gegenueber einem sofort ausgefuehrten Portfolio verschoben werden.

### f) Kapazitaet und Handelbarkeit

Aehnlich eng wie Kandidat 1, mit dem zusaetzlichen Hinweis, dass DFA selbst ueber die Jahrzehnte gezwungen war, die Marktkapitalisierungs-Untergrenze fuer "Micro Cap" mehrfach nach oben anzupassen, um wachsendes AUM unterzubringen — ein impliziter Beleg dafuer, dass die reine Microcap-Kapazitaet frueh erschoepft ist und Kapazitaetserweiterung nur durch Verwaesserung der Definition ("weniger micro") moeglich ist.

### g) Regimeabhaengigkeit und Tail-Risiko

Wie Kandidat 1/2: prozyklisch, zinssensitiv. Zusaetzlich spezifisch fuer Illiquiditaetsstrategien: in Liquiditaetskrisen (2008, Maerz 2020) verschwindet Marktbreite fuer Microcaps am schnellsten und am staerksten (Bid-Ask-Spreads koennen sich vervielfachen, Handelsvolumen kann phasenweise nahe Null gehen) — das ist exakt die Phase, in der ein "geduldiger" Investor am meisten Verluste realisiert, wenn er doch verkaufen muss, und in der ein systematisches Rebalancing gegen den Markt (antizyklisches Kaufen von Illiquiditaet) am schwersten umzusetzen ist.

### h) Bekannte Kritik/Widerlegungen

Ben-Rephael/Kadan/Wohl (2015) als Hauptkritik (siehe d). Zusaetzlich: die urspruengliche Amihud/Mendelson-Illiquiditaetspraemien-Literatur selbst wird kritisiert, weil viele Illiquiditaetsmasse (Amihud-ILLIQ, Bid-Ask-Spread) stark mit Size korrelieren — es ist in der Literatur nicht immer sauber trennbar, ob eine gefundene "Illiquiditaetspraemie" nicht schlicht die Size-Praemie unter anderem Namen ist (was die Asness-et-al.-Kritik ausdruecklich als einen der sieben Einwaende gegen die rohe Size-Praemie nennt: "is subsumed by proxies for illiquidity" bzw. umgekehrt).

**Urteil: WEAK.** Der einzige Silberstreif ist ein 40+-Jahres-Live-Track-Record eines einzelnen, hochspezialisierten Managers — nicht eine robuste, von der akademischen Literatur unabhaengig bestaetigte, systematisch replizierbare Praemie. Die Fachliteratur zum zugrunde liegenden Kanal (Illiquiditaet) spricht explizit von Verschwinden seit Mitte der 1980er Jahre.

## 5. Klassenuebergreifende Synthese: Kapazitaet als das eigentliche Kernproblem

Alle drei Kandidaten teilen ein gemeinsames strukturelles Problem, das wichtiger ist als jede einzelne Signifikanzfrage: **selbst im guenstigsten Fall (Kandidat 2, mit dokumentiertem In-Sample-t-Stat ~4) ist die maximal moegliche institutionelle Kapitalallokation so klein**, dass sie fuer einen Fonds mit relevanter verwaltbarer Grosse (typischerweise >100 Mio. USD Sleeve-Groesse fuer eine einzelne Strategie) irrelevant ist. Die quantifizierten Eckdaten:

- Aggregiertes taegliches Dollarvolumen des gesamten US-Microcap-Segments: Groessenordnung **wenige hundert Mio. USD** (branchenueblich zitiert: ~420 Mio. USD), gegenueber 43x (Small Cap) und 245x (Large Cap) hoeheren Volumina in den jeweils naechstgroesseren Segmenten.
- Ein einzelner Fonds "wird zum Markt" bei ca. **5 Mrd. USD AUM** — realistische verlustfreie Kapazitaetsgrenze liegt deutlich darunter, im niedrigen einstelligen Milliardenbereich fuer Long-only, im **dreistelligen Millionenbereich** fuer Long-Short-Varianten mit Short-Bein in Junk-Microcaps.
- Market Impact fuer institutionell relevante Tickets (10 Mio. USD) reicht bis **220 Basispunkte** in den illiquidesten Titeln — das entspricht bereits einem Vielfachen der behaupteten monatlichen Alpha-Groessen (20-44 Bp/Monat bei Kandidat 2).

Diese Zahlen bedeuten: selbst wenn man der optimistischsten Lesart der Asness-et-al.-Ergebnisse vollstaendig folgt, ist das Ergebnis fuer ein institutionelles Multi-Strategie-Mandat **kein einsetzbarer Baustein**, sondern bestenfalls eine theoretisch interessante Fussnote zur Marktmikrostruktur-Forschung. Dies ist ein Fall, in dem "Limits to Arbitrage als Erklaerung fuer eine fortbestehende Ineffizienz" und "Limits to Arbitrage als Grund, warum diese Ineffizienz fuer uns nicht nutzbar ist" **beide gleichzeitig wahr sein koennen und sich nicht gegenseitig ausschliessen** — genau das ist hier der Fall.

Ein interessanter Nebenbefund, der nicht in die drei Hauptkandidaten passt, aber erwaehnenswert ist: Acadian-Research zeigt, dass aktive Small-Cap-Manager im Median in den letzten fuenf Jahren **2,8% p.a. Brutto-Excess-Return** erzielt haben, gegenueber praktisch **0% fuer aktive Large-Cap-Manager**. Das deutet darauf hin, dass in Small Caps eine echte, aber **idiosynkratische Stock-Picking-Ineffizienz** (mangelnde Analysten-Coverage, Informationsasymmetrie) fortbesteht — das ist jedoch eine fundamentale/bottom-up Alpha-Quelle, keine systematische Size- oder Size+Quality-Faktorpraemie, und faellt damit ausserhalb des hier untersuchten Mandats (systematische Anomalien), waere aber ein moeglicher Hinweis fuer ein anderes Team (fundamentales Long/Short-Stock-Picking-Mandat).

## 6. Gesamturteil und Empfehlung

| Kandidat | Urteil | p(echte Ineffizienz) | Netto-Sharpe-Erwartung |
|---|---|---|---|
| Rohe Size-Praemie | KILL | 0,08 | 0,0-0,05 |
| Size + Quality (Asness et al. 2018) | WEAK | 0,40 | 0,15-0,30 brutto / 0,0-0,15 netto bei Skalierung |
| Mikrocap-Illiquiditaetspraemie (DFA-Stil) | WEAK | 0,30 | 0,10-0,20 |

**Keine der drei Strategien erreicht die CANDIDATE-Schwelle.** Die rohe Size-Praemie ist ein Lehrbuch-Fall einer Anomalie, die nach Publikation verschwunden ist (Schwert 2003) — Delisting-Bias, Januar-Konzentration und Microcap-/Equal-Weighting-Artefakte erklaeren den Grossteil des historischen Befunds. Die "Size+Quality"-Rettung von Asness et al. (2018) haelt akademisch beeindruckend gut Stand (t-Statistiken um 4, Robustheit ueber 24 Laender und 30 Industrien), scheitert aber an der Kombination aus (a) fehlender sauberer Post-Publication-Bestaetigung — verschaerft durch den Umstand, dass der Qualitaetsfaktor selbst seit 2021 in seiner schlimmsten Schwaechephase seit 20 Jahren steckt — und (b) strukturell hohen Kosten und minimaler Kapazitaet im fuer das Alpha entscheidenden Short-Bein aus Junk-Microcaps. Die dritte, praktisch orientierte Variante zeigt zwar den einzigen wirklich langfristigen positiven Netto-Track-Record in dieser Klasse (DFA, +1,5% p.a. seit 1981), aber die zugrunde liegende akademische Illiquiditaetspraemie gilt in der Fachliteratur seit Mitte der 1980er als statistisch tot (Ben-Rephael/Kadan/Wohl 2015) — die beobachtete Outperformance ist plausibler als manager-spezifisches Exekutions-Alpha denn als systematische, replizierbare Marktineffizienz zu interpretieren.

**Empfehlung fuer das Gesamtmandat**: Small Caps & Micro Caps als eigene Anomalieklasse fuer ein institutionelles quantitatives Multi-Strategie-Buch **nicht allokieren**. Falls die Klasse dennoch aus Diversifikationsgruenden beruecksichtigt werden soll, dann ausschliesslich als (a) sehr kleine Sleeve-Groesse (deutlich unter 1% des Gesamtbuchs), (b) mit Fokus auf die Size+Quality-Long-Seite ohne das kostentreibende Short-Bein in Junk-Microcaps, und (c) mit expliziter Erwartungshaltung, dass ein Grossteil der akademisch dokumentierten Praemie durch Kosten und Kapazitaetsengpaesse aufgezehrt wird. Ein ehrliches "diese Klasse ist im Wesentlichen tot fuer institutionelles Kapital" ist das primaere und valide Ergebnis dieser Untersuchung.

## 7. Quellenverzeichnis (in dieser Recherche verwendet)

- Asness, C., Frazzini, A., Israel, R., Moskowitz, T., Pedersen, L.H. (2018): *Size Matters, If You Control Your Junk*, Journal of Financial Economics 129(3), 479-509. https://www.sciencedirect.com/science/article/pii/S0304405X18301326 ; SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3122326 ; AQR: https://www.aqr.com/Insights/Research/Working-Paper/Size-Matters-If-You-Control-Your-Junk
- Asness, C., Israel, R., Moskowitz, T. et al.: *Fact, Fiction, and the Size Effect*, verwandte AQR/JPM-Publikation. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2553889
- Banz, R.W. (1981): *The Relationship Between Return and Market Value of Common Stocks*, Journal of Financial Economics 9, 3-18 (Sekundaerzitate, Primaertext nicht direkt einsehbar).
- Schwert, G.W. (2003): *Anomalies and Market Efficiency*, NBER Working Paper 9277. https://www.nber.org/papers/w9277
- Keim, D. (1983): *Size-Related Anomalies and Stock Return Seasonality: Further Empirical Evidence*, Journal of Financial Economics 12. https://www.sciencedirect.com/science/article/abs/pii/0304405X83900259
- Shumway, T., Warther, V. (1999): *The Delisting Bias in CRSP's Nasdaq Data and Its Implications for the Size Effect*, Journal of Finance. https://onlinelibrary.wiley.com/doi/abs/10.1111/0022-1082.00192
- Hou, K., Xue, C., Zhang, L. (2020): *Replicating Anomalies*, Review of Financial Studies 33, 2019-2133. https://www.nber.org/system/files/working_papers/w23394/w23394.pdf
- Ben-Rephael, A., Kadan, O., Wohl, A. (2015): *The Diminishing Liquidity Premium*, Journal of Financial and Quantitative Analysis. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1099829
- Morningstar: *What Happened to the Size Premium?* https://www.morningstar.com/alternative-investments/what-happened-size-premium
- MSCI: *High Short Interest and Low Quality Hurt Small Caps' Performance*. https://www.msci.com/research-and-insights/blog-post/high-short-interest-and-low-quality-hurt-small-caps-performance
- Acadian Asset Management: *U.S. Small-Cap Performance: Bad But Still Fine*. https://www.acadian-asset.com/investment-insights/equities/us-small-cap-performance-relatively-bad-but-absolutely-fine
- Factor Investor / O'Shaughnessy Asset Management: *Micro Caps, Factor Spreads, Structural Biases, and the Institutional Imperative*. https://www.factorinvestor.com/blog/micro-caps-factor-spreads-structural-biases-and-the-institutional-imperative
- Dimensional Fund Advisors: *The Evolution of Small Cap Investing: Four Decades of Innovation at Dimensional*. https://www.dimensional.com/us-en/insights/the-evolution-of-small-cap-investing-four-decades-of-innovation-at-dimensional
- AAII Fund Data: DFA US Micro Cap I (DFSCX). https://www.aaii.com/fund/ticker/DFSCX
- CFA Institute Enterprising Investor (2025): *Patience Pays: Why Quality Shares Outperform in the Long Run*. https://blogs.cfainstitute.org/investor/2025/12/02/patience-pays-why-quality-shares-outperform-in-the-long-run/
- Davy: *Quality Investing: Why Performance Has Lagged and What Comes Next* (2026). https://www.davy.ie/market-and-insights/insights/investing-insights/2026/quality-on-the-backfoot-what-happened--implications-going-forward.html

**Hinweis zur Evidenzqualitaet**: Web-Suche war grossteils verfuegbar und wurde extensiv genutzt; einige Primaerquellen (SSRN-Volltexte, Alpha-Architect-Artikel) waren per WebFetch nicht zugaenglich (403-Fehler bzw. PDF-Encoding-Probleme) und wurden durch Sekundaerzitate aus Suchmaschinen-Snippets ersetzt. Exakte Banz-1981-Originalzahlen sowie einige Randdetails stammen aus internem Modellwissen (Stand Anfang 2026) und sind im Text entsprechend als Literaturkonsens statt Primaerverifikation gekennzeichnet.
