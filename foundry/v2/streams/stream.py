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
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.streams.models._record import Record
from foundry.v2.streams.models._stream import Stream
from foundry.v2.streams.models._view_rid import ViewRid


class StreamClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        stream_branch_name: BranchName,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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

    @validate_call
    @handle_unexpected
    def publish_record(
        self,
        dataset_rid: DatasetRid,
        stream_branch_name: BranchName,
        *,
        record: Record,
        preview: Optional[PreviewMode] = None,
        view_rid: Optional[ViewRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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

    @validate_call
    @handle_unexpected
    def publish_records(
        self,
        dataset_rid: DatasetRid,
        stream_branch_name: BranchName,
        *,
        records: List[Record],
        preview: Optional[PreviewMode] = None,
        view_rid: Optional[ViewRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
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
