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

from foundry.v1.models._contains_query_v2_dict import ContainsQueryV2Dict
from foundry.v1.models._property_api_name import PropertyApiName
from foundry.v1.models._property_value import PropertyValue


class ContainsQueryV2(BaseModel):
    """Returns objects where the specified array contains a value."""

    field: PropertyApiName

    value: PropertyValue

    type: Literal["contains"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ContainsQueryV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ContainsQueryV2Dict, self.model_dump(by_alias=True, exclude_unset=True))
