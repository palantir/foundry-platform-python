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

#  (c) Copyright 2023 Palantir Technologies Inc. All rights reserved.

import os
from typing import Optional, TypeVar, Tuple, Callable

from foundry.auth._auth_utils import Auth
from foundry.auth._auth_utils import Token


T = TypeVar("T")


class _UserToken(Token):
    def __init__(self, token: str) -> None:
        self._token = token

    @property
    def access_token(self) -> str:
        return self._token


class UserTokenAuth(Auth):
    """
    :param hostname: Your Foundry instance's hostname. (optional)
    :param token: Your bearer access token. (optional)
    """

    HOSTNAME_VAR = "FOUNDRY_HOSTNAME"
    TOKEN_VAR = "FOUNDRY_TOKEN"

    def __init__(
        self,
        hostname: Optional[str] = None,
        token: Optional[str] = None,
    ) -> None:
        if hostname is not None and token is not None:
            pass
        elif hostname is None and token is None:
            hostname, token = self._init_from_env()
        else:
            raise ValueError(
                """Unable to configure client: Either both
                the hostname and token are must be provided as keyword
                arguments or both from environmental variables."""
            )

        self.hostname = hostname
        self.token = token
        self._token = _UserToken(token)

        super().__init__(hostname=hostname)
        assert isinstance(token, str), f"token must be a str, not {type(token)}"

    def get_token(self) -> Token:
        return self._token

    def execute_with_token(self, func: Callable[[Token], T]) -> T:
        return func(self.get_token())

    def _init_from_env(self) -> Tuple[str, str]:
        hostname = os.environ.get(self.HOSTNAME_VAR)
        token = os.environ.get(self.TOKEN_VAR)

        if hostname is None:
            raise ValueError(
                f"Unable to configure client: ${self.HOSTNAME_VAR} not found in environment."
            )

        if token is None:
            raise ValueError(
                f"Unable to configure client: ${self.TOKEN_VAR} not found in environment."
            )

        return hostname, token
