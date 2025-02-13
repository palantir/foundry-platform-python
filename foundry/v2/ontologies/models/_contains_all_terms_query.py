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

from foundry.v2.ontologies.models._contains_all_terms_query_dict import (
    ContainsAllTermsQueryDict,
)  # NOQA
from foundry.v2.ontologies.models._fuzzy_v2 import FuzzyV2
from foundry.v2.ontologies.models._property_api_name import PropertyApiName
from foundry.v2.ontologies.models._property_identifier import PropertyIdentifier


class ContainsAllTermsQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field contains all of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching. Allows you to specify a property to query on
    by a variety of means. Either `field` or `propertyIdentifier` must be supplied, but not both.
    """

    field: Optional[PropertyApiName] = None

    property_identifier: Optional[PropertyIdentifier] = pydantic.Field(alias=str("propertyIdentifier"), default=None)  # type: ignore[literal-required]

    value: str

    fuzzy: Optional[FuzzyV2] = None

    type: Literal["containsAllTerms"] = "containsAllTerms"

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> ContainsAllTermsQueryDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ContainsAllTermsQueryDict, self.model_dump(by_alias=True, exclude_none=True))
