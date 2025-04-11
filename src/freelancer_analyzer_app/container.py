import pandas as pd
from dishka import Container, Provider, Scope, make_container, provide
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

from freelancer_analyzer_app.agent import Agent
from freelancer_analyzer_app.config import Settings


class AppProvider(Provider):
    @provide
    def settings(self) -> Settings:
        return Settings()

    @provide
    def chat_model(self, settings: Settings) -> ChatOpenAI:
        return ChatOpenAI(
            openai_api_base=settings.CHAT_SETTINGS.API_URL,
            openai_api_key=settings.CHAT_SETTINGS.API_KEY,
            temperature=0,
        )

    @provide
    def agent(self, df: pd.DataFrame, settings: Settings, llm: ChatOpenAI) -> Agent:
        agent = create_pandas_dataframe_agent(
            llm=llm,
            df=df,
            allow_dangerous_code=True,
            verbose=settings.CHAT_SETTINGS.VERBOSE_AGENT,
        )
        return Agent(agent)

    @provide
    def df(self, settings: Settings) -> pd.DataFrame:
        return pd.read_csv(settings.CSV_FILE)


def get_container() -> Container:
    return make_container(AppProvider(scope=Scope.APP))
