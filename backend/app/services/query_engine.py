import os
import httpx
from datetime import date, timedelta


def run_query(intent: dict) -> dict:
    """
    Run a Supabase REST query based on validated intent.
    """

    # 🔒 Read and sanitize env vars
    supabase_url = os.getenv("SUPABASE_URL", "").strip()
    anon_key = os.getenv("SUPABASE_ANON_KEY", "").strip()

    if not supabase_url.startswith("http"):
        raise RuntimeError("SUPABASE_URL is invalid or missing protocol")

    if not anon_key:
        raise RuntimeError("SUPABASE_ANON_KEY is missing")

    headers = {
        "apikey": anon_key,
        "Authorization": f"Bearer {anon_key}",
    }

    metric = intent.get("metric")
    time_range = intent.get("time_range")

    today = date.today()

    if time_range == "today":
        start_date = today
    elif time_range == "last_7_days":
        start_date = today - timedelta(days=7)
    elif time_range == "last_month":
        end_last_month = today.replace(day=1) - timedelta(days=1)
        start_date = end_last_month.replace(day=1)
    else:
        start_date = today

    # Decide table
    if metric in ("sales", "revenue"):
        table = "sales"
    elif metric == "expenses":
        table = "expenses"
    else:
        return {"value": 0, "rows": []}

    params = {
        "select": "*",
        "date": f"gte.{start_date.isoformat()}",
    }

    # ✅ SAFE URL BUILD
    url = f"{supabase_url}/rest/v1/{table}"

    print("Calling Supabase URL:", url)
    print("With params:", params)

    with httpx.Client(timeout=10) as client:
        response = client.get(url, headers=headers, params=params)
        response.raise_for_status()
        rows = response.json()

    # Calculate metric
    if metric == "sales":
        value = len(rows)
    elif metric == "revenue":
        value = sum(r.get("revenue", 0) for r in rows)
    elif metric == "expenses":
        value = sum(r.get("amount", 0) for r in rows)
    else:
        value = 0

    return {
        "value": value,
        "rows": rows
    }
