import re
from collections import Counter

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    return text

def simple_keyphrases(text: str, top_k: int = 10) -> List[str]:
    tokens = re.findall(r"[a-zA-Z][a-zA-Z\-]{2,}", normalize(text))
    stop = set(["the","and","for","with","that","this","from","into","are","was","were","has","have"])
    tokens = [t for t in tokens if t not in stop]
    return [w for w, _ in Counter(tokens).most_common(top_k)]
