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
from foundry_sdk.v2.datasets import errors as datasets_errors
from foundry_sdk.v2.datasets import models as datasets_models


class FileClient:
    """
    The API client for the File Resource.

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

        self.with_streaming_response = _FileClientStreaming(self)
        self.with_raw_response = _FileClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def content(
        self,
        dataset_rid: datasets_models.DatasetRid,
        file_path: core_models.FilePath,
        *,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        start_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Gets the content of a File contained in a Dataset. By default this retrieves the file's content from the latest
        view of the default branch - `master` for most enrollments.
        #### Advanced Usage
        See [Datasets Core Concepts](https://palantir.com/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
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

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param file_path:
        :type file_path: FilePath
        :param branch_name: The name of the Branch that contains the File. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param start_transaction_rid: The Resource Identifier (RID) of the start Transaction.
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FileNotFoundOnBranch: The requested file could not be found on the given branch, or the client token does not have access to it.
        :raises GetFileContentPermissionDenied: Could not content the File.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "FileNotFoundOnBranch": datasets_errors.FileNotFoundOnBranch,
                    "GetFileContentPermissionDenied": datasets_errors.GetFileContentPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        dataset_rid: datasets_models.DatasetRid,
        file_path: core_models.FilePath,
        *,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Deletes a File from a Dataset. By default the file is deleted in a new transaction on the default
        branch - `master` for most enrollments. The file will still be visible on historical views.
        #### Advanced Usage
        See [Datasets Core Concepts](https://palantir.com/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
        To **delete a File from a specific Branch** specify the Branch's name as `branchName`. A new delete Transaction
        will be created and committed on this branch.
        To **delete a File using a manually opened Transaction**, specify the Transaction's resource identifier
        as `transactionRid`. The transaction must be of type `DELETE`. This is useful for deleting multiple files in a
        single transaction. See [createTransaction](https://palantir.com/docs/foundry/api/datasets-resources/transactions/create-transaction/) to
        open a transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param file_path:
        :type file_path: FilePath
        :param branch_name: The name of the Branch on which to delete the File. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param transaction_rid: The Resource Identifier (RID) of the open delete Transaction on which to delete the File.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DeleteFilePermissionDenied: Could not delete the File.
        :raises FileNotFoundOnBranch: The requested file could not be found on the given branch, or the client token does not have access to it.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DeleteFilePermissionDenied": datasets_errors.DeleteFilePermissionDenied,
                    "FileNotFoundOnBranch": datasets_errors.FileNotFoundOnBranch,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
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
        file_path: core_models.FilePath,
        *,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        start_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.File:
        """
        Gets metadata about a File contained in a Dataset. By default this retrieves the file's metadata from the latest
        view of the default branch - `master` for most enrollments.
        #### Advanced Usage
        See [Datasets Core Concepts](https://palantir.com/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
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

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param file_path:
        :type file_path: FilePath
        :param branch_name: The name of the Branch that contains the File. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param start_transaction_rid: The Resource Identifier (RID) of the start Transaction.
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.File

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FileNotFound: The given File could not be found.
        :raises FileNotFoundOnBranch: The requested file could not be found on the given branch, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.File,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "FileNotFound": datasets_errors.FileNotFound,
                    "FileNotFoundOnBranch": datasets_errors.FileNotFoundOnBranch,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def list(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        start_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[datasets_models.File]:
        """
        Lists Files contained in a Dataset. By default files are listed on the latest view of the default
        branch - `master` for most enrollments.
        #### Advanced Usage
        See [Datasets Core Concepts](https://palantir.com/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
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

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name: The name of the Branch on which to list Files. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param start_transaction_rid: The Resource Identifier (RID) of the start Transaction.
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[datasets_models.File]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.ListFilesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def upload(
        self,
        dataset_rid: datasets_models.DatasetRid,
        file_path: core_models.FilePath,
        body: bytes,
        *,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        transaction_type: typing.Optional[datasets_models.TransactionType] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.File:
        """
        Uploads a File to an existing Dataset.
        The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
        By default the file is uploaded to a new transaction on the default branch - `master` for most enrollments.
        If the file already exists only the most recent version will be visible in the updated view.
        #### Advanced Usage
        See [Datasets Core Concepts](https://palantir.com/docs/foundry/data-integration/datasets/) for details on using branches and transactions.
        To **upload a file to a specific Branch** specify the Branch's name as `branchName`. A new transaction will
        be created and committed on this branch. By default the TransactionType will be `UPDATE`, to override this
        default specify `transactionType` in addition to `branchName`.
        See [createBranch](https://palantir.com/docs/foundry/api/datasets-resources/branches/create-branch/) to create a custom branch.
        To **upload a file on a manually opened transaction** specify the Transaction's resource identifier as
        `transactionRid`. This is useful for uploading multiple files in a single transaction.
        See [createTransaction](https://palantir.com/docs/foundry/api/datasets-resources/transactions/create-transaction/) to open a transaction.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param file_path:
        :type file_path: FilePath
        :param body: Body of the request
        :type body: bytes
        :param branch_name: The name of the Branch on which to upload the File. Defaults to `master` for most enrollments.
        :type branch_name: Optional[BranchName]
        :param transaction_rid: The Resource Identifier (RID) of the open Transaction on which to upload the File.
        :type transaction_rid: Optional[TransactionRid]
        :param transaction_type: The type of the Transaction to create when using branchName. Defaults to `UPDATE`.
        :type transaction_type: Optional[TransactionType]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.File

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FileAlreadyExists: The given file path already exists in the dataset and transaction.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        :raises UploadFilePermissionDenied: The provided token does not have permission to upload the given file to the given dataset and transaction.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.File,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "FileAlreadyExists": datasets_errors.FileAlreadyExists,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
                    "UploadFilePermissionDenied": datasets_errors.UploadFilePermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _FileClientRaw:
    def __init__(self, client: FileClient) -> None:
        def content(_: bytes): ...
        def delete(_: None): ...
        def get(_: datasets_models.File): ...
        def list(_: datasets_models.ListFilesResponse): ...
        def upload(_: datasets_models.File): ...

        self.content = core.with_raw_response(content, client.content)
        self.delete = core.with_raw_response(delete, client.delete)
        self.get = core.with_raw_response(get, client.get)
        self.list = core.with_raw_response(list, client.list)
        self.upload = core.with_raw_response(upload, client.upload)


class _FileClientStreaming:
    def __init__(self, client: FileClient) -> None:
        def content(_: bytes): ...
        def get(_: datasets_models.File): ...
        def list(_: datasets_models.ListFilesResponse): ...
        def upload(_: datasets_models.File): ...

        self.content = core.with_streaming_response(content, client.content)
        self.get = core.with_streaming_response(get, client.get)
        self.list = core.with_streaming_response(list, client.list)
        self.upload = core.with_streaming_response(upload, client.upload)
