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


class OntologyObjectClient:
    """
    The API client for the OntologyObject Resource.

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

        self.with_streaming_response = _OntologyObjectClientStreaming(self)
        self.with_raw_response = _OntologyObjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        aggregation: typing.List[ontologies_models.Aggregation],
        group_by: typing.List[ontologies_models.AggregationGroupBy],
        query: typing.Optional[ontologies_models.SearchJsonQuery] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.AggregateObjectsResponse:
        """
        Perform functions on object fields in the specified ontology and object type.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the objects.
        :type ontology_rid: OntologyRid
        :param object_type: The type of the object to aggregate on.
        :type object_type: ObjectTypeApiName
        :param aggregation:
        :type aggregation: List[Aggregation]
        :param group_by:
        :type group_by: List[AggregationGroupBy]
        :param query:
        :type query: Optional[SearchJsonQuery]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.AggregateObjectsResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "query": query,
                    "groupBy": group_by,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[ontologies_models.Aggregation],
                        "query": typing.Optional[ontologies_models.SearchJsonQuery],
                        "groupBy": typing.List[ontologies_models.AggregationGroupBy],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponse,
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
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        *,
        properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.OntologyObject:
        """
        Gets a specific object with the given primary key.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the object. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the requested object. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param properties: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.OntologyObject
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}",
                query_params={
                    "properties": properties,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.OntologyObject,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_linked_object(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        link_type: ontologies_models.LinkTypeApiName,
        linked_object_primary_key: ontologies_models.PropertyValueEscapedString,
        *,
        properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.OntologyObject:
        """
        Get a specific linked object that originates from another object. If there is no link between the two objects,
        LinkedObjectNotFound is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the object. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object from which the links originate. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object from which the link originates. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param link_type: The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param linked_object_primary_key: The primary key of the requested linked object. To look up the expected primary key for your object type, use the `Get object type` endpoint (passing the linked object type) or the **Ontology Manager**.
        :type linked_object_primary_key: PropertyValueEscapedString
        :param properties: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.OntologyObject
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}",
                query_params={
                    "properties": properties,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "linkType": link_type,
                    "linkedObjectPrimaryKey": linked_object_primary_key,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.OntologyObject,
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
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        order_by: typing.Optional[ontologies_models.OrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[ontologies_models.OntologyObject]:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](https://palantir.com/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the objects. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param order_by:
        :type order_by: Optional[OrderBy]
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param properties: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.OntologyObject]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}",
                query_params={
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "properties": properties,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_linked_objects(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        link_type: ontologies_models.LinkTypeApiName,
        *,
        order_by: typing.Optional[ontologies_models.OrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[ontologies_models.OntologyObject]:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](https://palantir.com/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the objects. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object from which the links originate. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param link_type: The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param order_by:
        :type order_by: Optional[OrderBy]
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param properties: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[ontologies_models.OntologyObject]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}",
                query_params={
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "properties": properties,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListLinkedObjectsResponse,
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
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        fields: typing.List[ontologies_models.PropertyApiName],
        query: ontologies_models.SearchJsonQuery,
        order_by: typing.Optional[ontologies_models.SearchOrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> ontologies_models.SearchObjectsResponse:
        """
        Search for objects in the specified ontology and object type. The request body is used
        to filter objects based on the specified query. The supported queries are:

        | Query type            | Description                                                                       | Supported Types                 |
        |----------|-----------------------------------------------------------------------------------|---------------------------------|
        | lt       | The provided property is less than the provided value.                            | number, string, date, timestamp |
        | gt       | The provided property is greater than the provided value.                         | number, string, date, timestamp |
        | lte      | The provided property is less than or equal to the provided value.                | number, string, date, timestamp |
        | gte      | The provided property is greater than or equal to the provided value.             | number, string, date, timestamp |
        | eq       | The provided property is exactly equal to the provided value.                     | number, string, date, timestamp |
        | isNull   | The provided property is (or is not) null.                                        | all                             |
        | contains | The provided property contains the provided value.                                | array                           |
        | not      | The sub-query does not match.                                                     | N/A (applied on a query)        |
        | and      | All the sub-queries match.                                                        | N/A (applied on queries)        |
        | or       | At least one of the sub-queries match.                                            | N/A (applied on queries)        |
        | prefix   | The provided property starts with the provided term.                              | string                          |
        | phrase   | The provided property contains the provided term as a substring.                  | string                          |
        | anyTerm  | The provided property contains at least one of the terms separated by whitespace. | string                          |
        | allTerms | The provided property contains all the terms separated by whitespace.             | string                          |

        Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
        Partial terms are not matched by terms filters except where explicitly noted.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the objects.
        :type ontology_rid: OntologyRid
        :param object_type: The type of the requested objects.
        :type object_type: ObjectTypeApiName
        :param fields: The API names of the object type properties to include in the response.
        :type fields: List[PropertyApiName]
        :param query:
        :type query: SearchJsonQuery
        :param order_by:
        :type order_by: Optional[SearchOrderBy]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ontologies_models.SearchObjectsResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/search",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "query": query,
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "fields": fields,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": ontologies_models.SearchJsonQuery,
                        "orderBy": typing.Optional[ontologies_models.SearchOrderBy],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "fields": typing.List[ontologies_models.PropertyApiName],
                    },
                ),
                response_type=ontologies_models.SearchObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _OntologyObjectClientRaw:
    def __init__(self, client: OntologyObjectClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponse): ...
        def get(_: ontologies_models.OntologyObject): ...
        def get_linked_object(_: ontologies_models.OntologyObject): ...
        def list(_: ontologies_models.ListObjectsResponse): ...
        def list_linked_objects(_: ontologies_models.ListLinkedObjectsResponse): ...
        def search(_: ontologies_models.SearchObjectsResponse): ...

        self.aggregate = core.with_raw_response(aggregate, client.aggregate)
        self.get = core.with_raw_response(get, client.get)
        self.get_linked_object = core.with_raw_response(get_linked_object, client.get_linked_object)
        self.list = core.with_raw_response(list, client.list)
        self.list_linked_objects = core.with_raw_response(
            list_linked_objects, client.list_linked_objects
        )
        self.search = core.with_raw_response(search, client.search)


class _OntologyObjectClientStreaming:
    def __init__(self, client: OntologyObjectClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponse): ...
        def get(_: ontologies_models.OntologyObject): ...
        def get_linked_object(_: ontologies_models.OntologyObject): ...
        def list(_: ontologies_models.ListObjectsResponse): ...
        def list_linked_objects(_: ontologies_models.ListLinkedObjectsResponse): ...
        def search(_: ontologies_models.SearchObjectsResponse): ...

        self.aggregate = core.with_streaming_response(aggregate, client.aggregate)
        self.get = core.with_streaming_response(get, client.get)
        self.get_linked_object = core.with_streaming_response(
            get_linked_object, client.get_linked_object
        )
        self.list = core.with_streaming_response(list, client.list)
        self.list_linked_objects = core.with_streaming_response(
            list_linked_objects, client.list_linked_objects
        )
        self.search = core.with_streaming_response(search, client.search)


class AsyncOntologyObjectClient:
    """
    The API client for the OntologyObject Resource.

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

        self.with_streaming_response = _AsyncOntologyObjectClientStreaming(self)
        self.with_raw_response = _AsyncOntologyObjectClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def aggregate(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        aggregation: typing.List[ontologies_models.Aggregation],
        group_by: typing.List[ontologies_models.AggregationGroupBy],
        query: typing.Optional[ontologies_models.SearchJsonQuery] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.AggregateObjectsResponse]:
        """
        Perform functions on object fields in the specified ontology and object type.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the objects.
        :type ontology_rid: OntologyRid
        :param object_type: The type of the object to aggregate on.
        :type object_type: ObjectTypeApiName
        :param aggregation:
        :type aggregation: List[Aggregation]
        :param group_by:
        :type group_by: List[AggregationGroupBy]
        :param query:
        :type query: Optional[SearchJsonQuery]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.AggregateObjectsResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "query": query,
                    "groupBy": group_by,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": typing.List[ontologies_models.Aggregation],
                        "query": typing.Optional[ontologies_models.SearchJsonQuery],
                        "groupBy": typing.List[ontologies_models.AggregationGroupBy],
                    },
                ),
                response_type=ontologies_models.AggregateObjectsResponse,
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
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        *,
        properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.OntologyObject]:
        """
        Gets a specific object with the given primary key.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the object. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the requested object. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param properties: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.OntologyObject]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}",
                query_params={
                    "properties": properties,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.OntologyObject,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_linked_object(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        link_type: ontologies_models.LinkTypeApiName,
        linked_object_primary_key: ontologies_models.PropertyValueEscapedString,
        *,
        properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.OntologyObject]:
        """
        Get a specific linked object that originates from another object. If there is no link between the two objects,
        LinkedObjectNotFound is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the object. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object from which the links originate. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object from which the link originates. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param link_type: The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param linked_object_primary_key: The primary key of the requested linked object. To look up the expected primary key for your object type, use the `Get object type` endpoint (passing the linked object type) or the **Ontology Manager**.
        :type linked_object_primary_key: PropertyValueEscapedString
        :param properties: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.OntologyObject]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}",
                query_params={
                    "properties": properties,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "linkType": link_type,
                    "linkedObjectPrimaryKey": linked_object_primary_key,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.OntologyObject,
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
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        order_by: typing.Optional[ontologies_models.OrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[ontologies_models.OntologyObject]:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](https://palantir.com/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the objects. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param order_by:
        :type order_by: Optional[OrderBy]
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param properties: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.OntologyObject]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}",
                query_params={
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "properties": properties,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list_linked_objects(
        self,
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        primary_key: ontologies_models.PropertyValueEscapedString,
        link_type: ontologies_models.LinkTypeApiName,
        *,
        order_by: typing.Optional[ontologies_models.OrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[ontologies_models.OntologyObject]:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](https://palantir.com/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the objects. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object from which the links originate. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param primary_key: The primary key of the object from which the links originate. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**.
        :type primary_key: PropertyValueEscapedString
        :param link_type: The API name of the link that exists between the object and the requested objects. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param order_by:
        :type order_by: Optional[OrderBy]
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](https://palantir.com/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param properties: The properties of the object type that should be included in the response. Omit this parameter to get all the properties.
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[ontologies_models.OntologyObject]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}",
                query_params={
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "properties": properties,
                },
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ontologies_models.ListLinkedObjectsResponse,
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
        ontology_rid: ontologies_models.OntologyRid,
        object_type: ontologies_models.ObjectTypeApiName,
        *,
        fields: typing.List[ontologies_models.PropertyApiName],
        query: ontologies_models.SearchJsonQuery,
        order_by: typing.Optional[ontologies_models.SearchOrderBy] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[ontologies_models.SearchObjectsResponse]:
        """
        Search for objects in the specified ontology and object type. The request body is used
        to filter objects based on the specified query. The supported queries are:

        | Query type            | Description                                                                       | Supported Types                 |
        |----------|-----------------------------------------------------------------------------------|---------------------------------|
        | lt       | The provided property is less than the provided value.                            | number, string, date, timestamp |
        | gt       | The provided property is greater than the provided value.                         | number, string, date, timestamp |
        | lte      | The provided property is less than or equal to the provided value.                | number, string, date, timestamp |
        | gte      | The provided property is greater than or equal to the provided value.             | number, string, date, timestamp |
        | eq       | The provided property is exactly equal to the provided value.                     | number, string, date, timestamp |
        | isNull   | The provided property is (or is not) null.                                        | all                             |
        | contains | The provided property contains the provided value.                                | array                           |
        | not      | The sub-query does not match.                                                     | N/A (applied on a query)        |
        | and      | All the sub-queries match.                                                        | N/A (applied on queries)        |
        | or       | At least one of the sub-queries match.                                            | N/A (applied on queries)        |
        | prefix   | The provided property starts with the provided term.                              | string                          |
        | phrase   | The provided property contains the provided term as a substring.                  | string                          |
        | anyTerm  | The provided property contains at least one of the terms separated by whitespace. | string                          |
        | allTerms | The provided property contains all the terms separated by whitespace.             | string                          |

        Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
        Partial terms are not matched by terms filters except where explicitly noted.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the objects.
        :type ontology_rid: OntologyRid
        :param object_type: The type of the requested objects.
        :type object_type: ObjectTypeApiName
        :param fields: The API names of the object type properties to include in the response.
        :type fields: List[PropertyApiName]
        :param query:
        :type query: SearchJsonQuery
        :param order_by:
        :type order_by: Optional[SearchOrderBy]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[ontologies_models.SearchObjectsResponse]
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/search",
                query_params={},
                path_params={
                    "ontologyRid": ontology_rid,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "query": query,
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "fields": fields,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": ontologies_models.SearchJsonQuery,
                        "orderBy": typing.Optional[ontologies_models.SearchOrderBy],
                        "pageSize": typing.Optional[core_models.PageSize],
                        "pageToken": typing.Optional[core_models.PageToken],
                        "fields": typing.List[ontologies_models.PropertyApiName],
                    },
                ),
                response_type=ontologies_models.SearchObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncOntologyObjectClientRaw:
    def __init__(self, client: AsyncOntologyObjectClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponse): ...
        def get(_: ontologies_models.OntologyObject): ...
        def get_linked_object(_: ontologies_models.OntologyObject): ...
        def list(_: ontologies_models.ListObjectsResponse): ...
        def list_linked_objects(_: ontologies_models.ListLinkedObjectsResponse): ...
        def search(_: ontologies_models.SearchObjectsResponse): ...

        self.aggregate = core.async_with_raw_response(aggregate, client.aggregate)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_linked_object = core.async_with_raw_response(
            get_linked_object, client.get_linked_object
        )
        self.list = core.async_with_raw_response(list, client.list)
        self.list_linked_objects = core.async_with_raw_response(
            list_linked_objects, client.list_linked_objects
        )
        self.search = core.async_with_raw_response(search, client.search)


class _AsyncOntologyObjectClientStreaming:
    def __init__(self, client: AsyncOntologyObjectClient) -> None:
        def aggregate(_: ontologies_models.AggregateObjectsResponse): ...
        def get(_: ontologies_models.OntologyObject): ...
        def get_linked_object(_: ontologies_models.OntologyObject): ...
        def list(_: ontologies_models.ListObjectsResponse): ...
        def list_linked_objects(_: ontologies_models.ListLinkedObjectsResponse): ...
        def search(_: ontologies_models.SearchObjectsResponse): ...

        self.aggregate = core.async_with_streaming_response(aggregate, client.aggregate)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_linked_object = core.async_with_streaming_response(
            get_linked_object, client.get_linked_object
        )
        self.list = core.async_with_streaming_response(list, client.list)
        self.list_linked_objects = core.async_with_streaming_response(
            list_linked_objects, client.list_linked_objects
        )
        self.search = core.async_with_streaming_response(search, client.search)
