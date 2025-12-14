from __future__ import annotations
from typing import List, Dict, Any
from .retrieval import Chunk

def make_tower1(chunks: List[Chunk]) -> str:
    # Educational heuristic summarizer (offline)
    key_points = []
    for ch in chunks[:3]:
        key_points.append(f"- {ch.title} ({ch.date}): {ch.text.strip()[:160]}...")
    return """# Tower 1 — Strategic Insight

**Insight (educational demo):** SME networks can democratize foresight by combining AI-assisted pre-processing with human collective sensemaking. The three-tower structure enables fast scanning (Tower 1), explanatory narratives (Tower 2), and evidence verification (Tower 3), reducing attention scarcity while preserving interpretive responsibility.

## Evidence highlights
""" + "\n".join(key_points) + "\n"

def make_tower2(chunks: List[Chunk]) -> str:
    return """# Tower 2 — Thematic Contexts

## Context A — Resource scarcity and attention scarcity
SMEs face constraints that limit dedicated scanning capacity. A SCALE-inspired pipeline reduces manual effort by structuring information hierarchically while keeping humans responsible for interpretation.

## Context B — Network collaboration and shared intelligence
Inter-organizational collaboration distributes scanning burdens and diversifies perspectives, strengthening collective sensemaking and reducing over-reliance on any single expert.

## Context C — Traceability and validation
Each strategic claim must remain linked to traceable fragments (Tower 3) to enable verification, debate, and responsible governance.
"""

def make_tower3(chunks: List[Chunk]) -> Dict[str, Any]:
    frags = []
    for ch in chunks:
        frags.append({
            "fragment_id": ch.chunk_id,
            "doc_id": ch.doc_id,
            "title": ch.title,
            "date": ch.date,
            "source": ch.source,
            "excerpt": ch.text.strip()[:520]
        })
    return {"fragments": frags, "note": "Educational sample: students should replace with real sources and add URLs/DOIs."}
