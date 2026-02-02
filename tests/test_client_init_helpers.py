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
from contextvars import ContextVar
from typing import Optional
from unittest.mock import patch

from expects import equal
from expects import expect
from expects import raise_error

from foundry_sdk._core.client_init_helpers import (
    get_hostname_from_context_or_environment_vars,
)  # NOQA
from foundry_sdk._core.client_init_helpers import (
    get_user_token_auth_from_context_or_environment_vars,
)  # NOQA
from foundry_sdk._core.context_and_environment_vars import HOSTNAME_ENV_VAR
from foundry_sdk._core.context_and_environment_vars import HOSTNAME_VAR
from foundry_sdk._core.context_and_environment_vars import TOKEN_ENV_VAR
from foundry_sdk._core.context_and_environment_vars import TOKEN_VAR
from foundry_sdk._core.context_and_environment_vars import _maybe_get_environment_var
from foundry_sdk._core.context_and_environment_vars import maybe_get_context_var
from foundry_sdk._core.context_and_environment_vars import (
    maybe_get_value_from_context_or_environment_vars,
)  # NOQA
from foundry_sdk._errors.environment_not_configured import EnvironmentNotConfigured

CONTEXT_VAR1: ContextVar[Optional[str]] = ContextVar("CONTEXT VAR1", default=None)
CONTEXT_VAR2: ContextVar[Optional[str]] = ContextVar("CONTEXT VAR2", default=None)


def test_maybe_get_context_var():
    example_context_vars = [CONTEXT_VAR1, CONTEXT_VAR2]

    CONTEXT_VAR2.set("context_var 2")
    expect(maybe_get_context_var(context_vars=example_context_vars)).to(equal("context_var 2"))
    CONTEXT_VAR2.set(None)

    CONTEXT_VAR1.set("context_var 1")
    CONTEXT_VAR2.set("context_var 2")
    expect(maybe_get_context_var(context_vars=example_context_vars)).to(equal("context_var 1"))
    CONTEXT_VAR1.set(None)
    CONTEXT_VAR2.set(None)


def test_maybe_get_environment_var():
    example_env_vars = ["ENV VAR1", "ENV VAR2", "ENV VAR3"]

    with patch.dict(os.environ, {"ENV VAR3": "environment_var 3"}):
        expect(_maybe_get_environment_var(env_vars=example_env_vars)).to(equal("environment_var 3"))
    with patch.dict(os.environ, {"ENV VAR1": "environment_var 1", "ENV VAR3": "environment_var 3"}):
        expect(_maybe_get_environment_var(env_vars=example_env_vars)).to(equal("environment_var 1"))


def test_get_value_from_context_or_env():
    # Test case 1: Context variable is set
    CONTEXT_VAR1.set("context_var")
    expect(
        maybe_get_value_from_context_or_environment_vars(
            context_vars=[CONTEXT_VAR1], env_vars=["ENV_VAR_NAME"]
        )
    ).to(equal("context_var"))
    CONTEXT_VAR1.set(None)

    # Test case 2: Context variable is not set and FOUNDRY_HOSTNAME environment variable is set
    with patch.dict(os.environ, {"ENV_VAR_NAME": "environment_var"}):
        expect(
            maybe_get_value_from_context_or_environment_vars(
                context_vars=[CONTEXT_VAR1], env_vars=["ENV_VAR_NAME"]
            )
        ).to(equal("environment_var"))

    # Test case 3: Both Context variable and environment variable are not set
    expect(
        maybe_get_value_from_context_or_environment_vars(
            context_vars=[CONTEXT_VAR1], env_vars=["ENV_VAR_NAME"]
        )
    ).to(equal(None))

    # Test case 4: Test context vars are used before env vars
    CONTEXT_VAR1.set("context_var")
    with patch.dict(os.environ, {"ENV_VAR_NAME": "environment_var"}):
        expect(
            maybe_get_value_from_context_or_environment_vars(
                context_vars=[CONTEXT_VAR1], env_vars=["ENV_VAR_NAME"]
            )
        ).to(equal("context_var"))
    CONTEXT_VAR1.set(None)


def test_get_hostname_from_context_or_environment_vars():
    # Test case 1: Context variable is set
    HOSTNAME_VAR.set("hostname_context_var")
    expect(get_hostname_from_context_or_environment_vars()).to(equal("hostname_context_var"))
    HOSTNAME_VAR.set(None)

    # Test case 2: Context variable is not set and environment variable is set
    with patch.dict(os.environ, {HOSTNAME_ENV_VAR: "hostname_environment_var"}):
        expect(get_hostname_from_context_or_environment_vars()).to(
            equal("hostname_environment_var")
        )

    # Test case 3: Both Context variable and environment variable are not set
    expect(lambda: get_hostname_from_context_or_environment_vars()).to(
        raise_error(EnvironmentNotConfigured)
    )

    # Test case 4: Test Context variables are used before environment variables
    HOSTNAME_VAR.set("hostname_context_var")
    with patch.dict(os.environ, {HOSTNAME_ENV_VAR: "hostname_environment_var"}):
        expect(get_hostname_from_context_or_environment_vars()).to(equal("hostname_context_var"))
    HOSTNAME_VAR.set(None)


def test_get_user_token_auth_from_context_or_environment_vars():
    # Test case 1: Context variable is set
    TOKEN_VAR.set("user_token_context_var")
    expect(get_user_token_auth_from_context_or_environment_vars().get_token().access_token).to(
        equal("user_token_context_var")
    )
    TOKEN_VAR.set(None)

    # Test case 2: Context variable is not set and environment variable is set
    with patch.dict(os.environ, {TOKEN_ENV_VAR: "user_token_environment_var"}):
        expect(get_user_token_auth_from_context_or_environment_vars().get_token().access_token).to(
            equal("user_token_environment_var")
        )

    # Test case 3: Both Context variable and environment variable are not set
    expect(lambda: get_user_token_auth_from_context_or_environment_vars()).to(
        raise_error(EnvironmentNotConfigured)
    )

    # Test case 4: Test Context variables are used before environment variables
    TOKEN_VAR.set("user_token_context_var")
    with patch.dict(os.environ, {TOKEN_ENV_VAR: "user_token_environment_var"}):
        expect(get_user_token_auth_from_context_or_environment_vars().get_token().access_token).to(
            equal("user_token_context_var")
        )
    TOKEN_VAR.set(None)
