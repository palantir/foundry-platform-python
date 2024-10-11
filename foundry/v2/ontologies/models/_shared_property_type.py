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

import pydantic

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.ontologies.models._object_property_type import ObjectPropertyType
from foundry.v2.ontologies.models._shared_property_type_api_name import (
    SharedPropertyTypeApiName,
)  # NOQA
from foundry.v2.ontologies.models._shared_property_type_dict import SharedPropertyTypeDict  # NOQA
from foundry.v2.ontologies.models._shared_property_type_rid import SharedPropertyTypeRid


class SharedPropertyType(pydantic.BaseModel):
    """A property type that can be shared across object types."""

    rid: SharedPropertyTypeRid

    api_name: SharedPropertyTypeApiName = pydantic.Field(alias="apiName")

    display_name: DisplayName = pydantic.Field(alias="displayName")

    description: Optional[pydantic.StrictStr] = None
    """A short text that describes the SharedPropertyType."""

    data_type: ObjectPropertyType = pydantic.Field(alias="dataType")

    model_config = {"extra": "allow"}

    def to_dict(self) -> SharedPropertyTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(SharedPropertyTypeDict, self.model_dump(by_alias=True, exclude_unset=True))
