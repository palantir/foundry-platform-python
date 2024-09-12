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

from foundry.v2.models._object_primary_key import ObjectPrimaryKey
from foundry.v2.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.models._property_api_name import PropertyApiName
from foundry.v2.models._reference_update_dict import ReferenceUpdateDict
from foundry.v2.models._reference_value import ReferenceValue


class ReferenceUpdate(BaseModel):
    """
    The updated data value associated with an object instance's external reference. The object instance
    is uniquely identified by an object type and a primary key. Note that the value of the property
    field returns a dereferenced value rather than the reference itself.
    """

    object_type: ObjectTypeApiName = Field(alias="objectType")

    primary_key: ObjectPrimaryKey = Field(alias="primaryKey")

    property: PropertyApiName

    value: ReferenceValue

    type: Literal["reference"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ReferenceUpdateDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ReferenceUpdateDict, self.model_dump(by_alias=True, exclude_unset=True))
