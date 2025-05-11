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

import typing

import pydantic

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.datasets import models as datasets_models
from foundry_sdk.v2.filesystem import models as filesystem_models

Compressed = bool
"""
Compression helps reduce the size of the data being sent, resulting in lower network usage and
storage, at the cost of some additional CPU usage for compression and decompression. This stream type
is only recommended if your stream contains a high volume of repetitive strings and is experiencing poor
network bandwidth symptoms like non-zero lag, lower than expected throughput, or dropped records.
"""


class CreateStreamRequestStreamSchema(pydantic.BaseModel):
    """CreateStreamRequestStreamSchema"""

    key_field_names: typing.Optional[typing.List[core_models.FieldName]] = pydantic.Field(alias=str("keyFieldNames"), default=None)  # type: ignore[literal-required]
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
    [streaming keys](https://palantir.com/docs/foundry/building-pipelines/streaming-keys/) user documentation.
    """

    fields: typing.List[core_models.Field]
    change_data_capture: typing.Optional[core_models.ChangeDataCaptureConfiguration] = pydantic.Field(alias=str("changeDataCapture"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Dataset(pydantic.BaseModel):
    """Dataset"""

    rid: datasets_models.DatasetRid
    name: datasets_models.DatasetName
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


PartitionsCount = int
"""The number of partitions for a Foundry stream."""


Record = typing.Dict[str, typing.Optional[typing.Any]]
"""A record to be published to a stream."""


class Stream(pydantic.BaseModel):
    """Stream"""

    branch_name: datasets_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    schema_: core_models.StreamSchema = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    """The Foundry schema for this stream."""

    view_rid: ViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]
    """The view that this stream corresponds to."""

    partitions_count: PartitionsCount = pydantic.Field(alias=str("partitionsCount"))  # type: ignore[literal-required]
    """
    The number of partitions for the Foundry stream. Defaults to 1.

    Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions
    are recommended.
    """

    stream_type: StreamType = pydantic.Field(alias=str("streamType"))  # type: ignore[literal-required]
    """
    A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and
    LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
    """

    compressed: Compressed
    """Whether or not compression is enabled for the stream. Defaults to false."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


StreamType = typing.Literal["LOW_LATENCY", "HIGH_THROUGHPUT"]
"""
LOW_LATENCY: The default stream type. Recommended for most use cases.

HIGH_THROUGHPUT: Best for streams that send large amounts of data every second. Using this stream type might
introduce some non-zero latency at the expense of a higher throughput. This stream type is only
recommended if you inspect your stream metrics in-platform and observe that the average batch size is equal
to the max match size, or if jobs using the stream are failing due to Kafka producer batches expiring. For
additional information on inspecting stream metrics, refer to the 
(stream monitoring)[/docs/foundry/data-integration/stream-monitoring/#viewing-metrics] documentation.

For more information, refer to the [stream types](https://palantir.com/docs/foundry/data-integration/streams/#stream-types)
documentation.
"""


ViewRid = core.RID
"""The resource identifier (RID) of the view that represents a stream."""


core.resolve_forward_references(Record, globalns=globals(), localns=locals())

__all__ = [
    "Compressed",
    "CreateStreamRequestStreamSchema",
    "Dataset",
    "PartitionsCount",
    "Record",
    "Stream",
    "StreamType",
    "ViewRid",
]
