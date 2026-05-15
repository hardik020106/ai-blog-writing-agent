from pydantic import BaseModel
from typing import List


class OutlineSchema(BaseModel):

    title: str

    sections: List[str]