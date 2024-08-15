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

from pydantic import StrictBool
from pydantic import StrictStr
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v1.models._display_name import DisplayName
from foundry.v1.models._interface_link_type_api_name import InterfaceLinkTypeApiName
from foundry.v1.models._interface_link_type_cardinality import InterfaceLinkTypeCardinality  # NOQA
from foundry.v1.models._interface_link_type_linked_entity_api_name_dict import (
    InterfaceLinkTypeLinkedEntityApiNameDict,
)  # NOQA
from foundry.v1.models._interface_link_type_rid import InterfaceLinkTypeRid


class InterfaceLinkTypeDict(TypedDict):
    """
    A link type constraint defined at the interface level where the implementation of the links is provided
    by the implementing object types.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: InterfaceLinkTypeRid

    apiName: InterfaceLinkTypeApiName

    displayName: DisplayName

    description: NotRequired[StrictStr]
    """The description of the interface link type."""

    linkedEntityApiName: InterfaceLinkTypeLinkedEntityApiNameDict

    cardinality: InterfaceLinkTypeCardinality

    required: StrictBool
    """Whether each implementing object type must declare at least one implementation of this link."""
