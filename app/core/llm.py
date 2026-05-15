from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

# Model setup
llm = ChatMistralAI(model = "mistral-small-2506",temperature = 0,streaming=True)

