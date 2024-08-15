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

from foundry.v2.models._contains_all_terms_in_order_prefix_last_term_dict import (
    ContainsAllTermsInOrderPrefixLastTermDict,
)  # NOQA
from foundry.v2.models._contains_all_terms_in_order_query_dict import (
    ContainsAllTermsInOrderQueryDict,
)  # NOQA
from foundry.v2.models._contains_all_terms_query_dict import ContainsAllTermsQueryDict
from foundry.v2.models._contains_any_term_query_dict import ContainsAnyTermQueryDict
from foundry.v2.models._contains_query_v2_dict import ContainsQueryV2Dict
from foundry.v2.models._does_not_intersect_bounding_box_query_dict import (
    DoesNotIntersectBoundingBoxQueryDict,
)  # NOQA
from foundry.v2.models._does_not_intersect_polygon_query_dict import (
    DoesNotIntersectPolygonQueryDict,
)  # NOQA
from foundry.v2.models._equals_query_v2_dict import EqualsQueryV2Dict
from foundry.v2.models._gt_query_v2_dict import GtQueryV2Dict
from foundry.v2.models._gte_query_v2_dict import GteQueryV2Dict
from foundry.v2.models._intersects_bounding_box_query_dict import (
    IntersectsBoundingBoxQueryDict,
)  # NOQA
from foundry.v2.models._intersects_polygon_query_dict import IntersectsPolygonQueryDict
from foundry.v2.models._is_null_query_v2_dict import IsNullQueryV2Dict
from foundry.v2.models._lt_query_v2_dict import LtQueryV2Dict
from foundry.v2.models._lte_query_v2_dict import LteQueryV2Dict
from foundry.v2.models._starts_with_query_dict import StartsWithQueryDict
from foundry.v2.models._within_bounding_box_query_dict import WithinBoundingBoxQueryDict
from foundry.v2.models._within_distance_of_query_dict import WithinDistanceOfQueryDict
from foundry.v2.models._within_polygon_query_dict import WithinPolygonQueryDict


class AndQueryV2Dict(TypedDict):
    """Returns objects where every query is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: List[SearchJsonQueryV2Dict]

    type: Literal["and"]


class OrQueryV2Dict(TypedDict):
    """Returns objects where at least 1 query is satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: List[SearchJsonQueryV2Dict]

    type: Literal["or"]


class NotQueryV2Dict(TypedDict):
    """Returns objects where the query is not satisfied."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    value: SearchJsonQueryV2Dict

    type: Literal["not"]


SearchJsonQueryV2Dict = Annotated[
    Union[
        LtQueryV2Dict,
        GtQueryV2Dict,
        LteQueryV2Dict,
        GteQueryV2Dict,
        EqualsQueryV2Dict,
        IsNullQueryV2Dict,
        ContainsQueryV2Dict,
        AndQueryV2Dict,
        OrQueryV2Dict,
        NotQueryV2Dict,
        StartsWithQueryDict,
        ContainsAllTermsInOrderQueryDict,
        ContainsAllTermsInOrderPrefixLastTermDict,
        ContainsAnyTermQueryDict,
        ContainsAllTermsQueryDict,
        WithinDistanceOfQueryDict,
        WithinBoundingBoxQueryDict,
        IntersectsBoundingBoxQueryDict,
        DoesNotIntersectBoundingBoxQueryDict,
        WithinPolygonQueryDict,
        IntersectsPolygonQueryDict,
        DoesNotIntersectPolygonQueryDict,
    ],
    Field(discriminator="type"),
]
"""SearchJsonQueryV2"""
