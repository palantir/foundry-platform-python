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
from pydantic import StrictInt
from typing import Annotated
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field
from pydantic import validate_call

from foundry._errors.sdk_internal_error import handle_unexpected
from foundry.api_client import ApiClient

from foundry.models._branch_id import BranchId
from foundry.models._dataset_rid import DatasetRid
from foundry.models._file import File
from foundry.models._file_path import FilePath
from foundry.models._list_files_response import ListFilesResponse
from foundry.models._page_size import PageSize
from foundry.models._page_token import PageToken
from foundry.models._transaction_rid import TransactionRid
from foundry.models._transaction_type import TransactionType


class FileResource:
    def __init__(self, api_client: ApiClient) -> None:
        self._api_client = api_client

    @validate_call
    @handle_unexpected
    def iterator(
        self,
        dataset_rid: DatasetRid,
        *,
        branch_id: Optional[BranchId] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        page_size: Optional[PageSize] = None,
        page_token: Optional[PageToken] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> ListFilesResponse:
        """
        Lists Files contained in a Dataset. By default files are listed on the latest view of the default
        branch - `master` for most enrollments.

        #### Advanced Usage

        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

        To **list files on a specific Branch** specify the Branch's identifier as `branchId`. This will include the most
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

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to list Files.
        :type dataset_rid: DatasetRid
        :param branch_id: The identifier (name) of the Branch on which to list Files. Defaults to `master` for most enrollments.
        :type branch_id: Optional[BranchId]
        :param start_transaction_rid: The Resource Identifier (RID) of the start Transaction.
        :type start_transaction_rid: Optional[TransactionRid]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param page_size: The desired size of the page to be returned. Defaults to 1,000. See [page sizes](/docs/foundry/api/general/overview/paging/#page-sizes) for details.
        :type page_size: Optional[PageSize]
        :param page_token: pageToken
        :type page_token: Optional[PageToken]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ListFilesResponse
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["branchId"] = branch_id

        _query_params["startTransactionRid"] = start_transaction_rid

        _query_params["endTransactionRid"] = end_transaction_rid

        _query_params["pageSize"] = page_size

        _query_params["pageToken"] = page_token

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: ListFilesResponse,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/datasets/{datasetRid}/files".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def upload(
        self,
        dataset_rid: DatasetRid,
        *,
        body: bytes,
        file_path: FilePath,
        branch_id: Optional[BranchId] = None,
        transaction_rid: Optional[TransactionRid] = None,
        transaction_type: Optional[TransactionType] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> File:
        """
        Uploads a File to an existing Dataset.
        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

        By default the file is uploaded to a new transaction on the default branch - `master` for most enrollments.
        If the file already exists only the most recent version will be visible in the updated view.

        #### Advanced Usage

        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

        To **upload a file to a specific Branch** specify the Branch's identifier as `branchId`. A new transaction will
        be created and committed on this branch. By default the TransactionType will be `UPDATE`, to override this
        default specify `transactionType` in addition to `branchId`.
        See [createBranch](/docs/foundry/api/datasets-resources/branches/create-branch/) to create a custom branch.

        To **upload a file on a manually opened transaction** specify the Transaction's resource identifier as
        `transactionRid`. This is useful for uploading multiple files in a single transaction.
        See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to open a transaction.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to upload the File.
        :type dataset_rid: DatasetRid
        :param file_path: The File's path within the Dataset.
        :type file_path: FilePath
        :param branch_id: The identifier (name) of the Branch on which to upload the File. Defaults to `master` for most enrollments.
        :type branch_id: Optional[BranchId]
        :param transaction_type: The type of the Transaction to create when using branchId. Defaults to `UPDATE`.
        :type transaction_type: Optional[TransactionType]
        :param transaction_rid: The Resource Identifier (RID) of the open Transaction on which to upload the File.
        :type transaction_rid: Optional[TransactionRid]
        :param body: Body of the request
        :type body: bytes
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: File
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = body
        _query_params["filePath"] = file_path

        _query_params["branchId"] = branch_id

        _query_params["transactionType"] = transaction_type

        _query_params["transactionRid"] = transaction_rid

        _path_params["datasetRid"] = dataset_rid

        _header_params["Accept"] = "application/json"

        _header_params["Content-Type"] = "*/*"

        _response_types_map: Dict[int, Any] = {
            200: File,
        }

        return self._api_client.call_api(
            method="POST",
            resource_path="/v1/datasets/{datasetRid}/files:upload".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def get_metadata(
        self,
        dataset_rid: DatasetRid,
        file_path: FilePath,
        *,
        branch_id: Optional[BranchId] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> File:
        """
        Gets metadata about a File contained in a Dataset. By default this retrieves the file's metadata from the latest
        view of the default branch - `master` for most enrollments.

        #### Advanced Usage

        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

        To **get a file's metadata from a specific Branch** specify the Branch's identifier as `branchId`. This will
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

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset that contains the File.
        :type dataset_rid: DatasetRid
        :param file_path: The File's path within the Dataset.
        :type file_path: FilePath
        :param branch_id: The identifier (name) of the Branch that contains the File. Defaults to `master` for most enrollments.
        :type branch_id: Optional[BranchId]
        :param start_transaction_rid: The Resource Identifier (RID) of the start Transaction.
        :type start_transaction_rid: Optional[TransactionRid]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: File
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["branchId"] = branch_id

        _query_params["startTransactionRid"] = start_transaction_rid

        _query_params["endTransactionRid"] = end_transaction_rid

        _path_params["datasetRid"] = dataset_rid

        _path_params["filePath"] = file_path

        _header_params["Accept"] = "application/json"

        _response_types_map: Dict[int, Any] = {
            200: File,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/datasets/{datasetRid}/files/{filePath}".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def delete(
        self,
        dataset_rid: DatasetRid,
        file_path: FilePath,
        *,
        branch_id: Optional[BranchId] = None,
        transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> None:
        """
        Deletes a File from a Dataset. By default the file is deleted in a new transaction on the default
        branch - `master` for most enrollments. The file will still be visible on historical views.

        #### Advanced Usage

        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

        To **delete a File from a specific Branch** specify the Branch's identifier as `branchId`. A new delete Transaction
        will be created and committed on this branch.

        To **delete a File using a manually opened Transaction**, specify the Transaction's resource identifier
        as `transactionRid`. The transaction must be of type `DELETE`. This is useful for deleting multiple files in a
        single transaction. See [createTransaction](/docs/foundry/api/datasets-resources/transactions/create-transaction/) to
        open a transaction.

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-write`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset on which to delete the File.
        :type dataset_rid: DatasetRid
        :param file_path: The File path within the Dataset.
        :type file_path: FilePath
        :param branch_id: The identifier (name) of the Branch on which to delete the File. Defaults to `master` for most enrollments.
        :type branch_id: Optional[BranchId]
        :param transaction_rid: The Resource Identifier (RID) of the open delete Transaction on which to delete the File.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["branchId"] = branch_id

        _query_params["transactionRid"] = transaction_rid

        _path_params["datasetRid"] = dataset_rid

        _path_params["filePath"] = file_path

        _response_types_map: Dict[int, Any] = {
            204: None,
        }

        return self._api_client.call_api(
            method="DELETE",
            resource_path="/v1/datasets/{datasetRid}/files/{filePath}".format(**_path_params),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )

    @validate_call
    @handle_unexpected
    def get_content(
        self,
        dataset_rid: DatasetRid,
        file_path: FilePath,
        *,
        branch_id: Optional[BranchId] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[StrictInt, Field(gt=0)]] = None,
    ) -> bytes:
        """
        Gets the content of a File contained in a Dataset. By default this retrieves the file's content from the latest
        view of the default branch - `master` for most enrollments.

        #### Advanced Usage

        See [Datasets Core Concepts](/docs/foundry/data-integration/datasets/) for details on using branches and transactions.

        To **get a file's content from a specific Branch** specify the Branch's identifier as `branchId`. This will
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

        Third-party applications using this endpoint via OAuth2 must request the following operation scope: `api:datasets-read`.

        :param dataset_rid: The Resource Identifier (RID) of the Dataset that contains the File.
        :type dataset_rid: DatasetRid
        :param file_path: The File's path within the Dataset.
        :type file_path: FilePath
        :param branch_id: The identifier (name) of the Branch that contains the File. Defaults to `master` for most enrollments.
        :type branch_id: Optional[BranchId]
        :param start_transaction_rid: The Resource Identifier (RID) of the start Transaction.
        :type start_transaction_rid: Optional[TransactionRid]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        _path_params: Dict[str, str] = {}
        _query_params: Dict[str, Any] = {}
        _header_params: Dict[str, str] = {}
        _body_params: Any = None
        _query_params["branchId"] = branch_id

        _query_params["startTransactionRid"] = start_transaction_rid

        _query_params["endTransactionRid"] = end_transaction_rid

        _path_params["datasetRid"] = dataset_rid

        _path_params["filePath"] = file_path

        _header_params["Accept"] = "*/*"

        _response_types_map: Dict[int, Any] = {
            200: bytes,
        }

        return self._api_client.call_api(
            method="GET",
            resource_path="/v1/datasets/{datasetRid}/files/{filePath}/content".format(
                **_path_params
            ),
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            response_types_map=_response_types_map,
            request_timeout=request_timeout,
        )
