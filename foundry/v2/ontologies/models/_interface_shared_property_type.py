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
from foundry.v2.ontologies.models._interface_shared_property_type_dict import (
    InterfaceSharedPropertyTypeDict,
)  # NOQA
from foundry.v2.ontologies.models._object_property_type import ObjectPropertyType
from foundry.v2.ontologies.models._shared_property_type_api_name import (
    SharedPropertyTypeApiName,
)  # NOQA
from foundry.v2.ontologies.models._shared_property_type_rid import SharedPropertyTypeRid


class InterfaceSharedPropertyType(pydantic.BaseModel):
    """
    A shared property type with an additional field to indicate whether the property must be included on every
    object type that implements the interface, or whether it is optional.
    """

    rid: SharedPropertyTypeRid

    api_name: SharedPropertyTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]

    display_name: DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]

    description: Optional[str] = None

    """A short text that describes the SharedPropertyType."""

    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]

    required: bool

    """Whether each implementing object type must declare an implementation for this property."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> InterfaceSharedPropertyTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            InterfaceSharedPropertyTypeDict, self.model_dump(by_alias=True, exclude_none=True)
        )
