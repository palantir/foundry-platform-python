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

from foundry.models._list_ontologies_v2_response import ListOntologiesV2Response
from foundry.models._ontology_full_metadata import OntologyFullMetadata
from foundry.models._ontology_identifier import OntologyIdentifier
from foundry.models._ontology_v2 import OntologyV2


class OntologyV2Resource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def iterator(
        self,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListOntologiesV2Response:
        """
        Lists the Ontologies visible to the current user.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListOntologiesV2Response
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: ListOntologiesV2Response,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v2/ontologies",
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
        ontology: OntologyIdentifier,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> OntologyV2:
        """
        Gets a specific ontology with the given Ontology RID.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:read-data`.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: OntologyV2
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _path_params["ontology"] = ontology

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: OntologyV2,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v2/ontologies/{ontology}".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def get_ontology_full_metadata(
        self,
        ontology: OntologyIdentifier,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> OntologyFullMetadata:
        """
        Get the full Ontology metadata. This includes the objects, links, actions, and queries.

        :param ontology: The API name of the ontology. To find the API name, use the **List ontologies** endpoint or check the **Ontology Manager**.
        :type ontology: OntologyIdentifier
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: OntologyFullMetadata
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None

        _path_params["ontology"] = ontology

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: OntologyFullMetadata,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v2/ontologies/{ontology}/fullMetadata".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )
