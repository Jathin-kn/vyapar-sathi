"""
Training QA Module
Simple keyword-based Q&A system for business analytics queries.
No external AI dependencies - uses rule-based matching.
"""

import string
from typing import Optional

# Training Q&A pairs for business analytics
TRAINING_QA_PAIRS = [
    {
        "pattern": "what was my revenue last month",
        "keywords": ["revenue", "last", "month"],
        "answer": "Your revenue last month showed strong performance with consistent sales across all product categories. The month-over-month trend indicates steady customer demand, with peak sales occurring during the mid-month promotional period. To maintain this momentum, consider analyzing which products drove the highest margins and replicate those success factors in your upcoming campaigns.",
    },
    {
        "pattern": "how is my business performing this month",
        "keywords": ["business", "performing", "this", "month"],
        "answer": "Your business is performing well this month with healthy metrics across key areas. Revenue is on track to meet targets, customer acquisition remains steady, and operational efficiency has improved. Key highlights include: strong repeat customer rate, reduced customer acquisition costs, and improved inventory turnover. Focus on maintaining current strategies while exploring opportunities to scale successful initiatives.",
    },
    {
        "pattern": "why did my revenue increase recently",
        "keywords": ["why", "revenue", "increase", "recently"],
        "answer": "Your recent revenue increase can be attributed to several factors: 1) Successful marketing campaigns that drove higher customer engagement, 2) Seasonal demand patterns aligning with your product offerings, 3) Improved conversion rates from your sales funnel optimizations, 4) Positive word-of-mouth and customer referrals. To sustain this growth, continue monitoring customer feedback, maintain product quality, and reinvest in the channels that generated the highest ROI.",
    },
    {
        "pattern": "what are my sales trends",
        "keywords": ["sales", "trends"],
        "answer": "Your sales trends show promising patterns with upward momentum in recent periods. Key observations include: consistent week-over-week growth, strong performance in core product categories, and increasing average order values. Seasonal patterns indicate higher sales during specific months, which can inform inventory planning. Customer segments with the highest lifetime value are showing repeat purchase behavior, suggesting strong brand loyalty and product-market fit.",
    },
    {
        "pattern": "how can i improve my business growth",
        "keywords": ["improve", "business", "growth"],
        "answer": "To improve your business growth, focus on these strategic areas: 1) Customer Retention - implement loyalty programs and personalized marketing to increase repeat purchases, 2) Market Expansion - explore new customer segments or geographic markets, 3) Product Development - enhance existing offerings or introduce complementary products, 4) Operational Efficiency - streamline processes to reduce costs and improve margins, 5) Digital Presence - strengthen your online channels and leverage data analytics for better decision-making. Start with quick wins in retention and efficiency while planning longer-term expansion strategies.",
    },
    {
        "pattern": "give me a summary of my business",
        "keywords": ["summary", "business"],
        "answer": "Your business demonstrates solid fundamentals with healthy performance across key metrics. Revenue streams are diversified with strong customer retention rates. Your operational efficiency continues to improve, reflected in better profit margins. The customer base shows loyalty with growing lifetime values. Current market position is competitive with opportunities for expansion. Key strengths include: consistent cash flow, scalable operations, and a proven product-market fit. Areas for optimization include: exploring new market segments, enhancing digital marketing efforts, and implementing advanced analytics for predictive insights.",
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


def _all_keywords_present(input_text: str, keywords: list) -> bool:
    """
    Check if ALL keywords are present in the input text.
    
    Args:
        input_text: Normalized input question
        keywords: List of required keywords
        
    Returns:
        True if all keywords are found in input_text, False otherwise
    """
    input_words = set(input_text.split())
    required_keywords = set(keywords)
    
    # Check if all required keywords are in the input
    return required_keywords.issubset(input_words)


def get_trained_answer(question: str) -> Optional[dict]:
    """
    Find and return a trained answer for the given question.
    
    Matching rules:
    - Convert to lowercase
    - Strip punctuation
    - Match if ALL key words from training pattern are present in input
    
    Args:
        question: Natural language question string
        
    Returns:
        dict with "answer" and "why" keys if match found
        None if no match found
    """
    if not question or not isinstance(question, str):
        return None
    
    # Normalize the input question
    normalized_question = _normalize_text(question)
    
    # Check each training pair
    for qa_pair in TRAINING_QA_PAIRS:
        if _all_keywords_present(normalized_question, qa_pair["keywords"]):
            return {
                "answer": qa_pair["answer"],
                "why": [],
            }
    
    # No match found
    return None
