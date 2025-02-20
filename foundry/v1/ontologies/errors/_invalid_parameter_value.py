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

from dataclasses import dataclass
from typing import Literal

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry._errors import BadRequestError
from foundry.v1.ontologies.models._data_value import DataValue
from foundry.v1.ontologies.models._ontology_data_type import OntologyDataType
from foundry.v1.ontologies.models._parameter_id import ParameterId
from foundry.v1.ontologies.models._value_type import ValueType


class InvalidParameterValueParameters(TypedDict):
    """
    The value of the given parameter is invalid. See the documentation of `DataValue` for details on
    how parameters are represented.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterBaseType: NotRequired[ValueType]

    parameterDataType: NotRequired[OntologyDataType]

    parameterId: ParameterId

    parameterValue: NotRequired[DataValue]


@dataclass
class InvalidParameterValue(BadRequestError):
    name: Literal["InvalidParameterValue"]
    parameters: InvalidParameterValueParameters
    error_instance_id: str


__all__ = ["InvalidParameterValue"]
