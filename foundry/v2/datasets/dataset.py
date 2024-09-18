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
from pydantic import StrictStr
from pydantic import validate_call
from typing_extensions import Annotated
from typing_extensions import TypedDict

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._errors import handle_unexpected
from foundry.v2.core.models._preview_mode import PreviewMode
from foundry.v2.datasets.branch import BranchClient
from foundry.v2.datasets.file import FileClient
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset import Dataset
from foundry.v2.datasets.models._dataset_name import DatasetName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.datasets.models._table_export_format import TableExportFormat
from foundry.v2.datasets.models._transaction_rid import TransactionRid
from foundry.v2.datasets.transaction import TransactionClient
from foundry.v2.filesystem.models._folder_rid import FolderRid


class DatasetClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

        self.Branch = BranchClient(auth=auth, hostname=hostname)
        self.Transaction = TransactionClient(auth=auth, hostname=hostname)
        self.File = FileClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def create(
        self,
        *,
        name: DatasetName,
        parent_folder_rid: FolderRid,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "name": name,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "name": DatasetName,
                    },
                ),
                response_type=Dataset,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        *,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Get the Dataset with the specified rid.
        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Dataset,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def read_table(
        self,
        dataset_rid: DatasetRid,
        *,
        format: TableExportFormat,
        branch_name: Optional[BranchName] = None,
        columns: Optional[List[StrictStr]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        preview: Optional[PreviewMode] = None,
        row_limit: Optional[StrictInt] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (Virtual datasets composed of other datasets).

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param format: format
        :type format: TableExportFormat
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param columns: columns
        :type columns: Optional[List[StrictStr]]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param row_limit: rowLimit
        :type row_limit: Optional[StrictInt]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/readTable",
                query_params={
                    "format": format,
                    "branchName": branch_name,
                    "columns": columns,
                    "endTransactionRid": end_transaction_rid,
                    "preview": preview,
                    "rowLimit": row_limit,
                    "startTransactionRid": start_transaction_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/octet-stream",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )
