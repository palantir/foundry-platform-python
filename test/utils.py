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
from unittest.mock import Mock
import pytest
from urllib3 import PoolManager
from foundry import FoundryClient
from foundry import UserTokenAuth


@pytest.fixture
def client():
    yield FoundryClient(auth=UserTokenAuth(hostname="test.com", token="test"))


def mock_responses(monkeypatch, request_responses: list):
    # Define a side_effect function for our mock. This will be called instead of the original method
    def mock_request(_, method, url, body=None, **kwargs):
        for request, response in request_responses:
            if request["method"] != method:
                continue

            if request["url"] != url:
                continue

            if body is not None and request["body"] != json.loads(body):
                continue

            # Mock response
            mock_response = Mock()
            mock_response.status = response["status"]

            if "body" in response:
                mock_response.data = json.dumps(response["body"]).encode()
            elif "data" in response:
                mock_response.data = response["data"]
            else:
                mock_response.data = None

            mock_response.headers = {}

            return mock_response

        pytest.fail(f"Unexpected request: {method} {url} {body}")

    # Use monkeypatch to replace the PoolManager.request method with our side_effect function
    monkeypatch.setattr(PoolManager, "request", mock_request)
