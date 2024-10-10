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

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.ontologies.models._artifact_repository_rid import ArtifactRepositoryRid
from foundry.v2.ontologies.models._link_type_api_name import LinkTypeApiName
from foundry.v2.ontologies.models._list_linked_objects_response_v2 import (
    ListLinkedObjectsResponseV2,
)  # NOQA
from foundry.v2.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.ontologies.models._ontology_identifier import OntologyIdentifier
from foundry.v2.ontologies.models._ontology_object_v2 import OntologyObjectV2
from foundry.v2.ontologies.models._order_by import OrderBy
from foundry.v2.ontologies.models._property_value_escaped_string import (
    PropertyValueEscapedString,
)  # NOQA
from foundry.v2.ontologies.models._sdk_package_name import SdkPackageName
from foundry.v2.ontologies.models._selected_property_api_name import SelectedPropertyApiName  # NOQA


class LinkedObjectClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def get_linked_object(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        linked_object_primary_key: PropertyValueEscapedString,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[pydantic.StrictBool] = None,
        package_name: Optional[SdkPackageName] = None,
        select: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> OntologyObjectV2:
        """
        Get a specific linked object that originates from another object.

        If there is no link between the two objects, `LinkedObjectNotFound` is thrown.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param linked_object_primary_key: linkedObjectPrimaryKey
        :type linked_object_primary_key: PropertyValueEscapedString
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
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}",
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
                    "linkType": link_type,
                    "linkedObjectPrimaryKey": linked_object_primary_key,
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
    def list_linked_objects(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
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
        Lists the linked objects for a specific object and the given link type.

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
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
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
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}",
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
                    "primaryKey": primary_key,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListLinkedObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def page_linked_objects(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        primary_key: PropertyValueEscapedString,
        link_type: LinkTypeApiName,
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[pydantic.StrictBool] = None,
        order_by: Optional[OrderBy] = None,
        package_name: Optional[SdkPackageName] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        select: Optional[List[SelectedPropertyApiName]] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListLinkedObjectsResponseV2:
        """
        Lists the linked objects for a specific object and the given link type.

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
        :param primary_key: primaryKey
        :type primary_key: PropertyValueEscapedString
        :param link_type: linkType
        :type link_type: LinkTypeApiName
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
        :rtype: ListLinkedObjectsResponseV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}",
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
                    "primaryKey": primary_key,
                    "linkType": link_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListLinkedObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )
