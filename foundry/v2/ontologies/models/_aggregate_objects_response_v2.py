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
from typing import Optional
from typing import cast

import pydantic

from foundry.v2.ontologies.models._aggregate_objects_response_item_v2 import (
    AggregateObjectsResponseItemV2,
)  # NOQA
from foundry.v2.ontologies.models._aggregate_objects_response_v2_dict import (
    AggregateObjectsResponseV2Dict,
)  # NOQA
from foundry.v2.ontologies.models._aggregation_accuracy import AggregationAccuracy


class AggregateObjectsResponseV2(pydantic.BaseModel):
    """AggregateObjectsResponseV2"""

    excluded_items: Optional[pydantic.StrictInt] = pydantic.Field(
        alias="excludedItems", default=None
    )

    accuracy: AggregationAccuracy

    data: List[AggregateObjectsResponseItemV2]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AggregateObjectsResponseV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AggregateObjectsResponseV2Dict, self.model_dump(by_alias=True, exclude_unset=True)
        )
