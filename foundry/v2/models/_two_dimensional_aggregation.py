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
from pydantic import Field

from foundry.v2.models._query_aggregation_key_type import QueryAggregationKeyType
from foundry.v2.models._query_aggregation_value_type import QueryAggregationValueType
from foundry.v2.models._two_dimensional_aggregation_dict import (
    TwoDimensionalAggregationDict,
)  # NOQA


class TwoDimensionalAggregation(BaseModel):
    """TwoDimensionalAggregation"""

    key_type: QueryAggregationKeyType = Field(alias="keyType")

    value_type: QueryAggregationValueType = Field(alias="valueType")

    type: Literal["twoDimensionalAggregation"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> TwoDimensionalAggregationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            TwoDimensionalAggregationDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
