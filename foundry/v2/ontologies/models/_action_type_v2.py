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
from typing import Optional
from typing import cast

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictStr

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.core.models._release_status import ReleaseStatus
from foundry.v2.ontologies.models._action_parameter_v2 import ActionParameterV2
from foundry.v2.ontologies.models._action_type_api_name import ActionTypeApiName
from foundry.v2.ontologies.models._action_type_rid import ActionTypeRid
from foundry.v2.ontologies.models._action_type_v2_dict import ActionTypeV2Dict
from foundry.v2.ontologies.models._logic_rule import LogicRule
from foundry.v2.ontologies.models._parameter_id import ParameterId


class ActionTypeV2(BaseModel):
    """Represents an action type in the Ontology."""

    api_name: ActionTypeApiName = Field(alias="apiName")

    description: Optional[StrictStr] = None

    display_name: Optional[DisplayName] = Field(alias="displayName", default=None)

    status: ReleaseStatus

    parameters: Dict[ParameterId, ActionParameterV2]

    rid: ActionTypeRid

    operations: List[LogicRule]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ActionTypeV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ActionTypeV2Dict, self.model_dump(by_alias=True, exclude_unset=True))
