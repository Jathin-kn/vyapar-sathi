import json
import re
from .groq_client import get_groq_response


KNOWN_METRICS = ["revenue", "profit", "expenses", "sales"]
KNOWN_TIME_RANGES = {
    "today": "today",
    "last 7 days": "last_7_days",
    "last seven days": "last_7_days",
    "last week": "last_7_days",
    "last month": "last_month",
}


def fallback_intent(question: str) -> dict | None:
    """
    Deterministic fallback if LLM asks for clarification
    but question clearly contains intent.
    """
    q = question.lower()

    metric = None
    for m in KNOWN_METRICS:
        if m in q:
            metric = m
            break

    time_range = None
    for phrase, value in KNOWN_TIME_RANGES.items():
        if phrase in q:
            time_range = value
            break

    if metric and time_range:
        return {
            "metric": metric,
            "time_range": time_range,
            "comparison": "none",
            "breakdown": "none",
            "why_analysis": "why" in q,
        }

    return None


def extract_intent(question: str) -> dict:
    """
    Extract structured intent from a natural-language business question.
    """

    system_prompt = """You are an intent extractor for MSME business analytics queries.

Return ONLY valid JSON.

Allowed values:
- metric: revenue | profit | expenses | sales
- time_range: today | last_7_days | last_month
- comparison: none | previous_period
- breakdown: none | product | category
- why_analysis: true | false

Rules:
- If metric and time_range are clearly mentioned, infer intent.
- Default values:
  - comparison: none
  - breakdown: none
  - why_analysis: false
- Return {"clarification_required": true} ONLY if completely ambiguous.
- No explanations.
- No markdown.
"""

    try:
        response = get_groq_response(system_prompt, question)
        intent = json.loads(response)

        # 🔒 Deterministic fallback if LLM is too strict
        if intent.get("clarification_required") is True:
            forced = fallback_intent(question)
            if forced:
                return forced

        return intent

    except Exception:
        forced = fallback_intent(question)
        if forced:
            return forced

        return {"clarification_required": True}
