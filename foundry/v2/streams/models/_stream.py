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

from foundry.v2.core.models._stream_schema import StreamSchema
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.streams.models._compressed import Compressed
from foundry.v2.streams.models._partitions_count import PartitionsCount
from foundry.v2.streams.models._stream_dict import StreamDict
from foundry.v2.streams.models._stream_type import StreamType
from foundry.v2.streams.models._view_rid import ViewRid


class Stream(pydantic.BaseModel):
    """Stream"""

    branch_name: BranchName = pydantic.Field(alias="branchName")

    schema_: StreamSchema = pydantic.Field(alias="schema")
    """The Foundry schema for this stream."""

    view_rid: ViewRid = pydantic.Field(alias="viewRid")
    """The view that this stream corresponds to."""

    partitions_count: PartitionsCount = pydantic.Field(alias="partitionsCount")
    """
    The number of partitions for the Foundry stream. Defaults to 1.

    Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions
    are recommended.
    """

    stream_type: StreamType = pydantic.Field(alias="streamType")
    """
    A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and
    LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
    """

    compressed: Compressed
    """Whether or not compression is enabled for the stream. Defaults to false."""

    model_config = {"extra": "allow"}

    def to_dict(self) -> StreamDict:
        """Return the dictionary representation of the model using the field aliases."""
        return cast(StreamDict, self.model_dump(by_alias=True, exclude_unset=True))
