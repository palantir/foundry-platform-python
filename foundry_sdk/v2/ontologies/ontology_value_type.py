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
from foundry_sdk.v2.ontologies import models as ontologies_models


class OntologyValueTypeClient:
    """
    The API client for the OntologyValueType Resource.

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

        self.with_streaming_response = _OntologyValueTypeClientStreaming(self)
        self.with_raw_response = _OntologyValueTypeClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        value_type: ontologies_models.ValueTypeApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.OntologyValueType:
        """
        Gets a specific value type with the given API name.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param value_type: The API name of the value type. To find the API name, use the **List value types** endpoint or check the **Ontology Manager**.
        :type value_type: ValueTypeApiName
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.OntologyValueType
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/valueTypes/{valueType}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "valueType": value_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.OntologyValueType,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.ListOntologyValueTypesResponse:
        """
        Lists the latest versions of the value types for the given Ontology.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ListOntologyValueTypesResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/valueTypes",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListOntologyValueTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OntologyValueTypeClientRaw:
    def __init__(self, client: OntologyValueTypeClient) -> None:
        def get(_: ontologies_models.OntologyValueType): ...
        def list(_: ontologies_models.ListOntologyValueTypesResponse): ...

        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)


class _OntologyValueTypeClientStreaming:
    def __init__(self, client: OntologyValueTypeClient) -> None:
        def get(_: ontologies_models.OntologyValueType): ...
        def list(_: ontologies_models.ListOntologyValueTypesResponse): ...

        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)


class AsyncOntologyValueTypeClient:
    """
    The API client for the OntologyValueType Resource.

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

        self.with_streaming_response = _AsyncOntologyValueTypeClientStreaming(self)
        self.with_raw_response = _AsyncOntologyValueTypeClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        value_type: ontologies_models.ValueTypeApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.OntologyValueType]:
        """
        Gets a specific value type with the given API name.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param value_type: The API name of the value type. To find the API name, use the **List value types** endpoint or check the **Ontology Manager**.
        :type value_type: ValueTypeApiName
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.OntologyValueType]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/valueTypes/{valueType}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "valueType": value_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.OntologyValueType,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.ListOntologyValueTypesResponse]:
        """
        Lists the latest versions of the value types for the given Ontology.

        :param ontology:
        :type ontology: OntologyIdentifier
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.ListOntologyValueTypesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/valueTypes",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListOntologyValueTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOntologyValueTypeClientRaw:
    def __init__(self, client: AsyncOntologyValueTypeClient) -> None:
        def get(_: ontologies_models.OntologyValueType): ...
        def list(_: ontologies_models.ListOntologyValueTypesResponse): ...

        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)


class _AsyncOntologyValueTypeClientStreaming:
    def __init__(self, client: AsyncOntologyValueTypeClient) -> None:
        def get(_: ontologies_models.OntologyValueType): ...
        def list(_: ontologies_models.ListOntologyValueTypesResponse): ...

        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
