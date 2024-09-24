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
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.functions.models._data_value import DataValue
from foundry.v2.functions.models._execute_query_response import ExecuteQueryResponse
from foundry.v2.functions.models._function_rid import FunctionRid
from foundry.v2.functions.models._parameter_id import ParameterId
from foundry.v2.functions.models._query import Query
from foundry.v2.functions.models._query_api_name import QueryApiName


class QueryClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def execute(
        self,
        query_api_name: QueryApiName,
        *,
        parameters: Dict[ParameterId, Optional[DataValue]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ExecuteQueryResponse:
        """
        Executes a Query using the given parameters.

        Optional parameters do not need to be supplied.

        :param query_api_name: queryApiName
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ExecuteQueryResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/{queryApiName}/execute",
                query_params={
                    "preview": preview,
                },
                path_params={
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

    @validate_call
    @handle_unexpected
    def get(
        self,
        query_api_name: QueryApiName,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Query:
        """
        Gets a specific query type with the given API name.

        :param query_api_name: queryApiName
        :type query_api_name: QueryApiName
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Query
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/functions/queries/{queryApiName}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Query,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_by_rid(
        self,
        *,
        rid: FunctionRid,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Query:
        """
        Gets a specific query type with the given RID.

        :param rid:
        :type rid: FunctionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Query
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/getByRid",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "rid": rid,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "rid": FunctionRid,
                    },
                ),
                response_type=Query,
                request_timeout=request_timeout,
            ),
        )
