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


import typing

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.datasets import models as datasets_models
from foundry_sdk.v2.sql_queries import errors as sql_queries_errors
from foundry_sdk.v2.sql_queries import models as sql_queries_models


class SqlQueryClient:
    """
    The API client for the SqlQuery Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _SqlQueryClientStreaming(self)
        self.with_raw_response = _SqlQueryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def cancel(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Cancels a query. If the query is no longer running this is effectively a no-op.

        :param sql_query_id: The id of a query.
        :type sql_query_id: SqlQueryId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises CancelSqlQueryPermissionDenied: Could not cancel the SqlQuery.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryParseError: The query cannot be parsed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        :raises QueryRunning: The query is running.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/{sqlQueryId}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelSqlQueryPermissionDenied": sql_queries_errors.CancelSqlQueryPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                    "QueryRunning": sql_queries_errors.QueryRunning,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        *,
        query: str,
        fallback_branch_ids: typing.Optional[typing.List[datasets_models.BranchName]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> sql_queries_models.QueryStatus:
        """
        Executes a new query. Only the user that invoked the query can operate on the query. The size of query
        results are limited by default to 1 million rows. Contact your Palantir representative to discuss limit
        increases.

        :param query: The SQL query to execute. Queries should conform to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only. Refer the following [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets) on the supported syntax for referencing datasets in SQL queries.
        :type query: str
        :param fallback_branch_ids: The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
        :type fallback_branch_ids: Optional[List[BranchName]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: sql_queries_models.QueryStatus

        :raises ExecuteSqlQueryPermissionDenied: Could not execute the SqlQuery.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryParseError: The query cannot be parsed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        :raises QueryRunning: The query is running.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/execute",
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": str,
                        "fallbackBranchIds": typing.Optional[
                            typing.List[datasets_models.BranchName]
                        ],
                    },
                ),
                response_type=sql_queries_models.QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteSqlQueryPermissionDenied": sql_queries_errors.ExecuteSqlQueryPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                    "QueryRunning": sql_queries_errors.QueryRunning,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_results(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Gets the results of a query. The results of the query are returned in the
        [Apache Arrow](https://arrow.apache.org/) format.

        This endpoint implements long polling and requests will time out after one minute. They can be safely
        retried while the query is still running.

        :param sql_query_id: The id of a query.
        :type sql_query_id: SqlQueryId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises GetResultsSqlQueryPermissionDenied: Could not getResults the SqlQuery.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryParseError: The query cannot be parsed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        :raises QueryRunning: The query is running.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/{sqlQueryId}/getResults",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResultsSqlQueryPermissionDenied": sql_queries_errors.GetResultsSqlQueryPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                    "QueryRunning": sql_queries_errors.QueryRunning,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_status(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> sql_queries_models.QueryStatus:
        """
        Gets the status of a query.

        :param sql_query_id: The id of a query.
        :type sql_query_id: SqlQueryId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: sql_queries_models.QueryStatus

        :raises GetStatusSqlQueryPermissionDenied: Could not getStatus the SqlQuery.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryParseError: The query cannot be parsed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        :raises QueryRunning: The query is running.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/{sqlQueryId}/getStatus",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=sql_queries_models.QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetStatusSqlQueryPermissionDenied": sql_queries_errors.GetStatusSqlQueryPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                    "QueryRunning": sql_queries_errors.QueryRunning,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _SqlQueryClientRaw:
    def __init__(self, client: SqlQueryClient) -> None:
        def cancel(_: None): ...
        def execute(_: sql_queries_models.QueryStatus): ...
        def get_results(_: bytes): ...
        def get_status(_: sql_queries_models.QueryStatus): ...

        self.cancel = core.with_raw_response(cancel, client.cancel)
        self.execute = core.with_raw_response(execute, client.execute)
        self.get_results = core.with_raw_response(get_results, client.get_results)
        self.get_status = core.with_raw_response(get_status, client.get_status)


class _SqlQueryClientStreaming:
    def __init__(self, client: SqlQueryClient) -> None:
        def execute(_: sql_queries_models.QueryStatus): ...
        def get_results(_: bytes): ...
        def get_status(_: sql_queries_models.QueryStatus): ...

        self.execute = core.with_streaming_response(execute, client.execute)
        self.get_results = core.with_streaming_response(get_results, client.get_results)
        self.get_status = core.with_streaming_response(get_status, client.get_status)


class AsyncSqlQueryClient:
    """
    The API client for the SqlQuery Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncSqlQueryClientStreaming(self)
        self.with_raw_response = _AsyncSqlQueryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def cancel(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Cancels a query. If the query is no longer running this is effectively a no-op.

        :param sql_query_id: The id of a query.
        :type sql_query_id: SqlQueryId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises CancelSqlQueryPermissionDenied: Could not cancel the SqlQuery.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryParseError: The query cannot be parsed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        :raises QueryRunning: The query is running.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/{sqlQueryId}/cancel",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "CancelSqlQueryPermissionDenied": sql_queries_errors.CancelSqlQueryPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                    "QueryRunning": sql_queries_errors.QueryRunning,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        *,
        query: str,
        fallback_branch_ids: typing.Optional[typing.List[datasets_models.BranchName]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[sql_queries_models.QueryStatus]:
        """
        Executes a new query. Only the user that invoked the query can operate on the query. The size of query
        results are limited by default to 1 million rows. Contact your Palantir representative to discuss limit
        increases.

        :param query: The SQL query to execute. Queries should conform to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only. Refer the following [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets) on the supported syntax for referencing datasets in SQL queries.
        :type query: str
        :param fallback_branch_ids: The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
        :type fallback_branch_ids: Optional[List[BranchName]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[sql_queries_models.QueryStatus]

        :raises ExecuteSqlQueryPermissionDenied: Could not execute the SqlQuery.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryParseError: The query cannot be parsed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        :raises QueryRunning: The query is running.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/execute",
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": str,
                        "fallbackBranchIds": typing.Optional[
                            typing.List[datasets_models.BranchName]
                        ],
                    },
                ),
                response_type=sql_queries_models.QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteSqlQueryPermissionDenied": sql_queries_errors.ExecuteSqlQueryPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                    "QueryRunning": sql_queries_errors.QueryRunning,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_results(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Gets the results of a query. The results of the query are returned in the
        [Apache Arrow](https://arrow.apache.org/) format.

        This endpoint implements long polling and requests will time out after one minute. They can be safely
        retried while the query is still running.

        :param sql_query_id: The id of a query.
        :type sql_query_id: SqlQueryId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]

        :raises GetResultsSqlQueryPermissionDenied: Could not getResults the SqlQuery.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryParseError: The query cannot be parsed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        :raises QueryRunning: The query is running.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/{sqlQueryId}/getResults",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetResultsSqlQueryPermissionDenied": sql_queries_errors.GetResultsSqlQueryPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                    "QueryRunning": sql_queries_errors.QueryRunning,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_status(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[sql_queries_models.QueryStatus]:
        """
        Gets the status of a query.

        :param sql_query_id: The id of a query.
        :type sql_query_id: SqlQueryId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[sql_queries_models.QueryStatus]

        :raises GetStatusSqlQueryPermissionDenied: Could not getStatus the SqlQuery.
        :raises QueryCanceled: The query was canceled.
        :raises QueryFailed: The query failed.
        :raises QueryParseError: The query cannot be parsed.
        :raises QueryPermissionDenied: The provided token does not have permission to access the given query.
        :raises QueryRunning: The query is running.
        :raises ReadQueryInputsPermissionDenied: The provided token does not have permission to access the inputs to the query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/sqlQueries/{sqlQueryId}/getStatus",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=sql_queries_models.QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetStatusSqlQueryPermissionDenied": sql_queries_errors.GetStatusSqlQueryPermissionDenied,
                    "QueryCanceled": sql_queries_errors.QueryCanceled,
                    "QueryFailed": sql_queries_errors.QueryFailed,
                    "QueryParseError": sql_queries_errors.QueryParseError,
                    "QueryPermissionDenied": sql_queries_errors.QueryPermissionDenied,
                    "QueryRunning": sql_queries_errors.QueryRunning,
                    "ReadQueryInputsPermissionDenied": sql_queries_errors.ReadQueryInputsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncSqlQueryClientRaw:
    def __init__(self, client: AsyncSqlQueryClient) -> None:
        def cancel(_: None): ...
        def execute(_: sql_queries_models.QueryStatus): ...
        def get_results(_: bytes): ...
        def get_status(_: sql_queries_models.QueryStatus): ...

        self.cancel = core.async_with_raw_response(cancel, client.cancel)
        self.execute = core.async_with_raw_response(execute, client.execute)
        self.get_results = core.async_with_raw_response(get_results, client.get_results)
        self.get_status = core.async_with_raw_response(get_status, client.get_status)


class _AsyncSqlQueryClientStreaming:
    def __init__(self, client: AsyncSqlQueryClient) -> None:
        def execute(_: sql_queries_models.QueryStatus): ...
        def get_results(_: bytes): ...
        def get_status(_: sql_queries_models.QueryStatus): ...

        self.execute = core.async_with_streaming_response(execute, client.execute)
        self.get_results = core.async_with_streaming_response(get_results, client.get_results)
        self.get_status = core.async_with_streaming_response(get_status, client.get_status)
