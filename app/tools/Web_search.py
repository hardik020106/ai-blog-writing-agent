from langchain.tools import tool
from tavily import TavilyClient
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

@tool
def search(Query:str):
    """It has to do an indepth search of the given query"""
    response = client.search(query=Query,
                             search_depth="advanced",
                             max_results=5)
    return response['results']

