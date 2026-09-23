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


"""
Provides context and environment variables for the authentication user token and hostname.
They are used as an option to initialize the FoundryClient.
"""

import os
from contextvars import ContextVar
from typing import Optional
from typing import TypeVar

# Token and hostname variables
TOKEN_VAR: ContextVar[Optional[str]] = ContextVar("FOUNDRY_TOKEN", default=None)
HOSTNAME_VAR: ContextVar[Optional[str]] = ContextVar("FOUNDRY_HOSTNAME", default=None)
TOKEN_CONTEXT_VARS: list[ContextVar[Optional[str]]] = [TOKEN_VAR]
HOSTNAME_CONTEXT_VARS: list[ContextVar[Optional[str]]] = [HOSTNAME_VAR]

TOKEN_ENV_VAR: str = "FOUNDRY_TOKEN"
HOSTNAME_ENV_VAR: str = "FOUNDRY_HOSTNAME"
TOKEN_ENV_VARS: list[str] = [TOKEN_ENV_VAR]
HOSTNAME_ENV_VARS: list[str] = [HOSTNAME_ENV_VAR]

# Attribution variables
ATTRIBUTION_VAR: ContextVar[Optional[list[str]]] = ContextVar("ATTRIBUTION_RESOURCES", default=None)
ATTRIBUTION_CONTEXT_VARS: list[ContextVar[Optional[list[str]]]] = [ATTRIBUTION_VAR]

# Additional user agent variables
ADDITIONAL_USER_AGENTS: ContextVar[Optional[list[str]]] = ContextVar(
    "ADDITIONAL_USER_AGENTS", default=None
)

# Trace and Span context variables
TRACE_ID_VAR: ContextVar[Optional[str]] = ContextVar("FOUNDRY_TRACE_ID", default=None)
SPAN_ID_VAR: ContextVar[Optional[str]] = ContextVar("FOUNDRY_SPAN_ID", default=None)
SAMPLED_VAR: ContextVar[Optional[str]] = ContextVar("FOUNDRY_SAMPLED", default=None)
TRACE_ID_CONTEXT_VARS: list[ContextVar[Optional[str]]] = [TRACE_ID_VAR]
SPAN_ID_CONTEXT_VARS: list[ContextVar[Optional[str]]] = [SPAN_ID_VAR]
SAMPLED_CONTEXT_VARS: list[ContextVar[Optional[str]]] = [SAMPLED_VAR]

TRACE_ID_ENV_VAR: str = "FOUNDRY_TRACE_ID"
SPAN_ID_ENV_VAR: str = "FOUNDRY_SPAN_ID"
SAMPLED_ENV_VAR: str = "FOUNDRY_SAMPLED"
TRACE_ID_ENV_VARS: list[str] = [TRACE_ID_ENV_VAR]
SPAN_ID_ENV_VARS: list[str] = [SPAN_ID_ENV_VAR]
SAMPLED_ENV_VARS: list[str] = [SAMPLED_ENV_VAR]

# Execution context variables
TRANSACTION_ID_VAR: ContextVar[Optional[str]] = ContextVar("FOUNDRY_TRANSACTION_ID", default=None)
SCENARIO_RID_VAR: ContextVar[Optional[str]] = ContextVar("FOUNDRY_SCENARIO_RID", default=None)
TRANSACTION_ID_CONTEXT_VARS: list[ContextVar[Optional[str]]] = [TRANSACTION_ID_VAR]
SCENARIO_RID_CONTEXT_VARS: list[ContextVar[Optional[str]]] = [SCENARIO_RID_VAR]

T = TypeVar("T")


def _maybe_get_environment_var(env_vars: list[str]) -> Optional[str]:
    for env_var in env_vars:
        value = os.environ.get(env_var)
        if value is not None:
            return value
    return None


def maybe_get_context_var(
    context_vars: list[ContextVar[Optional[T]]],
) -> Optional[T]:
    for context_var in context_vars:
        value = context_var.get()
        if value is not None:
            return value
    return None


def maybe_get_value_from_context_or_environment_vars(
    context_vars: list[ContextVar[Optional[str]]], env_vars: list[str]
) -> Optional[str]:
    return maybe_get_context_var(context_vars) or _maybe_get_environment_var(env_vars)
