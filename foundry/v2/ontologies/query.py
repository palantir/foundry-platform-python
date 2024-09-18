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

from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.ontologies.models._artifact_repository_rid import ArtifactRepositoryRid
from foundry.v2.ontologies.models._data_value import DataValue
from foundry.v2.ontologies.models._execute_query_response import ExecuteQueryResponse
from foundry.v2.ontologies.models._ontology_identifier import OntologyIdentifier
from foundry.v2.ontologies.models._parameter_id import ParameterId
from foundry.v2.ontologies.models._query_api_name import QueryApiName
from foundry.v2.ontologies.models._sdk_package_name import SdkPackageName


class QueryClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def execute(
        self,
        ontology: OntologyIdentifier,
        query_api_name: QueryApiName,
        *,
        parameters: Dict[ParameterId, Optional[DataValue]],
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ExecuteQueryResponse:
        """
        Executes a Query using the given parameters.

        Optional parameters do not need to be supplied.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param query_api_name: queryApiName
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ExecuteQueryResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/queries/{queryApiName}/execute",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "queryApiName": query_api_name,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": Dict[ParameterId, Optional[DataValue]],
                    },
                ),
                response_type=ExecuteQueryResponse,
                request_timeout=request_timeout,
            ),
        )
