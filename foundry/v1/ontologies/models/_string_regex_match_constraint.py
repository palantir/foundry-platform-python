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
from typing import Optional
from typing import cast

import pydantic

from foundry.v1.ontologies.models._string_regex_match_constraint_dict import (
    StringRegexMatchConstraintDict,
)  # NOQA


class StringRegexMatchConstraint(pydantic.BaseModel):
    """The parameter value must match a predefined regular expression."""

    regex: pydantic.StrictStr
    """The regular expression configured in the **Ontology Manager**."""

    configured_failure_message: Optional[pydantic.StrictStr] = pydantic.Field(
        alias="configuredFailureMessage", default=None
    )
    """
    The message indicating that the regular expression was not matched.
    This is configured per parameter in the **Ontology Manager**.
    """

    type: Literal["stringRegexMatch"] = "stringRegexMatch"

    model_config = {"extra": "allow"}

    def to_dict(self) -> StringRegexMatchConstraintDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            StringRegexMatchConstraintDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
