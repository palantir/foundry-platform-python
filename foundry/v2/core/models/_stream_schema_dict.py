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

from typing import List

from typing_extensions import NotRequired
from typing_extensions import TypedDict

from foundry.v2.core.models._change_data_capture_configuration_dict import (
    ChangeDataCaptureConfigurationDict,
)  # NOQA
from foundry.v2.core.models._field_dict import FieldDict
from foundry.v2.core.models._field_name import FieldName


class StreamSchemaDict(TypedDict):
    """The schema for a Foundry stream. Records pushed to this stream must match this schema."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    fields: List[FieldDict]

    keyFieldNames: NotRequired[List[FieldName]]
    """
    The names of the fields to be used as keys for partitioning records. These key fields are used to group
    all records with the same key into the same partition, to guarantee processing order of grouped records. These
    keys are not meant to uniquely identify records, and do not by themselves deduplicate records. To deduplicate
    records, provide a change data capture configuration for the schema.

    Key fields can only be of the following types:
    - Boolean
    - Byte
    - Date
    - Decimal
    - Integer
    - Long
    - Short
    - String
    - Timestamp

    For additional information on keys for Foundry streams, see the
    [streaming keys](/docs/foundry/building-pipelines/streaming-keys/) user documentation.
    """

    changeDataCapture: NotRequired[ChangeDataCaptureConfigurationDict]
