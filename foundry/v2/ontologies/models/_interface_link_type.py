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

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.ontologies.models._interface_link_type_api_name import (
    InterfaceLinkTypeApiName,
)  # NOQA
from foundry.v2.ontologies.models._interface_link_type_cardinality import (
    InterfaceLinkTypeCardinality,
)  # NOQA
from foundry.v2.ontologies.models._interface_link_type_dict import InterfaceLinkTypeDict
from foundry.v2.ontologies.models._interface_link_type_linked_entity_api_name import (
    InterfaceLinkTypeLinkedEntityApiName,
)  # NOQA
from foundry.v2.ontologies.models._interface_link_type_rid import InterfaceLinkTypeRid


class InterfaceLinkType(pydantic.BaseModel):
    """
    A link type constraint defined at the interface level where the implementation of the links is provided
    by the implementing object types.
    """

    rid: InterfaceLinkTypeRid

    api_name: InterfaceLinkTypeApiName = pydantic.Field(alias="apiName")

    display_name: DisplayName = pydantic.Field(alias="displayName")

    description: Optional[pydantic.StrictStr] = None
    """The description of the interface link type."""

    linked_entity_api_name: InterfaceLinkTypeLinkedEntityApiName = pydantic.Field(
        alias="linkedEntityApiName"
    )

    cardinality: InterfaceLinkTypeCardinality

    required: pydantic.StrictBool
    """Whether each implementing object type must declare at least one implementation of this link."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> InterfaceLinkTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(InterfaceLinkTypeDict, self.model_dump(by_alias=True, exclude_unset=True))
