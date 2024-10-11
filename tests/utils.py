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
from contextlib import contextmanager
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import cast
from unittest.mock import Mock
from unittest.mock import patch
from urllib.parse import quote

import pydantic
import pytest
from typing_extensions import NotRequired
from typing_extensions import TypedDict

import foundry
from foundry.v1 import FoundryClient as FoundryV1Client
from foundry.v2 import FoundryClient as FoundryV2Client


class MockResponse(TypedDict):
    status: int
    content_type: Optional[str]
    json: Optional[Any]


class MockRequest(TypedDict):
    method: Literal["GET", "POST", "DELETE", "PATCH", "PUT"]
    url: str
    path_params: Dict[str, Any]
    response: MockResponse
    json: Optional[Any]


@pytest.fixture
def client_v1():
    yield FoundryV1Client(
        auth=foundry.UserTokenAuth(hostname="example.palantirfoundry.com", token="<TOKEN>"),
        hostname="example.palantirfoundry.com",
    )


@pytest.fixture
def client_v2():
    yield FoundryV2Client(
        auth=foundry.UserTokenAuth(hostname="example.palantirfoundry.com", token="<TOKEN>"),
        hostname="example.palantirfoundry.com",
    )


def serialize_response(response: Any):
    """Serialize the response to primitive data structures (lists, dicts, str, int, etc.)"""
    if response is None:
        return None
    elif isinstance(response, list):
        return [serialize_response(value) for value in response]
    elif isinstance(response, dict):
        return {key: serialize_response(value) for key, value in response.items()}
    elif isinstance(response, pydantic.BaseModel):
        # The to_dict() method will exist on each data model
        return cast(Any, response).to_dict()
    else:
        return response


@contextmanager
def mock_requests(mocks: List[MockRequest]):
    def _mock_request_impl(method: str, url: str, **kwargs):
        if kwargs["data"] is None:
            given_body = None
        else:
            given_body = json.loads(kwargs["data"].decode())

            if isinstance(given_body, dict):
                given_body = {key: value for key, value in given_body.items() if value is not None}

        for expected in mocks:
            expected_url = expected["url"]

            for k, v in expected["path_params"].items():
                expected_url = expected_url.replace(f"{{{k}}}", quote(v, safe=""))

            if (
                method == expected["method"]
                and url == expected_url
                and given_body == expected["json"]
            ):
                # Create a mock response object
                mock_response = Mock()
                mock_response.status_code = expected["response"]["status"]
                mock_response.json.return_value = expected["response"]["json"]
                mock_response.content = (
                    b""
                    if expected["response"]["json"] is None
                    else json.dumps(expected["response"]["json"]).encode()
                )
                mock_response.headers.get = lambda key: {
                    "content-type": expected["response"]["content_type"]
                }.get(key)
                return mock_response

        # If no match is found, return a default 404 response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {}
        return mock_response

    with patch("requests.Session.request", side_effect=_mock_request_impl):
        yield
