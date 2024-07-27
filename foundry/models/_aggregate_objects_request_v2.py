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

from foundry.models._aggregate_objects_request_v2_dict import AggregateObjectsRequestV2Dict  # NOQA
from foundry.models._aggregation_accuracy_request import AggregationAccuracyRequest
from foundry.models._aggregation_group_by_v2 import AggregationGroupByV2
from foundry.models._aggregation_v2 import AggregationV2
from foundry.models._search_json_query_v2 import SearchJsonQueryV2


class AggregateObjectsRequestV2(BaseModel):
    """AggregateObjectsRequestV2"""

    aggregation: List[AggregationV2]

    where: Optional[SearchJsonQueryV2] = None

    group_by: List[AggregationGroupByV2] = Field(alias="groupBy")

    accuracy: Optional[AggregationAccuracyRequest] = None

    model_config = {"extra": "allow"}

    def to_dict(self) -> AggregateObjectsRequestV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            AggregateObjectsRequestV2Dict, self.model_dump(by_alias=True, exclude_unset=True)
        )
