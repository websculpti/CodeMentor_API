from app.schemas.review_request import ReviewRequest
from app.utils.logger import get_logger

logger = get_logger(__name__)


def build_code_review_prompt(request: ReviewRequest) -> str:
    logger.info("Building code review prompt")

    focus_areas = ", ".join(request.review_focus or [])

    prompt = f"""
You are an expert software engineer and code reviewer.

Review the following code carefully and provide a structured code review.

Programming Language:
{request.language}

Review Focus Areas:
{focus_areas}

Code:
```{request.language}
{request.code}