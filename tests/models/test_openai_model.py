import pytest

from dataclasses import dataclass
from unittest.mock import patch, MagicMock
from chatbot.models.openai import OpenAIPrompt
from chatbot.domain.prompt import Response


@dataclass
class OpenAIChoiceMock:
    text: str


@dataclass
class OpenAIResponseMock:
    choices: list[OpenAIChoiceMock]


@pytest.fixture
def open_ai_prompt():
    prompt = OpenAIPrompt()
    return prompt


@patch("openai.Completion.create")
def test_open_ai_prompt_returns_response_object(
    create: MagicMock, open_ai_prompt: OpenAIPrompt
):
    create.return_value = OpenAIResponseMock(
        choices=[OpenAIChoiceMock("first"), OpenAIChoiceMock("second")]
    )
    response = open_ai_prompt.complete("testing")
    assert isinstance(response, Response)


@patch("openai.Completion.create")
def test_open_ai_prompt_returns_first_response_from_api(
    create: MagicMock, open_ai_prompt: OpenAIPrompt
):
    create.return_value = OpenAIResponseMock(
        choices=[OpenAIChoiceMock("first"), OpenAIChoiceMock("second")]
    )
    response = open_ai_prompt.complete("testing")

    assert response.text == "first"


@patch("openai.Completion.create")
def test_open_ai_prompt_uses_correct_input(
    create: MagicMock, open_ai_prompt: OpenAIPrompt
):
    create.return_value = OpenAIResponseMock(
        choices=[OpenAIChoiceMock("first"), OpenAIChoiceMock("second")]
    )
    open_ai_prompt.complete("testing")

    create.assert_called_once_with(
        engine="text-davinci-002", prompt="testing", temperature=0.5, max_tokens=2048
    )
