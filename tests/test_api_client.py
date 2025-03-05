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
import warnings
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional
from typing import cast
from unittest.mock import ANY
from unittest.mock import Mock
from unittest.mock import patch

import httpx
import pytest

from foundry import ApiNotFoundError
from foundry import BadRequestError
from foundry import ConfidentialClientAuth
from foundry import Config
from foundry import ConflictError
from foundry import ConnectionError
from foundry import InternalServerError
from foundry import NotFoundError
from foundry import PalantirRPCException
from foundry import PermissionDeniedError
from foundry import ProxyError
from foundry import RateLimitError
from foundry import ReadTimeout
from foundry import RequestEntityTooLargeError
from foundry import StreamConsumedError
from foundry import UnauthorizedError
from foundry import UnprocessableEntityError
from foundry import UserTokenAuth
from foundry import WriteTimeout
from foundry import __version__
from foundry._core import ApiClient
from foundry._core import RequestInfo

HOSTNAME = "localhost:8123"


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
    build_request = cast(Mock, client._session.build_request)
    build_request.assert_called_with(
        **{
            "method": ANY,
            "url": ANY,
            "headers": ANY,
            "params": ANY,
            "content": ANY,
            "timeout": ANY,
            **kwargs,
        }
    )


def _throw(exception: Exception):
    def wrapper(*_args, **_kwargs):
        raise exception

    return wrapper


def create_mock_client(config: Optional[Config] = None, hostname=HOSTNAME):
    client = ApiClient(auth=UserTokenAuth(token="bar"), hostname=hostname, config=config)
    client._session.build_request = Mock(wraps=client._session.build_request)
    client._session.send = Mock(return_value=AttrDict(status_code=200, headers={}))
    return client


def create_client(
    config: Optional[Config] = None,
    hostname=HOSTNAME,
    scheme: Literal["https", "http"] = "http",
):
    config = config or Config()
    config.scheme = scheme
    return ApiClient(auth=UserTokenAuth(token="bar"), hostname=hostname, config=config)


def test_can_override_session_using_deprecated_method():
    client = create_mock_client()

    with warnings.catch_warnings(record=True) as w:
        assert isinstance(client.session._session, httpx.Client)
        # Ensure the warning is emitted when accessing the session
        assert len(w) == 1

        client.session._session.headers["Foo"] = "Bar"


def test_authorization_header():
    client = create_mock_client()
    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar"))
    # Ensure the bearer token gets added to the headers
    assert_called_with(client, headers={"Authorization": "Bearer bar"})


def test_timeout():
    client = create_mock_client(config=Config(timeout=60))
    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=30))
    assert_called_with(client, timeout=30)


def test_config_passed_to_http_client():
    # Just check that at least one config var was set correctly to ensure
    # the config is being passed to the http client
    client = create_client(config=Config(timeout=60))
    assert client._session.timeout == httpx.Timeout(60)


def test_path_encoding():
    client = create_mock_client()

    client.call_api(
        RequestInfo.with_defaults(
            "GET",
            "/files/{path}",
            path_params={"path": "/my/file.txt"},
        )
    )

    assert_called_with(client, url="/api/files/%2Fmy%2Ffile.txt")


def test_null_query_params():
    client = create_mock_client()
    client.call_api(
        RequestInfo.with_defaults("GET", "/foo/bar", query_params={"foo": "foo", "bar": None})
    )
    assert_called_with(client, url="/api/foo/bar", params=[("foo", "foo")])


def test_shared_transport():
    client1 = create_mock_client()
    client2 = create_mock_client()
    session1 = client1._session
    session2 = client2._session
    assert session1._transport == session2._transport


def call_api_helper(
    status_code: int,
    data: str,
    headers: Dict[str, str] = {},
):
    client = ApiClient(auth=UserTokenAuth(token="bar"), hostname="foo")

    client._session.send = Mock(
        return_value=AttrDict(
            status_code=status_code,
            headers=headers,
            content=data.encode(),
            text=data,
            json=lambda: json.loads(data),
        )
    )

    return client.call_api(RequestInfo.with_defaults("POST", "/abc"))


def test_call_api_400():
    with pytest.raises(BadRequestError) as info:
        call_api_helper(status_code=400, data=EXAMPLE_ERROR, headers={"Header": "A"})

    assert info.value.name == "ERROR_NAME"
    assert info.value.error_instance_id == "123"
    assert info.value.parameters == {}


def test_401_error():
    with pytest.raises(UnauthorizedError):
        call_api_helper(status_code=401, data=EXAMPLE_ERROR)


def test_403_error():
    with pytest.raises(PermissionDeniedError):
        call_api_helper(status_code=403, data=EXAMPLE_ERROR)


def test_404_error():
    with pytest.raises(NotFoundError):
        call_api_helper(status_code=404, data=EXAMPLE_ERROR)


def test_422_error():
    with pytest.raises(UnprocessableEntityError):
        call_api_helper(status_code=422, data=EXAMPLE_ERROR)


def test_429_error():
    with pytest.raises(RateLimitError):
        call_api_helper(status_code=429, data=EXAMPLE_ERROR)


def test_413_error():
    with pytest.raises(RequestEntityTooLargeError):
        call_api_helper(status_code=413, data=EXAMPLE_ERROR)


def test_409_error():
    with pytest.raises(ConflictError):
        call_api_helper(status_code=409, data=EXAMPLE_ERROR)


def test_call_api_500():
    with pytest.raises(InternalServerError):
        call_api_helper(status_code=500, data=EXAMPLE_ERROR)


def test_call_api_599():
    with pytest.raises(InternalServerError):
        call_api_helper(status_code=599, data=EXAMPLE_ERROR)


def test_call_api_600():
    with pytest.raises(PalantirRPCException):
        call_api_helper(status_code=600, data=EXAMPLE_ERROR)


def test_cannot_cause_invalid_url_error():
    client = create_client()
    request_info = RequestInfo.with_defaults("GET", "/foo/{bar}", path_params={"bar": "|https://"})

    # This confirms that the path parameters are encoded since "|https://" in a URL is invalid
    # The encoded path doesn't exist so we get back a 404 error
    with pytest.raises(NotFoundError):
        client.call_api(request_info)


def test_connect_timeout():
    client = create_client(hostname="localhost:9876", config=Config(timeout=1e-6))
    request_info = RequestInfo.with_defaults("GET", "/foo/bar")

    with pytest.raises(ConnectionError):
        client.call_api(request_info)


def test_read_timeout():
    client = create_client(config=Config(timeout=1e-6))
    request_info = RequestInfo.with_defaults("GET", "/foo/timeout")

    with pytest.raises(ReadTimeout):
        client.call_api(request_info)


def test_write_timeout():
    client = create_client(config=Config(timeout=1e-6))
    data = b"*" * 1024 * 1024 * 100
    request_info = RequestInfo.with_defaults("GET", "/foo/timeout", body=data, body_type=bytes)

    with pytest.raises(WriteTimeout):
        client.call_api(request_info)


def test_stream_consumed_error():
    client = create_client()
    request_info = RequestInfo.with_defaults("GET", "/foo/stream")

    with client.stream_api(request_info) as response:
        for _ in response.iter_bytes():
            pass

        with pytest.raises(StreamConsumedError):
            for _ in response.iter_bytes():
                pass


def test_proxy_error():
    client = create_client()
    request_info = RequestInfo.with_defaults("GET", "/proxy/error")

    # I can't figure out a way to mock "ProxyError" since it involves connecting to a server
    # using https
    # https://github.com/encode/httpcore/blob/a1735520e3826ccc861cdadf3e692abfbb19ac6a/httpcore/_sync/http_proxy.py#L156
    # This is an error we could hit so I'll just use the mock library to simulate the error
    with patch("httpx.Client.send", side_effect=_throw(httpx.ProxyError("foo"))):
        with pytest.raises(ProxyError):
            client.call_api(request_info)


def test_ssl_error():
    client = create_client(scheme="https", config=Config(timeout=1))
    request_info = RequestInfo.with_defaults("GET", "localhost:8123")

    with pytest.raises(ConnectionError) as error:
        client.call_api(request_info)

    assert "SSL" in str(error.value)


def test_passing_in_str_auth():
    with pytest.raises(TypeError) as e:
        ApiClient(auth="foo", hostname="localhost:8123")  # type: ignore
        assert str(e.value).startswith(
            "auth must be an instance of UserTokenAuth, ConfidentialClientAuth or PublicClientAuth, not a string."
        )


def test_passing_in_int_to_auth():
    with pytest.raises(TypeError) as e:
        ApiClient(auth=2, hostname="localhost:8123")  # type: ignore
        assert (
            str(e.value)
            == "auth must be an instance of UserTokenAuth, ConfidentialClientAuth or PublicClientAuth, not an instance of int."
        )


def test_passing_in_int_to_hostname():
    with pytest.raises(TypeError) as e:
        ApiClient(auth=UserTokenAuth(token="foo"), hostname=2)  # type: ignore
        assert str(e.value) == "hostname must be a string, not int."


def test_passing_in_int_to_config():
    with pytest.raises(TypeError) as e:
        ApiClient(auth=UserTokenAuth(token="foo"), hostname="localhost:1234", config=2)  # type: ignore
        assert str(e.value) == "config must be an instance of Config, not int."


def test_config_shared_with_auth():
    config = Config(timeout=1)
    auth = ConfidentialClientAuth(client_id="foo", client_secret="bar")
    assert auth._hostname is None
    assert auth._config is None

    with warnings.catch_warnings(record=True) as w:
        ApiClient(auth=auth, hostname="localhost:1234", config=config)
        assert len(w) == 0

    assert auth._hostname == "localhost:1234"
    assert auth._config == config


def test_client_hostname_prioritized():
    config = Config(timeout=1)
    auth = ConfidentialClientAuth(client_id="foo", client_secret="bar", hostname="localhost:9876")

    with warnings.catch_warnings(record=True) as w:
        ApiClient(auth=auth, hostname="localhost:1234", config=config)

        # Make sure the ApiClient hostname is prioritized
        assert auth._hostname == "localhost:1234"

        # And make sure the user receives a warning
        assert len(w) == 1


def test_empty_404_error():
    with pytest.raises(ApiNotFoundError):
        client = ApiClient(auth=UserTokenAuth(token="bar"), hostname="foo")

        client._session.send = Mock(
            return_value=AttrDict(
                status_code=404,
                headers={},
                content=b"",
                text="",
            )
        )

        client.call_api(RequestInfo.with_defaults("POST", "/abc"))
