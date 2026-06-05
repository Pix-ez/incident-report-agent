from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class RCAResponse(BaseModel):
    root_cause: str
    confidence: float
    severity: str
    evidence_summary: Dict[str, Any]
    recommendations: List[str]