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

import pydantic

from foundry.v2.ontologies.models._object_set import ObjectSet
from foundry.v2.ontologies.models._object_set_as_type_type_dict import (
    ObjectSetAsTypeTypeDict,
)  # NOQA


class ObjectSetAsTypeType(pydantic.BaseModel):
    """
    Casts an object set to a specified object type or interface type API name. Any object whose object type does
    not match the object type provided or implement the interface type provided will be dropped from the resulting
    object set. This is currently unsupported and an exception will be thrown if used.
    """

    entity_type: str = pydantic.Field(alias=str("entityType"))  # type: ignore[literal-required]

    """An object type or interface type API name."""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]

    type: Literal["asType"] = "asType"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ObjectSetAsTypeTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectSetAsTypeTypeDict, self.model_dump(by_alias=True, exclude_none=True))
