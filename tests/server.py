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
from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from pydantic import Field

app = FastAPI()
router = APIRouter()


class FooBar(BaseModel):
    foo: str
    bar: int


@router.get("/foo/bar", response_model=FooBar)
def foo_bar() -> FooBar:
    return FooBar(foo="foo", bar=2)


class FooData(BaseModel):
    data: List[FooBar]
    next_page_token: Optional[str] = Field(alias="nextPageToken", default=None)


@router.get("/foo/iterator", response_model=FooData)
def foo_iterator() -> FooData:
    return FooData(
        data=[
            FooBar(foo="foo", bar=1),
            FooBar(foo="foo", bar=2),
        ],
        nextPageToken=None,
    )


@router.get("/foo/timeout", response_model=FooBar)
def timeout() -> FooBar:
    time.sleep(10)
    return FooBar(foo="foo", bar=2)


@router.get("/foo/stream")
def stream() -> StreamingResponse:
    content = "foo\nbar\nbaz"

    def generate_data():
        lines = content.split("\n")
        for i, line in enumerate(lines):
            is_final_line = i == len(lines) - 1
            yield line if is_final_line else line + "\n"

    return StreamingResponse(generate_data(), media_type="text/plain")


@router.get("/foo/sse")
def foo_sse() -> StreamingResponse:
    # A stream of Server-Sent Events whose ``data`` payloads are FooBar JSON objects. Exercises:
    # a plain event, a comment/keep-alive line (ignored), and a multi-line ``data:`` event that
    # the SSE decoder joins with newlines before JSON parsing.
    def generate_data():
        yield 'data: {"foo": "a", "bar": 1}\n\n'
        yield ": keep-alive\n\n"
        yield 'data: {"foo": "b", "bar": 2}\n\n'
        yield 'data: {"foo": "c",\ndata: "bar": 3}\n\n'

    return StreamingResponse(generate_data(), media_type="text/event-stream")


@router.get("/foo/sse-keepalive")
def foo_sse_keepalive() -> StreamingResponse:
    # Once an event sets ``id:``, the SSE decoder dispatches an empty-data event on every following
    # blank line (it never resets last_event_id), and an ``event:``-only terminator does the same.
    # Those carry no payload and must be skipped, not decoded.
    def generate_data():
        yield 'id: 1\ndata: {"foo": "a", "bar": 1}\n\n'
        yield ": keep-alive\n\n"
        yield 'data: {"foo": "b", "bar": 2}\n\n'
        yield "event: done\n\n"

    return StreamingResponse(generate_data(), media_type="text/event-stream")


@router.get("/foo/sse-bad-json")
def foo_sse_bad_json() -> StreamingResponse:
    # Event data that is not valid JSON.
    return StreamingResponse(iter(["data: {not json}\n\n"]), media_type="text/event-stream")


@router.get("/foo/sse-bad-shape")
def foo_sse_bad_shape() -> StreamingResponse:
    # Valid JSON whose shape does not match the event type (FooBar requires an int ``bar``).
    return StreamingResponse(iter(['data: {"foo": "x"}\n\n']), media_type="text/event-stream")


@router.get("/foo/sse-error")
def foo_sse_error():
    # A non-2xx response to an SSE-mode request: the client must fully read the body and raise a
    # typed error rather than hand back a broken stream.
    raise HTTPException(status_code=404, detail="not found")


@app.api_route("/proxy/error", methods=["CONNECT"])
def proxy_error(full_path: str):
    raise HTTPException(status_code=400, detail="Bad Request")


app.include_router(router, prefix="/api")
