import os
from typing import Tuple, TypeVar, Callable

from foundry._core.auth_utils import Auth, Token
from foundry._errors.environment_not_configured import EnvironmentNotConfigured
from foundry._errors.not_authenticated import NotAuthenticated


T = TypeVar("T")


class _UserToken(Token):
    def __init__(self, token: str) -> None:
        self._token = token

    @property
    def access_token(self) -> str:
        return self._token


class UserTokenAuth(Auth):
    def __init__(self, hostname: str, token: str) -> None:
        self._hostname = hostname
        self._token = _UserToken(token)

    def get_token(self) -> Token:
        if self._token is None:
            raise NotAuthenticated("Client has not been authenticated.")
        return self._token

    def execute_with_token(self, func: Callable[[Token], T]) -> T:
        return func(self.get_token())

    def run_with_token(self, func: Callable[[Token], None]) -> None:
        func(self.get_token())
