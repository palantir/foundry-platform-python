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

from foundry.v2.ontologies.models._query_aggregation_key_type import QueryAggregationKeyType  # NOQA
from foundry.v2.ontologies.models._three_dimensional_aggregation_dict import (
    ThreeDimensionalAggregationDict,
)  # NOQA
from foundry.v2.ontologies.models._two_dimensional_aggregation import (
    TwoDimensionalAggregation,
)  # NOQA


class ThreeDimensionalAggregation(BaseModel):
    """ThreeDimensionalAggregation"""

    key_type: QueryAggregationKeyType = Field(alias="keyType")

    value_type: TwoDimensionalAggregation = Field(alias="valueType")

    type: Literal["threeDimensionalAggregation"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> ThreeDimensionalAggregationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ThreeDimensionalAggregationDict, self.model_dump(by_alias=True, exclude_unset=True)
        )