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

from foundry.v2.core.models._custom_metadata import CustomMetadata
from foundry.v2.core.models._field_data_type import FieldDataType
from foundry.v2.core.models._field_schema_dict import FieldSchemaDict


class FieldSchema(pydantic.BaseModel):
    """The specification of the type of a Foundry schema field."""

    nullable: pydantic.StrictBool

    custom_metadata: Optional[CustomMetadata] = pydantic.Field(alias="customMetadata", default=None)

    data_type: FieldDataType = pydantic.Field(alias="dataType")

    model_config = {"extra": "allow"}

    def to_dict(self) -> FieldSchemaDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FieldSchemaDict, self.model_dump(by_alias=True, exclude_unset=True))
