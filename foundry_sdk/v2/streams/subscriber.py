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
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.streams import errors as streams_errors
from foundry_sdk.v2.streams import models as streams_models


class SubscriberClient:
    """
    The API client for the Subscriber Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.ApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _SubscriberClientStreaming(self)
        self.with_raw_response = _SubscriberClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def commit_offsets(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        offsets: streams_models.PartitionOffsets,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> streams_models.PartitionOffsets:
        """
        Explicitly commit offsets for a subscriber. Required when `autoCommit` is false.

        Pass the last offset you processed for each partition.

        For example, if you processed a record at offset 50, commit `{"0": 50}` and the next
        read from partition "0" will start at offset 51.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param offsets: The last processed offset for each partition. The server will store these as read positions (offset + 1), so the next read starts after the committed offset.
        :type offsets: PartitionOffsets
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: The view RID to commit offsets for. If not provided, uses the latest view for the dataset/branch.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: streams_models.PartitionOffsets

        :raises CommitSubscriberOffsetsPermissionDenied: Could not commitOffsets the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/commitOffsets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=streams_models.CommitSubscriberOffsetsRequest(
                    view_rid=view_rid,
                    offsets=offsets,
                ),
                response_type=streams_models.PartitionOffsets,
                request_timeout=request_timeout,
                throwable_errors={
                    "CommitSubscriberOffsetsPermissionDenied": streams_errors.CommitSubscriberOffsetsPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
                endpoint_type=core.EndpointType.HIGH_SCALE,
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        *,
        subscriber_id: streams_models.SubscriberId,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_position: typing.Optional[streams_models.ReadPosition] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> streams_models.Subscriber:
        """
        Register a new subscriber for a stream. Subscribers maintain server-side offset tracking,
        allowing reliable consumption without client-side state management.

        If a subscriber with the same ID already exists for this stream, the existing registration
        is returned. If a subscriber with the same ID exists for a different stream, an error is returned.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_id:
        :type subscriber_id: SubscriberId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param read_position: Where to start reading from. Defaults to `earliest` if not specified.  The `readPosition` determines where the subscriber will start reading: - `earliest`: Start from the beginning of each partition (offset 0). Use this to process   all historical data. - `latest`: Start from the current end of each partition. Use this to skip historical data   and only process new records arriving after registration. - `specific`: Start from explicit offsets for each partition. Use this to resume from a   known checkpoint.
        :type read_position: Optional[ReadPosition]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: streams_models.Subscriber

        :raises CreateSubscriberPermissionDenied: Could not create the Subscriber.
        :raises SubscriberAlreadyExists: A subscriber with this ID already exists for a different stream.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers",
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
                body=streams_models.CreateSubscriberRequest(
                    subscriber_id=subscriber_id,
                    read_position=read_position,
                ),
                response_type=streams_models.Subscriber,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSubscriberPermissionDenied": streams_errors.CreateSubscriberPermissionDenied,
                    "SubscriberAlreadyExists": streams_errors.SubscriberAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Delete a subscriber and all its committed offset state. After deletion, the subscriber ID
        can be reused to create a new subscriber.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises DeleteSubscriberPermissionDenied: Could not delete the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteSubscriberPermissionDenied": streams_errors.DeleteSubscriberPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_read_position(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> streams_models.PartitionOffsets:
        """
        Get the current read position for a subscriber. Returns the offset per partition where the next read
        will begin.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: The view RID to get positions for. If not provided, uses the latest view for the dataset/branch.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: streams_models.PartitionOffsets

        :raises GetSubscriberReadPositionPermissionDenied: Could not getReadPosition the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/getReadPosition",
                query_params={
                    "preview": preview,
                    "viewRid": view_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=streams_models.PartitionOffsets,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetSubscriberReadPositionPermissionDenied": streams_errors.GetSubscriberReadPositionPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
                endpoint_type=core.EndpointType.HIGH_SCALE,
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read_records(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        auto_commit: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        partition_ids: typing.Optional[typing.List[streams_models.PartitionId]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> streams_models.ReadSubscriberRecordsResponse:
        """
        Fetch records for a subscriber starting from their committed offset. Returns records
        grouped by partition.

        If `autoCommit` is true, offsets are automatically committed after the records are
        fetched, so the next read will start from where this one left off.

        If `autoCommit` is false, you must call `commitOffsets` to update the read position.
        Use manual commits for at-least-once processing where you need to ensure records are
        processed before acknowledging them.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param auto_commit: If true, the read position is automatically committed after reading records. The committed position will be the offset after the last record read. If false, you must call the `commitOffsets` endpoint to commit offsets. Defaults to false.
        :type auto_commit: Optional[bool]
        :param limit: Maximum number of records to return across all partitions. Defaults to 100, max 1000. If a value  greater than 1000 is requested, only 1000 records will be returned.
        :type limit: Optional[int]
        :param partition_ids: If specified, only read from these partitions. Otherwise, read from all partitions.
        :type partition_ids: Optional[List[PartitionId]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: The view RID to read from. If not provided, reads from the latest view for the dataset/branch.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: streams_models.ReadSubscriberRecordsResponse

        :raises ReadRecordsFromSubscriberPermissionDenied: Could not readRecords the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/readRecords",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=streams_models.ReadRecordsFromSubscriberRequest(
                    view_rid=view_rid,
                    limit=limit,
                    partition_ids=partition_ids,
                    auto_commit=auto_commit,
                ),
                response_type=streams_models.ReadSubscriberRecordsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReadRecordsFromSubscriberPermissionDenied": streams_errors.ReadRecordsFromSubscriberPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
                endpoint_type=core.EndpointType.HIGH_SCALE,
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def reset_offsets(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        position: streams_models.ReadPosition,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> streams_models.PartitionOffsets:
        """
        Reset subscriber offsets to a specific position. Use this to replay data from the
        beginning, skip to the latest records, or jump to specific offsets.

        The `position` parameter determines where reading will resume:
        - `earliest`: Reset to the beginning of each partition (offset 0)
        - `latest`: Reset to the current end of each partition
        - `specific`: Reset to explicit offsets for each partition

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param position: The position to reset offsets to.
        :type position: ReadPosition
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: streams_models.PartitionOffsets

        :raises ResetSubscriberOffsetsPermissionDenied: Could not resetOffsets the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/resetOffsets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=streams_models.ResetSubscriberOffsetsRequest(
                    position=position,
                ),
                response_type=streams_models.PartitionOffsets,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResetSubscriberOffsetsPermissionDenied": streams_errors.ResetSubscriberOffsetsPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
                endpoint_type=core.EndpointType.HIGH_SCALE,
            ),
        )


class _SubscriberClientRaw:
    def __init__(self, client: SubscriberClient) -> None:
        def commit_offsets(_: streams_models.PartitionOffsets): ...
        def create(_: streams_models.Subscriber): ...
        def delete(_: None): ...
        def get_read_position(_: streams_models.PartitionOffsets): ...
        def read_records(_: streams_models.ReadSubscriberRecordsResponse): ...
        def reset_offsets(_: streams_models.PartitionOffsets): ...

        self.commit_offsets = core.with_raw_response(commit_offsets, client.commit_offsets)
        self.create = core.with_raw_response(create, client.create)
        self.delete = core.with_raw_response(delete, client.delete)
        self.get_read_position = core.with_raw_response(get_read_position, client.get_read_position)
        self.read_records = core.with_raw_response(read_records, client.read_records)
        self.reset_offsets = core.with_raw_response(reset_offsets, client.reset_offsets)


class _SubscriberClientStreaming:
    def __init__(self, client: SubscriberClient) -> None:
        def commit_offsets(_: streams_models.PartitionOffsets): ...
        def create(_: streams_models.Subscriber): ...
        def get_read_position(_: streams_models.PartitionOffsets): ...
        def read_records(_: streams_models.ReadSubscriberRecordsResponse): ...
        def reset_offsets(_: streams_models.PartitionOffsets): ...

        self.commit_offsets = core.with_streaming_response(commit_offsets, client.commit_offsets)
        self.create = core.with_streaming_response(create, client.create)
        self.get_read_position = core.with_streaming_response(
            get_read_position, client.get_read_position
        )
        self.read_records = core.with_streaming_response(read_records, client.read_records)
        self.reset_offsets = core.with_streaming_response(reset_offsets, client.reset_offsets)


class AsyncSubscriberClient:
    """
    The API client for the Subscriber Resource.

    :param auth: Your auth configuration.
    :param hostname: The hostname supplier for resolving base URLs.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: typing.Union[str, core.HostnameSupplier],
        config: typing.Optional[core.Config] = None,
    ):
        self._auth = auth
        if isinstance(hostname, core.HostnameSupplier):
            self._hostname_supplier = hostname
        else:
            self._hostname_supplier = core.create_hostname_supplier(hostname, config)
        self._hostname = self._hostname_supplier.get_hostname()
        self._config = config
        self._api_client = core.AsyncApiClient(
            auth=auth, hostname=self._hostname_supplier, config=config
        )

        self.with_streaming_response = _AsyncSubscriberClientStreaming(self)
        self.with_raw_response = _AsyncSubscriberClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def commit_offsets(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        offsets: streams_models.PartitionOffsets,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[streams_models.PartitionOffsets]:
        """
        Explicitly commit offsets for a subscriber. Required when `autoCommit` is false.

        Pass the last offset you processed for each partition.

        For example, if you processed a record at offset 50, commit `{"0": 50}` and the next
        read from partition "0" will start at offset 51.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param offsets: The last processed offset for each partition. The server will store these as read positions (offset + 1), so the next read starts after the committed offset.
        :type offsets: PartitionOffsets
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: The view RID to commit offsets for. If not provided, uses the latest view for the dataset/branch.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[streams_models.PartitionOffsets]

        :raises CommitSubscriberOffsetsPermissionDenied: Could not commitOffsets the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/commitOffsets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=streams_models.CommitSubscriberOffsetsRequest(
                    view_rid=view_rid,
                    offsets=offsets,
                ),
                response_type=streams_models.PartitionOffsets,
                request_timeout=request_timeout,
                throwable_errors={
                    "CommitSubscriberOffsetsPermissionDenied": streams_errors.CommitSubscriberOffsetsPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
                endpoint_type=core.EndpointType.HIGH_SCALE,
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        *,
        subscriber_id: streams_models.SubscriberId,
        preview: typing.Optional[core_models.PreviewMode] = None,
        read_position: typing.Optional[streams_models.ReadPosition] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[streams_models.Subscriber]:
        """
        Register a new subscriber for a stream. Subscribers maintain server-side offset tracking,
        allowing reliable consumption without client-side state management.

        If a subscriber with the same ID already exists for this stream, the existing registration
        is returned. If a subscriber with the same ID exists for a different stream, an error is returned.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_id:
        :type subscriber_id: SubscriberId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param read_position: Where to start reading from. Defaults to `earliest` if not specified.  The `readPosition` determines where the subscriber will start reading: - `earliest`: Start from the beginning of each partition (offset 0). Use this to process   all historical data. - `latest`: Start from the current end of each partition. Use this to skip historical data   and only process new records arriving after registration. - `specific`: Start from explicit offsets for each partition. Use this to resume from a   known checkpoint.
        :type read_position: Optional[ReadPosition]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[streams_models.Subscriber]

        :raises CreateSubscriberPermissionDenied: Could not create the Subscriber.
        :raises SubscriberAlreadyExists: A subscriber with this ID already exists for a different stream.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers",
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
                body=streams_models.CreateSubscriberRequest(
                    subscriber_id=subscriber_id,
                    read_position=read_position,
                ),
                response_type=streams_models.Subscriber,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateSubscriberPermissionDenied": streams_errors.CreateSubscriberPermissionDenied,
                    "SubscriberAlreadyExists": streams_errors.SubscriberAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Delete a subscriber and all its committed offset state. After deletion, the subscriber ID
        can be reused to create a new subscriber.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises DeleteSubscriberPermissionDenied: Could not delete the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="DELETE",
                resource_path="/v2/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={},
                body=None,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "DeleteSubscriberPermissionDenied": streams_errors.DeleteSubscriberPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_read_position(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[streams_models.PartitionOffsets]:
        """
        Get the current read position for a subscriber. Returns the offset per partition where the next read
        will begin.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: The view RID to get positions for. If not provided, uses the latest view for the dataset/branch.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[streams_models.PartitionOffsets]

        :raises GetSubscriberReadPositionPermissionDenied: Could not getReadPosition the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/getReadPosition",
                query_params={
                    "preview": preview,
                    "viewRid": view_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                response_type=streams_models.PartitionOffsets,
                request_timeout=request_timeout,
                throwable_errors={
                    "GetSubscriberReadPositionPermissionDenied": streams_errors.GetSubscriberReadPositionPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
                endpoint_type=core.EndpointType.HIGH_SCALE,
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read_records(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        auto_commit: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        partition_ids: typing.Optional[typing.List[streams_models.PartitionId]] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        view_rid: typing.Optional[streams_models.ViewRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[streams_models.ReadSubscriberRecordsResponse]:
        """
        Fetch records for a subscriber starting from their committed offset. Returns records
        grouped by partition.

        If `autoCommit` is true, offsets are automatically committed after the records are
        fetched, so the next read will start from where this one left off.

        If `autoCommit` is false, you must call `commitOffsets` to update the read position.
        Use manual commits for at-least-once processing where you need to ensure records are
        processed before acknowledging them.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param auto_commit: If true, the read position is automatically committed after reading records. The committed position will be the offset after the last record read. If false, you must call the `commitOffsets` endpoint to commit offsets. Defaults to false.
        :type auto_commit: Optional[bool]
        :param limit: Maximum number of records to return across all partitions. Defaults to 100, max 1000. If a value  greater than 1000 is requested, only 1000 records will be returned.
        :type limit: Optional[int]
        :param partition_ids: If specified, only read from these partitions. Otherwise, read from all partitions.
        :type partition_ids: Optional[List[PartitionId]]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param view_rid: The view RID to read from. If not provided, reads from the latest view for the dataset/branch.
        :type view_rid: Optional[ViewRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[streams_models.ReadSubscriberRecordsResponse]

        :raises ReadRecordsFromSubscriberPermissionDenied: Could not readRecords the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/readRecords",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=streams_models.ReadRecordsFromSubscriberRequest(
                    view_rid=view_rid,
                    limit=limit,
                    partition_ids=partition_ids,
                    auto_commit=auto_commit,
                ),
                response_type=streams_models.ReadSubscriberRecordsResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "ReadRecordsFromSubscriberPermissionDenied": streams_errors.ReadRecordsFromSubscriberPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
                endpoint_type=core.EndpointType.HIGH_SCALE,
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def reset_offsets(
        self,
        dataset_rid: core_models.DatasetRid,
        stream_branch_name: core_models.BranchName,
        subscriber_subscriber_id: streams_models.SubscriberId,
        *,
        position: streams_models.ReadPosition,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[streams_models.PartitionOffsets]:
        """
        Reset subscriber offsets to a specific position. Use this to replay data from the
        beginning, skip to the latest records, or jump to specific offsets.

        The `position` parameter determines where reading will resume:
        - `earliest`: Reset to the beginning of each partition (offset 0)
        - `latest`: Reset to the current end of each partition
        - `specific`: Reset to explicit offsets for each partition

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param stream_branch_name:
        :type stream_branch_name: BranchName
        :param subscriber_subscriber_id:
        :type subscriber_subscriber_id: SubscriberId
        :param position: The position to reset offsets to.
        :type position: ReadPosition
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[streams_models.PartitionOffsets]

        :raises ResetSubscriberOffsetsPermissionDenied: Could not resetOffsets the Subscriber.
        :raises SubscriberNotFound: No subscriber with the given ID was found.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/resetOffsets",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "streamBranchName": stream_branch_name,
                    "subscriberSubscriberId": subscriber_subscriber_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=streams_models.ResetSubscriberOffsetsRequest(
                    position=position,
                ),
                response_type=streams_models.PartitionOffsets,
                request_timeout=request_timeout,
                throwable_errors={
                    "ResetSubscriberOffsetsPermissionDenied": streams_errors.ResetSubscriberOffsetsPermissionDenied,
                    "SubscriberNotFound": streams_errors.SubscriberNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
                endpoint_type=core.EndpointType.HIGH_SCALE,
            ),
        )


class _AsyncSubscriberClientRaw:
    def __init__(self, client: AsyncSubscriberClient) -> None:
        def commit_offsets(_: streams_models.PartitionOffsets): ...
        def create(_: streams_models.Subscriber): ...
        def delete(_: None): ...
        def get_read_position(_: streams_models.PartitionOffsets): ...
        def read_records(_: streams_models.ReadSubscriberRecordsResponse): ...
        def reset_offsets(_: streams_models.PartitionOffsets): ...

        self.commit_offsets = core.async_with_raw_response(commit_offsets, client.commit_offsets)
        self.create = core.async_with_raw_response(create, client.create)
        self.delete = core.async_with_raw_response(delete, client.delete)
        self.get_read_position = core.async_with_raw_response(
            get_read_position, client.get_read_position
        )
        self.read_records = core.async_with_raw_response(read_records, client.read_records)
        self.reset_offsets = core.async_with_raw_response(reset_offsets, client.reset_offsets)


class _AsyncSubscriberClientStreaming:
    def __init__(self, client: AsyncSubscriberClient) -> None:
        def commit_offsets(_: streams_models.PartitionOffsets): ...
        def create(_: streams_models.Subscriber): ...
        def get_read_position(_: streams_models.PartitionOffsets): ...
        def read_records(_: streams_models.ReadSubscriberRecordsResponse): ...
        def reset_offsets(_: streams_models.PartitionOffsets): ...

        self.commit_offsets = core.async_with_streaming_response(
            commit_offsets, client.commit_offsets
        )
        self.create = core.async_with_streaming_response(create, client.create)
        self.get_read_position = core.async_with_streaming_response(
            get_read_position, client.get_read_position
        )
        self.read_records = core.async_with_streaming_response(read_records, client.read_records)
        self.reset_offsets = core.async_with_streaming_response(reset_offsets, client.reset_offsets)
