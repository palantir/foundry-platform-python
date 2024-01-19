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

"""This file was auto-generated from our API Definition."""

from foundry.api.datasets_api_service_api import DatasetsApiServiceApi
from foundry.api.ontologies_api_service_api import OntologiesApiServiceApi
from foundry.api.ontologies_v2_api_service_api import OntologiesV2ApiServiceApi
from foundry.api_client import ApiClient
from foundry.auth._auth_utils import Auth
from foundry.configuration import Configuration


class FoundryClient:
    """
    The Foundry API client.

    :param auth: Your auth configuration.

    """

    def __init__(self, auth: Auth):
        self.configuration = Configuration(auth=auth)
        _api_client = ApiClient(configuration=self.configuration)
        self.ontologies_v2 = OntologiesV2ApiServiceApi(api_client=_api_client)
        self.datasets = DatasetsApiServiceApi(api_client=_api_client)
        self.ontologies = OntologiesApiServiceApi(api_client=_api_client)
