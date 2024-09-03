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

from foundry._errors import handle_unexpected
from foundry.api_client import ApiClient
from foundry.api_client import RequestInfo
from foundry.v2._namespaces.ontologies.action_type import ActionTypeResource
from foundry.v2._namespaces.ontologies.object_type import ObjectTypeResource
from foundry.v2._namespaces.ontologies.query_type import QueryTypeResource
from foundry.v2.models._ontology_full_metadata import OntologyFullMetadata
from foundry.v2.models._ontology_identifier import OntologyIdentifier
from foundry.v2.models._ontology_v2 import OntologyV2


class OntologyResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

        self.ActionType = ActionTypeResource(api_client=api_client)
        self.ObjectType = ObjectTypeResource(api_client=api_client)
        self.QueryType = QueryTypeResource(api_client=api_client)

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

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: OntologyV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["ontology"] = ontology

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=OntologyV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get_full_metadata(
        self,
        ontology: OntologyIdentifier,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> OntologyFullMetadata:
        """
        Get the full Ontology metadata. This includes the objects, links, actions, queries, and interfaces.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: OntologyFullMetadata
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = None

        _path_params["ontology"] = ontology

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/fullMetadata",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=None,
                response_type=OntologyFullMetadata,
                request_timeout=request_timeout,
            ),
        )
