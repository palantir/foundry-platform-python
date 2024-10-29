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

from foundry.v2.ontologies.models._contains_any_term_query_dict import (
    ContainsAnyTermQueryDict,
)  # NOQA
from foundry.v2.ontologies.models._fuzzy_v2 import FuzzyV2
from foundry.v2.ontologies.models._property_api_name import PropertyApiName


class ContainsAnyTermQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field contains any of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching.
    """

    field: PropertyApiName

    value: pydantic.StrictStr

    fuzzy: Optional[FuzzyV2] = None

    type: Literal["containsAnyTerm"] = "containsAnyTerm"

    model_config = {"extra": "allow"}

    def to_dict(self) -> ContainsAnyTermQueryDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ContainsAnyTermQueryDict, self.model_dump(by_alias=True, exclude_unset=True))
