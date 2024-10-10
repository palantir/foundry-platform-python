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

import pydantic
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v1.core.models._display_name import DisplayName
from foundry.v1.core.models._release_status import ReleaseStatus
from foundry.v1.ontologies.models._action_type_api_name import ActionTypeApiName
from foundry.v1.ontologies.models._action_type_rid import ActionTypeRid
from foundry.v1.ontologies.models._logic_rule_dict import LogicRuleDict
from foundry.v1.ontologies.models._parameter_dict import ParameterDict
from foundry.v1.ontologies.models._parameter_id import ParameterId


class ActionTypeDict(TypedDict):
    """Represents an action type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: ActionTypeApiName

    description: NotRequired[pydantic.StrictStr]

    displayName: NotRequired[DisplayName]

    status: ReleaseStatus

    parameters: Dict[ParameterId, ParameterDict]

    rid: ActionTypeRid

    operations: List[LogicRuleDict]
