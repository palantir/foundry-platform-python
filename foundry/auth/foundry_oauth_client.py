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

from typing import Callable
from typing import List
from typing import Optional
from typing import TypeVar


from foundry.auth._auth_utils import Auth
from foundry.auth._oauth_utils import ServerOAuthFlowProvider, OAuthToken
from foundry.auth.oauth import SignInResponse, SignOutResponse
from foundry.exceptions import OpenApiException, UnauthorizedException


T = TypeVar("T")


class ConfidentialClientAuth(Auth):
    """
    Client for OAuth-authenticated Ontology applications.
    Runs a background thread to periodically refresh access token.

    :param client_id: OAuth client id to be used by the application.
    :param client_secret: OAuth client secret to be used by the application.
    :param hostname: Hostname for authentication and ontology endpoints.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        hostname: str,
        scopes: List[str],
    ) -> None:
        if len(scopes) == 0:
            raise ValueError(
                "You have not provided any scopes. At least one scope must be provided."
            )

        super().__init__(hostname=hostname)
        self._client_id = client_id
        self._client_secret = client_secret
        self._token: Optional[OAuthToken] = None
        self._server_oauth_flow_provider = ServerOAuthFlowProvider(
            client_id,
            client_secret,
            hostname,
            scopes=scopes,
        )

    def get_token(self) -> OAuthToken:
        if self._token is None:
            raise OpenApiException(
                "ConfidentialClientAuth has not been authenticated. Please call sign_in_as_service_user() first."
            )

        return self._token

    def execute_with_token(self, func: Callable[[OAuthToken], T]) -> T:
        try:
            return self._run_with_attempted_refresh(func)
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
        except UnauthorizedException:
            self._refresh_token()
            return func(self.get_token())

    def _refresh_token(self):
        self._token = self._server_oauth_flow_provider.get_token()

    def sign_in_as_service_user(self) -> SignInResponse:
        token = self._server_oauth_flow_provider.get_token()
        self._token = token

        return SignInResponse(
            session={"accessToken": token.access_token, "expiresIn": token.expires_in}
        )

    def sign_out(self) -> SignOutResponse:
        if self._token:
            self._server_oauth_flow_provider.revoke_token(self._token.access_token)

        self._token = None
        return SignOutResponse()
