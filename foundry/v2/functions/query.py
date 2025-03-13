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

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.functions import errors as functions_errors
from foundry.v2.functions import models as functions_models


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
        self.with_streaming_response = _QueryClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _QueryClientRaw(auth=auth, hostname=hostname, config=config)

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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> functions_models.ExecuteQueryResponse:
        """
        Executes a Query using the given parameters.

        Optional parameters do not need to be supplied.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
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
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            functions_models.ParameterId,
                            typing.Optional[functions_models.DataValue],
                        ],
                    },
                ),
                response_type=functions_models.ExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteQueryPermissionDenied": functions_errors.ExecuteQueryPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        query_api_name: functions_models.QueryApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> functions_models.Query:
        """
        Gets a specific query type with the given API name.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
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
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_by_rid(
        self,
        *,
        rid: functions_models.FunctionRid,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> functions_models.Query:
        """
        Gets a specific query type with the given RID.

        :param rid:
        :type rid: FunctionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
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
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "rid": functions_models.FunctionRid,
                    },
                ),
                response_type=functions_models.Query,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[functions_models.ExecuteQueryResponse]:
        """
        Executes a Query using the given parameters.

        Optional parameters do not need to be supplied.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[functions_models.ExecuteQueryResponse]

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
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            functions_models.ParameterId,
                            typing.Optional[functions_models.DataValue],
                        ],
                    },
                ),
                response_type=functions_models.ExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteQueryPermissionDenied": functions_errors.ExecuteQueryPermissionDenied,
                },
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[functions_models.Query]:
        """
        Gets a specific query type with the given API name.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[functions_models.Query]

        :raises QueryNotFound: The given Query could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "QueryNotFound": functions_errors.QueryNotFound,
                },
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[functions_models.Query]:
        """
        Gets a specific query type with the given RID.

        :param rid:
        :type rid: FunctionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[functions_models.Query]

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
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "rid": functions_models.FunctionRid,
                    },
                ),
                response_type=functions_models.Query,
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
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[functions_models.ExecuteQueryResponse]:
        """
        Executes a Query using the given parameters.

        Optional parameters do not need to be supplied.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[functions_models.ExecuteQueryResponse]

        :raises ExecuteQueryPermissionDenied: Could not execute the Query.
        """

        return self._api_client.stream_api(
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
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parameters": parameters,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            functions_models.ParameterId,
                            typing.Optional[functions_models.DataValue],
                        ],
                    },
                ),
                response_type=functions_models.ExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ExecuteQueryPermissionDenied": functions_errors.ExecuteQueryPermissionDenied,
                },
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[functions_models.Query]:
        """
        Gets a specific query type with the given API name.

        :param query_api_name:
        :type query_api_name: QueryApiName
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[functions_models.Query]

        :raises QueryNotFound: The given Query could not be found.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
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
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "QueryNotFound": functions_errors.QueryNotFound,
                },
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[functions_models.Query]:
        """
        Gets a specific query type with the given RID.

        :param rid:
        :type rid: FunctionRid
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[functions_models.Query]

        :raises GetByRidQueriesPermissionDenied: Could not getByRid the Query.
        """

        return self._api_client.stream_api(
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
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "rid": functions_models.FunctionRid,
                    },
                ),
                response_type=functions_models.Query,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetByRidQueriesPermissionDenied": functions_errors.GetByRidQueriesPermissionDenied,
                },
            ),
        )
