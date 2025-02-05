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

from foundry.v2.ontologies.models._property_api_name import PropertyApiName
from foundry.v2.ontologies.models._struct_field_api_name import StructFieldApiName
from foundry.v2.ontologies.models._struct_field_selector_dict import StructFieldSelectorDict  # NOQA


class StructFieldSelector(pydantic.BaseModel):
    """
    A combination of a struct property api name and a struct field api name. This is used to select struct fields
    to query on. Note that you can still select struct properties with only a 'PropertyApiNameSelector'; the queries
    will then become 'OR' queries across the fields of the struct property.
    """

    property_api_name: PropertyApiName = pydantic.Field(alias=str("propertyApiName"))  # type: ignore[literal-required]

    struct_field_api_name: StructFieldApiName = pydantic.Field(alias=str("structFieldApiName"))  # type: ignore[literal-required]

    type: Literal["structField"] = "structField"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> StructFieldSelectorDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(StructFieldSelectorDict, self.model_dump(by_alias=True, exclude_none=True))
