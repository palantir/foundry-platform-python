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

from typing import Optional
from typing import cast

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictStr

from foundry.v1.models._display_name import DisplayName
from foundry.v1.models._object_property_type import ObjectPropertyType
from foundry.v1.models._property_v2_dict import PropertyV2Dict


class PropertyV2(BaseModel):
    """Details about some property of an object."""

    description: Optional[StrictStr] = None

    display_name: Optional[DisplayName] = Field(alias="displayName", default=None)

    data_type: ObjectPropertyType = Field(alias="dataType")

    model_config = {"extra": "allow"}

    def to_dict(self) -> PropertyV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(PropertyV2Dict, self.model_dump(by_alias=True, exclude_unset=True))
