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

from functools import cached_property
from typing import Any
from typing import Dict
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.functions import errors as functions_errors
from foundry.v2.functions.models._data_value import DataValue
from foundry.v2.functions.models._execute_query_response import ExecuteQueryResponse
from foundry.v2.functions.models._function_rid import FunctionRid
from foundry.v2.functions.models._parameter_id import ParameterId
from foundry.v2.functions.models._query import Query
from foundry.v2.functions.models._query_api_name import QueryApiName


class QueryClient:
    """
    The API client for the Query Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _QueryClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _QueryClientRaw(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        query_api_name: QueryApiName,
        *,
        parameters: Dict[ParameterId, Optional[DataValue]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
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

        :raises ExecuteQueryPermissionDenied: Could not execute the Query.
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
                throwable_errors={
                    "ExecuteQueryPermissionDenied": functions_errors.ExecuteQueryPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        query_api_name: QueryApiName,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
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

        :raises QueryNotFound: The given Query could not be found.
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
                throwable_errors={
                    "QueryNotFound": functions_errors.QueryNotFound,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_by_rid(
        self,
        *,
        rid: FunctionRid,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
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

        :raises GetByRidQueriesPermissionDenied: Could not getByRid the Query.
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
                throwable_errors={
                    "GetByRidQueriesPermissionDenied": functions_errors.GetByRidQueriesPermissionDenied,
                },
            ),
        ).decode()


class _QueryClientRaw:
    """
    The API client for the Query Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        query_api_name: QueryApiName,
        *,
        parameters: Dict[ParameterId, Optional[DataValue]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ExecuteQueryResponse]:
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
        :rtype: ApiResponse[ExecuteQueryResponse]

        :raises ExecuteQueryPermissionDenied: Could not execute the Query.
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
                throwable_errors={
                    "ExecuteQueryPermissionDenied": functions_errors.ExecuteQueryPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        query_api_name: QueryApiName,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Query]:
        """
        Gets a specific query type with the given API name.

        :param query_api_name: queryApiName
        :type query_api_name: QueryApiName
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Query]

        :raises QueryNotFound: The given Query could not be found.
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
                throwable_errors={
                    "QueryNotFound": functions_errors.QueryNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_by_rid(
        self,
        *,
        rid: FunctionRid,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Query]:
        """
        Gets a specific query type with the given RID.

        :param rid:
        :type rid: FunctionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Query]

        :raises GetByRidQueriesPermissionDenied: Could not getByRid the Query.
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
                throwable_errors={
                    "GetByRidQueriesPermissionDenied": functions_errors.GetByRidQueriesPermissionDenied,
                },
            ),
        )


class _QueryClientStreaming:
    """
    The API client for the Query Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        query_api_name: QueryApiName,
        *,
        parameters: Dict[ParameterId, Optional[DataValue]],
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ExecuteQueryResponse]:
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
        :rtype: StreamingContextManager[ExecuteQueryResponse]

        :raises ExecuteQueryPermissionDenied: Could not execute the Query.
        """

        return self._api_client.stream_api(
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
                throwable_errors={
                    "ExecuteQueryPermissionDenied": functions_errors.ExecuteQueryPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        query_api_name: QueryApiName,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Query]:
        """
        Gets a specific query type with the given API name.

        :param query_api_name: queryApiName
        :type query_api_name: QueryApiName
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Query]

        :raises QueryNotFound: The given Query could not be found.
        """

        return self._api_client.stream_api(
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
                throwable_errors={
                    "QueryNotFound": functions_errors.QueryNotFound,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_by_rid(
        self,
        *,
        rid: FunctionRid,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Query]:
        """
        Gets a specific query type with the given RID.

        :param rid:
        :type rid: FunctionRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Query]

        :raises GetByRidQueriesPermissionDenied: Could not getByRid the Query.
        """

        return self._api_client.stream_api(
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
                throwable_errors={
                    "GetByRidQueriesPermissionDenied": functions_errors.GetByRidQueriesPermissionDenied,
                },
            ),
        )
