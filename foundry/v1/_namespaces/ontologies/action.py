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
from foundry.v1.models._action_type_api_name import ActionTypeApiName
from foundry.v1.models._apply_action_request import ApplyActionRequest
from foundry.v1.models._apply_action_request_dict import ApplyActionRequestDict
from foundry.v1.models._apply_action_response import ApplyActionResponse
from foundry.v1.models._batch_apply_action_request import BatchApplyActionRequest
from foundry.v1.models._batch_apply_action_request_dict import BatchApplyActionRequestDict  # NOQA
from foundry.v1.models._batch_apply_action_response import BatchApplyActionResponse
from foundry.v1.models._ontology_rid import OntologyRid
from foundry.v1.models._validate_action_request import ValidateActionRequest
from foundry.v1.models._validate_action_request_dict import ValidateActionRequestDict
from foundry.v1.models._validate_action_response import ValidateActionResponse


class ActionResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def apply(
        self,
        ontology_rid: OntologyRid,
        action_type: ActionTypeApiName,
        apply_action_request: Union[ApplyActionRequest, ApplyActionRequestDict],
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ApplyActionResponse:
        """
        Applies an action using the given parameters. Changes to the Ontology are eventually consistent and may take
        some time to be visible.

        Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param action_type: actionType
        :type action_type: ActionTypeApiName
        :param apply_action_request: Body of the request
        :type apply_action_request: Union[ApplyActionRequest, ApplyActionRequestDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApplyActionResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = apply_action_request

        _path_params["ontologyRid"] = ontology_rid

        _path_params["actionType"] = action_type

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/actions/{actionType}/apply",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[ApplyActionRequest, ApplyActionRequestDict],
                response_type=ApplyActionResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def apply_batch(
        self,
        ontology_rid: OntologyRid,
        action_type: ActionTypeApiName,
        batch_apply_action_request: Union[BatchApplyActionRequest, BatchApplyActionRequestDict],
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> BatchApplyActionResponse:
        """
        Applies multiple actions (of the same Action Type) using the given parameters.
        Changes to the Ontology are eventually consistent and may take some time to be visible.

        Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
        call Functions may receive a higher limit.

        Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) and
        [notifications](/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param action_type: actionType
        :type action_type: ActionTypeApiName
        :param batch_apply_action_request: Body of the request
        :type batch_apply_action_request: Union[BatchApplyActionRequest, BatchApplyActionRequestDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BatchApplyActionResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = batch_apply_action_request

        _path_params["ontologyRid"] = ontology_rid

        _path_params["actionType"] = action_type

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/actions/{actionType}/applyBatch",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[BatchApplyActionRequest, BatchApplyActionRequestDict],
                response_type=BatchApplyActionResponse,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def validate(
        self,
        ontology_rid: OntologyRid,
        action_type: ActionTypeApiName,
        validate_action_request: Union[ValidateActionRequest, ValidateActionRequestDict],
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ValidateActionResponse:
        """
        Validates if an action can be run with the given set of parameters.
        The response contains the evaluation of parameters and **submission criteria**
        that determine if the request is `VALID` or `INVALID`.
        For performance reasons, validations will not consider existing objects or other data in Foundry.
        For example, the uniqueness of a primary key or the existence of a user ID will not be checked.
        Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint. Unspecified parameters will be given a default value of `null`.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read`.

        :param ontology_rid: ontologyRid
        :type ontology_rid: OntologyRid
        :param action_type: actionType
        :type action_type: ActionTypeApiName
        :param validate_action_request: Body of the request
        :type validate_action_request: Union[ValidateActionRequest, ValidateActionRequestDict]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ValidateActionResponse
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = validate_action_request

        _path_params["ontologyRid"] = ontology_rid

        _path_params["actionType"] = action_type

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/ontologies/{ontologyRid}/actions/{actionType}/validate",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[ValidateActionRequest, ValidateActionRequestDict],
                response_type=ValidateActionResponse,
                request_timeout=request_timeout,
            ),
        )
