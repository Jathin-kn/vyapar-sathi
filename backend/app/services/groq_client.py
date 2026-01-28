import os
from groq import Groq


def get_groq_response(system_prompt: str, user_prompt: str) -> str:
    """
    Send a request to Groq LLM and return the raw text response.
    
    Args:
        system_prompt: System message to guide the model's behavior
        user_prompt: User's actual question or prompt
        
    Returns:
        str: Raw text response from the model
        
    Raises:
        ValueError: If GROQ_API_KEY environment variable is not set
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set")
    
    client = Groq(api_key=api_key)
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    
    return response.choices[0].message.content
