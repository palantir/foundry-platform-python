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

from typing import Dict
from typing import List

from pydantic import StrictStr
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.models._action_parameter_v2_dict import ActionParameterV2Dict
from foundry.models._action_type_api_name import ActionTypeApiName
from foundry.models._action_type_rid import ActionTypeRid
from foundry.models._display_name import DisplayName
from foundry.models._logic_rule_dict import LogicRuleDict
from foundry.models._parameter_id import ParameterId
from foundry.models._release_status import ReleaseStatus


class ActionTypeV2Dict(TypedDict):
    """Represents an action type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: ActionTypeApiName

    description: NotRequired[StrictStr]

    displayName: NotRequired[DisplayName]

    status: ReleaseStatus

    parameters: Dict[ParameterId, ActionParameterV2Dict]

    rid: ActionTypeRid

    operations: List[LogicRuleDict]
