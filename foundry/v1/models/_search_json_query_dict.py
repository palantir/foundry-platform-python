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

from typing import Annotated
from typing import List
from typing import Literal
from typing import Union

from pydantic import Field
from typing_extensions import TypedDict

from foundry.v1.models._all_terms_query_dict import AllTermsQueryDict
from foundry.v1.models._any_term_query_dict import AnyTermQueryDict
from foundry.v1.models._contains_query_dict import ContainsQueryDict
from foundry.v1.models._equals_query_dict import EqualsQueryDict
from foundry.v1.models._gt_query_dict import GtQueryDict
from foundry.v1.models._gte_query_dict import GteQueryDict
from foundry.v1.models._is_null_query_dict import IsNullQueryDict
from foundry.v1.models._lt_query_dict import LtQueryDict
from foundry.v1.models._lte_query_dict import LteQueryDict
from foundry.v1.models._phrase_query_dict import PhraseQueryDict
from foundry.v1.models._prefix_query_dict import PrefixQueryDict


class AndQueryDict(TypedDict):
    """Returns objects where every query is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: List[SearchJsonQueryDict]

    type: Literal["and"]


class OrQueryDict(TypedDict):
    """Returns objects where at least 1 query is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: List[SearchJsonQueryDict]

    type: Literal["or"]


class NotQueryDict(TypedDict):
    """Returns objects where the query is not satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: SearchJsonQueryDict

    type: Literal["not"]


SearchJsonQueryDict = Annotated[
    Union[
        LtQueryDict,
        GtQueryDict,
        LteQueryDict,
        GteQueryDict,
        EqualsQueryDict,
        IsNullQueryDict,
        ContainsQueryDict,
        AndQueryDict,
        OrQueryDict,
        NotQueryDict,
        PrefixQueryDict,
        PhraseQueryDict,
        AnyTermQueryDict,
        AllTermsQueryDict,
    ],
    Field(discriminator="type"),
]
"""SearchJsonQuery"""
