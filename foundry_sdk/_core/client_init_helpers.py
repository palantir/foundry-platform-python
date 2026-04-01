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
from typing import Optional

from foundry_sdk._core.auth_utils import Auth
from foundry_sdk._core.config import Config
from foundry_sdk._core.context_and_environment_vars import HOSTNAME_CONTEXT_VARS
from foundry_sdk._core.context_and_environment_vars import HOSTNAME_ENV_VARS
from foundry_sdk._core.context_and_environment_vars import TOKEN_CONTEXT_VARS
from foundry_sdk._core.context_and_environment_vars import TOKEN_ENV_VARS
from foundry_sdk._core.context_and_environment_vars import (
    maybe_get_value_from_context_or_environment_vars,
)  # NOQA
from foundry_sdk._core.hostname_supplier import HostnameSupplier
from foundry_sdk._core.hostname_supplier import ServiceDiscoveryHostnameSupplier
from foundry_sdk._core.hostname_supplier import StaticHostnameSupplier
from foundry_sdk._core.user_token_auth_client import UserTokenAuth
from foundry_sdk._core.utils import assert_non_empty_string
from foundry_sdk._errors.environment_not_configured import EnvironmentNotConfigured


def maybe_get_hostname_from_context_or_environment_vars() -> Optional[str]:
    return maybe_get_value_from_context_or_environment_vars(
        context_vars=HOSTNAME_CONTEXT_VARS,
        env_vars=HOSTNAME_ENV_VARS,
    )


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


def _clean_hostname(hostname: str, config: Optional[Config] = None) -> str:
    """Clean a raw hostname string: strip slashes, extract scheme, return base_url."""
    config = config or Config()
    stripped_hostname = hostname.split("://", maxsplit=1)[-1].strip("/")

    return f"{config.scheme}://{stripped_hostname}"


def maybe_create_hostname_supplier(
    base_url: Optional[str] = None, config: Optional[Config] = None
) -> Optional[HostnameSupplier]:
    config = config or Config()

    if base_url is not None:
        assert_non_empty_string(base_url, "hostname")
        return StaticHostnameSupplier(_clean_hostname(base_url, config))

    service_discovery_path = os.environ.get("FOUNDRY_SERVICE_DISCOVERY_V2", None)
    if service_discovery_path is not None:
        import yaml

        with open(service_discovery_path, "r") as f:
            services = yaml.safe_load(f)
            return ServiceDiscoveryHostnameSupplier(services)

    env_hostname = maybe_get_hostname_from_context_or_environment_vars()
    if env_hostname is not None:
        return StaticHostnameSupplier(_clean_hostname(env_hostname, config))

    return None


def create_hostname_supplier(
    base_url: Optional[str] = None, config: Optional[Config] = None
) -> HostnameSupplier:
    supplier = maybe_create_hostname_supplier(base_url, config)
    if supplier is None:
        raise ValueError(
            "Unable to infer Foundry hostname. Please provide a hostname parameter to the client."
        )
    return supplier
