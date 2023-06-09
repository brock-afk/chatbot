import openai

from chatbot.domain.prompt import PromptAPI, Response


class OpenAIPrompt(PromptAPI):
    def __init__(
        self, engine: str | None = "curie:ft-personal:css-rfp-2023-06-08-21-39-03", temperature: int | None = 0
    ) -> None:
        self.engine = engine
        self.temperature = temperature
        super().__init__()

    def complete(self, text: str) -> Response:
        completion = openai.Completion.create(
            engine=self.engine,
            prompt=text,
            temperature=self.temperature,
            max_tokens=256,
        )

        choices = completion.choices

        return Response(choices[0].text)
