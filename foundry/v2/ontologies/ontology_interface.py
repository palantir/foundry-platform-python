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
from pydantic import StrictInt
from pydantic import validate_call
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.core.models._preview_mode import PreviewMode
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
from foundry.v2.ontologies.models._interface_type import InterfaceType
from foundry.v2.ontologies.models._interface_type_api_name import InterfaceTypeApiName
from foundry.v2.ontologies.models._list_interface_types_response import (
    ListInterfaceTypesResponse,
)  # NOQA
from foundry.v2.ontologies.models._ontology_identifier import OntologyIdentifier
from foundry.v2.ontologies.models._search_json_query_v2_dict import SearchJsonQueryV2Dict  # NOQA


class OntologyInterfaceClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def aggregate(
        self,
        ontology: OntologyIdentifier,
        interface_type: InterfaceTypeApiName,
        *,
        aggregation: List[AggregationV2Dict],
        group_by: List[AggregationGroupByV2Dict],
        accuracy: Optional[AggregationAccuracyRequest] = None,
        preview: Optional[PreviewMode] = None,
        where: Optional[SearchJsonQueryV2Dict] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> AggregateObjectsResponseV2:
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

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param interface_type: interfaceType
        :type interface_type: InterfaceTypeApiName
        :param aggregation:
        :type aggregation: List[AggregationV2Dict]
        :param group_by:
        :type group_by: List[AggregationGroupByV2Dict]
        :param accuracy:
        :type accuracy: Optional[AggregationAccuracyRequest]
        :param preview: preview
        :type preview: Optional[PreviewMode]
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

    @validate_call
    @handle_unexpected
    def get(
        self,
        ontology: OntologyIdentifier,
        interface_type: InterfaceTypeApiName,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> InterfaceType:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Gets a specific object type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param interface_type: interfaceType
        :type interface_type: InterfaceTypeApiName
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: InterfaceType
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=InterfaceType,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def list(
        self,
        ontology: OntologyIdentifier,
        *,
        page_size: Optional[PageSize] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ResourceIterator[InterfaceType]:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Lists the interface types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[InterfaceType]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/interfaceTypes",
                query_params={
                    "pageSize": page_size,
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
                response_type=ListInterfaceTypesResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def page(
        self,
        ontology: OntologyIdentifier,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListInterfaceTypesResponse:
        """
        :::callout{theme=warning title=Warning}
          This endpoint is in preview and may be modified or removed at any time.
          To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Lists the interface types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListInterfaceTypesResponse
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=ListInterfaceTypesResponse,
                request_timeout=request_timeout,
            ),
        )
