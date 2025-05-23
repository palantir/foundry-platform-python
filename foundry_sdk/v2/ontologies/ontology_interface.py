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

        self.with_streaming_response = _OntologyInterfaceClientStreaming(self)
        self.with_raw_response = _OntologyInterfaceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        aggregation: typing.List[ontologies_models.AggregationV2],
        group_by: typing.List[ontologies_models.AggregationGroupByV2],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[ontologies_models.SearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
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
        :type aggregation: List[AggregationV2]
        :param group_by:
        :type group_by: List[AggregationGroupByV2]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[SearchJsonQueryV2]
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
                        "aggregation": typing.List[ontologies_models.AggregationV2],
                        "where": typing.Optional[ontologies_models.SearchJsonQueryV2],
                        "groupBy": typing.List[ontologies_models.AggregationGroupByV2],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
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
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
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
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
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
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        augmented_properties: typing.Dict[
            ontologies_models.ObjectTypeApiName, typing.List[ontologies_models.PropertyApiName]
        ],
        augmented_shared_property_types: typing.Dict[
            ontologies_models.InterfaceTypeApiName,
            typing.List[ontologies_models.SharedPropertyTypeApiName],
        ],
        other_interface_types: typing.List[ontologies_models.InterfaceTypeApiName],
        selected_object_types: typing.List[ontologies_models.ObjectTypeApiName],
        selected_shared_property_types: typing.List[ontologies_models.SharedPropertyTypeApiName],
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[ontologies_models.SearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.SearchObjectsResponseV2:
        """
        :::callout{theme=warning title=Warning}
          This endpoint will be removed once TS OSDK is updated to use `objectSets/loadObjects` with interface object
          sets.
        :::
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Search for objects in the specified ontology and interface type. Any properties specified in the "where" or
        "orderBy" parameters must be shared property type API names defined on the interface. The following search
        queries are supported:

        | Query type                              | Description                                                                                                       | Supported Types                 |
        |-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------|
        | lt                                      | The provided property is less than the provided value.                                                            | number, string, date, timestamp |
        | gt                                      | The provided property is greater than the provided value.                                                         | number, string, date, timestamp |
        | lte                                     | The provided property is less than or equal to the provided value.                                                | number, string, date, timestamp |
        | gte                                     | The provided property is greater than or equal to the provided value.                                             | number, string, date, timestamp |
        | eq                                      | The provided property is exactly equal to the provided value.                                                     | number, string, date, timestamp |
        | isNull                                  | The provided property is (or is not) null.                                                                        | all                             |
        | contains                                | The provided property contains the provided value.                                                                | array                           |
        | not                                     | The sub-query does not match.                                                                                     | N/A (applied on a query)        |
        | and                                     | All the sub-queries match.                                                                                        | N/A (applied on queries)        |
        | or                                      | At least one of the sub-queries match.                                                                            | N/A (applied on queries)        |
        | startsWith                              | The provided property starts with the provided term.                                                              | string                          |
        | containsAllTermsInOrderPrefixLastTerm   | The provided property contains all the terms provided in order. The last term can be a partial prefix match.      | string                          |
        | containsAllTermsInOrder                 | The provided property contains the provided terms as a substring.                                                 | string                          |
        | containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
        | containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |

        Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
        Partial terms are not matched by terms filters except where explicitly noted.

        Attempting to use an unsupported query will result in a validation error. Third-party applications using this
        endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param interface_type: The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
        :type interface_type: InterfaceTypeApiName
        :param augmented_properties: A map from object type API name to a list of property type API names. For each returned object, if the  object’s object type is a key in the map, then we augment the response for that object type with the list  of properties specified in the value.
        :type augmented_properties: Dict[ObjectTypeApiName, List[PropertyApiName]]
        :param augmented_shared_property_types: A map from interface type API name to a list of shared property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.
        :type augmented_shared_property_types: Dict[InterfaceTypeApiName, List[SharedPropertyTypeApiName]]
        :param other_interface_types: A list of interface type API names. Object types must implement all the mentioned interfaces in order to be  included in the response.
        :type other_interface_types: List[InterfaceTypeApiName]
        :param selected_object_types: A list of object type API names that should be included in the response. If non-empty, object types that are not mentioned will not be included in the response even if they implement the specified interface. Omit the  parameter to include all object types.
        :type selected_object_types: List[ObjectTypeApiName]
        :param selected_shared_property_types: A list of shared property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.
        :type selected_shared_property_types: List[SharedPropertyTypeApiName]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[SearchJsonQueryV2]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.SearchObjectsResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/interfaces/{interfaceType}/search",
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
                    "where": where,
                    "orderBy": order_by,
                    "augmentedProperties": augmented_properties,
                    "augmentedSharedPropertyTypes": augmented_shared_property_types,
                    "selectedSharedPropertyTypes": selected_shared_property_types,
                    "selectedObjectTypes": selected_object_types,
                    "otherInterfaceTypes": other_interface_types,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Optional[ontologies_models.SearchJsonQueryV2],
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "augmentedProperties": typing.Dict[
                            ontologies_models.ObjectTypeApiName,
                            typing.List[ontologies_models.PropertyApiName],
                        ],
                        "augmentedSharedPropertyTypes": typing.Dict[
                            ontologies_models.InterfaceTypeApiName,
                            typing.List[ontologies_models.SharedPropertyTypeApiName],
                        ],
                        "selectedSharedPropertyTypes": typing.List[
                            ontologies_models.SharedPropertyTypeApiName
                        ],
                        "selectedObjectTypes": typing.List[ontologies_models.ObjectTypeApiName],
                        "otherInterfaceTypes": typing.List[ontologies_models.InterfaceTypeApiName],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
                ),
                response_type=ontologies_models.SearchObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OntologyInterfaceClientRaw:
    def __init__(self, client: OntologyInterfaceClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def get(_: ontologies_models.InterfaceType): ...
        def list(_: ontologies_models.ListInterfaceTypesResponse): ...
        def search(_: ontologies_models.SearchObjectsResponseV2): ...

        self.aggregate = core.with_raw_response(aggregate, client.aggregate)
        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)
        self.search = core.with_raw_response(search, client.search)


class _OntologyInterfaceClientStreaming:
    def __init__(self, client: OntologyInterfaceClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def get(_: ontologies_models.InterfaceType): ...
        def list(_: ontologies_models.ListInterfaceTypesResponse): ...
        def search(_: ontologies_models.SearchObjectsResponseV2): ...

        self.aggregate = core.with_streaming_response(aggregate, client.aggregate)
        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)
        self.search = core.with_streaming_response(search, client.search)


class AsyncOntologyInterfaceClient:
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
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncOntologyInterfaceClientStreaming(self)
        self.with_raw_response = _AsyncOntologyInterfaceClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        aggregation: typing.List[ontologies_models.AggregationV2],
        group_by: typing.List[ontologies_models.AggregationGroupByV2],
        accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[ontologies_models.SearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.AggregateObjectsResponseV2]:
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
        :type aggregation: List[AggregationV2]
        :param group_by:
        :type group_by: List[AggregationGroupByV2]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[SearchJsonQueryV2]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.AggregateObjectsResponseV2]
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
                        "aggregation": typing.List[ontologies_models.AggregationV2],
                        "where": typing.Optional[ontologies_models.SearchJsonQueryV2],
                        "groupBy": typing.List[ontologies_models.AggregationGroupByV2],
                        "accuracy": typing.Optional[ontologies_models.AggregationAccuracyRequest],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
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
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.InterfaceType]:
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
        :rtype: typing.Awaitable[ontologies_models.InterfaceType]
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
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[ontologies_models.InterfaceType]:
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
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.InterfaceType]
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
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        ontology: ontologies_models.OntologyIdentifier,
        interface_type: ontologies_models.InterfaceTypeApiName,
        *,
        augmented_properties: typing.Dict[
            ontologies_models.ObjectTypeApiName, typing.List[ontologies_models.PropertyApiName]
        ],
        augmented_shared_property_types: typing.Dict[
            ontologies_models.InterfaceTypeApiName,
            typing.List[ontologies_models.SharedPropertyTypeApiName],
        ],
        other_interface_types: typing.List[ontologies_models.InterfaceTypeApiName],
        selected_object_types: typing.List[ontologies_models.ObjectTypeApiName],
        selected_shared_property_types: typing.List[ontologies_models.SharedPropertyTypeApiName],
        order_by: typing.Optional[ontologies_models.SearchOrderByV2] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[ontologies_models.SearchJsonQueryV2] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.SearchObjectsResponseV2]:
        """
        :::callout{theme=warning title=Warning}
          This endpoint will be removed once TS OSDK is updated to use `objectSets/loadObjects` with interface object
          sets.
        :::
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Search for objects in the specified ontology and interface type. Any properties specified in the "where" or
        "orderBy" parameters must be shared property type API names defined on the interface. The following search
        queries are supported:

        | Query type                              | Description                                                                                                       | Supported Types                 |
        |-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------|
        | lt                                      | The provided property is less than the provided value.                                                            | number, string, date, timestamp |
        | gt                                      | The provided property is greater than the provided value.                                                         | number, string, date, timestamp |
        | lte                                     | The provided property is less than or equal to the provided value.                                                | number, string, date, timestamp |
        | gte                                     | The provided property is greater than or equal to the provided value.                                             | number, string, date, timestamp |
        | eq                                      | The provided property is exactly equal to the provided value.                                                     | number, string, date, timestamp |
        | isNull                                  | The provided property is (or is not) null.                                                                        | all                             |
        | contains                                | The provided property contains the provided value.                                                                | array                           |
        | not                                     | The sub-query does not match.                                                                                     | N/A (applied on a query)        |
        | and                                     | All the sub-queries match.                                                                                        | N/A (applied on queries)        |
        | or                                      | At least one of the sub-queries match.                                                                            | N/A (applied on queries)        |
        | startsWith                              | The provided property starts with the provided term.                                                              | string                          |
        | containsAllTermsInOrderPrefixLastTerm   | The provided property contains all the terms provided in order. The last term can be a partial prefix match.      | string                          |
        | containsAllTermsInOrder                 | The provided property contains the provided terms as a substring.                                                 | string                          |
        | containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
        | containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |

        Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
        Partial terms are not matched by terms filters except where explicitly noted.

        Attempting to use an unsupported query will result in a validation error. Third-party applications using this
        endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param interface_type: The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**.
        :type interface_type: InterfaceTypeApiName
        :param augmented_properties: A map from object type API name to a list of property type API names. For each returned object, if the  object’s object type is a key in the map, then we augment the response for that object type with the list  of properties specified in the value.
        :type augmented_properties: Dict[ObjectTypeApiName, List[PropertyApiName]]
        :param augmented_shared_property_types: A map from interface type API name to a list of shared property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object  type with the list of properties specified in the value.
        :type augmented_shared_property_types: Dict[InterfaceTypeApiName, List[SharedPropertyTypeApiName]]
        :param other_interface_types: A list of interface type API names. Object types must implement all the mentioned interfaces in order to be  included in the response.
        :type other_interface_types: List[InterfaceTypeApiName]
        :param selected_object_types: A list of object type API names that should be included in the response. If non-empty, object types that are not mentioned will not be included in the response even if they implement the specified interface. Omit the  parameter to include all object types.
        :type selected_object_types: List[ObjectTypeApiName]
        :param selected_shared_property_types: A list of shared property type API names of the interface type that should be included in the response.  Omit this parameter to include all properties of the interface type in the response.
        :type selected_shared_property_types: List[SharedPropertyTypeApiName]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: A boolean flag that, when set to true, enables the use of beta features in preview mode.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[SearchJsonQueryV2]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.SearchObjectsResponseV2]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/interfaces/{interfaceType}/search",
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
                    "where": where,
                    "orderBy": order_by,
                    "augmentedProperties": augmented_properties,
                    "augmentedSharedPropertyTypes": augmented_shared_property_types,
                    "selectedSharedPropertyTypes": selected_shared_property_types,
                    "selectedObjectTypes": selected_object_types,
                    "otherInterfaceTypes": other_interface_types,
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Optional[ontologies_models.SearchJsonQueryV2],
                        "orderBy": typing.Optional[ontologies_models.SearchOrderByV2],
                        "augmentedProperties": typing.Dict[
                            ontologies_models.ObjectTypeApiName,
                            typing.List[ontologies_models.PropertyApiName],
                        ],
                        "augmentedSharedPropertyTypes": typing.Dict[
                            ontologies_models.InterfaceTypeApiName,
                            typing.List[ontologies_models.SharedPropertyTypeApiName],
                        ],
                        "selectedSharedPropertyTypes": typing.List[
                            ontologies_models.SharedPropertyTypeApiName
                        ],
                        "selectedObjectTypes": typing.List[ontologies_models.ObjectTypeApiName],
                        "otherInterfaceTypes": typing.List[ontologies_models.InterfaceTypeApiName],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                    },
                ),
                response_type=ontologies_models.SearchObjectsResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOntologyInterfaceClientRaw:
    def __init__(self, client: AsyncOntologyInterfaceClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def get(_: ontologies_models.InterfaceType): ...
        def list(_: ontologies_models.ListInterfaceTypesResponse): ...
        def search(_: ontologies_models.SearchObjectsResponseV2): ...

        self.aggregate = core.async_with_raw_response(aggregate, client.aggregate)
        self.get = core.async_with_raw_response(get, client.get)
        self.list = core.async_with_raw_response(list, client.list)
        self.search = core.async_with_raw_response(search, client.search)


class _AsyncOntologyInterfaceClientStreaming:
    def __init__(self, client: AsyncOntologyInterfaceClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponseV2): ...
        def get(_: ontologies_models.InterfaceType): ...
        def list(_: ontologies_models.ListInterfaceTypesResponse): ...
        def search(_: ontologies_models.SearchObjectsResponseV2): ...

        self.aggregate = core.async_with_streaming_response(aggregate, client.aggregate)
        self.get = core.async_with_streaming_response(get, client.get)
        self.list = core.async_with_streaming_response(list, client.list)
        self.search = core.async_with_streaming_response(search, client.search)
