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

import pydantic

from foundry.v2.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v2.ontologies.models._ontology_object_set_type_dict import (
    OntologyObjectSetTypeDict,
)  # NOQA


class OntologyObjectSetType(pydantic.BaseModel):
    """OntologyObjectSetType"""

    object_api_name: Optional[ObjectTypeApiName] = pydantic.Field(
        alias="objectApiName", default=None
    )

    object_type_api_name: Optional[ObjectTypeApiName] = pydantic.Field(
        alias="objectTypeApiName", default=None
    )

    type: Literal["objectSet"] = "objectSet"

    model_config = {"extra": "allow"}

    def to_dict(self) -> OntologyObjectSetTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OntologyObjectSetTypeDict, self.model_dump(by_alias=True, exclude_unset=True))
