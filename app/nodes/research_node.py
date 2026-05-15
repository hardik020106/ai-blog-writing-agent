from app.state.blog_state import BlogState
from app.tools.Web_search import search
from app.core.llm import llm
from app.prompts.research_prompt import get_research_prompt
from app.schemas.research_schema import ResearchSchema

structured_llm = llm.with_structured_output(
    ResearchSchema
)
def research_node(state:BlogState):
    topic = state['topic']
    
    print(f"\n Researching: {topic}\n")
    
    search_results = search.invoke(topic)
    
    combined_content = "\n\n".join([
        result["content"]
        for result in search_results
    ])
    
    prompt = get_research_prompt(
    topic,
    combined_content
)
    response = structured_llm.invoke(prompt)

    return {
        "research_summary": response.summary,
        "key_points": response.key_points,
        "trends": response.trends,
        "statistics": response.statistics
    }