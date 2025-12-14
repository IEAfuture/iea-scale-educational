from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass
class Document:
    doc_id: str
    title: str
    date: str
    source: str
    text: str

def load_documents(folder: Path) -> List[Document]:
    docs: List[Document] = []
    for fp in sorted(folder.glob("*.txt")):
        raw = fp.read_text(encoding="utf-8").strip()
        # Minimal header parser: Title/Date/Source lines, then body
        lines = raw.splitlines()
        title = lines[0].replace("Title:", "").strip() if lines and lines[0].startswith("Title:") else fp.stem
        date = lines[1].replace("Date:", "").strip() if len(lines) > 1 and lines[1].startswith("Date:") else ""
        source = lines[2].replace("Source:", "").strip() if len(lines) > 2 and lines[2].startswith("Source:") else ""
        body = "\n".join(lines[3:]).strip() if len(lines) > 3 else raw
        docs.append(Document(doc_id=fp.stem, title=title, date=date, source=source, text=body))
    if not docs:
        raise SystemExit(f"No .txt documents found in {folder}")
    return docs
