def get_writer_prompt(topic,title,section,summary):
    return f"""
    You are an expert blog writer.

    Write a detailed professional blog article.
    
    Topic:
    {topic}
    
    Research Summary:
    {summary}
    
    Outline Title:
    {title}
    
    Outline section:
    {section}

    Write in:
    - human conversational tone
    - medium article style
    - natural transitions
    - avoid robotic wording
    - avoid repetitive phrasing
    - vary sentence lengths
    - use engaging storytelling
    """