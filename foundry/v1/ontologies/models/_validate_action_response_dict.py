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

from typing_extensions import TypedDict

from foundry.v1.ontologies.models._parameter_evaluation_result_dict import (
    ParameterEvaluationResultDict,
)  # NOQA
from foundry.v1.ontologies.models._parameter_id import ParameterId
from foundry.v1.ontologies.models._submission_criteria_evaluation_dict import (
    SubmissionCriteriaEvaluationDict,
)  # NOQA
from foundry.v1.ontologies.models._validation_result import ValidationResult


class ValidateActionResponseDict(TypedDict):
    """ValidateActionResponse"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    result: ValidationResult

    submissionCriteria: List[SubmissionCriteriaEvaluationDict]

    parameters: Dict[ParameterId, ParameterEvaluationResultDict]
