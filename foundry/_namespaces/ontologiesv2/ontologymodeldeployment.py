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


from __future__ import annotations
from pydantic import StrictInt
from typing import Annotated
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from pydantic import validate_call

from foundry._errors.sdk_internal_error import handle_unexpected
from foundry.api_client import ApiClient

from foundry.models._deployment_api_name import DeploymentApiName
from foundry.models._deployment_metadata import DeploymentMetadata
from foundry.models._list_deployments_response import ListDeploymentsResponse
from foundry.models._ontology_identifier import OntologyIdentifier


class OntologyModelDeploymentResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def get(
        self,
        ontology: OntologyIdentifier,
        deployment: DeploymentApiName,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> DeploymentMetadata:
        """
        Fetches information about a model deployment within a given Ontology.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param deployment: The API name of the deployment you want to fetch information about.
        :type deployment: DeploymentApiName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: DeploymentMetadata
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _path_params["ontology"] = ontology

        _path_params["deployment"] = deployment

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: DeploymentMetadata,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v2/ontologies/{ontology}/models/deployments/{deployment}".format(
                **_path_params
            ),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def list(
        self,
        ontology: OntologyIdentifier,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListDeploymentsResponse:
        """
        Fetches a list of the available model deployments within a given Ontology.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListDeploymentsResponse
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _path_params["ontology"] = ontology

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: ListDeploymentsResponse,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v2/ontologies/{ontology}/models/deployments".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )
