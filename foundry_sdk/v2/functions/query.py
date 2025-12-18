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
from foundry_sdk.v2.functions import errors as functions_errors
from foundry_sdk.v2.functions import models as functions_models
from foundry_sdk.v2.ontologies import models as ontologies_models


class QueryClient:
    """
    The API client for the Query Resource.

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
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.ExecuteQueryResponse:
        """
        Executes a Query using the given parameters. By default, this executes the latest version of the query.

        This endpoint is maintained for backward compatibility only.

        For all new implementations, use the `streamingExecute` endpoint, which supports all function types
        and provides enhanced functionality.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and all workflows may not be supported.
        :type transaction_id: Optional[TransactionId]
        :param version:
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
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.Query:
        """
        Gets a specific query type with the given RID.By default, this gets the latest version of the query.

        :param rid:
        :type rid: FunctionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version:
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: functions_models.Query

        :raises GetByRidQueriesPermissionDenied: Could not getByRid the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body=functions_models.GetByRidQueriesRequest(
                    rid=rid,
                    version=version,
                ),
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByRidQueriesPermissionDenied": functions_errors.GetByRidQueriesPermissionDenied,
                },
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
        ontology: typing.Optional[ontologies_models.OntologyIdentifier] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Executes a Query using the given parameters, returning results as an NDJSON stream. By default, this executes the latest version of the query.

        This endpoint supports all Query functions. The endpoint name 'streamingExecute' refers to the NDJSON
        streaming response format. Both streaming and non-streaming functions can use this endpoint.
        Non-streaming functions return a single-line NDJSON response, while streaming functions return multi-line NDJSON responses.
        This is the recommended endpoint for all query execution.

        The response is returned as a binary stream in NDJSON (Newline Delimited JSON) format, where each line
        is a StreamingExecuteQueryResponse containing either a data batch or an error.

        For a function returning a list of 5 records with a batch size of 3, the response stream would contain
        two lines. The first line contains the first 3 items, and the second line contains the remaining 2 items:

        ```
        {"type":"data","value":[{"productId":"SKU-001","price":29.99},{"productId":"SKU-002","price":49.99},{"productId":"SKU-003","price":19.99}]}
        {"type":"data","value":[{"productId":"SKU-004","price":39.99},{"productId":"SKU-005","price":59.99}]}
        ```

        Each line is a separate JSON object followed by a newline character. Clients should parse the stream
        line-by-line to process results as they arrive. If an error occurs during execution, the stream will
        contain an error line:

        ```
        {"type":"error","errorCode":"INVALID_ARGUMENT","errorName":"QueryRuntimeError","errorInstanceId":"3f8a9c7b-2e4d-4a1f-9b8c-7d6e5f4a3b2c","errorDescription":"Division by zero","parameters":{}}
        ```

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param ontology: Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
        :type ontology: Optional[OntologyIdentifier]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and all workflows may not be supported.
        :type transaction_id: Optional[TransactionId]
        :param version:
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

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
                    "Accept": "application/octet-stream",
                },
                body=functions_models.StreamingExecuteQueryRequest(
                    ontology=ontology,
                    parameters=parameters,
                    version=version,
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "StreamingExecuteQueryPermissionDenied": functions_errors.StreamingExecuteQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _QueryClientRaw:
    def __init__(self, client: QueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...
        def streaming_execute(_: bytes): ...

        self.execute = core.with_raw_response(execute, client.execute)
        self.get = core.with_raw_response(get, client.get)
        self.get_by_rid = core.with_raw_response(get_by_rid, client.get_by_rid)
        self.streaming_execute = core.with_raw_response(streaming_execute, client.streaming_execute)


class _QueryClientStreaming:
    def __init__(self, client: QueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...
        def streaming_execute(_: bytes): ...

        self.execute = core.with_streaming_response(execute, client.execute)
        self.get = core.with_streaming_response(get, client.get)
        self.get_by_rid = core.with_streaming_response(get_by_rid, client.get_by_rid)
        self.streaming_execute = core.with_streaming_response(
            streaming_execute, client.streaming_execute
        )


class AsyncQueryClient:
    """
    The API client for the Query Resource.

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
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.ExecuteQueryResponse]:
        """
        Executes a Query using the given parameters. By default, this executes the latest version of the query.

        This endpoint is maintained for backward compatibility only.

        For all new implementations, use the `streamingExecute` endpoint, which supports all function types
        and provides enhanced functionality.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and all workflows may not be supported.
        :type transaction_id: Optional[TransactionId]
        :param version:
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
        preview: typing.Optional[core_models.PreviewMode] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.Query]:
        """
        Gets a specific query type with the given RID.By default, this gets the latest version of the query.

        :param rid:
        :type rid: FunctionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version:
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[functions_models.Query]

        :raises GetByRidQueriesPermissionDenied: Could not getByRid the Query.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body=functions_models.GetByRidQueriesRequest(
                    rid=rid,
                    version=version,
                ),
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByRidQueriesPermissionDenied": functions_errors.GetByRidQueriesPermissionDenied,
                },
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
        ontology: typing.Optional[ontologies_models.OntologyIdentifier] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        transaction_id: typing.Optional[functions_models.TransactionId] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Executes a Query using the given parameters, returning results as an NDJSON stream. By default, this executes the latest version of the query.

        This endpoint supports all Query functions. The endpoint name 'streamingExecute' refers to the NDJSON
        streaming response format. Both streaming and non-streaming functions can use this endpoint.
        Non-streaming functions return a single-line NDJSON response, while streaming functions return multi-line NDJSON responses.
        This is the recommended endpoint for all query execution.

        The response is returned as a binary stream in NDJSON (Newline Delimited JSON) format, where each line
        is a StreamingExecuteQueryResponse containing either a data batch or an error.

        For a function returning a list of 5 records with a batch size of 3, the response stream would contain
        two lines. The first line contains the first 3 items, and the second line contains the remaining 2 items:

        ```
        {"type":"data","value":[{"productId":"SKU-001","price":29.99},{"productId":"SKU-002","price":49.99},{"productId":"SKU-003","price":19.99}]}
        {"type":"data","value":[{"productId":"SKU-004","price":39.99},{"productId":"SKU-005","price":59.99}]}
        ```

        Each line is a separate JSON object followed by a newline character. Clients should parse the stream
        line-by-line to process results as they arrive. If an error occurs during execution, the stream will
        contain an error line:

        ```
        {"type":"error","errorCode":"INVALID_ARGUMENT","errorName":"QueryRuntimeError","errorInstanceId":"3f8a9c7b-2e4d-4a1f-9b8c-7d6e5f4a3b2c","errorDescription":"Division by zero","parameters":{}}
        ```

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param attribution:
        :type attribution: Optional[Attribution]
        :param ontology: Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function.
        :type ontology: Optional[OntologyIdentifier]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
        :param transaction_id: The ID of a transaction to read from. Transactions are an experimental feature and all workflows may not be supported.
        :type transaction_id: Optional[TransactionId]
        :param version:
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]

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
                    "Accept": "application/octet-stream",
                },
                body=functions_models.StreamingExecuteQueryRequest(
                    ontology=ontology,
                    parameters=parameters,
                    version=version,
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={
                    "StreamingExecuteQueryPermissionDenied": functions_errors.StreamingExecuteQueryPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncQueryClientRaw:
    def __init__(self, client: AsyncQueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...
        def streaming_execute(_: bytes): ...

        self.execute = core.async_with_raw_response(execute, client.execute)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_by_rid = core.async_with_raw_response(get_by_rid, client.get_by_rid)
        self.streaming_execute = core.async_with_raw_response(
            streaming_execute, client.streaming_execute
        )


class _AsyncQueryClientStreaming:
    def __init__(self, client: AsyncQueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...
        def streaming_execute(_: bytes): ...

        self.execute = core.async_with_streaming_response(execute, client.execute)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_by_rid = core.async_with_streaming_response(get_by_rid, client.get_by_rid)
        self.streaming_execute = core.async_with_streaming_response(
            streaming_execute, client.streaming_execute
        )
