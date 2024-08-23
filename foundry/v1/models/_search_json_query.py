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
from typing import cast

from pydantic import BaseModel
from pydantic import Field

from foundry.v1.models._all_terms_query import AllTermsQuery
from foundry.v1.models._any_term_query import AnyTermQuery
from foundry.v1.models._contains_query import ContainsQuery
from foundry.v1.models._equals_query import EqualsQuery
from foundry.v1.models._gt_query import GtQuery
from foundry.v1.models._gte_query import GteQuery
from foundry.v1.models._is_null_query import IsNullQuery
from foundry.v1.models._lt_query import LtQuery
from foundry.v1.models._lte_query import LteQuery
from foundry.v1.models._phrase_query import PhraseQuery
from foundry.v1.models._prefix_query import PrefixQuery
from foundry.v1.models._search_json_query_dict import AndQueryDict
from foundry.v1.models._search_json_query_dict import NotQueryDict
from foundry.v1.models._search_json_query_dict import OrQueryDict


class AndQuery(BaseModel):
    """Returns objects where every query is satisfied."""

    value: List[SearchJsonQuery]

    type: Literal["and"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AndQueryDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AndQueryDict, self.model_dump(by_alias=True, exclude_unset=True))


class OrQuery(BaseModel):
    """Returns objects where at least 1 query is satisfied."""

    value: List[SearchJsonQuery]

    type: Literal["or"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> OrQueryDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OrQueryDict, self.model_dump(by_alias=True, exclude_unset=True))


class NotQuery(BaseModel):
    """Returns objects where the query is not satisfied."""

    value: SearchJsonQuery

    type: Literal["not"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> NotQueryDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(NotQueryDict, self.model_dump(by_alias=True, exclude_unset=True))


SearchJsonQuery = Annotated[
    Union[
        LtQuery,
        GtQuery,
        LteQuery,
        GteQuery,
        EqualsQuery,
        IsNullQuery,
        ContainsQuery,
        AndQuery,
        OrQuery,
        NotQuery,
        PrefixQuery,
        PhraseQuery,
        AnyTermQuery,
        AllTermsQuery,
    ],
    Field(discriminator="type"),
]
"""SearchJsonQuery"""
