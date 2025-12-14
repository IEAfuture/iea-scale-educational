from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Any
import math
import re

from .text_io import Document

def _tokenize(s: str) -> List[str]:
    return re.findall(r"[a-zA-Z0-9]+", s.lower())

@dataclass
class Chunk:
    doc_id: str
    title: str
    date: str
    source: str
    chunk_id: str
    text: str
    tf: Dict[str, int]

def build_simple_index(docs: List[Document], chunk_size: int = 450) -> List[Chunk]:
    chunks: List[Chunk] = []
    for d in docs:
        t = d.text.strip()
        parts = [t[i:i+chunk_size] for i in range(0, len(t), chunk_size)]
        for i, part in enumerate(parts):
            toks = _tokenize(part)
            tf: Dict[str, int] = {}
            for w in toks:
                tf[w] = tf.get(w, 0) + 1
            chunks.append(Chunk(
                doc_id=d.doc_id, title=d.title, date=d.date, source=d.source,
                chunk_id=f"{d.doc_id}:{i}", text=part, tf=tf
            ))
    return chunks

def _cosine(a: Dict[str,int], b: Dict[str,int]) -> float:
    # Sparse cosine on term frequencies (educational / lightweight)
    dot = 0.0
    na = 0.0
    nb = 0.0
    for k,v in a.items():
        na += v*v
        if k in b:
            dot += v*b[k]
    for v in b.values():
        nb += v*v
    if na == 0 or nb == 0:
        return 0.0
    return dot / (math.sqrt(na) * math.sqrt(nb))

def top_k(index: List[Chunk], query: str, k: int = 6) -> List[Chunk]:
    qtf: Dict[str,int] = {}
    for w in _tokenize(query):
        qtf[w] = qtf.get(w, 0) + 1
    scored = [( _cosine(ch.tf, qtf), ch) for ch in index]
    scored.sort(key=lambda x: x[0], reverse=True)
    return [ch for s,ch in scored[:k]]
