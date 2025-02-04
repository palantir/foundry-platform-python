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
import ssl
import sys
import warnings
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import cast
from unittest.mock import ANY
from unittest.mock import Mock
from unittest.mock import patch

import httpcore
import httpx
import pytest
from httpx._utils import URLPattern

from foundry import BadRequestError
from foundry import ConnectionError
from foundry import InternalServerError
from foundry import NotFoundError
from foundry import PalantirRPCException
from foundry import PermissionDeniedError
from foundry import ProxyError
from foundry import RateLimitError
from foundry import ReadTimeout
from foundry import StreamConsumedError
from foundry import UnauthorizedError
from foundry import UnprocessableEntityError
from foundry import UserTokenAuth
from foundry import WriteTimeout
from foundry import __version__
from foundry._core import ApiClient
from foundry._core import RequestInfo
from foundry._core.config import Config

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


def assert_http_transport(transport: Optional[httpx.BaseTransport]) -> httpx.HTTPTransport:
    return assert_isinstance(transport, httpx.HTTPTransport)


def assert_http_proxy(pool: Optional[httpcore.ConnectionPool]) -> httpcore.HTTPProxy:
    return assert_isinstance(pool, httpcore.HTTPProxy)


T = TypeVar("T")


def assert_isinstance(instance: Any, type: Type[T]) -> T:
    if not isinstance(instance, type):
        raise Exception(f"Not an instance of {type}", instance)

    return instance


def _throw(exception: Exception):
    def wrapper(*_args, **_kwargs):
        raise exception

    return wrapper


def url_to_str(url: httpcore.URL) -> str:
    """
    Convert an httpcore.URL object to a string without including the default port.

    Args:
    url (httpcore.URL): The URL object to be converted.

    Returns:
    str: The URL as a string without the default port.
    """
    # Default ports for common schemes
    default_ports = {
        "http": 80,
        "https": 443,
    }

    # Extract components of the URL
    scheme = url.scheme.decode("utf-8")
    host = url.host.decode("utf-8")
    port = url.port
    target = url.target.decode("utf-8")

    # Construct the URL without the default port
    if port and port == default_ports.get(scheme):
        port = None

    # Reconstruct the URL
    netloc = f"{host}:{port}" if port else host
    url_str = f"{scheme}://{netloc}{target}"

    return url_str


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


def test_client_hostname():
    assert (
        ApiClient(
            auth=UserTokenAuth(token="bar"), hostname="https://a.b.c.com", config=None
        )._hostname
        == "a.b.c.com"
    )
    assert (
        ApiClient(
            auth=UserTokenAuth(token="bar"), hostname="http://a.b.c.com", config=None
        )._hostname
        == "a.b.c.com"
    )
    assert (
        ApiClient(auth=UserTokenAuth(token="bar"), hostname="a.b.c.com/", config=None)._hostname
        == "a.b.c.com"
    )


def test_can_override_session_using_deprecated_method():
    client = create_mock_client()
    assert isinstance(client.session._session, httpx.Client)
    client.session._session.headers["Foo"] = "Bar"


def test_accessing_session_emits_warnings():
    client = create_mock_client()
    with warnings.catch_warnings(record=True) as w:
        client.session
        assert len(w) == 1


def test_default_headers():
    """Test that the user agent is set correctly."""
    client = create_mock_client()
    assert client._session.headers == {
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "User-Agent": f"python-foundry-platform-sdk/{__version__} python/3.{sys.version_info.minor}",
    }

    """Test that additional headers can be added."""
    client = create_mock_client(Config(default_headers={"Foo": "Bar"}))
    assert client._session.headers == {
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Foo": "Bar",
        "User-Agent": f"python-foundry-platform-sdk/{__version__} python/3.{sys.version_info.minor}",
    }


def test_authorization_header():
    client = create_mock_client()
    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar"))
    # Ensure the bearer token gets added to the headers
    assert_called_with(client, headers={"Authorization": "Bearer bar"})


def test_proxies():
    client = create_mock_client(
        Config(proxies={"https": "https://foo.bar", "http": "http://foo.bar"})
    )

    transport = assert_http_transport(client._session._mounts[URLPattern("https://")])
    proxy = assert_http_proxy(transport._pool)
    assert url_to_str(proxy._proxy_url) == "https://foo.bar/"

    transport = assert_http_transport(client._session._mounts[URLPattern("http://")])
    proxy = assert_http_proxy(transport._pool)
    assert url_to_str(proxy._proxy_url) == "http://foo.bar/"


def test_timeout():
    client = create_mock_client(config=Config(timeout=60))

    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=None))
    assert_called_with(client, timeout=60)

    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=30))
    assert_called_with(client, timeout=30)


def test_verify():
    client = create_mock_client()
    transport = assert_http_transport(client._session._transport)
    pool = assert_isinstance(transport._pool, httpcore.ConnectionPool)

    assert pool._ssl_context is not None
    assert pool._ssl_context.verify_mode == ssl.VerifyMode.CERT_REQUIRED

    client = create_mock_client(Config(verify=False))
    transport = assert_http_transport(client._session._transport)
    pool = assert_isinstance(transport._pool, httpcore.ConnectionPool)

    assert pool._ssl_context is not None
    assert pool._ssl_context.verify_mode == ssl.VerifyMode.CERT_NONE


def test_default_params():
    client = create_mock_client(Config(default_params={"foo": "bar"}))
    assert client._session.params._dict == {"foo": ["bar"]}


def test_scheme():
    client = create_mock_client()
    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=30))
    assert_called_with(client, url="https://localhost:8123/api/foo/bar")

    client = create_mock_client(Config(scheme="http"))
    client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=30))
    assert_called_with(client, url="http://localhost:8123/api/foo/bar")


def test_path_encoding():
    client = create_mock_client()

    client.call_api(
        RequestInfo.with_defaults(
            "GET",
            "/files/{path}",
            path_params={"path": "/my/file.txt"},
        )
    )

    assert_called_with(client, url="https://localhost:8123/api/files/%2Fmy%2Ffile.txt")


def test_null_query_params():
    client = create_mock_client()
    client.call_api(
        RequestInfo.with_defaults("GET", "/foo/bar", query_params={"foo": "foo", "bar": None})
    )
    assert_called_with(client, url="https://localhost:8123/api/foo/bar", params=[("foo", "foo")])


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
