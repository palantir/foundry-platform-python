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

from functools import cached_property
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.core.models._stream_schema import StreamSchema
from foundry.v2.core.models._stream_schema_dict import StreamSchemaDict
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_name import DatasetName
from foundry.v2.filesystem import errors as filesystem_errors
from foundry.v2.filesystem.models._folder_rid import FolderRid
from foundry.v2.streams import errors as streams_errors
from foundry.v2.streams.models._compressed import Compressed
from foundry.v2.streams.models._dataset import Dataset
from foundry.v2.streams.models._partitions_count import PartitionsCount
from foundry.v2.streams.models._stream_type import StreamType


class DatasetClient:
    """
    The API client for the Dataset Resource.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)
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

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        name: DatasetName,
        parent_folder_rid: FolderRid,
        schema: Union[StreamSchema, StreamSchemaDict],
        branch_name: Optional[BranchName] = None,
        compressed: Optional[Compressed] = None,
        partitions_count: Optional[PartitionsCount] = None,
        preview: Optional[PreviewMode] = None,
        stream_type: Optional[StreamType] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Dataset:
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
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset

        :raises CreateStreamingDatasetPermissionDenied: Could not create the Dataset.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": DatasetName,
                        "parentFolderRid": FolderRid,
                        "schema": Union[StreamSchema, StreamSchemaDict],
                        "branchName": Optional[BranchName],
                        "partitionsCount": Optional[PartitionsCount],
                        "streamType": Optional[StreamType],
                        "compressed": Optional[Compressed],
                    },
                ),
                response_type=Dataset,
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
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        name: DatasetName,
        parent_folder_rid: FolderRid,
        schema: Union[StreamSchema, StreamSchemaDict],
        branch_name: Optional[BranchName] = None,
        compressed: Optional[Compressed] = None,
        partitions_count: Optional[PartitionsCount] = None,
        preview: Optional[PreviewMode] = None,
        stream_type: Optional[StreamType] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Dataset]:
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
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Dataset]

        :raises CreateStreamingDatasetPermissionDenied: Could not create the Dataset.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": DatasetName,
                        "parentFolderRid": FolderRid,
                        "schema": Union[StreamSchema, StreamSchemaDict],
                        "branchName": Optional[BranchName],
                        "partitionsCount": Optional[PartitionsCount],
                        "streamType": Optional[StreamType],
                        "compressed": Optional[Compressed],
                    },
                ),
                response_type=Dataset,
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
        auth: Auth,
        hostname: str,
        config: Optional[Config] = None,
    ):
        self._auth = auth
        self._hostname = hostname
        self._config = config
        self._api_client = ApiClient(auth=auth, hostname=hostname, config=config)

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        name: DatasetName,
        parent_folder_rid: FolderRid,
        schema: Union[StreamSchema, StreamSchemaDict],
        branch_name: Optional[BranchName] = None,
        compressed: Optional[Compressed] = None,
        partitions_count: Optional[PartitionsCount] = None,
        preview: Optional[PreviewMode] = None,
        stream_type: Optional[StreamType] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Dataset]:
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
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param stream_type: A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.
        :type stream_type: Optional[StreamType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Dataset]

        :raises CreateStreamingDatasetPermissionDenied: Could not create the Dataset.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": DatasetName,
                        "parentFolderRid": FolderRid,
                        "schema": Union[StreamSchema, StreamSchemaDict],
                        "branchName": Optional[BranchName],
                        "partitionsCount": Optional[PartitionsCount],
                        "streamType": Optional[StreamType],
                        "compressed": Optional[Compressed],
                    },
                ),
                response_type=Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateStreamingDatasetPermissionDenied": streams_errors.CreateStreamingDatasetPermissionDenied,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        )
