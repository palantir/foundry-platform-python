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
from foundry_sdk.v1.core import models as core_models
from foundry_sdk.v1.ontologies import models as ontologies_models


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
        ontology_rid: ontologies_models.OntologyRid,
        query_api_name: ontologies_models.QueryApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ExecuteQueryResponse:
        """
        Executes a Query using the given parameters. Optional parameters do not need to be supplied.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the Query. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param query_api_name: The API name of the Query to execute.
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param trace_parent: The W3C trace parent header included in the request.
        :type trace_parent: Optional[TraceParent]
        :param trace_state: The W3C trace state header included in the request.
        :type trace_state: Optional[TraceState]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ExecuteQueryResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
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
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            ontologies_models.ParameterId,
                            typing.Optional[ontologies_models.DataValue],
                        ],
                    },
                ),
                response_type=ontologies_models.ExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _QueryClientRaw:
    def __init__(self, client: QueryClient) -> None:
        def execute(_: ontologies_models.ExecuteQueryResponse): ...

        self.execute = core.with_raw_response(execute, client.execute)


class _QueryClientStreaming:
    def __init__(self, client: QueryClient) -> None:
        def execute(_: ontologies_models.ExecuteQueryResponse): ...

        self.execute = core.with_streaming_response(execute, client.execute)


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
        ontology_rid: ontologies_models.OntologyRid,
        query_api_name: ontologies_models.QueryApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        trace_parent: typing.Optional[core_models.TraceParent] = None,
        trace_state: typing.Optional[core_models.TraceState] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ExecuteQueryResponse]:
        """
        Executes a Query using the given parameters. Optional parameters do not need to be supplied.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the Query. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param query_api_name: The API name of the Query to execute.
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param trace_parent: The W3C trace parent header included in the request.
        :type trace_parent: Optional[TraceParent]
        :param trace_state: The W3C trace state header included in the request.
        :type trace_state: Optional[TraceState]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ExecuteQueryResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
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
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parameters": typing.Dict[
                            ontologies_models.ParameterId,
                            typing.Optional[ontologies_models.DataValue],
                        ],
                    },
                ),
                response_type=ontologies_models.ExecuteQueryResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncQueryClientRaw:
    def __init__(self, client: AsyncQueryClient) -> None:
        def execute(_: ontologies_models.ExecuteQueryResponse): ...

        self.execute = core.async_with_raw_response(execute, client.execute)


class _AsyncQueryClientStreaming:
    def __init__(self, client: AsyncQueryClient) -> None:
        def execute(_: ontologies_models.ExecuteQueryResponse): ...

        self.execute = core.async_with_streaming_response(execute, client.execute)
