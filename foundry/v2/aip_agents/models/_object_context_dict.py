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

from typing_extensions import TypedDict

from foundry.v2.ontologies.models._object_rid import ObjectRid
from foundry.v2.ontologies.models._property_type_rid import PropertyTypeRid


class ObjectContextDict(TypedDict):
    """
    Details of relevant retrieved object instances for a user's message to include as
    additional context in the prompt to the Agent.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectRids: List[ObjectRid]
    """The RIDs of the relevant object instances to include in the prompt."""

    propertyTypeRids: List[PropertyTypeRid]
    """The RIDs of the property types for the given objects to include in the prompt."""

    type: Literal["objectContext"]
