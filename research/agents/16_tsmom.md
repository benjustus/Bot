```yaml
agent: 16
klasse: "Zeitreihen-Momentum / Trendfolge"
websuche_verfuegbar: ja
strategien:
  - name: "Klassisches 12-Monats-TSMOM (Single-Signal, Moskowitz/Ooi/Pedersen 2012)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 4
      kapazitaet: 4
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.3
    netto_sharpe_erwartung: "0.1-0.3"
    kernrisiko: "Huang/Li/Wang/Zhou (2020, JFE): gepoolte Panel-Regression unterstellt identisches Alpha über alle 58 Instrumente und überschätzt dadurch Signifikanz massiv; asset-by-asset-Tests zeigen kaum TSM-Evidenz. Profitabilität evtl. nur Reflex der positiven historischen Durchschnittsrendite langer Bullenmärkte (Anleihen 1985-2020, Aktien) statt echter Trendfolge."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Kontinuierliche Futures-Kurse (Stooq, Yahoo Finance); AQR 'Time Series Momentum Original Paper Data' (öffentlich, aqr.com/Insights/Datasets)"
  - name: "Diversifizierte Multi-Horizont-Trendfolge (CTA-Stil; Hurst/Ooi/Pedersen 'Century of Evidence' + Live-Indizes SG Trend/BTOP50)"
    urteil: CANDIDATE
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 3
      regimestabilitaet: 3
      handelbarkeit: 5
      kapazitaet: 5
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.5
    netto_sharpe_erwartung: "0.2-0.4"
    kernrisiko: "Strukturelle Renditekompression seit ca. 2010: Netto-Performance hängt fast vollständig von wenigen Krisenjahren ab (2022 trägt den Großteil der kumulierten 2020-2025-Rendite); 2025 erneut zweistellig negativ (SG Trend YTD Aug. 2025: -9.3%). Charakter zunehmend 'Krisen-Versicherung' statt 'Alpha'; langes Flat-/Drawdown-Regime = reales Karriere-/Redemption-Risiko für Investoren und Manager."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "SG Trend Index (täglich, öffentlich, wholesale.banking.societegenerale.com); BTOP50 (barclayhedge.com); ETF-Proxies DBMF/KMLM/CTA (Yahoo Finance)"
  - name: "Kurzfristige / beschleunigte Trendfolge (verkürzte Lookback-Fenster, 'Speed'-Trend)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 1
      regimestabilitaet: 1
      handelbarkeit: 4
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "-0.1 bis 0.1"
    kernrisiko: "Crowding/Noise-Chasing: der von der Branche selbst berichtete Trend zu kürzeren Lookback-Fenstern (2015-2025) fällt zeitlich mit der schwächsten CTA-Performance-Periode zusammen; kein robustes ökonomisches Fundament jenseits reiner Geschwindigkeits-Arbitrage, die gegen HFT/Market-Maker-Kapital konkurriert."
    testbar_mit_freien_daten: ja
    freie_datenquelle: "Kontinuierliche Futures-Kurse (Stooq/Yahoo Finance), kurze Lookback-Fenster selbst konstruierbar; kein etablierter freier Referenzindex"
```

# Agent 16 – Zeitreihen-Momentum / Trendfolge (TSMOM, Managed-Futures-Stil)

**Mandat:** Unabhängige, adversariale Prüfung der Anomalieklasse "Zeitreihen-Momentum über Assetklassen" (12-Monats-Trendsignale auf liquide Futures, CTA-/Managed-Futures-Stil). Nullhypothese: Es gibt kein echtes Alpha in dieser Klasse. Stand: Juli 2026. Websuche war verfügbar und wurde für Kern-Fakten (Originalstudien-Kennzahlen, Kritikpapier, reale Index-Performance 2022-2025, CTA-Branchen-AUM) genutzt; einzelne Detailzahlen (insbesondere aus einer nicht direkt lesbaren Original-PDF) stammen aus Sekundärquellen/Aggregatoren und sind entsprechend gekennzeichnet.

---

## 0. Zusammenfassung des Urteils

Diese Anomalieklasse ist **nicht tot, aber deutlich geschwächter als die Gründungsliteratur suggeriert**. Es gibt drei zu unterscheidende Versionen:

1. **Das akademische Einzelsignal-TSMOM** (Moskowitz/Ooi/Pedersen 2012, "12M-Signum-Regel pro Instrument") ist statistisch fragiler als sein Ruf – eine direkte Replikations-/Kritikstudie (Huang/Li/Wang/Zhou 2020, *Journal of Financial Economics*) zeigt, dass die gepoolte Signifikanz der Originalstudie methodisch aufgebläht ist und die Strategie kaum von einer simplen "historischer Durchschnitt war positiv"-Regel zu unterscheiden ist. **Urteil: WEAK.**

2. **Die real gehandelte, diversifizierte Multi-Horizont-Trendfolge**, wie sie CTAs seit Jahrzehnten betreiben und wie sie in Live-Indizes (SG Trend Index, BTOP50) sowie in der Langzeitstudie Hurst/Ooi/Pedersen ("A Century of Evidence", 1880-2016) dokumentiert ist, hat die glaubwürdigste Post-Publication-Evidenz aller drei Kandidaten: jahrzehntelange, unabhängige, netto-von-Gebühren-Track-Records mit wiederkehrendem positivem Skew und "Crisis Alpha" (2008: positiv, während 60/40 kollabierte; 2022: SG Trend Index +27.3%, während Aktien und Anleihen zweistellig verloren). Gleichzeitig ist die Dekade 2010-2019 dokumentiert schwach ("Lost Decade"), und die aktuellste Evidenz (2023-2025) zeigt eine **erneute, nicht abgeschlossene Schwächephase** (SG Trend Index 2025 YTD bis August: -9.3%; BTOP50: -3.1%). Der Netto-Alpha-Charakter ist fragwürdig; plausibler ist eine Interpretation als **konvexe Krisenversicherung mit im Mittel niedriger, aber rechtsschiefer Prämie**. **Urteil: CANDIDATE** (schwach, mit erheblichen Vorbehalten – siehe unten).

3. **Kurzfristige/beschleunigte Varianten** (verkürzte Lookback-Fenster, die seit ca. 2015 als Branchentrend beschrieben werden) zeigen keine robuste ökonomische Begründung und fallen zeitlich mit der schwächsten Performance-Periode der Branche zusammen – ein klassisches Crowding-/Overfitting-Muster. **Urteil: KILL.**

---

## 1. Kandidat 1: Klassisches 12-Monats-TSMOM (Single-Signal, Moskowitz/Ooi/Pedersen 2012)

### 1a. Ökonomische Begründung

Die Originalstudie und die Folgeliteratur stützen sich auf drei sich ergänzende Mechanismen:

- **Underreaction / graduelle Informationsdiffusion:** In Modellen à la Hong/Stein (1999) diffundiert fundamentale Information langsam zwischen heterogenen, begrenzt rationalen Marktteilnehmern. Preise passen sich verzögert an, was zu positiver Autokorrelation über 1-12 Monate führt, gefolgt von Überreaktion und partieller Reversion über 12-36 Monate (dieses "Auf- und Abbauen" von Trends wird explizit in MOP 2012 dokumentiert).
- **Nicht-profitorientierte Gegenseite / Hedging-Nachfrage:** Kommerzielle Hedger (Ölproduzenten, Fluggesellschaften, Getreidefarmer, Goldminen) und Zentralbanken (FX-Interventionen, insbesondere in den 2000er/2010er Jahren bei EUR/CHF, JPY-Interventionen) transferieren Risiko ohne Gewinnmaximierungsmotiv und sind bereit, dafür eine Prämie zu zahlen. Spekulanten (inkl. Trendfolger), die diese Positionen übernehmen, vereinnahmen diese Prämie strukturell.
- **Slow-moving / gebundenes Kapital institutioneller Investoren:** Pensionsfonds und andere Großinvestoren rebalancieren nach Kalender-/Mandatslogik statt nach Preisinformation, was Kapitalflüsse erzeugt, die Trends verstärken, unabhängig von Fundamentaldaten.

### 1b. Limits to Arbitrage

- **Volatilität und Drawdown-Risiko begrenzen Fremdkapitaleinsatz:** TSMOM-Strategien benötigen i.d.R. Volatilitäts-Skalierung/Leverage, um auf Ziel-Sharpe zu kommen; das macht sie anfällig für Margin-Calls und Fremdkapitalgeber-Restriktionen genau in Stressphasen (prozyklische Deleveraging-Spiralen).
- **Patientes Kapital nötig, aber selten vorhanden:** Die Strategie erfordert das Aushalten mehrjähriger Flat-/Verlustphasen (siehe 1g), was einem Principal-Agent-Problem entspricht: Fondsmanager mit kurzfristigen Track-Record-Anreizen und Investoren mit kurzem Geduldshorizont schichten typischerweich nach 2-3 schlechten Jahren um – wodurch die Anomalie strukturell nicht "wegarbitriert" werden kann, weil das arbitragierende Kapital selbst prozyklisch abfließt.
- **Keine klassische "Short-die-teure-Seite"-Arbitrage möglich:** Da die Gegenseite (Hedger/Zentralbanken) nicht preissensitiv im klassischen Sinne handelt, gibt es keinen einfachen Mechanismus, der die Prämie kompetitiv wegarbitriert – gleichzeitig bedeutet das aber auch, dass die Prämie strukturell klein und volatil bleiben kann, ohne dass "billige" Arbitrage sie vergrößert.

### 1c. Originalstudien

**Moskowitz, Ooi, Pedersen (2012), "Time Series Momentum", Journal of Financial Economics 104, S. 228-250.**
- Stichprobe: 58 hochliquide Futures-Kontrakte (24 Commodities, 12 FX-Paare, 9 entwickelte Aktienindizes, 13 Staatsanleihen-Futures), Commodities teils ab 1965, Gesamtsample bis Dezember 2009.
- Kernbefund: 52 von 58 Instrumenten zeigen positive und bei 5%-Niveau signifikante Zeitreihen-Vorhersagbarkeit (12-Monats-Return sagt Vorzeichen des Folgemonats-Returns vorher).
- Diversifiziertes, volatilitätsskaliertes TSMOM-Portfolio (gemäß einer häufig zitierten Drittquellen-Replikation/Datenbank-Angabe, **nicht direkt aus dem Originaltext verifizierbar** – PDF-Extraktion schlug fehl): annualisiertes Alpha ca. 20.7% p.a. (Fama-French-adjustiert), Sharpe Ratio ≈ 1.31, Vol ≈ 15.7%, Max-Drawdown ≈ -34%, t-Statistik der Portfolio-Alpha ≈ 7.5. **Wichtig: Dies sind Brutto-Zahlen ohne realistische Kosten/Kapazitätsannahmen und stammen aus einer In-Sample-Periode, die von den Autoren selbst gewählt wurde.**
- Regressions-Alpha bei Kontrolle auf Standard-Faktoren: in 90% der Fälle positiv, davon 26% signifikant positiv, keiner der wenigen negativen Fälle signifikant.
- Strategie performt am besten in Extremmärkten (rechtsschiefe, "crisis-alpha"-artige Payoff-Struktur).

**Kritischer Kontrapunkt (siehe 1h):** Huang, Li, Wang, Zhou (2020) zeigen, dass die gepoolte t-Statistik der Originalstudie eine implizite Annahme identischer Alphas über alle 58 Assets voraussetzt – eine Annahme, die bei asset-by-asset-Tests nicht haltbar ist.

### 1d. Out-of-Sample- / Post-Publication-Evidenz

- Die unmittelbare Post-Publication-Dekade (2010-2019) war für klassische TSMOM-/CTA-Strategien eine dokumentierte "Lost Decade": Marktkommentare sprechen explizit von einer Periode, in der CTAs "nicht lieferten (aber auch nicht viel Schaden anrichteten)", verursacht durch beispiellose Zentralbank-Interventionen, die Volatilität und Trendbildung unterdrückten.
- Huang/Li/Wang/Zhou (2020, JFE 135, S. 774-794), "Time Series Momentum: Is It There?": Zeigen anhand asset-by-asset-Zeitreihenregressionen und Bootstrap-Verfahren (parametrisch und nichtparametrisch), dass die scheinbar hohe gepoolte t-Statistik der Originalstudie **unter den simulierten kritischen Werten liegt**, sobald korrekt für die implizite Annahme identischer Alphas kontrolliert wird. Ihr zentraler, für diese Klasse "vernichtender" Befund: **die Profitabilität der TSM-Strategie ist von einer Strategie, die auf dem historischen (erweiterten) Stichprobenmittelwert basiert, praktisch nicht zu unterscheiden** – d.h. ein Großteil des dokumentierten "Trendfolge-Alphas" könnte schlicht die (durch lange Bullenmärkte in Anleihen 1985-2020 und Aktien getriebene) positive Durchschnittsrendite der Long-Seite sein, nicht ein echter Autokorrelations-/Trendeffekt.
- Für einzelne Assets (u.a. S&P 500) finden Huang et al. **praktisch keine** signifikante Kurzfrist-Momentum-Evidenz in- wie out-of-sample.

### 1e. Kosten

- Ausführungskosten für die zugrundeliegenden liquiden Futures sind niedrig: Beispielrechnung E-Mini S&P 500 (ES): 1 Tick = 0.25 Indexpunkte = 12.50 USD auf ca. 280.000 USD Notional ≈ 0.04-0.05 Basispunkte pro Tick; 10-Year-T-Note-Future (ZN): 1 Tick ≈ 15.63 USD auf ca. 112.000 USD Notional ≈ 1.4 Bp; Crude Oil (CL): 1 Tick ≈ 10 USD auf ca. 68.000 USD Notional ≈ 1.5 Bp; Gold (GC): ≈ 0.3 Bp. Für ein diversifiziertes Multi-Asset-Buch liegen realistische Round-Trip-Kosten (Spread + Kommission) für die liquidesten Kontrakte typischerweise im Bereich von 1-10 Bp.
- **Rollkosten** kommen hinzu, da Futures-Positionen quartalsweise (Finanzkontrakte) bis monatlich (einige Commodities) gerollt werden müssen: zusätzlicher Spread-/Slippage-Aufwand pro Rollvorgang, geschätzt in der Größenordnung von wenigen bis ca. 15-20 Bp p.a. kumuliert für ein diversifiziertes Buch, in stark contangierten Commodity-Märkten (Öl, Erdgas, VIX-nahe Kontrakte) strukturell höher.
- Baltas/Kosowski ("Demystifying Time-Series Momentum Strategies", SSRN, Sample 1974-2013) untersuchen gezielt Turnover- und Kostentreiber (Volatilitätsschätzer, Handelsregeln) und finden, dass effizientere Signalkonstruktion Turnover und damit Rebalancing-Kosten signifikant senken kann – ein Hinweis, dass ein erheblicher Teil der Netto-Rendite-Erosion **implementierungsabhängig**, nicht strukturell unvermeidbar ist.
- **Management-/Performance-Gebühren realer CTAs** sind der eigentlich dominante Kosten-Faktor, nicht die Trading-Kosten: historisch "2-and-20", nach Gebührenkompression der letzten Dekade häufiger im Bereich 1-1.5% Management- plus 15-20% Performance-Fee. Bei einem angenommenen Brutto-Sharpe von 0.5-0.7 kann diese Gebührenstruktur den Netto-Sharpe um 0.2-0.4 senken – ein sehr großer Anteil der ohnehin schon moderaten Bruttoprämie. Die im Folgenden zitierten Indizes (SG Trend, BTOP50) sind bereits **netto** dieser Gebühren, was ihre schwache 2010-2025-Performance zusätzlich einordnet.

### 1f. Kapazität

- Baltas/Kosowski finden anhand zweier Methodologien **keine Evidenz für bindende Kapazitätsbeschränkungen** bis 2013, führen die 2008-2013-Schwäche stattdessen primär auf gestiegene Cross-Asset-Korrelationen (sinkender Diversifikationsnutzen) zurück.
- Da dieser Kandidat (Einzelsignal-Version) aber selten in Reinform in großem Volumen gehandelt wird (reale CTAs nutzen Multi-Horizont-Varianten, siehe Kandidat 2), ist die Kapazitätsfrage für die "reine" akademische Version letztlich nicht direkt am Markt getestet.

### 1g. Regimeabhängigkeit

- Bester dokumentierter Fall: Verhalten in Extremmärkten/Crashs (positiver Skew, siehe Kandidat 2 für Live-Zahlen).
- Schwächster Fall: Seitwärts-/Whipsaw-Regime mit häufigen Trendbrüchen – historisch v.a. 2011-2017 (Zentralbank-induzierte Niedrigvolatilität, politikgetriebene abrupte Reversals, insbesondere in FX). Ein 2014 veröffentlichter Branchenkommentar trug bereits den Titel "Observations on the Death of Trend Following" – ein früher Beleg dafür, dass die Karriererisiko-Problematik (siehe 1b) real und nicht nur theoretisch ist.

### 1h. Bekannte Kritik / Widerlegungen

- **Huang/Li/Wang/Zhou (2020)** ist die zentrale, im Mandat explizit genannte Widerlegung: Methodische Kritik an der gepoolten Regression, Nachweis der statistischen Nicht-Robustheit via Bootstrap, und die pointierte Reformulierung "TSM-Profitabilität ≈ Profitabilität einer Strategie basierend auf dem historischen Stichprobenmittelwert".
- Kritiker weisen zudem auf **Data-Mining-/Multiple-Testing-Risiken** hin: 58 Instrumente, viele mögliche Lookback-Fenster (die Literatur hat de facto 1, 3, 6, 12 Monate etc. getestet, bevor sich 12 Monate als "Standard" etablierte) – klassisches Multiple-Comparisons-Problem, das die MTK-adjustierte Signifikanz (score 2/5 oben) weiter senkt.
- Gegenposition (AlphaArchitect u.a.): Auch wenn die gepoolte Signifikanz überschätzt sei, bleibe die *ökonomische* Diversifikations- und Tail-Hedge-Eigenschaft der Strategie in der Praxis werthaltig – dies ist aber ein Portfolio-Konstruktions-Argument, kein Alpha-Argument, und wird daher separat unter Kandidat 2 bewertet.

**Fazit Kandidat 1: WEAK.** Die ökonomische Grundidee ist plausibel, aber die zentrale Originalstudie steht einer methodisch soliden, direkten Widerlegung in derselben Top-Journal-Reihe (JFE) gegenüber, die den Kernbefund (echte Autokorrelation vs. bloßer Durchschnittsrenditen-Effekt) explizit in Frage stellt. Reproduzierbarkeit und nachtestierte Signifikanz sind entsprechend niedrig anzusetzen.

---

## 2. Kandidat 2: Diversifizierte Multi-Horizont-Trendfolge (CTA-Stil; Hurst/Ooi/Pedersen "Century of Evidence" + Live-Indizes SG Trend/BTOP50)

Dies ist die Version, die tatsächlich von der 350-470-Mrd.-USD-CTA-Industrie gehandelt wird: mehrere Lookback-Fenster kombiniert, volatilitätsskaliert, über Dutzende bis Hunderte Instrumente diversifiziert.

### 2a. Ökonomische Begründung

Dieselben drei Mechanismen wie unter 1a (Underreaction, Hedging-Gegenseite, gebundenes institutionelles Kapital), zusätzlich verstärkt durch:
- **Zentralbank-Interventionen als explizit nicht-profitorientierte Gegenseite**, dokumentiert u.a. in FX-Märkten (2012 als besonders von Interventionen geprägt beschrieben, was TSMOM-FX-Signale kurzfristig "mean-reverting" statt trendfolgend erscheinen ließ – ein Beleg dafür, dass die Gegenseite real ist, aber ihr Verhalten sich über Zeit ändert und dadurch die Signalqualität schwankt).
- **Aggregation über viele unabhängige Lookback-Fenster und Assets** reduziert Idiosynkrasie-/Data-Mining-Risiko gegenüber Kandidat 1, da die Strategie nicht von einem einzelnen 12-Monats-Parameter abhängt.

### 2b. Limits to Arbitrage

Wie 1b, mit einem empirisch dokumentierten Zusatzpunkt: Steigende Cross-Asset-Korrelationen 2008-2013 (Baltas/Kosowski) zeigen, dass in Stressphasen genau der Diversifikationsnutzen zusammenbricht, den die Strategie braucht, um ihr Sharpe-Ratio zu erzielen – ein struktureller, nicht wegarbitrierbarer Effekt, da er aus dem gemeinsamen Krisenverhalten aller Marktteilnehmer entsteht, nicht aus einer korrigierbaren Fehlbepreisung.

### 2c. Originalstudien

**Hurst, Ooi, Pedersen (2017), "A Century of Evidence on Trend-Following Investing", Journal of Portfolio Management 44(1), S. 15-29** (AQR Capital, WP bereits 2012/2014 zirkuliert).
- Stichprobe: 67 Märkte (29 Commodities, 11 Aktienindizes, 15 Anleihemärkte, 12 FX-Paare), Januar 1880 – Dezember 2016 – **explizit als Erweiterung/Robustheitstest der MOP-2012-Stichprobe um mehr als 100 Jahre konzipiert**.
- Kernbefund: In jeder Dekade seit 1880 positive durchschnittliche Trendfolge-Rendite; durchschnittlicher Sharpe Ratio über alle Märkte ≈ 0.4 (deutlich niedriger als die für Kandidat 1 zitierte 1.31 – bereits ein erstes Warnsignal, dass die MOP-2012-Zahl mit hoher Wahrscheinlichkeit optimistisch/In-Sample-verzerrt war).
- Trendfolge lieferte positive Renditen in 8 von 10 der größten historischen Drawdown-Perioden eines 60/40-Portfolios – die empirische Basis des "Crisis Alpha"-Arguments.
- **Wichtiger Interessenkonflikt-Hinweis:** Alle drei Autoren sind/waren bei AQR Capital Management tätig, einem der größten kommerziellen Anbieter von Trendfolge-/Managed-Futures-Produkten. Dies ist keine unabhängige Drittstudie, sondern (teilweise) Eigenmarketing eines Anbieters – die Ergebnisse sind entsprechend mit einem Discount zu versehen, auch wenn die Methodik in einem Peer-Review-Journal veröffentlicht wurde.

### 2d. Out-of-Sample- / Post-Publication-Evidenz (Kernstück der Bewertung)

Reale, netto-von-Gebühren Live-Track-Records liefern hier die aussagekräftigste (weil am wenigsten manipulierbare) Evidenz:

- **SG Trend Index** (Societe Generale, gleichgewichtete Top-10-Trendfolge-CTAs, öffentlich, täglich):
  - **2022: +27.3%** (Rekordjahr) – während Aktien und Anleihen gleichzeitig zweistellig verloren; getragen v.a. durch Zins-, FX- und Energie-Trends. Das Kern-"Crisis-Alpha"-Beispiel der letzten Dekade.
  - **2024: +2.4%** – nahezu flach trotz gutem Jahresstart; Trend Indicator (kürzere Signale) lag zeitweise fast 8% hinter dem Trend Index zurück, Zeichen für hohe Streuung zwischen Managern (Pairwise-Korrelation der Konstituenten 2024: 0.78, aber Return-Spread zwischen ihnen ~15%).
  - **2025 (YTD bis August): -9.3%** (SG Trend Index) bzw. -9.0% bis -9.4% (weitere Trend-Indizes wie der TTU-Trend-Following-Index); **BTOP50 (breiter diversifiziert): -3.1% YTD**. April 2025 wird explizit als einer der härtesten Monate des Jahres beschrieben (Korrelationsbrüche, abrupte Reversals). Eine leichte Erholung ab Sommer 2025 (+2.3% im August) ändert am negativen Jahressaldo wenig.
  - 2023: gemischt/leicht negativ (punktuelle Quelle: SG-CTA-Subindex YTD bis August 2023 bei -1.3%; vollständige Jahreszahl nicht zweifelsfrei verifizierbar aus den vorliegenden Quellen – **hier Unsicherheit explizit gekennzeichnet**).
  - **Netto-Einordnung 2020-2025:** Der weit überwiegende Teil der kumulierten Rendite dieser sechs Jahre stammt aus dem einen Jahr 2022. Ohne 2022 wäre die Periode netto in etwa flach bis leicht negativ – ein zentraler adversarialer Befund gegen ein "stetiges Alpha"-Narrativ und für ein "seltene-Großereignisse-Versicherung"-Narrativ.
- **BTOP50 Index** (breiter, Barclay/BarclayHedge, seit 1987, replizierbar-gewichtet nach AUM der größten CTAs): Dokumentiert dieselbe "Lost Decade" 2011-2019 mit Flat-bis-leicht-negativer Performance und großen historischen Drawdowns; in der Literatur explizit auf beispiellose Zentralbank-Interventionen zur Volatilitätsdämpfung zurückgeführt. Vor 2010 (inkl. TMT-Crash und GFC 2008) war BTOP50 hingegen der Top-Performer unter Diversifikatoren, da es beide großen Drawdown-Perioden vermied und 2008/09 positiv abschloss.
- **CTA-Branchen-AUM** ist selbst ein Stück Post-Publication-Evidenz: von einer früheren Schätzung um 348 Mrd. USD auf ca. 472 Mrd. USD Ende 2023 gewachsen (+15% ggü. Vorjahr) – das zeigt reales, bei institutionellen Investoren verankertes Vertrauen trotz der schwachen 2010er-Dekade, aber auch ein erhebliches Rückschlagsrisiko (Mittelabflüsse), sollte die 2023-2025-Schwächephase anhalten.
- **Bezug zur Huang/Li/Wang/Zhou-Kritik:** Deren Kernaussage ("TSM ≈ historischer Durchschnitt") lässt sich hier nicht direkt anwenden, weil Live-Indizes keine reine Backtest-Konstruktion sind, sondern tatsächlich gehandeltes, gebührenbelastetes Kapital abbilden. Das entkräftet die Kritik aber nicht vollständig – es verschiebt sie nur: Die reale Netto-Performance ist niedriger und volatiler als MOP-2012 suggeriert, was in dieselbe Richtung wie die Kritik zeigt (überzeichnetes Alpha in der Originalstudie).

**Decay-Schätzung:** Aus dem verfügbaren Material lässt sich ein grober Decay konstruieren: Hurst/Ooi/Pedersen-Sharpe (Langzeit-Durchschnitt 1880-2016) ≈ 0.4; MOP-2012-Sharpe (1985-2009, In-Sample-lastig) ≈ 1.3 (brutto); reale Netto-Sharpe der Live-Indizes seit 2010 dürfte, grob geschätzt aus den oben zitierten Jahresrenditen (ein sehr gutes Jahr 2022, mehrere Flat-/Negativ-Jahre), eher im Bereich 0.1-0.3 liegen. Das impliziert einen **Decay von Backtest zu echter Netto-Live-Performance in der Größenordnung von 60-80%** – eine sehr konservative, aber durch mehrere unabhängige Linien (Century-Paper-Sharpe von 0.4 vs. MOP-Sharpe von 1.3, sowie die Jahres-für-Jahr-Live-Zahlen) gestützte Schätzung.

### 2e. Kosten

Wie unter 1e beschrieben: Ausführungskosten pro Trade niedrig (Basispunkt-Bereich für liquide Kontrakte), Rollkosten moderat, aber die **Gebührenstruktur realer CTA-Vehikel ist der dominante Kostenfaktor**. Wichtig: Die oben zitierten SG-Trend- und BTOP50-Zahlen sind bereits Netto-Zahlen (nach Management- und Performance-Fees der zugrundeliegenden Fonds) – die schwache 2023-2025-Performance ist also nicht durch "wir haben die Gebühren vergessen" erklärbar, sondern eine reale Investorenerfahrung.

### 2f. Kapazität und Handelbarkeit

- **Nachweislich hoch:** CTA-Branchen-AUM von ca. 350-470 Mrd. USD, gehandelt über hochliquide, börsennotierte Futures (Aktienindizes, Staatsanleihen, G10-FX, große Commodities) – die liquidesten Instrumente der globalen Kapitalmärkte.
- Baltas/Kosowski finden bis 2013 keine Evidenz für bindende Kapazitätsgrenzen; angesichts des seitherigen AUM-Wachstums ohne öffentlich dokumentierten "Kapazitätskollaps" ist dieser Befund nicht klar widerlegt, aber auch nicht unabhängig für die 2020er aktualisiert worden.
- Handelbarkeit exzellent: Long/Short ohne Leerverkaufsbeschränkungen, enge Spreads, hohe Markttiefe, tägliche Liquidität in Futures.
- Für externe Retail-/kleinere institutionelle Investoren zusätzlich über liquide ETF-Proxies zugänglich (DBMF, KMLM, CTA/Simplify Managed Futures Strategy ETF) – ein weiteres Stück "gelebter", nicht nur theoretischer Handelbarkeit.

### 2g. Regimeabhängigkeit

- **Positiver Skew / Crisis Alpha, empirisch belegt:** 2008 (GFC, positiv während 60/40 kollabierte), 2020 (COVID-Crash-Diversifikation), 2022 (SG Trend Index +27.3%, während klassische 60/40-Portfolios zweistellig verloren) – 8 von 10 der größten historischen 60/40-Drawdowns laut Hurst/Ooi/Pedersen mit positiver Trendfolge-Rendite.
- **Whipsaw-/Flat-Regime, ebenfalls empirisch belegt:** 2011-2019 ("Lost Decade", zentralbankgetriebene Volatilitätsunterdrückung), erneut 2023-2025 (dokumentierte zweistellige Verluste 2025 YTD, Korrelationsbrüche und "violent reversals" im April 2025).
- **Langer flacher Zeitraum als Karriererisiko:** Sowohl 2011-2019 als auch 2023-2025 zeigen, dass dieses Risiko nicht hypothetisch, sondern wiederkehrend real ist – Branchentitel wie "Observations on the Death of Trend Following" (2014) und aktuelle Berichte über Mittelabflüsse/Strategie-Anpassungen (Verkürzung der Lookback-Fenster, siehe Kandidat 3) sind direkte Symptome dieses Drucks.
- Ein zusätzlicher, in der Literatur genannter Struktur-Befund: Trend-Following-Performance ist "am robustesten in lang anhaltenden Krisen, gemischt bei Aktienkorrekturen, tendenziell negativ bei Anleihe-Marktkorrekturen" – die Diversifikationseigenschaft ist also selbst regimeabhängig und nicht garantiert (z.B. 2022 war für 60/40 auch ein Anleihe-Crash-Jahr, und dennoch profitierte Trendfolge – ein Gegenbeispiel zur eigenen Verallgemeinerung, das zeigt, wie heterogen die Evidenz je nach Krisentyp ist).

### 2h. Bekannte Kritik / Widerlegungen

- Interessenkonflikt der Century-Studie (AQR-Autoren, siehe 2c).
- Survivorship-/Konstruktions-Caveats bei CTA-Indizes: SG Trend Index wird jährlich neu auf die zehn größten, für neue Investments offenen Trendfolge-CTAs zusammengesetzt – das ist kein reines Survivorship-Bias-Problem (Auswahl nach Größe, nicht nach Performance), kann aber Selektionseffekte einführen (nur die überlebensfähigsten/größten Manager werden überhaupt aufgenommen).
- Grundsätzliche Huang/Li/Wang/Zhou-Kritik bleibt im Hintergrund relevant: Auch wenn sie sich direkt auf die MOP-2012-Konstruktion bezieht, untergräbt sie das Vertrauen in die statistische Reinheit des zugrunde liegenden Signals, das auch CTAs in modifizierter Form nutzen.
- Ein Teil der Branche selbst zweifelt öffentlich am Konzept ("Trend following is dead"-Artikel, 2025) – ein Symptom, kein Beweis, aber es zeigt, dass die Selbstzweifel innerhalb der Praktiker-Community real und aktuell sind.

**Fazit Kandidat 2: CANDIDATE** (schwach, mit Vorbehalt). Begründung für "CANDIDATE" statt "WEAK": (i) über 140 Jahre und Dutzende unabhängige Manager dokumentierte, wiederkehrende positive Schiefe in echten Krisen – ein Muster, das schwer allein durch Data-Mining zu erklären ist; (ii) nachweislich hohe, real absorbierte Kapazität (350-470 Mrd. USD); (iii) niedrige, gut quantifizierbare Ausführungskosten. Der Vorbehalt: Die Netto-Sharpe-Erwartung ist mit 0.2-0.4 sehr moderat, die jüngste Post-Publication-Evidenz (2023-2025) ist überwiegend negativ, und der Charakter der Strategie ist eher "seltene, aber wertvolle Krisenversicherung" als "verlässliches laufendes Alpha" – ein Unterschied, der für die Portfoliokonstruktion wichtig, für eine reine Alpha-Wette aber ein Warnsignal ist.

---

## 3. Kandidat 3: Kurzfristige / beschleunigte Trendfolge ("Speed"-Trend, verkürzte Lookback-Fenster)

### 3a. Ökonomische Begründung

Schwach: Das Argument lautet im Kern, dass kürzere Lookback-Fenster (Wochen statt Monate) schneller auf Trendwechsel reagieren und so Whipsaw-Verluste der klassischen 12-Monats-Signale vermeiden sollen. Es fehlt jedoch eine überzeugende strukturelle Begründung, warum eine nicht-profitorientierte Gegenseite (Hedger, Zentralbanken) systematisch auf so kurzen Horizonten vorhersagbares Verhalten zeigen sollte – auf diesen Zeitskalen dominieren typischerweise Marktmikrostruktur-Effekte und algorithmisches/HFT-Handeln, gegen das ein CTA im Geschwindigkeitswettbewerb strukturell im Nachteil ist.

### 3b. Limits to Arbitrage

Kaum vorhanden in klassischem Sinne – dies ist eher ein Feld, in dem Kapitalstärke und technologische Infrastruktur (Kolokation, Ausführungsqualität) entscheiden, was tendenziell gegen "Limits to Arbitrage" als schützenden Mechanismus für Nicht-HFT-Akteure spricht.

### 3c. Originalstudien

Keine eigenständige, breit anerkannte Originalstudie in derselben Kategorie wie MOP 2012 oder Hurst/Ooi/Pedersen 2017; es handelt sich um eine in der Praxis beobachtete Weiterentwicklung/Modifikation, dokumentiert eher in Branchenkommentaren als in Peer-Review-Journalen.

### 3d. Out-of-Sample-Evidenz

Die verfügbare Evidenz ist indirekt, aber bemerkenswert: Marktbeobachter (Top Traders Unplugged, 2025) beschreiben explizit einen "branchenweiten Trend zu kürzeren Lookback-Fenstern, da Geschwindigkeit in der letzten Dekade in Mode gekommen ist", verbunden mit der Einschätzung, dass Trader dadurch "zunehmend mit Rauschen statt Signal" konfrontiert sind – als einer der genannten Gründe für die enttäuschende CTA-Performance 2025. Das ist ein seltener Fall, in dem eine Strategie-Anpassung zeitlich mit einer Verschlechterung der Ergebnisse zusammenfällt und von Praktikern selbst als Fehlerquelle benannt wird.

### 3e. Kosten

Höher als bei Kandidat 1/2: kürzere Lookback-Fenster bedeuten höheren Turnover, mehr Rollvorgänge/Rebalancing, höhere kumulierte Spread-/Slippage-Kosten – bei gleichzeitig kleinerem, unsichererem Signal.

### 3f. Kapazität

Niedriger: Konkurriert direkt mit HFT- und Market-Making-Kapital auf denselben kurzen Zeitskalen, wodurch die effektiv nutzbare Kapazität für CTA-Größenordnungen begrenzter ist als bei der klassischen 12-Monats-Variante.

### 3g. Regimeabhängigkeit

Keine belastbare eigene Evidenz für stabile Regimes; die verfügbare Evidenz deutet eher auf erhöhte Fragilität in genau den volatilen, korrelationsbrechenden Phasen (z.B. April 2025), die für längerfristige Trendfolge noch am ehesten profitabel wären.

### 3h. Bekannte Kritik

Die Selbstkritik der Branche ("Geschwindigkeit ist Mode geworden, aber es ist Rauschen, kein Signal") ist bereits die schärfste verfügbare Widerlegung und deckt sich mit dem klassischen Crowding-Argument: Wenn viele CTAs gleichzeitig auf kürzere Fenster wechseln, verstärkt das genau die Korrelationsbrüche und abrupten Reversals, unter denen die gesamte Klasse 2025 gelitten hat.

**Fazit Kandidat 3: KILL.** Kein robustes ökonomisches Fundament, keine eigenständige Originalstudie mit dokumentierter Effektgröße, und die verfügbare Evidenz deutet eher auf einen Crowding-/Noise-Chasing-Effekt hin als auf eine eigenständige Anomalie.

---

## 4. Vergleichstabelle

| Kriterium | Kandidat 1 (Single-Signal TSMOM) | Kandidat 2 (Diversifizierte Multi-Horizont/CTA) | Kandidat 3 (Speed-Trend) |
|---|---|---|---|
| Originalstudie | Moskowitz/Ooi/Pedersen 2012 | Hurst/Ooi/Pedersen 2017 + Live-Indizes | keine anerkannte |
| Sample | 58 Futures, 1965/1985-2009 | 67 Märkte, 1880-2016 + Live seit 1987 (BTOP50) | branchenintern, undokumentiert |
| Zentrale Gegenevidenz | Huang/Li/Wang/Zhou 2020 (JFE) | 2010-2019 "Lost Decade", 2023-2025 erneut negativ | 2025-CTA-Schwäche, Crowding |
| Bestes Jahr (Beispiel) | – (Backtest) | 2022: SG Trend Index +27.3% | – |
| Schwächstes dokum. Jahr | – | 2025 YTD (Aug.): SG Trend -9.3% | – |
| Urteil | WEAK | CANDIDATE (schwach) | KILL |

---

## 5. Gesamtfazit zur Nullhypothese

Die Nullhypothese "kein echtes Alpha" lässt sich für diese Klasse **nicht vollständig verwerfen, aber auch nicht mit der in der Gründungsliteratur suggerierten Stärke bestätigen**. Das ehrlichste Bild:

- Es gibt eine **schwache, aber über 140+ Jahre und viele unabhängige Live-Manager wiederkehrende Tendenz** zu positiver Schiefe in extremen Marktphasen (2008, 2022) – dies ist die stärkste verfügbare Evidenz für einen echten, nicht-arbitrierten Effekt, am ehesten erklärbar durch strukturelle Hedging-Nachfrage nicht-profitorientierter Akteure.
- Die **statistische Signifikanz der Gründungsstudie ist durch eine methodisch überzeugende Direktkritik (Huang/Li/Wang/Zhou 2020) erheblich geschwächt** – ein seltener Fall, in dem eine "Killer-Studie" tatsächlich in derselben Top-Journal-Reihe wie das Original erschienen ist.
- Die **reale, netto-von-Gebühren Performance seit Publikation ist deutlich schwächer und volatiler** als die Originalpapiere suggerieren (Decay-Schätzung 60-80% ggü. MOP-2012-Sharpe), mit zwei dokumentierten mehrjährigen Schwächephasen (2011-2019 und 2023-2025) und einem stark konzentrierten Renditebeitrag aus einzelnen Krisenjahren.
- **Kosten und Kapazität sind nicht das Kernproblem** dieser Klasse (Futures-Handel ist günstig, Kapazität nachweislich hoch bei 350-470 Mrd. USD Branchen-AUM) – das Kernproblem ist die **Regimeabhängigkeit und das daraus resultierende Karriere-/Redemption-Risiko**, das strukturell verhindert, dass Kapital lange genug geduldig bleibt, um die seltenen guten Jahre "auszusitzen".
- Die **Erwartung für ein neues, aus dieser Klasse abgeleitetes Signal sollte konservativ sein**: eine realistische Netto-Sharpe-Erwartung von 0.2-0.4, verbunden mit erheblicher Pfadabhängigkeit (der Großteil der Rendite kommt aus wenigen Jahren) und einem Diversifikations-/Tail-Hedge-Nutzen, der wertvoller sein kann als der reine Sharpe-Beitrag suggeriert – aber das ist ein Portfoliokonstruktions-Argument, kein reines Alpha-Argument.

---

## Quellen (Web-Recherche, Juli 2026)

- [Time series momentum – ScienceDirect (Moskowitz/Ooi/Pedersen 2012, JFE)](https://www.sciencedirect.com/science/article/pii/S0304405X11002613)
- [Time Series Momentum Effect – Quantpedia](https://quantpedia.com/strategies/time-series-momentum-effect)
- [Time Series Momentum: Original Paper Data – AQR](https://www.aqr.com/Insights/Datasets/Time-Series-Momentum-Original-Paper-Data)
- [A Century of Evidence on Trend-Following Investing – SSRN (Hurst/Ooi/Pedersen)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2993026)
- [A Century of Evidence on Trend-Following Investing – AQR](https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing)
- [Time-Series Momentum: Is It There? – SSRN (Huang/Li/Wang/Zhou)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3165284)
- [Time series momentum: Is it there? – ScienceDirect (JFE 2020)](https://www.sciencedirect.com/science/article/abs/pii/S0304405X19301953)
- [Time Series Momentum: Theory and Evidence – AlphaArchitect](https://alphaarchitect.com/2020/06/time-series-momentum-theory-and-evidence/)
- [Are Trend-Following and Time-Series Momentum Research Results Robust? – AlphaArchitect](https://alphaarchitect.com/are-trend-following-and-time-series-momentum-research-results-robust/)
- [Demystifying Time-Series Momentum Strategies – Baltas/Kosowski (CME/SSRN)](https://www.cmegroup.com/education/files/demystifiing-time-series-momentum-strategies.pdf)
- [Momentum Strategies in Futures Markets and Trend-following Funds – Baltas/Kosowski](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1968996)
- [Keeping up with the Trend-Followers – SG Markets, 2025](https://content.sgmarkets.com/CTA_UPDATE_KEEPING_UP_WITH_THE_TRENDFOLLOWERS_2025)
- [Steady Trends: The Reality of CTA Return Dispersion – CFM](https://www.cfm.com/steady-trends-the-reality-of-cta-return-dispersion/)
- [Is Trend really having a bad year? – CFM](https://www.cfm.com/is-trend-really-having-a-bad-year/)
- [SG Trend Index – BarclayHedge Indices](https://portal.barclayhedge.com/cgi-bin/indices/displayHfIndex.cgi?indexCat=SG-Prime-Services-Indices&indexName=SG-Trend-Index)
- [BTOP50 Index – BarclayHedge Indices](https://portal.barclayhedge.com/cgi-bin/indices/displayHfIndex.cgi?indexCat=Barclay-Investable-Benchmarks&indexName=BTOP50-Index)
- [Trend followers turn leaders as CTAs deliver record returns in 2022 – Hedgeweek](https://www.hedgeweek.com/trend-followers-turn-leaders-ctas-deliver-record-returns-2022/)
- [Trend Following Performance Report — April, 2025 – Top Traders Unplugged](https://www.toptradersunplugged.com/trend-following-performance-report-april-2025/)
- [Trend Following Performance Report — August, 2025 – Top Traders Unplugged](https://www.toptradersunplugged.com/trend-following-performance-report-august-2025/)
- [CTAs and trend-following hedge funds fight back after H1 rout – Alternatives Watch](https://www.alternativeswatch.com/2025/09/02/ctas-trend-following-hedge-funds-rebound-h1-rout-societe-generale-indices/)
- [Mixed CTA Performance as Traditional Trend-Followers Lead – HedgeNordic](https://hedgenordic.com/2025/02/mixed-cta-performance-as-traditional-trend-followers-lead/)
- [Bringing Back "Crisis Alpha" – HedgeNordic](https://hedgenordic.com/2023/03/bringing-back-crisis-alpha/)
- [Reflections on Ten Years in Trend Following – Kaminski, AlphaSimplex](https://www.alphasimplex.com/assets/files/2020.09---10-years-of-trend-following---kaminski.pdf)
- [Go Skew Yourself with Managed Futures – AlphaArchitect](https://alphaarchitect.com/go-skew-yourself-with-managed-futures/)
- [Observations On the Death of Trend Following – IASG, 2014](https://www.iasg.com/blog/2014/03/18/observations-death-trend-following)
- [CTA Industry Assets Under Management – ION Analytics/BarclayHedge](https://ionanalytics.com/barclayhedge/solutions/assets-under-management/cta-industry-assets-under-management/)

**Hinweis zur Evidenzqualität:** Ein direkter PDF-Abruf der Originalstudie (NYU Stern, Moskowitz/Ooi/Pedersen) schlug technisch fehl (nicht lesbares Binärformat); die unter 1c zitierten Detailkennzahlen (Alpha 20.7%, Sharpe 1.31, t=7.55) stammen aus einer Drittquellen-Replikation (Quantpedia) und sind als **nicht letztgültig verifiziert** zu kennzeichnen. Die 2023-Jahresrendite des SG Trend Index konnte nicht zweifelsfrei aus den verfügbaren Quellen ermittelt werden. Alle übrigen zentralen Zahlen (2022, 2024, 2025-YTD SG Trend/BTOP50, Huang/Li/Wang/Zhou-Kernaussage, CTA-AUM) stützen sich auf mehrere konsistente, unabhängige Web-Quellen.
