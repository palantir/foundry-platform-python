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
import webbrowser
from typing import Callable
from typing import List
from typing import Optional
from typing import TypeVar

import requests

from foundry._core.auth_utils import Auth
from foundry._core.oauth import SignOutResponse
from foundry._core.oauth_utils import AuthorizeRequest
from foundry._core.oauth_utils import OAuthToken
from foundry._core.oauth_utils import PublicClientOAuthFlowProvider
from foundry._errors.not_authenticated import NotAuthenticated
from foundry._errors.sdk_internal_error import SDKInternalError

T = TypeVar("T")


class PublicClientAuth(Auth):
    scopes: List[str] = ["api:read-data", "api:write-data", "offline_access"]

    """
    Client for Public Client OAuth-authenticated Ontology applications.
    Runs a background thread to periodically refresh access token.

    :param client_id: OAuth client id to be used by the application.
    :param client_secret: OAuth client secret to be used by the application.
    :param hostname: Hostname for authentication and ontology endpoints.
    """

    def __init__(
        self, client_id: str, redirect_url: str, hostname: str, should_refresh: bool = False
    ) -> None:
        self._client_id = client_id
        self._redirect_url = redirect_url

        self._token: Optional[OAuthToken] = None
        self._should_refresh = should_refresh
        self._stop_refresh_event = threading.Event()
        self._hostname = hostname
        self._server_oauth_flow_provider = PublicClientOAuthFlowProvider(
            client_id=client_id, redirect_url=redirect_url, url=self.url, scopes=self.scopes
        )
        self._auth_request: Optional[AuthorizeRequest] = None

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

    def _refresh_token(self):
        if self._token is None:
            raise Exception("")

        self._token = self._server_oauth_flow_provider.refresh_token(
            refresh_token=self._token.refresh_token
        )

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

    def sign_in(self) -> None:
        self._auth_request = self._server_oauth_flow_provider.generate_auth_request()
        webbrowser.open(self._auth_request.url)

    def _start_auto_refresh(self):
        def _auto_refresh_token():
            while not self._stop_refresh_event.is_set():
                if self._token:
                    # Sleep for (expires_in - 60) seconds to refresh the token 1 minute before it expires
                    time.sleep(self._token.expires_in - 60)
                    self._token = self._server_oauth_flow_provider.refresh_token(
                        refresh_token=self._token.refresh_token
                    )
                else:
                    # Wait 10 seconds and check again if the token is set
                    time.sleep(10)

        refresh_thread = threading.Thread(target=_auto_refresh_token, daemon=True)
        refresh_thread.start()

    def set_token(self, code: str, state: str) -> None:
        if self._auth_request is None or state != self._auth_request.state:
            raise RuntimeError("Unable to verify the state")

        self._token = self._server_oauth_flow_provider.get_token(
            code=code, code_verifier=self._auth_request.code_verifier
        )

        if self._should_refresh:
            self._start_auto_refresh()
        return

    def sign_out(self) -> SignOutResponse:
        if self._token:
            self._server_oauth_flow_provider.revoke_token(self._token.access_token)

        self._token = None

        # Signal the auto-refresh thread to stop
        self._stop_refresh_event.set()

        return SignOutResponse()
