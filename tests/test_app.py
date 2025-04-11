from unittest.mock import patch

from click.testing import CliRunner

from freelancer_analyzer_app.app import app


def test_app_running(mock_agent_executor, mock_info_console):
    mocked_response = {
        "output": "some response",
    }

    with (
        patch.object(mock_agent_executor, "invoke", return_value=mocked_response),
        patch.object(
            mock_info_console,
            "input",
            side_effect=["some question", ""],
        ) as mocked_prompt,
    ):
        runner = CliRunner()
        runner.invoke(app)

    mock_info_console.print.assert_called_with("Завершение программы...")
    assert mocked_prompt.call_count == 2


def test_question_and_response(
    mock_agent_executor, mock_info_console, mock_response_console
):
    test_value = "some response"

    mocked_response = {
        "output": test_value,
    }

    with (
        patch.object(
            mock_agent_executor, "invoke", return_value=mocked_response
        ) as mocked_agent_invoke,
        patch.object(
            mock_info_console,
            "input",
            side_effect=["some question", ""],
        ),
    ):
        runner = CliRunner()
        runner.invoke(app)

    mocked_agent_invoke.assert_called_once()
    mock_response_console.print.assert_called_once()

    assert test_value in mock_response_console.print.call_args[0][0]
