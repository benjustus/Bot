"""Aggregiert die YAML-Frontmatter aller Agent-Dossiers zu einer Rangliste.

Ranking NICHT nach Rendite, sondern nach dem Mandats-Score:
  40% p_echte_ineffizienz, je 10% Reproduzierbarkeit, Signifikanz nach MTK,
  Regimestabilitaet, Handelbarkeit, Kostenrobustheit, 10% Kapazitaet.
"""
import glob
import json
import re
import yaml

AGENTS = "/home/user/Bot/research/agents"

WEIGHTS = {
    "reproduzierbarkeit": 0.10,
    "signifikanz_nach_mtk": 0.10,
    "regimestabilitaet": 0.10,
    "handelbarkeit": 0.10,
    "kapazitaet": 0.10,
    "kostenrobustheit": 0.10,
}


def parse_dossier(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"```yaml\n(.*?)```", text, re.S)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        print(f"YAML-Fehler in {path}: {e}")
        return None


def main():
    rows = []
    for path in sorted(glob.glob(f"{AGENTS}/*.md")):
        d = parse_dossier(path)
        if not d:
            print(f"WARN: kein YAML in {path}")
            continue
        for s in d.get("strategien", []):
            sc = s.get("scores", {})
            try:
                score = 0.4 * float(s.get("p_echte_ineffizienz", 0)) * 5
                for k, w in WEIGHTS.items():
                    score += w * float(sc.get(k, 0))
            except (TypeError, ValueError):
                score = None
            rows.append({
                "agent": d.get("agent"),
                "klasse": d.get("klasse"),
                "strategie": s.get("name"),
                "urteil": s.get("urteil"),
                "p_echte_ineffizienz": s.get("p_echte_ineffizienz"),
                "netto_sharpe": s.get("netto_sharpe_erwartung"),
                "kernrisiko": s.get("kernrisiko"),
                "testbar": s.get("testbar_mit_freien_daten"),
                "datenquelle": s.get("freie_datenquelle"),
                "scores": sc,
                "mandats_score": round(score, 2) if score is not None else None,
            })
    rows.sort(key=lambda r: (r["mandats_score"] or 0), reverse=True)
    with open("/home/user/Bot/research/empirics/ranking.json", "w") as f:
        json.dump(rows, f, indent=1, ensure_ascii=False)
    print(f"{len(rows)} Strategien aus {len(glob.glob(f'{AGENTS}/*.md'))} Dossiers")
    for r in rows:
        print(f"{r['mandats_score']:>5}  {str(r['urteil']):<9} "
              f"[{r['agent']}] {r['strategie']}")


if __name__ == "__main__":
    main()
