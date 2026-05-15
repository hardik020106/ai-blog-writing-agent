from app.graph.blog_graph import create_blog_graph
import os
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown


console = Console()


graph = create_blog_graph()


console.print(
    "[bold cyan]Starting Blog Generation Workflow...[/bold cyan]\n"
)


final_state = graph.invoke({
    "topic": topic
})

os.makedirs("outputs", exist_ok=True)
with open(
    "outputs/final_blog.md",
    "w",
    encoding="utf-8"
) as file:

    file.write(final_state["final_blog"])


# console.print(
#     "\n[bold green]Blog Saved Successfully![/bold green]\n"
# )


# markdown = Markdown(final_state["final_blog"])


# console.print(
#     Panel(
#         markdown,
#         title="Final Blog",
#         border_style="green"
#     )
# )