from chatbot.domain.prompt import Prompt, Response


class PromptAPITestDouble:
    def __init__(self) -> None:
        self.searched_text = None

    def complete(self, text: str) -> Response:
        self.searched_text = text
        return Response(text="Very smart response")


def test_chatbot_prompt_returns_response_object():
    prompt_api = PromptAPITestDouble()
    prompt = Prompt(prompt_api)
    response = prompt.complete("testing")

    assert isinstance(response, Response)
