from functools import lru_cache

from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from freelancer_analyzer_app.config import get_settings


@lru_cache(maxsize=1)
def get_chat_model() -> BaseChatModel:
    settings = get_settings()
    return ChatOpenAI(
        openai_api_base=settings.CHAT_SETTINGS.API_URL,
        openai_api_key=settings.CHAT_SETTINGS.API_KEY,
        temperature=0,
    )
