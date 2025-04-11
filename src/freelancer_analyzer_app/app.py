import click
from dishka.integrations.click import setup_dishka

from freelancer_analyzer_app.agent import Agent
from freelancer_analyzer_app.container import get_container
from freelancer_analyzer_app.utils import get_info_console, get_response_console


@click.command()
@click.pass_context
def app(context: click.Context) -> None:
    """
    Приложение для анализа данных фрилансеров
    """
    container = get_container()
    setup_dishka(container=container, context=context)

    agent = container.get(Agent)

    response_console = get_response_console()
    info_console = get_info_console()

    while True:
        info_console.print("-" * 80)
        question = info_console.input("Введите запрос: ")
        if not question:
            info_console.print("Завершение программы...")
            exit()
        with info_console.status("Формирую ответ..."):
            response = agent.get_response(question)
        response_console.print(f"Ответ: {response}")
