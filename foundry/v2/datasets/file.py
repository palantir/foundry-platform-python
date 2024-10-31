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

import pydantic
from typing_extensions import Annotated

from foundry._core import ApiClient
from foundry._core import Auth
from foundry._core import RequestInfo
from foundry._core import ResourceIterator
from foundry._errors import handle_unexpected
from foundry.v2.core.models._file_path import FilePath
from foundry.v2.core.models._page_size import PageSize
from foundry.v2.core.models._page_token import PageToken
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.datasets.models._file import File
from foundry.v2.datasets.models._list_files_response import ListFilesResponse
from foundry.v2.datasets.models._transaction_rid import TransactionRid
from foundry.v2.datasets.models._transaction_type import TransactionType


class FileClient:
    def __init__(self, auth: Auth, hostname: str) -> None:
        self._api_client = ApiClient(auth=auth, hostname=hostname)

    @pydantic.validate_call
    @handle_unexpected
    def content(
        self,
        dataset_rid: DatasetRid,
        file_path: FilePath,
        *,
        branch_name: Optional[BranchName] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> bytes:
        """
        Gets the content of a File contained in a Dataset. By default this retrieves the file's content from the latest
        view of the default branch - `master` for most enrollments.
        #### Advanced Usage
        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
        To **get a file's content from a specific Branch** specify the Branch's name as `branchName`. This will
        retrieve the content for the most recent version of the file since the latest snapshot transaction, or the
        earliest ancestor transaction of the branch if there are no snapshot transactions.
        To **get a file's content from the resolved view of a transaction** specify the Transaction's resource identifier
        as `endTransactionRid`. This will retrieve the content for the most recent version of the file since the latest
        snapshot transaction, or the earliest ancestor transaction if there are no snapshot transactions.
        To **get a file's content from the resolved view of a range of transactions** specify the the start transaction's
        resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`.
        This will retrieve the content for the most recent version of the file since the `startTransactionRid` up to the
        `endTransactionRid`. Note that an intermediate snapshot transaction will remove all files from the view. Behavior
        is undefined when the start and end transactions do not belong to the same root-to-leaf path.
        To **get a file's content from a specific transaction** specify the Transaction's resource identifier as both the
        `startTransactionRid` and `endTransactionRid`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param file_path: filePath
        :type file_path: FilePath
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
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
                resource_path="/v2/datasets/{datasetRid}/files/{filePath}/content",
                query_params={
                    "branchName": branch_name,
                    "endTransactionRid": end_transaction_rid,
                    "startTransactionRid": start_transaction_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "filePath": file_path,
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

    @pydantic.validate_call
    @handle_unexpected
    def delete(
        self,
        dataset_rid: DatasetRid,
        file_path: FilePath,
        *,
        branch_name: Optional[BranchName] = None,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> None:
        """
        Deletes a File from a Dataset. By default the file is deleted in a new transaction on the default
        branch - `master` for most enrollments. The file will still be visible on historical views.
        #### Advanced Usage
        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
        To **delete a File from a specific Branch** specify the Branch's name as `branchName`. A new delete Transaction
        will be created and committed on this branch.
        To **delete a File using a manually opened Transaction**, specify the Transaction's resource identifier
        as `transactionRid`. The transaction must be of type `DELETE`. This is useful for deleting multiple files in a
        single transaction. See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to
        open a transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param file_path: filePath
        :type file_path: FilePath
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
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
                resource_path="/v2/datasets/{datasetRid}/files/{filePath}",
                query_params={
                    "branchName": branch_name,
                    "transactionRid": transaction_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "filePath": file_path,
                },
                header_params={},
                body=None,
                body_type=None,
                response_type=None,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        file_path: FilePath,
        *,
        branch_name: Optional[BranchName] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> File:
        """
        Gets metadata about a File contained in a Dataset. By default this retrieves the file's metadata from the latest
        view of the default branch - `master` for most enrollments.
        #### Advanced Usage
        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
        To **get a file's metadata from a specific Branch** specify the Branch's name as `branchName`. This will
        retrieve metadata for the most recent version of the file since the latest snapshot transaction, or the earliest
        ancestor transaction of the branch if there are no snapshot transactions.
        To **get a file's metadata from the resolved view of a transaction** specify the Transaction's resource identifier
        as `endTransactionRid`. This will retrieve metadata for the most recent version of the file since the latest snapshot
        transaction, or the earliest ancestor transaction if there are no snapshot transactions.
        To **get a file's metadata from the resolved view of a range of transactions** specify the the start transaction's
        resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`.
        This will retrieve metadata for the most recent version of the file since the `startTransactionRid` up to the
        `endTransactionRid`. Behavior is undefined when the start and end transactions do not belong to the same root-to-leaf path.
        To **get a file's metadata from a specific transaction** specify the Transaction's resource identifier as both the
        `startTransactionRid` and `endTransactionRid`.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param file_path: filePath
        :type file_path: FilePath
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: File
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/files/{filePath}",
                query_params={
                    "branchName": branch_name,
                    "endTransactionRid": end_transaction_rid,
                    "startTransactionRid": start_transaction_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "filePath": file_path,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=File,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def list(
        self,
        dataset_rid: DatasetRid,
        *,
        branch_name: Optional[BranchName] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        page_size: Optional[PageSize] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ResourceIterator[File]:
        """
        Lists Files contained in a Dataset. By default files are listed on the latest view of the default
        branch - `master` for most enrollments.
        #### Advanced Usage
        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
        To **list files on a specific Branch** specify the Branch's name as `branchName`. This will include the most
        recent version of all files since the latest snapshot transaction, or the earliest ancestor transaction of the
        branch if there are no snapshot transactions.
        To **list files on the resolved view of a transaction** specify the Transaction's resource identifier
        as `endTransactionRid`. This will include the most recent version of all files since the latest snapshot
        transaction, or the earliest ancestor transaction if there are no snapshot transactions.
        To **list files on the resolved view of a range of transactions** specify the the start transaction's resource
        identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This
        will include the most recent version of all files since the `startTransactionRid` up to the `endTransactionRid`.
        Note that an intermediate snapshot transaction will remove all files from the view. Behavior is undefined when
        the start and end transactions do not belong to the same root-to-leaf path.
        To **list files on a specific transaction** specify the Transaction's resource identifier as both the
        `startTransactionRid` and `endTransactionRid`. This will include only files that were modified as part of that
        Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ResourceIterator[File]
        """

        return self._api_client.iterate_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/files",
                query_params={
                    "branchName": branch_name,
                    "endTransactionRid": end_transaction_rid,
                    "pageSize": page_size,
                    "startTransactionRid": start_transaction_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListFilesResponse,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def page(
        self,
        dataset_rid: DatasetRid,
        *,
        branch_name: Optional[BranchName] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ListFilesResponse:
        """
        Lists Files contained in a Dataset. By default files are listed on the latest view of the default
        branch - `master` for most enrollments.
        #### Advanced Usage
        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
        To **list files on a specific Branch** specify the Branch's name as `branchName`. This will include the most
        recent version of all files since the latest snapshot transaction, or the earliest ancestor transaction of the
        branch if there are no snapshot transactions.
        To **list files on the resolved view of a transaction** specify the Transaction's resource identifier
        as `endTransactionRid`. This will include the most recent version of all files since the latest snapshot
        transaction, or the earliest ancestor transaction if there are no snapshot transactions.
        To **list files on the resolved view of a range of transactions** specify the the start transaction's resource
        identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This
        will include the most recent version of all files since the `startTransactionRid` up to the `endTransactionRid`.
        Note that an intermediate snapshot transaction will remove all files from the view. Behavior is undefined when
        the start and end transactions do not belong to the same root-to-leaf path.
        To **list files on a specific transaction** specify the Transaction's resource identifier as both the
        `startTransactionRid` and `endTransactionRid`. This will include only files that were modified as part of that
        Transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param page_size: pageSize
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListFilesResponse
        """

        return self._api_client.call_api(
            RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/files",
                query_params={
                    "branchName": branch_name,
                    "endTransactionRid": end_transaction_rid,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "startTransactionRid": start_transaction_rid,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=ListFilesResponse,
                request_timeout=request_timeout,
            ),
        )

    @pydantic.validate_call
    @handle_unexpected
    def upload(
        self,
        dataset_rid: DatasetRid,
        file_path: FilePath,
        body: bytes,
        *,
        branch_name: Optional[BranchName] = None,
        transaction_rid: Optional[TransactionRid] = None,
        transaction_type: Optional[TransactionType] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> File:
        """
        Uploads a File to an existing Dataset.
        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
        By default the file is uploaded to a new transaction on the default branch - `master` for most enrollments.
        If the file already exists only the most recent version will be visible in the updated view.
        #### Advanced Usage
        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
        To **upload a file to a specific Branch** specify the Branch's name as `branchName`. A new transaction will
        be created and committed on this branch. By default the TransactionType will be `UPDATE`, to override this
        default specify `transactionType` in addition to `branchName`.
        See [createBranch](/docs/foundry/api/datasets-resources/branches/create-branch/) to create a custom branch.
        To **upload a file on a manually opened transaction** specify the Transaction's resource identifier as
        `transactionRid`. This is useful for uploading multiple files in a single transaction.
        See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to open a transaction.

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param file_path: filePath
        :type file_path: FilePath
        :param body: Body of the request
        :type body: bytes
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param transaction_rid: transactionRid
        :type transaction_rid: Optional[TransactionRid]
        :param transaction_type: transactionType
        :type transaction_type: Optional[TransactionType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: File
        """

        return self._api_client.call_api(
            RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/files/{filePath}/upload",
                query_params={
                    "branchName": branch_name,
                    "transactionRid": transaction_rid,
                    "transactionType": transaction_type,
                },
                path_params={
                    "datasetRid": dataset_rid,
                    "filePath": file_path,
                },
                header_params={
                    "Content-Type": "application/octet-stream",
                    "Accept": "application/json",
                },
                body=body,
                body_type=bytes,
                response_type=File,
                request_timeout=request_timeout,
            ),
        )
