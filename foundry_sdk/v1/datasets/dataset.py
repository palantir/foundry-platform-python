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
from foundry_sdk.v1.core import errors as core_errors
from foundry_sdk.v1.core import models as core_models
from foundry_sdk.v1.datasets import errors as datasets_errors
from foundry_sdk.v1.datasets import models as datasets_models


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
        from foundry_sdk.v1.datasets.branch import BranchClient

        return BranchClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def File(self):
        from foundry_sdk.v1.datasets.file import FileClient

        return FileClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Transaction(self):
        from foundry_sdk.v1.datasets.transaction import TransactionClient

        return TransactionClient(
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
        parent_folder_rid: core_models.FolderRid,
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
        :raises FolderNotFound: The requested folder could not be found, or the client token does not have access to it.
        :raises InvalidBranchId: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        :raises TransactionNotCommitted: The given transaction has not been committed.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": datasets_models.DatasetName,
                        "parentFolderRid": core_models.FolderRid,
                    },
                ),
                response_type=datasets_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchAlreadyExists": datasets_errors.BranchAlreadyExists,
                    "CreateBranchPermissionDenied": datasets_errors.CreateBranchPermissionDenied,
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "FolderNotFound": core_errors.FolderNotFound,
                    "InvalidBranchId": datasets_errors.InvalidBranchId,
                    "ResourceNameAlreadyExists": core_errors.ResourceNameAlreadyExists,
                    "TransactionNotCommitted": datasets_errors.TransactionNotCommitted,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_id: typing.Optional[datasets_models.BranchId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Deletes the Schema from a Dataset and Branch.

        :param dataset_rid: The RID of the Dataset on which to delete the schema.
        :type dataset_rid: DatasetRid
        :param branch_id: The ID of the Branch on which to delete the schema.
        :type branch_id: Optional[BranchId]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param transaction_rid: The RID of the Transaction on which to delete the schema.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DeleteSchemaPermissionDenied: todo
        :raises InvalidBranchId: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DeleteSchemaPermissionDenied": datasets_errors.DeleteSchemaPermissionDenied,
                    "InvalidBranchId": datasets_errors.InvalidBranchId,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
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
        Gets the Dataset with the given DatasetRid.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.Dataset

        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_id: typing.Optional[datasets_models.BranchId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Optional[typing.Any]:
        """
        Retrieves the Schema for a Dataset and Branch, if it exists.

        :param dataset_rid: The RID of the Dataset.
        :type dataset_rid: DatasetRid
        :param branch_id: The ID of the Branch.
        :type branch_id: Optional[BranchId]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param transaction_rid: The TransactionRid that contains the Schema.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Optional[typing.Any]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises InvalidBranchId: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=typing.Optional[typing.Any],
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "InvalidBranchId": datasets_errors.InvalidBranchId,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        format: datasets_models.TableExportFormat,
        branch_id: typing.Optional[datasets_models.BranchId] = None,
        columns: typing.Optional[typing.List[str]] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        row_limit: typing.Optional[int] = None,
        start_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (Virtual datasets composed of other datasets).

        :param dataset_rid: The RID of the Dataset.
        :type dataset_rid: DatasetRid
        :param format: The export format. Must be `ARROW` or `CSV`.
        :type format: TableExportFormat
        :param branch_id: The identifier (name) of the Branch.
        :type branch_id: Optional[BranchId]
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
        :raises ReadTablePermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                throwable_errors={
                    "ColumnTypesNotSupported": datasets_errors.ColumnTypesNotSupported,
                    "DatasetReadNotSupported": datasets_errors.DatasetReadNotSupported,
                    "InvalidParameterCombination": core_errors.InvalidParameterCombination,
                    "ReadTablePermissionDenied": datasets_errors.ReadTablePermissionDenied,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        body: typing.Any,
        *,
        branch_id: typing.Optional[datasets_models.BranchId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> None:
        """
        Puts a Schema on an existing Dataset and Branch.

        :param dataset_rid: The RID of the Dataset on which to put the Schema.
        :type dataset_rid: DatasetRid
        :param body: Body of the request
        :type body: Any
        :param branch_id: The ID of the Branch on which to put the Schema.
        :type branch_id: Optional[BranchId]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: None

        :raises AbortTransactionPermissionDenied: The provided token does not have permission to abort the given transaction on the given dataset.
        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CommitTransactionPermissionDenied: The provided token does not have permission to commit the given transaction on the given dataset.
        :raises CreateTransactionPermissionDenied: The provided token does not have permission to create a transaction on this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FileNotFoundOnTransactionRange: The requested file could not be found on the given transaction range, or the client token does not have access to it.
        :raises InvalidBranchId: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises InvalidTransactionType: The given transaction type is not valid. Valid transaction types are `SNAPSHOT`, `UPDATE`, `APPEND`, and `DELETE`.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        :raises PutSchemaPermissionDenied: todo
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        :raises TransactionNotOpen: The given transaction is not open.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing.Any,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortTransactionPermissionDenied": datasets_errors.AbortTransactionPermissionDenied,
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CommitTransactionPermissionDenied": datasets_errors.CommitTransactionPermissionDenied,
                    "CreateTransactionPermissionDenied": datasets_errors.CreateTransactionPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "FileNotFoundOnTransactionRange": datasets_errors.FileNotFoundOnTransactionRange,
                    "InvalidBranchId": datasets_errors.InvalidBranchId,
                    "InvalidTransactionType": datasets_errors.InvalidTransactionType,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
                    "PutSchemaPermissionDenied": datasets_errors.PutSchemaPermissionDenied,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                    "TransactionNotOpen": datasets_errors.TransactionNotOpen,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _DatasetClientRaw:
    def __init__(self, client: DatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def delete_schema(_: None): ...
        def get(_: datasets_models.Dataset): ...
        def get_schema(_: typing.Optional[typing.Any]): ...
        def read(_: bytes): ...
        def replace_schema(_: None): ...

        self.create = core.with_raw_response(create, client.create)
        self.delete_schema = core.with_raw_response(delete_schema, client.delete_schema)
        self.get = core.with_raw_response(get, client.get)
        self.get_schema = core.with_raw_response(get_schema, client.get_schema)
        self.read = core.with_raw_response(read, client.read)
        self.replace_schema = core.with_raw_response(replace_schema, client.replace_schema)


class _DatasetClientStreaming:
    def __init__(self, client: DatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schema(_: typing.Optional[typing.Any]): ...
        def read(_: bytes): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.get_schema = core.with_streaming_response(get_schema, client.get_schema)
        self.read = core.with_streaming_response(read, client.read)


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
        from foundry_sdk.v1.datasets.branch import AsyncBranchClient

        return AsyncBranchClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def File(self):
        from foundry_sdk.v1.datasets.file import AsyncFileClient

        return AsyncFileClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Transaction(self):
        from foundry_sdk.v1.datasets.transaction import AsyncTransactionClient

        return AsyncTransactionClient(
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
        parent_folder_rid: core_models.FolderRid,
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
        :raises FolderNotFound: The requested folder could not be found, or the client token does not have access to it.
        :raises InvalidBranchId: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises ResourceNameAlreadyExists: The provided resource name is already in use by another resource in the same folder.
        :raises TransactionNotCommitted: The given transaction has not been committed.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": datasets_models.DatasetName,
                        "parentFolderRid": core_models.FolderRid,
                    },
                ),
                response_type=datasets_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchAlreadyExists": datasets_errors.BranchAlreadyExists,
                    "CreateBranchPermissionDenied": datasets_errors.CreateBranchPermissionDenied,
                    "CreateDatasetPermissionDenied": datasets_errors.CreateDatasetPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "FolderNotFound": core_errors.FolderNotFound,
                    "InvalidBranchId": datasets_errors.InvalidBranchId,
                    "ResourceNameAlreadyExists": core_errors.ResourceNameAlreadyExists,
                    "TransactionNotCommitted": datasets_errors.TransactionNotCommitted,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_id: typing.Optional[datasets_models.BranchId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Deletes the Schema from a Dataset and Branch.

        :param dataset_rid: The RID of the Dataset on which to delete the schema.
        :type dataset_rid: DatasetRid
        :param branch_id: The ID of the Branch on which to delete the schema.
        :type branch_id: Optional[BranchId]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param transaction_rid: The RID of the Transaction on which to delete the schema.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DeleteSchemaPermissionDenied: todo
        :raises InvalidBranchId: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DeleteSchemaPermissionDenied": datasets_errors.DeleteSchemaPermissionDenied,
                    "InvalidBranchId": datasets_errors.InvalidBranchId,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
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
        Gets the Dataset with the given DatasetRid.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.Dataset]

        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=datasets_models.Dataset,
                request_timeout=request_timeout,
                throwable_errors={
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_id: typing.Optional[datasets_models.BranchId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[typing.Optional[typing.Any]]:
        """
        Retrieves the Schema for a Dataset and Branch, if it exists.

        :param dataset_rid: The RID of the Dataset.
        :type dataset_rid: DatasetRid
        :param branch_id: The ID of the Branch.
        :type branch_id: Optional[BranchId]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param transaction_rid: The TransactionRid that contains the Schema.
        :type transaction_rid: Optional[TransactionRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[typing.Optional[typing.Any]]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises InvalidBranchId: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                response_type=typing.Optional[typing.Any],
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "InvalidBranchId": datasets_errors.InvalidBranchId,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def read(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        format: datasets_models.TableExportFormat,
        branch_id: typing.Optional[datasets_models.BranchId] = None,
        columns: typing.Optional[typing.List[str]] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        row_limit: typing.Optional[int] = None,
        start_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[bytes]:
        """
        Gets the content of a dataset as a table in the specified format.

        This endpoint currently does not support views (Virtual datasets composed of other datasets).

        :param dataset_rid: The RID of the Dataset.
        :type dataset_rid: DatasetRid
        :param format: The export format. Must be `ARROW` or `CSV`.
        :type format: TableExportFormat
        :param branch_id: The identifier (name) of the Branch.
        :type branch_id: Optional[BranchId]
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
        :raises ReadTablePermissionDenied: The provided token does not have permission to read the given dataset as a table.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                throwable_errors={
                    "ColumnTypesNotSupported": datasets_errors.ColumnTypesNotSupported,
                    "DatasetReadNotSupported": datasets_errors.DatasetReadNotSupported,
                    "InvalidParameterCombination": core_errors.InvalidParameterCombination,
                    "ReadTablePermissionDenied": datasets_errors.ReadTablePermissionDenied,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def replace_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        body: typing.Any,
        *,
        branch_id: typing.Optional[datasets_models.BranchId] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[None]:
        """
        Puts a Schema on an existing Dataset and Branch.

        :param dataset_rid: The RID of the Dataset on which to put the Schema.
        :type dataset_rid: DatasetRid
        :param body: Body of the request
        :type body: Any
        :param branch_id: The ID of the Branch on which to put the Schema.
        :type branch_id: Optional[BranchId]
        :param preview:
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[None]

        :raises AbortTransactionPermissionDenied: The provided token does not have permission to abort the given transaction on the given dataset.
        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises CommitTransactionPermissionDenied: The provided token does not have permission to commit the given transaction on the given dataset.
        :raises CreateTransactionPermissionDenied: The provided token does not have permission to create a transaction on this dataset.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises FileNotFoundOnTransactionRange: The requested file could not be found on the given transaction range, or the client token does not have access to it.
        :raises InvalidBranchId: The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs.
        :raises InvalidTransactionType: The given transaction type is not valid. Valid transaction types are `SNAPSHOT`, `UPDATE`, `APPEND`, and `DELETE`.
        :raises OpenTransactionAlreadyExists: A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time.
        :raises PutSchemaPermissionDenied: todo
        :raises TransactionNotFound: The requested transaction could not be found on the dataset, or the client token does not have access to it.
        :raises TransactionNotOpen: The given transaction is not open.
        """

        return self._api_client.call_api(
            core.RequestInfo(
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
                body_type=typing.Any,
                response_type=None,
                request_timeout=request_timeout,
                throwable_errors={
                    "AbortTransactionPermissionDenied": datasets_errors.AbortTransactionPermissionDenied,
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "CommitTransactionPermissionDenied": datasets_errors.CommitTransactionPermissionDenied,
                    "CreateTransactionPermissionDenied": datasets_errors.CreateTransactionPermissionDenied,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "FileNotFoundOnTransactionRange": datasets_errors.FileNotFoundOnTransactionRange,
                    "InvalidBranchId": datasets_errors.InvalidBranchId,
                    "InvalidTransactionType": datasets_errors.InvalidTransactionType,
                    "OpenTransactionAlreadyExists": datasets_errors.OpenTransactionAlreadyExists,
                    "PutSchemaPermissionDenied": datasets_errors.PutSchemaPermissionDenied,
                    "TransactionNotFound": datasets_errors.TransactionNotFound,
                    "TransactionNotOpen": datasets_errors.TransactionNotOpen,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _AsyncDatasetClientRaw:
    def __init__(self, client: AsyncDatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def delete_schema(_: None): ...
        def get(_: datasets_models.Dataset): ...
        def get_schema(_: typing.Optional[typing.Any]): ...
        def read(_: bytes): ...
        def replace_schema(_: None): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.delete_schema = core.async_with_raw_response(delete_schema, client.delete_schema)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_schema = core.async_with_raw_response(get_schema, client.get_schema)
        self.read = core.async_with_raw_response(read, client.read)
        self.replace_schema = core.async_with_raw_response(replace_schema, client.replace_schema)


class _AsyncDatasetClientStreaming:
    def __init__(self, client: AsyncDatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schema(_: typing.Optional[typing.Any]): ...
        def read(_: bytes): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_schema = core.async_with_streaming_response(get_schema, client.get_schema)
        self.read = core.async_with_streaming_response(read, client.read)
