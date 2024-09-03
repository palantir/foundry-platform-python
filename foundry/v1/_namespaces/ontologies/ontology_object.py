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

from typing import Annotated
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call

from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v1.models._aggregate_objects_request import AggregateObjectsRequest
from foundry.v1.models._aggregate_objects_request_dict import AggregateObjectsRequestDict  # NOQA
from foundry.v1.models._aggregate_objects_response import AggregateObjectsResponse
from foundry.v1.models._link_type_api_name import LinkTypeApiName
from foundry.v1.models._list_linked_objects_response import ListLinkedObjectsResponse
from foundry.v1.models._list_objects_response import ListObjectsResponse
from foundry.v1.models._object_type_api_name import ObjectTypeApiName
from foundry.v1.models._ontology_object import OntologyObject
from foundry.v1.models._ontology_rid import OntologyRid
from foundry.v1.models._order_by import OrderBy
from foundry.v1.models._page_size import PageSize
from foundry.v1.models._page_token import PageToken
from foundry.v1.models._property_value_escaped_string import PropertyValueEscapedString
from foundry.v1.models._search_objects_request import SearchObjectsRequest
from foundry.v1.models._search_objects_request_dict import SearchObjectsRequestDict
from foundry.v1.models._search_objects_response import SearchObjectsResponse
from foundry.v1.models._selected_property_api_name import SelectedPropertyApiName


class OntologyObjectResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def aggregate(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        aggregate_objects_request: Union[AggregateObjectsRequest, AggregateObjectsRequestDict],
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> AggregateObjectsResponse:
        """
        Perform functions on object fields in the specified ontology and object type.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param aggregate_objects_request: Body of the request
        :type aggregate_objects_request: Union[AggregateObjectsRequest, AggregateObjectsRequestDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AggregateObjectsResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = aggregate_objects_request

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[AggregateObjectsRequest, AggregateObjectsRequestDict],
                response_type=AggregateObjectsResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        *,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["properties"] = properties

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _path_params["primaryKey"] = primary_key

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=OntologyObject,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
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
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["properties"] = properties

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _path_params["primaryKey"] = primary_key

        _path_params["linkType"] = link_type

        _path_params["linkedObjectPrimaryKey"] = linked_object_primary_key

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=OntologyObject,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def list(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        order_by: Optional[OrderBy] = None,
        page_size: Optional[PageSize] = None,
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ResourceIterator[OntologyObject]:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

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
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[OntologyObject]
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["orderBy"] = order_by

        _query_params["pageSize"] = page_size

        _query_params["properties"] = properties

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListObjectsResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
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
        properties: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ResourceIterator[OntologyObject]:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

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
        :param properties: properties
        :type properties: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[OntologyObject]
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["orderBy"] = order_by

        _query_params["pageSize"] = page_size

        _query_params["properties"] = properties

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _path_params["primaryKey"] = primary_key

        _path_params["linkType"] = link_type

        _header_params["Accept"] = "application/json"

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListLinkedObjectsResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
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
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListObjectsResponse:
        """
        Lists the objects for the given Ontology and object type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["orderBy"] = order_by

        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _query_params["properties"] = properties

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListObjectsResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
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
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListLinkedObjectsResponse:
        """
        Lists the linked objects for a specific object and the given link type.

        This endpoint supports filtering objects.
        See the [Filtering Objects documentation](/docs/foundry/api/ontology-resources/objects/object-basics/#filtering-objects) for details.

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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["orderBy"] = order_by

        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _query_params["properties"] = properties

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _path_params["primaryKey"] = primary_key

        _path_params["linkType"] = link_type

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListLinkedObjectsResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def search(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        search_objects_request: Union[SearchObjectsRequest, SearchObjectsRequestDict],
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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
        | prefix   | The provided property starts with the provided value.                             | string                          |
        | phrase   | The provided property contains the provided value as a substring.                 | string                          |
        | anyTerm  | The provided property contains at least one of the terms separated by whitespace. | string                          |
        | allTerms | The provided property contains all the terms separated by whitespace.             | string                          |                                                                            |

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param search_objects_request: Body of the request
        :type search_objects_request: Union[SearchObjectsRequest, SearchObjectsRequestDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SearchObjectsResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = search_objects_request

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/objects/{objectType}/search",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[SearchObjectsRequest, SearchObjectsRequestDict],
                response_type=SearchObjectsResponse,
                request_timeout=request_timeout,
            ),
        )
