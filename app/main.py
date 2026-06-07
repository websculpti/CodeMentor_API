from fastapi import FastAPI
from app.utils.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="A FastAPI backend that reviews code using an AI-powered endpoint.",
    version=settings.APP_VERSION
)


@app.get("/")
def root():
    return {
        "status": "success",
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }