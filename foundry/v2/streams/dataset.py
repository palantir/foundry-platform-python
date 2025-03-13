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
from functools import cached_property

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.core import models as core_models
from foundry.v2.datasets import models as datasets_models
from foundry.v2.filesystem import errors as filesystem_errors
from foundry.v2.filesystem import models as filesystem_models
from foundry.v2.streams import errors as streams_errors
from foundry.v2.streams import models as streams_models


class DatasetClient:
    """
    The API client for the Dataset Resource.

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
        self.with_streaming_response = _DatasetClientStreaming(
            auth=auth, hostname=hostname, config=config
        )
        self.with_raw_response = _DatasetClientRaw(auth=auth, hostname=hostname, config=config)

    @cached_property
    def Stream(self):
        from foundry.v2.streams.stream import StreamClient

        return StreamClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        name: datasets_models.DatasetName,
        parent_folder_rid: filesystem_models.FolderRid,
        schema: typing.Union[core_models.StreamSchema, core_models.StreamSchemaDict],
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        compressed: typing.Optional[streams_models.Compressed] = None,
        partitions_count: typing.Optional[streams_models.PartitionsCount] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        stream_type: typing.Optional[streams_models.StreamType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> streams_models.Dataset:
        """
        Creates a streaming dataset with a stream on the specified branch, or if no branch is specified, on the
        default branch ('master' for most enrollments). For more information on streaming datasets, refer to the
        [streams](/docs/foundry/data-integration/streams/) user documentation.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param schema: The Foundry schema to apply to the new stream.
        :type schema: Union[StreamSchema, StreamSchemaDict]
        :param branch_name: The branch to create the initial stream on. If not specified, the default branch will be used ('master' for most enrollments).
        :type branch_name: Optional[BranchName]
        :param compressed: Whether or not compression is enabled for the stream. Defaults to false.
        :type compressed: Optional[Compressed]
        :param partitions_count: The number of partitions for the Foundry stream.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If not specified, 1 partition is used.  This value cannot be changed later.
        :type partitions_count: Optional[PartitionsCount]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: streams_models.Dataset

        :raises CreateStreamingDatasetPermissionDenied: Could not create the Dataset.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/streams/datasets/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "parentFolderRid": parent_folder_rid,
                    "schema": schema,
                    "branchName": branch_name,
                    "partitionsCount": partitions_count,
                    "streamType": stream_type,
                    "compressed": compressed,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": datasets_models.DatasetName,
                        "parentFolderRid": filesystem_models.FolderRid,
                        "schema": typing.Union[
                            core_models.StreamSchema, core_models.StreamSchemaDict
                        ],
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "partitionsCount": typing.Optional[streams_models.PartitionsCount],
                        "streamType": typing.Optional[streams_models.StreamType],
                        "compressed": typing.Optional[streams_models.Compressed],
                    },
                ),
                response_type=streams_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateStreamingDatasetPermissionDenied": streams_errors.CreateStreamingDatasetPermissionDenied,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        ).decode()


class _DatasetClientRaw:
    """
    The API client for the Dataset Resource.

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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        name: datasets_models.DatasetName,
        parent_folder_rid: filesystem_models.FolderRid,
        schema: typing.Union[core_models.StreamSchema, core_models.StreamSchemaDict],
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        compressed: typing.Optional[streams_models.Compressed] = None,
        partitions_count: typing.Optional[streams_models.PartitionsCount] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        stream_type: typing.Optional[streams_models.StreamType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[streams_models.Dataset]:
        """
        Creates a streaming dataset with a stream on the specified branch, or if no branch is specified, on the
        default branch ('master' for most enrollments). For more information on streaming datasets, refer to the
        [streams](/docs/foundry/data-integration/streams/) user documentation.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param schema: The Foundry schema to apply to the new stream.
        :type schema: Union[StreamSchema, StreamSchemaDict]
        :param branch_name: The branch to create the initial stream on. If not specified, the default branch will be used ('master' for most enrollments).
        :type branch_name: Optional[BranchName]
        :param compressed: Whether or not compression is enabled for the stream. Defaults to false.
        :type compressed: Optional[Compressed]
        :param partitions_count: The number of partitions for the Foundry stream.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If not specified, 1 partition is used.  This value cannot be changed later.
        :type partitions_count: Optional[PartitionsCount]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[streams_models.Dataset]

        :raises CreateStreamingDatasetPermissionDenied: Could not create the Dataset.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/streams/datasets/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "parentFolderRid": parent_folder_rid,
                    "schema": schema,
                    "branchName": branch_name,
                    "partitionsCount": partitions_count,
                    "streamType": stream_type,
                    "compressed": compressed,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": datasets_models.DatasetName,
                        "parentFolderRid": filesystem_models.FolderRid,
                        "schema": typing.Union[
                            core_models.StreamSchema, core_models.StreamSchemaDict
                        ],
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "partitionsCount": typing.Optional[streams_models.PartitionsCount],
                        "streamType": typing.Optional[streams_models.StreamType],
                        "compressed": typing.Optional[streams_models.Compressed],
                    },
                ),
                response_type=streams_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateStreamingDatasetPermissionDenied": streams_errors.CreateStreamingDatasetPermissionDenied,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        )


class _DatasetClientStreaming:
    """
    The API client for the Dataset Resource.

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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        name: datasets_models.DatasetName,
        parent_folder_rid: filesystem_models.FolderRid,
        schema: typing.Union[core_models.StreamSchema, core_models.StreamSchemaDict],
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        compressed: typing.Optional[streams_models.Compressed] = None,
        partitions_count: typing.Optional[streams_models.PartitionsCount] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        stream_type: typing.Optional[streams_models.StreamType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[streams_models.Dataset]:
        """
        Creates a streaming dataset with a stream on the specified branch, or if no branch is specified, on the
        default branch ('master' for most enrollments). For more information on streaming datasets, refer to the
        [streams](/docs/foundry/data-integration/streams/) user documentation.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param schema: The Foundry schema to apply to the new stream.
        :type schema: Union[StreamSchema, StreamSchemaDict]
        :param branch_name: The branch to create the initial stream on. If not specified, the default branch will be used ('master' for most enrollments).
        :type branch_name: Optional[BranchName]
        :param compressed: Whether or not compression is enabled for the stream. Defaults to false.
        :type compressed: Optional[Compressed]
        :param partitions_count: The number of partitions for the Foundry stream.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If not specified, 1 partition is used.  This value cannot be changed later.
        :type partitions_count: Optional[PartitionsCount]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[streams_models.Dataset]

        :raises CreateStreamingDatasetPermissionDenied: Could not create the Dataset.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.stream_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/streams/datasets/create",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "parentFolderRid": parent_folder_rid,
                    "schema": schema,
                    "branchName": branch_name,
                    "partitionsCount": partitions_count,
                    "streamType": stream_type,
                    "compressed": compressed,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": datasets_models.DatasetName,
                        "parentFolderRid": filesystem_models.FolderRid,
                        "schema": typing.Union[
                            core_models.StreamSchema, core_models.StreamSchemaDict
                        ],
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "partitionsCount": typing.Optional[streams_models.PartitionsCount],
                        "streamType": typing.Optional[streams_models.StreamType],
                        "compressed": typing.Optional[streams_models.Compressed],
                    },
                ),
                response_type=streams_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateStreamingDatasetPermissionDenied": streams_errors.CreateStreamingDatasetPermissionDenied,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        )
