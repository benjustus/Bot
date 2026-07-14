```yaml
agent: 14
klasse: "Cross-Sectional Momentum"
websuche_verfuegbar: ja
strategien:
  - name: "12-1 Preis-Momentum (Winners-minus-Losers, Jegadeesh-Titman-Standard)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 5
      signifikanz_nach_mtk: 4
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.45
    netto_sharpe_erwartung: "0.15-0.35 unmanaged; siehe Kandidat 2 fuer risikogemanagte Variante"
    kernrisiko: "Linksschiefe Crash-Tail bei V-foermigen Markterholungen nach Abverkaeufen (1932, 2009, 2020, Jan/Jun-Jul 2026); Crowding verstaerkt genau dieses Muster"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken French Data Library: 'Momentum Factor (Mom)' bzw. '10 Portfolios Formed on Momentum', monatlich seit 1927"
  - name: "Residual-/Idiosynkratisches Momentum mit Volatility-Scaling (Blitz/Huij/Martens + Barroso/Santa-Clara)"
    urteil: CANDIDATE
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 4
      regimestabilitaet: 3
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.5
    netto_sharpe_erwartung: "0.30-0.50, mit Vol-Scaling in ruhigen Regimen ggf. hoeher; Tail-Risiko reduziert, nicht eliminiert"
    kernrisiko: "Faktor-Crowding (Hedgefonds-Momentum-Positionierung lt. Goldman Sachs Juli 2026 im 92. Perzentil der letzten 5 Jahre) plus Konstruktions-/Kapazitaetsgrenzen; Vol-Scaling mindert, verhindert aber keine Crashes wie Nov. 2020"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Ken-French 'F-F Research Data 5 Factors (2x3)' fuer Residuenberechnung + freie Einzelkursdaten (z.B. Stooq); kein fertiges Ken-French Residual-Momentum-Dataset vorhanden"
```

# Agent 14 — Cross-Sectional Momentum / Relative Strength

**Mandat:** 12-1-Momentum (Jegadeesh & Titman 1993), residuales Momentum, Momentum-Crashes und deren Management.
**Haltung:** Adversarial. Nullhypothese: Es gibt kein echtes, nach Kosten und Crash-Risiko robustes Alpha in dieser Klasse.
**Evidenzbasis:** Websuche funktionierte (WebSearch/WebFetch verfuegbar) und wurde fuer Originalstudien, Post-Publication-Literatur sowie tagesaktuelle Marktereignisse bis 09.07.2026 genutzt. Wo Zahlen nicht direkt durch eine Suchquelle verifiziert werden konnten, ist dies explizit als "internes Wissen, ungeprüft" markiert — Vorsicht ist geboten, da diese Klasse extrem gut erforscht, aber auch extrem anfaellig fuer selektive Zitate ist.

---

## 0. Executive Summary

Cross-Sectional Momentum ist vermutlich die am besten dokumentierte Anomalie der Asset-Pricing-Literatur: >30 Jahre akademische Historie, >200 Jahre Out-of-Sample-Backtest (Geczy & Samonov), Replikation in acht Anlageklassen und Dutzenden Laendern (Asness, Moskowitz & Pedersen 2013). Gleichzeitig ist sie das Lehrbuchbeispiel fuer eine Anomalie mit **eingebautem Selbstzerstoerungsmechanismus**: negative Schiefe, episodische Crashes von historischem Ausmass (2009: Verlierer schlugen Gewinner in drei Monaten um >70 Prozentpunkte) und eine seit 2000 spuerbar schwaechere Sharpe Ratio. Bemerkenswert: Just in der Woche dieser Analyse (Juli 2026) melden Bloomberg und Goldman Sachs den **zweiten schweren Momentum-Crowding-Unwind des Jahres 2026** (nach Januar 2026), ausgeloest durch eine Rotation aus AI-/Chip-/Memory-"Momentum"-Aktien — ein Live-Fallbeispiel fuer exakt den Mechanismus, den Daniel & Moskowitz (2016) theoretisch beschreiben. Das ist kein Zufall, sondern strukturell: Momentum ist crowded, weil es funktioniert hat, und es crasht periodisch, weil es crowded ist.

Fazit vorweg: Die Klasse ist **nicht tot**, aber die "reine", ungemanagte Long-Short-Variante ist als eigenstaendiges investierbares Produkt fragil (WEAK). Eine risikogemanagte Variante (residual/idiosynkratisch, vol-skaliert) verdient das Praedikat CANDIDATE — mit der ausdruecklichen Einschraenkung, dass auch sie 2026 sichtbar unter Crowding-Stress steht.

---

## Kandidat 1: 12-1 Preis-Momentum (Winners-minus-Losers)

### a) Oekonomische Begruendung: Underreaction vs. Overreaction

Die kanonische Erklaerung ist ein **zweistufiges Verhaltensmuster**:

1. **Kurzfristige Unterreaktion (3-12 Monate):** Information diffundiert langsam (Hong & Stein 1999 "Underreaction, Momentum Trading, and Overreaction"). Analysten passen Schaetzungen verzoegert an (Hong, Lim & Stein 2000, "Bad News Travels Slowly" — Unterreaktion staerker bei geringer Analystenabdeckung). Der Dispositionseffekt (Grinblatt & Han 2005) fuehrt dazu, dass Anleger Gewinner zu frueh verkaufen und Verlierer zu lange halten, was den Preis von der neuen Information "verankert" (Anchoring) haelt und die Kursanpassung streckt.
2. **Mittelfristige Fortsetzung durch Trendfolger/Feedback-Trader:** Sobald der Trend etabliert ist, verstaerken positive-feedback-trader und Momentum-Investoren selbst die Bewegung (Barberis, Shleifer & Vishny 1998; De Long et al. 1990), was ueber 3-12 Monate zur Fortsetzung, danach (12-36 Monate) typischerweise zur Ueberreaktion und Trendumkehr fuehrt (De Bondt & Thaler 1985 langfristige Reversal-Literatur als Spiegelbild).

**Wer ist die Gegenseite (Counterparty)?** Strukturell verkaufen/kaufen gegen Momentum: (i) dispositionsgetriebene Privatanleger, die Gewinner zu frueh verkaufen (liefern damit dem Momentum-Trader die "billigen" fortlaufenden Gewinner); (ii) langsame institutionelle Anleger mit Rebalancing-Regeln (z.B. Value-orientierte oder Index-nahe Fonds, die antizyklisch gegen den Trend handeln); (iii) Short-Interest-Constraints bei Verlierern begrenzen das Ausmass, in dem Pessimisten den Kurs sofort korrigieren.

**Wichtige Gegenerzaehlung (Kritik der behavioralen Story):** Ehsani & Linnainmaa ("Factor Momentum and the Momentum Factor", Journal of Finance 2022) zeigen, dass ein grosser Teil des Aktien-Momentums schlicht **Autokorrelation in Faktor-Renditen** widerspiegelt (Faktor-Momentum) — d.h. Einzelaktien-Momentum koennte teilweise ein mechanisches Nebenprodukt persistenter Faktorexposures sein und nicht primaer eine aktienspezifische Informationsdiffusions-Anomalie. Das schwaecht die reine Behavioral-Story und stuetzt tendenziell eine (teil-)rationale, risikobasierte Interpretation.

### b) Limits to Arbitrage

Das zentrale Arbitrage-Hemmnis ist **nicht** Leerverkaufsbeschraenkung oder Illiquiditaet allein (wie z.B. bei Small-Cap-Anomalien), sondern **Crash-Risiko selbst als Barriere**:

- Momentum-Strategien sind strukturell **short die grossen Verlierer nach einem Marktabschwung** — genau die Aktien, die bei einer scharfen Erholung (V-Rebound) am staerksten steigen (hohes Beta, hohe Distress-Sensitivitaet, oft hard-to-borrow). Der Arbitrageur wird also gezwungen, in der volatilsten Marktphase die Position zu halten, in der ein Fehler am teuersten ist.
- **Funding-Liquidity-Spiralen** (Brunnermeier & Pedersen 2009): Nach einem Crash schrumpft das Risikokapital der Arbitrageure genau dann, wenn Prime-Broker-Margins steigen — VaR-getriebene Deleveraging-Zwaenge verstaerken den Momentum-Crash selbst (siehe 2009, 2020, 2026 unten).
- **Karriererisiko / Principal-Agent-Problem** (Shleifer & Vishny 1997): Weil Momentum-Crashes selten, aber sehr gross sind, fuehren sie zu Redemptions genau zum ungluecklichsten Zeitpunkt. Ein PM, der eine -30% bis -50%-Drawdown-Episode "durchhaelt", riskiert Kapitalabzug, bevor die Erholung eintritt — das begrenzt strukturell, wie viel Kapital dauerhaft in reinem Momentum investiert bleibt, und erklaert teilweise, warum die Anomalie trotz jahrzehntelanger Bekanntheit nicht wegarbitriert wurde.

### c) Originalstudien

**Jegadeesh & Titman (1993)**, "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency", Journal of Finance 48(1), 65-91. Stichprobe: NYSE/AMEX 1965-1989. Kernresultat: Long-Short-Strategien (Formation J Monate, Holding K Monate) erzielen signifikant positive Renditen ueber 3-12-Monats-Horizonte. Die staerkste Spezifikation (12 Monate Formation, 3 Monate Holding) erzielt ca. **1,31% pro Monat** fuer das Winner-minus-Loser-Portfolio; die vielzitierte 6/6-Spezifikation liefert rund 12% p.a. mit einer t-Statistik von ca. 3,0 (Literaturkonsens; exakte t-Werte je nach Subperiode/Spezifikation zwischen ca. 2,8 und 4,5). Damit klart die Studie auch strengere, spaeter vorgeschlagene Multiple-Testing-Huerden wie t>3,0 (Harvey, Liu & Zhu 2016) — zumindest in der Originalstichprobe.

**Blitz, Huij & Martens (2011)**, "Residual Momentum", Journal of Empirical Finance 18(3), 506-521. Kernidee: Statt auf totale Renditen zu sortieren, wird auf **residuale Renditen** (nach Herausrechnen der Fama-French-3-Faktor-Exposures) sortiert. Ergebnis: Risikoadjustierte Profite sind **etwa doppelt so hoch** wie bei konventionellem Total-Return-Momentum, weil die zeitvariable Faktor-Exponierung (insbesondere das dynamische Beta konventioneller Momentum-Portfolios, siehe Grundy & Martin 2001) eliminiert wird. Residual-Momentum-Renditen sind zudem gleichmaessiger ueber die Zeit verteilt und weniger in den Extremdezilen der Renditeverteilung konzentriert — ein direkter Hinweis auf geringeres Crash-Exposure. Nachfolgeliteratur (Huij & Lansdorp, "Residual Momentum and Reversal Strategies Revisited"; Hanauer & Windmueller, "Enhanced Momentum Strategies") bestaetigt signifikant hoehere Return-to-Risk-Ratios international und out-of-sample.

### d) Out-of-Sample- / Post-Publication-Evidenz

- **Geczy & Samonov (2016), "Two Centuries of Price-Return Momentum"** (teils publiziert als "212 Years of Price Momentum"): Datensatz US-Aktienkurse 1801-1926 als echter Pre-Sample-Out-of-Sample-Test fuer die post-1927-Literatur. Ergebnis: Der Momentum-Premium bleibt ueber den gesamten Zeitraum 1801-2012 (212 Jahre) positiv und statistisch signifikant, mit durchschnittlichen Ueberschussrenditen von rund **0,4% pro Monat**. Wichtig: Die Autoren zeigen auch, dass Momentum dynamisch positioniertes Markt-Beta traegt — an Markt-Wendepunkten ist das Beta der Strategie systematisch "falsch" positioniert, was direkt die Crash-Mechanik erklaert.
- **Asness, Moskowitz & Pedersen (2013), "Value and Momentum Everywhere"**, Journal of Finance 68, 929-985: Momentum (und Value) sind in acht diversen Maerkten/Anlageklassen nachweisbar (US-, UK-, Kontinentaleuropa-, Japan-Aktien, Laenderindizes, Staatsanleihen, Waehrungen, Rohstoffe) — mit konsistenter Faktorstruktur ueber Anlageklassen hinweg. Das ist die staerkste verfuegbare Evidenz gegen eine reine Datamining-Erklaerung, da die Effekte in Maerkten mit unterschiedlicher Mikrostruktur, Investorenbasis und Publikationszeitpunkt auftauchen.
- **US-Performance nach 2000, spuerbar schwaecher:** Nach internem Wissen (nicht durch eine einzelne Quelle exakt beziffert, Vorsicht geboten) fiel die annualisierte Sharpe Ratio des US-Momentumfaktors (UMD/MOM) von ca. 0,5-0,6 im Gesamtsample (1927-2000) auf deutlich niedrigere, teils nahe null oder negative Werte in rollierenden 10-Jahres-Fenstern nach 2000 — getrieben v.a. durch die 2009-Krise. Presse-/Sekundaerquellen sprechen vom "verlorenen Jahrzehnt" 2000-2009 fuer den Faktor. Diese Angabe ist als grobe Naeherung zu verstehen, nicht als praezise verifizierte Zahl.
- **McLean & Pontiff (2016), "Does Academic Research Destroy Stock Return Predictability?"**, Journal of Finance: Untersuchung von 97 publizierten Renditepraediktoren. Durchschnittlicher Rueckgang der Portfoliorenditen **26% out-of-sample** (obere Schranke fuer reinen Data-Mining-Bias) und **58% post-publication** (zusaetzlicher Rueckgang durch "Investor Learning"/Publikations-Trading). Momentum ist Teil der untersuchten Stichprobe; ein separater, verifizierter Einzelwert nur fuer Momentum liegt uns nicht vor — Sekundaerliteratur zitiert haeufig eine Groessenordnung von ca. 50% Decay, was aber als Naeherung zu behandeln ist.
- **Momentum-Crashes 2009/2016/2020-21 (Daniel & Moskowitz 2016, "Momentum Crashes", Journal of Financial Economics; NBER WP 20439):** Zentrale Befunde: Momentum-Renditen sind linksschief mit seltenen, aber extremen Verlustserien, die typischerweise nach Marktabschwuengen bei hoher Volatilitaet auftreten und mit Marktrebounds zusammenfallen ("Panikzustaende"). Konkretes Beispiel Maerz-Mai 2009: Der Gesamtmarkt stieg um ca. 26%, das Verlierer-Dezil um ca. 156-163%, waehrend Gewinner nur ca. 15% zulegten — die WML-Faktor-Rendite kollabierte in diesen drei Monaten um Groessenordnungen, die einzelne Quellen mit bis zu -80% ueber wenige Monate beziffern. Eine implementierbare dynamische Strategie (Prognose von Momentum-Mean und -Varianz) verdoppelt laut den Autoren naeherungsweise Alpha und Sharpe Ratio der statischen Strategie. November 2020 (Post-Vaccine-Announcement-Rotation aus Covid-Gewinnern in Covid-Verlierer) gilt als einer der schaerfsten Einzelmonats-Reversal-Ereignisse der dokumentierten Geschichte; ein klassisches WML-Portfolio verzeichnete laut Sekundaerquellen einen Drawdown von rund -50% von Oktober 2020 bis Mai 2021, eine modifizierte (Crash-geschuetzte) Variante rund -25%.

### e) Kosten: Wer hat recht — Lesmond/Schill/Zhou oder Frazzini/Israel/Moskowitz?

Dies ist der zentrale Streitpunkt, den ich adversarial aufloesen muss:

- **Lesmond, Schill & Zhou (2004), "The Illusory Nature of Momentum Profits"**, Journal of Financial Economics 71(2), 349-380: Zeigen, dass Standard-Relative-Strength-Strategien ueberproportional in Aktien mit hohen Handelskosten (kleine, illiquide, hoher Bid-Ask-Spread) konzentriert sind. Mit indirekten Kostenschaetzern (LOT-Mass, Roll-Spread-Proxies) kommen sie zum Schluss, dass die Handelskosten die Bruttorendite vollstaendig auffressen — die Anomalie sei eine "Illusion".
- **Novy-Marx & Velikov (2016), "A Taxonomy of Anomalies and Their Trading Costs"**, Review of Financial Studies 29(1), 104-147: Systematischere Kostenanalyse ueber 23 Anomalien. Zentrales Ergebnis: Anomalien mit >50% monatlichem Turnover ueberleben Handelskosten selten in ihrer naiven Form — Momentum gehoert mit sehr hohem Turnover (haeufig deutlich >50%/Monat je Bein) zu den kostenanfaelligsten Strategien. ABER: Mit **Kostenminderungstechniken** — insbesondere einer Buy/Hold-Spread-Regel (strengere Aufnahme- als Haltekriterien, reduziert unnoetiges Rebalancing) — laesst sich der effektive Turnover deutlich senken, wonach ein signifikanter Netto-Spread uebrig bleibt. D.h. auch NV2016 bestaetigen implizit: naiv gehandeltes Momentum verliert einen Grossteil seines Alphas an Kosten, klug implementiertes Momentum nicht vollstaendig.
- **Frazzini, Israel & Moskowitz (2012/2018), "Trading Costs of Asset Pricing Anomalies" / "Trading Costs"**: Nutzen **reale Ausfuehrungsdaten von 1,7 Billionen USD** eines grossen institutionellen Managers (AQR) ueber 21 entwickelte Aktienmaerkte und 19 Jahre. Kernbefund: **tatsaechliche Handelskosten sind eine Groessenordnung kleiner** als die in Lesmond et al. (2004) und aehnlichen Modellstudien geschaetzten Kosten. Ein auf reale Ausfuehrungsdaten kalibriertes Modell erklaert Kosten ueber Handelsgroesse, Aktienmerkmale und Zeit signifikant besser als literaturuebliche Modellansaetze.

**Aufloesung des Widerspruchs:** Lesmond/Schill/Zhou (2004) verwenden **indirekte, modellbasierte Kostenproxys** (LOT-Mass, geschaetzte Effective Spreads), die fuer genau die kleinen/illiquiden Aktien in den Momentum-Extremdezilen die Kosten systematisch **ueberschaetzen** — diese Proxys sind fuer Retail-groesse Round-Trip-Trades kalibriert, nicht fuer institutionelle Ausfuehrung mit Order-Splitting, algorithmischem Trading und Liquiditaetsmanagement. Frazzini/Israel/Moskowitz zeigen mit echten Live-Daten, dass ein grosser, erfahrener institutioneller Trader (AQR) diese Kosten durch geschickte Ausfuehrung massiv unterschreitet. Novy-Marx & Velikov liefern die methodische Bruecke: Mit realistischer, kostenminimierender Implementierung (nicht die "Lehrbuch"-Rebalancing-Regel, die JT93 fuer akademische Zwecke verwendet) bleibt ein signifikanter Netto-Spread erhalten, der aber deutlich kleiner ist als der Brutto-Spread. **Fazit: Beide Seiten haben in ihrem jeweiligen Kontext recht** — naiv/akademisch gehandeltes Momentum verliert einen erheblichen Teil (vermutlich 40-70%, grobe Naeherung) seines Bruttoalphas an Kosten; professionell/institutionell mit Kostenminderungstechniken implementiertes Momentum ueberlebt mit reduziertem, aber positivem Netto-Alpha. Das reale, jahrzehntelange Live-Trackrecord der AQR-Momentumfonds (siehe unten) ist der praktische Beleg fuer die zweite Sichtweise — allerdings mit erheblicher Volatilitaet.

**Live-Datenpunkt (AQR-Fonds, aus SEC-Filings/Factsheets, Stand Ende 2025):** AQR Large Cap Momentum Style Fund (AMOMX): 2022 +4,65%, 2023 +23,88%, 2024 -3,84%, 2025 (YTD per 31.12.) +15,88%. AQR International Momentum Style Fund (AIMOX): 2022 -3,63%, 2023 +25,25%, 2024 -15,28%, 2025 +35,05%. Diese Zahlen zeigen ein real gehandeltes, nach Kosten und Gebuehren investierbares Produkt mit signifikanter Jahr-zu-Jahr-Streuung — konsistent mit "Alpha existiert netto, aber ist volatil und regimeabhaengig", nicht mit "Alpha ist illusorisch".

### f) Kapazitaet

Praktikerschaetzungen (nicht durch eine einzelne autoritative Studie exakt verifiziert, daher als grobe Groessenordnung zu verstehen) siedeln die Kapazitaet von US-Large-Cap-Momentum im niedrigen bis mittleren zweistelligen Milliarden-USD-Bereich an, deutlich unterhalb von Size/Value (Novy-Marx & Velikov 2016 finden explizit, dass Size, Value und Profitability die groesste Kapazitaet fuer neues Kapital haben, invers zum Turnover — Momentum hat wegen seines hohen Turnovers strukturell **geringere** Kapazitaet als diese Faktoren). AQR verwaltet ueber mehrere Momentum-/Style-Fonds gemeinsam einen mittleren zweistelligen Milliarden-Betrag (AQR Gesamt-AUM ca. 165-166 Mrd. USD per Ende September 2025, Momentum ist einer von mehreren Sleeves) — ein Indiz, dass die Strategie bei Milliarden-, nicht bei Billionen-Kapazitaet skalierbar bleibt, bevor Market-Impact-Kosten das Alpha erodieren.

### g) Regimeabhaengigkeit und Tail-Risiko

Negative Schiefe und Crash-Cluster sind das definierende Merkmal dieser Strategie (siehe c/d oben). **Barroso & Santa-Clara (2015), "Momentum Has Its Moments"**, Journal of Financial Economics 116(1), 111-120: Zeigen, dass das Risiko von Momentum (gemessen an realisierter 6-Monats-Volatilitaet) selbst zeitlich vorhersagbar ist. Eine Skalierung der Positionsgroesse invers zur realisierten Volatilitaet (Ziel: konstante 12% Vol) **eliminiert praktisch die Crashes und verdoppelt nahezu die Sharpe Ratio** — von 0,53 (unmanaged) auf 0,97 (vol-managed) in ihrer Stichprobe. Das ist eine der wenigen Techniken in der gesamten Faktor-Literatur mit derart drastischer dokumentierter Wirkung.

**Aber:** Vol-Scaling ist kein Free Lunch. Es wirkt am besten gegen **graduell ansteigende** Volatilitaet (funktioniert also gut, wenn die Krise sich "ankuendigt"), versagt aber tendenziell bei **plötzlichen** Sprunggefahren wie der scharfen Ein-Monats-Rotation im November 2020, wo Vol-Scaling laut Sekundaerquellen den Drawdown zwar von ca. -50% auf ca. -25% reduzierte, aber keineswegs auf null. Die 212-Jahre-Studie von Geczy & Samonov zeigt zudem, dass an Markt-Wendepunkten das Beta der Momentum-Strategie strukturell "falsch" ausgerichtet ist — ein Muster, das reines Vol-Scaling (das nur die Grosse, nicht die Richtung der Exposure adressiert) nicht vollstaendig loest.

### h) Bekannte Kritik / Widerlegungen

1. **Lesmond, Schill & Zhou (2004):** Handelskosten machen die Anomalie illusorisch (s.o., partiell durch bessere Kostendaten widerlegt, aber nicht vollstaendig entkraeftet fuer naive Implementierung).
2. **Risikobasierte Gegenerklaerung:** Momentum-Crashes koennten Kompensation fuer ein Crash-Risiko/"Peso-Problem" sein (rationales Risikopremium statt Mispricing) — Grundy & Martin (2001) zeigen zeitvariable Faktor-Exposures als (Teil-)Erklaerung der Renditen; das relativiert die reine Behavioral-Story.
3. **Ehsani & Linnainmaa (2022), "Factor Momentum and the Momentum Factor":** Aktien-Momentum ist groesstenteils ein Nebenprodukt der Persistenz von Faktor-Renditen selbst (Faktor-Momentum), nicht primaer eine aktienspezifische Anomalie — schwaecht die Informationsdiffusions-Story als alleinige Erklaerung.
4. **Harvey, Liu & Zhu (2016), "...and the Cross-Section of Expected Returns":** Fordern angesichts hunderter publizierter Faktoren eine hoehere t-Stat-Huerde (t>3,0) zur Kontrolle von Multiple Testing/p-Hacking. Momentum uebersteht diese Huerde in den meisten Studien, ist aber nicht immun gegen den generellen Verdacht des Data-Snooping in der Faktor-Zoo-Literatur.
5. **McLean & Pontiff (2016):** Dokumentierter Decay nach Publikation — konsistent mit (teilweisem) Crowding-Effekt statt reinem, dauerhaftem Verhaltensfehler.

**Urteilsbegruendung Kandidat 1 — WEAK:** Die Evidenzbasis fuer die Existenz eines historischen Effekts ist aussergewoehnlich stark (212 Jahre, 8 Anlageklassen, Dutzende Laender). Das disqualifiziert eine KILL-Einstufung. Gegen CANDIDATE sprechen: (i) die dokumentierte Kostenerosion bei naiver Implementierung, (ii) die strukturelle, wiederkehrende Crash-Anfaelligkeit gerade in den Marktphasen, in denen Kapital am knappsten ist, (iii) die spuerbar schwaechere Post-2000-Performance, und (iv) — am staerksten gewichtet — die **laufende, tagesaktuelle Evidenz aus 2026** (siehe Abschnitt "Uebergreifende Beobachtungen"), die zeigt, dass genau dieser Crash-Mechanismus gerade jetzt wieder aktiv ist. Ohne explizites Risikomanagement (Vol-Scaling, Residualisierung) ist reines 12-1-Momentum ein fragiles, regimeabhaengiges Produkt.

---

## Kandidat 2: Residual-/Idiosynkratisches Momentum mit Volatility-Scaling

### a) Oekonomische Begruendung

Identisch zur Grundstory in Kandidat 1 (langsame Informationsdiffusion, Anchoring, Dispositionseffekt), jedoch mit einer wichtigen Praezisierung: Blitz, Huij & Martens (2011) argumentieren, dass ein erheblicher Teil der scheinbaren "Momentum-Rendite" in der konventionellen Sortierung tatsaechlich **kompensierte, zeitvariable Faktor-Exposure** ist (z.B. Value-, Size- oder Marktbeta-Tilts, die sich aus der Sortierung auf totale Renditen ergeben) und nicht aktienspezifische Informationsverarbeitung. Durch Herausrechnen dieser Exposures (Sortierung auf **Residuen** einer Fama-French-Regression) wird die Strategie naeher an eine reine Wette auf firmenspezifische, verhaltensbedingte Fehlbewertung gebracht. Das macht die behaviorale Interpretation (Unterreaktion auf firmenspezifische Nachrichten) **sauberer und glaubwuerdiger** als bei Total-Return-Momentum, wo ein Teil der Rendite eine verdeckte Faktor-Wette sein koennte (vgl. Ehsani & Linnainmaa 2022, Kandidat 1 Punkt h.3).

**Gegenseite:** Dieselbe wie bei Kandidat 1, aber mit einer zusaetzlichen Nuance — da Marktbeta und Industrie-Exposure explizit herausgerechnet werden, ist die Gegenseite staerker auf firmenspezifische (nicht marktweite) langsame Informationsverarbeiter beschraenkt: Sell-Side-Analysten mit trager Coverage, Retail-Anleger mit Dispositionseffekt auf Einzeltitelebene.

### b) Limits to Arbitrage

Grundsaetzlich dieselben Mechanismen wie Kandidat 1 (Crash-Risiko, Funding-Spiralen, Karriererisiko), jedoch **abgeschwaecht**, weil die explizite Beta-/Faktor-Hedging-Komponente die extremsten Markt-Rebound-Szenarien (die bei Kandidat 1 den groessten Schaden anrichten) teilweise neutralisiert. Zusaetzliches Arbitrage-Hemmnis: **Konstruktionskomplexitaet** — residuales Momentum erfordert laufende Rolling-Regressionen und Faktor-Hedges, was operationelle Kosten, Modellrisiko (Fehlspezifikation der Faktoren) und zusaetzlichen Turnover durch die Hedge-Beine erzeugt. Das ist eine hoehere Eintrittsbarriere fuer kleinere/unsophistiziertere Arbitrageure als simples Preis-Ranking — was paradoxerweise das Alpha potenziell laenger erhalten haben koennte, aber gleichzeitig bedeutet, dass die Strategie fast ausschliesslich von sophistizierten (und damit potenziell stark korrelierten/crowded) Quant-Häusern gehandelt wird.

### c) Originalstudie

Siehe Kandidat 1c fuer Blitz/Huij/Martens (2011): Residualmomentum liefert **ca. doppelt so hohe risikoadjustierte Profite** wie Total-Return-Momentum, mit signifikant reduzierter zeitvariabler Faktor-Exponierung. Ergaenzt durch **Barroso & Santa-Clara (2015)** fuer die Vol-Scaling-Komponente (Sharpe-Verdopplung von 0,53 auf 0,97 im Basisfall, s.o.).

### d) Out-of-Sample-/Post-Publication-Evidenz

- **Huij & Lansdorp, "Residual Momentum and Reversal Strategies Revisited":** Bestaetigen die Robustheit residualer Momentum-Strategien in erweiterten/aktualisierten Stichproben.
- **Hanauer & Windmueller, "Enhanced Momentum Strategies"** (Multi-Hurdle-Konferenzpapier): Internationale Evidenz fuer verbesserte Return-to-Risk-Ratios durch Kombination von Residual-Momentum mit weiteren Filtern (z.B. 52-Wochen-Hoch, Saisonalitaet).
- **Chinesische Evidenz** (Residual Momentum in China, ScienceDirect): Replikation ausserhalb entwickelter Maerkte, mit gewissen Abweichungen (chinesische Marktmikrostruktur, Retail-dominiert), aber grundsaetzlich bestaetigendem Befund.
- **Wichtige Einschraenkung:** Es gibt — anders als beim klassischen UMD-Faktor — kein etabliertes, jahrzehntelang oeffentlich verfuegbares Live-Fonds-Trackrecord speziell fuer "reines" Residual-Momentum in vergleichbarer Groessenordnung wie AQR's Total-Momentum-Fonds. Die Post-Publication-Evidenz ist daher staerker akademisch/Backtest-basiert als bei Kandidat 1.

### e) Kosten

Aehnliche Turnover-Charakteristik wie Kandidat 1 (hoher Umschlag durch monatliches Re-Ranking), **zusaetzlich** Kosten durch die Hedge-Beine (Faktor-neutralisierende Positionen). Novy-Marx & Velikov (2016) und Frazzini/Israel/Moskowitz (2012/2018) beziehen sich primaer auf Total-Return-Momentum; eine direkte, verifizierte Kostenanalyse speziell fuer Residual-Momentum liegt uns aus der Websuche nicht vor (Kennzeichnung: internes Wissen/Extrapolation). Plausibel ist, dass die zusaetzliche Hedge-Komponente die Kosten pro Einheit Brutto-Alpha tendenziell erhoeht, waehrend gleichzeitig das hoehere Brutto-Alpha (laut Blitz et al. ca. doppelt so hoch risikoadjustiert) einen Teil davon kompensiert. Insgesamt vermutlich aehnliche bis leicht schlechtere Netto-Kostenrobustheit als Kandidat 1 — daher hier konservativ mit demselben Score (3) bewertet statt hoeher.

### f) Kapazitaet

Tendenziell **niedriger** als Kandidat 1: Die Faktor-Hedge-Beine binden zusaetzliches Handelsvolumen ohne direkten Alpha-Beitrag, und die Strategie wird primaer von einer kleineren Zahl sophistizierter Quant-Manager gehandelt (hoehere Homogenitaet der Investorenbasis = hoeheres Crowding-Risiko bei gegebenem AUM). Grobe Einschaetzung (nicht separat verifiziert): einstelliger bis niedriger zweistelliger Milliarden-USD-Bereich pro Markt, bevor Kapazitaetsgrenzen spuerbar werden.

### g) Regimeabhaengigkeit und Tail-Risiko

Kombiniert man Residualisierung (reduziert Faktor-Beta-Fehlausrichtung an Wendepunkten, siehe Geczy & Samonov) mit Vol-Scaling (Barroso & Santa-Clara: Sharpe-Verdopplung, Crash-Reduktion), ergibt sich die **theoretisch robusteste** Variante der Klasse gegenueber Regimewechseln. Wichtig ist aber: Auch risikogemanagtes Momentum ist nicht immun — die November-2020-Episode zeigte bei modifizierten/geschuetzten Momentum-Strategien laut Sekundaerquellen noch immer einen Drawdown von rund -25%. Tail-Risiko wird gemindert, nicht eliminiert.

### h) Bekannte Kritik/Widerlegungen

Dieselben grundsaetzlichen Kritikpunkte wie bei Kandidat 1 (Faktor-Momentum-Reinterpretation nach Ehsani & Linnainmaa; Multiple-Testing-Bedenken). Zusaetzlich: Die Komplexitaet der Residualisierung selbst introduziert **Modellrisiko** (welche Faktoren werden herausgerechnet? Fama-French-3, -5, oder mehr? Ergebnis ist je nach Spezifikation nicht identisch) — ein methodischer Freiheitsgrad, der die Reproduzierbarkeit potenziell verringert (daher hier reproduzierbarkeit=4 statt 5 wie bei der methodisch simpleren Kandidat-1-Variante).

**Urteilsbegruendung Kandidat 2 — CANDIDATE (mit Vorbehalt):** Die Kombination aus dokumentierter Verdopplung des risikoadjustierten Alphas (Blitz et al.), international/zeitlich replizierter Post-Publication-Evidenz, und einer expliziten, empirisch bestaetigten Loesung fuer das zentrale Crash-Problem (Barroso & Santa-Clara) erfuellt die Bar "dokumentierte Post-Publication-Evidenz UND Kostenrobustheit" knapper, aber nachvollziehbar besser als die reine Preis-Momentum-Variante. Der Vorbehalt: Kapazitaet ist begrenzter, die Strategie ist auch 2026 sichtbar Teil des allgemeinen Momentum-Crowding-Komplexes (wenn auch mit reduziertem, nicht eliminiertem Tail-Risiko), und ein oeffentlich zugaengliches, jahrzehntelanges Live-Trackrecord in vergleichbarer Transparenz zu Kandidat 1 fehlt. Dies ist ein CANDIDATE fuer eine kleine, sorgfaeltig risikogemanagte Allokation — kein Freibrief fuer naive Skalierung.

---

## Uebergreifende Beobachtungen: Live-Evidenz Januar-Juli 2026

Die Websuche lieferte ungewoehnlich aktuelle, fuer die adversariale Pruefung hochrelevante Datenpunkte, die zum Zeitpunkt dieser Analyse (14.07.2026) praktisch in Echtzeit ablaufen:

1. **Januar 2026:** Quant-Hedgefonds erlitten laut Bloomberg (21.01.2026, "Quants in Worst Drawdown Since October as Crowded Bets Buckle") den schlimmsten 10-Tage-Drawdown seit Oktober 2025, ausgeloest durch das Auseinanderbrechen ueberfuellter Positionen, nicht durch einen breiten Marktabschwung. UBS schaetzte einen Rueckgang US-fokussierter Quant-Fonds von ca. 2,8% in zwei Wochen. Renaissance Technologies (~-4%) und Schonfeld (~-3,9%) waren betroffen. Explizit genannt: Momentum-Crowding in AI-nahen Namen als Haupttreiber.
2. **Juni/Juli 2026:** Laut Goldman Sachs (Bloomberg, 06.07.2026 "Quant Hedge Funds Extend Worst Run Since 2023 as Momentum Slides") verzeichneten systematische Long/Short-Manager den schlimmsten Drawdown seit August 2025 (-3,6% seit dem 22.06.2026), wodurch rund ein Viertel der Jahresgewinne ausradiert wurde (von +14,4% auf +10,8% YTD). Goldmans proprietaeres "High-Beta-Momentum-Basket" (dominiert von Chip-/Memory-Aktien) fiel kumuliert **-19% in zwei Wochen**. Die Hedgefonds-Momentum-Positionierung wird mit dem **92. Perzentil der letzten fuenf Jahre** beziffert — ein direktes, quantitatives Crowding-Signal. Ein Goldman-Trader-Zitat bringt es auf den Punkt: "The 'buy everything AI' trade is over. Divergence will return."

**Bewertung:** Diese beiden Episoden sind live ablaufende Illustrationen der Daniel-Moskowitz-Crash-Mechanik (hohe vorangegangene Positionierung/Crowding + scharfe Rotation = überproportionaler Drawdown) und der Shleifer-Vishny-Limits-to-Arbitrage-Logik (Crowding zwingt zu synchronen Unwinds). Sie bestaetigen nicht, dass die Anomalie tot ist — im Gegenteil, sie bestaetigen, dass der zugrunde liegende Trend-Fortsetzungs-Mechanismus noch aktiv genug ist, um von genuegend Kapital gejagt zu werden, dass er sich selbst destabilisiert. Das ist fuer eine adversariale Bewertung ambivalent: einerseits ein Beleg, dass "etwas Reales" gehandelt wird (sonst gaebe es nichts zu crowden), andererseits ein akutes Warnsignal, dass die Netto-Sharpe-Erwartung fuer die naechsten 12-24 Monate eher am unteren Ende der oben angegebenen Bandbreiten liegen duerfte.

---

## Gesamturteil zur Klasse Cross-Sectional Momentum

Diese Anomalieklasse ist **nicht tot**, aber auch kein "Free Lunch". Die Nullhypothese ("kein echtes Alpha") ist mit hoher Wahrscheinlichkeit fuer die reine, langfristige Existenz des Phaenomens **abzulehnen** — die 212-Jahre-Evidenz und die Acht-Anlageklassen-Replikation sind zu breit, um allein durch Data-Mining erklaerbar zu sein. Gleichzeitig ist die Nullhypothese fuer die Frage "kann ein Investor 2026 mit vertretbarem Risiko-Rendite-Profil netto Alpha extrahieren" **nicht** klar zu verwerfen — dafuer sind Post-2000-Decay, Kostenrealitaet bei naiver Implementierung, strukturelles Crash-Risiko und die akute, live beobachtbare Crowding-Situation zu gewichtig.

**Praktische Implikation:** Reines, ungemanagtes 12-1-Preismomentum ist WEAK — theoretisch belegt, praktisch fragil. Residual-/vol-skaliertes Momentum verdient CANDIDATE-Status als kleine, diszipliniert risikogemanagte Beimischung, nicht als Kernstrategie. In beiden Faellen gilt: Positionsgroessen muessen explizit an Crowding-/Vol-Signale gekoppelt werden (Barroso-Santa-Clara-Logik), und ein hartes Drawdown-/Exposure-Limit ist angesichts der dokumentierten Crash-Historie (2009, Nov. 2020, Jan. 2026, Jun./Jul. 2026) keine Option, sondern Voraussetzung.

---

## Quellen (Auswahl, ueber Websuche verifiziert)

- Jegadeesh, N. & Titman, S. (1993). Returns to Buying Winners and Selling Losers. Journal of Finance 48(1). https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf
- Blitz, D., Huij, J. & Martens, M. (2011). Residual Momentum. Journal of Empirical Finance 18(3). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2319861
- Daniel, K. & Moskowitz, T. (2016). Momentum Crashes. Journal of Financial Economics. https://www.kentdaniel.net/papers/published/mom12.pdf ; https://www.nber.org/papers/w20439
- Geczy, C. & Samonov, M. (2016). Two Centuries of Price-Return Momentum. https://papers.ssrn.com/abstract=2292544
- Asness, C., Moskowitz, T. & Pedersen, L. (2013). Value and Momentum Everywhere. Journal of Finance 68. https://www.aqr.com/Insights/Research/Journal-Article/Value-and-Momentum-Everywhere
- Barroso, P. & Santa-Clara, P. (2015). Momentum Has Its Moments. Journal of Financial Economics 116(1).
- Lesmond, D., Schill, M. & Zhou, C. (2004). The Illusory Nature of Momentum Profits. Journal of Financial Economics 71(2). https://www.bauer.uh.edu/rsusmel/phd/Lesmond_et%20al%20_2004_JFE.pdf
- Novy-Marx, R. & Velikov, M. (2016). A Taxonomy of Anomalies and Their Trading Costs. Review of Financial Studies 29(1). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2535173
- Frazzini, A., Israel, R. & Moskowitz, T. Trading Costs / Trading Costs of Asset Pricing Anomalies. https://www.aqr.com/Insights/Research/Working-Paper/Trading-Costs
- McLean, R. & Pontiff, J. (2016). Does Academic Research Destroy Stock Return Predictability? Journal of Finance. https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365
- Ehsani, S. & Linnainmaa, J. (2022). Factor Momentum and the Momentum Factor.
- AQR Fondsdaten (AMOMX, AIMOX Factsheets, SEC-Filings, Stand 12/2025). https://funds.aqr.com/
- Bloomberg (21.01.2026): "Quants in Worst Drawdown Since October as Crowded Bets Buckle". https://www.bloomberg.com/news/articles/2026-01-21/quants-in-worst-drawdown-since-october-as-crowded-bets-buckle
- Bloomberg (06.07.2026): "Quant Hedge Funds Extend Worst Run Since 2023 as Momentum Slides". https://www.bloomberg.com/news/articles/2026-07-06/quant-hedge-funds-extend-worst-run-since-2023-as-momentum-slides
- "Not All Factors Crowd Equally" (arXiv 2512.11913, zurueckgezogen zur Ueberarbeitung Dez. 2025) — als nicht-peer-reviewtes Arbeitspapier nur zur Illustration der Crowding-Debatte herangezogen, nicht als belastbare Primaerquelle gewertet.

**Hinweis zur Datenqualitaet:** Einzelne Zahlen (Post-2000-Sharpe-Ratio, exakte Decay-Prozentsaetze fuer Momentum spezifisch, Kapazitaetsschaetzungen) konnten nicht durch eine einzelne autoritative Primaerquelle im Rahmen dieser Recherche exakt verifiziert werden und sind im Text entsprechend als Naeherung/internes Wissen gekennzeichnet. Fuer eine Investment-Entscheidung waeren Primaerdatenzugriff (CRSP, Ken French Library Rohdaten, WRDS) und eigene Nachrechnung erforderlich.
