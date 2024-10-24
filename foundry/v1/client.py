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


from foundry._core import Auth


class FoundryClient:
    """
    The Foundry V1 API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com").
    """

    def __init__(self, auth: Auth, hostname: str):
        from foundry.v1.datasets.client import DatasetsClient
        from foundry.v1.ontologies.client import OntologiesClient

        self.datasets = DatasetsClient(auth=auth, hostname=hostname)
        self.ontologies = OntologiesClient(auth=auth, hostname=hostname)
