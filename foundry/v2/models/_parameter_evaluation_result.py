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
from typing import cast

from pydantic import BaseModel
from pydantic import Field
from pydantic import StrictBool

from foundry.v2.models._parameter_evaluated_constraint import ParameterEvaluatedConstraint  # NOQA
from foundry.v2.models._parameter_evaluation_result_dict import (
    ParameterEvaluationResultDict,
)  # NOQA
from foundry.v2.models._validation_result import ValidationResult


class ParameterEvaluationResult(BaseModel):
    """Represents the validity of a parameter against the configured constraints."""

    result: ValidationResult

    evaluated_constraints: List[ParameterEvaluatedConstraint] = Field(alias="evaluatedConstraints")

    required: StrictBool
    """Represents whether the parameter is a required input to the action."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> ParameterEvaluationResultDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ParameterEvaluationResultDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
