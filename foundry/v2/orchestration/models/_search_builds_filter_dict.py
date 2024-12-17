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
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry.v2.orchestration.models._search_builds_equals_filter_dict import (
    SearchBuildsEqualsFilterDict,
)  # NOQA
from foundry.v2.orchestration.models._search_builds_gte_filter_dict import (
    SearchBuildsGteFilterDict,
)  # NOQA
from foundry.v2.orchestration.models._search_builds_lt_filter_dict import (
    SearchBuildsLtFilterDict,
)  # NOQA


class SearchBuildsNotFilterDict(TypedDict):
    """Returns the Builds where the filter is not satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: SearchBuildsFilterDict

    type: Literal["not"]


class SearchBuildsOrFilterDict(TypedDict):
    """Returns the Builds where at least one filter is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    items: List[SearchBuildsFilterDict]

    type: Literal["or"]


class SearchBuildsAndFilterDict(TypedDict):
    """Returns the Builds where every filter is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    items: List[SearchBuildsFilterDict]

    type: Literal["and"]


SearchBuildsFilterDict = Annotated[
    Union[
        SearchBuildsNotFilterDict,
        SearchBuildsOrFilterDict,
        SearchBuildsAndFilterDict,
        SearchBuildsLtFilterDict,
        SearchBuildsGteFilterDict,
        SearchBuildsEqualsFilterDict,
    ],
    pydantic.Field(discriminator="type"),
]
"""SearchBuildsFilter"""
