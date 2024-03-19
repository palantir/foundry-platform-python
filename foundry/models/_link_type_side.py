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


from foundry.models._display_name import DisplayName
from foundry.models._link_type_api_name import LinkTypeApiName
from foundry.models._link_type_side_cardinality import LinkTypeSideCardinality
from foundry.models._object_type_api_name import ObjectTypeApiName
from foundry.models._property_api_name import PropertyApiName
from foundry.models._release_status import ReleaseStatus


class LinkTypeSide(BaseModel):
    """LinkTypeSide"""

    api_name: LinkTypeApiName = Field(alias="apiName")
    """
    The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager**
    application.
    """

    display_name: DisplayName = Field(alias="displayName")
    """The display name of the entity."""

    status: ReleaseStatus = Field()
    """The release status of the entity."""

    object_type_api_name: ObjectTypeApiName = Field(alias="objectTypeApiName")
    """
    The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the
    `List object types` endpoint or check the **Ontology Manager**.
    """

    cardinality: LinkTypeSideCardinality = Field()
    """LinkTypeSideCardinality"""

    foreign_key_property_api_name: Optional[PropertyApiName] = Field(
        alias="foreignKeyPropertyApiName", default=None
    )
    """
    The name of the property in the API. To find the API name for your property, use the `Get object type`
    endpoint or check the **Ontology Manager**.
    """

    _properties: ClassVar[Set[str]] = set(
        [
            "apiName",
            "displayName",
            "status",
            "objectTypeApiName",
            "cardinality",
            "foreignKeyPropertyApiName",
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
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "LinkTypeSide":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)
