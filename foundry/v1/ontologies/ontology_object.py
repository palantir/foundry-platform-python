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


from __future__ import annotations

import warnings
from functools import cached_property
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v1.core.models._page_size import PageSize
from foundry.v1.core.models._page_token import PageToken
from foundry.v1.ontologies.models._aggregate_objects_response import (
    AggregateObjectsResponse,
)  # NOQA
from foundry.v1.ontologies.models._aggregation import Aggregation
from foundry.v1.ontologies.models._aggregation_dict import AggregationDict
from foundry.v1.ontologies.models._aggregation_group_by import AggregationGroupBy
from foundry.v1.ontologies.models._aggregation_group_by_dict import AggregationGroupByDict  # NOQA
from foundry.v1.ontologies.models._link_type_api_name import LinkTypeApiName
from foundry.v1.ontologies.models._list_linked_objects_response import (
    ListLinkedObjectsResponse,
)  # NOQA
from foundry.v1.ontologies.models._list_objects_response import ListObjectsResponse
from foundry.v1.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v1.ontologies.models._ontology_object import OntologyObject
from foundry.v1.ontologies.models._ontology_rid import OntologyRid
from foundry.v1.ontologies.models._order_by import OrderBy
from foundry.v1.ontologies.models._property_api_name import PropertyApiName
from foundry.v1.ontologies.models._property_value_escaped_string import (
    PropertyValueEscapedString,
)  # NOQA
from foundry.v1.ontologies.models._search_json_query import SearchJsonQuery
from foundry.v1.ontologies.models._search_json_query_dict import SearchJsonQueryDict
from foundry.v1.ontologies.models._search_objects_response import SearchObjectsResponse
from foundry.v1.ontologies.models._search_order_by import SearchOrderBy
from foundry.v1.ontologies.models._search_order_by_dict import SearchOrderByDict
from foundry.v1.ontologies.models._selected_property_api_name import SelectedPropertyApiName  # NOQA


class OntologyObjectClient:
    """
    The API client for the OntologyObject Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
        self.with_streaming_response = _OntologyObjectClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _OntologyObjectClientRaw(
            auth=auth, hostname=hostname, config=config
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def aggregate(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        aggregation: List[Union[Aggregation, AggregationDict]],
        group_by: List[Union[AggregationGroupBy, AggregationGroupByDict]],
        query: Optional[Union[SearchJsonQuery, SearchJsonQueryDict]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> AggregateObjectsResponse:
        """
        Perform functions on object fields in the specified ontology and object type.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param aggregation:
        :type aggregation: List[Union[Aggregation, AggregationDict]]
        :param group_by:
        :type group_by: List[Union[AggregationGroupBy, AggregationGroupByDict]]
        :param query:
        :type query: Optional[Union[SearchJsonQuery, SearchJsonQueryDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AggregateObjectsResponse
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": List[Union[Aggregation, AggregationDict]],
                        "query": Optional[Union[SearchJsonQuery, SearchJsonQueryDict]],
                        "groupBy": List[Union[AggregationGroupBy, AggregationGroupByDict]],
                    },
                ),
                response_type=AggregateObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        *,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> OntologyObject:
        """
        Gets a specific object with the given primary key.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: OntologyObject
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=OntologyObject,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_linked_object(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        linked_object_primary_key: PropertyValueEscapedString,
        *,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> OntologyObject:
        """
        Get a specific linked object that originates from another object. If there is no link between the two objects,
        LinkedObjectNotFound is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param linked_object_primary_key: linkedObjectPrimaryKey
        :type linked_object_primary_key: PropertyValueEscapedString
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: OntologyObject
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=OntologyObject,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[OntologyObject]:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[OntologyObject]
        """

        return self._api_client.iterate_api(
            RequestInfo(
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
                response_type=ListObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list_linked_objects(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[OntologyObject]:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[OntologyObject]
        """

        return self._api_client.iterate_api(
            RequestInfo(
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
                response_type=ListLinkedObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListObjectsResponse:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListObjectsResponse
        """

        warnings.warn(
            "The client.ontologies.OntologyObject.page(...) method has been deprecated. Please use client.ontologies.OntologyObject.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page_linked_objects(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListLinkedObjectsResponse:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListLinkedObjectsResponse
        """

        warnings.warn(
            "The client.ontologies.OntologyObject.page_linked_objects(...) method has been deprecated. Please use client.ontologies.OntologyObject.list_linked_objects(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListLinkedObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def search(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        fields: List[PropertyApiName],
        query: Union[SearchJsonQuery, SearchJsonQueryDict],
        order_by: Optional[Union[SearchOrderBy, SearchOrderByDict]] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> SearchObjectsResponse:
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

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param fields: The API names of the object type properties to include in the response.
        :type fields: List[PropertyApiName]
        :param query:
        :type query: Union[SearchJsonQuery, SearchJsonQueryDict]
        :param order_by:
        :type order_by: Optional[Union[SearchOrderBy, SearchOrderByDict]]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SearchObjectsResponse
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": Union[SearchJsonQuery, SearchJsonQueryDict],
                        "orderBy": Optional[Union[SearchOrderBy, SearchOrderByDict]],
                        "pageSize": Optional[PageSize],
                        "pageToken": Optional[PageToken],
                        "fields": List[PropertyApiName],
                    },
                ),
                response_type=SearchObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        ).decode()


class _OntologyObjectClientRaw:
    """
    The API client for the OntologyObject Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def aggregate(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        aggregation: List[Union[Aggregation, AggregationDict]],
        group_by: List[Union[AggregationGroupBy, AggregationGroupByDict]],
        query: Optional[Union[SearchJsonQuery, SearchJsonQueryDict]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[AggregateObjectsResponse]:
        """
        Perform functions on object fields in the specified ontology and object type.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param aggregation:
        :type aggregation: List[Union[Aggregation, AggregationDict]]
        :param group_by:
        :type group_by: List[Union[AggregationGroupBy, AggregationGroupByDict]]
        :param query:
        :type query: Optional[Union[SearchJsonQuery, SearchJsonQueryDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[AggregateObjectsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": List[Union[Aggregation, AggregationDict]],
                        "query": Optional[Union[SearchJsonQuery, SearchJsonQueryDict]],
                        "groupBy": List[Union[AggregationGroupBy, AggregationGroupByDict]],
                    },
                ),
                response_type=AggregateObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        *,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[OntologyObject]:
        """
        Gets a specific object with the given primary key.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[OntologyObject]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=OntologyObject,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_linked_object(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        linked_object_primary_key: PropertyValueEscapedString,
        *,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[OntologyObject]:
        """
        Get a specific linked object that originates from another object. If there is no link between the two objects,
        LinkedObjectNotFound is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param linked_object_primary_key: linkedObjectPrimaryKey
        :type linked_object_primary_key: PropertyValueEscapedString
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[OntologyObject]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=OntologyObject,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListObjectsResponse]:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListObjectsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list_linked_objects(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListLinkedObjectsResponse]:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListLinkedObjectsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListLinkedObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListObjectsResponse]:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListObjectsResponse]
        """

        warnings.warn(
            "The client.ontologies.OntologyObject.page(...) method has been deprecated. Please use client.ontologies.OntologyObject.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page_linked_objects(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[ListLinkedObjectsResponse]:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[ListLinkedObjectsResponse]
        """

        warnings.warn(
            "The client.ontologies.OntologyObject.page_linked_objects(...) method has been deprecated. Please use client.ontologies.OntologyObject.list_linked_objects(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListLinkedObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def search(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        fields: List[PropertyApiName],
        query: Union[SearchJsonQuery, SearchJsonQueryDict],
        order_by: Optional[Union[SearchOrderBy, SearchOrderByDict]] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[SearchObjectsResponse]:
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

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param fields: The API names of the object type properties to include in the response.
        :type fields: List[PropertyApiName]
        :param query:
        :type query: Union[SearchJsonQuery, SearchJsonQueryDict]
        :param order_by:
        :type order_by: Optional[Union[SearchOrderBy, SearchOrderByDict]]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[SearchObjectsResponse]
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": Union[SearchJsonQuery, SearchJsonQueryDict],
                        "orderBy": Optional[Union[SearchOrderBy, SearchOrderByDict]],
                        "pageSize": Optional[PageSize],
                        "pageToken": Optional[PageToken],
                        "fields": List[PropertyApiName],
                    },
                ),
                response_type=SearchObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )


class _OntologyObjectClientStreaming:
    """
    The API client for the OntologyObject Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def aggregate(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        aggregation: List[Union[Aggregation, AggregationDict]],
        group_by: List[Union[AggregationGroupBy, AggregationGroupByDict]],
        query: Optional[Union[SearchJsonQuery, SearchJsonQueryDict]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[AggregateObjectsResponse]:
        """
        Perform functions on object fields in the specified ontology and object type.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param aggregation:
        :type aggregation: List[Union[Aggregation, AggregationDict]]
        :param group_by:
        :type group_by: List[Union[AggregationGroupBy, AggregationGroupByDict]]
        :param query:
        :type query: Optional[Union[SearchJsonQuery, SearchJsonQueryDict]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[AggregateObjectsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": List[Union[Aggregation, AggregationDict]],
                        "query": Optional[Union[SearchJsonQuery, SearchJsonQueryDict]],
                        "groupBy": List[Union[AggregationGroupBy, AggregationGroupByDict]],
                    },
                ),
                response_type=AggregateObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        *,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[OntologyObject]:
        """
        Gets a specific object with the given primary key.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[OntologyObject]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=OntologyObject,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get_linked_object(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        linked_object_primary_key: PropertyValueEscapedString,
        *,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[OntologyObject]:
        """
        Get a specific linked object that originates from another object. If there is no link between the two objects,
        LinkedObjectNotFound is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param linked_object_primary_key: linkedObjectPrimaryKey
        :type linked_object_primary_key: PropertyValueEscapedString
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[OntologyObject]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=OntologyObject,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListObjectsResponse]:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListObjectsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def list_linked_objects(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListLinkedObjectsResponse]:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListLinkedObjectsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListLinkedObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListObjectsResponse]:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListObjectsResponse]
        """

        warnings.warn(
            "The client.ontologies.OntologyObject.page(...) method has been deprecated. Please use client.ontologies.OntologyObject.list(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def page_linked_objects(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[ListLinkedObjectsResponse]:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/ontology-object-basics#filter-objects) for details.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[ListLinkedObjectsResponse]
        """

        warnings.warn(
            "The client.ontologies.OntologyObject.page_linked_objects(...) method has been deprecated. Please use client.ontologies.OntologyObject.list_linked_objects(...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=ListLinkedObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def search(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        fields: List[PropertyApiName],
        query: Union[SearchJsonQuery, SearchJsonQueryDict],
        order_by: Optional[Union[SearchOrderBy, SearchOrderByDict]] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[SearchObjectsResponse]:
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

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param fields: The API names of the object type properties to include in the response.
        :type fields: List[PropertyApiName]
        :param query:
        :type query: Union[SearchJsonQuery, SearchJsonQueryDict]
        :param order_by:
        :type order_by: Optional[Union[SearchOrderBy, SearchOrderByDict]]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[SearchObjectsResponse]
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": Union[SearchJsonQuery, SearchJsonQueryDict],
                        "orderBy": Optional[Union[SearchOrderBy, SearchOrderByDict]],
                        "pageSize": Optional[PageSize],
                        "pageToken": Optional[PageToken],
                        "fields": List[PropertyApiName],
                    },
                ),
                response_type=SearchObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
            ),
        )
