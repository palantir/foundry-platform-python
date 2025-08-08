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
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> functions_models.ExecuteQueryResponse:
        """
        Executes a Query using the given parameters. By default, this executes the latest version of the query.

        Optional parameters do not need to be supplied.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
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
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                    "version": version,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            functions_models.ParameterId,
                            typing.Optional[functions_models.DataValue],
                        ],
                        "version": typing.Optional[functions_models.FunctionVersion],
                    },
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
                body_type=None,
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
                body={
                    "rid": rid,
                    "version": version,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "rid": functions_models.FunctionRid,
                        "version": typing.Optional[functions_models.FunctionVersion],
                    },
                ),
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByRidQueriesPermissionDenied": functions_errors.GetByRidQueriesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _QueryClientRaw:
    def __init__(self, client: QueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...

        self.execute = core.with_raw_response(execute, client.execute)
        self.get = core.with_raw_response(get, client.get)
        self.get_by_rid = core.with_raw_response(get_by_rid, client.get_by_rid)


class _QueryClientStreaming:
    def __init__(self, client: QueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...

        self.execute = core.with_streaming_response(execute, client.execute)
        self.get = core.with_streaming_response(get, client.get)
        self.get_by_rid = core.with_streaming_response(get_by_rid, client.get_by_rid)


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
        preview: typing.Optional[core_models.PreviewMode] = None,
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        version: typing.Optional[functions_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[functions_models.ExecuteQueryResponse]:
        """
        Executes a Query using the given parameters. By default, this executes the latest version of the query.

        Optional parameters do not need to be supplied.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param trace_parent:
        :type trace_parent: Optional[TraceParent]
        :param trace_state:
        :type trace_state: Optional[TraceState]
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
                },
                path_params={
                    "queryApiName": query_api_name,
                },
                header_params={
                    "traceParent": trace_parent,
                    "traceState": trace_state,
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                    "version": version,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            functions_models.ParameterId,
                            typing.Optional[functions_models.DataValue],
                        ],
                        "version": typing.Optional[functions_models.FunctionVersion],
                    },
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
                body_type=None,
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
                body={
                    "rid": rid,
                    "version": version,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "rid": functions_models.FunctionRid,
                        "version": typing.Optional[functions_models.FunctionVersion],
                    },
                ),
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByRidQueriesPermissionDenied": functions_errors.GetByRidQueriesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncQueryClientRaw:
    def __init__(self, client: AsyncQueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...

        self.execute = core.async_with_raw_response(execute, client.execute)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_by_rid = core.async_with_raw_response(get_by_rid, client.get_by_rid)


class _AsyncQueryClientStreaming:
    def __init__(self, client: AsyncQueryClient) -> None:
        def execute(_: functions_models.ExecuteQueryResponse): ...
        def get(_: functions_models.Query): ...
        def get_by_rid(_: functions_models.Query): ...

        self.execute = core.async_with_streaming_response(execute, client.execute)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_by_rid = core.async_with_streaming_response(get_by_rid, client.get_by_rid)
