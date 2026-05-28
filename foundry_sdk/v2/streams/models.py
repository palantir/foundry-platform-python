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
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.datasets import models as datasets_models
from foundry_sdk.v2.filesystem import models as filesystem_models


class CommitSubscriberOffsetsRequest(core.ModelBase):
    """CommitSubscriberOffsetsRequest"""

    view_rid: typing.Optional[ViewRid] = pydantic.Field(alias=str("viewRid"), default=None)  # type: ignore[literal-required]
    """
    The view RID to commit offsets for. If not provided, uses the latest view for the
    dataset/branch.
    """

    offsets: PartitionOffsets
    """
    The last processed offset for each partition. The server will store these as
    read positions (offset + 1), so the next read starts after the committed offset.
    """


Compressed: typing_extensions.TypeAlias = bool
"""
Compression helps reduce the size of the data being sent, resulting in lower network usage and
storage, at the cost of some additional CPU usage for compression and decompression. This stream type
is only recommended if your stream contains a high volume of repetitive strings and is experiencing poor
network bandwidth symptoms like non-zero lag, lower than expected throughput, or dropped records.
"""


class CreateStreamRequest(core.ModelBase):
    """CreateStreamRequest"""

    schema_: CreateStreamRequestStreamSchema = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    """The Foundry schema for this stream."""

    partitions_count: typing.Optional[PartitionsCount] = pydantic.Field(alias=str("partitionsCount"), default=None)  # type: ignore[literal-required]
    """
    The number of partitions for the Foundry stream. Defaults to 1.

    Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions
    are recommended.
    """

    stream_type: typing.Optional[StreamType] = pydantic.Field(alias=str("streamType"), default=None)  # type: ignore[literal-required]
    """
    A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and
    LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
    """

    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    compressed: typing.Optional[Compressed] = None
    """Whether or not compression is enabled for the stream. Defaults to false."""


class CreateStreamRequestStreamSchema(core.ModelBase):
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


class CreateStreamingDatasetRequest(core.ModelBase):
    """CreateStreamingDatasetRequest"""

    name: datasets_models.DatasetName
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    schema_: core_models.StreamSchema = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    """The Foundry schema to apply to the new stream."""

    branch_name: typing.Optional[core_models.BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]
    """
    The branch to create the initial stream on. If not specified, the default branch will be used
    ('master' for most enrollments).
    """

    partitions_count: typing.Optional[PartitionsCount] = pydantic.Field(alias=str("partitionsCount"), default=None)  # type: ignore[literal-required]
    """
    The number of partitions for the Foundry stream.

    Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions
    are recommended.

    If not specified, 1 partition is used.

    This value cannot be changed later.
    """

    stream_type: typing.Optional[StreamType] = pydantic.Field(alias=str("streamType"), default=None)  # type: ignore[literal-required]
    """
    A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and
    LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
    """

    compressed: typing.Optional[Compressed] = None
    """Whether or not compression is enabled for the stream. Defaults to false."""


class CreateSubscriberRequest(core.ModelBase):
    """CreateSubscriberRequest"""

    subscriber_id: SubscriberId = pydantic.Field(alias=str("subscriberId"))  # type: ignore[literal-required]
    read_position: typing.Optional[ReadPosition] = pydantic.Field(alias=str("readPosition"), default=None)  # type: ignore[literal-required]
    """
    Where to start reading from. Defaults to `earliest` if not specified.

    The `readPosition` determines where the subscriber will start reading:
    - `earliest`: Start from the beginning of each partition (offset 0). Use this to process
      all historical data.
    - `latest`: Start from the current end of each partition. Use this to skip historical data
      and only process new records arriving after registration.
    - `specific`: Start from explicit offsets for each partition. Use this to resume from a
      known checkpoint.
    """


class Dataset(core.ModelBase):
    """Dataset"""

    rid: core_models.DatasetRid
    name: datasets_models.DatasetName
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]


class EarliestPosition(core.ModelBase):
    """
    Start reading from the beginning of the stream. Sets offset to 0 for all partitions,
    allowing the subscriber to read all historical data from the start.
    """

    type: typing.Literal["earliest"] = "earliest"


GetEndOffsetsResponse: typing_extensions.TypeAlias = typing.Dict["PartitionId", core.Long]
"""The end offsets for each partition of a stream."""


GetRecordsResponse: typing_extensions.TypeAlias = typing.List["RecordWithOffset"]
"""A list of records from a stream with their offsets."""


class LatestPosition(core.ModelBase):
    """
    Start reading from the current end of the stream. Sets offsets to the latest available
    offset for each partition, meaning the subscriber will only receive records published
    after this point.
    """

    type: typing.Literal["latest"] = "latest"


PartitionId: typing_extensions.TypeAlias = str
"""The identifier for a partition of a Foundry stream."""


PartitionOffsets: typing_extensions.TypeAlias = typing.Dict["PartitionId", core.Long]
"""A map of partition IDs to offsets."""


PartitionRecords: typing_extensions.TypeAlias = typing.List["RecordWithOffset"]
"""Records from a single partition with their offsets."""


PartitionsCount: typing_extensions.TypeAlias = int
"""The number of partitions for a Foundry stream."""


class PublishRecordToStreamRequest(core.ModelBase):
    """PublishRecordToStreamRequest"""

    record: Record
    """The record to publish to the stream"""

    view_rid: typing.Optional[ViewRid] = pydantic.Field(alias=str("viewRid"), default=None)  # type: ignore[literal-required]
    """
    If provided, this endpoint will only write to the stream corresponding to the specified view RID. If
    not provided, this endpoint will write the latest stream on the branch.

    Providing this value is an advanced configuration, to be used when additional control over the
    underlying streaming data structures is needed.
    """


class PublishRecordsToStreamRequest(core.ModelBase):
    """PublishRecordsToStreamRequest"""

    records: typing.List[Record]
    """The records to publish to the stream"""

    view_rid: typing.Optional[ViewRid] = pydantic.Field(alias=str("viewRid"), default=None)  # type: ignore[literal-required]
    """
    If provided, this endpoint will only write to the stream corresponding to the specified view RID. If
    not provided, this endpoint will write to the latest stream on the branch.

    Providing this value is an advanced configuration, to be used when additional control over the
    underlying streaming data structures is needed.
    """


ReadPosition: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["SpecificPosition", "EarliestPosition", "LatestPosition"],
    pydantic.Field(discriminator="type"),
]
"""
Position to start reading from when registering a subscriber or resetting offsets.

- `earliest`: Start reading from the beginning of each partition (offset 0). Use this to
  reprocess all historical data in the stream.
- `latest`: Start reading from the current end of each partition. Use this to skip
  historical data and only process new records arriving after registration.
- `specific`: Start reading from explicit offsets for each partition. Use this for precise
  replay scenarios or to resume from a known checkpoint.
"""


class ReadRecordsFromSubscriberRequest(core.ModelBase):
    """ReadRecordsFromSubscriberRequest"""

    view_rid: typing.Optional[ViewRid] = pydantic.Field(alias=str("viewRid"), default=None)  # type: ignore[literal-required]
    """
    The view RID to read from. If not provided, reads from the latest view for the
    dataset/branch.
    """

    limit: typing.Optional[int] = None
    """
    Maximum number of records to return across all partitions. Defaults to 100, max 1000. If a value 
    greater than 1000 is requested, only 1000 records will be returned.
    """

    partition_ids: typing.Optional[typing.List[PartitionId]] = pydantic.Field(alias=str("partitionIds"), default=None)  # type: ignore[literal-required]
    """If specified, only read from these partitions. Otherwise, read from all partitions."""

    auto_commit: typing.Optional[bool] = pydantic.Field(alias=str("autoCommit"), default=None)  # type: ignore[literal-required]
    """
    If true, the read position is automatically committed after reading records.
    The committed position will be the offset after the last record read.
    If false, you must call the `commitOffsets` endpoint to commit offsets.
    Defaults to false.
    """


class ReadSubscriberRecordsResponse(core.ModelBase):
    """Response containing records grouped by partition ID."""

    records_by_partition: typing.Dict[PartitionId, PartitionRecords] = pydantic.Field(alias=str("recordsByPartition"))  # type: ignore[literal-required]
    """Records grouped by partition ID."""


Record: typing_extensions.TypeAlias = typing.Dict[str, typing.Optional[typing.Any]]
"""A record to be published to a stream."""


class RecordWithOffset(core.ModelBase):
    """A record retrieved from a stream, including its offset within the partition."""

    offset: core.Long
    """The offset of the record within the partition."""

    value: Record
    """The record value as a map of field names to values."""


class ResetStreamRequest(core.ModelBase):
    """ResetStreamRequest"""

    schema_: typing.Optional[core_models.StreamSchema] = pydantic.Field(alias=str("schema"), default=None)  # type: ignore[literal-required]
    """
    The Foundry schema to apply to the new stream. 

    If omitted, the schema of the existing stream on the branch will be used.
    """

    partitions_count: typing.Optional[PartitionsCount] = pydantic.Field(alias=str("partitionsCount"), default=None)  # type: ignore[literal-required]
    """
    The number of partitions for the Foundry stream.
    Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions
    are recommended.

    If omitted, the partitions count of the existing stream on the branch will be used.
    """

    stream_type: typing.Optional[StreamType] = pydantic.Field(alias=str("streamType"), default=None)  # type: ignore[literal-required]
    """
    A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and
    LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.

    If omitted, the stream type of the existing stream on the branch will be used.
    """

    compressed: typing.Optional[Compressed] = None
    """
    Whether or not compression is enabled for the stream.

    If omitted, the compression setting of the existing stream on the branch will be used.
    """


class ResetSubscriberOffsetsRequest(core.ModelBase):
    """ResetSubscriberOffsetsRequest"""

    position: ReadPosition
    """The position to reset offsets to."""


class SpecificPosition(core.ModelBase):
    """
    Start reading from specific offsets for each partition. Useful for resuming from a known
    checkpoint or replaying from a specific point in time.
    """

    offsets: PartitionOffsets
    """
    Specific offsets for each partition. Offsets must be valid (non-negative and not
    beyond the end of the partition).
    """

    type: typing.Literal["specific"] = "specific"


class Stream(core.ModelBase):
    """Stream"""

    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
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


StreamType: typing_extensions.TypeAlias = typing.Literal["LOW_LATENCY", "HIGH_THROUGHPUT"]
"""
LOW_LATENCY: The default stream type. Recommended for most use cases.

HIGH_THROUGHPUT: Best for streams that send large amounts of data every second. Using this stream type might
introduce some non-zero latency at the expense of a higher throughput. This stream type is only
recommended if you inspect your stream metrics in-platform and observe that the average batch size is equal
to the max match size, or if jobs using the stream are failing due to Kafka producer batches expiring. For
additional information on inspecting stream metrics, refer to the 
[stream monitoring](https://palantir.com/docs/foundry/data-integration/stream-monitoring/#viewing-metrics) documentation.

For more information, refer to the [stream types](https://palantir.com/docs/foundry/data-integration/streams/#stream-types)
documentation.
"""


class Subscriber(core.ModelBase):
    """Subscriber"""

    subscriber_id: SubscriberId = pydantic.Field(alias=str("subscriberId"))  # type: ignore[literal-required]
    read_position: typing.Optional[ReadPosition] = pydantic.Field(alias=str("readPosition"), default=None)  # type: ignore[literal-required]
    """
    Where to start reading from. Defaults to `earliest` if not specified.

    The `readPosition` determines where the subscriber will start reading:
    - `earliest`: Start from the beginning of each partition (offset 0). Use this to process
      all historical data.
    - `latest`: Start from the current end of each partition. Use this to skip historical data
      and only process new records arriving after registration.
    - `specific`: Start from explicit offsets for each partition. Use this to resume from a
      known checkpoint.
    """

    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset the subscriber is bound to."""

    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    """The branch of the stream the subscriber is bound to."""

    view_rid: ViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]
    """
    The current view RID being read from. This may change over time if the stream's
    schema is migrated to a new view.
    """

    start_offsets: PartitionOffsets = pydantic.Field(alias=str("startOffsets"))  # type: ignore[literal-required]
    """The offsets where reading began for each partition, based on the initial read position."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """Timestamp when the subscriber was registered."""


SubscriberId: typing_extensions.TypeAlias = str
"""A unique identifier for a stream subscriber. Must be unique within the scope of a stream."""


ViewRid: typing_extensions.TypeAlias = core.RID
"""The resource identifier (RID) of the view that represents a stream."""


core.resolve_forward_references_in_module(__name__)

__all__ = [
    "CommitSubscriberOffsetsRequest",
    "Compressed",
    "CreateStreamRequest",
    "CreateStreamRequestStreamSchema",
    "CreateStreamingDatasetRequest",
    "CreateSubscriberRequest",
    "Dataset",
    "EarliestPosition",
    "GetEndOffsetsResponse",
    "GetRecordsResponse",
    "LatestPosition",
    "PartitionId",
    "PartitionOffsets",
    "PartitionRecords",
    "PartitionsCount",
    "PublishRecordToStreamRequest",
    "PublishRecordsToStreamRequest",
    "ReadPosition",
    "ReadRecordsFromSubscriberRequest",
    "ReadSubscriberRecordsResponse",
    "Record",
    "RecordWithOffset",
    "ResetStreamRequest",
    "ResetSubscriberOffsetsRequest",
    "SpecificPosition",
    "Stream",
    "StreamType",
    "Subscriber",
    "SubscriberId",
    "ViewRid",
]
