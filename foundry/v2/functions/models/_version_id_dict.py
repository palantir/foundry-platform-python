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

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.functions.models._value_type_api_name import ValueTypeApiName
from foundry.v2.functions.models._value_type_data_type_dict import ValueTypeDataTypeDict
from foundry.v2.functions.models._value_type_description import ValueTypeDescription
from foundry.v2.functions.models._value_type_rid import ValueTypeRid
from foundry.v2.functions.models._value_type_version import ValueTypeVersion
from foundry.v2.functions.models._value_type_version_id import ValueTypeVersionId


class VersionIdDict(TypedDict):
    """VersionId"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rid: ValueTypeRid

    version: ValueTypeVersion

    versionId: ValueTypeVersionId

    apiName: ValueTypeApiName

    displayName: DisplayName

    description: NotRequired[ValueTypeDescription]

    baseType: NotRequired[ValueTypeDataTypeDict]
