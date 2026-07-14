```yaml
agent: 09
klasse: "Reverse Splits"
websuche_verfuegbar: ja
strategien:
  - name: "Post-Reverse-Split Short-Drift (Short reverse-gesplitteter Aktien nach Ex-Datum, 6-36 Monate)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 4
      signifikanz_nach_mtk: 3
      regimestabilitaet: 3
      handelbarkeit: 2
      kapazitaet: 1
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.45
    netto_sharpe_erwartung: "0.0-0.2 nach realistischen Kosten; brutto ggf. 0.3-0.5"
    kernrisiko: "Borrow-Kosten/Non-Availability und FINRA-4210-Margin bei Sub-5-USD-Aktien fressen die Prämie genau in dem Segment, in dem der Effekt am größten ist; Short-Squeeze- und Buy-in-Risiko bei dünnem Float bei gleichzeitig extrem geringer Kapazität."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "SEC EDGAR Full-Text-Search (8-K Item 5.03) fuer Event-Identifikation + Stooq/Yahoo Finance fuer Kurse (kein Ken-French- oder Standard-Datensatz verfuegbar, da keine etablierte Faktor-Anomalie)"
  - name: "Serielle/multiple Reverse Splits als verstaerktes Distress-Short-Signal"
    urteil: KILL
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 3
      handelbarkeit: 1
      kapazitaet: 1
      kostenrobustheit: 1
    p_echte_ineffizienz: 0.35
    netto_sharpe_erwartung: "~0.0 bis leicht negativ nach Kosten"
    kernrisiko: "Genau die Untergruppe mit dem staerksten dokumentierten Effekt (Crutchley/Swidler: 65% Delisting/Liquidation) ist laut Originalstudie selbst noch illiquider als einfache Reverse-Split-Titel; oft kein Borrow verfuegbar, Trading-Halts und Uplisting-Verlust (OTC/Pink) schneiden Prime-Broker-Shortability exakt dann ab, wenn die These greifen wuerde."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
  - name: "Regulaerer (Forward) Stock-Split Long-Drift (Kontrastkandidat, long)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 1
      regimestabilitaet: 2
      handelbarkeit: 4
      kapazitaet: 3
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "~0.0"
    kernrisiko: "Effekt verschwindet bei methodisch sauberer Messung ab Ex-Datum statt Ankuendigungsdatum (Byun/Rozeff 2003, n=12.747); klassisches Artefakt langfristiger BHAR-Event-Studies (Benchmark-/Skewness-Bias, Fama 1998, Mitchell/Stafford 2000)."
    testbar_mit_freien_daten: nein
    freie_datenquelle: "-"
```

# Anomalieklasse: Reverse Splits — Adversarial Review

**Agent 09 | Juli 2026 | Nullhypothese: Es gibt kein handelbares Netto-Alpha in dieser Klasse**

Websuche war während dieser Recherche funktionsfähig; die im Folgenden zitierten Studien und Zahlen stammen aus einer Kombination von Web-Recherche (Abstracts, Zitationen, Sekundärquellen) und internem Wissen. Primärquellen wurden dort, wo der Volltextzugriff fehlschlug (SSRN-PDF-Downloads, ScienceDirect-Paywalls), über Sekundärzitate (ResearchGate, RePEc/IDEAS, Kanzlei-Analysen, Thesis-Digests) plausibilisiert. Wo Zahlen aus Sekundärquellen leicht divergieren (siehe unten), wird das explizit als Fragilitätssignal gewertet, nicht geglättet.

---

## 0. Zusammenfassung des Urteils

Reverse Splits sind eines der ältesten dokumentierten "Anomalie"-Muster der Event-Study-Literatur (erste Arbeiten Anfang/Mitte der 1980er). Die Richtung des Effekts — negative Ankündigungsrenditen und negative langfristige Abnormal Returns nach Reverse Splits — ist über vier Jahrzehnte, mehrere unabhängige Datenbanken und mittlerweile auch internationale Stichproben (24 entwickelte Märkte) bemerkenswert robust reproduziert worden. Das ist ungewöhnlich stabil für eine Alt-Anomalie.

Aber: Die Autoren der methodisch sorgfältigsten Studie (Kim, Klein & Rosenfeld 2008) kommen selbst zu dem Schluss, dass die Ergebnisse "consistent with an economically efficient market" sind, sobald Shortselling-Restriktionen berücksichtigt werden. Das ist der zentrale Befund dieser Recherche: Die Klasse zerfällt fast exakt entlang der Trennlinie "brutto real vs. netto handelbar". Der ökonomische Effekt existiert; er konzentriert sich aber systematisch in genau dem Marktsegment (Sub-5-USD-Microcaps, oft OTC-migrierend), in dem Spreads, Borrow-Kosten, Marginanforderungen und Kapazität eine Monetarisierung im institutionellen Maßstab verhindern oder auf ökonomisch uninteressante Sharpe Ratios drücken. Mein Gesamturteil für die Klasse: **WEAK bis KILL** — kein CANDIDATE. Es gibt keinen Kandidaten in dieser Klasse, der die Bar "dokumentierte Post-Publication-Evidenz UND Kostenrobustheit" gleichzeitig reißt.

---

## 1. Kandidat 1: Post-Reverse-Split Short-Drift

### 1a) Ökonomische Begründung

Drei sich ergänzende Mechanismen werden in der Literatur genannt:

1. **Signaling / private Information + Marktunterreaktion**: Management wählt einen Reverse Split typischerweich *weil* es keine fundamentale Erholung des Aktienkurses erwartet und stattdessen strukturell (Listing-Erhalt, institutionelle Zulassungsschwellen) reagieren muss. Der Split selbst überträgt negative private Information, auf die der Markt gemäß Desai & Jain (1997) systematisch *unterreagiert* — daher die anhaltende Drift statt eines einmaligen Sprungs am Ankündigungstag.
2. **Nominal-Price-Illusion bei Retail-Investoren**: Retail-Anleger bevorzugen nominal "billige" Aktien (Green & Hwang 2009-artige Befunde zu Nominalpreis-Präferenzen); nach einem Reverse Split verschwindet dieser Nominalpreis-Reiz, was Nachfrage strukturell verändert.
3. **Künstliche institutionelle Nachfrage-Spitze**: Sobald der Kurs die $5-Schwelle überschreitet, dürfen viele institutionelle Mandate (Investment Policy Statements, Prime-Broker-Margin-Regeln) die Aktie erstmals wieder halten. Das erzeugt einen kurzfristigen, nicht fundamental getriebenen Kaufimpuls direkt nach dem Split, der die nachfolgende Korrektur/Drift verzögert und verstärkt (konsistent mit Befunden zu steigenden institutionellen Beständen bei Splits mit Vorsplit-Preis < $5 und Nachsplit-Preis > $5).

Wer die Fehlbewertung verursacht: primär Retail- und "constrained" institutionelle Nachfrage kurz nach dem Event; die Korrektur erfolgt graduell über 12-36 Monate, was auf eine strukturelle Friktion (begrenzte Shortability, s.u.) als Haupt-Erhaltungsmechanismus hindeutet, nicht auf einen reinen Behavioral-Bias, der sich sofort auflösen würde.

### 1b) Limits to Arbitrage

Das ist der entscheidende Abschnitt für diese Klasse:

- **Borrow-Kosten**: Microcap/Penny-Stock-Borrow-Raten liegen typischerweise bei 5-50% p.a. für "hard to borrow"-Namen, bei gehypten/eng-Float-Titeln nicht selten über 100% p.a., in Extremfällen (2024 dokumentiert) über 1.000% p.a. annualisiert. Reverse-Split-Titel sind fast per Definition Microcaps mit geringem Streubesitz.
- **FINRA Rule 4210 / Reg-T-Sondermargin**: Für Aktien unter $2,50-$5 gelten verschärfte Maintenance-Margin-Regeln (oft nahe 100% des Positionswerts statt der üblichen 150% Reg-T-Leverage), was die Kapitaleffizienz einer Shortposition massiv verschlechtert — genau in dem Preissegment, in dem der historische Effekt am stärksten ist.
- **Locate-Anforderungen (Reg SHO Rule 203)**: Natürliche Verleiher (Indexfonds, große long-only-Bestände) halten diese Namen kaum, daher ist die Leihpool-Tiefe strukturell dünn und volatil; Recalls und Buy-ins sind häufig.
- **Delisting-/OTC-Migration**: Ein erheblicher Teil der Reverse-Split-Firmen wird binnen weniger Jahre von der Hauptbörse delisted (siehe Kandidat 2) und wandert in den OTC/Pink-Markt. Prime Broker schließen OTC-Titel häufig komplett von Shortability aus — der Moment, in dem die Distress-These am stärksten auszahlen würde, ist oft der Moment, in dem die Position technisch nicht mehr haltbar ist bzw. zwangsweise eingedeckt wird.
- **Short-Squeeze-Risiko**: Enger Float + hohes Short-Interest + dünne Liquidität ist exakt das strukturelle Setup, das Short-Squeezes (Meme-Stock-Dynamik seit 2021) begünstigt. Payoff-Verteilung ist damit stark linksschief für den Shortseller: viele kleine Gewinne, seltene aber sehr große Verluste.

Blau, Cox, Griffith & Voges (Journal of Financial Markets, 2023) zeigen mittels Diff-in-Diff, dass Leerverkaufsaktivität erst *nach* der Reverse-Split-Ankündigung ansteigt (nicht vorher) und dass Shortseller um diese Events herum *nicht* überdurchschnittlich informiert sind. Interpretation: Sophisticated Trader positionieren sich reaktiv, nicht antizipativ — konsistent damit, dass ein systematisches Pre-Positioning wegen der oben genannten Friktionen unattraktiv ist.

### 1c) Originalstudien

| Studie | Stichprobe | Zeitraum | Kernresultat |
|---|---|---|---|
| Woolridge & Chambers (1983) | Reverse Splits | ~1962-1980 | Ankündigungsrendite ca. -4,8% |
| Han (1995), JFQA | Reverse Splits | — | Signifikant negative Renditen um Ex-Datum; Liquiditätseffekte |
| **Desai & Jain (1997)**, J. Business 70(3) | 5.596 Splits, **76 Reverse Splits** | 1976-1991 | 1J-BHAR Reverse Split: **-10,76%**; 3J-BHAR: **-33,90%** (Kontrast: Forward Split 1J +7,05%, 3J +11,87%) |
| **Kim, Klein & Rosenfeld (2008)**, Financial Management 37(2) | **1.612 Reverse Splits** | 1962-2001 | Signifikant negative 3-Jahres-Abnormal-Returns und schwächere operative Performance vs. Matched Firms; Effekt statistisch nur signifikant für Post-Split-Preis ≤ $5; explizite Schlussfolgerung: Shortselling-Restriktionen verhindern Profitrealisierung — "consistent with an economically efficient market" |

Anmerkung zur Stichprobengröße: Desai & Jain haben nur **n=76** Reverse-Split-Events — eine für ein 3-Jahres-BHAR-Ergebnis mit derart großer Effektgröße (-33,9%) kritisch kleine Stichprobe, anfällig für einzelne Ausreißer-Titel (Survivorship/Idiosynkrasie). Kim/Klein/Rosenfeld mit n=1.612 ist die belastbarere Referenz.

### 1d) Out-of-Sample-/Post-Publication-Evidenz (2015-2026)

- **Zaremba, Okoń, Asyngier & Schroeter (2019)**, Research in International Business and Finance 47: **>5.000 Reverse Splits in 24 entwickelten Märkten, 1990-2016**. Bestätigt Unterperformance (ca. 18 Monate Persistenz) in Nordamerika, Europa und Asien-Pazifik. Zentraler Zusatzbefund: Die abnormale Performance wird **fast ausschließlich von Microcaps/Penny Stocks getrieben** — also exakt dem Segment mit den höchsten Handelskosten. Das ist ein starkes Warnsignal: Der Effekt ist dort am größten, wo er am wenigsten monetarisierbar ist ("phantom alpha"-Muster, wie es auch beim Size- und Distress-Faktor dokumentiert ist).
- **Neuhauser & Thompson (2015/2016)**, Journal of Business Research: 1.206 Reverse Splits, 1995-2011. Nur ca. 500/1.206 (**41%**) überleben 5+ Jahre eigenständig; ca. 47% gehen in Insolvenz/Delisting wegen Nichterfüllung von Listing-Standards, ca. 11% werden übernommen. Bestätigt die Distress-Signalwirkung, aber die hohe Delisting-Quote ist zugleich ein Datenbank-Bias-Warnsignal (s. 1h) und ein Shortability-Warnsignal (s. 1b).
- **Blau, Cox, Griffith & Voges (2023)**, Journal of Financial Markets 65: siehe 1b — Shortseller sind reaktiv, nicht prädiktiv informiert.
- Decay-Schätzung: Eine punktgenaue Prä-/Post-Publication-Decay-Zahl wie bei McLean & Pontiff (2016) existiert für Reverse Splits nicht (die Anomalie ist nicht Teil von deren 97-Prädiktoren-Set). Als groben Anhaltspunkt für die Größenordnung ziehe ich McLean/Pontiff heran: Publizierte Anomalien verlieren im Schnitt **~58% ihrer In-Sample-Rendite post-Publikation** (bzw. ~26% bereits out-of-sample vor Publikation). Reverse Splits sind eine Alt-Anomalie (Erstpublikation ~1983), die 40+ Jahre später (Zaremba et al. 2019, Blau et al. 2023) im Vorzeichen noch replizierbar ist — das spricht für eine strukturelle statt rein statistische Erklärung. Gleichzeitig variiert die *Magnitude* zwischen Studien um den Faktor 3-5 (10,8% vs. 33,9% vs. teils zitierte 15,6/36/54% je nach Jahr in journalistischen Sekundärzitaten von KKR-artigen Zahlen) — diese Streuung ist selbst ein Fragilitätsindikator, konsistent mit dem allgemeinen Muster, dass Langfrist-BHAR-Punktschätzungen stark methodenabhängig sind (Benchmarkwahl, Skewness-Bias, Kalenderzeit- vs. Event-Zeit-Aggregation; Fama 1998, Mitchell & Stafford 2000, Kothari & Warner 1997).
- **Regulatorisches Strukturbrechen 2024/2025**: Nach einem Rekordjahr 2023 (495 Reverse Splits bei US-gelisteten Firmen) haben Nasdaq und NYSE 2024/2025 (SEC-Genehmigung Januar 2025) die Regeln verschärft: Firmen, die innerhalb von zwei Jahren einen kumulativen Reverse-Split-Faktor von ≥250:1 erreichen, verlieren die Cure-Period und werden ohne Aufschub delisted. Das verändert das zukünftige Sample (weniger serielle Reverse-Splitter, ggf. schnelleres direktes Delisting statt "Zombie"-Verlängerung) — ein Regimebruch, dessen Effekt auf die Rendite-Statistik noch nicht in publizierter Literatur vermessen ist.
- Aktuelle Marktbeobachtung Mitte 2026: Berichte (Investing.com, Wall Street Horizon, Kavout, Juni/Juli 2026) beschreiben ein "K-shaped"-Muster, in dem reguläre Forward-Splits 2026 deutlich zurückgegangen sind, während Reverse Splits (auch bei bekannten Namen) anhaltend/dominant bleiben — konsistent mit der These, dass Reverse Splits ein defensives Signal für Bewertungsschwäche in einem Teil des Marktes sind, während der Rest boomt.

### 1e) Kosten

- **Spreads**: Microcap-/Penny-Stock-Spreads liegen häufig im Bereich von 1-5%+ des Kurses (bei Sub-Dollar-Titeln teils zweistellig in relativen Prozentpunkten); allein Round-Trip-Spreadkosten können einen zweistelligen Prozentsatz der erwarteten Drift auffressen.
- **Borrow-Fees**: 5-50% p.a. Normalfall, Spitzen >100-1.000% p.a. (s. 1b). Bei einer Halteperiode von 12-36 Monaten (wie in den Originalstudien gemessen) frisst allein der Borrow-Fee bei einem mittleren Satz von z.B. 15-20% p.a. über 2-3 Jahre kumulativ 30-60% Rendite auf — das liegt in derselben Größenordnung wie die dokumentierte Brutto-Drift selbst.
- **Market Impact**: Bei ADV oft im Bereich von wenigen Hunderttausend bis niedrigen Millionen USD/Tag ist schon eine mittlere institutionelle Positionsgröße (>5-10% ADV) mit erheblichem Impact verbunden; Aufbau/Abbau muss über Tage gestreckt werden, was Timing-Risiko erhöht.
- **Netto-Rendite-Realität**: Nach Spread, Borrow und Impact ist die Bandbreite plausibler Netto-Sharpe-Ratios sehr niedrig; die explizite Schlussfolgerung von Kim/Klein/Rosenfeld (2008) — dass die Ergebnisse mit Markteffizienz nach Reibungskosten vereinbar sind — sollte als Ankerpunkt ernst genommen werden, nicht wegdiskutiert werden.

### 1f) Kapazität

Grobe Schätzung: ca. 200-500 Reverse Splits p.a. bei US-gelisteten Firmen (2023: 495, Rekordjahr). Davon sind nur ein Bruchteil überhaupt liquide/borrow-fähig genug für ein institutionelles Buch. Bei angenommenen Positionsgrößen von $50.000-$300.000 pro Name (um Market Impact <10% ADV zu halten) und vielleicht 50-150 gleichzeitig haltbaren, tatsächlich shortbaren Namen ergibt sich ein realistisches Gesamtbuch von **grob USD 20-80 Mio.** für eine dedizierte Short-Strategie dieser Klasse — deutlich zu klein für ein institutionelles Multi-Strategie-Mandat als Standalone-Sleeve, allenfalls als sehr kleine Satellite-Position innerhalb eines breiteren Microcap-Short-/Quality-Short-Buchs sinnvoll.

Die spiegelbildliche "Long-seitige Vermeidungsstrategie" (Reverse-Split-Titel aus einem bestehenden Long-only-Microcap-Portfolio ausschließen/untergewichten) ist praktisch unbegrenzt kapazitätsstark, ist aber keine Alpha-Quelle, sondern ein Risiko-Overlay/Negativ-Screen.

### 1g) Regimeabhängigkeit und Tail-Risiko

- Der Effekt scheint über verschiedene Makro-Regime (1962-2016 laut internationalen Daten) im Vorzeichen stabil, was für einen strukturellen statt zyklischen Ursprung spricht.
- Tail-Risiko ist jedoch klar linksschief für den Shortseller: Short-Squeeze-Episoden (dünner Float, hohes Short-Interest, mediengetriebene Retail-Aufmerksamkeit — das "Meme-Stock"-Muster seit 2021) können einzelne Positionen um mehrere hundert Prozent gegen den Shortseller laufen lassen, mit potenziell unbegrenztem Verlust und Zwangs-Eindeckung bei Borrow-Recall.
- Regulatorischer Regimebruch 2024/2025 (s. 1d) verändert die zukünftige Grundgesamtheit der Events.

### 1h) Bekannte Kritik / Widerlegungen

- **Datenbank-/Survivorship-Bias**: CRSP und ähnliche Datenbanken behandeln Delisting-Renditen uneinheitlich (Shumway 1997 Delisting-Bias-Problematik ist Standardkritik an allen Distress-/Microcap-Langfriststudien). Da 47-65% der Reverse-Split-Firmen (Neuhauser/Thompson; Crutchley/Swidler) binnen weniger Jahre delisted werden, hängt ein erheblicher Teil der gemessenen Brutto-Rendite an der korrekten Behandlung der Delisting-Rendite — ein Bereich, der historisch für Fehlspezifikation bekannt ist (in beide Richtungen: sowohl Über- als auch Unterschätzung der wahren Verlustrendite möglich).
- **Mikrostruktur-Artefakte**: Bei Sub-Dollar-/Sub-5-Dollar-Titeln sind Bid-Ask-Bounce, Spätnachmittags-Illiquidität und Stale-Pricing bekannte Verzerrungsquellen für gemessene Tagesrenditen und CAR/BHAR-Schätzungen.
- **Methodenabhängigkeit langfristiger Event Studies generell**: Fama (1998) und Mitchell & Stafford (2000) zeigen, dass BHAR-basierte Langfristresultate extrem sensitiv auf Benchmark-Wahl (Size/BM-matched Firm vs. Portfolio) und Aggregationsmethode (Buy-and-Hold vs. Kalenderzeit-Faktorregression) reagieren. Ein Kalenderzeit-Ansatz (der ökonomisch der korrekten Handhabung eines diversifizierten Portfolios entspricht) tendiert generell dazu, kleinere und weniger signifikante Effekte zu liefern als Event-Zeit-BHAR — dieses Muster zeigt sich explizit bei Forward Splits (s. Kandidat 3) und ist mit hoher Wahrscheinlichkeit auch bei Reverse Splits wirksam, auch wenn mir keine Studie bekannt ist, die dies für Reverse Splits explizit mit Kalenderzeit-Faktorregression re-testet — das ist selbst eine Forschungslücke und ein Warnsignal.
- **Eigenkritik der besten Studie**: Wie erwähnt kommt Kim/Klein/Rosenfeld (2008) selbst zu einem Effizienzurteil nach Frictions — das ist ungewöhnlich offen für eine Studie, die formal einen Anomalie-Befund publiziert, und sollte entsprechend hoch gewichtet werden.

### Urteil Kandidat 1: WEAK

Real, robust im Vorzeichen über 40+ Jahre und mehrere Kontinente — aber nach Kosten wahrscheinlich nahe Netto-Null bis leicht positiv, mit sehr geringer Kapazität und linksschiefer Tail-Risiko-Verteilung. Kein CANDIDATE, weil die Kostenrobustheit fehlt (Kriterium explizit gefordert) und die Originalautoren selbst Effizienz nach Friktionen attestieren.

---

## 2. Kandidat 2: Serielle/multiple Reverse Splits als verstärktes Distress-Signal

### 2a-h (kompakt, da strukturell Unterfall von Kandidat 1)

**Ökonomische Begründung**: Ein zweiter (dritter, vierter) Reverse Split innerhalb weniger Jahre ist ein noch stärkeres Signal für strukturelle Verzweiflung als ein Erstsplit — "wenn ein Reverse Split Verzweiflung signalisiert, ist ein mehrfacher Reverse Split ein Zeichen extremer Not" (Crutchley & Swidler 2013, Journal of Economics and Finance).

**Originalstudie**: Crutchley & Swidler (2013) zeigen, dass Firmen mit mehrfachen Reverse Splits niedrigere Folgerenditen UND **noch geringere Liquidität** als Einzel-Reverse-Split-Firmen aufweisen, und dass **65% der Mehrfach-Reverse-Split-Firmen letztlich liquidiert oder delisted werden**.

**Limits to Arbitrage**: Das ist der Casus knacksus dieses Kandidaten — die Studie selbst dokumentiert, dass genau die Untergruppe mit dem (vermutlich) stärksten Effekt noch illiquider ist als die Grundgesamtheit aus Kandidat 1. Borrow ist in dieser Untergruppe häufig gar nicht verfügbar; viele dieser Namen sind zum Zeitpunkt des zweiten/dritten Splits bereits OTC/Pink-gelistet, außerhalb des Universums, das die meisten Prime Broker überhaupt für Shortselling freigeben.

**Kosten/Kapazität**: Strikt schlechter als Kandidat 1 auf allen Dimensionen — kleinere Grundgesamtheit (Teilmenge), noch geringere Liquidität, noch höhere Borrow-Kosten (wo überhaupt verfügbar), höheres Halt-/Delisting-Risiko während der Haltedauer (was die Short-Position technisch "einfriert", ohne dass P&L realisiert werden kann — OTC-Notierungen und Halts können Positionen über Monate illiquide machen).

**Regime/Tail-Risiko**: Bimodale Auszahlung — entweder Totalverlust der Aktie (gut für Short) oder Short-Squeeze bei Turnaround-Spekulation/Übernahmegerücht (Crutchley/Swidler: ~11% der nicht-überlebenden Firmen werden übernommen, oft mit Kurssprung) — beide Enden der Verteilung sind für einen Shortseller mit Zwangs-Eindeckungsrisiko ungünstig händelbar.

**Kritik**: Kleine Stichprobe (Untermenge einer bereits kleinen Grundgesamtheit), keine mir bekannte unabhängige Replikation außerhalb der Originalstudie, hohes Risiko von Selection/Survivorship in der Klassifikation "seriell" (nur Firmen, die lange genug überleben, um einen zweiten Split zu versuchen, kommen überhaupt in die Stichprobe).

### Urteil Kandidat 2: KILL

Der ökonomische Mechanismus ist plausibel und die Delisting-Statistik eindrucksvoll — aber als **handelbare** Strategie scheitert sie noch deutlicher an denselben Friktionen wie Kandidat 1, potenziert statt gemildert. Besser als Aktien-Short lässt sich diese Distress-These ohnehin über Credit/Options/strukturierte Produkte ausdrücken, sofern überhaupt vorhanden — was aber bei diesen Marktkapitalisierungen praktisch nie der Fall ist (keine Optionsketten, kein Bond-Markt).

---

## 3. Kandidat 3 (Kontrast): Regulärer (Forward) Stock-Split Long-Drift

Zum Kontrast, wie im Mandat gefordert — die spiegelbildliche "positive" Anomalie.

**Originalstudie**: Ikenberry, Rankine & Stice (1996), JFQA 31(3): 1.275 2-für-1-Splits, Ankündigungsrendite +3,38%, **1-Jahres-Post-Split-Abnormal-Return +7,93%**. Desai & Jain (1997): 5.596 Forward Splits, 1J-BHAR +7,05%, 3J-BHAR +11,87%.

**Out-of-Sample/Widerlegung**: **Byun & Rozeff (2003)**, Journal of Finance 58(3), mit der deutlich größeren und längeren Stichprobe (**12.747 Splits, 1927-1996**): Wenn die Performance ab **Ex-Datum statt Ankündigungsdatum** gemessen wird, verschwindet der signifikante langfristige Abnormal Return. Für Splits ≥25% finden beide verwendeten Methoden (Size/BM-Referenzportfolio mit Bootstrapping, Kalenderzeit-Faktorregression) über den Gesamtzeitraum keine signifikant von Null verschiedene Performance. Fazit der Autoren: "the stock split evidence against market efficiency is neither pervasive nor compelling."

Das ist ein Lehrbuchbeispiel für Methodenabhängigkeit: Derselbe zugrunde liegende Datensatz-Typ liefert ein "Alpha" oder "kein Alpha", je nachdem ob man ab Ankündigung oder ab Ex-Datum misst, und ob man Event-Zeit-BHAR oder Kalenderzeit-Faktorregression verwendet.

**Kosten/Handelbarkeit**: Anders als Reverse Splits betreffen Forward Splits häufig große, liquide Namen (2026: z.B. prominente Large-Cap-Splits) — Handelbarkeit und Kapazität wären hier grundsätzlich kein Problem. Das Problem ist, dass der Effekt selbst nicht robust genug ist, um ihn zu handeln.

### Urteil Kandidat 3: KILL

Der Kontrast bestätigt das Gesamtbild der Klasse: Wo die Handelbarkeit gut wäre (große, liquide Forward-Split-Namen), ist der Effekt bei sauberer Methodik nicht signifikant von Null verschieden. Wo der Effekt am robustesten ist (Reverse Splits, Vorzeichen über 40 Jahre stabil), ist die Handelbarkeit am schlechtesten.

---

## 4. Übergreifende Beobachtungen

1. **Strukturelle Antikorrelation zwischen Effektgröße und Handelbarkeit**: Über alle drei Kandidaten hinweg zeigt sich dasselbe Muster wie bei vielen anderen "alten" Microcap-Anomalien (Size-Effekt, Distress-/Failure-Anomalie, Penny-Stock-Momentum): Der beobachtbare Effekt ist am stärksten genau dort, wo Spreads, Borrow-Kosten und Kapazität am ungünstigsten sind. Das ist entweder (a) der Preis, den der Markt für Illiquidität verlangt (Risikoprämie, nicht Ineffizienz), oder (b) eine reale Ineffizienz, die aber strukturell nicht in institutionellem Maßstab monetarisierbar ist. Für die Fondsallokation ist der Unterschied zwischen (a) und (b) irrelevant — in beiden Fällen ist das Netto-Sharpe-Profil nach Kosten unattraktiv.
2. **Datenbasis nicht frei verfügbar**: Anders als Standard-Faktoren (Value, Momentum, Size) gibt es keinen Ken-French-artigen, kuratierten, kostenlosen Datensatz für Stock-Split-/Reverse-Split-Ereignisse. Eine Replikation erfordert eigenständiges Event-Mining aus SEC-EDGAR-Volltextsuche (8-K Item 5.03, kostenlos, aber manuell/skriptbasiert aufwendig) kombiniert mit einer kostenlosen Kursquelle (Stooq, Yahoo Finance) — machbar, aber kein "Freitext-Ticker"-Task.
3. **Delisting-Bias ist in dieser Klasse besonders akut**: Da 40-65% der Reverse-Split-Firmen binnen weniger Jahre delisted werden, hängt jede Renditeschätzung kritisch an der (in Sekundärquellen oft nicht transparent gemachten) Behandlung von Delisting-Returns. Das ist eine der methodisch heikelsten Ecken der gesamten Event-Study-Literatur (Shumway 1997) und sollte bei jeder Eigenreplikation explizit adressiert werden, bevor man den Zahlen traut.
4. **Regimebruch 2024/2025**: Die neuen Nasdaq/NYSE-Delisting-Regeln zu seriellen Reverse Splits sind ein aktives, noch nicht in der akademischen Literatur vermessenes Strukturänderungsrisiko für jede Forward-Looking-Kalibrierung dieser Strategie.

## 5. Gesamtfazit

Reverse Splits sind keine tote Anomalie im Sinne von "Effekt existiert nicht" — das Vorzeichen der Unterperformance ist eines der am robustesten replizierten Muster in dieser Recherche, über 40+ Jahre und interkontinental bestätigt (Zaremba et al. 2019). Aber die Klasse ist nach ehrlicher Kostenrechnung **kommerziell tot bis grenzwertig**: Die maßgeblichste Studie kommt selbst zu einem Effizienzurteil nach Friktionen, die Effektgröße konzentriert sich nachweislich in den am wenigsten handelbaren Marktsegmenten, die Kapazität ist auf niedrige zweistellige bis niedrige dreistellige Millionen-USD-Beträge begrenzt, und das Tail-Risiko (Short-Squeeze, Borrow-Recall, Delisting-Einfrierung) ist strukturell gegen den Shortseller verzerrt. Der Kontrastkandidat (Forward-Split-Long-Drift) fällt bei sauberer Methodik komplett in sich zusammen. Kein Kandidat dieser Klasse erreicht die CANDIDATE-Schwelle. Für ein institutionelles Multi-Strategie-Buch ist mein Rat: **nicht allokieren**, allenfalls als kostenlose Nebenprodukt-Information (Negativ-Screen für bestehende Long-Microcap-Bücher) nutzen.
