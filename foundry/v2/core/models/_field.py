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

from typing import cast

import pydantic

from foundry.v2.core.models._field_dict import FieldDict
from foundry.v2.core.models._field_name import FieldName
from foundry.v2.core.models._field_schema import FieldSchema


class Field(pydantic.BaseModel):
    """
    A field in a Foundry schema. For more information on supported data types, see the
    [supported field types](/docs/foundry/data-integration/datasets/#supported-field-types) user documentation.
    """

    name: FieldName

    schema_: FieldSchema = pydantic.Field(alias="schema")

    model_config = {"extra": "allow"}

    def to_dict(self) -> FieldDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(FieldDict, self.model_dump(by_alias=True, exclude_unset=True))
