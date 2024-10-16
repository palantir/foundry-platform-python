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

from foundry.v2.ontologies.models._object_edit import ObjectEdit
from foundry.v2.ontologies.models._object_edits_dict import ObjectEditsDict


class ObjectEdits(pydantic.BaseModel):
    """ObjectEdits"""

    edits: List[ObjectEdit]

    added_object_count: pydantic.StrictInt = pydantic.Field(alias="addedObjectCount")

    modified_objects_count: pydantic.StrictInt = pydantic.Field(alias="modifiedObjectsCount")

    deleted_objects_count: pydantic.StrictInt = pydantic.Field(alias="deletedObjectsCount")

    added_links_count: pydantic.StrictInt = pydantic.Field(alias="addedLinksCount")

    deleted_links_count: pydantic.StrictInt = pydantic.Field(alias="deletedLinksCount")

    type: Literal["edits"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectEditsDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectEditsDict, self.model_dump(by_alias=True, exclude_unset=True))
