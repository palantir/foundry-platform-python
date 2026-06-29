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

import annotated_types
import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.functions import errors as functions_errors
from foundry_sdk.v2.functions import models as functions_models
from foundry_sdk.v2.ontologies import models as ontologies_models


class QueryClient:
    """
    The API client for the Query Resource.

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

        self.with_streaming_response = _QueryClientStreaming(self)
        self.with_raw_response = _QueryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        parameters: typing.Dict[
            functions_models.ParameterId, typing.Optional[functions_models.DataValue]
        ],
        attribution: typing.Optional[core_models.Attribution] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.ExecuteQueryResponse:
        """
        Executes a Query and returns the result as a single JSON object. By default, this executes
        the latest version of the query. The latest version is the one that was most recently
        published, which may be a pre-release version.

        This endpoint executes global (non-ontology-scoped) query functions. For ontology-scoped
        functions, use the equivalent endpoint under
        `/v2/ontologies/{ontology}/queries/{queryApiName}/execute`. For streaming or incremental
        result delivery, use `streamingExecute`.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param branch: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
        :type branch: Optional[FoundryBranch]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and not all workflows may be supported.
        :type transaction_id: Optional[TransactionId]
        :param version: The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.ExecuteQueryResponse

        :raises ExecuteQueryPermissionDenied: Could not execute the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/{queryApiName}/execute",
                query_params={
                    "preview": preview,
                    "transactionId": transaction_id,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "attribution": attribution,
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=functions_models.ExecuteQueryRequest(
                    parameters=parameters,
                    version=version,
                    branch=branch,
                ),
                response_type=functions_models.ExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteQueryPermissionDenied": functions_errors.ExecuteQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute_async(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        parameters: typing.Dict[
            functions_models.ParameterId, typing.Optional[functions_models.DataValue]
        ],
        attribution: typing.Optional[core_models.Attribution] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        ontology: typing.Optional[ontologies_models.OntologyIdentifier] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.ExecuteQueryAsyncResponse:
        """
        Submits a Query for asynchronous execution. Returns either an execution ID
        for polling, or the complete result if execution finished immediately.

        Use the Execution resource's getResult endpoint to poll for the
        result of a submitted execution.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param branch: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
        :type branch: Optional[FoundryBranch]
        :param ontology: Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
        :type ontology: Optional[OntologyIdentifier]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and not all workflows may be supported.
        :type transaction_id: Optional[TransactionId]
        :param version: The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.ExecuteQueryAsyncResponse

        :raises ExecuteAsyncQueryPermissionDenied: Could not executeAsync the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/{queryApiName}/executeAsync",
                query_params={
                    "preview": preview,
                    "transactionId": transaction_id,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "attribution": attribution,
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=functions_models.ExecuteAsyncQueryRequest(
                    ontology=ontology,
                    parameters=parameters,
                    version=version,
                    branch=branch,
                ),
                response_type=functions_models.ExecuteQueryAsyncResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteAsyncQueryPermissionDenied": functions_errors.ExecuteAsyncQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.Query:
        """
        Gets a specific query type with the given API name. By default, this gets the latest version of the query.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version:
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.Query

        :raises QueryNotFound: The given Query could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/functions/queries/{queryApiName}",
                query_params={
                    "preview": preview,
                    "version": version,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "QueryNotFound": functions_errors.QueryNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_rid(
        self,
        *,
        rid: functions_models.FunctionRid,
        include_prerelease: typing.Optional[bool] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.Query:
        """
        Gets a specific query type with the given RID. By default, this gets the latest version of the query.

        :param rid:
        :type rid: FunctionRid
        :param include_prerelease: When no version is specified and this flag is set to true, the latest version resolution will consider prerelease versions (e.g., 1.2.3-beta could be returned as the latest). When false, only stable versions are considered when determining the latest version.  Defaults to false.
        :type include_prerelease: Optional[bool]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version:
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.Query

        :raises GetByRidPermissionDenied: Could not getByRid the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/functions/queries/getByRid",
                query_params={
                    "rid": rid,
                    "includePrerelease": include_prerelease,
                    "preview": preview,
                    "version": version,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByRidPermissionDenied": functions_errors.GetByRidPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_rid_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[functions_models.GetByRidQueriesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.GetByRidQueriesBatchResponse:
        """
        Gets a list of query types by RID in bulk. By default, this gets the latest version of each query.

        Queries are filtered from the response if they don't exist or the requesting token lacks the required
        permissions.

        The maximum batch size for this endpoint is 100.
        :param body: Body of the request
        :type body: List[GetByRidQueriesBatchRequestElement]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.GetByRidQueriesBatchResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/getByRidBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=functions_models.GetByRidQueriesBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def streaming_execute(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        parameters: typing.Dict[
            functions_models.ParameterId, typing.Optional[functions_models.DataValue]
        ],
        attribution: typing.Optional[core_models.Attribution] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        ontology: typing.Optional[ontologies_models.OntologyIdentifier] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.SseContextManager[functions_models.StreamingExecuteQueryResponse]:
        """
        Executes a Query and returns results as a Server-Sent Events (`text/event-stream`) stream.
        By default, this executes the latest version of the query. The latest version is the one
        that was most recently published, which may be a pre-release version.

        This endpoint supports all Query functions. Each SSE event's `data` field is a JSON-encoded
        `StreamingExecuteQueryResponse` – either a data batch (`type: data`) carrying one or more
        result values, or an error (`type: error`) emitted before stream termination if execution
        fails. Non-streaming functions emit a single data event containing the entire result;
        streaming functions emit a data event per batch as results become available.

        Per the Server-Sent Events specification, each event is terminated by a blank line:

        ```
        data: {"type":"data","value":[{"productId":"SKU-001","price":29.99}]}

        data: {"type":"error","errorCode":"INVALID_ARGUMENT","errorName":"QueryRuntimeError","errorInstanceId":"3f8a9c7b-2e4d-4a1f-9b8c-7d6e5f4a3b2c","errorDescription":"Division by zero","parameters":{}}

        ```

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param branch: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
        :type branch: Optional[FoundryBranch]
        :param ontology: Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
        :type ontology: Optional[OntologyIdentifier]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and not all workflows may be supported.
        :type transaction_id: Optional[TransactionId]
        :param version: The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.SseContextManager[functions_models.StreamingExecuteQueryResponse]

        :raises StreamingExecuteQueryPermissionDenied: Could not streamingExecute the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/{queryApiName}/streamingExecute",
                query_params={
                    "preview": preview,
                    "transactionId": transaction_id,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "attribution": attribution,
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                },
                body=functions_models.StreamingExecuteQueryRequest(
                    ontology=ontology,
                    parameters=parameters,
                    version=version,
                    branch=branch,
                ),
                response_type=functions_models.StreamingExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "StreamingExecuteQueryPermissionDenied": functions_errors.StreamingExecuteQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "SSE"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def streaming_execute_events(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        parameters: typing.Dict[
            functions_models.ParameterId, typing.Optional[functions_models.DataValue]
        ],
        attribution: typing.Optional[core_models.Attribution] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        ontology: typing.Optional[ontologies_models.OntologyIdentifier] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.SseContextManager[functions_models.StreamingExecuteQueryResponse]:
        """
        Executes a Query and returns results as a Server-Sent Events (`text/event-stream`) stream.
        By default, this executes the latest version of the query. The latest version is the one
        that was most recently published, which may be a pre-release version.

        This endpoint supports all Query functions. Each SSE event's `data` field is a JSON-encoded
        `StreamingExecuteQueryResponse` – either a data batch (`type: data`) carrying one or more
        result values, or an error (`type: error`) emitted before stream termination if execution
        fails. Non-streaming functions emit a single data event containing the entire result;
        streaming functions emit a data event per batch as results become available.

        Per the Server-Sent Events specification, each event is terminated by a blank line:

        ```
        data: {"type":"data","value":[{"productId":"SKU-001","price":29.99}]}

        data: {"type":"error","errorCode":"INVALID_ARGUMENT","errorName":"QueryRuntimeError","errorInstanceId":"3f8a9c7b-2e4d-4a1f-9b8c-7d6e5f4a3b2c","errorDescription":"Division by zero","parameters":{}}

        ```

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param branch: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
        :type branch: Optional[FoundryBranch]
        :param ontology: Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
        :type ontology: Optional[OntologyIdentifier]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and not all workflows may be supported.
        :type transaction_id: Optional[TransactionId]
        :param version: The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.SseContextManager[functions_models.StreamingExecuteQueryResponse]

        :raises StreamingExecuteEventsQueryPermissionDenied: Could not streamingExecuteEvents the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/{queryApiName}/streamingExecuteEvents",
                query_params={
                    "preview": preview,
                    "transactionId": transaction_id,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "attribution": attribution,
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                },
                body=functions_models.StreamingExecuteEventsQueryRequest(
                    ontology=ontology,
                    parameters=parameters,
                    version=version,
                    branch=branch,
                ),
                response_type=functions_models.StreamingExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "StreamingExecuteEventsQueryPermissionDenied": functions_errors.StreamingExecuteEventsQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "SSE"),
            ),
        )


class _QueryClientRaw:
    def __init__(self, client: QueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def execute_async(_: functions_models.ExecuteQueryAsyncResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...
        def get_by_rid_batch(_: functions_models.GetByRidQueriesBatchResponse): ...
        def streaming_execute(_: functions_models.StreamingExecuteQueryResponse): ...
        def streaming_execute_events(_: functions_models.StreamingExecuteQueryResponse): ...

        self.execute = core.with_raw_response(execute, client.execute)
        self.execute_async = core.with_raw_response(execute_async, client.execute_async)
        self.get = core.with_raw_response(get, client.get)
        self.get_by_rid = core.with_raw_response(get_by_rid, client.get_by_rid)
        self.get_by_rid_batch = core.with_raw_response(get_by_rid_batch, client.get_by_rid_batch)
        self.streaming_execute = core.with_raw_response(streaming_execute, client.streaming_execute)
        self.streaming_execute_events = core.with_raw_response(
            streaming_execute_events, client.streaming_execute_events
        )


class _QueryClientStreaming:
    def __init__(self, client: QueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def execute_async(_: functions_models.ExecuteQueryAsyncResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...
        def get_by_rid_batch(_: functions_models.GetByRidQueriesBatchResponse): ...
        def streaming_execute(_: functions_models.StreamingExecuteQueryResponse): ...
        def streaming_execute_events(_: functions_models.StreamingExecuteQueryResponse): ...

        self.execute = core.with_streaming_response(execute, client.execute)
        self.execute_async = core.with_streaming_response(execute_async, client.execute_async)
        self.get = core.with_streaming_response(get, client.get)
        self.get_by_rid = core.with_streaming_response(get_by_rid, client.get_by_rid)
        self.get_by_rid_batch = core.with_streaming_response(
            get_by_rid_batch, client.get_by_rid_batch
        )
        self.streaming_execute = core.with_sse_response(streaming_execute, client.streaming_execute)
        self.streaming_execute_events = core.with_sse_response(
            streaming_execute_events, client.streaming_execute_events
        )


class AsyncQueryClient:
    """
    The API client for the Query Resource.

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

        self.with_streaming_response = _AsyncQueryClientStreaming(self)
        self.with_raw_response = _AsyncQueryClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        parameters: typing.Dict[
            functions_models.ParameterId, typing.Optional[functions_models.DataValue]
        ],
        attribution: typing.Optional[core_models.Attribution] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.ExecuteQueryResponse]:
        """
        Executes a Query and returns the result as a single JSON object. By default, this executes
        the latest version of the query. The latest version is the one that was most recently
        published, which may be a pre-release version.

        This endpoint executes global (non-ontology-scoped) query functions. For ontology-scoped
        functions, use the equivalent endpoint under
        `/v2/ontologies/{ontology}/queries/{queryApiName}/execute`. For streaming or incremental
        result delivery, use `streamingExecute`.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param branch: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
        :type branch: Optional[FoundryBranch]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and not all workflows may be supported.
        :type transaction_id: Optional[TransactionId]
        :param version: The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[functions_models.ExecuteQueryResponse]

        :raises ExecuteQueryPermissionDenied: Could not execute the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/{queryApiName}/execute",
                query_params={
                    "preview": preview,
                    "transactionId": transaction_id,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "attribution": attribution,
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=functions_models.ExecuteQueryRequest(
                    parameters=parameters,
                    version=version,
                    branch=branch,
                ),
                response_type=functions_models.ExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteQueryPermissionDenied": functions_errors.ExecuteQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def execute_async(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        parameters: typing.Dict[
            functions_models.ParameterId, typing.Optional[functions_models.DataValue]
        ],
        attribution: typing.Optional[core_models.Attribution] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        ontology: typing.Optional[ontologies_models.OntologyIdentifier] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.ExecuteQueryAsyncResponse]:
        """
        Submits a Query for asynchronous execution. Returns either an execution ID
        for polling, or the complete result if execution finished immediately.

        Use the Execution resource's getResult endpoint to poll for the
        result of a submitted execution.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param branch: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
        :type branch: Optional[FoundryBranch]
        :param ontology: Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
        :type ontology: Optional[OntologyIdentifier]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and not all workflows may be supported.
        :type transaction_id: Optional[TransactionId]
        :param version: The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[functions_models.ExecuteQueryAsyncResponse]

        :raises ExecuteAsyncQueryPermissionDenied: Could not executeAsync the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/{queryApiName}/executeAsync",
                query_params={
                    "preview": preview,
                    "transactionId": transaction_id,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "attribution": attribution,
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=functions_models.ExecuteAsyncQueryRequest(
                    ontology=ontology,
                    parameters=parameters,
                    version=version,
                    branch=branch,
                ),
                response_type=functions_models.ExecuteQueryAsyncResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteAsyncQueryPermissionDenied": functions_errors.ExecuteAsyncQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.Query]:
        """
        Gets a specific query type with the given API name. By default, this gets the latest version of the query.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version:
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[functions_models.Query]

        :raises QueryNotFound: The given Query could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/functions/queries/{queryApiName}",
                query_params={
                    "preview": preview,
                    "version": version,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "QueryNotFound": functions_errors.QueryNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_rid(
        self,
        *,
        rid: functions_models.FunctionRid,
        include_prerelease: typing.Optional[bool] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.Query]:
        """
        Gets a specific query type with the given RID. By default, this gets the latest version of the query.

        :param rid:
        :type rid: FunctionRid
        :param include_prerelease: When no version is specified and this flag is set to true, the latest version resolution will consider prerelease versions (e.g., 1.2.3-beta could be returned as the latest). When false, only stable versions are considered when determining the latest version.  Defaults to false.
        :type include_prerelease: Optional[bool]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version:
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[functions_models.Query]

        :raises GetByRidPermissionDenied: Could not getByRid the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/functions/queries/getByRid",
                query_params={
                    "rid": rid,
                    "includePrerelease": include_prerelease,
                    "preview": preview,
                    "version": version,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByRidPermissionDenied": functions_errors.GetByRidPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_rid_batch(
        self,
        body: typing_extensions.Annotated[
            typing.List[functions_models.GetByRidQueriesBatchRequestElement],
            annotated_types.Len(min_length=1, max_length=100),
        ],
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.GetByRidQueriesBatchResponse]:
        """
        Gets a list of query types by RID in bulk. By default, this gets the latest version of each query.

        Queries are filtered from the response if they don't exist or the requesting token lacks the required
        permissions.

        The maximum batch size for this endpoint is 100.
        :param body: Body of the request
        :type body: List[GetByRidQueriesBatchRequestElement]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[functions_models.GetByRidQueriesBatchResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/getByRidBatch",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=body,
                response_type=functions_models.GetByRidQueriesBatchResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def streaming_execute(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        parameters: typing.Dict[
            functions_models.ParameterId, typing.Optional[functions_models.DataValue]
        ],
        attribution: typing.Optional[core_models.Attribution] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        ontology: typing.Optional[ontologies_models.OntologyIdentifier] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncSseContextManager[functions_models.StreamingExecuteQueryResponse]:
        """
        Executes a Query and returns results as a Server-Sent Events (`text/event-stream`) stream.
        By default, this executes the latest version of the query. The latest version is the one
        that was most recently published, which may be a pre-release version.

        This endpoint supports all Query functions. Each SSE event's `data` field is a JSON-encoded
        `StreamingExecuteQueryResponse` – either a data batch (`type: data`) carrying one or more
        result values, or an error (`type: error`) emitted before stream termination if execution
        fails. Non-streaming functions emit a single data event containing the entire result;
        streaming functions emit a data event per batch as results become available.

        Per the Server-Sent Events specification, each event is terminated by a blank line:

        ```
        data: {"type":"data","value":[{"productId":"SKU-001","price":29.99}]}

        data: {"type":"error","errorCode":"INVALID_ARGUMENT","errorName":"QueryRuntimeError","errorInstanceId":"3f8a9c7b-2e4d-4a1f-9b8c-7d6e5f4a3b2c","errorDescription":"Division by zero","parameters":{}}

        ```

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param branch: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
        :type branch: Optional[FoundryBranch]
        :param ontology: Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
        :type ontology: Optional[OntologyIdentifier]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and not all workflows may be supported.
        :type transaction_id: Optional[TransactionId]
        :param version: The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncSseContextManager[functions_models.StreamingExecuteQueryResponse]

        :raises StreamingExecuteQueryPermissionDenied: Could not streamingExecute the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/{queryApiName}/streamingExecute",
                query_params={
                    "preview": preview,
                    "transactionId": transaction_id,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "attribution": attribution,
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                },
                body=functions_models.StreamingExecuteQueryRequest(
                    ontology=ontology,
                    parameters=parameters,
                    version=version,
                    branch=branch,
                ),
                response_type=functions_models.StreamingExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "StreamingExecuteQueryPermissionDenied": functions_errors.StreamingExecuteQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "SSE"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def streaming_execute_events(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        parameters: typing.Dict[
            functions_models.ParameterId, typing.Optional[functions_models.DataValue]
        ],
        attribution: typing.Optional[core_models.Attribution] = None,
        branch: typing.Optional[core_models.FoundryBranch] = None,
        ontology: typing.Optional[ontologies_models.OntologyIdentifier] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncSseContextManager[functions_models.StreamingExecuteQueryResponse]:
        """
        Executes a Query and returns results as a Server-Sent Events (`text/event-stream`) stream.
        By default, this executes the latest version of the query. The latest version is the one
        that was most recently published, which may be a pre-release version.

        This endpoint supports all Query functions. Each SSE event's `data` field is a JSON-encoded
        `StreamingExecuteQueryResponse` – either a data batch (`type: data`) carrying one or more
        result values, or an error (`type: error`) emitted before stream termination if execution
        fails. Non-streaming functions emit a single data event containing the entire result;
        streaming functions emit a data event per batch as results become available.

        Per the Server-Sent Events specification, each event is terminated by a blank line:

        ```
        data: {"type":"data","value":[{"productId":"SKU-001","price":29.99}]}

        data: {"type":"error","errorCode":"INVALID_ARGUMENT","errorName":"QueryRuntimeError","errorInstanceId":"3f8a9c7b-2e4d-4a1f-9b8c-7d6e5f4a3b2c","errorDescription":"Division by zero","parameters":{}}

        ```

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param branch: The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.
        :type branch: Optional[FoundryBranch]
        :param ontology: Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
        :type ontology: Optional[OntologyIdentifier]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and not all workflows may be supported.
        :type transaction_id: Optional[TransactionId]
        :param version: The version of the query to execute. When used with `branch`, the specified version must exist on the branch.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncSseContextManager[functions_models.StreamingExecuteQueryResponse]

        :raises StreamingExecuteEventsQueryPermissionDenied: Could not streamingExecuteEvents the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/functions/queries/{queryApiName}/streamingExecuteEvents",
                query_params={
                    "preview": preview,
                    "transactionId": transaction_id,
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "attribution": attribution,
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                },
                body=functions_models.StreamingExecuteEventsQueryRequest(
                    ontology=ontology,
                    parameters=parameters,
                    version=version,
                    branch=branch,
                ),
                response_type=functions_models.StreamingExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "StreamingExecuteEventsQueryPermissionDenied": functions_errors.StreamingExecuteEventsQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "SSE"),
            ),
        )


class _AsyncQueryClientRaw:
    def __init__(self, client: AsyncQueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def execute_async(_: functions_models.ExecuteQueryAsyncResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...
        def get_by_rid_batch(_: functions_models.GetByRidQueriesBatchResponse): ...
        def streaming_execute(_: functions_models.StreamingExecuteQueryResponse): ...
        def streaming_execute_events(_: functions_models.StreamingExecuteQueryResponse): ...

        self.execute = core.async_with_raw_response(execute, client.execute)
        self.execute_async = core.async_with_raw_response(execute_async, client.execute_async)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_by_rid = core.async_with_raw_response(get_by_rid, client.get_by_rid)
        self.get_by_rid_batch = core.async_with_raw_response(
            get_by_rid_batch, client.get_by_rid_batch
        )
        self.streaming_execute = core.async_with_raw_response(
            streaming_execute, client.streaming_execute
        )
        self.streaming_execute_events = core.async_with_raw_response(
            streaming_execute_events, client.streaming_execute_events
        )


class _AsyncQueryClientStreaming:
    def __init__(self, client: AsyncQueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def execute_async(_: functions_models.ExecuteQueryAsyncResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...
        def get_by_rid_batch(_: functions_models.GetByRidQueriesBatchResponse): ...
        def streaming_execute(_: functions_models.StreamingExecuteQueryResponse): ...
        def streaming_execute_events(_: functions_models.StreamingExecuteQueryResponse): ...

        self.execute = core.async_with_streaming_response(execute, client.execute)
        self.execute_async = core.async_with_streaming_response(execute_async, client.execute_async)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_by_rid = core.async_with_streaming_response(get_by_rid, client.get_by_rid)
        self.get_by_rid_batch = core.async_with_streaming_response(
            get_by_rid_batch, client.get_by_rid_batch
        )
        self.streaming_execute = core.async_with_sse_response(
            streaming_execute, client.streaming_execute
        )
        self.streaming_execute_events = core.async_with_sse_response(
            streaming_execute_events, client.streaming_execute_events
        )
