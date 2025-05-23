#  Copyright 2024 Palantir Technologies, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import os
from typing import Callable
from typing import TypeVar
from typing import Union

import httpx

from foundry_sdk._core.user_token_auth_client import Auth
from foundry_sdk._core.user_token_auth_client import Token
from foundry_sdk._errors.environment_not_configured import EnvironmentNotConfigured
from foundry_sdk._errors.not_authenticated import NotAuthenticated

T = TypeVar("T")


class _PipelineToken(Token):

    def __init__(self, token: str) -> None:
        self._token = token

    @property
    def access_token(self) -> str:
        return self._token


TOKEN_PATH_ENV_VAR = "BUILD2_TOKEN"


class ComputeModulePipelineAuth(Auth):
    """Use the token provided by Foundry when running in a Compute Module in Pipeline execution mode."""

    _token: Union[Token, None]

    def __init__(self) -> None:
        self._token = None
        super().__init__()

    def get_token(self) -> Token:
        if self._token is not None:
            return self._token

        build2_token_path = os.environ.get(TOKEN_PATH_ENV_VAR)
        if build2_token_path is None:
            raise EnvironmentNotConfigured(
                f"Missing environment variable {TOKEN_PATH_ENV_VAR}. Please ensure this code is running inside a Compute Module in Pipeline execution mode."
            )

        if not os.path.isfile(build2_token_path):
            raise EnvironmentNotConfigured(
                f"{TOKEN_PATH_ENV_VAR} environment variable points to a non-existent file: '{build2_token_path}'"
            )

        with open(build2_token_path, "r") as f:
            self._token = _PipelineToken(f.read().strip())
        return self._token

    def execute_with_token(self, func: Callable[[Token], T]) -> T:
        return func(self.get_token())

    def run_with_token(self, func: Callable[[Token], T]) -> None:
        func(self.get_token())
