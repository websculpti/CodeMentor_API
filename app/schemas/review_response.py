from typing import List
from pydantic import BaseModel


class ReviewResponse(BaseModel):
    status: str
    language: str
    summary: str
    issues: List[str]
    improvements: List[str]
    complexity_analysis: str
    model: str