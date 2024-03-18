import json as jsn
from typing import Any, Dict, List, Optional, Tuple, TypedDict
from unittest.mock import Mock

import pytest
from requests import Session

from foundry import FoundryClient
from foundry import UserTokenAuth


@pytest.fixture()
def client():
    yield FoundryClient(auth=UserTokenAuth(hostname="test.com", token="test"), hostname="test.com")


class MockRequest(TypedDict):
    method: str
    url: str
    params: Optional[Dict[str, Any]]
    json: Optional[Any]


class MockResponse(TypedDict):
    status: int
    content: Optional[bytes]
    json: Optional[Any]


def mock_responses(monkeypatch, request_responses: List[Tuple[MockRequest, MockResponse]]):
    # Define a side_effect function for our mock. This will be called instead of the original method
    def mock_request(_, method, url, json=None, **kwargs):
        for request, response in request_responses:
            if request["method"] != method:
                continue

            if request["url"] != url:
                continue

            if json is not None and json != request["json"]:
                continue

            # Mock response
            mock_response = Mock()
            mock_response.status_code = response["status"]

            if response["json"]:
                mock_response.content = jsn.dumps(response["json"]).encode()
            elif response["content"]:
                mock_response.content = response["content"]
            else:
                mock_response.content = None

            mock_response.headers = {}

            return mock_response

        pytest.fail(f"Unexpected request: {method} {url} {json}")

    # Use monkeypatch to replace the PoolManager.request method with our side_effect function
    monkeypatch.setattr(Session, "request", mock_request)
