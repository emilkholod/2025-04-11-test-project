import typer

from freelancer_analyzer_app.agent import get_agent
from freelancer_analyzer_app.utils import get_df, get_info_console, get_response_console


def app() -> None:
    """
    Приложение для анализа данных фрилансеров
    """
    response_console = get_response_console()
    info_console = get_info_console()
    df = get_df()
    agent = get_agent(df)

    while True:
        info_console.print("-" * 80)
        question = info_console.input("Введите запрос: ")
        if not question:
            info_console.print("Завершение программы...")
            raise typer.Exit()

        with info_console.status("Формирую ответ..."):
            response = agent.get_response(question)
        response_console.print(f"Ответ: {response}")
