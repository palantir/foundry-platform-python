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

from pydantic import BaseModel
from pydantic import Field

from foundry.models._aggregate_objects_request_dict import AggregateObjectsRequestDict
from foundry.models._aggregation import Aggregation
from foundry.models._aggregation_group_by import AggregationGroupBy
from foundry.models._search_json_query import SearchJsonQuery


class AggregateObjectsRequest(BaseModel):
    """AggregateObjectsRequest"""

    aggregation: List[Aggregation]

    group_by: List[AggregationGroupBy] = Field(alias="groupBy")

    query: Optional[SearchJsonQuery] = None

    model_config = {"extra": "allow"}

    def to_dict(self) -> AggregateObjectsRequestDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AggregateObjectsRequestDict, self.model_dump(by_alias=True, exclude_unset=True))
