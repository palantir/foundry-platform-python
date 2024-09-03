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
from typing import Optional
from typing import Union

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call

from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v2.models._aggregate_object_set_request_v2 import AggregateObjectSetRequestV2  # NOQA
from foundry.v2.models._aggregate_object_set_request_v2_dict import (
    AggregateObjectSetRequestV2Dict,
)  # NOQA
from foundry.v2.models._aggregate_objects_response_v2 import AggregateObjectsResponseV2
from foundry.v2.models._artifact_repository_rid import ArtifactRepositoryRid
from foundry.v2.models._create_temporary_object_set_request_v2 import (
    CreateTemporaryObjectSetRequestV2,
)  # NOQA
from foundry.v2.models._create_temporary_object_set_request_v2_dict import (
    CreateTemporaryObjectSetRequestV2Dict,
)  # NOQA
from foundry.v2.models._create_temporary_object_set_response_v2 import (
    CreateTemporaryObjectSetResponseV2,
)  # NOQA
from foundry.v2.models._load_object_set_request_v2 import LoadObjectSetRequestV2
from foundry.v2.models._load_object_set_request_v2_dict import LoadObjectSetRequestV2Dict  # NOQA
from foundry.v2.models._load_object_set_response_v2 import LoadObjectSetResponseV2
from foundry.v2.models._object_set import ObjectSet
from foundry.v2.models._object_set_rid import ObjectSetRid
from foundry.v2.models._ontology_identifier import OntologyIdentifier
from foundry.v2.models._sdk_package_name import SdkPackageName


class OntologyObjectSetResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def aggregate(
        self,
        ontology: OntologyIdentifier,
        aggregate_object_set_request_v2: Union[
            AggregateObjectSetRequestV2, AggregateObjectSetRequestV2Dict
        ],
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> AggregateObjectsResponseV2:
        """
        Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param aggregate_object_set_request_v2: Body of the request
        :type aggregate_object_set_request_v2: Union[AggregateObjectSetRequestV2, AggregateObjectSetRequestV2Dict]
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
        _body_params: Any = aggregate_object_set_request_v2
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/aggregate",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[AggregateObjectSetRequestV2, AggregateObjectSetRequestV2Dict],
                response_type=AggregateObjectsResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def create_temporary(
        self,
        ontology: OntologyIdentifier,
        create_temporary_object_set_request_v2: Union[
            CreateTemporaryObjectSetRequestV2, CreateTemporaryObjectSetRequestV2Dict
        ],
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> CreateTemporaryObjectSetResponseV2:
        """
        Creates a temporary `ObjectSet` from the given definition.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param create_temporary_object_set_request_v2: Body of the request
        :type create_temporary_object_set_request_v2: Union[CreateTemporaryObjectSetRequestV2, CreateTemporaryObjectSetRequestV2Dict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: CreateTemporaryObjectSetResponseV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = create_temporary_object_set_request_v2

        _path_params["ontology"] = ontology

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/createTemporary",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[
                    CreateTemporaryObjectSetRequestV2, CreateTemporaryObjectSetRequestV2Dict
                ],
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

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["ontology"] = ontology

        _path_params["objectSetRid"] = object_set_rid

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectSets/{objectSetRid}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
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
        load_object_set_request_v2: Union[LoadObjectSetRequestV2, LoadObjectSetRequestV2Dict],
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
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
        :param load_object_set_request_v2: Body of the request
        :type load_object_set_request_v2: Union[LoadObjectSetRequestV2, LoadObjectSetRequestV2Dict]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: LoadObjectSetResponseV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = load_object_set_request_v2
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/objectSets/loadObjects",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[LoadObjectSetRequestV2, LoadObjectSetRequestV2Dict],
                response_type=LoadObjectSetResponseV2,
                request_timeout=request_timeout,
            ),
        )
