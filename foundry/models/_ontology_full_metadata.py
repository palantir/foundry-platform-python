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


from foundry.models._action_type_v2 import ActionTypeV2
from foundry.models._object_type_with_link import ObjectTypeWithLink
from foundry.models._ontology_v2 import OntologyV2
from foundry.models._query_type_v2 import QueryTypeV2


class OntologyFullMetadata(BaseModel):
    """OntologyFullMetadata"""

    ontology: OntologyV2 = Field()
    """Metadata about an Ontology."""

    object_types: Optional[Dict[str, ObjectTypeWithLink]] = Field(alias="objectTypes", default=None)

    action_types: Optional[Dict[str, ActionTypeV2]] = Field(alias="actionTypes", default=None)

    query_types: Optional[Dict[str, QueryTypeV2]] = Field(alias="queryTypes", default=None)

    _properties: ClassVar[Set[str]] = set(["ontology", "objectTypes", "actionTypes", "queryTypes"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "OntologyFullMetadata":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)
