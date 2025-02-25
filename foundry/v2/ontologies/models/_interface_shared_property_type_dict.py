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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.ontologies.models._object_property_type_dict import ObjectPropertyTypeDict  # NOQA
from foundry.v2.ontologies.models._shared_property_type_api_name import (
    SharedPropertyTypeApiName,
)  # NOQA
from foundry.v2.ontologies.models._shared_property_type_rid import SharedPropertyTypeRid


class InterfaceSharedPropertyTypeDict(TypedDict):
    """
    A shared property type with an additional field to indicate whether the property must be included on every
    object type that implements the interface, or whether it is optional.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: SharedPropertyTypeRid

    apiName: SharedPropertyTypeApiName

    displayName: DisplayName

    description: NotRequired[str]
    """A short text that describes the SharedPropertyType."""

    dataType: ObjectPropertyTypeDict

    required: bool
    """Whether each implementing object type must declare an implementation for this property."""
