```yaml
agent: 18
klasse: "Short Interest"
websuche_verfuegbar: ja
strategien:
  - name: "Cross-sektionale Short-Interest-Anomalie (Miller 1977 / Asquith-Pathak-Ritter 2005 / Boehmer-Jones-Zhang 2008), kostenadjustiert"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 2
      kapazitaet: 2
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.3
    netto_sharpe_erwartung: "0.0-0.2"
    kernrisiko: "Borrow-Fees und Squeeze-Tail-Risiko konzentrieren sich exakt in den Titeln, in denen das rohe Signal am stärksten ist (Drechsler & Drechsler 2014); Value-Weighted-Version ist fast insignifikant; unbegrenztes Verlustpotenzial bei Squeeze-Events (GameStop Jan. 2021)"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "FINRA/NYSE/Nasdaq Bi-Weekly Short Interest Reports (frei) + CRSP/Yahoo Finance/Stooq Kursdaten; Borrow-Fees/Utilization NICHT frei verfügbar (IHS Markit Securities Finance, S3 Partners, Ortex sind kostenpflichtig)"
  - name: "Aggregiertes Short Interest als Markttiming-Signal (Rapach, Ringgenberg & Zhou 2016, JFE)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 4
      kapazitaet: 4
      kostenrobustheit: 4
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "0.1-0.3"
    kernrisiko: "Kernresultat ggf. stark durch Kalenderjahr 2008 getrieben; kein verifizierter Post-2016-Out-of-Sample-Replikationstest mit weiterhin starker Performance gefunden; Timing-Signal mit nur ~12 Monatsbeobachtungen p.a. -> geringe statistische Power pro Dekade"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "FINRA/NYSE aggregierte Short-Interest-Summen (frei) + Ken-French Mkt-RF / CRSP-Value-Weighted-Index"
  - name: "Short-Squeeze-Harvesting: systematischer Long in hochgeshorteten/Crowded-Short-Titeln zur Vereinnahmung der Squeeze-Prämie"
    urteil: KILL
    scores:
      reproduzierbarkeit: 1
      signifikanz_nach_mtk: 1
      regimestabilitaet: 1
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.05
    netto_sharpe_erwartung: "<0 (vermutlich negativ nach Kosten)"
    kernrisiko: "Keine akademische Studie belegt einen positiven Erwartungswert dieser Strategie; passt zum Muster der Lottery-Demand-Anomalie (Überzahlung für positive Skewness); Squeezes sind selten (<1% der Stock-Tage) und GameStop ist ein Survivorship-verzerrter Extremfall, kein wiederholbares Muster"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "FINRA Short Interest Reports + Yahoo Finance Days-to-Cover-Feld (z.B. GME, AMC, BBBY als historische Fallstudien)"
```

# Anomalieklasse: Short Interest — Adversarial Review

**Agent 18 | Stand: Juli 2026 | Websuche verfügbar: ja (mehrere Runden Web-Recherche durchgeführt, Quellen unten dokumentiert)**

**Nullhypothese (Ausgangspunkt): Es gibt kein handelbares Netto-Alpha in Short-Interest-basierten Strategien für einen Outsider-Investor ohne proprietäre Order-Flow- oder Fee-Daten.** Diese Nullhypothese wird im Folgenden für drei Kandidaten geprüft und nur teilweise verworfen — mit erheblichen Einschränkungen.

---

## Zusammenfassung des Urteils

Die Short-Interest-Literatur ist eine der am besten dokumentierten Anomalieklassen der Asset-Pricing-Forschung, UND sie ist zugleich ein Paradebeispiel dafür, wie eine gut replizierte akademische Korrelation nach Kosten verschwinden oder sich sogar umkehren kann. Die zentrale Falle aus dem Auftrag — dass die profitabelsten Shorts genau die mit den höchsten Borrow-Fees sind — ist in der Literatur nicht nur bestätigt, sondern von Drechsler & Drechsler (2014) explizit zum Kernresultat gemacht: Anomalien "verschwinden effektiv" in den 80% der Aktien mit niedrigen Fees und sind nur in den teuren 20% "stark verstärkt" — exakt dort, wo die Fee die Bruttorendite auffrisst. Keiner der drei geprüften Kandidaten erreicht das CANDIDATE-Niveau. Zwei sind WEAK (mit unterschiedlichen, aber jeweils gravierenden Einschränkungen), einer ist ein klares KILL.

---

## Kandidat 1: Cross-sektionale Short-Interest-Anomalie (Miller 1977 → Asquith/Meulbroek → Asquith-Pathak-Ritter 2005 → Boehmer-Jones-Zhang 2008)

### a) Ökonomische Begründung

Miller (1977) liefert das theoretische Fundament: Bei **Divergence of Opinion** (Meinungsdivergenz zwischen Investoren über den fairen Wert) und **Short-Sale-Constraints** wird der Preis eines Wertpapiers vom optimistischsten Grenzinvestor gesetzt, nicht vom Konsens. Pessimisten, die eigentlich eine negative Position halten wollen, sind auf null Aktien beschränkt (Short-Constraint) und scheiden aus der Preisbildung aus. Je größer die Meinungsdivergenz UND je bindender die Short-Constraint, desto größer die Überbewertung. Wichtig: Empirische Tests zeigen, dass **beide Bedingungen gleichzeitig** erfüllt sein müssen — Divergenz allein oder Constraint allein reicht nicht; robuste Überbewertungseffekte zeigen sich nur an der Schnittmenge (Interaktionseffekt).

**Wer hält die überteuerten Titel?** Strukturell: (1) Long-only-Fonds und Pensionskassen, die aus Mandats- oder Regulierungsgründen nicht shorten dürfen und daher als "erzwungene Optimisten" fungieren; (2) Retail-Investoren mit Sentiment-/Lottery-Präferenz (siehe Kandidat 3); (3) Insider und Management selbst, die naturgemäß nicht gegen die eigene Aktie wetten. Die Gegenseite — informierte Pessimisten — kann ihre negative Meinung nur über den Leihmarkt exprimieren, der begrenzt ist (begrenztes Aktienangebot zum Verleih, insbesondere bei Small Caps mit konzentriertem Insider-Besitz).

### b) Limits to Arbitrage

Drei Haupt-Constraints, alle empirisch belegt:

- **Borrow-Kosten (Fee):** Cohen, Diether & Malloy (2007, J. Finance) zeigen in einem Gleichgewichtsmodell für Leihmarkt und Aktienmarkt: Hard-to-borrow-Aktien (hohe Fee) haben eine um **4,8 Prozentpunkte niedrigere 3-Monats-Rendite** als andere Aktien, mit der stärksten Konzentration bei Titeln mit hoher Meinungsdivergenz (direkte Bestätigung von Miller). Der Aktienkurs ist positiv mit dem Fee-Niveau korreliert, die erwartete Risikoprämie negativ — d.h. ein Anstieg der Leihgebühr selbst ist ein negatives Renditesignal (Fee-Änderung als Timing-Signal), nicht nur das Fee-Niveau.
- **Recall-Risiko:** Engelberg, Reed & Ringgenberg (2018, J. Finance, "Short-Selling Risk") zeigen, dass Leihpositionen im Median **ca. 65 Tage** offen sind, bevor Aktien zurückgerufen werden ("recalled") oder die Fee sich ändert. Aktien mit hohem "Short-Selling-Risiko" (Risiko steigender Fees / Recall) zeigen **niedrigere** Renditen, **weniger** Preiseffizienz und **weniger** tatsächliche Shortaktivität — die Autoren interpretieren dies als gepreistes Risiko, nicht als freie Arbitragemöglichkeit: Der Markt kompensiert die Träger dieses Risikos, saugt die Überbewertung aber nur teilweise ab, weil zu wenige Arbitrageure bereit sind, das Risiko zu tragen.
- **Squeeze-Risiko (GameStop, Januar 2021):** Das Lehrbuchbeispiel für asymmetrisches Verlustpotenzial beim Shorting. GameStop erreichte im Januar 2021 ein Short Interest von **ca. 140% des Streubesitzes** (technisch möglich durch mehrfache Weiterverleihung derselben Aktien). Die Tage-zum-Covern-Kennzahl (Days-to-Cover) lag laut Crowding-Analysen (Omega Point/MSCI) das gesamte Jahr 2020 im obersten Dezil aller US-Aktien — ein Frühwarnsignal, das sich materialisierte. Folgen für Marktteilnehmer, die das Signal "long high SI ist billig zu shorten" gehandelt hatten: **Melvin Capital** verlor im ersten Quartal 2021 rund 49% und benötigte eine Kapitalspritze von rund 3 Mrd. USD von Citadel und Point72; **Citron Capital** erlitt praktisch einen Totalverlust (100%) auf seine GME-Shortposition und stellte daraufhin die öffentliche Short-Research ein; **White Square Capital** (London) meldete zweistellige Verluste durch die GME-Wette und schloss den Fonds im Juni 2021. Das Ereignis zeigt: Short-Verluste sind theoretisch unbegrenzt (Kurs kann beliebig steigen), während Long-Verluste auf 100% begrenzt sind — die Verlustverteilung der Strategie ist strukturell linksschief mit fettem Tail.

### c) Originalstudien — Effektgrößen und Stichproben

- **Asquith & Meulbroek (1996, Working Paper, Vorläufer der publizierten Version):** Erste systematische Dokumentation, dass hoch geshortete Aktien nachfolgend underperformen.
- **Asquith, Pathak & Ritter (2005, Journal of Financial Economics, Vol. 78, No. 2, S. 243–276):** Stichprobe 1988–2002, kombiniert Short-Interest-Ratio mit institutioneller Eigentümerschaft zur Identifikation "short-sale-constrained" Aktien. Ergebnis: **Equally-Weighted-Portfolio underperformt um 215 Basispunkte pro Monat**, aber das **Value-Weighted-Portfolio nur um 39 Basispunkte pro Monat** — ein Faktor-5,5-Unterschied. Das bedeutet: Der Effekt ist fast vollständig ein Small-Cap-Phänomen und bei ökonomisch realistischer Gewichtung (nach Marktkapitalisierung, wie ein großer Fonds tatsächlich handeln würde) schwach. Die Autoren selbst weisen darauf hin, dass die Umsetzung der High-Short-Interest-Strategie **erhebliches Portfolio-Turnover** erfordert und einen **Implementation-Shortfall** relativ zu den kostenfrei berechneten Renditen zur Folge hätte.
- **Boehmer, Jones & Zhang (2008, Journal of Finance, "Which Shorts Are Informed?"):** Nutzt einen proprietären, **täglichen** NYSE-Order-Flow-Datensatz 2000–2004 (nicht die öffentlich verfügbare, nur zweiwöchentlich gemeldete Short-Interest-Zahl!). Shortverkäufe machen 2000–2004 **>12,9% des NYSE-Volumens** aus. Kernresultat: Aktien mit hohem täglichem Shortvolumen underperformen Aktien mit niedrigem Shortvolumen um **1,16% risikoadjustiert über die folgenden 20 Handelstage (≈15,6% annualisiert)**. Bei Zerlegung nach Händlertyp: **institutionelle Non-Program-Shortverkäufe** sind am informativsten — Aktien, die stark von Institutionen geshortet werden, underperformen im Folgemonat um **1,43% (≈19,6% annualisiert)**. **Kritischer Punkt für die Handelbarkeit:** Dieses Ergebnis beruht auf täglichem, granularem Order-Flow, der öffentlich nicht verfügbar ist. Die öffentlich gemeldete (zweiwöchentliche, mit Meldeverzug behaftete) Short-Interest-Zahl, mit der Retail- und die meisten institutionellen Investoren tatsächlich arbeiten müssen, ist ein deutlich schwächeres und verzögertes Signal als das, was BJZ tatsächlich testen.

**Wichtige methodische Unterscheidung, die in der Praxis oft übersehen wird:** Die stärksten publizierten Effektgrößen (BJZ) stammen aus proprietären Intraday-/Daily-Order-Flow-Daten mit Informationsvorsprung gegenüber der Öffentlichkeit. Die für normale Investoren zugängliche, biweekly gemeldete Short-Interest-Zahl (FINRA/NYSE/Nasdaq) ist strukturell schwächer, weil sie (a) bereits 1–2 Wochen alt ist, wenn sie veröffentlicht wird, und (b) aggregiert ist, sodass Informationen über die Zusammensetzung (informierte institutionelle Shorts vs. Retail-Hedging, Wash Trades, Optionsmarkt-Delta-Hedging) verloren gehen.

### d) Out-of-Sample-/Post-Publication-Evidenz

Eine spezifische Post-Publication-Decay-Zahl für die Short-Interest-Anomalie im engeren Sinn wurde in der Recherche nicht gefunden (Datenlücke, wird hier offen benannt statt spekulativ gefüllt). Als Kontext dient die allgemeine Anomalie-Decay-Literatur: Jacobs & Müller (2020, "Anomalies across the globe: Once public, no longer existent?", 241 Anomalien, 39 Länder) zeigen, dass die **USA das einzige Land mit einem verlässlichen Post-Publication-Rückgang** der Long-Short-Renditen ist — durchschnittlicher Rückgang von **mehr als einem Drittel** nach Publikation, mit Reduktion vor allem durch Arbitragekapital-Zufluss, nicht durch Data-Mining-Artefakte. Da Short-Interest-Strategien besonders arbitragekapital-sensitiv sind (die Fee selbst ist ein Marktmechanismus, der bei erhöhter Nachfrage nach Leihe steigt und damit den Trade selbstlimitierend verteuert), ist ein überdurchschnittlicher Decay plausibel, aber nicht separat belegt.

**Strukturbruch Meme-Stock-Ära (2021):** Dies ist der wichtigste Kandidat für einen echten Regimewechsel. Vor 2021 war "Short-Squeeze" ein Tail-Risiko unter vielen; seit GameStop ist es ein bekannter, von einer koordinierten Retail-Community (r/wallstreetbets) aktiv gesuchter Trigger-Mechanismus. Empirisch dokumentiert: Seit dem Meme-Stock-Squeeze Anfang 2021 sind die am stärksten geshorteten Aktien **2- bis 3-mal so volatil** wie der gleichgewichtete S&P 500 (Crowding-Research von Marktteilnehmern, konsistent mit akademischer Squeeze-Literatur). Prime-Broker und Multi-Strategy-Fonds haben ihre Exposure zu "Crowded Shorts" seither systematisch über Crowding-Metriken (MSCI, Goldman Sachs Prime, Omega Point) gemanagt — das heißt, die Arbitrageure selbst haben ihr Verhalten strukturell angepasst, was ein Indiz für einen dauerhaften, nicht nur temporären Regimewechsel ist.

Eine aktuelle, direkt einschlägige Studie: **Allen, Haas, Pirovano & Tengulov ("How Prevalent Are Short Squeezes? Evidence from the US and Europe", J. Banking & Finance, 2025)** liefert Basisraten für die Häufigkeit von Squeezes: In den USA treten **Market Squeezes an 0,39%** und **Lender Squeezes an 0,77%** aller Aktien-Tage auf; auf Quartalsbasis erleben **9,9% der US-Aktien** irgendeinen Market Squeeze pro Quartal. Sektoral konzentrieren sich Squeezes in den USA auf Energie/Kohle/Bergbau, Finanzwerte und Tabak. Diese Zahlen relativieren GameStop: Ein Squeeze dieser Größenordnung ist ein extremes Tail-Event, aber kleinere Squeezes sind tatsächlich relativ häufig (fast 10% der Aktien pro Quartal betroffen) — das strukturelle Risiko ist also nicht auf 2021 beschränkt, sondern ein permanentes Feature des Short-Interest-Signals.

### e) Kosten — Borrow-Fees explizit (Drechsler & Drechsler)

Dies ist der Kern der im Auftrag beschriebenen Falle, und die Evidenz bestätigt sie eindeutig. **Drechsler & Drechsler ("The Shorting Premium and Asset Pricing Anomalies", NBER WP 20282 / erweitert publiziert):**

- Das Cheap-Minus-Expensive-to-short-Portfolio (CME) hat eine **durchschnittliche Bruttorendite von 1,43% pro Monat**, aber nach Abzug der tatsächlichen Leihgebühren nur noch **0,91% pro Monat netto** — die Fee frisst **rund 36% der Bruttorendite** allein auf Portfolioebene, bei den teuersten Einzeltiteln deutlich mehr.
- Der Vier-Faktor-Alpha des CME-Portfolios beträgt 1,53% pro Monat — die Autoren interpretieren dies **nicht als freies Alpha**, sondern als Kompensation für das konzentrierte Short-Risiko, das nur eine kleine Gruppe von Arbitrageuren trägt (Risikoprämie, kein Mispricing im engeren Sinn).
- **Zentrales Ergebnis für acht der bekanntesten Cross-Sectional-Anomalien:** Die Anomalie-Renditen **verschwinden effektiv innerhalb der 80% der Aktien mit niedrigen Short-Fees**, sind aber **stark verstärkt innerhalb der teuren 20%**. Das ist exakt das im Auftrag beschriebene Muster: Das Signal wirkt nur dort, wo die Fee am höchsten ist — und genau dort frisst die Fee die Rendite.
- Für Volatilitäts-bezogene Portfolios sind die Short-Fees **mehr als dreimal so hoch** wie normal.

**Implikation für die Praxis:** Ein Investor, der naiv "hohes Short Interest → short gehen" umsetzt, ohne die tatsächliche Borrow-Fee in Echtzeit zu berücksichtigen, wird strukturell in genau die Titel gedrängt, wo die Netto-Rendite nach Fee am kleinsten (oder negativ) ist. Eine profitable Umsetzung erfordert Echtzeit-Fee-Daten (IHS Markit Securities Finance, S3 Partners, Ortex) — kostenpflichtige, institutionelle Datenquellen, die für die Nullhypothesen-Prüfung mit frei verfügbaren Daten nicht reproduzierbar sind.

### f) Kapazität und Handelbarkeit

Strukturell gering und **selbstlimitierend**: Das Signal ist am stärksten bei kleinen, illiquiden, hard-to-borrow Aktien mit knappem Leihangebot. Genau das begrenzte Leihangebot ist die Ursache der hohen Fee — wenn ein Fonds versucht, die Position zu skalieren, treibt die zusätzliche Nachfrage nach Leihe die Fee weiter nach oben und verschlechtert die Netto-Rendite (negativer Feedback-Loop, im Gegensatz zu z.B. Value oder Momentum, wo Skalierung primär über Market Impact wirkt, nicht über einen expliziten, mengenabhängigen Leihpreis). Zusätzlich: Leihangebot kann jederzeit zurückgerufen werden (Recall, im Median nach ~65 Tagen gemäß Engelberg/Reed/Ringgenberg), was Zwangsdeckungen zu ungünstigen Zeitpunkten erzwingt.

### g) Regimeabhängigkeit und Tail-Risiko

- **Short-Bann 2008:** Am 18. September 2008 erließ die SEC ein Notfall-Verbot des Leerverkaufs für nahezu alle Finanzwerte. Die akademische Evidenz zur Wirkung ist **gemischt**: Autore et al. (2011) finden positive abnormale Renditen bei Bann-Einführung; Battalio, Mehran & Schultz (2012) kommen zum Schluss, dass der Bann **die Kurse nicht stützen konnte**; Boehmer, Jones & Zhang (2013, Review of Financial Studies, "Shackling Short Sellers: The 2008 Shorting Ban") finden höhere Kurse für gebannte **große** Finanzwerte, aber **nicht** für kleine — bei gleichzeitig **massiver Verschlechterung der Marktqualität** (breitere Spreads, höhere Volatilität für alle außer dem kleinsten Quartil) und einem Rückgang des Shortvolumens um **ca. 77%** bei Large Caps während des Banns. Für eine Short-Interest-Strategie bedeutet das: Regulatorisches Tail-Risiko kann die Strategie jederzeit und ohne Vorwarnung temporär unhandelbar machen — ein Risiko, das in keinem historischen Backtest vollständig eingepreist werden kann, da es diskretionär von Regulierungsbehörden ausgelöst wird.
- **Meme-Stock-Squeezes:** siehe (b) und (d) — GameStop als Extremfall, aber laut Allen/Haas/Pirovano/Tengulov (2025) sind kleinere Squeezes mit fast 10% Quartalsinzidenz ein strukturelles, nicht nur episodisches Risiko.
- **Krisenzeiten allgemein:** Short-Interest-Strategien sind prozyklisch riskant — in Stressphasen (2008, März 2020, Meme-Ära 2021) korrelieren Squeeze-Risiko, Fee-Spikes und regulatorisches Eingriffsrisiko gleichzeitig, was zu Klumpenrisiko in genau den Phasen führt, in denen ein Hedgefonds ohnehin unter Druck steht (Melvin Capital, Citron, White Square — alle drei Beispiele fallen in dieselbe Ereigniswoche).

### h) Bekannte Kritik/Widerlegungen

1. Value-Weighted-Version des Effekts ist gemäß Asquith/Pathak/Ritter (2005) fast insignifikant (39 Bp/Monat vs. 215 Bp/Monat EW) — der Effekt ist primär ein Small-Cap/Illiquiditäts-Phänomen, nicht robust bei kapitalisierungsgewichteter, realistischer Portfoliokonstruktion.
2. Die stärkste dokumentierte Effektgröße (Boehmer/Jones/Zhang) beruht auf proprietären, öffentlich nicht verfügbaren Order-Flow-Daten — nicht auf der öffentlich gemeldeten Short-Interest-Zahl, mit der die meisten Marktteilnehmer tatsächlich arbeiten müssen.
3. Drechsler & Drechsler (2014) interpretieren die Überrendite explizit als **Risikoprämie für konzentriertes Short-Risiko**, nicht als Mispricing — ein fundamentaler Einwand gegen die "Ineffizienz"-Interpretation der gesamten Kandidatengruppe.
4. Engelberg/Reed/Ringgenberg (2018) zeigen, dass hohes "Short-Selling-Risk" mit **weniger** tatsächlicher Shortaktivität und **weniger** Preiseffizienz einhergeht — d.h. der Markt selbst "weiß", dass diese Titel riskant zu shorten sind, und meidet sie, was die verbleibende Überbewertung stabilisiert statt sie wegzuarbitrieren.

---

## Kandidat 2: Aggregiertes Short Interest als Markttiming-Signal (Rapach, Ringgenberg & Zhou 2016)

### a) Ökonomische Begründung

Anders als Kandidat 1 ist dies **kein Stockpicking-Signal**, sondern ein **Markttiming-Signal**: die Summe des Short Interest über den gesamten NYSE-Markt als Prädiktor für die künftige Rendite des Gesamtmarktes (nicht Einzelaktien). Die ökonomische Begründung unterscheidet sich von Miller: Rapach/Ringgenberg/Zhou interpretieren aggregiertes Short Interest **nicht** primär als Sentiment-/Constraint-Signal, sondern über einen **Cashflow-Kanal**: Shortseller als Gruppe sind informierte Trader, die zukünftige aggregierte Cashflows (Unternehmensgewinne auf Marktebene) antizipieren können. Ein VAR-Zerlegung in der Originalstudie zeigt, dass die Prognosekraft überwiegend aus diesem Cashflow-Kanal stammt, nicht aus einem Diskontierungsraten-Kanal.

### b) Limits to Arbitrage

Hier unterscheidet sich das Bild fundamental von Kandidat 1: Die Umsetzung erfolgt typischerweise über **Indexinstrumente** (S&P-500-Futures, SPY, Cash-Allokation), nicht über Einzelaktien-Leerverkäufe. Damit entfällt das stock-spezifische Borrow-Fee-Problem weitgehend — Index-Futures haben keine individuelle Recall- oder Squeeze-Problematik. Das verbleibende Limit-to-Arbitrage ist eher klassisches Makro-Timing-Risiko: Das Signal ist niederfrequent (monatlich/biweekly), verrauscht, und ein zu aggressiver Einsatz von Leverage bei einem Fehlsignal kann trotzdem erhebliche Verluste erzeugen.

### c) Originalstudie — Effektgröße

**Rapach, Ringgenberg & Zhou (2016, Journal of Financial Economics, Vol. 121, Issue 1, S. 46–65):** Aggregiertes Short Interest wird als **"stärkster bekannter Prädiktor"** für Marktrenditen präsentiert, mit **In-Sample-R² von 12,89%** und **Out-of-Sample-R² von 13,24%** (annualisiert, Monatsdaten), und übertrifft damit eine Reihe etablierter Prädiktoren (Dividend Yield, Term Spread etc.) sowohl in- als auch out-of-sample. Für einen Mean-Variance-Investor werden **Nutzengewinne von über 300 Basispunkten pro Jahr** beziffert.

### d) Out-of-Sample-/Post-Publication-Evidenz

Zwei gegenläufige Befunde aus der Recherche, die hier transparent nebeneinandergestellt werden:

- **Stützend:** Eine internationale Erweiterungsstudie ("Short Interest and Aggregate Stock Returns: International Evidence", Review of Asset Pricing Studies) berichtet, dass Short Interest seine Prognosekraft **auch außerhalb der USA, nach der globalen Finanzkrise und außerhalb von Rezessionsperioden** behält.
- **Relativierend:** Eine per Websuche identifizierte Folgeuntersuchung (Titel/Autor über die Suchmaschinen-Zusammenfassung, nicht im Volltext verifiziert) berichtet, dass die **gesamte Prognosekraft verschwindet, wenn die Short-Interest-Daten für das Kalenderjahr 2008 aus der Stichprobe entfernt werden** — ein Hinweis darauf, dass das ursprüngliche Ergebnis möglicherweise stark durch die Finanzkrise 2008 (eine einzelne, extreme Episode) getrieben ist statt durch einen stabilen, wiederkehrenden Mechanismus. **Diese Quelle konnte nicht im Volltext verifiziert werden und wird daher mit reduziertem Vertrauen behandelt**, ist aber angesichts der ansonsten dünnen Post-Publication-Evidenzlage ernst zu nehmen.

Ein direkter, im Volltext bestätigter Post-2016-Out-of-Sample-Test (d.h. "hat das Signal 2017–2026 tatsächlich weiter funktioniert?") wurde in der Recherche **nicht gefunden** — dies ist eine explizite Evidenzlücke, kein negatives Ergebnis. Angesichts von zehn Jahren seit Publikation (2016–2026) ist das Fehlen einer bestätigten Erfolgsgeschichte selbst ein leicht negatives Signal (publication bias würde eine erfolgreiche Replikation eher sichtbar machen als eine stille).

### e) Kosten — Borrow-Fees

Der entscheidende Unterschied zu Kandidat 1: **Die Drechsler-&-Drechsler-Falle greift hier strukturell weniger**, weil die Implementierung über liquide Indexinstrumente erfolgt und keine Einzelaktien-Leihe involviert. Die relevanten Kosten sind Futures-Rollkosten, Finanzierungskosten (Repo-Rate-Spread) und Slippage bei Index-Rebalancing — typischerweise eine bis zwei Größenordnungen kleiner als Einzelaktien-Borrow-Fees bei hard-to-borrow Small Caps.

### f) Kapazität und Handelbarkeit

Deutlich höher als Kandidat 1: Index-Futures und große Index-ETFs haben praktisch unbegrenzte Liquidität relativ zu den Kapitalgrößen, die ein einzelner Marktteilnehmer für ein Timing-Overlay einsetzen würde. Dies ist der stärkste Pluspunkt dieses Kandidaten.

### g) Regimeabhängigkeit und Tail-Risiko

Die zentrale Schwäche: Falls das relativierende Kritikergebnis (Punkt d) korrekt ist, ist das Signal im Kern ein **Krisenperioden-Signal** (funktioniert primär während/um 2008), nicht ein stabiler, das ganze Zyklus über wirksamer Prädiktor. Für den Short-Bann 2008 gilt hier zusätzlich: Der Leerverkaufsbann selbst hat 2008 die aggregierte Short-Interest-Zahl mechanisch verzerrt (Shortvolumen fiel bei Large-Cap-Finanzwerten um ~77%), was die Interpretierbarkeit des Signals ausgerechnet in der Periode einschränkt, die es laut Kritik am stärksten trägt — ein potenzielles Zirkularitätsproblem.

### h) Bekannte Kritik/Widerlegungen

Neben der 2008-Sensitivität (Punkt d) ist grundsätzlich zu beachten, dass Markttiming-Signale mit R² im niedrigen zweistelligen Prozentbereich auf Monatsbasis zwar statistisch bemerkenswert sind (relativ zur üblichen Größenordnung von 1–3% R² in der Return-Predictability-Literatur), aber ökonomisch bescheidene, nicht spektakuläre Sharpe-Verbesserungen implizieren (die berichteten 300 Bp Nutzengewinn p.a. sind real, aber kein "Free Lunch"-Ausmaß). Zusätzlich: Aggregierte Prädiktoren dieser Art sind historisch anfällig für nachträglich entdeckte Data-Mining- oder Small-Sample-Verzerrungen (klassisches Problem der Return-Predictability-Literatur seit Goyal & Welch 2008).

---

## Kandidat 3: Short-Squeeze-Harvesting (systematischer Long in Crowded-Short-Titeln)

Dieser dritte Kandidat dreht Miller/Asquith-Pathak-Ritter um: Statt hohes Short Interest als Shortsignal zu nutzen, versucht die Strategie, die Squeeze-Prämie selbst zu vereinnahmen — systematischer Long-Einstieg in Aktien mit hohem Short Interest, hohem Days-to-Cover und hoher Utilization, in der Erwartung wiederkehrender Short-Squeeze-Ereignisse (GameStop als "Proof of Concept").

**Kurzbewertung entlang a–h:**

- **(a) Ökonomische Begründung:** Keine seriöse akademische Theorie postuliert einen strukturell positiven Erwartungswert für diese Seite des Trades. Im Gegenteil: Die Lottery-Demand-/Skewness-Präferenz-Literatur (verwandt mit dem MAX-Effekt) legt nahe, dass Titel mit hoher positiver Skewness-Erwartung (Squeeze-Potenzial) systematisch **überbezahlt** werden, was zu **niedrigeren**, nicht höheren erwarteten Renditen führt.
- **(b) Limits to Arbitrage:** Keine relevante Constraint auf der Long-Seite (kein Leihmarkt-Problem beim Kaufen einer Aktie) — das eigentliche Risiko ist Overpaying/Crowding auf der eigenen Seite plus extreme Einzeltitel-Volatilität.
- **(c) Originalstudien:** Es existiert keine mir bekannte, im Volltext verifizierte akademische Studie, die einen validierten, positiven Netto-Erwartungswert für eine systematische "Long-Squeeze-Candidates"-Strategie dokumentiert. Die verfügbare Literatur (Allen/Haas/Pirovano/Tengulov 2025) beschreibt **Basisraten** von Squeeze-Ereignissen (0,39% Market-Squeeze-Tage in den USA, ~9,9% Quartalsinzidenz), liefert aber keine Evidenz für eine handelbare, robuste Überrendite-Strategie auf dieser Basis.
- **(d) Out-of-Sample/Strukturbruch:** GameStop (Januar 2021) ist der einzige wirklich spektakuläre Fall dieser Größenordnung in der modernen Marktgeschichte — ein einzelnes Ereignis ist keine Grundlage für eine systematische Strategie (Survivorship-/Selection-Bias: für jeden GameStop gibt es zahlreiche hoch geshortete Aktien, die einfach weiter fielen, weil sie aus fundamentalen Gründen zu Recht geshortet wurden).
- **(e) Kosten:** Keine Borrow-Fee (Long-Position), aber hohe implizite Kosten durch weite Spreads, hohe Optionsimplied-Vol (falls über Calls/Optionen gehebelt gespielt) und Slippage in Extremphasen; zusätzlich Ausführungsrisiko (im GameStop-Fall haben Broker wie Robinhood im Januar 2021 zeitweise den Kauf bestimmter Meme-Aktien eingeschränkt — ein weiteres, nicht modellierbares operationelles Risiko).
- **(f) Kapazität:** Sehr gering — die Zahl der Titel, die zu einem gegebenen Zeitpunkt echte Squeeze-Kandidaten sind, ist klein, und die Positionen sind naturgemäß illiquide/volatil.
- **(g) Regimeabhängigkeit:** Extrem episodisch — abhängig von einer spezifischen Marktmikrostruktur-Konstellation (Null-Kommission-Broker, Retail-Koordination über Social Media, Optionsdealer-Gamma-Verstärkung, Null-/Niedrigzinsumfeld mit Stimulus-Liquidität 2021). Diese Konstellation ist nicht beliebig reproduzierbar und seit 2021 zusätzlich durch verschärfte regulatorische Aufmerksamkeit (Payment-for-Order-Flow-Debatte, Broker-Risikomanagement) erschwert.
- **(h) Kritik:** Diese Strategie ist im Kern eine Wette auf ein seltenes Tail-Event ohne dokumentierten positiven Erwartungswert — strukturell näher an Glücksspiel/Lottery-Trading als an einer Asset-Pricing-Anomalie im akademischen Sinn.

**Urteil: KILL.** Es gibt keine belastbare akademische Evidenz für einen positiven Erwartungswert; die verfügbare Evidenz (Lottery-Demand-Literatur, niedrige Squeeze-Basisraten) deutet eher auf einen negativen Erwartungswert nach Kosten hin.

---

## Synthese und Gesamturteil

| Kandidat | Urteil | p(echte Ineffizienz) | Netto-Sharpe-Erwartung | Kernproblem |
|---|---|---|---|---|
| Cross-sektionales SI (kostenadjustiert) | WEAK | 0,30 | 0,0–0,2 | Fee frisst Alpha exakt dort, wo Signal stark ist (Drechsler & Drechsler); VW-Effekt fast null; Squeeze-Tail-Risiko unbegrenzt |
| Aggregiertes SI (Markttiming, RRZ 2016) | WEAK | 0,35 | 0,1–0,3 | Möglicherweise 2008-getrieben; kein bestätigter Post-2016-OOS-Test; aber strukturell fee-robust (Index-Implementierung) |
| Squeeze-Harvesting (Long Crowded Shorts) | KILL | 0,05 | <0 | Kein dokumentierter positiver Erwartungswert; Lottery-Demand-Muster; GameStop ist Einzelfall, kein System |

**Ehrliches Gesamturteil zur Klasse:** Die Short-Interest-Anomalieklasse ist **kein "totes" Forschungsfeld** im Sinne von "widerlegt" — die zugrunde liegende Informationshypothese (Shortseller sind im Schnitt informiert, Miller-Mechanismus existiert real) ist gut repliziert und ökonomisch plausibel. Aber sie ist auch **kein handelbares Alpha für einen Outsider-Investor ohne proprietäre Order-Flow- und Echtzeit-Fee-Daten**. Die Klasse illustriert einen Archetyp aus der Limits-to-Arbitrage-Literatur, der über die reine Renditebetrachtung hinausgeht: Es handelt sich größtenteils um eine **Risikoprämie für die Bereitschaft, konzentriertes, linksschiefes Short-Risiko zu tragen** (Drechsler & Drechsler-Interpretation), nicht um kostenlos geerntetes Mispricing. Wer die Prämie vereinnahmen will, muss auch das Tailrisiko tragen — und die Fälle Melvin Capital, Citron Capital und White Square Capital (alle 2021) zeigen, dass dieses Tailrisiko real und potenziell existenzbedrohend ist, nicht nur ein theoretisches Modellrisiko.

Der einzige Kandidat mit einer strukturell überzeugenden Antwort auf die Borrow-Fee-Falle ist das aggregierte Markttiming-Signal (Kandidat 2), weil es über Indexinstrumente statt Einzelaktien-Leihe implementiert wird — aber genau dieser Kandidat hat das schwächste bestätigte Out-of-Sample-Fundament (unklare 2008-Abhängigkeit, keine verifizierte Post-Publication-Erfolgsgeschichte). Es gibt also einen Trade-off zwischen "kostenrobust, aber evidenzschwach" (Kandidat 2) und "evidenzstark, aber kostenfragil" (Kandidat 1) — keiner der beiden vereint beide Eigenschaften, weshalb kein CANDIDATE-Urteil vergeben wird.

---

## Datenlücken und Einschränkungen dieser Recherche

- Kein Volltext-Zugriff auf die Originalpapiere (nur Suchmaschinen-Zusammenfassungen/Abstracts); exakte t-Statistiken sind, wo nicht explizit in den Suchergebnissen genannt, bewusst **nicht** erfunden worden, sondern es wurden nur die tatsächlich gefundenen Effektgrößen (Basispunkte, R², Prozentangaben) berichtet.
- Die Kritik "RRZ-2016-Ergebnis verschwindet ohne 2008" stammt aus einer Suchmaschinen-Synthese, nicht aus verifiziertem Primärtext — mit entsprechendem Caveat übernommen.
- Borrow-Fee-/Utilization-Zeitreihen (IHS Markit, S3 Partners, Ortex) sind kostenpflichtig und konnten nicht direkt geprüft werden; alle Fee-bezogenen Zahlen stammen aus akademischen Sekundärquellen (primär Drechsler & Drechsler).
- Für einen rigorosen eigenen Backtest mit freien Daten ist Kandidat 1 nur mit der Einschränkung "kein echtes Fee-Overlay" durchführbar, Kandidat 2 ist am saubersten mit freien Daten testbar.

---

## Quellen (aus Websuche, Juli 2026)

- [Short Interest and Aggregate Stock Returns (Rapach, Ringgenberg, Zhou 2016) — SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2474930)
- [Short Interest and Aggregate Stock Returns — ScienceDirect/JFE](https://www.sciencedirect.com/science/article/abs/pii/S0304405X16300320)
- [Short Interest and Aggregate Stock Returns: International Evidence — Review of Asset Pricing Studies](https://academic.oup.com/raps/article/13/4/691/7127046)
- [Which Shorts Are Informed? (Boehmer, Jones, Zhang 2008) — SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=855044)
- [Which Shorts Are Informed? — Journal of Finance, Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2008.01324.x)
- [The Shorting Premium and Asset Pricing Anomalies (Drechsler & Drechsler) — NBER Working Paper 20282](https://www.nber.org/system/files/working_papers/w20282/w20282.pdf)
- [The Shorting Premium and Asset Pricing Anomalies — SSRN](https://papers.ssrn.com/abstract=2387099)
- [Short Interest and Stock Returns (Asquith, Pathak, Ritter) — NBER Working Paper 10434](https://www.nber.org/system/files/working_papers/w10434/w10434.pdf)
- [Short Interest, Institutional Ownership, and Stock Returns — Warrington/Ritter PDF](https://site.warrington.ufl.edu/ritter/files/2015/04/Short-interest-institutional-ownership-and-stock-returns-2005-08.pdf)
- [Short-Selling Risk (Engelberg, Reed, Ringgenberg 2018) — SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2312625)
- [Short Selling Risk — Rady School of Management PDF](https://rady.ucsd.edu/faculty/directory/engelberg/pub/portfolios/SHORT_RISK.pdf)
- [Dynamic Equilibrium with Costly Short-Selling and Lending Market — Review of Financial Studies](https://academic.oup.com/rfs/article/37/2/444/7243191)
- [How prevalent are short squeezes? Evidence from the US and Europe (Allen, Haas, Pirovano, Tengulov 2025) — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0378426625000561)
- [How Prevalent Are Short Squeezes? — SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4526147)
- [Shackling Short Sellers: The 2008 Shorting Ban — Review of Financial Studies](https://academic.oup.com/rfs/article/26/6/1363/1595651)
- [Shackling Short Sellers: The 2008 Shorting Ban — Harvard Law School Forum](https://corpgov.law.harvard.edu/2013/05/23/shackling-short-sellers-the-2008-shorting-ban/)
- [The 2008 short sale ban: Liquidity, dispersion of opinion, and cross-section of returns — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0378426611000471)
- [Anomalies across the globe: Once public, no longer existent? (Jacobs & Müller 2020) — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0304405X19301618)
- [GameStop short squeeze — Wikipedia](https://en.wikipedia.org/wiki/GameStop_short_squeeze)
- [How Much did Hedge Funds Lose on GameStop?](https://infinityinvesting.com/gamestop-hedge-fund/)
- [Identifying Crowded Names — Q1 2021 Earnings Season — Omega Point](https://www.omegapoint.ai/factor-spotlight-article/identifying-crowded-names-q1-2021-earnings-season)
