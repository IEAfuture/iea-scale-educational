from __future__ import annotations
import argparse
from pathlib import Path
import json

from .text_io import load_documents
from .retrieval import build_simple_index, top_k
from .towers import make_tower1, make_tower2, make_tower3

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Folder with .txt documents")
    p.add_argument("--out", default="out", help="Output folder")
    p.add_argument("--k", type=int, default=6, help="Top-K chunks to retrieve for generation")
    args = p.parse_args()

    in_dir = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    docs = load_documents(in_dir)
    # chunking + embedding index (simple)
    index = build_simple_index(docs)

    # retrieval: here we use a simple query derived from docs (educational shortcut)
    query = "weak signals for SMEs, governance, foresight, networks"
    retrieved = top_k(index, query=query, k=args.k)

    t1 = make_tower1(retrieved)
    t2 = make_tower2(retrieved)
    t3 = make_tower3(retrieved)

    (out_dir / "tower1.md").write_text(t1, encoding="utf-8")
    (out_dir / "tower2.md").write_text(t2, encoding="utf-8")
    (out_dir / "tower3.json").write_text(json.dumps(t3, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Done. Outputs written to: {out_dir}")

if __name__ == "__main__":
    main()
