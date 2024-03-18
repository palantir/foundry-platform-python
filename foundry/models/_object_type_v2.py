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
from typing import Any
from typing import ClassVar
from typing import Dict
from typing import Optional
from typing import Set

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictStr


from foundry.models._display_name import DisplayName
from foundry.models._object_type_api_name import ObjectTypeApiName
from foundry.models._object_type_rid import ObjectTypeRid
from foundry.models._object_type_visibility import ObjectTypeVisibility
from foundry.models._property_api_name import PropertyApiName
from foundry.models._property_v2 import PropertyV2
from foundry.models._release_status import ReleaseStatus


class ObjectTypeV2(BaseModel):
    """Represents an object type in the Ontology."""

    api_name: ObjectTypeApiName = Field(alias="apiName")
    """
    The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the
    `List object types` endpoint or check the **Ontology Manager**.
    """

    display_name: Optional[DisplayName] = Field(alias="displayName", default=None)
    """The display name of the entity."""

    status: ReleaseStatus = Field()
    """The release status of the entity."""

    description: Optional[StrictStr] = Field(default=None)
    """The description of the object type."""

    primary_key: PropertyApiName = Field(alias="primaryKey")
    """
    The name of the property in the API. To find the API name for your property, use the `Get object type`
    endpoint or check the **Ontology Manager**.
    """

    properties: Optional[Dict[str, PropertyV2]] = Field(default=None)
    """A map of the properties of the object type."""

    rid: ObjectTypeRid = Field()
    """The unique resource identifier of an object type, useful for interacting with other Foundry APIs."""

    visibility: Optional[ObjectTypeVisibility] = Field(default=None)
    """The suggested visibility of the object type."""

    _properties: ClassVar[Set[str]] = set(
        [
            "apiName",
            "displayName",
            "status",
            "description",
            "primaryKey",
            "properties",
            "rid",
            "visibility",
        ]
    )

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "ObjectTypeV2":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)
