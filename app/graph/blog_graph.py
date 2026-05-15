from langgraph.graph import StateGraph, END
from app.state.blog_state import BlogState
from app.nodes.research_node import research_node
from app.nodes.outline_node import outline
from app.nodes.writer_node import writer_node
from app.nodes.SEO_writer_node import seo_writer
from app.nodes.editor_node import editor_node

def create_blog_graph():

    workflow = StateGraph(BlogState)

    workflow.add_node(
        "research",
        research_node
    )
    workflow.add_node(
        "outline",
        outline
    )
    workflow.add_node(
        "writer",
        writer_node
    )
    workflow.add_node(
        "SEO_writer",
        seo_writer
    )
    workflow.add_node(
        "editor",
        editor_node
    )

    workflow.set_entry_point("research")

    workflow.add_edge(
        "research",
        "outline"
    )
    workflow.add_edge(
        "outline",
        "writer"
    )
    workflow.add_edge(
        "writer",
        "SEO_writer"
    )
    workflow.add_edge(
        "SEO_writer",
        "editor"
    )
    workflow.add_edge(
        "editor",
        END
    )

    return workflow.compile()