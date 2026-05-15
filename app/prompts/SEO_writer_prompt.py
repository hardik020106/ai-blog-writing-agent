def get_seo_writer_prompt(topic,blog):
    return f"""
    You are an expert SEO content optimizer.

    Optimize the following blog for SEO.


    Topic:
    {topic}

    Blog:
    {blog}
"""