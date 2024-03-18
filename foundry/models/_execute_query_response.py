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
from typing import Set

from pydantic import BaseModel
from pydantic import Field


from foundry.models._data_value import DataValue


class ExecuteQueryResponse(BaseModel):
    """ExecuteQueryResponse"""

    value: DataValue = Field()
    """
    Represents the value of data in the following format. Note that these values can be nested, for example an array of structs.
    | Type                        | JSON encoding                                         | Example                                                                       |
    |-----------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------|
    | Array                       | array                                                 | `["alpha", "bravo", "charlie"]`                                               |
    | Attachment                  | string                                                | `"ri.attachments.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e"`       |
    | Boolean                     | boolean                                               | `true`                                                                        |
    | Byte                        | number                                                | `31`                                                                          |
    | Date                        | ISO 8601 extended local date string                   | `"2021-05-01"`                                                                |
    | Decimal                     | string                                                | `"2.718281828"`                                                               |
    | Float                       | number                                                | `3.14159265`                                                                  |
    | Double                      | number                                                | `3.14159265`                                                                  |
    | Integer                     | number                                                | `238940`                                                                      |
    | Long                        | string                                                | `"58319870951433"`                                                            |
    | Null                        | null                                                  | `null`                                                                        |
    | Object Set                  | string                                                | `ri.object-set.main.versioned-object-set.h13274m8-23f5-431c-8aee-a4554157c57z`|
    | Ontology Object Reference   | JSON encoding of the object's primary key             | `10033123` or `"EMP1234"`                                                     |
    | Set                         | array                                                 | `["alpha", "bravo", "charlie"]`                                               |
    | Short                       | number                                                | `8739`                                                                        |
    | String                      | string                                                | `"Call me Ishmael"`                                                           |
    | Struct                      | JSON object                                           | `{"name": "John Doe", "age": 42}`                                             |
    | TwoDimensionalAggregation   | JSON object                                           | `{"groups": [{"key": "alpha", "value": 100}, {"key": "beta", "value": 101}]}` |
    | ThreeDimensionalAggregation | JSON object                                           | `{"groups": [{"key": "NYC", "groups": [{"key": "Engineer", "value" : 100}]}]}`|
    | Timestamp                   | ISO 8601 extended offset date-time string in UTC zone | `"2021-01-04T05:00:00Z"`                                                      |
    """

    _properties: ClassVar[Set[str]] = set(["value"])

    model_config = {"populate_by_name": True, "validate_assignment": True, "extra": "forbid"}

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:
        """
        return self.model_dump(by_alias=True)

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> "ExecuteQueryResponse":
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if allow_extra and isinstance(obj, dict) and any(key not in cls._properties for key in obj):
            obj = {key: value for key, value in obj.items() if key in cls._properties}

        return cls.model_validate(obj)