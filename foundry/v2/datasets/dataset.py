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

import warnings
from functools import cached_property
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

import pydantic
from typing_extensions import Annotated
from typing_extensions import TypedDict
from typing_extensions import deprecated
from typing_extensions import overload

from foundry._core import ApiClient
from foundry._core import ApiResponse
from foundry._core import Auth
from foundry._core import BinaryStream
from foundry._core import Config
from foundry._core import RequestInfo
from foundry._core import StreamingContextManager
from foundry._core.utils import maybe_ignore_preview
from foundry._errors import handle_unexpected
from foundry.v2.datasets import errors as datasets_errors
from foundry.v2.datasets.models._branch_name import BranchName
from foundry.v2.datasets.models._dataset import Dataset
from foundry.v2.datasets.models._dataset_name import DatasetName
from foundry.v2.datasets.models._dataset_rid import DatasetRid
from foundry.v2.datasets.models._table_export_format import TableExportFormat
from foundry.v2.datasets.models._transaction_rid import TransactionRid
from foundry.v2.filesystem import errors as filesystem_errors
from foundry.v2.filesystem.models._folder_rid import FolderRid


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

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def create(
        self,
        *,
        name: DatasetName,
        parent_folder_rid: FolderRid,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset

        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "name": DatasetName,
                    },
                ),
                response_type=Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                },
            ),
        ).decode()

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Dataset:
        """
        Get the Dataset with the specified rid.
        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Dataset

        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        ).decode()

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read_table(
        self,
        dataset_rid: DatasetRid,
        *,
        stream: Literal[True],
        format: TableExportFormat,
        branch_name: Optional[BranchName] = None,
        columns: Optional[List[str]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        row_limit: Optional[int] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> BinaryStream:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (virtual datasets composed of other datasets).

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param format: format
        :type format: TableExportFormat
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param columns: columns
        :type columns: Optional[List[str]]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param row_limit: rowLimit
        :type row_limit: Optional[int]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: BinaryStream

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """
        ...

    @overload
    def read_table(
        self,
        dataset_rid: DatasetRid,
        *,
        format: TableExportFormat,
        branch_name: Optional[BranchName] = None,
        columns: Optional[List[str]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        row_limit: Optional[int] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        stream: Literal[False] = False,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> bytes:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (virtual datasets composed of other datasets).

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param format: format
        :type format: TableExportFormat
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param columns: columns
        :type columns: Optional[List[str]]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param row_limit: rowLimit
        :type row_limit: Optional[int]
        :param start_transaction_rid: startTransactionRid
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

    @overload
    @deprecated(
        "Using the `stream` parameter is deprecated. Please use the `with_streaming_response` instead."
    )
    def read_table(
        self,
        dataset_rid: DatasetRid,
        *,
        stream: bool,
        format: TableExportFormat,
        branch_name: Optional[BranchName] = None,
        columns: Optional[List[str]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        row_limit: Optional[int] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (virtual datasets composed of other datasets).

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param format: format
        :type format: TableExportFormat
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param columns: columns
        :type columns: Optional[List[str]]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param row_limit: rowLimit
        :type row_limit: Optional[int]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """
        ...

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def read_table(
        self,
        dataset_rid: DatasetRid,
        *,
        format: TableExportFormat,
        branch_name: Optional[BranchName] = None,
        columns: Optional[List[str]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        row_limit: Optional[int] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        stream: bool = False,
        chunk_size: Optional[int] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> Union[bytes, BinaryStream]:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (virtual datasets composed of other datasets).

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param format: format
        :type format: TableExportFormat
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param columns: columns
        :type columns: Optional[List[str]]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param row_limit: rowLimit
        :type row_limit: Optional[int]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param stream: Whether to stream back the binary data in an iterator. This avoids reading the entire content of the response into memory at once.
        :type stream: bool
        :param chunk_size: The number of bytes that should be read into memory for each chunk. If set to None, the data will become available as it arrives in whatever size is sent from the host.
        :type chunk_size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: Union[bytes, BinaryStream]

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
            RequestInfo(
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
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Dataset]:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Dataset]

        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "name": DatasetName,
                    },
                ),
                response_type=Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[Dataset]:
        """
        Get the Dataset with the specified rid.
        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[Dataset]

        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.call_api(
            RequestInfo(
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
                response_type=Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def read_table(
        self,
        dataset_rid: DatasetRid,
        *,
        format: TableExportFormat,
        branch_name: Optional[BranchName] = None,
        columns: Optional[List[str]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        row_limit: Optional[int] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> ApiResponse[bytes]:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (virtual datasets composed of other datasets).

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param format: format
        :type format: TableExportFormat
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param columns: columns
        :type columns: Optional[List[str]]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param row_limit: rowLimit
        :type row_limit: Optional[int]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: ApiResponse[bytes]

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
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
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Dataset]:
        """
        Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

        :param name:
        :type name: DatasetName
        :param parent_folder_rid:
        :type parent_folder_rid: FolderRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Dataset]

        :raises CreateDatasetPermissionDenied: The provided token does not have permission to create a dataset in this folder.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                body_type=TypedDict(
                    "Body",
                    {  # type: ignore
                        "parentFolderRid": FolderRid,
                        "name": DatasetName,
                    },
                ),
                response_type=Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def get(
        self,
        dataset_rid: DatasetRid,
        *,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[Dataset]:
        """
        Get the Dataset with the specified rid.
        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[Dataset]

        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
                response_type=Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "ResourceNameAlreadyExists": filesystem_errors.ResourceNameAlreadyExists,
                },
            ),
        )

    @maybe_ignore_preview
    @pydantic.validate_call
    @handle_unexpected
    def read_table(
        self,
        dataset_rid: DatasetRid,
        *,
        format: TableExportFormat,
        branch_name: Optional[BranchName] = None,
        columns: Optional[List[str]] = None,
        end_transaction_rid: Optional[TransactionRid] = None,
        row_limit: Optional[int] = None,
        start_transaction_rid: Optional[TransactionRid] = None,
        request_timeout: Optional[Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]] = None,
    ) -> StreamingContextManager[bytes]:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (virtual datasets composed of other datasets).

        :param dataset_rid: datasetRid
        :type dataset_rid: DatasetRid
        :param format: format
        :type format: TableExportFormat
        :param branch_name: branchName
        :type branch_name: Optional[BranchName]
        :param columns: columns
        :type columns: Optional[List[str]]
        :param end_transaction_rid: endTransactionRid
        :type end_transaction_rid: Optional[TransactionRid]
        :param row_limit: rowLimit
        :type row_limit: Optional[int]
        :param start_transaction_rid: startTransactionRid
        :type start_transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: StreamingContextManager[bytes]

        :raises ColumnTypesNotSupported: The dataset contains column types that are not supported.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableDatasetPermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises ReadTableError: An error occurred while reading the table. Refer to the message for more details.
        :raises ReadTableRowLimitExceeded: The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit.
        :raises ReadTableTimeout: The request to read the table timed out.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """

        return self._api_client.stream_api(
            RequestInfo(
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
