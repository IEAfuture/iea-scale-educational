def parse_json_or_fallback(text: str) -> Dict:
    try:
        return json.loads(text)
    except Exception:
        return {"raw_text": text}

def run_tri_expert(signal: WeakSignal) -> Dict[str, Dict]:
    payload = to_jsonable(signal)
    out = {}

    for name, prompt in [("security", SECURITY_PROMPT),
                         ("market", MARKET_PROMPT),
                         ("regulatory", REG_PROMPT)]:
        text, meta = call_gpt(prompt, payload)  # or call_gemini(...)
        out[name] = {"result": parse_json_or_fallback(text), "meta": meta}

    return out

tri = run_tri_expert(ws)
print(json.dumps(tri, ensure_ascii=False, indent=2))
