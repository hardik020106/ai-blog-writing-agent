from pydantic import BaseModel
from typing import List

class WriterSchema(BaseModel):
    topic:str
    blog_contet:str
