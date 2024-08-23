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

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call

from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v2.models._link_type_api_name import LinkTypeApiName
from foundry.v2.models._link_type_side_v2 import LinkTypeSideV2
from foundry.v2.models._list_object_types_v2_response import ListObjectTypesV2Response
from foundry.v2.models._list_outgoing_link_types_response_v2 import (
    ListOutgoingLinkTypesResponseV2,
)  # NOQA
from foundry.v2.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.models._object_type_v2 import ObjectTypeV2
from foundry.v2.models._ontology_identifier import OntologyIdentifier
from foundry.v2.models._page_size import PageSize
from foundry.v2.models._page_token import PageToken


class ObjectTypeResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def get(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ObjectTypeV2:
        """
        Gets a specific object type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ObjectTypeV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ObjectTypeV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_outgoing_link_type(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        link_type: LinkTypeApiName,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> LinkTypeSideV2:
        """
        Get an outgoing link for an object type.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param link_type: linkType
        :type link_type: LinkTypeApiName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: LinkTypeSideV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _path_params["linkType"] = link_type

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=LinkTypeSideV2,
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
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ResourceIterator[ObjectTypeV2]:
        """
        Lists the object types for the given Ontology.

        Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
        more results available, at least one result will be present in the
        response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[ObjectTypeV2]
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _path_params["ontology"] = ontology

        _header_params["Accept"] = "application/json"

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListObjectTypesV2Response,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def list_outgoing_link_types(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        page_size: Optional[PageSize] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ResourceIterator[LinkTypeSideV2]:
        """
        List the outgoing links for an object type.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[LinkTypeSideV2]
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListOutgoingLinkTypesResponseV2,
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
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListObjectTypesV2Response:
        """
        Lists the object types for the given Ontology.

        Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
        more results available, at least one result will be present in the
        response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListObjectTypesV2Response
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _path_params["ontology"] = ontology

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListObjectTypesV2Response,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def page_outgoing_link_types(
        self,
        ontology: OntologyIdentifier,
        object_type: ObjectTypeApiName,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListOutgoingLinkTypesResponseV2:
        """
        List the outgoing links for an object type.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param object_type: objectType
        :type object_type: ObjectTypeApiName
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListOutgoingLinkTypesResponseV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _path_params["ontology"] = ontology

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=ListOutgoingLinkTypesResponseV2,
                request_timeout=request_timeout,
            ),
        )
