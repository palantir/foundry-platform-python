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

from typing import Dict
from typing import List
from typing import cast

import pydantic

from foundry.v2.ontologies.models._parameter_evaluation_result import (
    ParameterEvaluationResult,
)  # NOQA
from foundry.v2.ontologies.models._parameter_id import ParameterId
from foundry.v2.ontologies.models._submission_criteria_evaluation import (
    SubmissionCriteriaEvaluation,
)  # NOQA
from foundry.v2.ontologies.models._validate_action_response_v2_dict import (
    ValidateActionResponseV2Dict,
)  # NOQA
from foundry.v2.ontologies.models._validation_result import ValidationResult


class ValidateActionResponseV2(pydantic.BaseModel):
    """ValidateActionResponseV2"""

    result: ValidationResult

    submission_criteria: List[SubmissionCriteriaEvaluation] = pydantic.Field(
        alias="submissionCriteria"
    )

    parameters: Dict[ParameterId, ParameterEvaluationResult]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ValidateActionResponseV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ValidateActionResponseV2Dict, self.model_dump(by_alias=True, exclude_unset=True)
        )
