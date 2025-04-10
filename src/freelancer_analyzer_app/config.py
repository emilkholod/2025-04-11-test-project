from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class ChatSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="CHAT_", case_sensitive=True)

    API_URL: str = ""
    API_KEY: str = ""
    LANGUAGE: str = "EN"
    VERBOSE_AGENT: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    CHAT_SETTINGS: ChatSettings = ChatSettings()

    CSV_FILE: str = "raw_data/freelancer_earnings_bd.csv"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
