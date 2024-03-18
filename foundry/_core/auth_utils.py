from abc import ABC, abstractmethod
from typing import Callable, TypeVar

T = TypeVar("T")


class Token(ABC):
    @property
    @abstractmethod
    def access_token(self) -> str:
        pass


class Auth(ABC):
    @abstractmethod
    def get_token(self) -> "Token":
        pass

    @abstractmethod
    def execute_with_token(self, func: Callable[["Token"], T]) -> T:
        pass

    @abstractmethod
    def run_with_token(self, func: Callable[["Token"], None]) -> None:
        pass
