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

import time
import json
from typing import Dict
from typing import Optional
from typing import List

from pydantic import BaseModel
import urllib.parse
import urllib3

from foundry.auth._auth_utils import Token
from foundry.exceptions import ApiException


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

    @staticmethod
    def post(url: str, data: Dict[str, str]):
        res = urllib3.request(
            method="POST",
            url=url,
            body=urllib.parse.urlencode(data),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if 200 <= res.status < 300:
            return json.loads(res.data.decode("utf-8"))
        else:
            raise ApiException(res)


class OAuthTokenResponse(BaseModel):
    access_token: str
    token_type: str
    refresh_token: Optional[str]
    expires_in: int

    def __init__(self, token_response: dict) -> None:
        super().__init__(**token_response)


class OAuthToken(Token):
    def __init__(self, token: OAuthTokenResponse):
        self._token = token

    @property
    def access_token(self) -> str:
        return self._token.access_token

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


class ServerOAuthFlowProvider:
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
        response = OAuthUtils.post(token_url, data=params)
        return OAuthToken(token=OAuthTokenResponse(token_response=response))

    def revoke_token(self, access_token: str) -> None:
        body = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "token": access_token,
        }

        token_url = OAuthUtils.get_revoke_uri(self.url, self.multipass_context_path)
        OAuthUtils.post(token_url, data=body)

    def get_scopes(self) -> List[str]:
        scopes = []
        if self.scopes:
            scopes.extend(self.scopes)
        scopes.append("offline_access")
        return scopes
