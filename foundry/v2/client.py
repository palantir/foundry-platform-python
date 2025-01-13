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


from typing import Optional

from foundry._core import Auth
from foundry._core import Config


class FoundryClient:
    """
    The Foundry V2 API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com").
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        from foundry.v2.admin.client import AdminClient
        from foundry.v2.aip_agents.client import AipAgentsClient
        from foundry.v2.connectivity.client import ConnectivityClient
        from foundry.v2.datasets.client import DatasetsClient
        from foundry.v2.filesystem.client import FilesystemClient
        from foundry.v2.functions.client import FunctionsClient
        from foundry.v2.ontologies.client import OntologiesClient
        from foundry.v2.orchestration.client import OrchestrationClient
        from foundry.v2.streams.client import StreamsClient
        from foundry.v2.third_party_applications.client import ThirdPartyApplicationsClient  # NOQA

        self.admin = AdminClient(auth=auth, hostname=hostname, config=config)
        self.aip_agents = AipAgentsClient(auth=auth, hostname=hostname, config=config)
        self.connectivity = ConnectivityClient(auth=auth, hostname=hostname, config=config)
        self.datasets = DatasetsClient(auth=auth, hostname=hostname, config=config)
        self.filesystem = FilesystemClient(auth=auth, hostname=hostname, config=config)
        self.functions = FunctionsClient(auth=auth, hostname=hostname, config=config)
        self.ontologies = OntologiesClient(auth=auth, hostname=hostname, config=config)
        self.orchestration = OrchestrationClient(auth=auth, hostname=hostname, config=config)
        self.streams = StreamsClient(auth=auth, hostname=hostname, config=config)
        self.third_party_applications = ThirdPartyApplicationsClient(
            auth=auth, hostname=hostname, config=config
        )
