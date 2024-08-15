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
from typing import Union

from pydantic import Field

from foundry.v2.models._boolean_type_dict import BooleanTypeDict
from foundry.v2.models._date_type_dict import DateTypeDict
from foundry.v2.models._double_type_dict import DoubleTypeDict
from foundry.v2.models._integer_type_dict import IntegerTypeDict
from foundry.v2.models._query_aggregation_range_type_dict import (
    QueryAggregationRangeTypeDict,
)  # NOQA
from foundry.v2.models._string_type_dict import StringTypeDict
from foundry.v2.models._timestamp_type_dict import TimestampTypeDict

QueryAggregationKeyTypeDict = Annotated[
    Union[
        BooleanTypeDict,
        DateTypeDict,
        DoubleTypeDict,
        IntegerTypeDict,
        StringTypeDict,
        TimestampTypeDict,
        QueryAggregationRangeTypeDict,
    ],
    Field(discriminator="type"),
]
"""A union of all the types supported by query aggregation keys."""
