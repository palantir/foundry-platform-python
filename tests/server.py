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
from fastapi import Request
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


@app.api_route("/proxy/error", methods=["CONNECT"])
def proxy_error(full_path: str):
    raise HTTPException(status_code=400, detail="Bad Request")


app.include_router(router, prefix="/api")
