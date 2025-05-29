from ai_agents.gemini_helper import ask_gemini


def classify_format_and_intent(data):
    prompt = f"""
    Given the following input, classify the format (PDF, JSON, Email, or Other) and the intent 
    (Invoice, RFQ, Complaint, Regulation, or General).
    
    Input:
    {data}
    
    Respond in this format:
    Format: <format>
    Intent: <intent>
    """
    result = ask_gemini(prompt)
    return result