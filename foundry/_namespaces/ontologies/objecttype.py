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
from pydantic import StrictInt
from typing import Annotated
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from pydantic import validate_call

from foundry._errors.sdk_internal_error import handle_unexpected
from foundry.api_client import ApiClient

from foundry.models._link_type_api_name import LinkTypeApiName
from foundry.models._link_type_side import LinkTypeSide
from foundry.models._list_object_types_response import ListObjectTypesResponse
from foundry.models._list_outgoing_link_types_response import ListOutgoingLinkTypesResponse
from foundry.models._object_type import ObjectType
from foundry.models._object_type_api_name import ObjectTypeApiName
from foundry.models._ontology_rid import OntologyRid
from foundry.models._page_size import PageSize
from foundry.models._page_token import PageToken


class ObjectTypeResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def iterator(
        self,
        ontology_rid: OntologyRid,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListObjectTypesResponse:
        """
        Lists the object types for the given Ontology.

        Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
        more results available, at least one result will be present in the
        response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the object types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param page_size: The desired size of the page to be returned. Defaults to 500. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListObjectTypesResponse
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _path_params["ontologyRid"] = ontology_rid

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: ListObjectTypesResponse,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/ontologies/{ontologyRid}/objectTypes".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ObjectType:
        """
        Gets a specific object type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**.
        :type object_type: ObjectTypeApiName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ObjectType
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: ObjectType,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/ontologies/{ontologyRid}/objectTypes/{objectType}".format(
                **_path_params
            ),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def list_outgoing_link_types(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListOutgoingLinkTypesResponse:
        """
        List the outgoing links for an object type.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:read-data`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager** application.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
        :type object_type: ObjectTypeApiName
        :param page_size: The desired size of the page to be returned.
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListOutgoingLinkTypesResponse
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: ListOutgoingLinkTypesResponse,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes".format(
                **_path_params
            ),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def get_outgoing_link_type(
        self,
        ontology_rid: OntologyRid,
        object_type: ObjectTypeApiName,
        link_type: LinkTypeApiName,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> LinkTypeSide:
        """
        Get an outgoing link for an object type.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:read-data`.

        :param ontology_rid: The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager** application.
        :type ontology_rid: OntologyRid
        :param object_type: The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application.
        :type object_type: ObjectTypeApiName
        :param link_type: The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**.
        :type link_type: LinkTypeApiName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: LinkTypeSide
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _path_params["ontologyRid"] = ontology_rid

        _path_params["objectType"] = object_type

        _path_params["linkType"] = link_type

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: LinkTypeSide,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes/{linkType}".format(
                **_path_params
            ),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )
