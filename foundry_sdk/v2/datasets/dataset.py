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

from foundry_sdk import _core as core
from foundry_sdk import _errors as errors
from foundry_sdk.v2.core import errors as core_errors
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.datasets import errors as datasets_errors
from foundry_sdk.v2.datasets import models as datasets_models
from foundry_sdk.v2.filesystem import errors as filesystem_errors
from foundry_sdk.v2.filesystem import models as filesystem_models


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

        self.with_streaming_response = _DatasetClientStreaming(self)
        self.with_raw_response = _DatasetClientRaw(self)

    @cached_property
    def Branch(self):
        from foundry_sdk.v2.datasets.branch import BranchClient

        return BranchClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Transaction(self):
        from foundry_sdk.v2.datasets.transaction import TransactionClient

        return TransactionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def File(self):
        from foundry_sdk.v2.datasets.file import FileClient

        return FileClient(
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
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.Dataset:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Dataset

        :raises BranchAlreadyExists: The branch cannot be created because a branch with that name already exists.
        :raises CreateBranchPermissionDenied: The provided token does not have permission to create a branch of this dataset.
        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FolderNotFound: The given Folder could not be found.
        :raises InvalidBranchName: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        :raises TransactionNotCommitted: The given transaction has not been committed.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "name": name,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": filesystem_models.FolderRid,
                        "name": datasets_models.DatasetName,
                    },
                ),
                response_type=datasets_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchAlreadyExists": datasets_errors.BranchAlreadyExists,
                    "CreateBranchPermissionDenied": datasets_errors.CreateBranchPermissionDenied,
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                    "InvalidBranchName": datasets_errors.InvalidBranchName,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                    "TransactionNotCommitted": datasets_errors.TransactionNotCommitted,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
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
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.Dataset:
        """
        Get the Dataset with the specified rid.
        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Dataset

        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_schedules(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[core_models.ScheduleRid]:
        """
        Get the RIDs of the Schedules that target the given Dataset

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name: The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.
        :type branch_name: Optional[BranchName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[core_models.ScheduleRid]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises GetDatasetSchedulesPermissionDenied: Could not getSchedules the Dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/getSchedules",
                query_params={
                    "branchName": branch_name,
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=datasets_models.ListSchedulesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "GetDatasetSchedulesPermissionDenied": datasets_errors.GetDatasetSchedulesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read_table(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        format: datasets_models.TableExportFormat,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        columns: typing.Optional[typing.List[str]] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        row_limit: typing.Optional[int] = None,
        start_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (virtual datasets composed of other datasets).

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param format: The export format. Must be `ARROW` or `CSV`.
        :type format: TableExportFormat
        :param branch_name: The name of the Branch.
        :type branch_name: Optional[BranchName]
        :param columns: A subset of the dataset columns to include in the result. Defaults to all columns.
        :type columns: Optional[List[str]]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param row_limit: A limit on the number of rows to return. Note that row ordering is non-deterministic.
        :type row_limit: Optional[int]
        :param start_transaction_rid: The Resource Identifier (RID) of the start Transaction.
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises DatasetReadNotSupported: The dataset does not support being read.
        :raises InvalidParameterCombination: The given parameters are individually valid but cannot be used in the given combination.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/readTable",
                query_params={
                    "format": format,
                    "branchName": branch_name,
                    "columns": columns,
                    "endTransactionRid": end_transaction_rid,
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
                throwable_errors={
                    "ColumnTypesNotSupported": datasets_errors.ColumnTypesNotSupported,
                    "DatasetReadNotSupported": datasets_errors.DatasetReadNotSupported,
                    "InvalidParameterCombination": core_errors.InvalidParameterCombination,
                    "ReadTableDatasetPermissionDenied": datasets_errors.ReadTableDatasetPermissionDenied,
                    "ReadTableError": datasets_errors.ReadTableError,
                    "ReadTableRowLimitExceeded": datasets_errors.ReadTableRowLimitExceeded,
                    "ReadTableTimeout": datasets_errors.ReadTableTimeout,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _DatasetClientRaw:
    def __init__(self, client: DatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schedules(_: datasets_models.ListSchedulesResponse): ...
        def read_table(_: bytes): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.get_schedules = core.with_raw_response(get_schedules, client.get_schedules)
        self.read_table = core.with_raw_response(read_table, client.read_table)


class _DatasetClientStreaming:
    def __init__(self, client: DatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schedules(_: datasets_models.ListSchedulesResponse): ...
        def read_table(_: bytes): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.get_schedules = core.with_streaming_response(get_schedules, client.get_schedules)
        self.read_table = core.with_streaming_response(read_table, client.read_table)


class AsyncDatasetClient:
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
        self._api_client = core.AsyncApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _AsyncDatasetClientStreaming(self)
        self.with_raw_response = _AsyncDatasetClientRaw(self)

    @cached_property
    def Branch(self):
        from foundry_sdk.v2.datasets.branch import AsyncBranchClient

        return AsyncBranchClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Transaction(self):
        from foundry_sdk.v2.datasets.transaction import AsyncTransactionClient

        return AsyncTransactionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def File(self):
        from foundry_sdk.v2.datasets.file import AsyncFileClient

        return AsyncFileClient(
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
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.Dataset]:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.Dataset]

        :raises BranchAlreadyExists: The branch cannot be created because a branch with that name already exists.
        :raises CreateBranchPermissionDenied: The provided token does not have permission to create a branch of this dataset.
        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FolderNotFound: The given Folder could not be found.
        :raises InvalidBranchName: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        :raises TransactionNotCommitted: The given transaction has not been committed.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets",
                query_params={},
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "parentFolderRid": parent_folder_rid,
                    "name": name,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": filesystem_models.FolderRid,
                        "name": datasets_models.DatasetName,
                    },
                ),
                response_type=datasets_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchAlreadyExists": datasets_errors.BranchAlreadyExists,
                    "CreateBranchPermissionDenied": datasets_errors.CreateBranchPermissionDenied,
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "FolderNotFound": filesystem_errors.FolderNotFound,
                    "InvalidBranchName": datasets_errors.InvalidBranchName,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                    "TransactionNotCommitted": datasets_errors.TransactionNotCommitted,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
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
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.Dataset]:
        """
        Get the Dataset with the specified rid.
        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.Dataset]

        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}",
                query_params={},
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_schedules(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[core_models.ScheduleRid]:
        """
        Get the RIDs of the Schedules that target the given Dataset

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name: The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.
        :type branch_name: Optional[BranchName]
        :param page_size:
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[core_models.ScheduleRid]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises GetDatasetSchedulesPermissionDenied: Could not getSchedules the Dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/getSchedules",
                query_params={
                    "branchName": branch_name,
                    "pageSize": page_size,
                    "pageToken": page_token,
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
                response_type=datasets_models.ListSchedulesResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "GetDatasetSchedulesPermissionDenied": datasets_errors.GetDatasetSchedulesPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read_table(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        format: datasets_models.TableExportFormat,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        columns: typing.Optional[typing.List[str]] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        row_limit: typing.Optional[int] = None,
        start_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (virtual datasets composed of other datasets).

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param format: The export format. Must be `ARROW` or `CSV`.
        :type format: TableExportFormat
        :param branch_name: The name of the Branch.
        :type branch_name: Optional[BranchName]
        :param columns: A subset of the dataset columns to include in the result. Defaults to all columns.
        :type columns: Optional[List[str]]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param row_limit: A limit on the number of rows to return. Note that row ordering is non-deterministic.
        :type row_limit: Optional[int]
        :param start_transaction_rid: The Resource Identifier (RID) of the start Transaction.
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[bytes]

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises DatasetReadNotSupported: The dataset does not support being read.
        :raises InvalidParameterCombination: The given parameters are individually valid but cannot be used in the given combination.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/readTable",
                query_params={
                    "format": format,
                    "branchName": branch_name,
                    "columns": columns,
                    "endTransactionRid": end_transaction_rid,
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
                throwable_errors={
                    "ColumnTypesNotSupported": datasets_errors.ColumnTypesNotSupported,
                    "DatasetReadNotSupported": datasets_errors.DatasetReadNotSupported,
                    "InvalidParameterCombination": core_errors.InvalidParameterCombination,
                    "ReadTableDatasetPermissionDenied": datasets_errors.ReadTableDatasetPermissionDenied,
                    "ReadTableError": datasets_errors.ReadTableError,
                    "ReadTableRowLimitExceeded": datasets_errors.ReadTableRowLimitExceeded,
                    "ReadTableTimeout": datasets_errors.ReadTableTimeout,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncDatasetClientRaw:
    def __init__(self, client: AsyncDatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schedules(_: datasets_models.ListSchedulesResponse): ...
        def read_table(_: bytes): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_schedules = core.async_with_raw_response(get_schedules, client.get_schedules)
        self.read_table = core.async_with_raw_response(read_table, client.read_table)


class _AsyncDatasetClientStreaming:
    def __init__(self, client: AsyncDatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schedules(_: datasets_models.ListSchedulesResponse): ...
        def read_table(_: bytes): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_schedules = core.async_with_streaming_response(get_schedules, client.get_schedules)
        self.read_table = core.async_with_streaming_response(read_table, client.read_table)
