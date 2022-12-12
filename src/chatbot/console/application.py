from argparse import ArgumentParser
from chatbot.domain.prompt import PromptAPI


class Application:
    def __init__(self, prompt_api: PromptAPI) -> None:
        self.prompt_api = prompt_api
        self.parser = ArgumentParser()
        self.parser.add_argument("text", help="Text for chatbot to analyze", type=str)

    def run(self) -> int:
        args = self.parser.parse_args()
        result = self.prompt_api.complete(args.text)
        print(result.text.strip())
