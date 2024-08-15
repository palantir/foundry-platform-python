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

from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional
from typing import cast

from pydantic import BaseModel

from foundry.v1.models._b_box import BBox
from foundry.v1.models._feature_dict import FeatureDict
from foundry.v1.models._feature_property_key import FeaturePropertyKey
from foundry.v1.models._geometry import Geometry


class Feature(BaseModel):
    """GeoJSon 'Feature' object"""

    geometry: Optional[Geometry] = None

    properties: Dict[FeaturePropertyKey, Any]
    """
    A `Feature` object has a member with the name "properties".  The
    value of the properties member is an object (any JSON object or a
    JSON null value).
    """

    id: Optional[Any] = None
    """
    If a `Feature` has a commonly used identifier, that identifier
    SHOULD be included as a member of the Feature object with the name
    "id", and the value of this member is either a JSON string or
    number.
    """

    bbox: Optional[BBox] = None

    type: Literal["Feature"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> FeatureDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FeatureDict, self.model_dump(by_alias=True, exclude_unset=True))
