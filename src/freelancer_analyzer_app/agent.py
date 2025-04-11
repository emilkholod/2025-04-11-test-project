from typing import cast

from langchain.agents import AgentExecutor
from langchain.schema import HumanMessage


class Agent:
    def __init__(self, agent: AgentExecutor):
        self.agent = agent

    def get_response(self, question: str) -> str:
        response = self.agent.invoke(
            [
                HumanMessage(content=question),
            ]
        )
        output = cast(str, response.get("output"))
        if not output:
            raise RuntimeError(
                "Не удалось получить ответ, попробуйте переформулировать вопрос"
            )
        return output
