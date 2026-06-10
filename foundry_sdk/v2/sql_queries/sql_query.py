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
from foundry_sdk.v2.sql_queries import errors as sql_queries_errors
from foundry_sdk.v2.sql_queries import models as sql_queries_models


class SqlQueryClient:
    """
    The API client for the SqlQuery Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _SqlQueryClientStreaming(self)
        self.with_raw_response = _SqlQueryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def cancel(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Cancels a query. If the query is no longer running this is effectively a no-op.

        :param sql_query_id: The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.
        :type sql_query_id: SqlQueryId
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
                query_params={},
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={},
                body=None,
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
        fallback_branch_ids: typing.Optional[typing.List[core_models.BranchName]] = None,
        serialization_format: typing.Optional[sql_queries_models.SerializationFormat] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> sql_queries_models.QueryStatus:
        """
        Executes a new query. Only the user that invoked the query can operate on the query. The size of query
        results are limited by default to 1 million rows. Contact your Palantir representative to discuss limit
        increases.

        :param query: The SQL query to execute. Queries should conform to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only. Datasets can be referenced in SQL queries by path or by RID. See the  [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets) for more details.
        :type query: str
        :param fallback_branch_ids: The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
        :type fallback_branch_ids: Optional[List[BranchName]]
        :param serialization_format: The format used to serialize query results. If not specified, defaults to `ARROW`.
        :type serialization_format: Optional[SerializationFormat]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: sql_queries_models.QueryStatus

        :raises ColumnTypesNotSupported: The query result contains column types that are not supported by the requested serialization format.
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
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=sql_queries_models.ExecuteSqlQueryRequest(
                    query=query,
                    fallback_branch_ids=fallback_branch_ids,
                    serialization_format=serialization_format,
                ),
                response_type=sql_queries_models.QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "ColumnTypesNotSupported": sql_queries_errors.ColumnTypesNotSupported,
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
    def execute_ontology(
        self,
        *,
        query: str,
        dry_run: typing.Optional[bool] = None,
        parameters: typing.Optional[sql_queries_models.Parameters] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        row_limit: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Executes a SQL query against the Ontology. Results are returned synchronously in
        [Apache Arrow](https://arrow.apache.org/) format.

        :param query: The SQL query to execute.
        :type query: str
        :param dry_run: If true, parse and validate the query without executing it. Defaults to false.
        :type dry_run: Optional[bool]
        :param parameters: Parameters for the SQL query. Can be either unnamed positional parameters or a named parameter mapping.
        :type parameters: Optional[Parameters]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param row_limit: Maximum number of rows to return.
        :type row_limit: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises ExecuteOntologySqlQueryPermissionDenied: Could not executeOntology the SqlQuery.
        :raises OntologyObjectTypeNotFound: The ontology query referenced an object type RID that does not exist or is not visible to the requesting user. Verify the RID (e.g. via list-object-types or get-object-type-details) and retry.
        :raises OntologyQueryFailed: The Ontology query failed.
        :raises OntologyQueryInvalidObjectBackend: The ontology query references object types or link types indexed in Object Storage V1, which is incompatible with Ontology SQL. Migrate the entities to Object Storage V2 or remove them from the query.
        :raises OntologyQueryNestedObjectSetTooLarge: The query references too many objects across joins, link lookups, or sub-queries. Narrow the scope (add filters, reduce joins, restrict object types) and retry. The actual and maximum object counts are returned as parameters.
        :raises OntologyQueryStringColumnTooLong: A string column in the query result contains a value larger than the platform's per-cell size limit. Exclude or filter the column, or scope the query to skip the oversized rows.
        :raises QueryParseError: The query cannot be parsed.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/executeOntology",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/octet-stream",
                },
                body=sql_queries_models.ExecuteOntologySqlQueryRequest(
                    query=query,
                    parameters=parameters,
                    row_limit=row_limit,
                    dry_run=dry_run,
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteOntologySqlQueryPermissionDenied": sql_queries_errors.ExecuteOntologySqlQueryPermissionDenied,
                    "OntologyObjectTypeNotFound": sql_queries_errors.OntologyObjectTypeNotFound,
                    "OntologyQueryFailed": sql_queries_errors.OntologyQueryFailed,
                    "OntologyQueryInvalidObjectBackend": sql_queries_errors.OntologyQueryInvalidObjectBackend,
                    "OntologyQueryNestedObjectSetTooLarge": sql_queries_errors.OntologyQueryNestedObjectSetTooLarge,
                    "OntologyQueryStringColumnTooLong": sql_queries_errors.OntologyQueryStringColumnTooLong,
                    "QueryParseError": sql_queries_errors.QueryParseError,
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
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.TableResponse:
        """
        Gets the results of a query. Results are returned in the `serializationFormat` specified at execute time
        (defaulting to [Apache Arrow](https://arrow.apache.org/) if no format is provided).

        This endpoint implements long polling and requests will time out after one minute. They can be safely
        retried while the query is still running.

        :param sql_query_id: The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.
        :type sql_query_id: SqlQueryId
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.TableResponse


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
                query_params={},
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
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
                response_mode=_sdk_internal.get("response_mode", "ARROW_TABLE"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_status(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> sql_queries_models.QueryStatus:
        """
        Gets the status of a query.

        :param sql_query_id: The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.
        :type sql_query_id: SqlQueryId
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
                query_params={},
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
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
        def execute_ontology(_: bytes): ...
        def get_results(_: bytes): ...
        def get_status(_: sql_queries_models.QueryStatus): ...

        self.cancel = core.with_raw_response(cancel, client.cancel)
        self.execute = core.with_raw_response(execute, client.execute)
        self.execute_ontology = core.with_raw_response(execute_ontology, client.execute_ontology)
        self.get_results = core.with_raw_response(get_results, client.get_results)
        self.get_status = core.with_raw_response(get_status, client.get_status)


class _SqlQueryClientStreaming:
    def __init__(self, client: SqlQueryClient) -> None:
        def execute(_: sql_queries_models.QueryStatus): ...
        def execute_ontology(_: bytes): ...
        def get_results(_: bytes): ...
        def get_status(_: sql_queries_models.QueryStatus): ...

        self.execute = core.with_streaming_response(execute, client.execute)
        self.execute_ontology = core.with_streaming_response(
            execute_ontology, client.execute_ontology
        )
        self.get_results = core.with_streaming_response(get_results, client.get_results)
        self.get_status = core.with_streaming_response(get_status, client.get_status)


class AsyncSqlQueryClient:
    """
    The API client for the SqlQuery Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncSqlQueryClientStreaming(self)
        self.with_raw_response = _AsyncSqlQueryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def cancel(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Cancels a query. If the query is no longer running this is effectively a no-op.

        :param sql_query_id: The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.
        :type sql_query_id: SqlQueryId
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
                query_params={},
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={},
                body=None,
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
        fallback_branch_ids: typing.Optional[typing.List[core_models.BranchName]] = None,
        serialization_format: typing.Optional[sql_queries_models.SerializationFormat] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[sql_queries_models.QueryStatus]:
        """
        Executes a new query. Only the user that invoked the query can operate on the query. The size of query
        results are limited by default to 1 million rows. Contact your Palantir representative to discuss limit
        increases.

        :param query: The SQL query to execute. Queries should conform to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only. Datasets can be referenced in SQL queries by path or by RID. See the  [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets) for more details.
        :type query: str
        :param fallback_branch_ids: The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.
        :type fallback_branch_ids: Optional[List[BranchName]]
        :param serialization_format: The format used to serialize query results. If not specified, defaults to `ARROW`.
        :type serialization_format: Optional[SerializationFormat]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[sql_queries_models.QueryStatus]

        :raises ColumnTypesNotSupported: The query result contains column types that are not supported by the requested serialization format.
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
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=sql_queries_models.ExecuteSqlQueryRequest(
                    query=query,
                    fallback_branch_ids=fallback_branch_ids,
                    serialization_format=serialization_format,
                ),
                response_type=sql_queries_models.QueryStatus,
                request_timeout=request_timeout,
                throwable_errors={
                    "ColumnTypesNotSupported": sql_queries_errors.ColumnTypesNotSupported,
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
    def execute_ontology(
        self,
        *,
        query: str,
        dry_run: typing.Optional[bool] = None,
        parameters: typing.Optional[sql_queries_models.Parameters] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        row_limit: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Executes a SQL query against the Ontology. Results are returned synchronously in
        [Apache Arrow](https://arrow.apache.org/) format.

        :param query: The SQL query to execute.
        :type query: str
        :param dry_run: If true, parse and validate the query without executing it. Defaults to false.
        :type dry_run: Optional[bool]
        :param parameters: Parameters for the SQL query. Can be either unnamed positional parameters or a named parameter mapping.
        :type parameters: Optional[Parameters]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param row_limit: Maximum number of rows to return.
        :type row_limit: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]

        :raises ExecuteOntologySqlQueryPermissionDenied: Could not executeOntology the SqlQuery.
        :raises OntologyObjectTypeNotFound: The ontology query referenced an object type RID that does not exist or is not visible to the requesting user. Verify the RID (e.g. via list-object-types or get-object-type-details) and retry.
        :raises OntologyQueryFailed: The Ontology query failed.
        :raises OntologyQueryInvalidObjectBackend: The ontology query references object types or link types indexed in Object Storage V1, which is incompatible with Ontology SQL. Migrate the entities to Object Storage V2 or remove them from the query.
        :raises OntologyQueryNestedObjectSetTooLarge: The query references too many objects across joins, link lookups, or sub-queries. Narrow the scope (add filters, reduce joins, restrict object types) and retry. The actual and maximum object counts are returned as parameters.
        :raises OntologyQueryStringColumnTooLong: A string column in the query result contains a value larger than the platform's per-cell size limit. Exclude or filter the column, or scope the query to skip the oversized rows.
        :raises QueryParseError: The query cannot be parsed.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/sqlQueries/executeOntology",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/octet-stream",
                },
                body=sql_queries_models.ExecuteOntologySqlQueryRequest(
                    query=query,
                    parameters=parameters,
                    row_limit=row_limit,
                    dry_run=dry_run,
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteOntologySqlQueryPermissionDenied": sql_queries_errors.ExecuteOntologySqlQueryPermissionDenied,
                    "OntologyObjectTypeNotFound": sql_queries_errors.OntologyObjectTypeNotFound,
                    "OntologyQueryFailed": sql_queries_errors.OntologyQueryFailed,
                    "OntologyQueryInvalidObjectBackend": sql_queries_errors.OntologyQueryInvalidObjectBackend,
                    "OntologyQueryNestedObjectSetTooLarge": sql_queries_errors.OntologyQueryNestedObjectSetTooLarge,
                    "OntologyQueryStringColumnTooLong": sql_queries_errors.OntologyQueryStringColumnTooLong,
                    "QueryParseError": sql_queries_errors.QueryParseError,
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
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[core.TableResponse]:
        """
                Gets the results of a query. Results are returned in the `serializationFormat` specified at execute time
                (defaulting to [Apache Arrow](https://arrow.apache.org/) if no format is provided).

                This endpoint implements long polling and requests will time out after one minute. They can be safely
                retried while the query is still running.

                :param sql_query_id: The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.
                :type sql_query_id: SqlQueryId
                :param request_timeout: timeout setting for this request in seconds.
                :type request_timeout: Optional[int]
                :return: Returns the result object.
                :rtype: typing.Awaitable[core.TableResponse
        ]

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
                query_params={},
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
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
                response_mode=_sdk_internal.get("response_mode", "ARROW_TABLE"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_status(
        self,
        sql_query_id: sql_queries_models.SqlQueryId,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[sql_queries_models.QueryStatus]:
        """
        Gets the status of a query.

        :param sql_query_id: The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints.
        :type sql_query_id: SqlQueryId
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
                query_params={},
                path_params={
                    "sqlQueryId": sql_query_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
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
        def execute_ontology(_: bytes): ...
        def get_results(_: bytes): ...
        def get_status(_: sql_queries_models.QueryStatus): ...

        self.cancel = core.async_with_raw_response(cancel, client.cancel)
        self.execute = core.async_with_raw_response(execute, client.execute)
        self.execute_ontology = core.async_with_raw_response(
            execute_ontology, client.execute_ontology
        )
        self.get_results = core.async_with_raw_response(get_results, client.get_results)
        self.get_status = core.async_with_raw_response(get_status, client.get_status)


class _AsyncSqlQueryClientStreaming:
    def __init__(self, client: AsyncSqlQueryClient) -> None:
        def execute(_: sql_queries_models.QueryStatus): ...
        def execute_ontology(_: bytes): ...
        def get_results(_: bytes): ...
        def get_status(_: sql_queries_models.QueryStatus): ...

        self.execute = core.async_with_streaming_response(execute, client.execute)
        self.execute_ontology = core.async_with_streaming_response(
            execute_ontology, client.execute_ontology
        )
        self.get_results = core.async_with_streaming_response(get_results, client.get_results)
        self.get_status = core.async_with_streaming_response(get_status, client.get_status)
