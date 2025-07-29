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


import typing

from foundry_sdk import _core as core
from foundry_sdk._core.client_init_helpers import (
    get_hostname_from_context_or_environment_vars,
)  # NOQA
from foundry_sdk._core.client_init_helpers import (
    get_user_token_auth_from_context_or_environment_vars,
)  # NOQA


class FoundryClient:
    """
    The Foundry V1 API client.

    :param auth: Required. Your auth configuration.
    :param hostname: Required. Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: typing.Optional[core.Auth] = None,
        hostname: typing.Optional[str] = None,
        config: typing.Optional[core.Config] = None,
    ):
        if auth is None:
            auth = get_user_token_auth_from_context_or_environment_vars()
        if hostname is None:
            hostname = get_hostname_from_context_or_environment_vars()

        from foundry_sdk.v1.datasets._client import DatasetsClient
        from foundry_sdk.v1.ontologies._client import OntologiesClient

        self.datasets = DatasetsClient(auth=auth, hostname=hostname, config=config)
        self.ontologies = OntologiesClient(auth=auth, hostname=hostname, config=config)


class AsyncFoundryClient:
    """
    The Async Foundry V1 API client.

    :param auth: Required. Your auth configuration.
    :param hostname: Required. Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: typing.Optional[core.Auth] = None,
        hostname: typing.Optional[str] = None,
        config: typing.Optional[core.Config] = None,
        preview: bool = False,
    ):
        if not preview:
            raise ValueError(
                "The AsyncFoundryClient client is in beta. "
                "Please set the preview parameter to True to use it."
            )
        if auth is None:
            auth = get_user_token_auth_from_context_or_environment_vars()
        if hostname is None:
            hostname = get_hostname_from_context_or_environment_vars()

        from foundry_sdk.v1.datasets._client import AsyncDatasetsClient
        from foundry_sdk.v1.ontologies._client import AsyncOntologiesClient

        self.datasets = AsyncDatasetsClient(auth=auth, hostname=hostname, config=config)
        self.ontologies = AsyncOntologiesClient(auth=auth, hostname=hostname, config=config)
