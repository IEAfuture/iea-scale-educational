# IEA-SCALE Educational Implementation (Three-Tower Weak-Signal Intelligence)

This repository contains **supplementary educational material** inspired by the IEA‑SCALE architecture described in **Case 2** (“Democratizing Foresight for SME Networks: the IEA‑SCALE Model”).  
It is intended for **teaching and reproducibility of core concepts** (three-tower information architecture; traceability; human-in-the-loop), **without disclosing any proprietary production implementation**.

## What this repo is
- A **minimal, didactic pipeline** that turns a small set of documents into:
  - **Tower 1**: short strategic insight
  - **Tower 2**: thematic contexts
  - **Tower 3**: traceable evidence fragments (with source metadata)
- A reference implementation that matches the **“SCALE-inspired”** approach in the chapter’s supplementary guide.

## What this repo is not
- Not the production IEA‑SCALE system.
- Not a ready-to-deploy product (no database, no scraping infrastructure, no private prompts).
- Not a claim of full automation: weak-signal meaning emerges through **human attention and interpretation**.

## Quick start (local)
1. Install Python 3.10+  
2. Create a virtual environment and install:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the demo pipeline:
   ```bash
   python -m src.pipeline --input data/sample_docs --out out
   ```

The demo uses a **stub LLM** by default (so it runs offline).  
If you want to connect an actual LLM provider, set `LLM_PROVIDER` and `LLM_API_KEY` in your environment and adjust `src/llm.py`.

## Outputs
- `out/tower1.md`
- `out/tower2.md`
- `out/tower3.json` (fragments + metadata)

## How to cite
If you cite the chapter, cite the chapter. If you cite the code:
- Use the GitHub repository URL and the release tag (recommended).
- Or use the `CITATION.cff` in this repository.

## License
MIT (educational code). See `LICENSE`.

## Contact
IEA Future Lab / UFRGS — for academic inquiries.
