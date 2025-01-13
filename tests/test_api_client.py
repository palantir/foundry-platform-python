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


import json
import sys
import warnings
from typing import Any
from typing import Dict
from typing import Optional
from typing import cast
from unittest.mock import ANY
from unittest.mock import Mock

import pytest
import requests

from foundry import PalantirRPCException
from foundry import UserTokenAuth
from foundry import __version__
from foundry._core import ApiClient
from foundry._core import RequestInfo
from foundry._core.config import Config


class AttrDict(Dict[str, Any]):
    def __init__(self, *args: Any, **kwargs: Any):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


EXAMPLE_ERROR = json.dumps(
    {
        "errorCode": "ERROR_CODE",
        "errorName": "ERROR_NAME",
        "errorInstanceId": "123",
        "parameters": {},
    }
)


def assert_called_with(client: ApiClient, **kwargs):
    request = cast(Mock, client._session.request)
    request.assert_called_with(
        **{
            "method": ANY,
            "url": ANY,
            "headers": ANY,
            "params": ANY,
            "data": ANY,
            "stream": ANY,
            "timeout": ANY,
            **kwargs,
        }
    )


def create_client(config: Optional[Config] = None):
    client = ApiClient(auth=UserTokenAuth(token="bar"), hostname="foo", config=config)
    client._session.request = Mock(return_value=AttrDict(status_code=200, headers={}))
    return client


def test_can_override_session_using_deprecated_method():
    client = create_client()
    assert isinstance(client.session._session, requests.Session)
    client.session._session.headers["Foo"] = "Bar"


def test_accessing_session_emits_warnings():
    client = create_client()
    with warnings.catch_warnings(record=True) as w:
        client.session
        assert len(w) == 1


def test_default_headers():
    """Test that the user agent is set correctly."""
    client = create_client()
    assert client._session.headers == {
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "User-Agent": f"python-foundry-platform-sdk/{__version__} python/3.{sys.version_info.minor}",
    }

    """Test that additional headers can be added."""
    client = create_client(Config(default_headers={"Foo": "Bar"}))
    assert client._session.headers == {
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Foo": "Bar",
        "User-Agent": f"python-foundry-platform-sdk/{__version__} python/3.{sys.version_info.minor}",
    }


def test_authorization_header():
    client = create_client()
    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar"))
    # Ensure the bearer token gets added to the headers
    assert_called_with(client, headers={"Authorization": "Bearer bar"})


def test_proxies():
    client = create_client(Config(proxies={"https": "https://foo.bar", "http": "http://foo.bar"}))
    assert client._session.proxies == {"https": "https://foo.bar", "http": "http://foo.bar"}


def test_timeout():
    client = create_client(config=Config(timeout=60))

    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=None))
    assert_called_with(client, timeout=60)

    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=30))
    assert_called_with(client, timeout=30)


def test_verify():
    client = create_client()
    assert client._session.verify == True

    client = create_client(Config(verify=False))
    assert client._session.verify == False


def test_default_params():
    client = create_client(Config(default_params={"foo": "bar"}))
    assert client._session.params == {"foo": "bar"}


def test_scheme():
    client = create_client()
    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=30))
    assert_called_with(client, url="https://foo/api/foo/bar")

    client = create_client(Config(scheme="http"))
    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=30))
    assert_called_with(client, url="http://foo/api/foo/bar")


def test_path_encoding():
    client = create_client()

    client.call_api(
        RequestInfo.with_defaults(
            "GET",
            "/files/{path}",
            path_params={"path": "/my/file.txt"},
        )
    )

    assert_called_with(client, url="https://foo/api/files/%2Fmy%2Ffile.txt")


def test_shared_connection_pool():
    client1 = create_client()
    client2 = create_client()
    session1 = client1._session
    session2 = client2._session

    assert (
        session1.get_adapter("http://").poolmanager == session2.get_adapter("http://").poolmanager  # type: ignore
    )

    assert (
        session1.get_adapter("https://").poolmanager == session2.get_adapter("https://").poolmanager  # type: ignore
    )


def call_api_helper(
    status_code: int,
    data: str,
    headers: Dict[str, str],
):
    client = ApiClient(auth=UserTokenAuth(token="bar"), hostname="foo")

    client._session.request = Mock(
        return_value=AttrDict(
            status_code=status_code,
            headers=headers,
            content=data.encode(),
            text=data,
            json=lambda: json.loads(data),
        )
    )

    return client.call_api(
        RequestInfo(
            method="POST",
            resource_path="/abc",
            query_params={},
            header_params={},
            path_params={},
            body={},
            body_type=Any,
            response_type={},
            request_timeout=None,
        )
    )


def test_call_api_400():
    with pytest.raises(PalantirRPCException) as info:
        call_api_helper(status_code=400, data=EXAMPLE_ERROR, headers={"Header": "A"})

    assert info.value.name == "ERROR_NAME"
    assert info.value.error_instance_id == "123"
    assert info.value.parameters == {}


def test_call_api_403():
    with pytest.raises(PalantirRPCException):
        call_api_helper(status_code=403, data=EXAMPLE_ERROR, headers={"Ha": "Ha"})


def test_call_api_404():
    with pytest.raises(PalantirRPCException):
        call_api_helper(status_code=404, data=EXAMPLE_ERROR, headers={"Ha": "Ha"})


def test_call_api_500():
    with pytest.raises(PalantirRPCException):
        call_api_helper(status_code=500, data=EXAMPLE_ERROR, headers={"Ha": "Ha"})


def test_call_api_333():
    with pytest.raises(PalantirRPCException):
        call_api_helper(status_code=333, data=EXAMPLE_ERROR, headers={"Ha": "Ha"})
