from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture(scope="function")
def mock_agent_executor():
    with patch(
        "langchain_experimental.agents.agent_toolkits.pandas.base.AgentExecutor"
    ) as mocked_agent_executor:
        yield mocked_agent_executor.return_value


@pytest.fixture(scope="function")
def mock_info_console():
    mocked_info_console = MagicMock()
    with patch(
        "freelancer_analyzer_app.app.get_info_console", return_value=mocked_info_console
    ):
        yield mocked_info_console


@pytest.fixture(scope="function")
def mock_response_console():
    mocked_response_console = MagicMock()
    with patch(
        "freelancer_analyzer_app.app.get_response_console",
        return_value=mocked_response_console,
    ):
        yield mocked_response_console
