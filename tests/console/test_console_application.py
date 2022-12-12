from argparse import Namespace
from pytest import CaptureFixture
from unittest.mock import patch, MagicMock
from tests.conftest import PromptAPITestDouble
from chatbot.console.application import Application


@patch("chatbot.console.application.ArgumentParser.parse_args")
def test_application_passes_args_to_prompt(
    parse_args: MagicMock, prompt_api: PromptAPITestDouble
):
    parse_args.return_value = Namespace(text="this is my test input")
    application = Application(prompt_api)
    application.run()

    assert prompt_api.searched_text == "this is my test input"


@patch("chatbot.console.application.ArgumentParser.parse_args")
def test_application_prints_response_to_screen(
    parse_args: MagicMock, prompt_api: PromptAPITestDouble, capfd: CaptureFixture
):
    parse_args.return_value = Namespace(text="this is my test input")
    application = Application(prompt_api)
    application.run()

    out, _ = capfd.readouterr()

    assert out == "Very smart response\n"
