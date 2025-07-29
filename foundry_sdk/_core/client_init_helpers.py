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


from contextvars import ContextVar
from typing import Optional

from foundry_sdk._core.auth_utils import Auth
from foundry_sdk._core.context_and_environment_vars import HOSTNAME_CONTEXT_VARS
from foundry_sdk._core.context_and_environment_vars import HOSTNAME_ENV_VARS
from foundry_sdk._core.context_and_environment_vars import TOKEN_CONTEXT_VARS
from foundry_sdk._core.context_and_environment_vars import TOKEN_ENV_VARS
from foundry_sdk._core.context_and_environment_vars import (
    maybe_get_value_from_context_or_environment_vars,
)  # NOQA
from foundry_sdk._core.user_token_auth_client import UserTokenAuth
from foundry_sdk._errors.environment_not_configured import EnvironmentNotConfigured


def get_hostname_from_context_or_environment_vars() -> str:
    hostname = maybe_get_value_from_context_or_environment_vars(
        context_vars=HOSTNAME_CONTEXT_VARS,
        env_vars=HOSTNAME_ENV_VARS,
    )
    if hostname is None:
        raise EnvironmentNotConfigured(
            "Unable to configure client hostname. Please pass in `hostname` to FoundryClient, "
            "or set the context variable in foundry_sdk."
        )
    return hostname


def get_user_token_auth_from_context_or_environment_vars() -> Auth:
    token = maybe_get_value_from_context_or_environment_vars(
        context_vars=TOKEN_CONTEXT_VARS,
        env_vars=TOKEN_ENV_VARS,
    )
    if token is None:
        raise EnvironmentNotConfigured(
            "Unable to configure client auth. Please pass in `auth` to FoundryClient, "
            "or set the context variable in foundry_sdk."
        )
    return UserTokenAuth(token=token)
