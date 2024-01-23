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
import re
from typing import Dict
from unittest.mock import ANY, Mock

import pytest
from foundry import PalantirRPCException
from foundry import UserTokenAuth
from foundry import __version__
from foundry.api_client import ApiClient


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
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


def test_user_agent():
    """Test that the user agent is set correctly."""
    client = ApiClient(auth=UserTokenAuth(hostname="foo", token="bar"), hostname="foo")
    client.session.request = Mock(return_value=AttrDict(status_code=200))

    client.call_api(
        method="POST",
        resource_path="/abc",
        path_params={},
        query_params={},
        header_params={},
        body={},
        post_params={},
        files={},
        collection_formats={},
        response_types_map={},
    )

    client.session.request.assert_called_with(
        ANY,
        ANY,
        headers={"User-Agent": f"foundry-platform-sdk/{__version__}"},
        body=ANY,
        post_params=ANY,
        _request_timeout=ANY,
    )


def call_api_helper(
    status_code: int,
    data: str,
    headers: Dict[str, str],
):
    client = ApiClient(auth=UserTokenAuth(hostname="foo", token="bar"), hostname="foo")

    client.session.request = Mock(
        return_value=AttrDict(
            status_code=status_code,
            headers=headers,
            content=data.encode(),
            text=data,
            json=lambda: json.loads(data),
        )
    )

    return client.call_api(
        method="POST",
        resource_path="/abc",
        path_params={},
        query_params={},
        header_params={},
        body={},
        post_params={},
        files={},
        collection_formats={},
        response_types_map={},
    )


def test_call_api_400():
    with pytest.raises(PalantirRPCException) as info:
        call_api_helper(status_code=400, data=EXAMPLE_ERROR, headers={"Header": "A"})

    assert info.value.name == "ERROR_NAME"
    assert info.value.error_instance_id == "123"
    assert info.value.parameters == {}
    assert (
        str(info.value)
        == f"(400)\nReason: None\nHTTP response headers: Header: A\nHTTP response body: {EXAMPLE_ERROR}\n"
    )


def test_call_api_401():
    with pytest.raises(PalantirRPCException) as info:
        call_api_helper(status_code=401, data=EXAMPLE_ERROR, headers={"Header": "A"})


def test_call_api_403():
    with pytest.raises(PalantirRPCException) as info:
        call_api_helper(status_code=403, data=EXAMPLE_ERROR, headers={"Ha": "Ha"})


def test_call_api_404():
    with pytest.raises(PalantirRPCException) as info:
        call_api_helper(status_code=404, data=EXAMPLE_ERROR, headers={"Ha": "Ha"})


def test_call_api_500():
    with pytest.raises(PalantirRPCException) as info:
        call_api_helper(status_code=500, data=EXAMPLE_ERROR, headers={"Ha": "Ha"})


def test_call_api_333():
    with pytest.raises(PalantirRPCException) as info:
        call_api_helper(status_code=333, data=EXAMPLE_ERROR, headers={"Ha": "Ha"})
