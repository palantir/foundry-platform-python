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


import typing

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import errors as core_errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.datasets import errors as datasets_errors
from foundry_sdk.v2.datasets import models as datasets_models
from foundry_sdk.v2.streams import errors as streams_errors
from foundry_sdk.v2.streams import models as streams_models


class StreamClient:
    """
    The API client for the Stream Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _StreamClientStreaming(self)
        self.with_raw_response = _StreamClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_name: datasets_models.BranchName,
        schema: streams_models.CreateStreamRequestStreamSchema,
        compressed: typing.Optional[streams_models.Compressed] = None,
        partitions_count: typing.Optional[streams_models.PartitionsCount] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        stream_type: typing.Optional[streams_models.StreamType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> streams_models.Stream:
        """
        Creates a new branch on the backing streaming dataset, and creates a new stream on that branch.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: BranchName
        :param schema: The Foundry schema for this stream.
        :type schema: CreateStreamRequestStreamSchema
        :param compressed: Whether or not compression is enabled for the stream. Defaults to false.
        :type compressed: Optional[Compressed]
        :param partitions_count: The number of partitions for the Foundry stream. Defaults to 1.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.
        :type partitions_count: Optional[PartitionsCount]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: streams_models.Stream

        :raises BranchAlreadyExists: The branch cannot be created because a branch with that name already exists.
        :raises CreateStreamPermissionDenied: Could not create the Stream.
        :raises InvalidFieldSchema: The field schema failed validations
        :raises InvalidSchema: The schema failed validations
        :raises InvalidStreamType: The stream type is invalid.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "schema": streams_models.CreateStreamRequestStreamSchema,
                        "partitionsCount": typing.Optional[streams_models.PartitionsCount],
                        "streamType": typing.Optional[streams_models.StreamType],
                        "branchName": datasets_models.BranchName,
                        "compressed": typing.Optional[streams_models.Compressed],
                    },
                ),
                response_type=streams_models.Stream,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchAlreadyExists": datasets_errors.BranchAlreadyExists,
                    "CreateStreamPermissionDenied": streams_errors.CreateStreamPermissionDenied,
                    "InvalidFieldSchema": core_errors.InvalidFieldSchema,
                    "InvalidSchema": core_errors.InvalidSchema,
                    "InvalidStreamType": streams_errors.InvalidStreamType,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> streams_models.Stream:
        """
        Get a stream by its branch name. If the branch does not exist, there is no stream on that branch, or the
        user does not have permission to access the stream, a 404 error will be returned.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: streams_models.Stream

        :raises InvalidFieldSchema: The field schema failed validations
        :raises InvalidStreamNoSchema: The requested stream exists but is invalid, as it does not have a schema.
        :raises InvalidStreamType: The stream type is invalid.
        :raises StreamNotFound: The given Stream could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=streams_models.Stream,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidFieldSchema": core_errors.InvalidFieldSchema,
                    "InvalidStreamNoSchema": streams_errors.InvalidStreamNoSchema,
                    "InvalidStreamType": streams_errors.InvalidStreamType,
                    "StreamNotFound": streams_errors.StreamNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def publish_binary_record(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        body: bytes,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Publish a single binary record to the stream. The stream's schema must be a single binary field.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param body: The binary record to publish to the stream
        :type body: bytes
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: If provided, this operation will only write to the stream corresponding to the specified view rid. If not provided, this operation will write to the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises PublishBinaryRecordToStreamPermissionDenied: Could not publishBinaryRecord the Stream.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                throwable_errors={
                    "PublishBinaryRecordToStreamPermissionDenied": streams_errors.PublishBinaryRecordToStreamPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def publish_record(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        *,
        record: streams_models.Record,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Publish a single record to the stream. The record will be validated against the stream's schema, and
        rejected if it is invalid.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param record: The record to publish to the stream
        :type record: Record
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises PublishRecordToStreamPermissionDenied: Could not publishRecord the Stream.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "record": streams_models.Record,
                        "viewRid": typing.Optional[streams_models.ViewRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PublishRecordToStreamPermissionDenied": streams_errors.PublishRecordToStreamPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def publish_records(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        *,
        records: typing.List[streams_models.Record],
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Publish a batch of records to the stream. The records will be validated against the stream's schema, and
        the batch will be rejected if one or more of the records are invalid.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param records: The records to publish to the stream
        :type records: List[Record]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write to the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises PublishRecordsToStreamPermissionDenied: Could not publishRecords the Stream.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "records": typing.List[streams_models.Record],
                        "viewRid": typing.Optional[streams_models.ViewRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PublishRecordsToStreamPermissionDenied": streams_errors.PublishRecordsToStreamPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def reset(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        *,
        compressed: typing.Optional[streams_models.Compressed] = None,
        partitions_count: typing.Optional[streams_models.PartitionsCount] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        schema: typing.Optional[core_models.StreamSchema] = None,
        stream_type: typing.Optional[streams_models.StreamType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> streams_models.Stream:
        """
        Reset the stream on the given dataset branch, clearing the existing records and allowing new configurations
        to be applied.

        To change the stream settings without clearing the records, update the stream settings in-platform.

        This will create a new stream view (as seen by the change of the `viewRid` on the branch),
        which will be the new stream view that will be written to for the branch.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param compressed: Whether or not compression is enabled for the stream.  If omitted, the compression setting of the existing stream on the branch will be used.
        :type compressed: Optional[Compressed]
        :param partitions_count: The number of partitions for the Foundry stream. Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If omitted, the partitions count of the existing stream on the branch will be used.
        :type partitions_count: Optional[PartitionsCount]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param schema: The Foundry schema to apply to the new stream.   If omitted, the schema of the existing stream on the branch will be used.
        :type schema: Optional[StreamSchema]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  If omitted, the stream type of the existing stream on the branch will be used.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: streams_models.Stream

        :raises InvalidFieldSchema: The field schema failed validations
        :raises InvalidSchema: The schema failed validations
        :raises InvalidStreamNoSchema: The requested stream exists but is invalid, as it does not have a schema.
        :raises InvalidStreamType: The stream type is invalid.
        :raises ResetStreamPermissionDenied: Could not reset the Stream.
        :raises StreamNotFound: The given Stream could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "schema": typing.Optional[core_models.StreamSchema],
                        "partitionsCount": typing.Optional[streams_models.PartitionsCount],
                        "streamType": typing.Optional[streams_models.StreamType],
                        "compressed": typing.Optional[streams_models.Compressed],
                    },
                ),
                response_type=streams_models.Stream,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidFieldSchema": core_errors.InvalidFieldSchema,
                    "InvalidSchema": core_errors.InvalidSchema,
                    "InvalidStreamNoSchema": streams_errors.InvalidStreamNoSchema,
                    "InvalidStreamType": streams_errors.InvalidStreamType,
                    "ResetStreamPermissionDenied": streams_errors.ResetStreamPermissionDenied,
                    "StreamNotFound": streams_errors.StreamNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _StreamClientRaw:
    def __init__(self, client: StreamClient) -> None:
        def create(_: streams_models.Stream): ...
        def get(_: streams_models.Stream): ...
        def publish_binary_record(_: None): ...
        def publish_record(_: None): ...
        def publish_records(_: None): ...
        def reset(_: streams_models.Stream): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.publish_binary_record = core.with_raw_response(
            publish_binary_record, client.publish_binary_record
        )
        self.publish_record = core.with_raw_response(publish_record, client.publish_record)
        self.publish_records = core.with_raw_response(publish_records, client.publish_records)
        self.reset = core.with_raw_response(reset, client.reset)


class _StreamClientStreaming:
    def __init__(self, client: StreamClient) -> None:
        def create(_: streams_models.Stream): ...
        def get(_: streams_models.Stream): ...
        def reset(_: streams_models.Stream): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.reset = core.with_streaming_response(reset, client.reset)


class AsyncStreamClient:
    """
    The API client for the Stream Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncStreamClientStreaming(self)
        self.with_raw_response = _AsyncStreamClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_name: datasets_models.BranchName,
        schema: streams_models.CreateStreamRequestStreamSchema,
        compressed: typing.Optional[streams_models.Compressed] = None,
        partitions_count: typing.Optional[streams_models.PartitionsCount] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        stream_type: typing.Optional[streams_models.StreamType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[streams_models.Stream]:
        """
        Creates a new branch on the backing streaming dataset, and creates a new stream on that branch.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: BranchName
        :param schema: The Foundry schema for this stream.
        :type schema: CreateStreamRequestStreamSchema
        :param compressed: Whether or not compression is enabled for the stream. Defaults to false.
        :type compressed: Optional[Compressed]
        :param partitions_count: The number of partitions for the Foundry stream. Defaults to 1.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.
        :type partitions_count: Optional[PartitionsCount]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[streams_models.Stream]

        :raises BranchAlreadyExists: The branch cannot be created because a branch with that name already exists.
        :raises CreateStreamPermissionDenied: Could not create the Stream.
        :raises InvalidFieldSchema: The field schema failed validations
        :raises InvalidSchema: The schema failed validations
        :raises InvalidStreamType: The stream type is invalid.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "schema": streams_models.CreateStreamRequestStreamSchema,
                        "partitionsCount": typing.Optional[streams_models.PartitionsCount],
                        "streamType": typing.Optional[streams_models.StreamType],
                        "branchName": datasets_models.BranchName,
                        "compressed": typing.Optional[streams_models.Compressed],
                    },
                ),
                response_type=streams_models.Stream,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchAlreadyExists": datasets_errors.BranchAlreadyExists,
                    "CreateStreamPermissionDenied": streams_errors.CreateStreamPermissionDenied,
                    "InvalidFieldSchema": core_errors.InvalidFieldSchema,
                    "InvalidSchema": core_errors.InvalidSchema,
                    "InvalidStreamType": streams_errors.InvalidStreamType,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[streams_models.Stream]:
        """
        Get a stream by its branch name. If the branch does not exist, there is no stream on that branch, or the
        user does not have permission to access the stream, a 404 error will be returned.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[streams_models.Stream]

        :raises InvalidFieldSchema: The field schema failed validations
        :raises InvalidStreamNoSchema: The requested stream exists but is invalid, as it does not have a schema.
        :raises InvalidStreamType: The stream type is invalid.
        :raises StreamNotFound: The given Stream could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=streams_models.Stream,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidFieldSchema": core_errors.InvalidFieldSchema,
                    "InvalidStreamNoSchema": streams_errors.InvalidStreamNoSchema,
                    "InvalidStreamType": streams_errors.InvalidStreamType,
                    "StreamNotFound": streams_errors.StreamNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def publish_binary_record(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        body: bytes,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Publish a single binary record to the stream. The stream's schema must be a single binary field.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param body: The binary record to publish to the stream
        :type body: bytes
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: If provided, this operation will only write to the stream corresponding to the specified view rid. If not provided, this operation will write to the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises PublishBinaryRecordToStreamPermissionDenied: Could not publishBinaryRecord the Stream.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                throwable_errors={
                    "PublishBinaryRecordToStreamPermissionDenied": streams_errors.PublishBinaryRecordToStreamPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def publish_record(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        *,
        record: streams_models.Record,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Publish a single record to the stream. The record will be validated against the stream's schema, and
        rejected if it is invalid.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param record: The record to publish to the stream
        :type record: Record
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises PublishRecordToStreamPermissionDenied: Could not publishRecord the Stream.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "record": streams_models.Record,
                        "viewRid": typing.Optional[streams_models.ViewRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PublishRecordToStreamPermissionDenied": streams_errors.PublishRecordToStreamPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def publish_records(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        *,
        records: typing.List[streams_models.Record],
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Publish a batch of records to the stream. The records will be validated against the stream's schema, and
        the batch will be rejected if one or more of the records are invalid.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param records: The records to publish to the stream
        :type records: List[Record]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: If provided, this endpoint will only write to the stream corresponding to the specified view rid. If not provided, this endpoint will write to the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises PublishRecordsToStreamPermissionDenied: Could not publishRecords the Stream.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "records": typing.List[streams_models.Record],
                        "viewRid": typing.Optional[streams_models.ViewRid],
                    },
                ),
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "PublishRecordsToStreamPermissionDenied": streams_errors.PublishRecordsToStreamPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def reset(
        self,
        dataset_rid: datasets_models.DatasetRid,
        stream_branch_name: datasets_models.BranchName,
        *,
        compressed: typing.Optional[streams_models.Compressed] = None,
        partitions_count: typing.Optional[streams_models.PartitionsCount] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        schema: typing.Optional[core_models.StreamSchema] = None,
        stream_type: typing.Optional[streams_models.StreamType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[streams_models.Stream]:
        """
        Reset the stream on the given dataset branch, clearing the existing records and allowing new configurations
        to be applied.

        To change the stream settings without clearing the records, update the stream settings in-platform.

        This will create a new stream view (as seen by the change of the `viewRid` on the branch),
        which will be the new stream view that will be written to for the branch.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param compressed: Whether or not compression is enabled for the stream.  If omitted, the compression setting of the existing stream on the branch will be used.
        :type compressed: Optional[Compressed]
        :param partitions_count: The number of partitions for the Foundry stream. Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If omitted, the partitions count of the existing stream on the branch will be used.
        :type partitions_count: Optional[PartitionsCount]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param schema: The Foundry schema to apply to the new stream.   If omitted, the schema of the existing stream on the branch will be used.
        :type schema: Optional[StreamSchema]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  If omitted, the stream type of the existing stream on the branch will be used.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[streams_models.Stream]

        :raises InvalidFieldSchema: The field schema failed validations
        :raises InvalidSchema: The schema failed validations
        :raises InvalidStreamNoSchema: The requested stream exists but is invalid, as it does not have a schema.
        :raises InvalidStreamType: The stream type is invalid.
        :raises ResetStreamPermissionDenied: Could not reset the Stream.
        :raises StreamNotFound: The given Stream could not be found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "schema": typing.Optional[core_models.StreamSchema],
                        "partitionsCount": typing.Optional[streams_models.PartitionsCount],
                        "streamType": typing.Optional[streams_models.StreamType],
                        "compressed": typing.Optional[streams_models.Compressed],
                    },
                ),
                response_type=streams_models.Stream,
                request_timeout=request_timeout,
                throwable_errors={
                    "InvalidFieldSchema": core_errors.InvalidFieldSchema,
                    "InvalidSchema": core_errors.InvalidSchema,
                    "InvalidStreamNoSchema": streams_errors.InvalidStreamNoSchema,
                    "InvalidStreamType": streams_errors.InvalidStreamType,
                    "ResetStreamPermissionDenied": streams_errors.ResetStreamPermissionDenied,
                    "StreamNotFound": streams_errors.StreamNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncStreamClientRaw:
    def __init__(self, client: AsyncStreamClient) -> None:
        def create(_: streams_models.Stream): ...
        def get(_: streams_models.Stream): ...
        def publish_binary_record(_: None): ...
        def publish_record(_: None): ...
        def publish_records(_: None): ...
        def reset(_: streams_models.Stream): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.publish_binary_record = core.async_with_raw_response(
            publish_binary_record, client.publish_binary_record
        )
        self.publish_record = core.async_with_raw_response(publish_record, client.publish_record)
        self.publish_records = core.async_with_raw_response(publish_records, client.publish_records)
        self.reset = core.async_with_raw_response(reset, client.reset)


class _AsyncStreamClientStreaming:
    def __init__(self, client: AsyncStreamClient) -> None:
        def create(_: streams_models.Stream): ...
        def get(_: streams_models.Stream): ...
        def reset(_: streams_models.Stream): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.reset = core.async_with_streaming_response(reset, client.reset)
