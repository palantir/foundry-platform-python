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
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from urllib.parse import urlencode

import pydantic
import requests

from foundry._core.auth_utils import Token


class OAuthUtils:
    base_context_path = "/multipass"
    authorize_request_path = "/api/oauth2/authorize"
    token_request_path = "/api/oauth2/token"
    revoke_request_path = "/api/oauth2/revoke_token"

    @staticmethod
    def get_token_uri(base_uri: str, context_path: Optional[str] = None) -> str:
        return OAuthUtils.create_uri(
            base_uri, context_path or OAuthUtils.base_context_path, OAuthUtils.token_request_path
        )

    @staticmethod
    def get_authorize_uri(base_uri: str, context_path: Optional[str] = None) -> str:
        return OAuthUtils.create_uri(
            base_uri,
            context_path or OAuthUtils.base_context_path,
            OAuthUtils.authorize_request_path,
        )

    @staticmethod
    def get_revoke_uri(base_uri: str, context_path: Optional[str] = None) -> str:
        return OAuthUtils.create_uri(
            base_uri, context_path or OAuthUtils.base_context_path, OAuthUtils.revoke_request_path
        )

    @staticmethod
    def create_uri(base_uri: str, context_path: str, request_path: str) -> str:
        if base_uri.startswith("https://"):
            return base_uri + context_path + request_path
        else:
            return "https://" + base_uri + context_path + request_path


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


class ConfidentialClientOAuthFlowProvider:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        url: str,
        multipass_context_path: Optional[str] = None,
        scopes: Optional[List[str]] = None,
    ):
        self._client_id = client_id
        self._client_secret = client_secret
        self.url = url
        self.multipass_context_path = multipass_context_path
        self.scopes = scopes

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def client_secret(self) -> str:
        return self._client_secret

    def get_token(self) -> OAuthToken:
        params = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "grant_type": "client_credentials",
        }
        scopes = self.get_scopes()
        if len(scopes) > 0:
            params["scope"] = " ".join(scopes)

        token_url = OAuthUtils.get_token_uri(self.url, self.multipass_context_path)
        response = requests.post(token_url, data=params)
        response.raise_for_status()
        return OAuthToken(token=OAuthTokenResponse(token_response=response.json()))

    def revoke_token(self, access_token: str) -> None:
        body = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "token": access_token,
        }

        token_url = OAuthUtils.get_revoke_uri(self.url, self.multipass_context_path)
        revoke_token_response = requests.post(token_url, data=body)
        revoke_token_response.raise_for_status()

    def get_scopes(self) -> List[str]:
        scopes = []
        if self.scopes:
            scopes.extend(self.scopes)
        scopes.append("offline_access")
        return scopes


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
        url: str,
        multipass_context_path: Optional[str] = None,
        scopes: Optional[List[str]] = None,
    ):
        self._client_id = client_id
        self._redirect_url = redirect_url
        self.url = url
        self.multipass_context_path = multipass_context_path
        self.scopes = scopes

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def redirect_url(self) -> str:
        return self._redirect_url

    def generate_auth_request(self) -> AuthorizeRequest:
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

        authorize_url = OAuthUtils.get_authorize_uri(self.url, self.multipass_context_path)

        return AuthorizeRequest(
            url=f"{authorize_url}?{urlencode(params, doseq=True)}",
            state=state,
            code_verifier=code_verifier,
        )

    def get_token(self, code: str, code_verifier: str) -> OAuthToken:
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

        token_url = OAuthUtils.get_token_uri(self.url, self.multipass_context_path)
        response = requests.post(token_url, data=params, headers=headers)
        response.raise_for_status()
        return OAuthToken(token=OAuthTokenResponse(token_response=response.json()))

    def refresh_token(self, refresh_token: str) -> OAuthToken:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {
            "grant_type": "refresh_token",
            "client_id": self._client_id,
            "refresh_token": refresh_token,
        }

        token_url = OAuthUtils.get_token_uri(self.url, self.multipass_context_path)
        response = requests.post(token_url, data=params, headers=headers)
        response.raise_for_status()
        return OAuthToken(token=OAuthTokenResponse(token_response=response.json()))

    def revoke_token(self, access_token: str) -> None:
        body = {
            "client_id": self._client_id,
            "token": access_token,
        }

        token_url = OAuthUtils.get_revoke_uri(self.url, self.multipass_context_path)
        revoke_token_response = requests.post(token_url, data=body)
        revoke_token_response.raise_for_status()

    def get_scopes(self) -> List[str]:
        scopes = []
        if self.scopes:
            scopes.extend(self.scopes)
        scopes.append("offline_access")
        return scopes
