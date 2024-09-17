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
from typing import Any
from typing import Dict
from unittest.mock import ANY
from unittest.mock import Mock

import pytest

from foundry import PalantirRPCException
from foundry import UserTokenAuth
from foundry import __version__
from foundry._core import ApiClient
from foundry._core import RequestInfo


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


def test_user_agent():
    """Test that the user agent is set correctly."""
    client = ApiClient(auth=UserTokenAuth(hostname="foo", token="bar"), hostname="foo")
    client.session.request = Mock(return_value=AttrDict(status_code=200, headers={}))

    client.call_api(
        RequestInfo(
            method="POST",
            resource_path="/abc",
            query_params={},
            header_params={},
            path_params={},
            body={},
            body_type=Any,
            response_type=None,
            request_timeout=None,
        )
    )

    client.session.request.assert_called_with(
        method="POST",
        url="https://foo/api/abc",
        headers={
            "User-Agent": f"python-foundry-platform-sdk/{__version__} python/3.{sys.version_info.minor}"
        },
        params=ANY,
        data=ANY,
        stream=False,
        timeout=None,
    )


def test_path_encoding():
    """Test that the user agent is set correctly."""
    client = ApiClient(auth=UserTokenAuth(hostname="foo", token="bar"), hostname="foo")
    client.session.request = Mock(return_value=AttrDict(status_code=200, headers={}))

    client.call_api(
        RequestInfo(
            method="GET",
            resource_path="/files/{path}",
            query_params={},
            header_params={},
            path_params={"path": "/my/file.txt"},
            body={},
            body_type=Any,
            response_type=None,
            request_timeout=None,
        )
    )

    client.session.request.assert_called_with(
        method="GET",
        url="https://foo/api/files/%2Fmy%2Ffile.txt",
        headers=ANY,
        params=ANY,
        data=ANY,
        stream=False,
        timeout=None,
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


def test_call_api_401():
    with pytest.raises(PalantirRPCException):
        call_api_helper(status_code=401, data=EXAMPLE_ERROR, headers={"Header": "A"})


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
