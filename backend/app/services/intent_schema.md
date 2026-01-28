INTENT SCHEMA (v1)

Fields:
- metric: revenue | profit | expenses | sales
- time_range: today | last_7_days | last_month
- comparison: none | previous_period
- breakdown: none | product | category
- why_analysis: true | false

Rules:
- Output MUST be valid JSON only
- No text outside JSON
- No markdown
- If intent is unclear, return:
  {"clarification_required": true}
