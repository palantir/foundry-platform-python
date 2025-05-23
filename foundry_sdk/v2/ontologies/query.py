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
        ontology: ontologies_models.OntologyIdentifier,
        query_api_name: ontologies_models.QueryApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        version: typing.Optional[ontologies_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ExecuteQueryResponse:
        """
        Executes a Query using the given parameters.

        Optional parameters do not need to be supplied.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param query_api_name: The API name of the Query to execute.
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param version: The version of the Query to execute.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ExecuteQueryResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/queries/{queryApiName}/execute",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                    "version": version,
                },
                path_params={
                    "ontology": ontology,
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
        ontology: ontologies_models.OntologyIdentifier,
        query_api_name: ontologies_models.QueryApiName,
        *,
        parameters: typing.Dict[
            ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]
        ],
        artifact_repository: typing.Optional[ontologies_models.ArtifactRepositoryRid] = None,
        package_name: typing.Optional[ontologies_models.SdkPackageName] = None,
        version: typing.Optional[ontologies_models.FunctionVersion] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ExecuteQueryResponse]:
        """
        Executes a Query using the given parameters.

        Optional parameters do not need to be supplied.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param query_api_name: The API name of the Query to execute.
        :type query_api_name: QueryApiName
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param artifact_repository: The repository associated with a marketplace installation.
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: The package name of the generated SDK.
        :type package_name: Optional[SdkPackageName]
        :param version: The version of the Query to execute.
        :type version: Optional[FunctionVersion]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ExecuteQueryResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/queries/{queryApiName}/execute",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                    "version": version,
                },
                path_params={
                    "ontology": ontology,
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
