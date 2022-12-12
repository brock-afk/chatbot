import pytest

from chatbot.domain.prompt import Response


class PromptAPITestDouble:
    def __init__(self) -> None:
        self.searched_text = None

    def complete(self, text: str) -> Response:
        self.searched_text = text
        return Response(text="Very smart response")


@pytest.fixture
def prompt_api():
    prompt_api = PromptAPITestDouble()
    return prompt_api
