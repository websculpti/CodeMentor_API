from fastapi import FastAPI
from app.utils.config import settings
from app.utils.logger import get_logger
from app.routes import health, review

logger = get_logger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    description="CodeMentor API is an AI powered backend for reviewing code snippets.",
    version=settings.APP_VERSION
)

app.include_router(health.router)
app.include_router(review.router)


@app.get("/", tags=["Root"])
def root():
    logger.info("Root endpoint accessed")

    return {
        "status": "success",
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }