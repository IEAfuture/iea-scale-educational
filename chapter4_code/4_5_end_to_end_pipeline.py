def run_pipeline(snippets: List[str]) -> Dict:
    clusters = cluster_snippets(snippets, k=3)
    weak_signals = cluster_to_weak_signals(clusters, source="Internal corpus + JRC (2024)", domain="Environment & Agriculture")

    results = {"weak_signals": [], "tri_expert": {}}
    for ws in weak_signals:
        results["weak_signals"].append(to_jsonable(ws))
        results["tri_expert"][ws.signal_id] = run_tri_expert(ws)

    return results

results = run_pipeline(snippets)
with open("lescaai_run.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved: lescaai_run.json")
