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
from foundry.v2.ontologies.models._search_json_query_v2_dict import SearchJsonQueryV2Dict  # NOQA


class ObjectSetFilterTypeDict(TypedDict):
    """ObjectSetFilterType"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectSet: ObjectSetDict

    where: SearchJsonQueryV2Dict

    type: Literal["filter"]
