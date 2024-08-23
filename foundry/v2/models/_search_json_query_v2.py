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

from foundry.v2.models._contains_all_terms_in_order_prefix_last_term import (
    ContainsAllTermsInOrderPrefixLastTerm,
)  # NOQA
from foundry.v2.models._contains_all_terms_in_order_query import (
    ContainsAllTermsInOrderQuery,
)  # NOQA
from foundry.v2.models._contains_all_terms_query import ContainsAllTermsQuery
from foundry.v2.models._contains_any_term_query import ContainsAnyTermQuery
from foundry.v2.models._contains_query_v2 import ContainsQueryV2
from foundry.v2.models._does_not_intersect_bounding_box_query import (
    DoesNotIntersectBoundingBoxQuery,
)  # NOQA
from foundry.v2.models._does_not_intersect_polygon_query import DoesNotIntersectPolygonQuery  # NOQA
from foundry.v2.models._equals_query_v2 import EqualsQueryV2
from foundry.v2.models._gt_query_v2 import GtQueryV2
from foundry.v2.models._gte_query_v2 import GteQueryV2
from foundry.v2.models._intersects_bounding_box_query import IntersectsBoundingBoxQuery
from foundry.v2.models._intersects_polygon_query import IntersectsPolygonQuery
from foundry.v2.models._is_null_query_v2 import IsNullQueryV2
from foundry.v2.models._lt_query_v2 import LtQueryV2
from foundry.v2.models._lte_query_v2 import LteQueryV2
from foundry.v2.models._search_json_query_v2_dict import AndQueryV2Dict
from foundry.v2.models._search_json_query_v2_dict import NotQueryV2Dict
from foundry.v2.models._search_json_query_v2_dict import OrQueryV2Dict
from foundry.v2.models._starts_with_query import StartsWithQuery
from foundry.v2.models._within_bounding_box_query import WithinBoundingBoxQuery
from foundry.v2.models._within_distance_of_query import WithinDistanceOfQuery
from foundry.v2.models._within_polygon_query import WithinPolygonQuery


class AndQueryV2(BaseModel):
    """Returns objects where every query is satisfied."""

    value: List[SearchJsonQueryV2]

    type: Literal["and"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> AndQueryV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(AndQueryV2Dict, self.model_dump(by_alias=True, exclude_unset=True))


class OrQueryV2(BaseModel):
    """Returns objects where at least 1 query is satisfied."""

    value: List[SearchJsonQueryV2]

    type: Literal["or"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> OrQueryV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(OrQueryV2Dict, self.model_dump(by_alias=True, exclude_unset=True))


class NotQueryV2(BaseModel):
    """Returns objects where the query is not satisfied."""

    value: SearchJsonQueryV2

    type: Literal["not"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> NotQueryV2Dict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(NotQueryV2Dict, self.model_dump(by_alias=True, exclude_unset=True))


SearchJsonQueryV2 = Annotated[
    Union[
        LtQueryV2,
        GtQueryV2,
        LteQueryV2,
        GteQueryV2,
        EqualsQueryV2,
        IsNullQueryV2,
        ContainsQueryV2,
        AndQueryV2,
        OrQueryV2,
        NotQueryV2,
        StartsWithQuery,
        ContainsAllTermsInOrderQuery,
        ContainsAllTermsInOrderPrefixLastTerm,
        ContainsAnyTermQuery,
        ContainsAllTermsQuery,
        WithinDistanceOfQuery,
        WithinBoundingBoxQuery,
        IntersectsBoundingBoxQuery,
        DoesNotIntersectBoundingBoxQuery,
        WithinPolygonQuery,
        IntersectsPolygonQuery,
        DoesNotIntersectPolygonQuery,
    ],
    Field(discriminator="type"),
]
"""SearchJsonQueryV2"""
