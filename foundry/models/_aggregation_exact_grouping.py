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
from pydantic import Field
from pydantic import StrictInt

from foundry.models._aggregation_exact_grouping_dict import AggregationExactGroupingDict
from foundry.models._field_name_v1 import FieldNameV1


class AggregationExactGrouping(BaseModel):
    """Divides objects into groups according to an exact value."""

    field: FieldNameV1

    max_group_count: Optional[StrictInt] = Field(alias="maxGroupCount", default=None)

    type: Literal["exact"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AggregationExactGroupingDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AggregationExactGroupingDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
