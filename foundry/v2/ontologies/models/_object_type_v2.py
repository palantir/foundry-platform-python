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
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.core.models._release_status import ReleaseStatus
from foundry.v2.ontologies.models._icon import Icon
from foundry.v2.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.ontologies.models._object_type_rid import ObjectTypeRid
from foundry.v2.ontologies.models._object_type_v2_dict import ObjectTypeV2Dict
from foundry.v2.ontologies.models._object_type_visibility import ObjectTypeVisibility
from foundry.v2.ontologies.models._property_api_name import PropertyApiName
from foundry.v2.ontologies.models._property_v2 import PropertyV2


class ObjectTypeV2(pydantic.BaseModel):
    """Represents an object type in the Ontology."""

    api_name: ObjectTypeApiName = pydantic.Field(alias="apiName")

    display_name: DisplayName = pydantic.Field(alias="displayName")

    status: ReleaseStatus

    description: Optional[pydantic.StrictStr] = None
    """The description of the object type."""

    plural_display_name: pydantic.StrictStr = pydantic.Field(alias="pluralDisplayName")
    """The plural display name of the object type."""

    icon: Icon

    primary_key: PropertyApiName = pydantic.Field(alias="primaryKey")

    properties: Dict[PropertyApiName, PropertyV2]
    """A map of the properties of the object type."""

    rid: ObjectTypeRid

    title_property: PropertyApiName = pydantic.Field(alias="titleProperty")

    visibility: Optional[ObjectTypeVisibility] = None

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectTypeV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ObjectTypeV2Dict, self.model_dump(by_alias=True, exclude_unset=True))
