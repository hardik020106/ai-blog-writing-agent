def get_outline_prompt(topic, research_summary):

    return f"""
    You are an expert outline creator.

    Blog Topic:
    {topic}

    Research Summary:
    {research_summary}

    Create a detailed blog outline with sections and subsections.
    """