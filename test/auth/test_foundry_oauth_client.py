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

import pytest
from foundry import ConfidentialClientAuth
from foundry.exceptions import OpenApiException


def test_fails_no_escopes():
    with pytest.raises(ValueError) as info:
        ConfidentialClientAuth(
            client_id="123",
            client_secret="abc",
            hostname="hey.com",
            scopes=[],
        )

    assert (
        str(info.value) == "You have not provided any scopes. At least one scope must be provided."
    )


def test_can_pass_config():
    config = ConfidentialClientAuth(
        client_id="123",
        client_secret="abc",
        hostname="hey.com",
        scopes=["hello"],
    )

    assert config.hostname == "hey.com"
    assert config._client_id == "123"
    assert config._client_secret == "abc"

    with pytest.raises(OpenApiException) as info:
        config.get_token()

    assert (
        str(info.value)
        == "ConfidentialClientAuth has not been authenticated. Please call sign_in_as_service_user() first."
    )
