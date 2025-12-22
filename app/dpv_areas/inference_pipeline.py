from __future__ import annotations

from .preprocessing import normalize_subject
from .providers import classify_asunto_llm

def classify_one(asunto: str) -> str:
    asunto_norm = normalize_subject(asunto)
    return classify_asunto_llm(asunto_norm)
