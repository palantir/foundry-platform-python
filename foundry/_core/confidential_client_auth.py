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


import asyncio
from typing import Callable
from typing import List
from typing import Optional
from typing import TypeVar

import requests

from foundry._core.auth_utils import Auth
from foundry._core.oauth import SignInResponse
from foundry._core.oauth import SignOutResponse
from foundry._core.oauth_utils import ConfidentialClientOAuthFlowProvider
from foundry._core.oauth_utils import OAuthToken
from foundry._errors.environment_not_configured import EnvironmentNotConfigured
from foundry._errors.not_authenticated import NotAuthenticated

T = TypeVar("T")


class ConfidentialClientAuth(Auth):
    """
    Client for Confidential Client OAuth-authenticated Ontology applications.
    Runs a background thread to periodically refresh access token.

    :param client_id: OAuth client id to be used by the application.
    :param client_secret: OAuth client secret to be used by the application.
    :param scopes: The list of scopes to request.
    :param hostname: Hostname for authentication and ontology endpoints.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        hostname: str,
        scopes: List[str],
        should_refresh: bool = False,
    ) -> None:
        if len(scopes) == 0:
            raise ValueError(
                "You have not provided any scopes. At least one scope must be provided."
            )

        self._client_id = client_id
        self._client_secret = client_secret
        self._token: Optional[OAuthToken] = None
        self._should_refresh = should_refresh
        self._refresh_task: Optional[asyncio.Task] = None
        self._hostname = hostname
        self._server_oauth_flow_provider = ConfidentialClientOAuthFlowProvider(
            client_id, client_secret, self.url, scopes=scopes
        )

    def get_token(self) -> OAuthToken:
        if self._token is None:
            raise NotAuthenticated("Client has not been authenticated.")
        return self._token

    def execute_with_token(self, func: Callable[[OAuthToken], T]) -> T:
        try:
            return self._run_with_attempted_refresh(func)
        except Exception as e:
            self.sign_out()
            raise e

    def run_with_token(self, func: Callable[[OAuthToken], T]) -> None:
        try:
            self._run_with_attempted_refresh(func)
        except Exception as e:
            self.sign_out()
            raise e

    def _run_with_attempted_refresh(self, func: Callable[[OAuthToken], T]) -> T:
        """
        Attempt to run func, and if it fails with a 401, refresh the token and try again.
        If it fails with a 401 again, raise the exception.
        """
        try:
            return func(self.get_token())
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code == 401:
                self._refresh_token()
                return func(self.get_token())
            else:
                raise e

    @property
    def url(self):
        return self._hostname.removeprefix("https://").removeprefix("http://")

    def _refresh_token(self):
        self._token = self._server_oauth_flow_provider.get_token()

    def sign_in_as_service_user(self) -> SignInResponse:
        token = self._server_oauth_flow_provider.get_token()
        self._token = token

        async def refresh_token_task():
            while True:
                if self._token is None:
                    raise RuntimeError("The token was None when trying to refresh.")

                await asyncio.sleep(self._token.expires_in / 60 - 10)
                self._token = self._server_oauth_flow_provider.get_token()

        if self._should_refresh:
            loop = asyncio.get_event_loop()
            self._refresh_task = loop.create_task(refresh_token_task())
        return SignInResponse(
            session={"accessToken": token.access_token, "expiresIn": token.expires_in}
        )

    def sign_out(self) -> SignOutResponse:
        if self._refresh_task:
            self._refresh_task.cancel()
            self._refresh_task = None

        if self._token:
            self._server_oauth_flow_provider.revoke_token(self._token.access_token)

        self._token = None
        return SignOutResponse()
