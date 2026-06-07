from app.schemas.review_request import ReviewRequest
from app.utils.logger import get_logger

logger = get_logger(__name__)


def build_code_review_prompt(request: ReviewRequest) -> str:
    logger.info("Building code review prompt")

    focus_areas = ", ".join(request.review_focus or [])

    prompt = f"""
You are an expert software engineer and code reviewer.

Review the given code and return the response only as valid JSON.
Do not include markdown, explanation outside JSON, or code fences.

Programming Language:
{request.language}

Review Focus Areas:
{focus_areas}

Code:
{request.code}

Return the response in exactly this JSON structure:

{{
  "summary": "Briefly explain what the code does.",
  "issues": [
    "List possible bugs, logical errors, or bad practices."
  ],
  "improvements": [
    "Suggest improvements for readability, maintainability, or performance."
  ],
  "complexity_analysis": "Explain approximate time and space complexity if possible."

}}

Keep the review practical, clear, and beginner friendly.
"""
    return prompt.strip()