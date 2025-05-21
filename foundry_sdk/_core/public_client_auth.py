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
from typing import List
from typing import Optional

from foundry_sdk._core.config import Config
from foundry_sdk._core.oauth_utils import AuthorizeRequest
from foundry_sdk._core.oauth_utils import OAuth
from foundry_sdk._core.oauth_utils import OAuthToken
from foundry_sdk._core.oauth_utils import PublicClientOAuthFlowProvider
from foundry_sdk._core.oauth_utils import SignOutResponse
from foundry_sdk._errors.not_authenticated import NotAuthenticated


class PublicClientAuth(OAuth):
    """
    Client for Public Client OAuth-authenticated Ontology applications.
    Runs a background thread to periodically refresh access token.

    :param client_id: OAuth client id to be used by the application.
    :param redirect_url: The URL the authorization server should redirect the user to after the user approves the request.
    :param scopes: The list of scopes to request. By default, no specific scope is provided and a token will be returned with all scopes.
    :param hostname: Hostname for authentication. This is only required if using PublicClientAuth independently of the FoundryClient.
    :param config: The HTTP config for authentication. This is only required if using ConfidentialClientAuth independently of the FoundryClient.
    """

    def __init__(
        self,
        client_id: str,
        redirect_url: str,
        hostname: Optional[str] = None,
        scopes: Optional[List[str]] = None,
        should_refresh: bool = True,
        *,
        config: Optional[Config] = None,
    ) -> None:
        self._client_id = client_id
        self._redirect_url = redirect_url

        self._token: Optional[OAuthToken] = None
        self._should_refresh = should_refresh
        self._stop_refresh_event = threading.Event()
        self._scopes = scopes
        self._auth_request: Optional[AuthorizeRequest] = None
        self._server_oauth_flow_provider = PublicClientOAuthFlowProvider(
            client_id=client_id,
            redirect_url=redirect_url,
            scopes=scopes,
        )
        super().__init__(hostname=hostname, should_refresh=should_refresh, config=config)

    @property
    def scopes(self) -> List[str]:
        return self._server_oauth_flow_provider.scopes or []

    def get_token(self) -> OAuthToken:
        if self._token is None:
            raise NotAuthenticated("Client has not been authenticated.")
        return self._token

    def _refresh_token(self) -> None:
        if not self._token:
            raise RuntimeError("must have token to refresh")

        if not self._token.refresh_token:
            raise RuntimeError("no refresh token provided")

        self._token = self._server_oauth_flow_provider.refresh_token(
            self._get_client(),
            refresh_token=self._token.refresh_token,
        )

    @property
    def url(self) -> str:
        return self._get_client().base_url.host

    def sign_in(self) -> str:
        self._auth_request = self._server_oauth_flow_provider.generate_auth_request(
            self._get_client()
        )
        return self._auth_request.url

    def _start_auto_refresh(self) -> None:
        def _auto_refresh_token() -> None:
            while not self._stop_refresh_event.is_set():
                if self._token and self._token.refresh_token:
                    # Sleep for (expires_in - 60) seconds to refresh the token 1 minute before it expires
                    time.sleep(self._token.expires_in - 60)
                    self._token = self._server_oauth_flow_provider.refresh_token(
                        self._get_client(),
                        refresh_token=self._token.refresh_token,
                    )
                else:
                    # Wait 10 seconds and check again if the token is set
                    time.sleep(10)

        refresh_thread = threading.Thread(target=_auto_refresh_token, daemon=True)
        refresh_thread.start()

    def set_token(self, code: str, state: str) -> None:
        if not self._auth_request:
            raise RuntimeError("Must sign in prior to setting token")

        if state != self._auth_request.state:
            raise RuntimeError("Unable to verify state")

        self._token = self._server_oauth_flow_provider.get_token(
            self._get_client(),
            code=code,
            code_verifier=self._auth_request.code_verifier,
        )

        if self._should_refresh:
            self._start_auto_refresh()

    def sign_out(self) -> SignOutResponse:
        if self._token:
            self._server_oauth_flow_provider.revoke_token(
                self._get_client(),
                self._token.access_token,
            )

        self._token = None

        # Signal the auto-refresh thread to stop
        self._stop_refresh_event.set()

        return SignOutResponse()
