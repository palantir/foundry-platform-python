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


from __future__ import annotations

import json
from dataclasses import dataclass
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Generic,
    Iterator,
    Optional,
    Type,
    TypeVar,
)

import httpx
import pydantic
from httpx_sse import EventSource, ServerSentEvent, SSEError

from foundry_sdk._core.api_client import (
    ApiResponse,
    AsyncApiResponse,
    RequestInfo,
    _decode_value,
)
from foundry_sdk._errors import (
    SseContentTypeError,
    SseEventDecodeError,
    StreamConsumedError,
)

T = TypeVar("T")


@dataclass
class SseEvent(Generic[T]):
    """A single parsed Server-Sent Event.

    ``data`` is the deserialized event payload (decoded into the operation's event type). The
    ``event``, ``id`` and ``retry`` fields carry the raw SSE framing for callers that need it.
    """

    data: T
    event: str
    id: str
    retry: Optional[int]


def _decode_sse_event(request_info: RequestInfo, sse: ServerSentEvent) -> "SseEvent[Any]":
    """Decode a raw ``ServerSentEvent`` into a typed ``SseEvent`` using the operation's event type.

    :raises SseEventDecodeError: if the event data is not valid JSON or does not match the event type.
    """
    try:
        data = _decode_value(request_info.response_type, json.loads(sse.data))
    except (json.JSONDecodeError, pydantic.ValidationError) as e:
        raise SseEventDecodeError(f"Failed to decode SSE event data: {e}") from e
    return SseEvent(
        data=data,
        event=sse.event,
        id=sse.id,
        retry=sse.retry,
    )


class SseApiResponse(Generic[T], ApiResponse[T]):
    def __init__(self, request_info: RequestInfo, response: httpx.Response):
        super().__init__(request_info, response)

    def iter_sse(self) -> Iterator[SseEvent[T]]:
        """Yield typed events from the stream as they arrive.

        :raises SseContentTypeError: if the response is not a ``text/event-stream``.
        """
        source = EventSource(self._response)
        try:
            for sse in source.iter_sse():
                if not sse.data:
                    # Empty-data dispatches (a lone ``id:`` or an ``event:``-only terminator) carry no
                    # JSON payload to decode, so skip them rather than feeding "" to ``json.loads``.
                    continue
                yield _decode_sse_event(self._request_info, sse)
        except SSEError as e:
            raise SseContentTypeError(str(e)) from e
        except httpx.StreamConsumed as e:
            raise StreamConsumedError(str(e)) from e

    def __iter__(self) -> Iterator[SseEvent[T]]:
        return self.iter_sse()


class AsyncSseApiResponse(Generic[T], AsyncApiResponse[T]):
    def __init__(self, request_info: RequestInfo, response: httpx.Response):
        super().__init__(request_info, response)

    async def aiter_sse(self) -> AsyncIterator[SseEvent[T]]:
        """Yield typed events from the stream as they arrive.

        :raises SseContentTypeError: if the response is not a ``text/event-stream``.
        """
        source = EventSource(self._response)
        try:
            async for sse in source.aiter_sse():
                if not sse.data:
                    # Empty-data dispatches (a lone ``id:`` or an ``event:``-only terminator) carry no
                    # JSON payload to decode, so skip them rather than feeding "" to ``json.loads``.
                    continue
                yield _decode_sse_event(self._request_info, sse)
        except SSEError as e:
            raise SseContentTypeError(str(e)) from e
        except httpx.StreamConsumed as e:
            raise StreamConsumedError(str(e)) from e

    def __aiter__(self) -> AsyncIterator[SseEvent[T]]:
        return self.aiter_sse()


class SseContextManager(Generic[T]):
    def __init__(self, request_info: RequestInfo, response: ApiResponse):
        self._request_info = request_info
        self._response = response

    def __enter__(self) -> SseApiResponse[T]:
        return SseApiResponse[T](self._request_info, self._response._response)

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[Any],
    ) -> None:
        self._response.close()


class AsyncSseContextManager(Generic[T]):
    def __init__(self, request_info: RequestInfo, response: Awaitable[AsyncApiResponse]):
        self._request_info = request_info
        self._awaitable_response = response
        self._response: Optional[AsyncApiResponse] = None

    async def __aenter__(self) -> AsyncSseApiResponse[T]:
        self._response = await self._awaitable_response
        return AsyncSseApiResponse[T](self._request_info, self._response._response)

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[Any],
    ) -> None:
        if self._response is not None:
            await self._response.aclose()
