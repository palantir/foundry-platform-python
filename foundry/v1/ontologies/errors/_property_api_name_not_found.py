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


class PropertyApiNameNotFoundParameters(typing_extensions.TypedDict):
    """
    A property that was required to have an API name, such as a primary key, is missing one. You can set an API
    name for it using the **Ontology Manager**.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyId: ontologies_models.PropertyId
    propertyBaseType: ontologies_models.ValueType


@dataclass
class PropertyApiNameNotFound(errors.BadRequestError):
    name: typing.Literal["PropertyApiNameNotFound"]
    parameters: PropertyApiNameNotFoundParameters
    error_instance_id: str


__all__ = ["PropertyApiNameNotFound"]
