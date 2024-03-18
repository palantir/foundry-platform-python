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
from typing import TypedDict
from typing import Union

from pydantic import Field
from typing_extensions import NotRequired


from foundry.models._all_terms_query_request import AllTermsQueryRequest
from foundry.models._any_term_query_request import AnyTermQueryRequest
from foundry.models._contains_query_request import ContainsQueryRequest
from foundry.models._equals_query_request import EqualsQueryRequest
from foundry.models._gt_query_request import GtQueryRequest
from foundry.models._gte_query_request import GteQueryRequest
from foundry.models._is_null_query_request import IsNullQueryRequest
from foundry.models._lt_query_request import LtQueryRequest
from foundry.models._lte_query_request import LteQueryRequest
from foundry.models._phrase_query_request import PhraseQueryRequest
from foundry.models._prefix_query_request import PrefixQueryRequest


class AndQueryRequest(TypedDict):
    """Returns objects where every query is satisfied."""

    __pydantic_config__ = {"extra": "forbid"}  # type: ignore

    value: NotRequired[List[SearchJsonQueryRequest]]

    type: Literal["and"]


class OrQueryRequest(TypedDict):
    """Returns objects where at least 1 query is satisfied."""

    __pydantic_config__ = {"extra": "forbid"}  # type: ignore

    value: NotRequired[List[SearchJsonQueryRequest]]

    type: Literal["or"]


class NotQueryRequest(TypedDict):
    """Returns objects where the query is not satisfied."""

    __pydantic_config__ = {"extra": "forbid"}  # type: ignore

    value: SearchJsonQueryRequest
    """SearchJsonQueryRequest"""

    type: Literal["not"]


SearchJsonQueryRequest = Annotated[
    Union[
        AllTermsQueryRequest,
        AndQueryRequest,
        AnyTermQueryRequest,
        ContainsQueryRequest,
        EqualsQueryRequest,
        GtQueryRequest,
        GteQueryRequest,
        IsNullQueryRequest,
        LtQueryRequest,
        LteQueryRequest,
        NotQueryRequest,
        OrQueryRequest,
        PhraseQueryRequest,
        PrefixQueryRequest,
    ],
    Field(discriminator="type"),
]
"""SearchJsonQueryRequest"""
