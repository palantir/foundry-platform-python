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
from typing import cast

import pydantic

from foundry.v2.ontologies.models._derived_property_api_name import DerivedPropertyApiName  # NOQA
from foundry.v2.ontologies.models._derived_property_definition import (
    DerivedPropertyDefinition,
)  # NOQA
from foundry.v2.ontologies.models._object_set import ObjectSet
from foundry.v2.ontologies.models._object_set_with_properties_type_dict import (
    ObjectSetWithPropertiesTypeDict,
)  # NOQA


class ObjectSetWithPropertiesType(pydantic.BaseModel):
    """
    ObjectSet which returns objects with additional derived properties.

    This feature is experimental and not yet generally available.
    """

    object_set: ObjectSet = pydantic.Field(alias="objectSet")

    derived_properties: Dict[DerivedPropertyApiName, DerivedPropertyDefinition] = pydantic.Field(
        alias="derivedProperties"
    )

    """Map of the name of the derived property to return and its definition"""

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectSetWithPropertiesTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetWithPropertiesTypeDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
