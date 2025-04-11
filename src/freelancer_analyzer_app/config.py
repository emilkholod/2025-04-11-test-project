from pydantic_settings import BaseSettings, SettingsConfigDict


class ChatSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="CHAT_", case_sensitive=True)

    API_URL: str = ""
    API_KEY: str = ""
    VERBOSE_AGENT: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    CHAT_SETTINGS: ChatSettings = ChatSettings()

    CSV_FILE: str = "raw_data/freelancer_earnings_bd.csv"
