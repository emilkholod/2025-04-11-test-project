from typing import cast

from langchain.agents import AgentExecutor
from langchain.schema import HumanMessage, SystemMessage


class Agent:
    def __init__(self, agent: AgentExecutor, language: str = "EN"):
        self.agent = agent
        self.language = language

    def get_response(self, question: str) -> str:
        response = self.agent.invoke(
            [
                SystemMessage(
                    content=(f"Use {self.language} language to answer questions"),
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
