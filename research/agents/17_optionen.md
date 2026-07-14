```yaml
agent: 17
klasse: "Optionsanomalien (VRP/VIX-Carry/Put-Writing)"
websuche_verfuegbar: ja
strategien:
  - name: "Equity Variance Risk Premium (Short-Vol via Delta-Hedged Optionen / Variance Swaps, Carr & Wu 2009 / Bakshi & Kapadia 2003)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 3
      kapazitaet: 3
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.3
    netto_sharpe_erwartung: "0.2-0.5 (long-run, vor Tail-Event), episodisch stark negativ"
    kernrisiko: "Linksschiefes Tail-Risiko: Verlust an einem einzigen Tag (Feb 2018, Mrz 2020) kann 2-5 Jahre kumulierter Prämie auslöschen; Peso-Problem in Backtests"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "CBOE PUT/BXM/BXMD-Indizes (öffentlich), CBOE VIX-Index-Historie, Yahoo Finance ^VIX/^GSPC, OptionMetrics falls verfügbar (nicht frei)"
  - name: "VIX-Terminstruktur-Carry (Contango-Roll, short VIX-Futures/kurzlaufende ETPs)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 1
      handelbarkeit: 3
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.25
    netto_sharpe_erwartung: "0.3-0.6 vor Crash-Perioden, langfristig durch Crash-Cluster auf ~0.1-0.3 gedrückt"
    kernrisiko: "Backwardation-Spikes (Vol-of-Vol-Explosion): XIV verlor -96% an einem Tag (5. Feb 2018), Totalverlust-Risiko bei gehebelten/inversen ETPs"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "CBOE VIX Futures/Term-Structure-Historie, CFE-Settlementdaten, Yahoo Finance (VXX, SVXY) Kurshistorie"
  - name: "Dispersion Trading / Correlation Risk Premium (short Index-Implied-Correlation vs. long Einzelaktien-Vol)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.4
    netto_sharpe_erwartung: "0.3-0.6 brutto, nach breiten Bid/Ask-Spreads und Rebalancing-Kosten deutlich niedriger, evtl. <0.2 netto"
    kernrisiko: "Korrelations-Spikes in Makro-Schocks (2008, 2020, 2022); Deng (2008) zeigt Sharpe-Kollaps von 1.2 (1996-2000) auf -0.17 (post-2000) - starkes Post-Publication-Decay-Signal"
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
```

# Optionsanomalien: Variance Risk Premium, VIX-Carry, Put-Writing, Dispersion
## Bericht Agent 17 — Juli 2026

Evidenzbasis: WebSearch/WebFetch waren in dieser Session funktionsfähig und wurden für aktuelle (2023-2026) Evidenz genutzt. Ergänzt durch internes Wissen, Stand Anfang 2026, wo Suchergebnisse lückenhaft waren (v.a. exakte t-Statistiken der Originalstudien, die hinter Paywalls liegen).

---

## 0. Nullhypothesen-Rahmen und zentrale Antwort vorweg

**Ist Short-Vol eine Ineffizienz oder eine Versicherungsprämie mit katastrophalem Tail?**

Nach Durchsicht der Literatur und aktueller Evidenz: **überwiegend Letzteres, mit abnehmender Prämiengröße**. Die Variance Risk Premium (VRP) ist ökonomisch am besten als kompensierte Risikoprämie für das Underwriting von Crash-Versicherung zu verstehen — keine reine Ineffizienz im Sinne von "kostenloses Geld liegt auf der Straße". Die entscheidende neue Evidenz (Chicago Fed Working Paper 2025-17, "The Decline of the Variance Risk Premium: Evidence from Traded and Synthetic Options") zeigt explizit: Über die letzten 15 Jahre sind Options-Alphas von "scharf negativ" zu "nicht mehr von Null unterscheidbar" gesunken. Das Paper argumentiert mit einem intermediär-basierten Modell, dass die historisch negativen Renditen gehandelter Optionen primär Intermediär-Friktionen/Kapitalkosten widerspiegelten (nicht reine Investoren-Präferenz für Crash-Versicherung) — und dass genau diese Friktionen durch den Vol-Selling-Boom, mehr Marktmacher-Kapazität und liquidere Absicherungsmärkte weggehandelt wurden. Das ist im Kern die Post-Publication-Decay-Geschichte dieser gesamten Anomalieklasse.

---

## 1. Kandidat 1: Equity Variance Risk Premium (VRP) — Bakshi/Kapadia (2003), Carr/Wu (2009)

### a) Ökonomische Begründung
Strukturelle Käufer von Volatilitäts-/Crash-Versicherung: (i) Pensionsfonds und Versicherer mit expliziten Tail-Hedging-Mandaten, (ii) Retail-Anleger, die Put-Optionen zur Portfolioabsicherung kaufen (dokumentierte systematische Overpaying-Neigung, "Lottery-Preference" für Puts), (iii) strukturierte Produkte/Autocallables, die Long-Vega-Exposure institutioneller Emittenten erzeugen, (iv) Risk-Parity- und Vol-Targeting-Fonds, die in Stressphasen prozyklisch Absicherung/Deleveraging nachfragen. Verkäufer/Prämien-Einsammler: Marktmacher (die die Prämie über Delta-Hedging vereinnahmen, aber Gamma-/Vega-Risiko tragen), spezialisierte Vol-Seller-Fonds (Put-Writing-Funds, "Alt-Risk-Premia"-Strategien), und seit ca. 2016-2018 ein stark gewachsenes Segment systematischer Retail-/RIA-Strategien (0DTE-Credit-Spreads, Covered-Call-ETFs wie JEPI/QYLD).

### b) Limits to Arbitrage
- Margin: Nackte Short-Optionen/Short-Varianz-Positionen erfordern hohe, im Crash prozyklisch steigende Margin (Reg-T/Portfolio-Margin-Spikes genau dann, wenn Liquidität am knappsten ist).
- Tail-Risiko: Verteilung ist extrem linksschief — die Strategie verliert selten, aber wenn, dann in Vielfachen der kumulierten Prämie eines gesamten Jahres oder mehrerer Jahre (siehe Abschnitt g).
- Kapitalkosten nach Crashes: Nach Feb 2018 und März 2020 haben Prime Broker und Clearinghäuser (OCC) die Margin-Anforderungen für Short-Vol-Strukturen strukturell erhöht; viele dedizierte Vol-Seller-Fonds (z.B. LJM Preservation and Growth Fund, -80% im Feb 2018) wurden liquidiert bzw. verloren ihre Investorenbasis dauerhaft — Kapital, das eine Ineffizienz arbitrieren könnte, verschwindet exakt dann, wenn die Prämie (kurzfristig) am höchsten ist.

### c) Originalstudien
- **Bakshi & Kapadia (2003)**, *Review of Financial Studies* 16(2), 527-566: Delta-gehedgte Gewinne aus S&P-500-Index-Calls sind systematisch negativ ("underperforms zero"), Effekt stärker bei ATM-Optionen als bei OTM, stärker in Hochvolatilitätsphasen. Interpretation: negative Marktpreis für Volatilitätsrisiko. Ergebnis robust über verschiedene Substichproben 1988-1995.
- **Carr & Wu (2009)**, *Review of Financial Studies* 22(3), 1311-1341: Modellfreie Konstruktion synthetischer Varianz-Swap-Sätze aus Optionsportfolios; Differenz zu realisierter Varianz = VRP. Für S&P 500 und S&P 100 sowie DJIA ist die durchschnittliche Varianzrisikoprämie **stark negativ und statistisch signifikant** (die Autoren berichten für die Indizes hochsignifikante negative Mittelwerte; für die meisten der 35 untersuchten Einzelaktien ist der Effekt dagegen statistisch schwächer/uneindeutig — ein wichtiger Cross-Sectional-Befund: der Effekt ist ein *Index*-Phänomen, kein generisches Aktien-Phänomen, was zur Korrelationsrisikoprämien-Interpretation passt, siehe Kandidat 3).
- **CBOE PUT-Index (seit 1986 investierbar nachgebildet)**: Über die vollen ~32+ Jahre Historie zeigen BXM/BXMD/PUT laut CBOE-eigenen Publikationen einen um ca. 46% höheren Sharpe Ratio als der S&P 500 bei deutlich niedrigerer Volatilität — aber mit ausgeprägter negativer Schiefe und höherer Kurtosis (Stutzer-Index und Sortino-Ratio bleiben trotzdem günstig, weil die Häufigkeit der großen Verluste gering ist). Dies ist die "praktische" Bestätigung des akademischen Befunds: Prämie ist real, aber mit Tail-Preis.

### d) Out-of-Sample-/Post-Publication-Evidenz (2010-2026) — der entscheidende Teil
- **Chicago Fed WP 2025-17** (Sept. 2025): Über die letzten 15 Jahre (~2010-2025) sind Options-Alphas ("option returns beyond risk compensation") von deutlich negativ auf **statistisch nicht mehr von Null unterscheidbar** gesunken. Das ist der direkteste verfügbare Beleg für Decay der gehandelten VRP.
- **Vol-Selling-Boom seit ca. 2012-2017**: massives Wachstum von XIV/SVXY/kurzfristigen inversen VIX-ETPs, systematischen Put-Writing-Funds und in-house Vol-Selling-Desks bei Banken. Geschätztes AUM in kurz-Vol-Strategien stieg auf mehrere hundert Milliarden USD Notional-Exposure bis Anfang 2018 — klassisches Crowding-Signal.
- **Volmageddon (5. Feb 2018)**: VIX stieg um +115,6% an einem Tag (17,31 → 37,32), der größte prozentuale Tagesanstieg der VIX-Historie. **XIV verlor -96% in einer einzigen Sitzung** und wurde am Folgetag von Credit Suisse liquidiert; SVXY (1x) verlor >80%; LJM-Fonds -80%. Dieses Ereignis allein hat mehrere Jahre kumulierter Prämie einer breiten Kohorte von Short-Vol-Strategien ausgelöscht und zu einer strukturellen Marktbereinigung geführt (Rückgang der ETP-Notional-Exposure um Größenordnung 90%+).
- **COVID-Crash März 2020**: S&P 500 -33,9% in 5 Wochen (19. Feb - 23. März), VIX auf 82,7 (Rekordhoch, übertraf sogar 2008). Short-Vol- und Put-Writing-Strategien erlitten erneut zweistellige bis extreme Drawdowns; anders als 2018 keine vollständige Produktauslöschung, aber erneute Bestätigung des Tail-Musters, diesmal mit deutlich größerer absoluter Marktbewegung.
- **0DTE-Ära seit 2022**: SPX-0DTE-Optionsvolumen stieg auf durchschnittlich >1,23 Mio. Kontrakte/Tag (~500 Mrd. USD Notional/Tag) 2023. Aktuelle Evidenz (CBOE-eigene Studien, JPMorgan-Research) deutet darauf hin, dass 0DTE-Flow die **intraday realisierte Volatilität eher komprimiert** (mehr ruhige Tage, unterbrochen von schärferen Reversals bei Dealer-Gamma-Flips), aber **keinen signifikanten Effekt auf die 30-Tage-VIX-Struktur** hat, da VIX auf 30-Tage-Erwartung zielt, nicht auf Intraday-Realisierung. Nettoeffekt auf die klassische 30-Tage-VRP: eher neutral bis leicht dämpfend (mehr Gegenparteien, engere Spreads, aber auch mehr Konkurrenz um dieselbe Prämie durch Retail-/systematische 0DTE-Credit-Spread-Verkäufer, was die Prämie pro Einheit Risiko weiter komprimiert).
- **Geschätzter Decay**: Kombiniert man die Chicago-Fed-Befunde mit dem beobachteten AUM-Wachstum im Vol-Selling-Segment, ist eine Kompression der Netto-VRP (nach Kosten) in der Größenordnung von **50-100% seit den frühen 2000ern** plausibel — von klar signifikant negativer Optionsrendite zu einer Prämie, die im Kern nur noch die reine Crash-Versicherungskompensation abbildet, nicht mehr zusätzlich Mispricing/Intermediär-Rente enthält.

### e) Kosten
Bid/Ask-Spreads bei OTM-Index-Puts sind strukturell breit (oft 5-15% des Optionspreises bei kurzlaufenden OTM-Kontrakten), Rollkosten bei systematischem monatlichen/wöchentlichen Rebalancing signifikant. Roll-Kosten von VIX-Futures-Positionen: durchschnittliche monatliche Roll-Rendite in Contango-Phasen (~80% der Handelstage ist die Kurve in Contango) liegt bei geschätzt 3-8% pro Monat je nach Kurvensteilheit — das ist der Haupttreiber der VIX-Carry-Rendite, aber symmetrisch: derselbe Mechanismus produziert bei Backwardation-Spikes explosive Verluste. Nach realistischen Transaktionskosten (Spread + Slippage + Financing) wird ein erheblicher Teil der brutto scheinbar attraktiven Sharpe Ratios (BXM/PUT: brutto ca. 0,4-0,6) auf deutlich niedrigere Netto-Werte reduziert, insbesondere für Strategien, die aktiver rollen als die passiven CBOE-Benchmark-Indizes.

### f) Kapazität und Handelbarkeit
Index-Optionen (SPX) sind hochliquide, Kapazität im Milliarden-Dollar-Bereich grundsätzlich vorhanden. Limitierend ist jedoch: (i) Konzentration der Liquidität in kurzlaufenden/ATM-Kontrakten, OTM-Tails dünner gehandelt, (ii) Marktimpact bei systematischem, vorhersagbarem Rollen (bekannte "0DTE/Monatsende-Roll"-Fenster werden von HFT-Gegenparteien gefrontrunnt), (iii) VIX-Futures-Kapazität ist kleiner als SPX-Optionsmarkt und war 2018 selbst Ursache der Krise (reflexive Feedback-Schleife: ETP-Rebalancing trieb VIX-Futures-Preise weiter nach oben).

### g) Regimeabhängigkeit und Tail-Risiko — quantifiziert
Die Renditeverteilung ist extrem linksschief. Illustrativ: Ein systematischer Put-Writer/Short-Vol-Fonds, der über Jahre 1-3% Monatsprämie einsammelt (~12-20% p.a. brutto in ruhigen Phasen), kann an einem einzigen Tag 50-95% seines Kapitals verlieren (XIV: -96% an einem Tag). **Rechnerisch**: Wenn eine Strategie im Mittel netto ~5-8% p.a. nach Kosten verdient (realistische Netto-Schätzung nach obigem Decay-Argument) und in einem Volmageddon-artigen Event 60-90% des Kapitals verliert, entspricht das **8-15+ Jahren kumulierter Prämie**, die in einem Tag/einer Woche ausgelöscht werden. Für gehebelte/inverse ETP-Strukturen (XIV) ist der Verlust ein Totalverlust-Ereignis (unendliche "Jahre Prämie", da das Produkt aufhört zu existieren). Diese Konvexität ist der zentrale Grund, warum Sharpe-Ratio-basierte Bewertung dieser Klasse irreführend ist — Sortino/Stutzer-Maße und insbesondere Conditional-Tail-Expectation sind aussagekräftiger, zeigen aber ebenfalls: die Prämie existiert, ist aber kein "Free Lunch".

### h) Kritik/Widerlegungen
Peso-Problem ist zentral: Backtests, die keine oder nur eine Volmageddon-artige Beobachtung enthalten, überschätzen systematisch den Sharpe Ratio, weil die Stichprobe die wahre Tail-Wahrscheinlichkeit unterschätzt (Survivorship der Beobachtungsperiode). Die Literatur (u.a. explizit im CFA-Institute-Volmageddon-Postmortem) verweist zudem auf eine **reflexive Endogenität**: Je mehr Kapital die "Prämie" einsammelt, desto fragiler wird genau der Mechanismus (VIX-Futures-Rebalancing-Kaskade), der die Prämie erzeugt — die Anomalie zerstört sich potenziell selbst in Crash-Momenten (negative Konvexität wird durch Crowding verstärkt, nicht nur durch Fundamentaldaten).

**Urteil: WEAK.** Reale, ökonomisch gut begründete Risikoprämie (keine reine Ineffizienz), aber mit dokumentiertem, substanziellem Post-Publication-Decay (Chicago Fed 2025) und einem Tail-Risiko-Profil, das naive Sharpe-Ratio-Vergleiche unbrauchbar macht. Für ein systematisches Fonds-Mandat nur mit explizitem Tail-Hedge/Positionsgrößenlimit vertretbar, nicht als eigenständige Alpha-Quelle mit attraktivem Netto-Sharpe.

---

## 2. Kandidat 2: VIX-Terminstruktur-Carry (Contango-Roll)

### a) Ökonomische Begründung
Identisch zu Kandidat 1 im Kern (beide sind Manifestationen derselben VRP), aber operationalisiert über VIX-Futures/ETPs statt Optionen. Käufer der "Versicherung": institutionelle Tail-Hedger, die lange VIX-Futures/Calls halten, sowie strukturelle Nachfrage nach Vol-Exposure zur Portfolio-Diversifikation. Contango (Future > Spot-VIX) entsteht, weil Investoren für längerfristige Absicherung eine Prämie zahlen und Volatilität mean-reversion-artig ist — Contango ist ca. 80% der Handelstage der Normalzustand.

### b) Limits to Arbitrage
Identisch, aber verschärft: VIX-Futures-Markt ist kleiner/illiquider als der zugrundeliegende SPX-Optionsmarkt, wodurch Rebalancing-Flows der ETPs selbst preisbewegend werden — eine strukturelle Fragilität, die 2018 direkt zur Krise beitrug (reflexiver Feedback-Loop: fallende ETP-NAV zwingt zu mehr Future-Käufen, treibt Futures-Preis weiter hoch, verstärkt NAV-Verlust).

### c) Empirische Basis
Kein einzelnes "Ur-Paper" wie bei VRP, sondern praktikerbasierte/Quantpedia-artige Evidenz: durchschnittliche monatliche Roll-Rendite in Contango 3-8%, was annualisiert scheinbar sehr hohe Renditen suggeriert — diese Zahlen sind jedoch stark von der Stichprobenperiode abhängig und schließen die Crash-Perioden typischerweise aus oder unterrepräsentieren sie.

### d) Out-of-Sample/Post-2018-Evidenz
Der Markt hat nach Feb 2018 strukturell reagiert: (i) XIV wurde komplett vom Markt genommen, (ii) SVXY wurde von 1x auf 0,5x Hebel reduziert (regulatorische/Emittenten-Reaktion), (iii) Leverage-Caps und Vermarktungsbeschränkungen für Privatanleger wurden verschärft. Das reduziert die adressierbare "naive" Retail-Kapazität dieser spezifischen Ausprägung erheblich, verschiebt die verbleibende Prämie stärker zu institutionellen/professionellen Akteuren mit besserem Risikomanagement — was tendenziell zu einer weiteren Kompression der Netto-Prämie für Nachzügler führt.

### e)-f) Kosten/Kapazität
Roll-Kosten sind der Strategie-Mechanismus selbst (nicht nur ein Kostenfaktor), Geld-Brief-Spreads bei VIX-Futures moderat, aber Financing/Margin-Kosten volatil. Kapazität geringer als bei SPX-Optionen (Kandidat 1), da VIX-Futures-Open-Interest kleiner ist.

### g) Tail-Risiko
Am extremsten in dieser gesamten Klasse: VIX stieg am 5. Feb. 2018 um +115,6% an einem Tag. Bei typischem Leverage/Beta dieser Produkte bedeutet das Totalverlust-Charakter. Kumulierte Jahresprämie-Äquivalente: siehe Kandidat 1 (noch extremer, da ETPs teils Totalverlust erlitten = unendlich viele "Jahre Prämie").

**Urteil: WEAK.** Mechanisch nachvollziehbarer Carry-Effekt, aber die reflexive Fragilität (Produkt selbst treibt die Krise) und der bereits erfolgte Strukturbruch 2018 (Marktbereinigung, Leverage-Reduktion) machen dies zur am wenigsten robusten Variante der Klasse. Kein Hinweis auf eine "neue", unentdeckte Ineffizienz — im Gegenteil, der Markt hat sichtbar und dauerhaft auf das Ereignis reagiert.

---

## 3. Kandidat 3: Dispersion Trading / Correlation Risk Premium

### a) Ökonomische Begründung
Index-Puts sind strukturell teurer relativ zu einem gewichteten Korb von Einzelaktien-Optionen, weil Index-Absicherung (breite, diversifizierte Portfolio-Versicherung) stärker nachgefragt wird als Einzeltitel-Absicherung. Implizite Korrelation liegt im Mittel über der später realisierten Korrelation — "Short Correlation" (long Einzelaktien-Vega, short Index-Vega) sammelt diese Differenz ein.

### b) Limits to Arbitrage
Hohe operative Komplexität (viele Einzeltitel-Optionspositionen simultan managen, Rebalancing bei Index-Kompositionsänderungen), breite Spreads bei Einzelaktien-Optionen (viel breiter als bei liquiden Index-Optionen), Korrelationsschocks in Makro-Krisen sind exakt dann am größten, wenn Diversifikation am meisten gebraucht würde ("alles korreliert in der Krise gegen 1").

### c) Originalstudien und Effektgrößen
- Deng (2008, zitiert in Folgeliteratur): Dispersion Trading auf S&P 100 war 1996-2000 "extrem profitabel" — durchschnittliche **Monatsrendite 24%, Sharpe Ratio 1,2**. Nach 2000: Monatsrendite kollabierte auf **-0,03%, Sharpe -0,17**. Dies ist eines der **klarsten dokumentierten Post-Publication-Decay-Beispiele** in der gesamten Optionsanomalie-Literatur — die Anomalie wurde nach Entdeckung/Publikation praktisch handelbar arbitriert.
- Große Backtest-Studie auf S&P-100-Optionen (mehrjährige Stichprobe): 14,52% bzw. 26,51% p.a. **nach** Transaktionskosten, Sharpe Ratios 0,40 bzw. 0,34.
- Teilstichprobe 2010-2015: 23,51% p.a., Sharpe 2,47 (deutlich höher — aber kurzer, günstiger Teilzeitraum, nicht robust über volle Historie).
- Korrelationsrisikoprämien-Literatur (Driessen/Maenhout/Vilkov-artige Ansätze): Sharpe Ratio von ca. 0,85 p.a. für spezifisch diffusive Korrelation, mit besonders hoher Prämie um die Dotcom-Krise.

### d) Interpretation: Ineffizienz oder Prämie?
Die Literatur ist hier **gespalten** — im Gegensatz zu Kandidat 1/2 gibt es explizite Studien, die für die **Markt-Ineffizienz-Hypothese statt Risikoprämien-Hypothese** argumentieren: Ein fundamentales Risikoprämien-Argument sollte nicht verschwinden, nur weil sich Marktstruktur ändert — genau das aber beobachtet Deng (2008) beim Kollaps nach 2000. Andere Studien relativieren dies und finden, dass die Korrelationsrisikoprämie "nur eine untergeordnete Rolle" für die Dispersion-Rendite spielt, was eher für Mispricing als Erklärung spricht.

### e)-f) Kosten/Kapazität
Am schwächsten in dieser Klasse: Notwendigkeit vieler simultaner Einzelaktien-Optionspositionen mit breiten Spreads begrenzt Kapazität stark und macht Netto-Renditen nach realistischen Kosten fragil — die brutto attraktiven Sharpe Ratios von 1,2+ (frühe Periode) sind mit hoher Wahrscheinlichkeit zu einem erheblichen Teil Kosten-/Liquiditäts-Artefakt.

### g) Tail-Risiko
Korrelation kann in Krisen (2008, 2020, 2022) sprunghaft gegen 1 gehen — konzentrierter Verlust in genau den Momenten, die für Portfolio-Diversifikation am wichtigsten wären.

**Urteil: WEAK**, tendenziell näher an KILL als Kandidat 1/2 wegen des expliziten, gut dokumentierten Sharpe-Kollaps (1,2 → -0,17) nach der ursprünglichen Entdeckungsperiode — ein Lehrbuchbeispiel für Arbitrage-Wegkonkurrieren einer Ineffizienz, nicht für eine stabile Risikoprämie. Keine frei zugängliche Datenquelle zum eigenständigen Testen (Einzelaktien-Optionsdaten mit Historie sind i.d.R. kostenpflichtig, z.B. OptionMetrics).

---

## 4. Gesamtfazit für die Anomalieklasse

Die Nullhypothese ("kein echtes Alpha") ist **nicht vollständig zu verwerfen, aber die Klasse liefert kein robustes, kostenbereinigtes Alpha im klassischen Sinn**. Was existiert, ist überwiegend eine **kompensierte Risikoprämie für das strukturelle Underwriting von Crash-Versicherung**, deren Größe seit den 2000ern durch (a) Vol-Selling-Crowding, (b) verbesserte Marktmacher-Kapazität, (c) den Volmageddon-Strukturbruch 2018 und (d) vermutlich auch 0DTE-bedingte Kompression der Intraday-Prämie **erheblich geschrumpft** ist (Chicago Fed 2025: Alpha "indistinguishable from zero" über die letzten 15 Jahre). Reine Ineffizienz-Anteile (am ehesten bei Dispersion Trading plausibel) sind bereits weitgehend wegarbitriert.

Für ein Portfolio, das auf dokumentierte Post-Publication-Robustheit UND Kostenrobustheit besteht, qualifiziert sich **keiner der drei Kandidaten als CANDIDATE**. Alle drei landen bei **WEAK**: ökonomisch plausibel, historisch signifikant, aber (i) mit stark abnehmender Netto-Prämie in der jüngeren Stichprobe, (ii) mit einem Tail-Risiko-Profil, das mehrjährige kumulierte Erträge in einzelnen Ereignissen auslöschen kann (XIV -96% an einem Tag ist der extremste, aber nicht einzige Beleg), und (iii) mit hohen, oft unterschätzten Handelskosten (breite Optionsspreads, Rollkosten, prozyklische Margin).

**Praktische Konsequenz für ein Multi-Strategie-Mandat**: Falls überhaupt eingesetzt, dann nur (a) in kleiner Positionsgröße mit hartem Tail-Hedge-Overlay, (b) mit expliziter Kill-Switch-Logik bei VIX-Term-Structure-Inversion, (c) nicht als eigenständiger "Alpha"-Baustein, sondern als bewusst eingegangene, gut verstandene Risikoprämie mit Versicherungscharakter — ehrlich benannt als das Sammeln einer Prämie, nicht als Ausnutzen einer Marktineffizienz.

---

## Quellen (Auswahl, aus WebSearch-Ergebnissen dieser Session)

- [The Decline of the Variance Risk Premium: Evidence from Traded and Synthetic Options — Chicago Fed WP 2025-17](https://www.chicagofed.org/publications/working-papers/2025/2025-17)
- [Variance Risk Premia — Carr & Wu (2009), Review of Financial Studies](https://engineering.nyu.edu/sites/default/files/2019-01/CarrReviewofFinStudiesMarch2009-a.pdf)
- [Delta-Hedged Gains and the Negative Market Volatility Risk Premium — Bakshi & Kapadia (2003)](https://people.umass.edu/~nkapadia/docs/Bakshi_and_Kapadia_2003_RFS.pdf)
- [Volmageddon and the Failure of Short Volatility Products — CFA Institute](https://rpc.cfainstitute.org/research/financial-analysts-journal/2021/volmageddon-failure-short-volatility-products)
- [What Caused the Volatility "Volmageddon" on 5-Feb-2018?](https://www.sixfigureinvesting.com/2019/02/what-caused-the-february-5th-2018-volatility-spike-xiv-termination/)
- [Key Cboe Benchmark Indexes Using SPX Options Offer Strong Risk-Adjusted Returns](https://www.cboe.com/insights/posts/key-cboe-benchmark-indexes-using-spx-options-offer-strong-risk-adjusted-returns/)
- [Options-Based Benchmark Indexes: Performance, Risk — Cboe/Wilshire 2019](https://cdn.cboe.com/resources/spx/wilshire-options-based-benchmark-indexes-2019.pdf)
- [0DTE Index Options and Market Volatility: How Large is Their Impact? — Cboe Research](https://cdn.cboe.com/resources/education/research_publications/gammasqueezes.pdf)
- [Evaluating the Market Impact of SPX 0DTE Options — Cboe Insights](https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/)
- [Dispersion trading: An empirical analysis on the S&P 100 options](https://www.researchgate.net/publication/331557612_Dispersion_trading_An_empirical_analysis_on_the_SP_100_options)
- [Dispersion trading: Empirical evidence from U.S. options markets — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1044028309000593)
- [Jumps and the Correlation Risk Premium: Evidence from Equity Options](https://www.aeaweb.org/conference/2020/preliminary/paper/dKnKSRZn)
- [VIX Futures Explained: Contango, Backwardation, and Roll Yield](https://volatilitybox.com/research/vix-contango-backwardation/)
- [2020 stock market crash — Wikipedia](https://en.wikipedia.org/wiki/2020_stock_market_crash)
