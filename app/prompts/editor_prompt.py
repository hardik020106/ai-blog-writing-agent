def get_editor_prompt(blog):
    return f"""
    You are a professional blog editor.

    Improve readability.
    Humanize the tone.
    Fix formatting consistency.
    Remove repetitive wording.
    Make the blog feel natural and polished.

    Blog:
    {blog}
    """