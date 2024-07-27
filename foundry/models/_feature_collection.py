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
from typing import Optional
from typing import cast

from pydantic import BaseModel

from foundry.models._b_box import BBox
from foundry.models._feature_collection_dict import FeatureCollectionDict
from foundry.models._feature_collection_types import FeatureCollectionTypes


class FeatureCollection(BaseModel):
    """GeoJSon 'FeatureCollection' object"""

    features: List[FeatureCollectionTypes]

    bbox: Optional[BBox] = None

    type: Literal["FeatureCollection"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> FeatureCollectionDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FeatureCollectionDict, self.model_dump(by_alias=True, exclude_unset=True))
