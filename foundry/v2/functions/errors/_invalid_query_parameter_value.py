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
from foundry.v2.functions.models._data_value import DataValue
from foundry.v2.functions.models._parameter_id import ParameterId
from foundry.v2.functions.models._query_data_type_dict import QueryDataTypeDict


class InvalidQueryParameterValueParameters(TypedDict):
    """
    The value of the given parameter is invalid. See the documentation of `DataValue` for details on
    how parameters are represented.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    parameterDataType: QueryDataTypeDict

    parameterId: ParameterId

    parameterValue: NotRequired[DataValue]


@dataclass
class InvalidQueryParameterValue(BadRequestError):
    name: Literal["InvalidQueryParameterValue"]
    parameters: InvalidQueryParameterValueParameters
    error_instance_id: str


__all__ = ["InvalidQueryParameterValue"]
