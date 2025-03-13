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


import typing
from dataclasses import dataclass

import typing_extensions

from foundry import _errors as errors
from foundry.v1.ontologies import models as ontologies_models


class InvalidPropertyFilterValueParameters(typing_extensions.TypedDict):
    """
    The value of the given property filter is invalid. For instance, 2 is an invalid value for
    `isNull` in `properties.address.isNull=2` because the `isNull` filter expects a value of boolean type.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    expectedType: ontologies_models.ValueType
    propertyFilter: ontologies_models.PropertyFilter
    propertyFilterValue: ontologies_models.FilterValue
    property: ontologies_models.PropertyApiName


@dataclass
class InvalidPropertyFilterValue(errors.BadRequestError):
    name: typing.Literal["InvalidPropertyFilterValue"]
    parameters: InvalidPropertyFilterValueParameters
    error_instance_id: str


__all__ = ["InvalidPropertyFilterValue"]
