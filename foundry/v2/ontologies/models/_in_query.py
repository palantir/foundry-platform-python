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

from foundry.v2.ontologies.models._in_query_dict import InQueryDict
from foundry.v2.ontologies.models._property_api_name import PropertyApiName
from foundry.v2.ontologies.models._property_value import PropertyValue


class InQuery(BaseModel):
    """Returns objects where the specified field equals any of the provided values."""

    field: PropertyApiName

    value: List[PropertyValue]

    type: Literal["in"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> InQueryDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(InQueryDict, self.model_dump(by_alias=True, exclude_unset=True))
