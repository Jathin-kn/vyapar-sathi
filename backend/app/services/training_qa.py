"""
Training QA Module
Simple keyword-based Q&A system for business analytics queries.
No external AI dependencies - uses rule-based matching.
"""

import re
import string
from typing import Optional

# Training Q&A pairs for business analytics
TRAINING_QA_PAIRS = [
    {
        "keywords": ["revenue", "sales", "income", "earnings"],
        "question_variants": [
            "What is our revenue?",
            "How much revenue did we generate?",
            "What are our sales figures?",
        ],
        "answer": "Revenue represents the total income generated from sales of goods or services. To track revenue, monitor monthly/quarterly sales figures, identify peak seasons, and compare year-over-year growth. Analyze revenue by product line or customer segment to understand which areas drive the most income.",
    },
    {
        "keywords": ["growth", "increase", "expand", "scale"],
        "question_variants": [
            "What is our growth rate?",
            "How is our business growing?",
            "Are we scaling effectively?",
        ],
        "answer": "Business growth can be measured by revenue increase, customer acquisition rate, market expansion, and product development. Focus on sustainable growth by monitoring: 1) YoY growth percentage, 2) Customer retention, 3) Market share, 4) Operational efficiency. Set realistic growth targets based on industry benchmarks and your resources.",
    },
    {
        "keywords": ["performance", "metrics", "kpi", "efficiency"],
        "question_variants": [
            "How is our performance?",
            "What are our key metrics?",
            "Are we meeting targets?",
        ],
        "answer": "Performance is measured through Key Performance Indicators (KPIs) specific to your business. Common metrics include: revenue growth, profit margin, customer acquisition cost (CAC), lifetime value (LTV), conversion rate, and operational efficiency. Track these metrics regularly and compare against historical data and industry standards to identify trends.",
    },
    {
        "keywords": ["trend", "pattern", "analysis", "forecast"],
        "question_variants": [
            "What are the current trends?",
            "Can you analyze our trends?",
            "What patterns do you see?",
        ],
        "answer": "Trend analysis helps identify patterns in your business data over time. Look for seasonal variations, cyclical patterns, and growth trajectories. Tools include: moving averages for smoothing data, year-over-year comparisons, cohort analysis, and forecasting models. Use historical trends to make informed predictions about future performance and adjust strategies accordingly.",
    },
    {
        "keywords": ["profit", "margin", "cost", "expense"],
        "question_variants": [
            "What is our profit margin?",
            "How do we control costs?",
            "What are our expenses?",
        ],
        "answer": "Profit margin is calculated as (Revenue - Expenses) / Revenue × 100. Track all costs including: COGS (cost of goods sold), operating expenses, and overhead. Improve profitability by: 1) Increasing revenue per transaction, 2) Reducing variable costs, 3) Optimizing operations. Regular expense audits help identify cost-saving opportunities.",
    },
    {
        "keywords": ["customer", "client", "market", "segment"],
        "question_variants": [
            "Who are our customers?",
            "Which market segment performs best?",
            "What is our customer base like?",
        ],
        "answer": "Understanding your customer segments is crucial for targeted growth. Analyze: demographics, purchase behavior, lifetime value by segment, and retention rates. Segment customers by: acquisition channel, revenue contribution, product preference, and engagement level. Use these insights to tailor marketing, pricing, and product development strategies.",
    },
]


def _normalize_text(text: str) -> str:
    """
    Normalize text for matching: lowercase, remove punctuation, extra spaces.
    """
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Remove extra spaces
    text = " ".join(text.split())
    return text


def _extract_keywords(text: str) -> set:
    """
    Extract individual words from normalized text.
    """
    normalized = _normalize_text(text)
    return set(normalized.split())


def _calculate_keyword_overlap(text: str, keywords: list) -> float:
    """
    Calculate overlap between text keywords and training keywords.
    Returns a score between 0 and 1.
    """
    text_keywords = _extract_keywords(text)
    training_keywords = set(keywords)
    
    if not training_keywords:
        return 0.0
    
    # Count overlapping keywords
    overlap = len(text_keywords & training_keywords)
    
    # Score is ratio of overlap to total training keywords
    score = overlap / len(training_keywords)
    return score


def get_trained_answer(question: str) -> Optional[dict]:
    """
    Find and return a trained answer for the given question.
    
    Uses keyword overlap matching:
    - Case-insensitive comparison
    - Ignores punctuation
    - Matches if sufficient keyword overlap exists (>= 0.3 threshold)
    
    Args:
        question: Natural language question string
        
    Returns:
        dict with "answer" and "why" keys if confident match found
        None if no confident match found
    """
    if not question or not isinstance(question, str):
        return None
    
    best_match = None
    best_score = 0.0
    confidence_threshold = 0.3  # At least 30% keyword overlap
    
    # Find the best matching QA pair
    for qa_pair in TRAINING_QA_PAIRS:
        score = _calculate_keyword_overlap(question, qa_pair["keywords"])
        
        if score > best_score:
            best_score = score
            best_match = qa_pair
    
    # Return answer only if we meet confidence threshold
    if best_score >= confidence_threshold and best_match:
        return {
            "answer": best_match["answer"],
            "why": [],  # Empty why list for training QA
        }
    
    return None
