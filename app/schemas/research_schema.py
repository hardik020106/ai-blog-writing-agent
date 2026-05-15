from pydantic import BaseModel
from typing import List


class ResearchSchema(BaseModel):

    summary: str

    key_points: List[str]

    trends: List[str]

    statistics: List[str]