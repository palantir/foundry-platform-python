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

from typing import List
from typing import Literal
from typing import cast

import pydantic

from foundry.v2.aip_agents.models._object_context_dict import ObjectContextDict
from foundry.v2.ontologies.models._object_rid import ObjectRid
from foundry.v2.ontologies.models._property_type_rid import PropertyTypeRid


class ObjectContext(pydantic.BaseModel):
    """
    Details of relevant retrieved object instances for a user's message to include as
    additional context in the prompt to the Agent.
    """

    object_rids: List[ObjectRid] = pydantic.Field(alias="objectRids")
    """The RIDs of the relevant object instances to include in the prompt."""

    property_type_rids: List[PropertyTypeRid] = pydantic.Field(alias="propertyTypeRids")
    """The RIDs of the property types for the given objects to include in the prompt."""

    type: Literal["objectContext"] = "objectContext"

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectContextDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectContextDict, self.model_dump(by_alias=True, exclude_unset=True))
