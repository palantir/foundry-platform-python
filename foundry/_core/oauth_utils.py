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


import base64
import hashlib
import secrets
import string
import time
import warnings
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from urllib.parse import urlencode

import httpx
import pydantic

from foundry._core.auth_utils import Auth
from foundry._core.auth_utils import Token
from foundry._core.config import Config
from foundry._core.http_client import HttpClient


class OAuthUtils:
    base_context_path = "/multipass"
    authorize_request_path = "/api/oauth2/authorize"
    token_request_path = "/api/oauth2/token"
    revoke_request_path = "/api/oauth2/revoke_token"

    @staticmethod
    def get_token_uri(context_path: Optional[str] = None) -> str:
        return OAuthUtils.create_uri(context_path, OAuthUtils.token_request_path)

    @staticmethod
    def get_authorize_uri(context_path: Optional[str] = None) -> str:
        return OAuthUtils.create_uri(context_path, OAuthUtils.authorize_request_path)

    @staticmethod
    def get_revoke_uri(context_path: Optional[str] = None) -> str:
        return OAuthUtils.create_uri(context_path, OAuthUtils.revoke_request_path)

    @staticmethod
    def create_uri(context_path: Optional[str], request_path: str) -> str:
        return (context_path or OAuthUtils.base_context_path) + request_path


class SignInResponse(pydantic.BaseModel):
    session: Dict[str, Any]


class SignOutResponse(pydantic.BaseModel):
    pass


class OAuthTokenResponse(pydantic.BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: Optional[str] = None

    def __init__(self, token_response: Dict[str, Any]) -> None:
        super().__init__(**token_response)


class OAuthToken(Token):
    def __init__(self, token: OAuthTokenResponse):
        self._token = token

    @property
    def access_token(self) -> str:
        return self._token.access_token

    @property
    def refresh_token(self) -> Optional[str]:
        return self._token.refresh_token

    @property
    def expires_in(self) -> int:
        return self._token.expires_in

    @property
    def token_type(self) -> str:
        return self._token.token_type

    def _calculate_expiration(self) -> int:
        return int(self._token.expires_in * 1000 + self.current_time())

    @property
    def expires_at(self) -> int:
        return self._calculate_expiration()

    @staticmethod
    def current_time() -> int:
        return int(time.time() * 1000)


class AuthorizeRequest(pydantic.BaseModel):
    url: str
    state: str
    code_verifier: str


class OAuth(Auth, ABC):
    def __init__(
        self,
        hostname: Optional[str],
        config: Optional[Config],
    ) -> None:
        self._config = config
        self._hostname = hostname
        self._parameterized_directly = config is not None or hostname is not None
        self._client: Optional[HttpClient] = None

    @abstractmethod
    def sign_out(self) -> SignOutResponse:
        pass

    def execute_with_token(self, func: Callable[[OAuthToken], httpx.Response]) -> httpx.Response:
        try:
            return self._run_with_attempted_refresh(func)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                self.sign_out()
            raise e
        except Exception as e:
            raise e

    def run_with_token(self, func: Callable[[OAuthToken], httpx.Response]) -> None:
        self.execute_with_token(func)

    @abstractmethod
    def _refresh_token(self) -> None:
        pass

    @abstractmethod
    def get_token(self) -> OAuthToken:
        pass

    def _run_with_attempted_refresh(
        self, func: Callable[[OAuthToken], httpx.Response]
    ) -> httpx.Response:
        """
        Attempt to run func, and if it fails with a 401, refresh the token and try again.
        If it fails with a 401 again, raise the exception.
        """
        try:
            return func(self.get_token())
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                self._refresh_token()
                return func(self.get_token())
            else:
                raise e

    def _parameterize(self, hostname: str, config: Optional[Config]) -> None:
        if self._parameterized_directly:
            warnings.warn(
                f"When a {self.__class__.__name__} instance is given to a FoundryClient, its hostname "
                "and config are automatically provided by the FoundryClient. Please remove these "
                "parameters from the {self.__class__.__name__} initialization.",
                UserWarning,
                stacklevel=2,
            )

        if self._client is not None:
            return

        self._config = config
        self._hostname = hostname

        # Set here so that the next call to _parameterize() doesn't re-create another HttpClient
        # This method may be called many times dependening on how many different ApiClients
        # are created with the same Auth object
        self._client = HttpClient(hostname, config)

    def _get_client(self) -> HttpClient:
        if self._client is None:
            if self._hostname is None:
                raise ValueError(
                    f"The hostname must be provided to {self.__class__.__name__} when fetching a token."
                )

            self._client = HttpClient(hostname=self._hostname, config=self._config)

        return self._client


class ConfidentialClientOAuthFlowProvider:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        multipass_context_path: Optional[str] = None,
        scopes: Optional[List[str]] = None,
    ):
        self._client_id = client_id
        self._client_secret = client_secret
        self.multipass_context_path = multipass_context_path
        self.scopes = scopes

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def client_secret(self) -> str:
        return self._client_secret

    def get_token(self, client: HttpClient) -> OAuthToken:
        params = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "grant_type": "client_credentials",
        }
        scopes = self.get_scopes()
        if len(scopes) > 0:
            params["scope"] = " ".join(scopes)

        token_url = OAuthUtils.get_token_uri(self.multipass_context_path)
        response = client.post(token_url, data=params)
        response.raise_for_status()
        return OAuthToken(token=OAuthTokenResponse(token_response=response.json()))

    def revoke_token(self, client: HttpClient, access_token: str) -> None:
        body = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "token": access_token,
        }

        token_url = OAuthUtils.get_revoke_uri(self.multipass_context_path)
        revoke_token_response = client.post(token_url, data=body)
        revoke_token_response.raise_for_status()

    def get_scopes(self) -> List[str]:
        if not self.scopes:
            return []
        return [*self.scopes, "offline_access"]


def generate_random_string(min_length: int = 43, max_length: int = 128) -> str:
    characters = string.ascii_letters + string.digits + "-._~"
    length = secrets.randbelow(max_length - min_length + 1) + min_length
    return "".join(secrets.choice(characters) for _ in range(length))


def generate_code_challenge(input_string: str) -> str:
    # Calculate the SHA256 hash
    sha256_hash = hashlib.sha256(input_string.encode("utf-8")).digest()

    # Base64-URL encode the hash and remove padding
    base64url_encoded = base64.urlsafe_b64encode(sha256_hash).rstrip(b"=")

    return base64url_encoded.decode("utf-8")


class PublicClientOAuthFlowProvider:
    def __init__(
        self,
        client_id: str,
        redirect_url: str,
        multipass_context_path: Optional[str] = None,
        scopes: Optional[List[str]] = None,
    ):
        self._client_id = client_id
        self._redirect_url = redirect_url
        self.multipass_context_path = multipass_context_path
        self.scopes = scopes

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def redirect_url(self) -> str:
        return self._redirect_url

    def generate_auth_request(self, client: HttpClient) -> AuthorizeRequest:
        state = generate_random_string()
        code_verifier = generate_random_string()
        code_challenge = generate_code_challenge(code_verifier)

        params = {
            "response_type": "code",
            "client_id": self._client_id,
            "redirect_uri": self._redirect_url,
            "code_challenge": code_challenge,
            "code_challenge_method": "S256",
            "state": state,
        }
        scopes = self.get_scopes()
        if len(scopes) > 0:
            params["scope"] = " ".join(scopes)

        authorize_url = OAuthUtils.get_authorize_uri(self.multipass_context_path)

        return AuthorizeRequest(
            url=f"{client.base_url}{authorize_url}?{urlencode(params, doseq=True)}",
            state=state,
            code_verifier=code_verifier,
        )

    def get_token(self, client: HttpClient, code: str, code_verifier: str) -> OAuthToken:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self._redirect_url,
            "client_id": self._client_id,
            "code_verifier": code_verifier,
        }
        scopes = self.get_scopes()
        if len(scopes) > 0:
            params["scope"] = " ".join(scopes)

        token_url = OAuthUtils.get_token_uri(self.multipass_context_path)
        response = client.post(token_url, data=params, headers=headers)
        response.raise_for_status()
        return OAuthToken(token=OAuthTokenResponse(token_response=response.json()))

    def refresh_token(self, client: HttpClient, refresh_token: str) -> OAuthToken:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {
            "grant_type": "refresh_token",
            "client_id": self._client_id,
            "refresh_token": refresh_token,
        }

        token_url = OAuthUtils.get_token_uri(self.multipass_context_path)
        response = client.post(token_url, data=params, headers=headers)
        response.raise_for_status()
        return OAuthToken(token=OAuthTokenResponse(token_response=response.json()))

    def revoke_token(self, client: HttpClient, access_token: str) -> None:
        body = {
            "client_id": self._client_id,
            "token": access_token,
        }

        token_url = OAuthUtils.get_revoke_uri(self.multipass_context_path)
        revoke_token_response = client.post(token_url, data=body)
        revoke_token_response.raise_for_status()

    def get_scopes(self) -> List[str]:
        if not self.scopes:
            return []
        return [*self.scopes, "offline_access"]
