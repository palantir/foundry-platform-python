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
from pydantic import StrictBool


from foundry.models._field_name import FieldName
from foundry.models._model_api_type import ModelApiType


class ModelApiDataType(BaseModel):
    """An object definition representing an input or an output type for the deployment API."""

    name: Optional[FieldName] = Field(default=None)
    """The name of a field."""

    required: Optional[StrictBool] = Field(default=None)

    property_type: Optional[ModelApiType] = Field(alias="propertyType", default=None)
    """A union of all the types supported by models."""

    _properties: ClassVar[Set[str]] = set(["name", "required", "propertyType"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "ModelApiDataType":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)