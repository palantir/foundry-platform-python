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
from pydantic import StrictStr

from foundry.v1.models._submission_criteria_evaluation_dict import (
    SubmissionCriteriaEvaluationDict,
)  # NOQA
from foundry.v1.models._validation_result import ValidationResult


class SubmissionCriteriaEvaluation(BaseModel):
    """
    Contains the status of the **submission criteria**.
    **Submission criteria** are the prerequisites that need to be satisfied before an Action can be applied.
    These are configured in the **Ontology Manager**.
    """

    configured_failure_message: Optional[StrictStr] = Field(
        alias="configuredFailureMessage", default=None
    )
    """
    The message indicating one of the **submission criteria** was not satisfied.
    This is configured per **submission criteria** in the **Ontology Manager**.
    """

    result: ValidationResult

    model_config = {"extra": "allow"}

    def to_dict(self) -> SubmissionCriteriaEvaluationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            SubmissionCriteriaEvaluationDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
