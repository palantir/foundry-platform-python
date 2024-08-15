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

from typing import Literal
from typing import cast

from pydantic import BaseModel

from foundry.v1.models._object_state import ObjectState
from foundry.v1.models._object_update_dict import ObjectUpdateDict
from foundry.v1.models._ontology_object_v2 import OntologyObjectV2


class ObjectUpdate(BaseModel):
    """ObjectUpdate"""

    object: OntologyObjectV2

    state: ObjectState

    type: Literal["object"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectUpdateDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectUpdateDict, self.model_dump(by_alias=True, exclude_unset=True))
