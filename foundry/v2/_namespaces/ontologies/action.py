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
from foundry.v2.models._action_type_api_name import ActionTypeApiName
from foundry.v2.models._apply_action_request_v2 import ApplyActionRequestV2
from foundry.v2.models._apply_action_request_v2_dict import ApplyActionRequestV2Dict
from foundry.v2.models._artifact_repository_rid import ArtifactRepositoryRid
from foundry.v2.models._batch_apply_action_request_v2 import BatchApplyActionRequestV2
from foundry.v2.models._batch_apply_action_request_v2_dict import (
    BatchApplyActionRequestV2Dict,
)  # NOQA
from foundry.v2.models._batch_apply_action_response_v2 import BatchApplyActionResponseV2
from foundry.v2.models._ontology_identifier import OntologyIdentifier
from foundry.v2.models._sdk_package_name import SdkPackageName
from foundry.v2.models._sync_apply_action_response_v2 import SyncApplyActionResponseV2


class ActionResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def apply(
        self,
        ontology: OntologyIdentifier,
        action: ActionTypeApiName,
        apply_action_request_v2: Union[ApplyActionRequestV2, ApplyActionRequestV2Dict],
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> SyncApplyActionResponseV2:
        """
        Applies an action using the given parameters.

        Changes to the Ontology are eventually consistent and may take some time to be visible.

        Note that [parameter default values](/docs/foundry/action-types/parameters-default-value/) are not currently supported by
        this endpoint.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param action: action
        :type action: ActionTypeApiName
        :param apply_action_request_v2: Body of the request
        :type apply_action_request_v2: Union[ApplyActionRequestV2, ApplyActionRequestV2Dict]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SyncApplyActionResponseV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = apply_action_request_v2
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _path_params["action"] = action

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actions/{action}/apply",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[ApplyActionRequestV2, ApplyActionRequestV2Dict],
                response_type=SyncApplyActionResponseV2,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def apply_batch(
        self,
        ontology: OntologyIdentifier,
        action: ActionTypeApiName,
        batch_apply_action_request_v2: Union[
            BatchApplyActionRequestV2, BatchApplyActionRequestV2Dict
        ],
        *,
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        package_name: Optional[SdkPackageName] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> BatchApplyActionResponseV2:
        """
        Applies multiple actions (of the same Action Type) using the given parameters.
        Changes to the Ontology are eventually consistent and may take some time to be visible.

        Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
        call Functions may receive a higher limit.

        Note that [notifications](/docs/foundry/action-types/notifications/) are not currently supported by this endpoint.

        Third-party applications using this endpoint via OAuth2 must request the
        following operation scopes: `api:ontologies-read api:ontologies-write`.

        :param ontology: ontology
        :type ontology: OntologyIdentifier
        :param action: action
        :type action: ActionTypeApiName
        :param batch_apply_action_request_v2: Body of the request
        :type batch_apply_action_request_v2: Union[BatchApplyActionRequestV2, BatchApplyActionRequestV2Dict]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BatchApplyActionResponseV2
        """

        _path_params: Dict[str, Any] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, Any] = {}
        _body_params: Any = batch_apply_action_request_v2
        _query_params["artifactRepository"] = artifact_repository

        _query_params["packageName"] = package_name

        _path_params["ontology"] = ontology

        _path_params["action"] = action

        _header_params["Content-Type"] = "application/json"

        _header_params["Accept"] = "application/json"

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actions/{action}/applyBatch",
                query_params=_query_params,
                path_params=_path_params,
                header_params=_header_params,
                body=_body_params,
                body_type=Union[BatchApplyActionRequestV2, BatchApplyActionRequestV2Dict],
                response_type=BatchApplyActionResponseV2,
                request_timeout=request_timeout,
            ),
        )
