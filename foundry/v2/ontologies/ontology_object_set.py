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

from pydantic import Field
from pydantic import StrictBool
from pydantic import StrictInt
from pydantic import validate_call
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
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
from foundry.v2.ontologies.models._create_temporary_object_set_response_v2 import (
    CreateTemporaryObjectSetResponseV2,
)  # NOQA
from foundry.v2.ontologies.models._load_object_set_response_v2 import (
    LoadObjectSetResponseV2,
)  # NOQA
from foundry.v2.ontologies.models._object_set import ObjectSet
from foundry.v2.ontologies.models._object_set_dict import ObjectSetDict
from foundry.v2.ontologies.models._object_set_rid import ObjectSetRid
from foundry.v2.ontologies.models._ontology_identifier import OntologyIdentifier
from foundry.v2.ontologies.models._sdk_package_name import SdkPackageName
from foundry.v2.ontologies.models._search_order_by_v2_dict import SearchOrderByV2Dict
from foundry.v2.ontologies.models._selected_property_api_name import SelectedPropertyApiName  # NOQA


class OntologyObjectSetClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def aggregate(
        self,
        ontology: OntologyIdentifier,
        *,
        aggregation: List[AggregationV2Dict],
        group_by: List[AggregationGroupByV2Dict],
        object_set: ObjectSetDict,
        accuracy: Optional[AggregationAccuracyRequest] = None,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> AggregateObjectsResponseV2:
        """
        Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param aggregation:
        :type aggregation: List[AggregationV2Dict]
        :param group_by:
        :type group_by: List[AggregationGroupByV2Dict]
        :param object_set:
        :type object_set: ObjectSetDict
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: AggregateObjectsResponseV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/aggregate",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "aggregation": aggregation,
                    "objectSet": object_set,
                    "groupBy": group_by,
                    "accuracy": accuracy,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "aggregation": List[AggregationV2Dict],
                        "objectSet": ObjectSetDict,
                        "groupBy": List[AggregationGroupByV2Dict],
                        "accuracy": Optional[AggregationAccuracyRequest],
                    },
                ),
                response_type=AggregateObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def create_temporary(
        self,
        ontology: OntologyIdentifier,
        *,
        object_set: ObjectSetDict,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> CreateTemporaryObjectSetResponseV2:
        """
        Creates a temporary `ObjectSet` from the given definition.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSetDict
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: CreateTemporaryObjectSetResponseV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/createTemporary",
                query_params={},
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "objectSet": object_set,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "objectSet": ObjectSetDict,
                    },
                ),
                response_type=CreateTemporaryObjectSetResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        ontology: OntologyIdentifier,
        object_set_rid: ObjectSetRid,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ObjectSet:
        """
        Gets the definition of the `ObjectSet` with the given RID.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_set_rid: objectSetRid
        :type object_set_rid: ObjectSetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ObjectSet
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectSets/{objectSetRid}",
                query_params={},
                path_params={
                    "ontology": ontology,
                    "objectSetRid": object_set_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ObjectSet,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def load(
        self,
        ontology: OntologyIdentifier,
        *,
        object_set: ObjectSetDict,
        select: List[SelectedPropertyApiName],
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        exclude_rid: Optional[StrictBool] = None,
        order_by: Optional[SearchOrderByV2Dict] = None,
        package_name: Optional[SdkPackageName] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> LoadObjectSetResponseV2:
        """
        Load the ontology objects present in the `ObjectSet` from the provided object set definition.

        For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
        are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

        Note that null value properties will not be returned.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_set:
        :type object_set: ObjectSetDict
        :param select:
        :type select: List[SelectedPropertyApiName]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param exclude_rid: A flag to exclude the retrieval of the `__rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2.
        :type exclude_rid: Optional[StrictBool]
        :param order_by:
        :type order_by: Optional[SearchOrderByV2Dict]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: LoadObjectSetResponseV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/loadObjects",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "objectSet": object_set,
                    "orderBy": order_by,
                    "select": select,
                    "pageToken": page_token,
                    "pageSize": page_size,
                    "excludeRid": exclude_rid,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "objectSet": ObjectSetDict,
                        "orderBy": Optional[SearchOrderByV2Dict],
                        "select": List[SelectedPropertyApiName],
                        "pageToken": Optional[PageToken],
                        "pageSize": Optional[PageSize],
                        "excludeRid": Optional[StrictBool],
                    },
                ),
                response_type=LoadObjectSetResponseV2,
                request_timeout=request_timeout,
            ),
        )
