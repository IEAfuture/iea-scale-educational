from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from datetime import datetime

@dataclass
class WeakSignal:
    signal_id: str
    title: str
    description: str
    source: str                  # e.g., "JRC Weak Signals 2024"
    domain: str                  # e.g., "Environment & Agriculture"
    tags: List[str]              # controlled vocabulary if available
    evidence: List[str]          # short snippets, URLs, citations, etc.
    date_detected: str           # ISO date, e.g., "2025-10-01"
    confidence: Optional[float] = None  # optional: scoring from clustering

@dataclass
class AgentOutput:
    agent_name: str              # e.g., "security", "market", "regulatory"
    opportunity: str
    risks: str
    assumptions: List[str]
    policy_notes: str
    confidence: Optional[float] = None

def to_jsonable(signal: WeakSignal) -> Dict:
    return asdict(signal)

# Example signal instance (from your Table 3 concepts)
ws = WeakSignal(
    signal_id="WS-AG-001",
    title="Cultivated Meat",
    description="Lab-grown meat produced from animal cell cultures in bioreactors.",
    source="JRC Weak Signals in Science and Technology (2024)",
    domain="Environment & Agriculture",
    tags=["future foods", "biomanufacturing", "protein transition"],
    evidence=["JRC (2024) cluster notes: Future Foods; related bibliometrics/patents"],
    date_detected=datetime.now().date().isoformat()
)
print(to_jsonable(ws))

