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

from typing import List
from typing import Literal
from typing import cast

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictBool

from foundry.v1.models._one_of_constraint_dict import OneOfConstraintDict
from foundry.v1.models._parameter_option import ParameterOption


class OneOfConstraint(BaseModel):
    """The parameter has a manually predefined set of options."""

    options: List[ParameterOption]

    other_values_allowed: StrictBool = Field(alias="otherValuesAllowed")
    """A flag denoting whether custom, user provided values will be considered valid. This is configured via the **Allowed "Other" value** toggle in the **Ontology Manager**."""

    type: Literal["oneOf"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> OneOfConstraintDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OneOfConstraintDict, self.model_dump(by_alias=True, exclude_unset=True))
