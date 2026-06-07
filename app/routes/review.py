from fastapi import APIRouter, HTTPException

from app.schemas.review_request import ReviewRequest
from app.schemas.review_response import ReviewResponse
from app.services.review_service import generate_code_review
from app.utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(
    tags=["Code Review"]
)


@router.post("/generate", response_model=ReviewResponse)
def generate_review(request: ReviewRequest):
    logger.info("POST /generate endpoint accessed")

    try:
        review_response = generate_code_review(request)
        return review_response

    except ValueError as error:
        logger.error(f"Validation error during code review: {str(error)}")
        raise HTTPException(status_code=400, detail=str(error))

    except RuntimeError as error:
        logger.error(f"AI service error during code review: {str(error)}")
        raise HTTPException(status_code=502, detail=str(error))

    except Exception as error:
        logger.exception("Unexpected error during code review")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while generating code review."
        )