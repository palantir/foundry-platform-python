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

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.ontologies.models._aggregate_objects_response_v2 import (
    AggregateObjectsResponseV2,
)  # NOQA
from foundry.v2.ontologies.models._aggregation_accuracy_request import (
    AggregationAccuracyRequest,
)  # NOQA
from foundry.v2.ontologies.models._aggregation_group_by_v2_dict import (
    AggregationGroupByV2Dict,
)  # NOQA
from foundry.v2.ontologies.models._aggregation_v2_dict import AggregationV2Dict
from foundry.v2.ontologies.models._artifact_repository_rid import ArtifactRepositoryRid
from foundry.v2.ontologies.models._count_objects_response_v2 import CountObjectsResponseV2  # NOQA
from foundry.v2.ontologies.models._list_objects_response_v2 import ListObjectsResponseV2
from foundry.v2.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.ontologies.models._ontology_identifier import OntologyIdentifier
from foundry.v2.ontologies.models._ontology_object_v2 import OntologyObjectV2
from foundry.v2.ontologies.models._order_by import OrderBy
from foundry.v2.ontologies.models._property_api_name import PropertyApiName
from foundry.v2.ontologies.models._property_value_escaped_string import (
    PropertyValueEscapedString,
)  # NOQA
from foundry.v2.ontologies.models._sdk_package_name import SdkPackageName
from foundry.v2.ontologies.models._search_json_query_v2_dict import SearchJsonQueryV2Dict  # NOQA
from foundry.v2.ontologies.models._search_objects_response_v2 import SearchObjectsResponseV2  # NOQA
from foundry.v2.ontologies.models._search_order_by_v2_dict import SearchOrderByV2Dict
from foundry.v2.ontologies.models._selected_property_api_name import SelectedPropertyApiName  # NOQA


class OntologyObjectClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def aggregate(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        aggregation: List[AggregationV2Dict],
        group_by: List[AggregationGroupByV2Dict],
        accuracy: Optional[AggregationAccuracyRequest] = None,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        where: Optional[SearchJsonQueryV2Dict] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> AggregateObjectsResponseV2:
        """
        Perform functions on object fields in the specified ontology and object type.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param aggregation:
        :type aggregation: List[AggregationV2Dict]
        :param group_by:
        :type group_by: List[AggregationGroupByV2Dict]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param where:
        :type where: Optional[SearchJsonQueryV2Dict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AggregateObjectsResponseV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/aggregate",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": List[AggregationV2Dict],
                        "where": Optional[SearchJsonQueryV2Dict],
                        "groupBy": List[AggregationGroupByV2Dict],
                        "accuracy": Optional[AggregationAccuracyRequest],
                    },
                ),
                response_type=AggregateObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def count(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
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

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/count",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=CountObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[pydantic.StrictBool] = None,
        package_name: Optional[SdkPackageName] = None,
        select: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
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
        :type exclude_rid: Optional[pydantic.StrictBool]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param select: select
        :type select: Optional[List[SelectedPropertyApiName]]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: OntologyObjectV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "excludeRid": exclude_rid,
                    "packageName": package_name,
                    "select": select,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                    "primaryKey": primary_key,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=OntologyObjectV2,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[pydantic.StrictBool] = None,
        order_by: Optional[OrderBy] = None,
        package_name: Optional[SdkPackageName] = None,
        page_size: Optional[PageSize] = None,
        select: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
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
        :type exclude_rid: Optional[pydantic.StrictBool]
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

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "excludeRid": exclude_rid,
                    "orderBy": order_by,
                    "packageName": package_name,
                    "pageSize": page_size,
                    "select": select,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[pydantic.StrictBool] = None,
        order_by: Optional[OrderBy] = None,
        package_name: Optional[SdkPackageName] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        select: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
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
        :type exclude_rid: Optional[pydantic.StrictBool]
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

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}",
                query_params={
                    "artifactRepository": artifact_repository,
                    "excludeRid": exclude_rid,
                    "orderBy": order_by,
                    "packageName": package_name,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "select": select,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def search(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        select: List[PropertyApiName],
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[pydantic.StrictBool] = None,
        order_by: Optional[SearchOrderByV2Dict] = None,
        package_name: Optional[SdkPackageName] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        where: Optional[SearchJsonQueryV2Dict] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
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
        :param select: The API names of the object type properties to include in the response.
        :type select: List[PropertyApiName]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[pydantic.StrictBool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2Dict]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param where:
        :type where: Optional[SearchJsonQueryV2Dict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SearchObjectsResponseV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/search",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "objectType": object_type,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "orderBy": order_by,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "select": select,
                    "excludeRid": exclude_rid,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": Optional[SearchJsonQueryV2Dict],
                        "orderBy": Optional[SearchOrderByV2Dict],
                        "pageSize": Optional[PageSize],
                        "pageToken": Optional[PageToken],
                        "select": List[PropertyApiName],
                        "excludeRid": Optional[pydantic.StrictBool],
                    },
                ),
                response_type=SearchObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )
