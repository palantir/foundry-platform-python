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
from foundry.api.ontologies_v2_api_service_api import OntologiesV2ApiServiceApi
from foundry.api.datasets_api_service_api import DatasetsApiServiceApi
from foundry.api.ontologies_api_service_api import OntologiesApiServiceApi
from foundry.api_client import ApiClient
from foundry._errors.environment_not_configured import EnvironmentNotConfigured


class FoundryClient:
    """
    The Foundry API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com").
    """

    def __init__(self, auth: Auth, hostname: str):
        api_client = ApiClient(auth=auth, hostname=hostname)
        self.ontologies_v2 = OntologiesV2ApiServiceApi(api_client=api_client)
        self.datasets = DatasetsApiServiceApi(api_client=api_client)
        self.ontologies = OntologiesApiServiceApi(api_client=api_client)
