from app.schemas.review_request import ReviewRequest
from app.schemas.review_response import ReviewResponse
from app.services.prompt_builder import build_code_review_prompt
from app.services.groq_service import generate_ai_response
from app.utils.config import settings
from app.utils.logger import get_logger
from app.utils.response_formatter import format_ai_review_response

logger = get_logger(__name__)


def generate_code_review(request: ReviewRequest) -> ReviewResponse:
    logger.info(f"Generating AI code review for language: {request.language}")

    prompt = build_code_review_prompt(request)

    logger.info(f"Prompt created successfully with length: {len(prompt)} characters")

    raw_ai_response = generate_ai_response(
        prompt=prompt,
        max_tokens=request.max_tokens,
        temperature=request.temperature
    )

    formatted_response = format_ai_review_response(raw_ai_response)

    logger.info("AI code review generated and formatted successfully")

    return ReviewResponse(
        status="success",
        language=request.language,
        summary=formatted_response["summary"],
        issues=formatted_response["issues"],
        improvements=formatted_response["improvements"],
        complexity_analysis=formatted_response["complexity_analysis"],
        model=settings.GROQ_MODEL
    )