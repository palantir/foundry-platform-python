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
from unittest.mock import ANY, Mock

import pytest
from foundry.api_client import ApiClient
from foundry.configuration import Configuration
from foundry.exceptions import BadRequestException
from foundry.exceptions import UnauthorizedException
from foundry.exceptions import ForbiddenException
from foundry.exceptions import NotFoundException
from foundry.exceptions import ServiceException
from foundry.exceptions import SDKInternalError
from foundry.rest import RESTResponse
from foundry import UserTokenAuth
from foundry import __version__


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
    client = ApiClient(configuration=Configuration(UserTokenAuth(hostname="foo", token="bar")))
    client.rest_client.request = Mock()

    client.call_api(
        method="POST",
        resource_path="/abc",
        path_params={},
        query_params={},
        header_params={},
        body={},
        post_params={},
        files={},
        auth_settings={},
        collection_formats={},
    )

    client.rest_client.request.assert_called_with(
        ANY,
        ANY,
        headers={"User-Agent": f"foundry-platform-sdk/{__version__}"},
        body=ANY,
        post_params=ANY,
        _request_timeout=ANY,
    )


def response_deserialize(
    status_code: int,
    data: str,
    headers: str,
):
    client = ApiClient(configuration=Configuration(UserTokenAuth(hostname="foo", token="bar")))
    res = RESTResponse(
        AttrDict(status=status_code, reason=None, data=data.encode(), headers=headers)  # type: ignore
    )
    res.read()
    client.response_deserialize(
        res,
        {},
    )


def test_response_deserialize_400():
    with pytest.raises(BadRequestException) as info:
        response_deserialize(status_code=400, data=EXAMPLE_ERROR, headers="Header: A")

    assert info.value.status == 400
    assert info.value.body == EXAMPLE_ERROR
    assert info.value.error_code == "ERROR_CODE"
    assert info.value.error_name == "ERROR_NAME"
    assert info.value.error_instance_id == "123"
    assert info.value.parameters == {}
    assert (
        str(info.value)
        == f"(400)\nReason: None\nHTTP response headers: Header: A\nHTTP response body: {EXAMPLE_ERROR}\n"
    )


def test_response_deserialize_401():
    with pytest.raises(UnauthorizedException) as info:
        response_deserialize(status_code=401, data=EXAMPLE_ERROR, headers="Header: A")

    assert info.value.status == 401
    assert (
        str(info.value)
        == f"(401)\nReason: None\nHTTP response headers: Header: A\nHTTP response body: {EXAMPLE_ERROR}\n"
    )


def test_response_deserialize_403():
    with pytest.raises(ForbiddenException) as info:
        response_deserialize(status_code=403, data=EXAMPLE_ERROR, headers="Ha: Ha")


def test_response_deserialize_404():
    with pytest.raises(NotFoundException) as info:
        response_deserialize(status_code=404, data=EXAMPLE_ERROR, headers="Ha: Ha")


def test_response_deserialize_500():
    with pytest.raises(ServiceException) as info:
        response_deserialize(status_code=500, data=EXAMPLE_ERROR, headers="Ha: Ha")


def test_response_deserialize_333():
    with pytest.raises(SDKInternalError) as info:
        response_deserialize(status_code=333, data=EXAMPLE_ERROR, headers="Ha: Ha")
