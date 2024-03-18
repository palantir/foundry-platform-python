import json
import sys
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
        query_params={},
        header_params={},
        body={},
        response_types_map={},
    )

    client.session.request.assert_called_with(
        method="POST",
        url="https://foo/api/abc",
        headers={
            "User-Agent": f"python-foundry-platform-sdk/{__version__} python/3.{sys.version_info.minor}"
        },
        json=ANY,
        params=ANY,
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
        method="POST",
        resource_path="/abc",
        query_params={},
        header_params={},
        body={},
        response_types_map={},
    )


def test_call_api_400():
    with pytest.raises(PalantirRPCException) as info:
        call_api_helper(status_code=400, data=EXAMPLE_ERROR, headers={"Header": "A"})

    assert info.value.name == "ERROR_NAME"
    assert info.value.error_instance_id == "123"
    assert info.value.parameters == {}


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
