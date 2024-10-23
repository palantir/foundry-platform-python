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

from typing import Optional
from typing import cast

import pydantic

from foundry.v2.core.models._display_name import DisplayName
from foundry.v2.functions.models._value_type_api_name import ValueTypeApiName
from foundry.v2.functions.models._value_type_data_type import ValueTypeDataType
from foundry.v2.functions.models._value_type_description import ValueTypeDescription
from foundry.v2.functions.models._value_type_dict import ValueTypeDict
from foundry.v2.functions.models._value_type_rid import ValueTypeRid
from foundry.v2.functions.models._value_type_version import ValueTypeVersion
from foundry.v2.functions.models._value_type_version_id import ValueTypeVersionId


class ValueType(pydantic.BaseModel):
    """ValueType"""

    rid: ValueTypeRid

    version: ValueTypeVersion

    version_id: ValueTypeVersionId = pydantic.Field(alias="versionId")

    api_name: ValueTypeApiName = pydantic.Field(alias="apiName")

    display_name: DisplayName = pydantic.Field(alias="displayName")

    description: Optional[ValueTypeDescription] = None

    base_type: Optional[ValueTypeDataType] = pydantic.Field(alias="baseType", default=None)

    model_config = {"extra": "allow"}

    def to_dict(self) -> ValueTypeDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(ValueTypeDict, self.model_dump(by_alias=True, exclude_unset=True))
