from app.schemas.editor_schema import EditorSchema
from app.core.llm import llm
from app.prompts.editor_prompt import get_editor_prompt
structured_llm = llm.with_structured_output(
    EditorSchema
)


def editor_node(state):

    blog = state["optimized_blog"]

    prompt = get_editor_prompt(blog)

    response = structured_llm.invoke(prompt)

    return {
        "final_blog": response.final_blog
    }