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
from typing import cast

from pydantic import BaseModel
from pydantic import Field

from foundry.v1.models._object_set import ObjectSet
from foundry.v1.models._object_set_stream_subscribe_request_dict import (
    ObjectSetStreamSubscribeRequestDict,
)  # NOQA
from foundry.v1.models._selected_property_api_name import SelectedPropertyApiName


class ObjectSetStreamSubscribeRequest(BaseModel):
    """ObjectSetStreamSubscribeRequest"""

    object_set: ObjectSet = Field(alias="objectSet")

    property_set: List[SelectedPropertyApiName] = Field(alias="propertySet")

    reference_set: List[SelectedPropertyApiName] = Field(alias="referenceSet")

    model_config = {"extra": "allow"}

    def to_dict(self) -> ObjectSetStreamSubscribeRequestDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            ObjectSetStreamSubscribeRequestDict, self.model_dump(by_alias=True, exclude_unset=True)
        )
