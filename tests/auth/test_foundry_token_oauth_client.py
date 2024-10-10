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
from foundry._errors.not_authenticated import NotAuthenticated


def test_can_pass_config():
    config = ConfidentialClientAuth(
        client_id="123",
        client_secret="abc",
        hostname="example.com",
        scopes=["hello"],
    )

    assert config._hostname == "example.com"  # type: ignore
    assert config._client_id == "123"  # type: ignore
    assert config._client_secret == "abc"  # type: ignore

    with pytest.raises(NotAuthenticated) as info:
        config.get_token()

    assert str(info.value) == "Client has not been authenticated."
