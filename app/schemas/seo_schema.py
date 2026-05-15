from pydantic import BaseModel
from typing import List


class SEOSchema(BaseModel):

    seo_title: str

    meta_description: str

    keywords: List[str]

    optimized_blog: str