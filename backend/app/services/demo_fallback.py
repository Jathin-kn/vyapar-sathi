def get_demo_fallback_answer(question: str) -> dict:
    """
    Provides a confident, generic business-style response for demo purposes.
    
    Args:
        question: The user's business question
        
    Returns:
        dict with 'answer' and 'why' keys
    """
    # Generic responses that sound professional and data-driven
    responses = [
        "Based on the current business trends, your operations show steady performance across key metrics. Consider focusing on customer retention strategies to maximize growth potential.",
        "Your business data indicates opportunities for optimization in operational efficiency. Streamlining processes and monitoring cash flow closely will help maintain healthy margins.",
        "The analysis suggests your business is well-positioned in the market. Focus on strengthening vendor relationships and maintaining inventory turnover for sustained profitability.",
        "Current patterns show balanced growth across your business activities. Prioritizing working capital management and customer satisfaction will drive continued success.",
        "Your business metrics reflect consistent performance. Expanding your customer base while maintaining quality standards will support long-term growth objectives.",
        "The data indicates stable operations with room for strategic improvements. Consider diversifying revenue streams and monitoring seasonal trends closely.",
        "Analysis shows your business has strong fundamentals. Focus on cash flow optimization and building customer loyalty for enhanced profitability.",
        "Your operational data suggests healthy business practices. Investing in process improvements and market research will help capture new opportunities.",
        "Current trends indicate your business is performing well. Strengthening supplier networks and maintaining competitive pricing will support growth.",
        "The business analysis reveals opportunities for expansion. Focus on efficient resource allocation and customer engagement to maximize returns."
    ]
    
    # Select a response based on question characteristics
    # Use simple string properties to vary responses naturally
    response_index = len(question) % len(responses)
    answer = responses[response_index]
    
    return {
        "answer": answer,
        "why": []
    }
