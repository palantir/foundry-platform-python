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


import functools
import json
import re
import sys
from contextlib import contextmanager
from dataclasses import dataclass
from inspect import isclass
from typing import Any
from typing import Dict
from typing import Generic
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
from typing import cast
from urllib.parse import quote

import httpx
import pydantic
from typing_extensions import deprecated

from foundry._core.auth_utils import Auth
from foundry._core.auth_utils import Token
from foundry._core.binary_stream import BinaryStream
from foundry._core.config import Config
from foundry._core.http_client import HttpClient
from foundry._core.resource_iterator import ResourceIterator
from foundry._errors import ApiNotFoundError
from foundry._errors import BadRequestError
from foundry._errors import ConflictError
from foundry._errors import ConnectionError
from foundry._errors import ConnectTimeout
from foundry._errors import InternalServerError
from foundry._errors import NotFoundError
from foundry._errors import PalantirRPCException
from foundry._errors import PermissionDeniedError
from foundry._errors import ProxyError
from foundry._errors import RateLimitError
from foundry._errors import ReadTimeout
from foundry._errors import RequestEntityTooLargeError
from foundry._errors import SDKInternalError
from foundry._errors import StreamConsumedError
from foundry._errors import UnauthorizedError
from foundry._errors import UnprocessableEntityError
from foundry._errors import WriteTimeout
from foundry._errors import deserialize_error
from foundry._versions import __version__

QueryParameters = Dict[str, Union[Any, List[Any]]]


@functools.cache
def _get_type_adapter(_type: Any) -> pydantic.TypeAdapter:
    """Create a type adapter that can be used to serialize the given data to JSON. For example,
    if the user provided a BaseModel class instance, call the "model_dump_json" method. Otherwise,
    if the user provided a non-BaseModel type (e.g. a TypedDict) create a TypeAdapter from the
    the type and serialize the data to JSON using dump_json().
    """

    if isclass(_type) and issubclass(_type, pydantic.BaseModel):
        # Return a "TypeAdapter" shim for a BaseModel since the API is not the same for dumping
        # to JSON
        return _BaseModelTypeAdapter(_type)  # type: ignore
    else:
        # Create an instance of a type adapter. This has a non-trivial overhead according
        # to the documentation so we do this once the first time we encounter this type
        return pydantic.TypeAdapter(_type)


@dataclass(frozen=True)
class RequestInfo:
    method: str
    resource_path: str
    response_type: Any
    query_params: QueryParameters
    path_params: Dict[str, Any]
    header_params: Dict[str, Any]
    body: Any
    body_type: Any
    request_timeout: Optional[int]
    throwable_errors: Dict[str, Type[PalantirRPCException]]

    # DEPRECATED: Remove the streaming details
    stream: bool = False
    chunk_size: Optional[int] = None

    def update(
        self,
        query_params: Optional[Dict[str, Any]] = None,
        header_params: Optional[Dict[str, Any]] = None,
        stream: Optional[bool] = None,
    ):
        return RequestInfo(
            method=self.method,
            resource_path=self.resource_path,
            response_type=self.response_type,
            query_params={**self.query_params, **(query_params or {})},
            path_params=self.path_params,
            header_params={**self.header_params, **(header_params or {})},
            body=self.body,
            body_type=self.body_type,
            request_timeout=self.request_timeout,
            stream=stream if stream is not None else self.stream,
            throwable_errors=self.throwable_errors,
        )

    @classmethod
    def with_defaults(
        cls,
        method: str,
        resource_path: str,
        response_type: Any = None,
        query_params: QueryParameters = {},
        path_params: Dict[str, Any] = {},
        header_params: Dict[str, Any] = {},
        body: Any = None,
        body_type: Any = None,
        request_timeout: Optional[int] = None,
        stream: bool = False,
        chunk_size: Optional[int] = None,
        throwable_errors: Dict[str, Type[PalantirRPCException]] = {},
    ):
        return cls(
            method=method,
            resource_path=resource_path,
            response_type=response_type,
            query_params=query_params,
            path_params=path_params,
            header_params=header_params,
            body=body,
            body_type=body_type,
            request_timeout=request_timeout,
            stream=stream,
            chunk_size=chunk_size,
            throwable_errors=throwable_errors,
        )


class _BaseModelTypeAdapter:
    def __init__(self, _type: Type[pydantic.BaseModel]) -> None:
        self._type = _type

    def validate_python(self, data: Any):
        return self._type.model_validate(data)

    def dump_json(self, data: Any, **kwargs: Dict[str, Any]):
        # .encode() to match the behaviour of pydantic.TypeAdapter.dump_json which returns bytes.
        return self._type.model_dump_json(data, **kwargs).encode()  # type: ignore


T = TypeVar("T")


class ApiResponse(Generic[T]):
    def __init__(self, request_info: RequestInfo, response: httpx.Response):
        self._response = response
        self._request_info = request_info

    @property
    def status_code(self) -> int:
        return self._response.status_code

    def json(self):
        content_type = self._response.headers.get("content-type")
        if content_type is not None:
            match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
        else:
            match = None

        encoding = match.group(1) if match else "utf-8"
        response_text = self._response.content.decode(encoding)
        return json.loads(response_text)

    def decode(self) -> T:
        if self._request_info.response_type is bytes:
            # DEPRECATED
            if self._request_info.stream:
                return cast(
                    T,
                    BinaryStream(
                        self._response.iter_bytes(chunk_size=self._request_info.chunk_size)
                    ),
                )
            else:
                return cast(T, self._response.content)
        elif self._request_info.response_type is None:
            return cast(T, None)

        data = self.json()

        if self._request_info.response_type is Any:
            return data

        type_adapter = _get_type_adapter(self._request_info.response_type)
        return type_adapter.validate_python(data)

    def close(self):
        """Close the response and release the connection. Automatically called if the response
        body is read to completion.
        """
        self._response.close()


class StreamedApiResponse(Generic[T], ApiResponse[T]):
    def __init__(self, request_info: RequestInfo, response: httpx.Response):
        super().__init__(request_info, response)

    def iter_bytes(self, chunk_size: Optional[int] = None) -> Iterator[bytes]:
        """
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        """
        try:
            for raw_bytes in self._response.iter_bytes(chunk_size=chunk_size):
                yield raw_bytes
        except httpx.StreamConsumed as e:
            raise StreamConsumedError(str(e)) from e


class StreamingContextManager(Generic[T]):
    def __init__(self, request_info: RequestInfo, response: ApiResponse):
        self._request_info = request_info
        self._response = response

    def __enter__(self) -> StreamedApiResponse[T]:
        return StreamedApiResponse[T](self._request_info, self._response._response)

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[Any],
    ) -> None:
        self._response.close()


class ApiClient:
    """
    The API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        if isinstance(auth, str):
            # This is a common error so we have a special error message
            # for these situations
            raise TypeError(
                "auth must be an instance of UserTokenAuth, ConfidentialClientAuth or "
                "PublicClientAuth, not a string. You likely want to use "
                "UserTokenAuth(token=<TOKEN>)."
            )
        elif not isinstance(auth, Auth):
            raise TypeError(
                "auth must be an instance of UserTokenAuth, ConfidentialClientAuth or "
                "PublicClientAuth, not an instance of {type(auth)}."
            )

        if not isinstance(hostname, str):
            raise TypeError(f"hostname must be a string, not {type(hostname)}.")

        if config is not None and not isinstance(config, Config):
            raise TypeError(f"config must be an instance of Config, not {type(config)}.")

        self._auth = auth
        self._session = HttpClient(hostname, config)
        self._auth._parameterize(hostname, config)

    @property
    @deprecated(
        "Accessing the session directly is deprecated. Please configure the session using the new Config class."
    )
    def session(self):
        # DEPRECATED: This ensures that users who were previously accessing the PalantirSession
        # will have code that continues to work (now we just return the ApiClient)
        return self

    def iterate_api(self, request_info: RequestInfo) -> ResourceIterator[Any]:
        def fetch_page(
            page_size: Optional[int],
            next_page_token: Optional[str],
        ) -> Tuple[Optional[str], List[Any]]:
            result = self.call_api(
                request_info.update(
                    # pageSize will already be present in the query params dictionary
                    query_params={"pageToken": next_page_token},
                ),
            ).decode()

            return result.next_page_token, result.data or []

        return ResourceIterator(paged_func=fetch_page)

    def call_api(self, request_info: RequestInfo) -> ApiResponse[Any]:
        """Makes the HTTP request (synchronous)"""
        try:

            def make_request(token: Token):
                request = self._session.build_request(
                    method=request_info.method,
                    url=self._create_url(request_info),
                    params=self._process_query_parameters(request_info.query_params),
                    content=self._serialize(request_info.body, request_info.body_type),
                    headers=self._create_headers(request_info, token),
                    timeout=(
                        httpx.USE_CLIENT_DEFAULT
                        if request_info.request_timeout is None
                        else request_info.request_timeout
                    ),
                )

                return self._session.send(request=request, stream=request_info.stream)

            res = self._auth.execute_with_token(make_request)
        except httpx.ProxyError as e:
            raise ProxyError(str(e)) from e
        except httpx.ConnectTimeout as e:
            raise ConnectTimeout(str(e)) from e
        except httpx.ConnectError as e:
            raise ConnectionError(str(e)) from e
        except httpx.ReadTimeout as e:
            raise ReadTimeout(str(e)) from e
        except httpx.WriteTimeout as e:
            raise WriteTimeout(str(e)) from e

        self._check_for_errors(request_info, res)
        return ApiResponse(request_info, res)

    def stream_api(self, request_info: RequestInfo) -> StreamingContextManager[Any]:
        """Makes the HTTP request (synchronous) and returns a streamed result"""
        return StreamingContextManager(
            request_info, self.call_api(request_info.update(stream=True))
        )

    def _process_query_parameters(self, query_params: QueryParameters):
        result: List[Tuple[str, Any]] = []

        for key, value in query_params.items():
            if value is None:
                continue

            if not isinstance(value, list):
                result.append((key, value))
                continue

            # Explode list query parameters
            for inner_value in value:
                result.append((key, inner_value))

        return result

    def _create_url(self, request_info: RequestInfo) -> str:
        resource_path = request_info.resource_path
        path_params = request_info.path_params

        for k, v in path_params.items():
            # the "safe" option defaults to "/"
            # this does not work with the backend which expects "/" characters to be encoded
            resource_path = resource_path.replace(f"{{{k}}}", quote(v, safe=""))

        return f"/api{resource_path}"

    def _create_headers(self, request_info: RequestInfo, token: Token) -> Dict[str, Any]:
        return {
            "Authorization": "Bearer " + token.access_token,
            # Passing in None leads to this
            # Header value must be str or bytes, not <class 'NoneType'>
            **{
                key: value for key, value in request_info.header_params.items() if value is not None
            },
        }

    def _check_for_errors(self, req: RequestInfo, res: httpx.Response):
        if 200 <= res.status_code <= 299:
            return

        # If the user is streaming back the response, we need to make sure we
        # wait for the entire response to be streamed back before we can access
        # the content. If we don't do this, accessing "text" or calling ".json()"
        # will raise an exception.
        if req.stream:
            res.read()

        if res.status_code == 404 and res.text == "":
            raise ApiNotFoundError(
                f'The reqeust to "{req.resource_path}" returned a 404 status code '
                "with no response body. This likely indicates that the API is not yet "
                "available on your Foundry instance."
            )

        try:
            error_json = res.json()
        except json.JSONDecodeError:
            raise SDKInternalError("Unable to decode JSON error response: " + res.text)

        if error_instance := deserialize_error(error_json, req.throwable_errors):
            raise error_instance
        elif res.status_code == 400:
            raise BadRequestError(error_json)
        elif res.status_code == 401:
            raise UnauthorizedError(error_json)
        elif res.status_code == 403:
            raise PermissionDeniedError(error_json)
        elif res.status_code == 404:
            raise NotFoundError(error_json)
        elif res.status_code == 409:
            raise ConflictError(error_json)
        elif res.status_code == 413:
            raise RequestEntityTooLargeError(error_json)
        elif res.status_code == 422:
            raise UnprocessableEntityError(error_json)
        elif res.status_code == 429:
            raise RateLimitError(error_json)
        elif 500 <= res.status_code <= 599:
            raise InternalServerError(error_json)
        else:
            raise PalantirRPCException(error_json)

    def _serialize(self, value: Any, value_type: Any) -> Optional[bytes]:
        """
        Serialize the data passed in to JSON bytes.
        """
        if value_type is bytes:
            return value
        elif value_type is None:
            return None

        json_bytes: bytes
        if value_type is Any:
            json_bytes = json.dumps(value).encode()
        else:
            type_adapter = _get_type_adapter(value_type)

            # Use "exclude_none" to remove optional inputs that weren't explicitely set
            # Use "by_alias" to use the expected field name rather than the class property name
            json_bytes = type_adapter.dump_json(value, exclude_none=True, by_alias=True)

        return json_bytes
