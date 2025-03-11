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
import warnings
from functools import cached_property

import pydantic
import typing_extensions

from foundry import _core as core
from foundry import _errors as errors
from foundry.v2.datasets import errors as datasets_errors
from foundry.v2.datasets import models as datasets_models
from foundry.v2.filesystem import errors as filesystem_errors
from foundry.v2.filesystem import models as filesystem_models


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
    def Branch(self):
        from foundry.v2.datasets.branch import BranchClient

        return BranchClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Transaction(self):
        from foundry.v2.datasets.transaction import TransactionClient

        return TransactionClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def File(self):
        from foundry.v2.datasets.file import FileClient

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

        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
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
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                },
            ),
        ).decode()

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        request_timeout: typing.Optional[core.Timeout] = None,
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
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        ).decode()

    @typing_extensions.overload
    @typing_extensions.deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read_table(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        stream: typing.Literal[True],
        format: datasets_models.TableExportFormat,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        columns: typing.Optional[typing.List[str]] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        row_limit: typing.Optional[int] = None,
        start_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.BinaryStream:
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
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.BinaryStream

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """
        ...

    @typing_extensions.overload
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
        stream: typing.Literal[False] = False,
        request_timeout: typing.Optional[core.Timeout] = None,
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
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """
        ...

    @typing_extensions.overload
    @typing_extensions.deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read_table(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        stream: bool,
        format: datasets_models.TableExportFormat,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        columns: typing.Optional[typing.List[str]] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        row_limit: typing.Optional[int] = None,
        start_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
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
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Union[bytes, core.BinaryStream]

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """
        ...

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
        stream: bool = False,
        chunk_size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> typing.Union[bytes, core.BinaryStream]:
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
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Union[bytes, core.BinaryStream]

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """

        if stream:
            warnings.warn(
                f"client.datasets.Dataset.read_table(..., stream=True, chunk_size={chunk_size}) is deprecated. Please use:\n\nwith client.datasets.Dataset.with_streaming_response.read_table(...) as response:\n    response.iter_bytes(chunk_size={chunk_size})\n",
                DeprecationWarning,
                stacklevel=2,
            )

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
                stream=stream,
                chunk_size=chunk_size,
                request_timeout=request_timeout,
                throwable_errors={
                    "ColumnTypesNotSupported": datasets_errors.ColumnTypesNotSupported,
                    "ReadTableDatasetPermissionDenied": datasets_errors.ReadTableDatasetPermissionDenied,
                    "ReadTableDatasetPermissionDenied": datasets_errors.ReadTableDatasetPermissionDenied,
                    "ReadTableError": datasets_errors.ReadTableError,
                    "ReadTableRowLimitExceeded": datasets_errors.ReadTableRowLimitExceeded,
                    "ReadTableTimeout": datasets_errors.ReadTableTimeout,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.ApiResponse[datasets_models.Dataset]:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.Dataset]

        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
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
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                },
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
    ) -> core.ApiResponse[datasets_models.Dataset]:
        """
        Get the Dataset with the specified rid.
        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ApiResponse[datasets_models.Dataset]

        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
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
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
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
    ) -> core.ApiResponse[bytes]:
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
        :rtype: core.ApiResponse[bytes]

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
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
                    "ReadTableDatasetPermissionDenied": datasets_errors.ReadTableDatasetPermissionDenied,
                    "ReadTableDatasetPermissionDenied": datasets_errors.ReadTableDatasetPermissionDenied,
                    "ReadTableError": datasets_errors.ReadTableError,
                    "ReadTableRowLimitExceeded": datasets_errors.ReadTableRowLimitExceeded,
                    "ReadTableTimeout": datasets_errors.ReadTableTimeout,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
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
        request_timeout: typing.Optional[core.Timeout] = None,
    ) -> core.StreamingContextManager[datasets_models.Dataset]:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.Dataset]

        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
        """

        return self._api_client.stream_api(
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
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                },
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
    ) -> core.StreamingContextManager[datasets_models.Dataset]:
        """
        Get the Dataset with the specified rid.
        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.StreamingContextManager[datasets_models.Dataset]

        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.stream_api(
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
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
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
    ) -> core.StreamingContextManager[bytes]:
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
        :rtype: core.StreamingContextManager[bytes]

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """

        return self._api_client.stream_api(
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
                    "ReadTableDatasetPermissionDenied": datasets_errors.ReadTableDatasetPermissionDenied,
                    "ReadTableDatasetPermissionDenied": datasets_errors.ReadTableDatasetPermissionDenied,
                    "ReadTableError": datasets_errors.ReadTableError,
                    "ReadTableRowLimitExceeded": datasets_errors.ReadTableRowLimitExceeded,
                    "ReadTableTimeout": datasets_errors.ReadTableTimeout,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
                },
            ),
        )
