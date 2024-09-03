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


from foundry._core.auth_utils import Auth
from foundry._errors.environment_not_configured import EnvironmentNotConfigured
from foundry.api_client import ApiClient


class FoundryV2Client:
    """
    The Foundry V2 API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com").
    """

    def __init__(self, auth: Auth, hostname: str):
        from foundry.v2._namespaces.namespaces import Admin
        from foundry.v2._namespaces.namespaces import Datasets
        from foundry.v2._namespaces.namespaces import Ontologies
        from foundry.v2._namespaces.namespaces import Orchestration
        from foundry.v2._namespaces.namespaces import ThirdPartyApplications

        api_client = ApiClient(auth=auth, hostname=hostname)
        self.admin = Admin(api_client=api_client)
        self.datasets = Datasets(api_client=api_client)
        self.ontologies = Ontologies(api_client=api_client)
        self.orchestration = Orchestration(api_client=api_client)
        self.third_party_applications = ThirdPartyApplications(api_client=api_client)
