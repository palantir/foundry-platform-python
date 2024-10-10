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

from typing import Literal
from typing import cast

import pydantic

from foundry.v2.core.models._field_name import FieldName
from foundry.v2.core.models._full_row_change_data_capture_configuration_dict import (
    FullRowChangeDataCaptureConfigurationDict,
)  # NOQA


class FullRowChangeDataCaptureConfiguration(pydantic.BaseModel):
    """
    Configuration for change data capture which resolves the latest state of the dataset based on new full rows
    being pushed to the stream. For example, if a value for a row is updated, it is only sufficient to publish
    the entire new state of that row to the stream.
    """

    deletion_field_name: FieldName = pydantic.Field(alias="deletionFieldName")
    """The name of a boolean field in the schema that indicates whether or not a row has been deleted."""

    ordering_field_name: FieldName = pydantic.Field(alias="orderingFieldName")
    """
    The name of an ordering field that determines the newest state for a row in the dataset. 

    The ordering field can only be of the following types:
    - Byte
    - Date
    - Decimal
    - Integer
    - Long
    - Short
    - String
    - Timestamp
    """

    type: Literal["fullRow"]

    model_config = {"extra": "allow"}

    def to_dict(self) -> FullRowChangeDataCaptureConfigurationDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(
            FullRowChangeDataCaptureConfigurationDict,
            self.model_dump(by_alias=True, exclude_unset=True),
        )
