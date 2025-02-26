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

import warnings
from functools import cached_property
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict
from typing_extensions import deprecated
from typing_extensions import overload

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import BinaryStream
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.sql_queries import errors as sql_queries_errors
from foundry.v2.sql_queries.models._query_id import QueryId
from foundry.v2.sql_queries.models._query_status import QueryStatus


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
    def cancel(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Cancels a query. If the query is no longer running this is effectively a no-op.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises CancelQueryPermissionDenied: Could not cancel the Query.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/queries/{queryId}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryId": query_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelQueryPermissionDenied": sql_queries_errors.CancelQueryPermissionDenied,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        *,
        query: str,
        fallback_branch_ids: Optional[List[BranchName]] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> QueryStatus:
        """
        Executes a new query. Only the user that invoked the query can operate on the query.

        :param query: The SQL query to execute. Queries should confirm to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only.
        :type query: str
        :param fallback_branch_ids: The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
        :type fallback_branch_ids: Optional[List[BranchName]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: QueryStatus

        :raises ExecuteQueryPermissionDenied: Could not execute the Query.
        :raises QueryParseError: The query cannot be parsed.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/queries/execute",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "query": query,
                    "fallbackBranchIds": fallback_branch_ids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": str,
                        "fallbackBranchIds": Optional[List[BranchName]],
                    },
                ),
                response_type=QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteQueryPermissionDenied": sql_queries_errors.ExecuteQueryPermissionDenied,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
            ),
        ).decode()

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def get_results(
        self,
        query_id: QueryId,
        *,
        stream: Literal[True],
        preview: Optional[PreviewMode] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> BinaryStream:
        """
        Gets the results of a query. This endpoint implements long polling and requests will time out after
        one minute.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BinaryStream

        :raises GetResultsPermissionDenied: Could not getResults the Query.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """
        ...

    @overload
    def get_results(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        stream: Literal[False] = False,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> bytes:
        """
        Gets the results of a query. This endpoint implements long polling and requests will time out after
        one minute.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises GetResultsPermissionDenied: Could not getResults the Query.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """
        ...

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def get_results(
        self,
        query_id: QueryId,
        *,
        stream: bool,
        preview: Optional[PreviewMode] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Gets the results of a query. This endpoint implements long polling and requests will time out after
        one minute.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]

        :raises GetResultsPermissionDenied: Could not getResults the Query.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """
        ...

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_results(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        stream: bool = False,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Gets the results of a query. This endpoint implements long polling and requests will time out after
        one minute.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]

        :raises GetResultsPermissionDenied: Could not getResults the Query.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """

        if stream:
            warnings.warn(
                f"client.sql_queries.Query.get_results(..., stream=True, chunk_size={chunk_size}) is deprecated. Please use:\n\nwith client.sql_queries.Query.with_streaming_response.get_results(...) as response:\n    response.iter_bytes(chunk_size={chunk_size})\n",
                DeprecationWarning,
                stacklevel=2,
            )

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/queries/{queryId}/getResults",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryId": query_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                stream=stream,
                chunk_size=chunk_size,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResultsPermissionDenied": sql_queries_errors.GetResultsPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_status(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> QueryStatus:
        """
        Gets the status of a query.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: QueryStatus

        :raises GetStatusPermissionDenied: Could not getStatus the Query.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/queries/{queryId}/getStatus",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryId": query_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetStatusPermissionDenied": sql_queries_errors.GetStatusPermissionDenied,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
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
    def cancel(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[None]:
        """
        Cancels a query. If the query is no longer running this is effectively a no-op.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[None]

        :raises CancelQueryPermissionDenied: Could not cancel the Query.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/queries/{queryId}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryId": query_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelQueryPermissionDenied": sql_queries_errors.CancelQueryPermissionDenied,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        *,
        query: str,
        fallback_branch_ids: Optional[List[BranchName]] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[QueryStatus]:
        """
        Executes a new query. Only the user that invoked the query can operate on the query.

        :param query: The SQL query to execute. Queries should confirm to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only.
        :type query: str
        :param fallback_branch_ids: The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
        :type fallback_branch_ids: Optional[List[BranchName]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[QueryStatus]

        :raises ExecuteQueryPermissionDenied: Could not execute the Query.
        :raises QueryParseError: The query cannot be parsed.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/queries/execute",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "query": query,
                    "fallbackBranchIds": fallback_branch_ids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": str,
                        "fallbackBranchIds": Optional[List[BranchName]],
                    },
                ),
                response_type=QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteQueryPermissionDenied": sql_queries_errors.ExecuteQueryPermissionDenied,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_results(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[bytes]:
        """
        Gets the results of a query. This endpoint implements long polling and requests will time out after
        one minute.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[bytes]

        :raises GetResultsPermissionDenied: Could not getResults the Query.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/queries/{queryId}/getResults",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryId": query_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResultsPermissionDenied": sql_queries_errors.GetResultsPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_status(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[QueryStatus]:
        """
        Gets the status of a query.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[QueryStatus]

        :raises GetStatusPermissionDenied: Could not getStatus the Query.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/queries/{queryId}/getStatus",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryId": query_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetStatusPermissionDenied": sql_queries_errors.GetStatusPermissionDenied,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
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
    def cancel(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[None]:
        """
        Cancels a query. If the query is no longer running this is effectively a no-op.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[None]

        :raises CancelQueryPermissionDenied: Could not cancel the Query.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/queries/{queryId}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryId": query_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelQueryPermissionDenied": sql_queries_errors.CancelQueryPermissionDenied,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def execute(
        self,
        *,
        query: str,
        fallback_branch_ids: Optional[List[BranchName]] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[QueryStatus]:
        """
        Executes a new query. Only the user that invoked the query can operate on the query.

        :param query: The SQL query to execute. Queries should confirm to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only.
        :type query: str
        :param fallback_branch_ids: The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
        :type fallback_branch_ids: Optional[List[BranchName]]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[QueryStatus]

        :raises ExecuteQueryPermissionDenied: Could not execute the Query.
        :raises QueryParseError: The query cannot be parsed.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/queries/execute",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "query": query,
                    "fallbackBranchIds": fallback_branch_ids,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": str,
                        "fallbackBranchIds": Optional[List[BranchName]],
                    },
                ),
                response_type=QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteQueryPermissionDenied": sql_queries_errors.ExecuteQueryPermissionDenied,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_results(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[bytes]:
        """
        Gets the results of a query. This endpoint implements long polling and requests will time out after
        one minute.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[bytes]

        :raises GetResultsPermissionDenied: Could not getResults the Query.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/queries/{queryId}/getResults",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryId": query_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResultsPermissionDenied": sql_queries_errors.GetResultsPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_status(
        self,
        query_id: QueryId,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[QueryStatus]:
        """
        Gets the status of a query.

        :param query_id: queryId
        :type query_id: QueryId
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[QueryStatus]

        :raises GetStatusPermissionDenied: Could not getStatus the Query.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        """

        return self._api_client.stream_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/queries/{queryId}/getStatus",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "queryId": query_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetStatusPermissionDenied": sql_queries_errors.GetStatusPermissionDenied,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                },
            ),
        )
