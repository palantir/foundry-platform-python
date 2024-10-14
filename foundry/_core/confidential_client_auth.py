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


import threading
import time
from typing import Callable
from typing import List
from typing import Optional

import requests

from foundry._core.auth_utils import Auth
from foundry._core.oauth import SignInResponse
from foundry._core.oauth import SignOutResponse
from foundry._core.oauth_utils import ConfidentialClientOAuthFlowProvider
from foundry._core.oauth_utils import OAuthToken
from foundry._core.utils import remove_prefixes
from foundry._errors.not_authenticated import NotAuthenticated


class ConfidentialClientAuth(Auth):
    """
    Client for Confidential Client OAuth-authenticated Ontology applications.
    Runs a background thread to periodically refresh access token.

    :param client_id: OAuth client id to be used by the application.
    :param client_secret: OAuth client secret to be used by the application.
    :param scopes: The list of scopes to request. By default, no specific scope is provided and a token will be returned with all scopes.
    :param hostname: Hostname for authentication and ontology endpoints.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        hostname: str,
        scopes: Optional[List[str]] = None,
        should_refresh: bool = False,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._token: Optional[OAuthToken] = None
        self._should_refresh = should_refresh
        self._stop_refresh_event = threading.Event()
        self._hostname = hostname
        self._server_oauth_flow_provider = ConfidentialClientOAuthFlowProvider(
            client_id, client_secret, self.url, scopes=scopes
        )

    def get_token(self) -> OAuthToken:
        if self._token is None:
            raise NotAuthenticated("Client has not been authenticated.")
        return self._token

    def execute_with_token(
        self, func: Callable[[OAuthToken], requests.Response]
    ) -> requests.Response:
        try:
            return self._run_with_attempted_refresh(func)
        except requests.HTTPError as http_e:
            if http_e.response.status_code == 401:
                self.sign_out()
            raise http_e
        except Exception as e:
            raise e

    def run_with_token(self, func: Callable[[OAuthToken], requests.Response]) -> None:
        try:
            self._run_with_attempted_refresh(func)
        except requests.HTTPError as http_e:
            if http_e.response.status_code == 401:
                self.sign_out()
            raise http_e
        except Exception as e:
            raise e

    def _run_with_attempted_refresh(
        self, func: Callable[[OAuthToken], requests.Response]
    ) -> requests.Response:
        """
        Attempt to run func, and if it fails with a 401, refresh the token and try again.
        If it fails with a 401 again, raise the exception.
        """
        try:
            return func(self.get_token())
        except requests.HTTPError as e:
            if e.response.status_code == 401:
                self._refresh_token()
                return func(self.get_token())
            else:
                raise e

    @property
    def url(self) -> str:
        return remove_prefixes(self._hostname, ["https://", "http://"])

    def _refresh_token(self) -> None:
        self._token = self._server_oauth_flow_provider.get_token()

    def _start_auto_refresh(self) -> None:
        def _auto_refresh_token() -> None:
            while not self._stop_refresh_event.is_set():
                if self._token:
                    # Sleep for (expires_in - 60) seconds to refresh the token 1 minute before it expires
                    time.sleep(self._token.expires_in - 60)
                    self._refresh_token()
                else:
                    # Wait 10 seconds and check again if the token is set
                    time.sleep(10)

        refresh_thread = threading.Thread(target=_auto_refresh_token, daemon=True)
        refresh_thread.start()

    def sign_in_as_service_user(self) -> SignInResponse:
        token = self._server_oauth_flow_provider.get_token()
        self._token = token

        if self._should_refresh:
            self._start_auto_refresh()
        return SignInResponse(
            session={"accessToken": token.access_token, "expiresIn": token.expires_in}
        )

    def sign_out(self) -> SignOutResponse:
        if self._token:
            self._server_oauth_flow_provider.revoke_token(self._token.access_token)

        self._token = None

        # Signal the auto-refresh thread to stop
        self._stop_refresh_event.set()

        return SignOutResponse()
