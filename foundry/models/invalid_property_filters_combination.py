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

# coding: utf-8

"""
    Palantir OpenAPI

    The Palantir REST API. Please see https://www.palantir.com/docs for more details.

    The version of the OpenAPI document: 1.738.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import json


from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from foundry.models.invalid_property_filters_combination_parameters import InvalidPropertyFiltersCombinationParameters
from typing_extensions import Self

class InvalidPropertyFiltersCombination(BaseModel):
    """
    The provided filters cannot be used together.
    """ # noqa: E501
    error_code: StrictStr = Field(alias="errorCode")
    error_instance_id: Optional[StrictStr] = Field(default=None, alias="errorInstanceId")
    error_name: StrictStr = Field(alias="errorName")
    parameters: InvalidPropertyFiltersCombinationParameters
    __properties: ClassVar[Set[str]] = set(("errorCode", "errorInstanceId", "errorName", "parameters"))

    @field_validator('error_code')
    def error_code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('INVALID_ARGUMENT'):
            raise ValueError("must be one of enum values ('INVALID_ARGUMENT')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "extra": "forbid"
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str, *, allow_extra=False) -> Self:
        """Create an instance of InvalidPropertyFiltersCombination from a JSON string"""
        return cls.from_dict(json.loads(json_str), allow_extra=allow_extra)

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict, *, allow_extra=False) -> Self:
        """Create an instance of AsyncActionOperation from a dict"""
        # If allowing extra properties and the given object is a dict,
        # then remove any properties in the dict that aren't present
        # in the model properties list
        # We need to do this since the model config forbids additional properties
        # and this cannot be changed at runtime
        if (
            allow_extra and
            isinstance(obj, dict) and
            any(key not in cls.__properties for key in obj)
        ):
            obj = {key: value for key, value in obj.items() if key in cls.__properties}

        return cls.model_validate(obj)


