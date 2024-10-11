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

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._stream_schema_dict import StreamSchemaDict
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.streams.models._compressed import Compressed
from foundry.v2.streams.models._create_stream_request_stream_schema_dict import (
    CreateStreamRequestStreamSchemaDict,
)  # NOQA
from foundry.v2.streams.models._partitions_count import PartitionsCount
from foundry.v2.streams.models._record import Record
from foundry.v2.streams.models._stream import Stream
from foundry.v2.streams.models._stream_type import StreamType
from foundry.v2.streams.models._view_rid import ViewRid


class StreamClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        dataset_rid: DatasetRid,
        *,
        branch_name: BranchName,
        schema: CreateStreamRequestStreamSchemaDict,
        compressed: Optional[Compressed] = None,
        partitions_count: Optional[PartitionsCount] = None,
        preview: Optional[PreviewMode] = None,
        stream_type: Optional[StreamType] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Stream:
        """
        Creates a new branch on the backing streaming dataset, and creates a new stream on that branch.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: BranchName
        :param schema: The Foundry schema for this stream.
        :type schema: CreateStreamRequestStreamSchemaDict
        :param compressed: Whether or not compression is enabled for the stream. Defaults to false.
        :type compressed: Optional[Compressed]
        :param partitions_count: The number of partitions for the Foundry stream. Defaults to 1.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.
        :type partitions_count: Optional[PartitionsCount]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Stream
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/streams/datasets/{datasetRid}/streams",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "schema": schema,
                    "partitionsCount": partitions_count,
                    "streamType": stream_type,
                    "branchName": branch_name,
                    "compressed": compressed,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "schema": CreateStreamRequestStreamSchemaDict,
                        "partitionsCount": Optional[PartitionsCount],
                        "streamType": Optional[StreamType],
                        "branchName": BranchName,
                        "compressed": Optional[Compressed],
                    },
                ),
                response_type=Stream,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        stream_branch_name: BranchName,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Stream:
        """
        Get a stream by its branch name. If the branch does not exist, there is no stream on that branch, or the
        user does not have permission to access the stream, a 404 error will be returned.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param stream_branch_name: streamBranchName
        :type stream_branch_name: BranchName
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Stream
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/streams/datasets/{datasetRid}/streams/{streamBranchName}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Stream,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def publish_binary_record(
        self,
        dataset_rid: DatasetRid,
        stream_branch_name: BranchName,
        body: bytes,
        *,
        preview: Optional[PreviewMode] = None,
        view_rid: Optional[ViewRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Publish a single binary record to the stream. The stream's schema must be a single binary field.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param stream_branch_name: streamBranchName
        :type stream_branch_name: BranchName
        :param body: The binary record to publish to the stream
        :type body: bytes
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param view_rid: viewRid
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/publishBinaryRecord",
                query_params={
                    "preview": preview,
                    "viewRid": view_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                },
                body=body,
                body_type=bytes,
                response_type=None,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def publish_record(
        self,
        dataset_rid: DatasetRid,
        stream_branch_name: BranchName,
        *,
        record: Record,
        preview: Optional[PreviewMode] = None,
        view_rid: Optional[ViewRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Publish a single record to the stream. The record will be validated against the stream's schema, and
        rejected if it is invalid.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param stream_branch_name: streamBranchName
        :type stream_branch_name: BranchName
        :param record: The record to publish to the stream
        :type record: Record
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param view_rid: If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/publishRecord",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "record": record,
                    "viewRid": view_rid,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "record": Record,
                        "viewRid": Optional[ViewRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def publish_records(
        self,
        dataset_rid: DatasetRid,
        stream_branch_name: BranchName,
        *,
        records: List[Record],
        preview: Optional[PreviewMode] = None,
        view_rid: Optional[ViewRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Publish a batch of records to the stream. The records will be validated against the stream's schema, and
        the batch will be rejected if one or more of the records are invalid.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param stream_branch_name: streamBranchName
        :type stream_branch_name: BranchName
        :param records: The records to publish to the stream
        :type records: List[Record]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param view_rid: If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write to the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/publishRecords",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body={
                    "records": records,
                    "viewRid": view_rid,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "records": List[Record],
                        "viewRid": Optional[ViewRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def reset(
        self,
        dataset_rid: DatasetRid,
        stream_branch_name: BranchName,
        *,
        compressed: Optional[Compressed] = None,
        partitions_count: Optional[PartitionsCount] = None,
        preview: Optional[PreviewMode] = None,
        schema: Optional[StreamSchemaDict] = None,
        stream_type: Optional[StreamType] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Stream:
        """
        Reset the stream on the given dataset branch, clearing the existing records and allowing new configurations
        to be applied.

        To change the stream settings without clearing the records, update the stream settings in-platform.

        This will create a new stream view (as seen by the change of the `viewRid` on the branch),
        which will be the new stream view that will be written to for the branch.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param stream_branch_name: streamBranchName
        :type stream_branch_name: BranchName
        :param compressed: Whether or not compression is enabled for the stream.  If omitted, the compression setting of the existing stream on the branch will be used.
        :type compressed: Optional[Compressed]
        :param partitions_count: The number of partitions for the Foundry stream. Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If omitted, the partitions count of the existing stream on the branch will be used.
        :type partitions_count: Optional[PartitionsCount]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param schema: The Foundry schema to apply to the new stream.   If omitted, the schema of the existing stream on the branch will be used.
        :type schema: Optional[StreamSchemaDict]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  If omitted, the stream type of the existing stream on the branch will be used.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Stream
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/streams/datasets/{datasetRid}/streams/{streamBranchName}/reset",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "schema": schema,
                    "partitionsCount": partitions_count,
                    "streamType": stream_type,
                    "compressed": compressed,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "schema": Optional[StreamSchemaDict],
                        "partitionsCount": Optional[PartitionsCount],
                        "streamType": Optional[StreamType],
                        "compressed": Optional[Compressed],
                    },
                ),
                response_type=Stream,
                request_timeout=request_timeout,
            ),
        )
