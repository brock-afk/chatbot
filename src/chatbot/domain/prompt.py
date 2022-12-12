from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Response:
    text: str


class PromptAPI(ABC):
    @abstractmethod
    def complete(self, text: str) -> Response:
        pass  # pragma: no cover
