from app.state.blog_state import BlogState
from app.core.llm import llm
from app.prompts.SEO_writer_prompt import get_seo_writer_prompt
from app.schemas.seo_schema import SEOSchema
structured_llm = llm.with_structured_output(
    SEOSchema
)
def seo_writer(state:BlogState):
    topic = state["topic"]
    blog = state['blog_content']
    
    prompt = get_seo_writer_prompt(topic,blog)
    response = structured_llm.invoke(prompt)
    
    return{
        "seo_title": response.seo_title,
        "meta_description": response.meta_description,
        "keywords": response.keywords,
        "optimized_blog": response.optimized_blog
    }
