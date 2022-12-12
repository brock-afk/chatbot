import openai

from chatbot.domain.prompt import PromptAPI, Response


class OpenAIPrompt(PromptAPI):
    def __init__(
        self, engine: str | None = "text-davinci-003", temperature: int | None = 0
    ) -> None:
        self.engine = engine
        self.temperature = temperature
        super().__init__()

    def complete(self, text: str) -> Response:
        completion = openai.Completion.create(
            engine=self.engine,
            prompt=text,
            temperature=self.temperature,
        )

        choices = completion.choices

        return Response(choices[0].text)
