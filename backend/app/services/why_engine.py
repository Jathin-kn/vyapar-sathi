def analyze_change(current: float, previous: float, metric: str) -> dict:
    """
    Analyze change between two values and explain direction.
    """
    if previous == 0:
        return {
            "change_percent": 0,
            "direction": "neutral",
            "reason": f"No previous data available for {metric}."
        }

    change = ((current - previous) / previous) * 100

    if change > 0:
        direction = "up"
        reason = f"{metric.capitalize()} increased compared to the previous period."
    elif change < 0:
        direction = "down"
        reason = f"{metric.capitalize()} decreased compared to the previous period."
    else:
        direction = "neutral"
        reason = f"{metric.capitalize()} remained stable."

    return {
        "change_percent": round(change, 2),
        "direction": direction,
        "reason": reason
    }
