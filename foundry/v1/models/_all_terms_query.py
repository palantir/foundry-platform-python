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

from pydantic import BaseModel
from pydantic import StrictStr

from foundry.v1.models._all_terms_query_dict import AllTermsQueryDict
from foundry.v1.models._field_name_v1 import FieldNameV1
from foundry.v1.models._fuzzy import Fuzzy


class AllTermsQuery(BaseModel):
    """
    Returns objects where the specified field contains all of the whitespace separated words in any
    order in the provided value. This query supports fuzzy matching.
    """

    field: FieldNameV1

    value: StrictStr

    fuzzy: Optional[Fuzzy] = None

    type: Literal["allTerms"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AllTermsQueryDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AllTermsQueryDict, self.model_dump(by_alias=True, exclude_unset=True))
