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

from typing import Optional
from typing import cast

import pydantic

from foundry.v1.core.models._display_name import DisplayName
from foundry.v1.core.models._release_status import ReleaseStatus
from foundry.v1.ontologies.models._link_type_api_name import LinkTypeApiName
from foundry.v1.ontologies.models._link_type_side_cardinality import LinkTypeSideCardinality  # NOQA
from foundry.v1.ontologies.models._link_type_side_dict import LinkTypeSideDict
from foundry.v1.ontologies.models._object_type_api_name import ObjectTypeApiName
from foundry.v1.ontologies.models._property_api_name import PropertyApiName


class LinkTypeSide(pydantic.BaseModel):
    """LinkTypeSide"""

    api_name: LinkTypeApiName = pydantic.Field(alias="apiName")

    display_name: DisplayName = pydantic.Field(alias="displayName")

    status: ReleaseStatus

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias="objectTypeApiName")

    cardinality: LinkTypeSideCardinality

    foreign_key_property_api_name: Optional[PropertyApiName] = pydantic.Field(
        alias="foreignKeyPropertyApiName", default=None
    )

    model_config = {"extra": "allow"}

    def to_dict(self) -> LinkTypeSideDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(LinkTypeSideDict, self.model_dump(by_alias=True, exclude_unset=True))
