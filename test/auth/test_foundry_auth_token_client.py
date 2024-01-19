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

import os
import pytest
from foundry import UserTokenAuth


@pytest.fixture
def temp_os_environ():
    old_environ = os.environ.copy()

    # Make sure to start with a clean slate
    for key in ["FOUNDRY_HOSTNAME", "FOUNDRY_TOKEN"]:
        if key in os.environ:
            os.environ.pop(key)

    yield
    os.environ = old_environ


def test_load_from_env(temp_os_environ):
    os.environ["FOUNDRY_HOSTNAME"] = "host_test"
    os.environ["FOUNDRY_TOKEN"] = "token_test"
    config = UserTokenAuth()
    assert config.hostname == "host_test"
    assert config.token == "token_test"


def test_load_from_env_missing_token(temp_os_environ):
    os.environ["FOUNDRY_HOSTNAME"] = "host_test"
    assert pytest.raises(ValueError, lambda: UserTokenAuth())


def test_load_from_env_missing_host(temp_os_environ):
    os.environ["FOUNDRY_TOKEN"] = "token_test"
    assert pytest.raises(ValueError, lambda: UserTokenAuth())


def test_can_pass_config():
    os.environ["FOUNDRY_HOSTNAME"] = "host_test"
    os.environ["FOUNDRY_TOKEN"] = "token_test"
    config = UserTokenAuth(hostname="host_test2", token="token_test2")
    assert config.hostname == "host_test2"
    assert config.token == "token_test2"


def test_can_pass_config_missing_token():
    assert pytest.raises(ValueError, lambda: UserTokenAuth(hostname="test"))


def test_can_pass_config_missing_host():
    assert pytest.raises(ValueError, lambda: UserTokenAuth(token="test"))


def test_checks_host_type():
    assert pytest.raises(ValueError, lambda: UserTokenAuth(hostname=1))  # type: ignore


def test_checks_token_type():
    assert pytest.raises(ValueError, lambda: UserTokenAuth(token=1))  # type: ignore
