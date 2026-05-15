from app.state.blog_state import BlogState
from app.core.llm import llm
from app.schemas.outline_schema import OutlineSchema
from app.prompts.outline_prompt import get_outline_prompt
structured_llm = llm.with_structured_output(
    OutlineSchema
)

def outline(state:BlogState):
    topic = state['topic']
    summary = state['research_summary']
    
    prompt = get_outline_prompt(topic,summary)

 
    response = structured_llm.invoke(prompt)
    
    return{
        "outline_title": response.title,
        "outline_sections": response.sections
    }