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


from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Tuple
from typing import Union

import requests

from foundry._core.auth_utils import Auth
from foundry._core.auth_utils import Token
from foundry._core.utils import remove_prefixes


def _run_with_401_status_check(
    callable: Callable[[Token], requests.Response]
) -> Callable[[Token], requests.Response]:
    def f(token: Token) -> requests.Response:
        response = callable(token)
        if response.status_code == 401:
            response.raise_for_status()
        return response

    func: Callable[[Token], requests.Response] = lambda token: f(token)
    return func


_Params = Union[Mapping[str, Any], List[Tuple[str, Any]]]


class PalantirSession:
    """Submits http requests with a dependency-injected authentication token provider.

    :param auth: Dependency that provides credentials for authentication.
    :param preview: Boolean that enables access to endpoints in Preview Mode by default. Defaults to False.
    """

    def __init__(self, auth: Auth, hostname: str, preview: bool = False) -> None:
        self._auth = auth
        self._hostname = remove_prefixes(hostname, ["https://", "http://"])
        self.preview = preview
        self._session = requests.Session()

    @property
    def hostname(self) -> str:
        return self._remove_host_prefix(self._hostname)

    def request(
        self,
        method: str,
        url: str,
        headers: Optional[Mapping[str, Any]] = None,
        params: Optional[_Params] = None,
        data: Optional[bytes] = None,
        json: Optional[Any] = None,
        stream: bool = True,
        timeout: Optional[int] = None,
    ) -> requests.Response:
        request_fn = _run_with_401_status_check(
            lambda token: self._session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json,
                headers=self._add_user_agent_and_auth_headers(token, headers),
                stream=stream,
                timeout=timeout,
            )
        )
        return self._auth.execute_with_token(request_fn)

    def get(
        self,
        url: str,
        headers: Optional[Mapping[str, Any]] = None,
        params: Optional[_Params] = None,
        data: Optional[bytes] = None,
        json: Optional[Any] = None,
        stream: bool = True,
    ) -> requests.Response:
        request_fn = _run_with_401_status_check(
            lambda token: self._session.get(
                url=url,
                params=params,
                data=data,
                json=json,
                headers=self._add_user_agent_and_auth_headers(token, headers),
                stream=stream,
            )
        )
        return self._auth.execute_with_token(request_fn)

    def post(
        self,
        url: str,
        headers: Optional[Mapping[str, Any]] = None,
        params: Optional[_Params] = None,
        data: Optional[bytes] = None,
        json: Optional[Any] = None,
        stream: bool = True,
    ) -> requests.Response:
        request_fn = _run_with_401_status_check(
            lambda token: self._session.post(
                url=url,
                params=params,
                data=data,
                json=json,
                headers=self._add_user_agent_and_auth_headers(token, headers),
                stream=stream,
            )
        )
        return self._auth.execute_with_token(request_fn)

    def put(
        self,
        url: str,
        headers: Optional[Mapping[str, Any]] = None,
        params: Optional[_Params] = None,
        data: Optional[bytes] = None,
        json: Optional[Any] = None,
        stream: bool = True,
    ) -> requests.Response:
        request_fn = _run_with_401_status_check(
            lambda token: self._session.put(
                url=url,
                params=params,
                data=data,
                json=json,
                headers=self._add_user_agent_and_auth_headers(token, headers),
                stream=stream,
            )
        )
        return self._auth.execute_with_token(request_fn)

    def delete(
        self,
        url: str,
        headers: Optional[Mapping[str, Any]] = None,
        params: Optional[_Params] = None,
        data: Optional[bytes] = None,
        json: Optional[Any] = None,
        stream: bool = True,
    ) -> requests.Response:
        request_fn = _run_with_401_status_check(
            lambda token: self._session.delete(
                url=url,
                params=params,
                data=data,
                json=json,
                headers=self._add_user_agent_and_auth_headers(token, headers),
                stream=stream,
            )
        )
        return self._auth.execute_with_token(request_fn)

    def patch(
        self,
        url: str,
        headers: Optional[Mapping[str, Any]] = None,
        params: Optional[_Params] = None,
        data: Optional[bytes] = None,
        json: Optional[Any] = None,
        stream: bool = True,
    ) -> requests.Response:
        request_fn = _run_with_401_status_check(
            lambda token: self._session.patch(
                url=url,
                params=params,
                data=data,
                json=json,
                headers=self._add_user_agent_and_auth_headers(token, headers),
                stream=stream,
            )
        )
        return self._auth.execute_with_token(request_fn)

    def _add_user_agent_and_auth_headers(
        self, token: Token, headers: Optional[Mapping[str, Any]] = None
    ) -> Dict[str, str]:
        return {
            **(headers or {}),
            "Authorization": "Bearer " + token.access_token,
            # "User-Agent": "palantir-python-sdk-codegen/{} foundry-api/{}".format(foundry.__codegen_version__, foundry.__version__)
        }

    def _remove_host_prefix(self, url: str) -> str:
        return remove_prefixes(url, ["https://", "http://"])
