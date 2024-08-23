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

from foundry.v1.models._display_name import DisplayName
from foundry.v1.models._object_type_api_name import ObjectTypeApiName
from foundry.v1.models._object_type_dict import ObjectTypeDict
from foundry.v1.models._object_type_rid import ObjectTypeRid
from foundry.v1.models._object_type_visibility import ObjectTypeVisibility
from foundry.v1.models._property import Property
from foundry.v1.models._property_api_name import PropertyApiName
from foundry.v1.models._release_status import ReleaseStatus


class ObjectType(BaseModel):
    """Represents an object type in the Ontology."""

    api_name: ObjectTypeApiName = Field(alias="apiName")

    display_name: Optional[DisplayName] = Field(alias="displayName", default=None)

    status: ReleaseStatus

    description: Optional[StrictStr] = None
    """The description of the object type."""

    visibility: Optional[ObjectTypeVisibility] = None

    primary_key: List[PropertyApiName] = Field(alias="primaryKey")
    """The primary key of the object. This is a list of properties that can be used to uniquely identify the object."""

    properties: Dict[PropertyApiName, Property]
    """A map of the properties of the object type."""

    rid: ObjectTypeRid

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectTypeDict, self.model_dump(by_alias=True, exclude_unset=True))
