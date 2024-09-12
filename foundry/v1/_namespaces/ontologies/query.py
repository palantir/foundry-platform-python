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

from typing import Annotated
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call

from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v1.models._execute_query_request import ExecuteQueryRequest
from foundry.v1.models._execute_query_request_dict import ExecuteQueryRequestDict
from foundry.v1.models._execute_query_response import ExecuteQueryResponse
from foundry.v1.models._ontology_rid import OntologyRid
from foundry.v1.models._query_api_name import QueryApiName


class QueryResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def execute(
        self,
        ontology_rid: OntologyRid,
        query_api_name: QueryApiName,
        execute_query_request: Union[ExecuteQueryRequest, ExecuteQueryRequestDict],
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ExecuteQueryResponse:
        """
        Executes a Query using the given parameters. Optional parameters do not need to be supplied.
        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param query_api_name: queryApiName
        :type query_api_name: QueryApiName
        :param execute_query_request: Body of the request
        :type execute_query_request: Union[ExecuteQueryRequest, ExecuteQueryRequestDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ExecuteQueryResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = execute_query_request

        _path_params["ontologyRid"] = ontology_rid

        _path_params["queryApiName"] = query_api_name

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[ExecuteQueryRequest, ExecuteQueryRequestDict],
                response_type=ExecuteQueryResponse,
                request_timeout=request_timeout,
            ),
        )
