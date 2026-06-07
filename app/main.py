from fastapi import FastAPI
from app.utils.config import settings
from app.routes import health
from app.utils.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    description="A FastAPI backend that reviews code using an AI-powered endpoint.",
    version=settings.APP_VERSION
)

app.include_router(health.router)

@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {
        "status": "success",
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }