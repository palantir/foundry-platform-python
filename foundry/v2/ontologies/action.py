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
from foundry._errors import handle_unexpected
from foundry.v2.ontologies.models._action_type_api_name import ActionTypeApiName
from foundry.v2.ontologies.models._apply_action_request_options_dict import (
    ApplyActionRequestOptionsDict,
)  # NOQA
from foundry.v2.ontologies.models._artifact_repository_rid import ArtifactRepositoryRid
from foundry.v2.ontologies.models._batch_apply_action_request_item_dict import (
    BatchApplyActionRequestItemDict,
)  # NOQA
from foundry.v2.ontologies.models._batch_apply_action_request_options_dict import (
    BatchApplyActionRequestOptionsDict,
)  # NOQA
from foundry.v2.ontologies.models._batch_apply_action_response_v2 import (
    BatchApplyActionResponseV2,
)  # NOQA
from foundry.v2.ontologies.models._data_value import DataValue
from foundry.v2.ontologies.models._ontology_identifier import OntologyIdentifier
from foundry.v2.ontologies.models._parameter_id import ParameterId
from foundry.v2.ontologies.models._sdk_package_name import SdkPackageName
from foundry.v2.ontologies.models._sync_apply_action_response_v2 import (
    SyncApplyActionResponseV2,
)  # NOQA


class ActionClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def apply(
        self,
        ontology: OntologyIdentifier,
        action: ActionTypeApiName,
        *,
        parameters: Dict[ParameterId, Optional[DataValue]],
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        options: Optional[ApplyActionRequestOptionsDict] = None,
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
        :param parameters:
        :type parameters: Dict[ParameterId, Optional[DataValue]]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param options:
        :type options: Optional[ApplyActionRequestOptionsDict]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: SyncApplyActionResponseV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actions/{action}/apply",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "action": action,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "options": options,
                    "parameters": parameters,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "options": Optional[ApplyActionRequestOptionsDict],
                        "parameters": Dict[ParameterId, Optional[DataValue]],
                    },
                ),
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
        *,
        requests: List[BatchApplyActionRequestItemDict],
        artifact_repository: Optional[ArtifactRepositoryRid] = None,
        options: Optional[BatchApplyActionRequestOptionsDict] = None,
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
        :param requests:
        :type requests: List[BatchApplyActionRequestItemDict]
        :param artifact_repository: artifactRepository
        :type artifact_repository: Optional[ArtifactRepositoryRid]
        :param options:
        :type options: Optional[BatchApplyActionRequestOptionsDict]
        :param package_name: packageName
        :type package_name: Optional[SdkPackageName]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BatchApplyActionResponseV2
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/ontologies/{ontology}/actions/{action}/applyBatch",
                query_params={
                    "artifactRepository": artifact_repository,
                    "packageName": package_name,
                },
                path_params={
                    "ontology": ontology,
                    "action": action,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "options": options,
                    "requests": requests,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "options": Optional[BatchApplyActionRequestOptionsDict],
                        "requests": List[BatchApplyActionRequestItemDict],
                    },
                ),
                response_type=BatchApplyActionResponseV2,
                request_timeout=request_timeout,
            ),
        )
