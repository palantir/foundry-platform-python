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
from typing import Optional

from pydantic import Field
from pydantic import StrictInt
from pydantic import validate_call
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_name import DatasetName
from foundry.v2.filesystem.models._folder_rid import FolderRid
from foundry.v2.streams.models._compressed import Compressed
from foundry.v2.streams.models._dataset import Dataset
from foundry.v2.streams.models._partitions_count import PartitionsCount
from foundry.v2.streams.models._stream_type import StreamType
from foundry.v2.streams.stream import StreamClient


class DatasetClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

        self.Stream = StreamClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def create(
        self,
        *,
        name: DatasetName,
        parent_folder_rid: FolderRid,
        branch_name: Optional[BranchName] = None,
        compressed: Optional[Compressed] = None,
        partitions_count: Optional[PartitionsCount] = None,
        preview: Optional[PreviewMode] = None,
        stream_type: Optional[StreamType] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Creates a streaming dataset with a stream on the specified branch, or if no branch is specified, on the
        default branch ('master' for most enrollments). For more information on streaming datasets, refer to the
        [streams](/docs/foundry/data-integration/streams/) user documentation.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
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
                        "branchName": Optional[BranchName],
                        "partitionsCount": Optional[PartitionsCount],
                        "streamType": Optional[StreamType],
                        "compressed": Optional[Compressed],
                    },
                ),
                response_type=Dataset,
                request_timeout=request_timeout,
            ),
        )
