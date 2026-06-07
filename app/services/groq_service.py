from typing import Optional
from groq import Groq

from app.utils.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


def get_groq_client() -> Groq:
    if not settings.GROQ_API_KEY:
        logger.error("GROQ_API_KEY is missing")
        raise ValueError("GROQ_API_KEY is missing. Please add it in the .env file.")

    return Groq(api_key=settings.GROQ_API_KEY)


def generate_ai_response(
    prompt: str,
    max_tokens: Optional[int] = None,
    temperature: Optional[float] = None
) -> str:
    if not prompt or not prompt.strip():
        logger.error("Empty prompt received")
        raise ValueError("Prompt cannot be empty")

    client = get_groq_client()

    used_max_tokens = max_tokens or settings.DEFAULT_MAX_TOKENS
    used_temperature = (
        temperature
        if temperature is not None
        else settings.DEFAULT_TEMPERATURE
    )

    logger.info(f"Calling Groq model: {settings.GROQ_MODEL}")

    try:
        chat_completion = client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant for code review."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=used_max_tokens,
            temperature=used_temperature
        )

        response_text = chat_completion.choices[0].message.content

        logger.info("Groq response generated successfully")

        return response_text.strip() if response_text else ""

    except Exception as error:
        logger.exception("Groq API call failed")
        raise RuntimeError(f"Groq API call failed: {str(error)}") from error