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

from foundry import _core as core


class FoundryClient:
    """
    The Foundry V2 API client.

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
        from foundry.v2.admin._client import AdminClient
        from foundry.v2.aip_agents._client import AipAgentsClient
        from foundry.v2.connectivity._client import ConnectivityClient
        from foundry.v2.datasets._client import DatasetsClient
        from foundry.v2.filesystem._client import FilesystemClient
        from foundry.v2.functions._client import FunctionsClient
        from foundry.v2.media_sets._client import MediaSetsClient
        from foundry.v2.ontologies._client import OntologiesClient
        from foundry.v2.orchestration._client import OrchestrationClient
        from foundry.v2.sql_queries._client import SqlQueriesClient
        from foundry.v2.streams._client import StreamsClient
        from foundry.v2.third_party_applications._client import ThirdPartyApplicationsClient  # NOQA

        self.admin = AdminClient(auth=auth, hostname=hostname, config=config)
        self.aip_agents = AipAgentsClient(auth=auth, hostname=hostname, config=config)
        self.connectivity = ConnectivityClient(auth=auth, hostname=hostname, config=config)
        self.datasets = DatasetsClient(auth=auth, hostname=hostname, config=config)
        self.filesystem = FilesystemClient(auth=auth, hostname=hostname, config=config)
        self.functions = FunctionsClient(auth=auth, hostname=hostname, config=config)
        self.media_sets = MediaSetsClient(auth=auth, hostname=hostname, config=config)
        self.ontologies = OntologiesClient(auth=auth, hostname=hostname, config=config)
        self.orchestration = OrchestrationClient(auth=auth, hostname=hostname, config=config)
        self.sql_queries = SqlQueriesClient(auth=auth, hostname=hostname, config=config)
        self.streams = StreamsClient(auth=auth, hostname=hostname, config=config)
        self.third_party_applications = ThirdPartyApplicationsClient(
            auth=auth, hostname=hostname, config=config
        )
