from app.state.blog_state import BlogState
from app.core.llm import llm
from app.schemas.writer_schema import WriterSchema
from app.prompts.writer_prompt import get_writer_prompt
import sys
structured_llm = llm.with_structured_output(
    WriterSchema
)
def writer_node(state:BlogState):
    topic = state['topic']
    outline_title = state['outline_title']
    outline_section = state['outline_sections']
    research_summary = state['research_summary']
    
    prompt = get_writer_prompt(topic,outline_title,outline_section,research_summary)
    response = llm.stream(prompt)

    full_blog = ""

    print("\n Writing Blog...\n")

    for chunk in response:

        if chunk.content:

            # sys.stdout.write(chunk.content)

            # sys.stdout.flush()

            full_blog += chunk.content

    print("\n")

    return {
        "blog_content": full_blog
    }