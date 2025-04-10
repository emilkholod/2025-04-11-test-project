from typing import cast

import pandas as pd
from langchain.agents import AgentExecutor
from langchain.schema import HumanMessage, SystemMessage
from langchain_experimental.agents import create_pandas_dataframe_agent

from freelancer_analyzer_app.chat_models import get_chat_model
from freelancer_analyzer_app.config import get_settings


class Agent:
    def __init__(self, agent: AgentExecutor):
        self.agent = agent
        self.settings = get_settings()

    def get_response(self, question: str) -> str:
        response = self.agent.invoke(
            [
                SystemMessage(
                    content=(
                        f"Use {self.settings.CHAT_SETTINGS.LANGUAGE} language"
                        " to answer questions"
                    ),
                ),
                HumanMessage(content=question),
            ]
        )
        output = cast(str, response.get("output"))
        if not output:
            raise RuntimeError(
                "Не удалось получить ответ, попробуйте переформулировать вопрос"
            )
        return output


def get_agent(df: pd.DataFrame) -> Agent:
    llm = get_chat_model()
    settings = get_settings()
    agent = create_pandas_dataframe_agent(
        llm=llm,
        df=df,
        allow_dangerous_code=True,
        verbose=settings.CHAT_SETTINGS.VERBOSE_AGENT,
    )
    return Agent(agent)
