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

from typing import Dict

from pydantic import StrictStr
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.models._display_name import DisplayName
from foundry.models._object_type_api_name import ObjectTypeApiName
from foundry.models._object_type_rid import ObjectTypeRid
from foundry.models._object_type_visibility import ObjectTypeVisibility
from foundry.models._property_api_name import PropertyApiName
from foundry.models._property_v2_dict import PropertyV2Dict
from foundry.models._release_status import ReleaseStatus


class ObjectTypeV2Dict(TypedDict):
    """Represents an object type in the Ontology."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    apiName: ObjectTypeApiName

    displayName: NotRequired[DisplayName]

    status: ReleaseStatus

    description: NotRequired[StrictStr]
    """The description of the object type."""

    primaryKey: PropertyApiName

    properties: Dict[PropertyApiName, PropertyV2Dict]
    """A map of the properties of the object type."""

    rid: ObjectTypeRid

    titleProperty: PropertyApiName

    visibility: NotRequired[ObjectTypeVisibility]
