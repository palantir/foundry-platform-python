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
from pydantic import StrictBool
from pydantic import StrictInt
from pydantic import validate_call

from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v2.models._aggregate_objects_request_v2 import AggregateObjectsRequestV2
from foundry.v2.models._aggregate_objects_request_v2_dict import (
    AggregateObjectsRequestV2Dict,
)  # NOQA
from foundry.v2.models._aggregate_objects_response_v2 import AggregateObjectsResponseV2
from foundry.v2.models._artifact_repository_rid import ArtifactRepositoryRid
from foundry.v2.models._count_objects_response_v2 import CountObjectsResponseV2
from foundry.v2.models._list_objects_response_v2 import ListObjectsResponseV2
from foundry.v2.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.models._ontology_identifier import OntologyIdentifier
from foundry.v2.models._ontology_object_v2 import OntologyObjectV2
from foundry.v2.models._order_by import OrderBy
from foundry.v2.models._page_size import PageSize
from foundry.v2.models._page_token import PageToken
from foundry.v2.models._property_value_escaped_string import PropertyValueEscapedString
from foundry.v2.models._sdk_package_name import SdkPackageName
from foundry.v2.models._search_objects_request_v2 import SearchObjectsRequestV2
from foundry.v2.models._search_objects_request_v2_dict import SearchObjectsRequestV2Dict
from foundry.v2.models._search_objects_response_v2 import SearchObjectsResponseV2
from foundry.v2.models._selected_property_api_name import SelectedPropertyApiName


class OntologyObjectResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def aggregate(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        aggregate_objects_request_v2: Union[
            AggregateObjectsRequestV2, AggregateObjectsRequestV2Dict
        ],
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> AggregateObjectsResponseV2:
        """
        Perform functions on object fields in the specified ontology and object type.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param aggregate_objects_request_v2: Body of the request
        :type aggregate_objects_request_v2: Union[AggregateObjectsRequestV2, AggregateObjectsRequestV2Dict]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AggregateObjectsResponseV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = aggregate_objects_request_v2
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/aggregate",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[AggregateObjectsRequestV2, AggregateObjectsRequestV2Dict],
                response_type=AggregateObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def count(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> CountObjectsResponseV2:
        """
        Returns a count of the objects of the given object type.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: CountObjectsResponseV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/count",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=CountObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[StrictBool] = None,
        package_name: Optional[SdkPackageName] = None,
        select: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> OntologyObjectV2:
        """
        Gets a specific object with the given primary key.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: excludeRid
        :type exclude_rid: Optional[StrictBool]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param select: select
        :type select: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: OntologyObjectV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["artifactRepository"] = artifact_repository

        _query_params["excludeRid"] = exclude_rid

        _query_params["packageName"] = package_name

        _query_params["select"] = select

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _path_params["primaryKey"] = primary_key

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=OntologyObjectV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def list(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[StrictBool] = None,
        order_by: Optional[OrderBy] = None,
        package_name: Optional[SdkPackageName] = None,
        page_size: Optional[PageSize] = None,
        select: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ResourceIterator[OntologyObjectV2]:
        """
        Lists the objects for the given Ontology and object type.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: excludeRid
        :type exclude_rid: Optional[StrictBool]
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param select: select
        :type select: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[OntologyObjectV2]
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["artifactRepository"] = artifact_repository

        _query_params["excludeRid"] = exclude_rid

        _query_params["orderBy"] = order_by

        _query_params["packageName"] = package_name

        _query_params["pageSize"] = page_size

        _query_params["select"] = select

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def page(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[StrictBool] = None,
        order_by: Optional[OrderBy] = None,
        package_name: Optional[SdkPackageName] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        select: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListObjectsResponseV2:
        """
        Lists the objects for the given Ontology and object type.

        Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
        repeated objects in the response pages.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Each page may be smaller or larger than the requested page size. However, it
        is guaranteed that if there are more results available, at least one result will be present
        in the response.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: excludeRid
        :type exclude_rid: Optional[StrictBool]
        :param order_by: orderBy
        :type order_by: Optional[OrderBy]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param select: select
        :type select: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListObjectsResponseV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["artifactRepository"] = artifact_repository

        _query_params["excludeRid"] = exclude_rid

        _query_params["orderBy"] = order_by

        _query_params["packageName"] = package_name

        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _query_params["select"] = select

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def search(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        search_objects_request_v2: Union[SearchObjectsRequestV2, SearchObjectsRequestV2Dict],
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> SearchObjectsResponseV2:
        """
        Search for objects in the specified ontology and object type. The request body is used
        to filter objects based on the specified query. The supported queries are:

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
        | startsWith                              | The provided property starts with the provided value.                                                             | string                          |
        | containsAllTermsInOrderPrefixLastTerm   | The provided property contains all the terms provided in order. The last term can be a partial prefix match.      | string                          |
        | containsAllTermsInOrder                 | The provided property contains the provided value as a substring.                                                 | string                          |
        | containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
        | containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param search_objects_request_v2: Body of the request
        :type search_objects_request_v2: Union[SearchObjectsRequestV2, SearchObjectsRequestV2Dict]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SearchObjectsResponseV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = search_objects_request_v2
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/search",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[SearchObjectsRequestV2, SearchObjectsRequestV2Dict],
                response_type=SearchObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )
