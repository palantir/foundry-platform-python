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
import warnings

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.ontologies import models as ontologies_models


class OntologyInterfaceClient:
    """
    The API client for the OntologyInterface Resource.

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
        self.with_streaming_response = _OntologyInterfaceClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _OntologyInterfaceClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        aggregation: typing.List[
            typing.Union[ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict]
        ],
        group_by: typing.List[
            typing.Union[
                ontologies_models.AggregationGroupByV2, ontologies_models.AggregationGroupByV2Dict
            ]
        ],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[
            typing.Union[
                ontologies_models.SearchJsonQueryV2, ontologies_models.SearchJsonQueryV2Dict
            ]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.AggregateObjectsResponseV2:
        """
        :::callout{theme=warning title=Warning}
        This endpoint will be removed once TS OSDK is updated to use `objectSets/aggregate` with interface object
        sets.
        :::
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Perform functions on object fields in the specified ontology and of the specified interface type. Any
        properties specified in the query must be shared property type API names defined on the interface.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param interface_type: The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
        :type interface_type: InterfaceTypeApiName
        :param aggregation:
        :type aggregation: List[Union[AggregationV2, AggregationV2Dict]]
        :param group_by:
        :type group_by: List[Union[AggregationGroupByV2, AggregationGroupByV2Dict]]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[Union[SearchJsonQueryV2, SearchJsonQueryV2Dict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.AggregateObjectsResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/interfaces/{interfaceType}/aggregate",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "interfaceType": interface_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "where": where,
                    "groupBy": group_by,
                    "accuracy": accuracy,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[
                            typing.Union[
                                ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict
                            ]
                        ],
                        "where": typing.Optional[
                            typing.Union[
                                ontologies_models.SearchJsonQueryV2,
                                ontologies_models.SearchJsonQueryV2Dict,
                            ]
                        ],
                        "groupBy": typing.List[
                            typing.Union[
                                ontologies_models.AggregationGroupByV2,
                                ontologies_models.AggregationGroupByV2Dict,
                            ]
                        ],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.InterfaceType:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Gets a specific interface type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param interface_type: The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
        :type interface_type: InterfaceTypeApiName
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.InterfaceType
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes/{interfaceType}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "interfaceType": interface_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.InterfaceType,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ResourceIterator[ontologies_models.InterfaceType]:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Lists the interface types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.InterfaceType]
        """

        return self._api_client.iterate_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ontologies_models.ListInterfaceTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> ontologies_models.ListInterfaceTypesResponse:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Lists the interface types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.ListInterfaceTypesResponse
        """

        warnings.warn(
            "The client.ontologies.OntologyInterface.page(...) method has been deprecated. Please use client.ontologies.OntologyInterface.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ontologies_models.ListInterfaceTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _OntologyInterfaceClientRaw:
    """
    The API client for the OntologyInterface Resource.

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
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        aggregation: typing.List[
            typing.Union[ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict]
        ],
        group_by: typing.List[
            typing.Union[
                ontologies_models.AggregationGroupByV2, ontologies_models.AggregationGroupByV2Dict
            ]
        ],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[
            typing.Union[
                ontologies_models.SearchJsonQueryV2, ontologies_models.SearchJsonQueryV2Dict
            ]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.AggregateObjectsResponseV2]:
        """
        :::callout{theme=warning title=Warning}
        This endpoint will be removed once TS OSDK is updated to use `objectSets/aggregate` with interface object
        sets.
        :::
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Perform functions on object fields in the specified ontology and of the specified interface type. Any
        properties specified in the query must be shared property type API names defined on the interface.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param interface_type: The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
        :type interface_type: InterfaceTypeApiName
        :param aggregation:
        :type aggregation: List[Union[AggregationV2, AggregationV2Dict]]
        :param group_by:
        :type group_by: List[Union[AggregationGroupByV2, AggregationGroupByV2Dict]]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[Union[SearchJsonQueryV2, SearchJsonQueryV2Dict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.AggregateObjectsResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/interfaces/{interfaceType}/aggregate",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "interfaceType": interface_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "where": where,
                    "groupBy": group_by,
                    "accuracy": accuracy,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[
                            typing.Union[
                                ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict
                            ]
                        ],
                        "where": typing.Optional[
                            typing.Union[
                                ontologies_models.SearchJsonQueryV2,
                                ontologies_models.SearchJsonQueryV2Dict,
                            ]
                        ],
                        "groupBy": typing.List[
                            typing.Union[
                                ontologies_models.AggregationGroupByV2,
                                ontologies_models.AggregationGroupByV2Dict,
                            ]
                        ],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.InterfaceType]:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Gets a specific interface type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param interface_type: The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
        :type interface_type: InterfaceTypeApiName
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.InterfaceType]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes/{interfaceType}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "interfaceType": interface_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.InterfaceType,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.ListInterfaceTypesResponse]:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Lists the interface types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.ListInterfaceTypesResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ontologies_models.ListInterfaceTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[ontologies_models.ListInterfaceTypesResponse]:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Lists the interface types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[ontologies_models.ListInterfaceTypesResponse]
        """

        warnings.warn(
            "The client.ontologies.OntologyInterface.page(...) method has been deprecated. Please use client.ontologies.OntologyInterface.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ontologies_models.ListInterfaceTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _OntologyInterfaceClientStreaming:
    """
    The API client for the OntologyInterface Resource.

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
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        aggregation: typing.List[
            typing.Union[ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict]
        ],
        group_by: typing.List[
            typing.Union[
                ontologies_models.AggregationGroupByV2, ontologies_models.AggregationGroupByV2Dict
            ]
        ],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[
            typing.Union[
                ontologies_models.SearchJsonQueryV2, ontologies_models.SearchJsonQueryV2Dict
            ]
        ] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.AggregateObjectsResponseV2]:
        """
        :::callout{theme=warning title=Warning}
        This endpoint will be removed once TS OSDK is updated to use `objectSets/aggregate` with interface object
        sets.
        :::
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Perform functions on object fields in the specified ontology and of the specified interface type. Any
        properties specified in the query must be shared property type API names defined on the interface.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param interface_type: The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
        :type interface_type: InterfaceTypeApiName
        :param aggregation:
        :type aggregation: List[Union[AggregationV2, AggregationV2Dict]]
        :param group_by:
        :type group_by: List[Union[AggregationGroupByV2, AggregationGroupByV2Dict]]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[Union[SearchJsonQueryV2, SearchJsonQueryV2Dict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.AggregateObjectsResponseV2]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/interfaces/{interfaceType}/aggregate",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "interfaceType": interface_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "where": where,
                    "groupBy": group_by,
                    "accuracy": accuracy,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[
                            typing.Union[
                                ontologies_models.AggregationV2, ontologies_models.AggregationV2Dict
                            ]
                        ],
                        "where": typing.Optional[
                            typing.Union[
                                ontologies_models.SearchJsonQueryV2,
                                ontologies_models.SearchJsonQueryV2Dict,
                            ]
                        ],
                        "groupBy": typing.List[
                            typing.Union[
                                ontologies_models.AggregationGroupByV2,
                                ontologies_models.AggregationGroupByV2Dict,
                            ]
                        ],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.InterfaceType]:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Gets a specific interface type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param interface_type: The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
        :type interface_type: InterfaceTypeApiName
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.InterfaceType]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes/{interfaceType}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "ontology": ontology,
                    "interfaceType": interface_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.InterfaceType,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.ListInterfaceTypesResponse]:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Lists the interface types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.ListInterfaceTypesResponse]
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ontologies_models.ListInterfaceTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def page(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[ontologies_models.ListInterfaceTypesResponse]:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Lists the interface types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[ontologies_models.ListInterfaceTypesResponse]
        """

        warnings.warn(
            "The client.ontologies.OntologyInterface.page(...) method has been deprecated. Please use client.ontologies.OntologyInterface.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=ontologies_models.ListInterfaceTypesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
