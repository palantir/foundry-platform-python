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

from typing import Union

import pydantic
from typing_extensions import Annotated

from foundry.v2.core.models._filter_binary_type_dict import FilterBinaryTypeDict
from foundry.v2.core.models._filter_boolean_type_dict import FilterBooleanTypeDict
from foundry.v2.core.models._filter_date_time_type_dict import FilterDateTimeTypeDict
from foundry.v2.core.models._filter_date_type_dict import FilterDateTypeDict
from foundry.v2.core.models._filter_double_type_dict import FilterDoubleTypeDict
from foundry.v2.core.models._filter_enum_type_dict import FilterEnumTypeDict
from foundry.v2.core.models._filter_float_type_dict import FilterFloatTypeDict
from foundry.v2.core.models._filter_integer_type_dict import FilterIntegerTypeDict
from foundry.v2.core.models._filter_long_type_dict import FilterLongTypeDict
from foundry.v2.core.models._filter_rid_type_dict import FilterRidTypeDict
from foundry.v2.core.models._filter_string_type_dict import FilterStringTypeDict
from foundry.v2.core.models._filter_uuid_type_dict import FilterUuidTypeDict

FilterTypeDict = Annotated[
    Union[
        FilterDateTimeTypeDict,
        FilterDateTypeDict,
        FilterBooleanTypeDict,
        FilterStringTypeDict,
        FilterDoubleTypeDict,
        FilterBinaryTypeDict,
        FilterIntegerTypeDict,
        FilterFloatTypeDict,
        FilterRidTypeDict,
        FilterUuidTypeDict,
        FilterEnumTypeDict,
        FilterLongTypeDict,
    ],
    pydantic.Field(discriminator="type"),
]
"""FilterType"""
