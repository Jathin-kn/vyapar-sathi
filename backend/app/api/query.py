from fastapi import APIRouter
from pydantic import BaseModel

from app.services.intent_validator import validate_intent


router = APIRouter(prefix="/api")


class QueryRequest(BaseModel):
	question: str


@router.post("/query")
def handle_query(payload: QueryRequest):
	"""Handle user queries by extracting and validating intent."""
	intent = validate_intent(payload.question)

	if isinstance(intent, dict) and intent.get("clarification_required") is True:
		answer_text = "Could you please clarify your question?"
	else:
		answer_text = "Mocked answer based on extracted intent."

	return {
		"answer": answer_text,
		"why": [],
		"table": [],
		"explainability": {},
	}
