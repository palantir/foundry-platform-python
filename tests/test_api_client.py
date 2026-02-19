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
from datetime import datetime
from datetime import timezone
from typing import Any
from typing import AsyncIterator
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Union
from typing import cast
from unittest.mock import ANY
from unittest.mock import Mock
from unittest.mock import patch

import httpx
import pytest

from foundry_sdk._core import ApiClient
from foundry_sdk._core import ApiResponse
from foundry_sdk._core import AsyncApiClient
from foundry_sdk._core import ConfidentialClientAuth
from foundry_sdk._core import Config
from foundry_sdk._core import RequestInfo
from foundry_sdk._core import UserTokenAuth
from foundry_sdk._errors import ApiNotFoundError
from foundry_sdk._errors import BadRequestError
from foundry_sdk._errors import ConflictError
from foundry_sdk._errors import ConnectionError
from foundry_sdk._errors import InternalServerError
from foundry_sdk._errors import NotFoundError
from foundry_sdk._errors import PalantirRPCException
from foundry_sdk._errors import PermissionDeniedError
from foundry_sdk._errors import ProxyError
from foundry_sdk._errors import RateLimitError
from foundry_sdk._errors import ReadTimeout
from foundry_sdk._errors import RequestEntityTooLargeError
from foundry_sdk._errors import ServiceUnavailable
from foundry_sdk._errors import StreamConsumedError
from foundry_sdk._errors import UnauthorizedError
from foundry_sdk._errors import UnprocessableEntityError
from foundry_sdk._errors import WriteTimeout
from tests.server import FooBar
from tests.server import FooData

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

EMPTY_BODY = ""


def assert_called_with(client: Union[ApiClient, AsyncApiClient], **kwargs):
    if isinstance(client, AsyncApiClient):
        build_request = cast(Mock, client._client.build_request)
    else:
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


def get_mock_awaitable(return_value):
    async def mock_awaitable(*args, **kwargs):
        return return_value

    return Mock(wraps=mock_awaitable)


def create_mock_client(config: Optional[Config] = None, hostname=HOSTNAME):
    client = ApiClient(auth=UserTokenAuth(token="bar"), hostname=hostname, config=config)
    client._session.build_request = Mock(wraps=client._session.build_request)  # type: ignore
    client._session.send = Mock(return_value=AttrDict(status_code=200, content=b"", headers={}))  # type: ignore
    return client


def create_async_mock_client(config: Optional[Config] = None, hostname=HOSTNAME):
    client = AsyncApiClient(auth=UserTokenAuth(token="bar"), hostname=hostname, config=config)
    client._client.build_request = Mock(wraps=client._client.build_request)  # type: ignore
    client._client.send = get_mock_awaitable(AttrDict(status_code=200, content=b"", headers={}))  # type: ignore
    return client


def create_client(
    config: Optional[Config] = None,
    hostname=HOSTNAME,
    scheme: Literal["https", "http"] = "http",
):
    config = config or Config()
    config.scheme = scheme
    return ApiClient(auth=UserTokenAuth(token="bar"), hostname=hostname, config=config)


def create_async_client(
    config: Optional[Config] = None,
    hostname=HOSTNAME,
    scheme: Literal["https", "http"] = "http",
):
    config = config or Config()
    config.scheme = scheme
    return AsyncApiClient(auth=UserTokenAuth(token="bar"), hostname=hostname, config=config)


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

    client._session.send = Mock(  # type: ignore
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


def test_404_with_no_body():
    with pytest.raises(ApiNotFoundError):
        call_api_helper(status_code=404, data=EMPTY_BODY)


def test_422_error():
    with pytest.raises(UnprocessableEntityError):
        call_api_helper(status_code=422, data=EXAMPLE_ERROR)


def test_429_error():
    with pytest.raises(RateLimitError):
        call_api_helper(status_code=429, data=EMPTY_BODY)


def test_503_with_propagate_to_caller():
    client = ApiClient(
        auth=UserTokenAuth(token="bar"),
        hostname="foo",
        config=Config(propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
    )

    client._session.send = Mock(
        side_effect=(
            AttrDict(status_code=503, headers={}, content=b"", text=""),
            AttrDict(status_code=200, headers={}, content=b"", text=""),
        )
    )

    with pytest.raises(ServiceUnavailable):
        client.call_api(RequestInfo.with_defaults("POST", "/abc"))

    assert client._session.send.call_count == 1


def test_503_with_retry():
    client = ApiClient(
        auth=UserTokenAuth(token="bar"),
        hostname="foo",
        config=Config(propagate_qos="AUTOMATIC_RETRY"),
    )

    client._session.send = Mock(
        side_effect=(
            AttrDict(status_code=503, headers={}, content=b"", text=""),
            AttrDict(status_code=200, headers={}, content=b"", text=""),
        )
    )

    response = client.call_api(RequestInfo.with_defaults("POST", "/abc", response_mode="RAW"))
    assert response.status_code == 200

    assert client._session.send.call_count == 2


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
    request_info = RequestInfo.with_defaults("GET", "/foo/timeout", body=data)

    with pytest.raises(WriteTimeout):
        client.call_api(request_info)


def test_stream_consumed_error():
    client = create_client()
    request_info = RequestInfo.with_defaults("GET", "/foo/stream", response_mode="STREAMING")

    with client.call_api(request_info) as response:
        for _ in response.iter_bytes():
            pass

        with pytest.raises(StreamConsumedError):
            for _ in response.iter_bytes():
                pass


def test_streaming_response_type():
    client = create_client()
    request_info = RequestInfo.with_defaults("GET", "/foo/stream", response_mode="STREAMING")

    with client.call_api(request_info) as response:
        iterator = response.iter_bytes()
        assert next(iterator) == b"foo\n"
        assert next(iterator) == b"bar\n"
        assert next(iterator) == b"baz"


def test_raw_response_type():
    client = create_client()
    request_info = RequestInfo.with_defaults("GET", "/foo/bar", response_mode="RAW")

    response = client.call_api(request_info)
    assert response.text == '{"foo":"foo","bar":2}'
    assert response.json() == {"foo": "foo", "bar": 2}


def test_iterator_response_type():
    client = create_client()
    request_info = RequestInfo.with_defaults(
        "GET",
        "/foo/iterator",
        response_mode="ITERATOR",
        response_type=FooData,
    )

    response = client.call_api(request_info)
    assert len(response.data) == 2
    assert len(list(response)) == 2


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

    with pytest.raises(TypeError) as e:
        AsyncApiClient(auth="foo", hostname="localhost:8123")  # type: ignore
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

    with pytest.raises(TypeError) as e:
        AsyncApiClient(auth=2, hostname="localhost:8123")  # type: ignore
    assert (
        str(e.value)
        == "auth must be an instance of UserTokenAuth, ConfidentialClientAuth or PublicClientAuth, not an instance of int."
    )


def test_passing_in_int_to_hostname():
    with pytest.raises(TypeError) as e:
        ApiClient(auth=UserTokenAuth(token="foo"), hostname=2)  # type: ignore
    assert str(e.value) == "The hostname must be a string, not <class 'int'>."

    with pytest.raises(TypeError) as e:
        AsyncApiClient(auth=UserTokenAuth(token="foo"), hostname=2)  # type: ignore
    assert str(e.value) == "The hostname must be a string, not <class 'int'>."


def test_passing_in_int_to_config():
    with pytest.raises(TypeError) as e:
        ApiClient(auth=UserTokenAuth(token="foo"), hostname="localhost:1234", config=2)  # type: ignore
    assert str(e.value) == "config must be an instance of Config, not <class 'int'>."

    with pytest.raises(TypeError) as e:
        AsyncApiClient(auth=UserTokenAuth(token="foo"), hostname="localhost:1234", config=2)  # type: ignore
    assert str(e.value) == "config must be an instance of Config, not <class 'int'>."


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


def test_auth_config_prioritized():
    auth_config = Config(timeout=1)
    auth = ConfidentialClientAuth(
        client_id="foo", client_secret="bar", hostname="localhost:9876", config=auth_config
    )

    with warnings.catch_warnings(record=True) as w:
        ApiClient(auth=auth, hostname="localhost:1234", config=Config(timeout=2))
        # No warning because the hostnames are different
        assert len(w) == 0

    # Make sure the ApiClient hostname is prioritized
    assert auth._hostname == "localhost:9876"
    assert auth._config == auth_config


def test_duplicate_auth_config_warns():
    hostname = "localhost:1234"
    config = Config(timeout=1)
    auth = ConfidentialClientAuth(
        client_id="foo", client_secret="bar", hostname=hostname, config=config
    )

    with warnings.catch_warnings(record=True) as w:
        ApiClient(auth=auth, hostname=hostname, config=config)
        # Two warnings because both the hostname and config are the same
        assert len(w) == 2

    # Make sure the ApiClient hostname is prioritized
    assert auth._hostname == hostname
    assert auth._config == config


def test_create_headers():
    client = create_client()
    expected_headers = {
        "Authorization": "Bearer bar",
        "bool_header": "true",
        "bytes_header": "bytes".encode("utf-8"),
        "datetime_header": "2025-01-01T10:00:00+00:00",
        "float_header": "123.123",
        "int_header": "123",
        "str_header": "string",
    }
    assert expected_headers == client._create_headers(
        request_info=RequestInfo.with_defaults(
            "GET",
            "/files/{path}",
            header_params={
                "bool_header": True,
                "bytes_header": "bytes".encode("utf-8"),
                "datetime_header": datetime(2025, 1, 1, 10, 0, 0, tzinfo=timezone.utc),
                "float_header": 123.123,
                "int_header": 123,
                "str_header": "string",
                "optional_header": None,
            },
        ),
        token=UserTokenAuth(token="bar").get_token(),
    )


def test_response_decode_bytes():
    response = ApiResponse(
        RequestInfo.with_defaults("GET", "/foo/bar", response_type=bytes),
        httpx.Response(200, content=b"foo"),
    )

    assert response.decode() == b"foo"


def test_response_decode_present_optional_bytes():
    response = ApiResponse(
        RequestInfo.with_defaults("GET", "/foo/bar", response_type=Optional[bytes]),
        httpx.Response(200, content=b"foo"),
    )

    assert response.decode() == b"foo"


def test_response_decode_empty_optional_bytes():
    response = ApiResponse(
        RequestInfo.with_defaults("GET", "/foo/bar", response_type=Optional[bytes]),
        httpx.Response(200, content=b""),
    )

    assert response.decode() is None


@pytest.mark.asyncio(scope="session")
async def test_async_headers():
    client = create_async_mock_client()
    await client.call_api(RequestInfo.with_defaults("GET", "/foo", header_params={"Foo": "Bar"}))
    assert_called_with(client, headers={"Authorization": "Bearer bar", "Foo": "Bar"})


@pytest.mark.asyncio(scope="session")
async def test_async_timeout():
    client = create_async_mock_client(config=Config(timeout=60))
    await client.call_api(RequestInfo.with_defaults("GET", "/foo/bar", request_timeout=30))
    assert_called_with(client, timeout=30)


@pytest.mark.asyncio(scope="session")
async def test_async_path():
    client = create_async_mock_client()
    await client.call_api(RequestInfo.with_defaults("GET", "/files"))
    assert_called_with(client, url="/api/files")


@pytest.mark.asyncio(scope="session")
async def test_async_query_params():
    client = create_async_mock_client()
    await client.call_api(RequestInfo.with_defaults("GET", "/foo", query_params={"foo": "bar"}))
    assert_called_with(client, url="/api/foo", params=[("foo", "bar")])


@pytest.mark.asyncio(scope="session")
async def test_async_default_raw_response_type():
    client = create_async_client()
    request_info = RequestInfo.with_defaults(
        "GET", "/foo/bar", response_mode="DECODED", response_type=FooBar
    )

    response = await client.call_api(request_info)
    assert response == FooBar(foo="foo", bar=2)


@pytest.mark.asyncio(scope="session")
async def test_async_streaming_response_type():
    client = create_async_client()
    request_info = RequestInfo.with_defaults("GET", "/foo/stream", response_mode="STREAMING")

    async with client.call_api(request_info) as response:
        iterator = response.aiter_bytes()
        assert await iterator.__anext__() == b"foo\n"
        assert await iterator.__anext__() == b"bar\n"
        assert await iterator.__anext__() == b"baz"


@pytest.mark.asyncio(scope="session")
async def test_async_raw_response_type():
    client = create_async_client()
    request_info = RequestInfo.with_defaults("GET", "/foo/bar", response_mode="RAW")

    response = await client.call_api(request_info)
    assert response.text == '{"foo":"foo","bar":2}'
    assert response.json() == {"foo": "foo", "bar": 2}


async def collect_async_iterator(aiterator: AsyncIterator[Any]) -> List[Any]:
    """Collects the items from an async iterator into a list."""
    result = []
    async for item in aiterator:
        result.append(item)
    return result


@pytest.mark.asyncio(scope="session")
async def test_async_iterator_response_type():
    client = create_async_client()
    request_info = RequestInfo.with_defaults(
        "GET",
        "/foo/iterator",
        response_mode="ITERATOR",
        response_type=FooData,
    )

    response = client.call_api(request_info)
    assert len(await response._page_iterator.get_data()) == 2
    assert len(await collect_async_iterator(response)) == 2
