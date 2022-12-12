from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Response:
    text: str


class PromptAPI(ABC):
    @abstractmethod
    def complete(self, text: str) -> Response:
        pass  # pragma: no cover


class Prompt:
    def __init__(self, api: PromptAPI) -> None:
        self.api = api

    def complete(self, text: str) -> Response:
        return self.api.complete(text)
