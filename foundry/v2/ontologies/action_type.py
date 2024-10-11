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
from foundry.v2.ontologies.models._action_type_api_name import ActionTypeApiName
from foundry.v2.ontologies.models._action_type_v2 import ActionTypeV2
from foundry.v2.ontologies.models._list_action_types_response_v2 import (
    ListActionTypesResponseV2,
)  # NOQA
from foundry.v2.ontologies.models._ontology_identifier import OntologyIdentifier


class ActionTypeClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        ontology: OntologyIdentifier,
        action_type: ActionTypeApiName,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ActionTypeV2:
        """
        Gets a specific action type with the given API name.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param action_type: actionType
        :type action_type: ActionTypeApiName
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ActionTypeV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes/{actionType}",
                query_params={},
                path_params={
                    "ontology": ontology,
                    "actionType": action_type,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ActionTypeV2,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        ontology: OntologyIdentifier,
        *,
        page_size: Optional[PageSize] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[ActionTypeV2]:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[ActionTypeV2]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes",
                query_params={
                    "pageSize": page_size,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListActionTypesResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        ontology: OntologyIdentifier,
        *,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListActionTypesResponseV2:
        """
        Lists the action types for the given Ontology.

        Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
        results available, at least one result will be present in the response.

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
        :rtype: ListActionTypesResponseV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/ontologies/{ontology}/actionTypes",
                query_params={
                    "pageSize": page_size,
                    "pageToken": page_token,
                },
                path_params={
                    "ontology": ontology,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListActionTypesResponseV2,
                request_timeout=request_timeout,
            ),
        )
