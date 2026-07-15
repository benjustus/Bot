```yaml
agent: 23
klasse: "Makroregime & Ankündigungseffekte"
websuche_verfuegbar: ja
strategien:
  - name: "Pre-FOMC Announcement Drift (Lucca & Moench 2015)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 1
      regimestabilitaet: 1
      handelbarkeit: 4
      kapazitaet: 3
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.15
    netto_sharpe_erwartung: "0.0-0.1 (post-2015 statistisch nicht von Null verschieden)"
    kernrisiko: "Effekt an strukturell gesunkene geldpolitische Unsicherheit (VIX-Rückgang) gebunden und seit ca. 2015 in mehreren unabhängigen Studien nicht mehr nachweisbar; Wette auf Rückkehr eines verschwundenen Musters bei fortbestehendem Tail-Risiko durch Policy-Überraschungen ohne kompensierende Prämie"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "SPY/ES-Tagesdaten (Yahoo Finance) + FOMC-Sitzungskalender (federalreserve.gov)"
  - name: "Makro-Ankündigungsprämie (Savor & Wilson 2013: CPI-/NFP-/FOMC-Tage)"
    urteil: WEAK
    scores:
      reproduzierbarkeit: 3
      signifikanz_nach_mtk: 2
      regimestabilitaet: 2
      handelbarkeit: 4
      kapazitaet: 4
      kostenrobustheit: 3
    p_echte_ineffizienz: 0.25
    netto_sharpe_erwartung: "0.1-0.3 brutto (Long-Beta an Ankündigungstagen); nach Marktbeta-Adjustierung vermutlich nahe 0"
    kernrisiko: "Kaum unterscheidbar von reiner, im Voraus bekannter Markt-Beta-Exposure an Tagen mit hohem systematischem Risiko; aktuelle Kritik (Management Science 2024) zeigt, dass die bedingte Volatilität an Ankündigungstagen entgegen der Risikoprämien-Theorie kaum fällt"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "CRSP/^GSPC Tagesrenditen + Fama-French Mkt-RF (Ken French Data Library) + BLS/BEA/FOMC-Terminkalender"
  - name: "FOMC-Zyklus-Effekt / gerade Wochen (Cieslak, Morse & Vissing-Jørgensen 2019)"
    urteil: KILL
    scores:
      reproduzierbarkeit: 2
      signifikanz_nach_mtk: 1
      regimestabilitaet: 1
      handelbarkeit: 4
      kapazitaet: 4
      kostenrobustheit: 2
    p_echte_ineffizienz: 0.10
    netto_sharpe_erwartung: "ca. 0.0 nach 2015"
    kernrisiko: "Mechanismus (informelle Fed-Kommunikation im 2-Wochen-Rhythmus der Board-Sitzungen) an eine seither veränderte institutionelle Struktur gebunden; Replikationen für 2014-2023 finden den Effekt nicht mehr; hohe Rebalancing-Frequenz (alle 2 Wochen) erhöht die Kostenlast bei verschwindendem Signal"
    testbar_mit_freien_daten: ja
    freie_datenquelle: "^GSPC Tagesrenditen + FOMC-Sitzungskalender (federalreserve.gov)"
```

# Anomalieklasse: Makroregime & Ankündigungseffekte
## Independent Quant Research Memo — Agent 23
Stand: Juli 2026. Nullhypothese: Es gibt kein echtes, handelbares Alpha in dieser Klasse. Diese Nullhypothese wird durch die Evidenz weitgehend **nicht widerlegt**.

Evidenzbasis: Websuche verfügbar und durchgeführt (WebSearch/WebFetch funktionierten). Es wurden Originalstudien, mehrere Post-Publication-Replikationen (2018–2025) und mindestens eine direkte theoretische Widerlegung der Risikoprämien-Interpretation (2024) recherchiert. Wo Volltexte nicht zugänglich waren (Paywall, z.B. Tandfonline 403), wird dies vermerkt und auf Abstracts/Sekundärquellen zurückgegriffen.

---

## Zusammenfassung des Urteils

Von den drei untersuchten Kandidaten ist **keiner** ein CANDIDATE. Der prominenteste und am häufigsten zitierte Effekt der Klasse — der Pre-FOMC-Announcement-Drift von Lucca & Moench (2015) — gehört zu den am klarsten dokumentierten Fällen von **Post-Publication-Decay** in der gesamten Asset-Pricing-Literatur: Der Effekt ist in unabhängigen Out-of-Sample-Studien (Kurov, Wolfe & Gilbert 2021) quantifizierbar um ca. 79–80% eingebrochen und seit 2016 statistisch nicht mehr von Null unterscheidbar. Der eng verwandte "FOMC-Zyklus"-Effekt (gerade Wochen, Cieslak/Morse/Vissing-Jørgensen 2019) zeigt dasselbe Muster. Die breitere "Makro-Ankündigungsprämie" (Savor & Wilson 2013, CPI/NFP/FOMC) ist widersprüchlicher: Es gibt sowohl neuere Bestätigungen (NBER-Papier Ai/Bansal/Guo 2023/2024, Fed-FEDS-Note 2025) als auch eine fundamentale methodische Widerlegung (Management-Science-Papier 2024, das zeigt, dass die für eine Risikoprämie nötige Volatilitätsreduktion an Ankündigungstagen empirisch nicht auftritt). Dieser Kandidat wird daher als WEAK statt KILL eingestuft — aber explizit nicht als CANDIDATE, weil die Post-Publication-Evidenz selbst unter Forschern umstritten ist und keine robuste, unangefochtene Bestätigung vorliegt.

---

## Kandidat 1: Pre-FOMC Announcement Drift (Lucca & Moench 2015)

### a) Ökonomische Begründung
Lucca & Moench postulieren, dass Investoren vor FOMC-Ankündigungen eine Prämie für die Übernahme von geldpolitischem Unsicherheitsrisiko verlangen, die sich in den 24 Stunden vor dem Announcement realisiert (Auflösung der Unsicherheit bei Bekanntgabe). Wer zahlt: Investoren, die kurzfristig Absicherung/Liquidität gegen das Ankündigungsrisiko nachfragen (z.B. weniger informierte oder risikoaverse Marktteilnehmer, die Positionen vor dem Termin schließen wollen), zahlen implizit eine Prämie an diejenigen, die bereit sind, das Pre-Announcement-Risiko zu tragen. Ein alternativer, später einflussreicher Mechanismus stammt von Laarits (2020, "Pre-Announcement Risk"/"Premium for Heightened Uncertainty"): Die Drift entsteht, weil Marktteilnehmer eine gegebene Fed-Aktion je nach vorangegangenen Wirtschaftsnachrichten unterschiedlich interpretieren (als Signal über die Konjunktur vs. als Signal über die Fed-Reaktionsfunktion) — kein Informationsleck nötig, aber auch kein robustes, handelbares Risikofaktor-Argument. Wichtig: Laarits zeigt, dass der VIX zwei Tage vor dem Meeting die Drift-Größe stark vorhersagt (eine Standardabweichung VIX-Anstieg → +31bp höhere Pre-FOMC-Rendite) — das liefert zugleich die Erklärung für den späteren Zerfall (siehe d).

### b) Limits to Arbitrage
Gering im klassischen Sinn: S&P-500-E-mini-Futures sind hochliquide, das Timing ist bekannt (FOMC-Termine werden Monate im Voraus veröffentlicht), Leerverkaufsbeschränkungen spielen keine Rolle, Kapitalkosten sind niedrig. Das eigentliche Limit ist statistischer, nicht struktureller Natur: Mit nur 8 Terminen pro Jahr lässt sich die Strategie nicht durch häufiges Reinvestieren skalieren; das Kapital ist 23,5 von 24 Stunden nicht im „Signal", sodass ein Arbitrageur entweder dauerhaft eine kleine Position hält oder aktiv timen muss — beides begrenzt die ökonomisch sinnvolle Kapitalallokation relativ zum übrigen Portfolio.

### c) Originalstudien
Lucca, D. & Moench, E. (2015), "The Pre-FOMC Announcement Drift", *Journal of Finance* 70(1), 329–371 (NY Fed Staff Report 512). Sample: September 1994 – März 2011 (ca. 17 Jahre, 136 FOMC-Meetings). Kernresultat: durchschnittliche Exzess-Rendite von **ca. 49 Basispunkten** in den 24 Stunden vor der Ankündigung (Vortagesschluss bis Ankündigungszeitpunkt), mit einer **t-Statistik von ca. 4–5**; dieser 24h-Zeitraum vereinnahmt nach Angaben der Autoren rund **80% der durchschnittlichen jährlichen Aktienmarktrendite** im Sample. Der Effekt ist außerhalb dieses engen Zeitfensters (an gewöhnlichen Tagen) nicht vorhanden — ein klassisches "Needle in a Haystack"-Ergebnis, das für Data-Mining-Bedenken anfällig ist (siehe h).

### d) Out-of-Sample-/Post-Publication-Evidenz (kritischer Punkt)
Dies ist der zentrale Befund dieser Recherche. Mehrere unabhängige Studien dokumentieren den Zerfall:

- **Kurov, A., Wolfe, M. H. & Gilbert, T. (2021), "The Disappearing Pre-FOMC Announcement Drift", Finance Research Letters 40** (SSRN 3134546; auch als NY Fed/PMC-Version verfügbar): Direkter Split der Post-2011-Periode. Für FOMC-Meetings mit Pressekonferenz sinkt die mittlere Pre-FOMC-Rendite von **44,5 Basispunkten** (April 2011 – Dez. 2015, n=20) auf **9,2 Basispunkte** (Jan. 2016 – Dez. 2019, n=20) — ein Rückgang von **ca. 79%**. Ein Wilcoxon-Rangsummentest verwirft die Gleichheit der zentralen Tendenz zwischen beiden Teilperioden auf dem 1%-Niveau. Für die Periode 2016–2019 ist die Pre-FOMC-Rendite (0,092%) statistisch nicht mehr von der Rendite an gewöhnlichen Tagen (0,054%) unterscheidbar. Die Autoren erklären dies mit gesunkener geldpolitischer Unsicherheit: durchschnittlicher VIX fällt von 17,7 (prä-ZLB-Exit) auf 14,7 (post-ZLB), signifikant auf 1%-Niveau; ein Post-ZLB-Dummy ist zunächst signifikant (Koeffizient −0,353, 5%-Niveau), wird aber insignifikant, sobald VIX kontrolliert wird — d.h. der Zerfall lässt sich vollständig durch gesunkene Unsicherheit erklären, nicht notwendigerweise durch Arbitrage-Aktivität. Das ist wichtig für die Bewertung: Es handelt sich nicht zwingend um "Alpha wegarbitriert", sondern eher um "Risikofaktor selbst kleiner geworden" — beides führt aber zum selben Resultat für einen heutigen Trader: kein Edge mehr vorhanden.
- **"The pre-FOMC announcement drift: short-lived or long-lasting? Evidence from financial and volatility markets" (Applied Economics, 2024, Tandfonline, Volltext nicht zugänglich/403):** Laut Abstract/Sekundärquellen nuanciertere Sicht — mögliche Persistenz in Volatilitätsmärkten (VIX-Futures) auch wenn der reine Aktienrenditen-Drift schwächer wird. Dies wird hier als Gegenevidenz mit reduziertem Gewicht vermerkt, da Primärtext nicht verifizierbar war.
- **Verwandter Befund (FOMC-Zykluseffekt, siehe Kandidat 3):** dasselbe Zerfallsmuster nach 2015, was die Robustheit des "Uncertainty-Decline"-Narrativs stützt.

Fazit d): Der prominenteste, am häufigsten zitierte Effekt der gesamten Makro-Ankündigungs-Literatur ist ein Lehrbuchbeispiel für Post-Publication-Decay — nicht nur graduelle Abschwächung, sondern faktisches Verschwinden in der zweiten Hälfte des Post-Publication-Zeitraums (2016–2019), mit einer sauber identifizierten ökonomischen Erklärung (VIX-Rückgang). Für 2020–2026 (Post-COVID, Zinserhöhungszyklus 2022–2023, erhöhte Unsicherheit) wäre a priori denkbar, dass die Drift wegen wieder gestiegener VIX-Niveaus zurückkehrt — hierzu wurde keine belastbare aktualisierte Studie mit Zahlen für 2020–2026 gefunden; dies ist eine Wissenslücke, die vor jeder Kapitalallokation zwingend mit aktuellen Daten (z.B. Backtest 2020–2026) zu schließen wäre.

### e) Kosten und Signalfrequenz/statistische Power
Kosten pro Trade sind sehr niedrig (E-mini S&P Futures, ein-Basispunkt-Bereich Spread+Kommission für institutionelle Größenordnungen). Das Problem ist nicht die Kostenseite, sondern die **statistische Power**: 8 FOMC-Termine/Jahr bedeuten selbst über 30 Jahre nur ca. 240–250 unabhängige Beobachtungen, und Subsample-Analysen (wie bei Kurov et al. nötig, um Regimewechsel zu erkennen) reduzieren dies auf n=20 pro Fenster — mit entsprechend breiten Konfidenzintervallen. Ein Sharpe Ratio, das auf 8 Ereignissen/Jahr basiert, hat selbst bei robustem Effekt eine sehr hohe Varianz der Sharpe-Schätzung von Jahr zu Jahr; die ursprüngliche t-Statistik von ~4 in der 17-Jahres-Stichprobe täuscht über die Fragilität einer Live-Umsetzung mit gleitendem Fenster hinweg.

### f) Kapazität und Handelbarkeit
Kapazität pro Einzelereignis ist sehr hoch (S&P-Futures-Markt ist extrem tief), aber die **effektive Strategiekapazität ist durch die Frequenz begrenzt**, nicht durch Marktliquidität: Ein Fonds kann pro Jahr nur 8-mal signifikantes Kapital in dieses Signal allokieren, was den Beitrag zum Gesamt-Sharpe eines Portfolios strukturell klein hält, selbst wenn der Effekt real wäre.

### g) Regimeabhängigkeit und Tail-Risiko
Der Effekt ist per Konstruktion regimeabhängig (siehe VIX-Erklärung oben) — das ist zugleich sein größtes Tail-Risiko: Man hält 24h vor jedem FOMC-Meeting eine Long-Aktienposition, exakt dem Ereignis ausgesetzt, das am ehesten eine Hawkish-Überraschung/Repricing auslösen kann (z.B. überraschende Zinserhöhung, hawkishe Forward Guidance, Bankenkrisen-Kontext wie März 2023). Das Ereignisrisiko ist strukturell gegen die Strategie gerichtet: Genau in Phasen hoher, unerwarteter geldpolitischer Unsicherheit (wenn die "Prämie" laut Theorie am größten sein sollte) ist auch das Verlustpotenzial bei negativen Überraschungen am größten — die Auszahlungsstruktur ist damit potenziell linksschief (kleine, häufige Gewinne, seltene große Verluste), was in den zitierten Durchschnittsrenditen nicht sichtbar wird.

### h) Bekannte Kritik/Widerlegungen
- Data-Mining/Multiple-Testing: Das 24h-Fenster ist eines von unzählig vielen möglichen Ereignisfenstern (12h, 48h, verschiedene Startzeitpunkte relativ zur Ankündigung), die in der Literatur getestet wurden, bevor dieses spezifische Fenster als "das" Ergebnis publiziert wurde — klassisches Susceptibility-to-p-hacking-Muster bei Event-Studien.
- Harvey/Liu/Zhu (2016, "…and the Cross-Section of Expected Returns") und Harvey & Liu ("False and Missed Discoveries") fordern angesichts der Zahl publizierter Anomalien einen t-Stat-Schwellenwert von ~3 statt 1,96 als Signifikanzhürde — der ursprüngliche Lucca-Moench-t-Stat von ~4 hätte diese Hürde knapp bestanden, ist aber nach der Post-2015-Halbierung/Auslöschung des Effekts ohnehin akademisch, da der Effekt selbst nicht mehr reproduzierbar ist.
- Direkte Widerlegung/Erklärung des Zerfalls: Kurov, Wolfe & Gilbert (2021), siehe oben — bislang keine überzeugende Gegen-Replikation mit aktuellen (2020–2026) Daten gefunden.

**Urteil: KILL.** Sauber dokumentierter, ökonomisch erklärter Post-Publication-Zerfall auf statistisch insignifikante Niveaus; niedrige Signalfrequenz verschärft das Problem zusätzlich.

---

## Kandidat 2: Makro-Ankündigungsprämie (Savor & Wilson 2013) — CPI/NFP/FOMC-Tage

### a) Ökonomische Begründung
Savor & Wilson argumentieren, dass an Tagen mit geplanten Makro-Ankündigungen (CPI, Arbeitsmarktbericht/NFP, FOMC-Zinsentscheid) das systematische Risiko höher und stärker über Aktien hinweg korreliert ist, sodass Investoren eine höhere Prämie für das Halten von Beta-Exposure an diesen Tagen verlangen — wer zahlt: Anleger, die Liquidität/Absicherung an unsicheren Tagen nachfragen, kompensieren Anbieter von Risikokapazität (Market Maker, Arbitrageure) mit einer Extra-Prämie, die sich in überdurchschnittlichen Marktrenditen just an diesen ex-ante bekannten Tagen zeigt.

### b) Limits to Arbitrage
Ähnlich niedrig wie bei Kandidat 1 — liquide Index-Futures, bekannte Termine. Wichtiger Unterschied: Deutlich höhere Signalfrequenz (siehe e), was die Arbitragefähigkeit strukturell erhöht (mehr Gelegenheiten für Preisfindung/Konvergenz) im Vergleich zum reinen FOMC-Drift.

### c) Originalstudien
Savor, P. & Wilson, M. (2013), "How Much Do Investors Care about Macroeconomic Risk? Evidence from Scheduled Economic Announcements", *Journal of Financial and Quantitative Analysis* 48(2), 343–375 (frühere Version: "Asset Pricing: A Tale of Two Days"). Sample: 1958–2009. Kernresultat: durchschnittliche tägliche Exzess-Rendite von **11,4 Basispunkten an Ankündigungstagen** vs. **1,1 Basispunkten an Nicht-Ankündigungstagen**; Ankündigungstage machen nur **ca. 13%** der Handelstage aus, vereinnahmen aber **über 60%** der kumulierten Aktienmarktrisikoprämie im Sample. Zusätzlich: An Ankündigungstagen ist die Beziehung zwischen Marktbeta und erwarteter Rendite (CAPM-Vorhersage) deutlich stärker als an gewöhnlichen Tagen — Autoren interpretieren dies als Bestätigung einer risikobasierten Erklärung.

### d) Out-of-Sample-/Post-Publication-Evidenz
Gemischtes Bild, mit einer wichtigen neueren Gegenstimme:
- **Bestätigend/erweiternd:** Ai, H., Bansal, R. & Guo, H. (NBER Working Paper 31923, "Macroeconomic Announcement Premium") erweitern die Stichprobe auf **1961–2023** und finden, dass ca. **44 Ankündigungstage/Jahr über 71% der aggregierten Aktienrisikoprämie** vereinnahmen — quantitativ sogar noch stärker als bei Savor & Wilson. Eine Fed-FEDS-Note (Okt. 2025, "Which Days Matter for Global Equity Markets?") liefert optionsbasierte annualisierte Prämienschätzungen für einen sehr aktuellen aber kurzen Zeitraum (Sept. 2023 – Juli 2025, ca. 22 Monate, limitiert durch Verfügbarkeit täglicher Optionsverfallstermine): CPI **45bp (t=10,4)**, NFP **53bp (t=8,8)**, FOMC **49bp (t=4,7)** — annualisierte Werte, methodisch nicht direkt vergleichbar mit Savor-Wilson, aber ein Indiz, dass Makro-Ankündigungstage auch 2023–2025 mit erhöhter impliziter Prämie gepreist werden.
- **Widerlegend/relativierend (zentral für "kritisch prüfen"):** "Is There a Macro-Announcement Premium?" (Management Science, 2024/2026, pubsonline.informs.org/doi/10.1287/mnsc.2024.06960). Dieses Papier greift die Kernlogik direkt an: Wenn hohe Ankündigungsrenditen eine Kompensation für Risiko darstellen, sollte die bedingte Renditevolatilität nach Auflösung der Unsicherheit (also nach der Ankündigung) merklich fallen. Empirisch **fällt die bedingte Volatilität an Makro-Ankündigungen kaum** — ein Befund, der der Risikoprämien-Interpretation widerspricht. Modelle **ohne** Ankündigungsprämie erklären die gemeinsamen Rendite-/Volatilitätsmuster besser als Modelle **mit** Prämie. Die Autoren führen die beobachteten hohen Ankündigungsrenditen stattdessen primär auf (i) geldpolitische Überraschungen (die im Mittel über lange Zeiträume nicht symmetrisch Null sein müssen, insbesondere in Zeiten tendenzieller Lockerung) und (ii) Small-Sample-Artefakte zurück, die sich nicht herausmitteln. Ihre Schätzung der "echten" Prämie ist klein.
- Ergänzend: Liu et al. (2022) zeigen laut Sekundärquellen, dass die Prämie **zeitvariabel** ist und von der Qualität/dem Rauschen des Informationsumfelds abhängt — kein stabiler, regimeunabhängiger Parameter.

Damit steht ein methodisch fundierter Widerspruch (Volatilitätspuzzle) gegen zwei Bestätigungsstudien mit längerer/aktuellerer Stichprobe. Dies ist per Definition **keine** saubere, unangefochtene Post-Publication-Bestätigung — es ist eine offene akademische Kontroverse Stand 2024–2026.

### e) Kosten und Signalfrequenz/statistische Power
Deutlich bessere statistische Power als Kandidat 1: ca. 44 Ankündigungstage/Jahr (CPI, NFP, FOMC zusammen) statt nur 8 FOMC-Termine — ein Faktor 5–6 mehr Beobachtungen pro Jahr, was Subsample-Tests und Regimeanalysen belastbarer macht. Kosten pro Trade bleiben niedrig (Index-Futures).

### f) Kapazität und Handelbarkeit
Höher als Kandidat 1 aufgrund der höheren Frequenz — mehr Gelegenheiten, Kapital zu allozieren, dieselbe hohe Liquidität der Instrumente (ES/SPX-Futures und -Optionen). Aus Kapazitätssicht der attraktivere der beiden Kandidaten.

### g) Regimeabhängigkeit und Tail-Risiko
Dieselbe Grundproblematik wie bei Kandidat 1, aber diversifizierter über mehr und unterschiedliche Ereignistypen (CPI-Überraschungen, NFP-Überraschungen, Fed-Entscheidungen), was das Tail-Risiko eines einzelnen Ereignistyps etwas abfedert, es aber nicht eliminiert (z.B. CPI-Schockmonate 2022 zeigten zweistellige Prozent-Tagesbewegungen in einzelnen Sektoren/Futures).

### h) Bekannte Kritik/Widerlegungen
- Zentral: das Volatilitäts-Puzzle aus dem Management-Science-2024-Papier — die Risikokompensations-Logik selbst wird in Frage gestellt, nicht nur die Effektgröße.
- Multiple-Testing: "Ankündigungstag" lässt sich auf viele Arten definieren (nur US-Daten vs. global, welche Ankündigungen zählen, Fenstergröße), was Grad an Robustheit gegenüber Freiheitsgraden in der Studienkonstruktion offenlässt.
- Beta-Konfundierung: Ein Großteil der scheinbaren "Prämie" könnte schlicht reflektieren, dass der Markt an Tagen mit bekanntermaßen hohem systematischem Risiko eine im CAPM-Sinn erwartbare höhere Rendite zeigt — für einen Fonds mit bereits vorhandenem Marktexposure ist das kein zusätzliches, unkorreliertes Alpha, sondern im Kern eine Beta-Timing-Strategie.

**Urteil: WEAK.** Es gibt aktuellere (2023–2025), teils sehr signifikante Bestätigungen (t-Stats 4,7–10,4), aber auch eine ernstzunehmende, aktuelle methodische Widerlegung der Risikoprämien-Interpretation. Die Diskrepanz zwischen "Prämie ist größer geworden" (Ai/Bansal/Guo) und "Prämie ist eigentlich klein/kein echter Risikofaktor" (Mgmt Science 2024) ist ungelöst. Ohne robuste, unangefochtene Post-Publication-Bestätigung erfüllt dieser Kandidat nicht die Schwelle für CANDIDATE.

---

## Kandidat 3: FOMC-Zyklus-Effekt / gerade Wochen (Cieslak, Morse & Vissing-Jørgensen 2019)

Aufgenommen als dritter, eng verwandter Kandidat der Klasse "Regime-Filter/Makro-Timing", da er eine reine Kalender-/Regimestruktur um den FOMC-Zyklus herum postuliert (kein Ankündigungsfenster, sondern ein bi-wöchentliches Muster relativ zum letzten FOMC-Meeting).

### a) Ökonomische Begründung
Cieslak, Morse & Vissing-Jørgensen (*Journal of Finance* 74(5), 2019, 2201–2248) zeigen, dass seit 1994 die gesamte Aktienrisikoprämie in geraden Wochen (0, 2, 4, 6) des FOMC-Zyklus verdient wurde, mit negativen Renditen in ungeraden Wochen. Mechanismus: informelle Kommunikation von Fed-Offiziellen mit Medien/Finanzsektor im Rhythmus zweiwöchentlicher interner Board-of-Governors-Sitzungen, die zu einer systematischen, unbeabsichtigten Informationsdiffusion über die künftige Geldpolitik führt — Anleger, die diese Kommunikationskanäle nicht haben, "zahlen" implizit durch entgangene Rendite in den nicht-informierten Wochen.

### b) Limits to Arbitrage
Wie bei den anderen Kandidaten strukturell niedrig (liquide Instrumente, öffentlich bekannter FOMC-Kalender), aber der Mechanismus selbst (informelle Kommunikation) ist per Definition nicht direkt beobachtbar/verifizierbar und daher schwer als robuster Risikofaktor zu verteidigen.

### c) Originalstudien
Wie oben: JoF 2019, Sample ab 1994, Kernresultat: Renditedifferenz zwischen geraden und ungeraden Wochen ist ökonomisch groß (praktisch 100% der Aktienrisikoprämie in der Hälfte der Wochen) und statistisch signifikant im Originalsample.

### d) Out-of-Sample-/Post-Publication-Evidenz
Eine Replikationsstudie ("Does the FOMC Cycle Still Drive Stock Returns? New Evidence from the US, UK, …", Ali Uppal) findet, dass der Effekt **ab ca. 2014 bzw. für das Fenster 2014–2023 nicht mehr besteht** — der Dummy für gerade Wochen wird statistisch nicht mehr von Null unterscheidbar. Als strukturelle Erklärung wird angeführt, dass die Board-of-Governors-Sitzungen im späteren Sample nicht mehr strikt zweiwöchentlich stattfinden, wodurch der postulierte Übertragungsmechanismus selbst nicht mehr intakt ist. Dies fällt zeitlich mit dem oben dokumentierten Verschwinden des Pre-FOMC-Drifts zusammen (Post-2015/Post-ZLB-Exit-Regimewechsel) und stützt die übergeordnete These eines strukturellen Bruchs in der gesamten "Fed-Kalender"-Anomalienfamilie um diese Zeit.

### e) Kosten und Signalfrequenz/statistische Power
Höhere Frequenz als reiner FOMC-Drift (26 Zwei-Wochen-Perioden/Jahr statt 8 Ereignisse), was theoretisch bessere Power ergäbe — praktisch relevant ist das aber nicht mehr, da der Effekt in der jüngeren Stichprobe schlicht nicht auftritt.

### f) Kapazität und Handelbarkeit
Technisch hoch (Futures, bekannter Kalender), aber irrelevant angesichts von d).

### g) Regimeabhängigkeit und Tail-Risiko
Extrem regimeabhängig — der Mechanismus ist an eine spezifische, nicht mehr geltende institutionelle Praxis (strikt zweiwöchentliche Board-Sitzungen, spezifisches Kommunikationsverhalten) gebunden. Kein stabiler Risikofaktor, eher ein Kalenderartefakt einer bestimmten Fed-Ära.

### h) Bekannte Kritik/Widerlegungen
Neben der oben genannten Replikation gehört dieser Effekt zu den in der Multiple-Testing-Debatte oft zitierten Beispielen für "zu gute" Kalenderanomalien (nahezu 100% der Prämie in exakt der Hälfte der Wochen ist ein statistisch auffällig cleanes Muster, das strukturelles Data-Mining nahelegt).

**Urteil: KILL.** Klar dokumentierter Zerfall, plausible strukturelle Erklärung (veränderte Fed-Kommunikationspraxis), Musterbildung selbst wirkt a priori data-mining-verdächtig.

---

## Übergreifende Bewertung der Klasse

**Multiple Testing über die gesamte Klasse hinweg:** Die drei Kandidaten sind nicht unabhängig — sie sind letztlich drei verschiedene Parametrisierungen desselben Grundphänomens ("etwas Systematisches passiert rund um FOMC-Termine"), getestet mit unterschiedlichen Fensterdefinitionen (24h vor Ankündigung; Ankündigungstag selbst; zweiwöchiger Zyklus). Wenn man diese als eine Familie mit vielen Freiheitsgraden (Fensterbreite, Startzeitpunkt, welche Ankündigungen zählen) betrachtet, potenziert sich das Multiple-Testing-Problem: Die Wahrscheinlichkeit, dass mindestens eine Parametrisierung im Original-Sample zufällig signifikant erscheint, ist deutlich höher als die nominale 5%- oder sogar 1%-Grenze suggeriert. Dass alle drei Varianten unabhängig voneinander um dieselbe Zeitperiode (ca. 2015/2016) herum zerfallen, spricht zwar eher für einen echten, gemeinsamen ökonomischen Treiber (strukturell gesunkene geldpolitische Unsicherheit, siehe VIX-Evidenz) als für reines Data-Mining des Originalfensters — es bedeutet aber gleichzeitig, dass der zugrundeliegende Risikofaktor selbst zeitvariabel und aktuell schwach/abwesend ist.

**Regimefrage 2020–2026:** Die verfügbare Literatur deckt den Zerfall überzeugend bis ca. 2019–2023 ab. Für die jüngste Phase (Zinserhöhungszyklus 2022/23, danach Senkungszyklus 2024/25, erhöhte geopolitische Unsicherheit) fehlt eine belastbare, zitierfähige Studie mit aktualisierten Pre-FOMC-Drift-Zahlen. Die einzige sehr aktuelle Datenquelle (Fed-FEDS-Note, Sept. 2023–Juli 2025) bezieht sich auf optionsimplizite Ankündigungsprämien (Kandidat 2), nicht auf den klassischen Pre-FOMC-Aktien-Drift (Kandidat 1), und deckt nur ~22 Monate ab — zu kurz für eine robuste Aussage über Regimewechsel. Diese Lücke ist eine der ehrlichsten Grenzen dieser Recherche und sollte vor jeder Kapitalallokation durch einen aktuellen eigenen Backtest (2016–2026) geschlossen werden.

**Statistische Power als Grundproblem der ganzen Klasse:** Selbst wenn ein echter Effekt bestünde, ist die Signalfrequenz (8 FOMC-Termine/Jahr für Kandidat 1 und 3 in ihrer reinsten Form; ca. 44 Makro-Ankündigungstage/Jahr für Kandidat 2) so gering, dass ein Portfolio, das ausschließlich auf diese Anomalieklasse setzt, over lange Zeiträume eine hohe Varianz der realisierten Sharpe Ratio aufweisen würde und schwer von einem reinen Glückstreffer zu unterscheiden ist — ein strukturelles Problem, das unabhängig von der Frage ist, ob der Effekt "echt" war.

**Ehrliches Gesamturteil:** Diese Anomalieklasse zeigt exemplarisch, wie akademisch publizierte, ursprünglich hochsignifikante Makro-Event-Effekte nach Publikation systematisch schwächer werden oder verschwinden — sei es durch tatsächliche Arbitrage, durch strukturelle Regimewechsel (gesunkene Unsicherheit, veränderte Fed-Kommunikation) oder durch ursprüngliche Überschätzung infolge von Multiple-Testing bei der Fensterwahl. Für den reinen Pre-FOMC-Drift und den FOMC-Zyklus-Effekt ist die Evidenz für "tot" stark und gut dokumentiert. Für die breitere Makro-Ankündigungsprämie ist das Bild differenzierter und Gegenstand einer offenen akademischen Kontroverse — genug Unsicherheit, um sie nicht auszuschließen, aber nicht genug dokumentierte, unangefochtene Post-Publication-Robustheit, um sie als Kapitalallokations-Kandidaten freizugeben.

---

## Quellen (Auswahl, aus Websuche)

- [The Pre-FOMC Announcement Drift — Wiley/JoF](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12196)
- [The Pre-FOMC Announcement Drift — NY Fed Staff Report 512](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.pdf)
- [The disappearing pre-FOMC announcement drift — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7525326/)
- [The disappearing pre-FOMC announcement drift — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1544612320315956)
- [The Disappearing Pre-FOMC Announcement Drift — SSRN (Kurov/Wolfe/Gilbert)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3134546)
- [The pre-FOMC announcement drift: short-lived or long-lasting? — Tandfonline](https://www.tandfonline.com/doi/full/10.1080/00036846.2024.2322573)
- [Pre-Announcement Risk — Toomas Laarits, AEA](https://www.aeaweb.org/conference/2021/preliminary/paper/QABNN7zD)
- [Premium for heightened uncertainty: Explaining pre-announcement market returns — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0304405X21004037)
- [Asset Pricing: A Tale of Two Days — Savor & Wilson, Wharton](https://faculty.wharton.upenn.edu/wp-content/uploads/2013/06/draft20130612pp-full.pdf)
- [Asset pricing: A tale of two days — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0304405X14000890)
- [How Much Do Investors Care About Macroeconomic Risk? — Semantic Scholar](https://www.semanticscholar.org/paper/How-Much-Do-Investors-Care-About-Macroeconomic-Risk-Savor-Wilson/80d71a46eb56ad3461cf264b55a5c472c5793468)
- [Is There a Macro-Announcement Premium? — Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.06960)
- [Macroeconomic Announcement Premium — NBER Working Paper 31923 (Ai, Bansal, Guo)](https://www.nber.org/system/files/working_papers/w31923/w31923.pdf)
- [Macroeconomic Announcements and the News That Matters Most to Investors — Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.07650)
- [The macroeconomic announcement premium and information environment — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0304393223000727)
- [Which Days Matter for Global Equity Markets? — Federal Reserve FEDS Notes, Okt. 2025](https://www.federalreserve.gov/econres/notes/feds-notes/which-days-matter-for-global-equity-markets-using-options-to-price-events-in-the-global-calendar-20251003.html)
- [Stock Returns over the FOMC Cycle — Cieslak, Morse, Vissing-Jørgensen, JoF (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2687614)
- [Does the FOMC Cycle Still Drive Stock Returns? — Ali Uppal](https://aliuppal.me/files/Ali_Uppal_CB_Cycles.pdf)
- [False (and Missed) Discoveries in Financial Economics — Harvey & Liu, SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3073799)
- [Anomalies and the Cross-Section of Expected Returns — Harvey, Liu & Zhu](https://people.duke.edu/~charvey/Research/Published_Papers/P118_and_the_cross.PDF)
