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

from pydantic import StrictStr
from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.ontologies.models._object_property_type_dict import ObjectPropertyTypeDict  # NOQA


class PropertyV2Dict(TypedDict):
    """Details about some property of an object."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    description: NotRequired[StrictStr]

    displayName: NotRequired[DisplayName]

    dataType: ObjectPropertyTypeDict
