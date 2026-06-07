from fastapi import APIRouter
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

    review_response = generate_code_review(request)

    return review_response