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


class FoundryClient:
    """
    The Foundry V1 API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        from foundry_sdk.v1.datasets._client import DatasetsClient
        from foundry_sdk.v1.ontologies._client import OntologiesClient

        self.datasets = DatasetsClient(auth=auth, hostname=hostname, config=config)
        self.ontologies = OntologiesClient(auth=auth, hostname=hostname, config=config)


class AsyncFoundryClient:
    """
    The Async Foundry V1 API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
        preview: bool = False,
    ):
        if not preview:
            raise ValueError(
                "The AsyncFoundryClient client is in beta. "
                "Please set the preview parameter to True to use it."
            )

        from foundry_sdk.v1.datasets._client import AsyncDatasetsClient
        from foundry_sdk.v1.ontologies._client import AsyncOntologiesClient

        self.datasets = AsyncDatasetsClient(auth=auth, hostname=hostname, config=config)
        self.ontologies = AsyncOntologiesClient(auth=auth, hostname=hostname, config=config)
