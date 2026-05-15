def get_research_prompt(topic, content):

    return f"""
    You are an expert research assistant.

    Research Topic:
    {topic}

    Research Content:
    {content}

    Generate:
    1. Summary
    2. Key Points
    3. Trends
    4. Statistics
    """