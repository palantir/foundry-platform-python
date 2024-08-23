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

from typing import Optional
from typing import cast

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictBool
from pydantic import StrictStr

from foundry.v2.models._ontology_data_type import OntologyDataType
from foundry.v2.models._parameter_dict import ParameterDict
from foundry.v2.models._value_type import ValueType


class Parameter(BaseModel):
    """Details about a parameter of an action or query."""

    description: Optional[StrictStr] = None

    base_type: ValueType = Field(alias="baseType")

    data_type: Optional[OntologyDataType] = Field(alias="dataType", default=None)

    required: StrictBool

    model_config = {"extra": "allow"}

    def to_dict(self) -> ParameterDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ParameterDict, self.model_dump(by_alias=True, exclude_unset=True))
