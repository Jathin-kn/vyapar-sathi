from fastapi import APIRouter
from pydantic import BaseModel

from app.services.intent_validator import validate_intent
from app.services.query_engine import run_query
from app.services.why_engine import analyze_change

router = APIRouter(prefix="/api")


class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def handle_query(payload: QueryRequest):
    """
    Handle user queries by extracting intent and fetching real data.
    """

    # ✅ ALWAYS define this first
    previous_value = None
    why_data = {}

    # Step 1: Extract and validate intent
    intent = validate_intent(payload.question)
    print("INTENT:", intent)

    # Step 2: Handle unclear intent safely
    if isinstance(intent, dict) and intent.get("clarification_required") is True:
        return {
            "answer": "Could you please clarify your question?",
            "why": [],
            "table": [],
            "explainability": {},
        }

    # Step 3: Run real query against Supabase
    result = run_query(intent)
    value = result.get("value", 0)
    rows = result.get("rows", [])

    metric = intent.get("metric")
    time_range = intent.get("time_range", "").replace("_", " ")

    # Step 4: Generate human-readable answer
    answer_text = f"Your {metric} for {time_range} is {value}."

    # Step 5: WHY mode (SAFE)
    comparison = intent.get("comparison")
    why_flag = intent.get("why_analysis")

    if comparison == "previous_period" or why_flag is True:
        # demo baseline (replace later with real previous query)
        previous_value = value * 1.2
        why_data = analyze_change(value, previous_value, metric)

    # Step 6: Return API response
    return {
        "answer": answer_text,
        "why": [why_data] if why_data else [],
        "table": rows,
        "explainability": why_data,
    }
