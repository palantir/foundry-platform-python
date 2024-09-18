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

from typing import Literal
from typing import cast

from pydantic import BaseModel

from foundry.v2.ontologies.models._unevaluable_constraint_dict import (
    UnevaluableConstraintDict,
)  # NOQA


class UnevaluableConstraint(BaseModel):
    """
    The parameter cannot be evaluated because it depends on another parameter or object set that can't be evaluated.
    This can happen when a parameter's allowed values are defined by another parameter that is missing or invalid.
    """

    type: Literal["unevaluable"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> UnevaluableConstraintDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(UnevaluableConstraintDict, self.model_dump(by_alias=True, exclude_unset=True))
