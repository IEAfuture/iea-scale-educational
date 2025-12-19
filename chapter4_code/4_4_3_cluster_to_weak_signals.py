CLUSTER_PROMPT = """
You are a foresight analyst. Given a cluster of related snippets, produce:
1) a weak-signal title,
2) a 2–3 sentence description,
3) 3 tags,
4) 2 pieces of evidence (directly referencing snippets).
Return JSON with keys: title, description, tags, evidence.
"""

def cluster_to_weak_signals(clusters: Dict[int, List[str]], source: str, domain: str) -> List[WeakSignal]:
    weak_signals = []
    for cid, texts in clusters.items():
        payload = {"cluster_id": cid, "snippets": texts, "source": source, "domain": domain}
        out_text, _ = call_gpt(CLUSTER_PROMPT, payload)
        out = parse_json_or_fallback(out_text)

        ws = WeakSignal(
            signal_id=f"WS-{domain[:2].upper()}-{cid:03d}",
            title=out.get("title", f"Cluster {cid}"),
            description=out.get("description", ""),
            source=source,
            domain=domain,
            tags=out.get("tags", []),
            evidence=out.get("evidence", []),
            date_detected=datetime.now().date().isoformat()
        )
        weak_signals.append(ws)
    return weak_signals

derived = cluster_to_weak_signals(clusters, source="Internal corpus + JRC (2024)", domain="Environment & Agriculture")
for s in derived:
    print(s.signal_id, s.title, s.tags)
