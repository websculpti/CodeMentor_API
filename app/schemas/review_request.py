from typing import List, Optional
from pydantic import BaseModel, Field


class ReviewRequest(BaseModel):
    language: str = Field(
        ...,
        min_length=1,
        description="Programming language of the submitted code"
    )

    code: str = Field(
        ...,
        min_length=10,
        description="Code snippet that needs to be reviewed"
    )

    review_focus: Optional[List[str]] = Field(
        default=["bugs", "readability", "performance"],
        description="Specific areas to focus on during code review"
    )

    max_tokens: Optional[int] = Field(
        default=1000,
        ge=100,
        le=2000,
        description="Maximum number of tokens for the AI response"
    )

    temperature: Optional[float] = Field(
        default=0.3,
        ge=0.0,
        le=1.0,
        description="Controls creativity of the AI response"
    )