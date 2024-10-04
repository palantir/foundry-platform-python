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

from typing_extensions import TypedDict

from foundry.v2.ontologies.models._object_set_dict import ObjectSetDict


class ObjectSetAsBaseObjectTypesTypeDict(TypedDict):
    """
    Casts the objects in the object set to their base type and thus ensures objects are returned with all of their
    properties in the resulting object set, not just the properties that implement interface properties. This is
    currently unsupported and an exception will be thrown if used.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    type: Literal["asBaseObjectTypes"]
