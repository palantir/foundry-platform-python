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
from foundry.v1.core.models._folder_rid import FolderRid
from foundry.v1.core.models._preview_mode import PreviewMode
from foundry.v1.datasets.branch import BranchClient
from foundry.v1.datasets.file import FileClient
from foundry.v1.datasets.models._branch_id import BranchId
from foundry.v1.datasets.models._dataset import Dataset
from foundry.v1.datasets.models._dataset_name import DatasetName
from foundry.v1.datasets.models._dataset_rid import DatasetRid
from foundry.v1.datasets.models._table_export_format import TableExportFormat
from foundry.v1.datasets.models._transaction_rid import TransactionRid
from foundry.v1.datasets.transaction import TransactionClient


class DatasetClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

        self.Branch = BranchClient(auth=auth, hostname=hostname)
        self.File = FileClient(auth=auth, hostname=hostname)
        self.Transaction = TransactionClient(auth=auth, hostname=hostname)

    @validate_call
    @handle_unexpected
    def create(
        self,
        *,
        name: DatasetName,
        parent_folder_rid: FolderRid,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v1/datasets",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "parentFolderRid": parent_folder_rid,
                },
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": DatasetName,
                        "parentFolderRid": FolderRid,
                    },
                ),
                response_type=Dataset,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def delete_schema(
        self,
        dataset_rid: DatasetRid,
        *,
        branch_id: Optional[BranchId] = None,
        preview: Optional[PreviewMode] = None,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """
        Deletes the Schema from a Dataset and Branch.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_id: branchId
        :type branch_id: Optional[BranchId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param transaction_rid: transactionRid
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
                method="DELETE",
                resource_path="/v1/datasets/{datasetRid}/schema",
                query_params={
                    "branchId": branch_id,
                    "preview": preview,
                    "transactionRid": transaction_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        *,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Gets the Dataset with the given DatasetRid.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}",
                query_params={},
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
    def get_schema(
        self,
        dataset_rid: DatasetRid,
        *,
        branch_id: Optional[BranchId] = None,
        preview: Optional[PreviewMode] = None,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> Any:
        """
        Retrieves the Schema for a Dataset and Branch, if it exists.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_id: branchId
        :type branch_id: Optional[BranchId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param transaction_rid: transactionRid
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Any
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v1/datasets/{datasetRid}/schema",
                query_params={
                    "branchId": branch_id,
                    "preview": preview,
                    "transactionRid": transaction_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=Any,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def read(
        self,
        dataset_rid: DatasetRid,
        *,
        format: TableExportFormat,
        branch_id: Optional[BranchId] = None,
        columns: Optional[List[StrictStr]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        row_limit: Optional[StrictInt] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (Virtual datasets composed of other datasets).

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param format: format
        :type format: TableExportFormat
        :param branch_id: branchId
        :type branch_id: Optional[BranchId]
        :param columns: columns
        :type columns: Optional[List[StrictStr]]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
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
                resource_path="/v1/datasets/{datasetRid}/readTable",
                query_params={
                    "format": format,
                    "branchId": branch_id,
                    "columns": columns,
                    "endTransactionRid": end_transaction_rid,
                    "rowLimit": row_limit,
                    "startTransactionRid": start_transaction_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
            ),
        )

    @validate_call
    @handle_unexpected
    def replace_schema(
        self,
        dataset_rid: DatasetRid,
        body: Any,
        *,
        branch_id: Optional[BranchId] = None,
        preview: Optional[PreviewMode] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """
        Puts a Schema on an existing Dataset and Branch.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param body: Body of the request
        :type body: Any
        :param branch_id: branchId
        :type branch_id: Optional[BranchId]
        :param preview: preview
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        return self._api_client.call_api(
            RequestInfo(
                method="PUT",
                resource_path="/v1/datasets/{datasetRid}/schema",
                query_params={
                    "branchId": branch_id,
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                },
                body=body,
                body_type=Any,
                response_type=None,
                request_timeout=request_timeout,
            ),
        )
