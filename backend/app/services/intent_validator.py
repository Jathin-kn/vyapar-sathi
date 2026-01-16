from .intent_extractor import extract_intent


def validate_intent(question: str) -> dict:
    """
    Validate and extract intent from a business question with retry logic.
    
    Args:
        question: User's natural language business question
        
    Returns:
        dict: Valid intent dictionary or {"clarification_required": true}
    """
    allowed_metrics = {"revenue", "profit", "expenses", "sales"}
    allowed_time_ranges = {"today", "last_7_days", "last_month"}
    allowed_comparisons = {"none", "previous_period"}
    allowed_breakdowns = {"none", "product", "category"}
    
    def is_valid_intent(intent: dict) -> bool:
        """Check if intent dict has valid structure and values."""
        if not isinstance(intent, dict):
            return False
        
        # Check for clarification_required
        if "clarification_required" in intent:
            return intent.get("clarification_required") is True and len(intent) == 1
        
        # Check all required fields are present
        required_fields = {"metric", "time_range", "comparison", "breakdown", "why_analysis"}
        if not required_fields.issubset(intent.keys()):
            return False
        
        # Validate enum values
        if intent.get("metric") not in allowed_metrics:
            return False
        if intent.get("time_range") not in allowed_time_ranges:
            return False
        if intent.get("comparison") not in allowed_comparisons:
            return False
        if intent.get("breakdown") not in allowed_breakdowns:
            return False
        if not isinstance(intent.get("why_analysis"), bool):
            return False
        
        return True
    
    # First extraction attempt
    intent = extract_intent(question)
    
    # Check if clarification is required
    if isinstance(intent, dict) and intent.get("clarification_required") is True:
        return intent
    
    # Validate intent
    if is_valid_intent(intent):
        return intent
    
    # Retry once
    intent = extract_intent(question)
    
    # Check if clarification is required after retry
    if isinstance(intent, dict) and intent.get("clarification_required") is True:
        return intent
    
    # Validate after retry
    if is_valid_intent(intent):
        return intent
    
    # Return clarification required if still invalid
    return {"clarification_required": True}
