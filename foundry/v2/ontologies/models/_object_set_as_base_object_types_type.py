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
from pydantic import Field

from foundry.v2.ontologies.models._object_set import ObjectSet
from foundry.v2.ontologies.models._object_set_as_base_object_types_type_dict import (
    ObjectSetAsBaseObjectTypesTypeDict,
)  # NOQA


class ObjectSetAsBaseObjectTypesType(BaseModel):
    """
    Casts the objects in the object set to their base type and thus ensures objects are returned with all of their
    properties in the resulting object set, not just the properties that implement interface properties. This is
    currently unsupported and an exception will be thrown if used.
    """

    object_set: ObjectSet = Field(alias="objectSet")

    type: Literal["asBaseObjectTypes"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectSetAsBaseObjectTypesTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetAsBaseObjectTypesTypeDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
