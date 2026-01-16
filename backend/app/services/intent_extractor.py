import json
from .groq_client import get_groq_response


def extract_intent(question: str) -> dict:
    """
    Extract structured intent from a natural-language business question.
    
    Args:
        question: User's natural language business question
        
    Returns:
        dict: Parsed intent following the schema, or {"clarification_required": true}
    """
    system_prompt = """You are an intent extractor for business analytics queries.
Extract intent from the user's question and return ONLY valid JSON.

Return ONLY JSON with this structure:
{
  "metric": "revenue | profit | expenses | sales",
  "time_range": "today | last_7_days | last_month",
  "comparison": "none | previous_period",
  "breakdown": "none | product | category",
  "why_analysis": true | false
}

If the intent is unclear, return:
{"clarification_required": true}

Rules:
- Return ONLY valid JSON
- No explanations
- No markdown
- No extra text
- No additional fields"""

    try:
        response = get_groq_response(system_prompt, question)
        intent = json.loads(response)
        return intent
    except json.JSONDecodeError:
        return {"clarification_required": True}
    except Exception:
        return {"clarification_required": True}
