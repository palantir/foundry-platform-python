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
    def get_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version_id: typing.Optional[core_models.VersionId] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.GetDatasetSchemaResponse:
        """
        Gets a dataset's schema. If no `endTransactionRid` is provided, the latest committed version will be used.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: Optional[BranchName]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction. If a user does not provide a value, the RID of the latest committed transaction will be used.
        :type end_transaction_rid: Optional[TransactionRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version_id: The schema version that should be used. If none is provided, the latest version will be used.
        :type version_id: Optional[VersionId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.GetDatasetSchemaResponse

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DatasetViewNotFound: The requested dataset view could not be found. A dataset view represents the effective file contents of a dataset  for a branch at a point in time, calculated from transactions (SNAPSHOT, APPEND, UPDATE, DELETE). The view may not  exist if the dataset has no transactions, contains no files, the branch is not valid, or the client token does not have access to it.
        :raises GetDatasetSchemaPermissionDenied: Could not getSchema the Dataset.
        :raises InvalidParameterCombination: The given parameters are individually valid but cannot be used in the given combination.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/getSchema",
                query_params={
                    "branchName": branch_name,
                    "endTransactionRid": end_transaction_rid,
                    "preview": preview,
                    "versionId": version_id,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.GetDatasetSchemaResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DatasetViewNotFound": datasets_errors.DatasetViewNotFound,
                    "GetDatasetSchemaPermissionDenied": datasets_errors.GetDatasetSchemaPermissionDenied,
                    "InvalidParameterCombination": core_errors.InvalidParameterCombination,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def jobs(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        order_by: typing.List[datasets_models.GetDatasetJobsSort],
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[datasets_models.GetDatasetJobsQuery] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.GetJobResponse:
        """
        Get the RIDs of the Jobs for the given dataset. By default, returned Jobs are sorted in descending order by the Job start time.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param order_by:
        :type order_by: List[GetDatasetJobsSort]
        :param branch_name: The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.
        :type branch_name: Optional[BranchName]
        :param page_size: Max number of results to return. A limit of 1000 on if no limit is supplied in the search request
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[GetDatasetJobsQuery]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.GetJobResponse

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises GetDatasetJobsPermissionDenied: Could not jobs the Dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/jobs",
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
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "orderBy": order_by,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Optional[datasets_models.GetDatasetJobsQuery],
                        "orderBy": typing.List[datasets_models.GetDatasetJobsSort],
                    },
                ),
                response_type=datasets_models.GetJobResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "GetDatasetJobsPermissionDenied": datasets_errors.GetDatasetJobsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def put_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        schema: core_models.DatasetSchema,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        dataframe_reader: typing.Optional[datasets_models.DataframeReader] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> datasets_models.GetDatasetSchemaResponse:
        """
        Adds a schema on an existing dataset using a PUT request.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param schema: The schema that will be added.
        :type schema: DatasetSchema
        :param branch_name:
        :type branch_name: Optional[BranchName]
        :param dataframe_reader: The dataframe reader used for reading the dataset schema. Defaults to PARQUET.
        :type dataframe_reader: Optional[DataframeReader]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: datasets_models.GetDatasetSchemaResponse

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DatasetViewNotFound: The requested dataset view could not be found. A dataset view represents the effective file contents of a dataset  for a branch at a point in time, calculated from transactions (SNAPSHOT, APPEND, UPDATE, DELETE). The view may not  exist if the dataset has no transactions, contains no files, the branch is not valid, or the client token does not have access to it.
        :raises InvalidSchema: The schema failed validations
        :raises PutDatasetSchemaPermissionDenied: Could not putSchema the Dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/datasets/{datasetRid}/putSchema",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branchName": branch_name,
                    "dataframeReader": dataframe_reader,
                    "endTransactionRid": end_transaction_rid,
                    "schema": schema,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "dataframeReader": typing.Optional[datasets_models.DataframeReader],
                        "endTransactionRid": typing.Optional[datasets_models.TransactionRid],
                        "schema": core_models.DatasetSchema,
                    },
                ),
                response_type=datasets_models.GetDatasetSchemaResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DatasetViewNotFound": datasets_errors.DatasetViewNotFound,
                    "InvalidSchema": core_errors.InvalidSchema,
                    "PutDatasetSchemaPermissionDenied": datasets_errors.PutDatasetSchemaPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def transactions(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.ResourceIterator[datasets_models.Transaction]:
        """
        Get the Transaction history for the given Dataset

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.ResourceIterator[datasets_models.Transaction]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions",
                query_params={
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
                response_type=datasets_models.ListTransactionsOfDatasetResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _DatasetClientRaw:
    def __init__(self, client: DatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schedules(_: datasets_models.ListSchedulesResponse): ...
        def get_schema(_: datasets_models.GetDatasetSchemaResponse): ...
        def jobs(_: datasets_models.GetJobResponse): ...
        def put_schema(_: datasets_models.GetDatasetSchemaResponse): ...
        def read_table(_: bytes): ...
        def transactions(_: datasets_models.ListTransactionsOfDatasetResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.get_schedules = core.with_raw_response(get_schedules, client.get_schedules)
        self.get_schema = core.with_raw_response(get_schema, client.get_schema)
        self.jobs = core.with_raw_response(jobs, client.jobs)
        self.put_schema = core.with_raw_response(put_schema, client.put_schema)
        self.read_table = core.with_raw_response(read_table, client.read_table)
        self.transactions = core.with_raw_response(transactions, client.transactions)


class _DatasetClientStreaming:
    def __init__(self, client: DatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schedules(_: datasets_models.ListSchedulesResponse): ...
        def get_schema(_: datasets_models.GetDatasetSchemaResponse): ...
        def jobs(_: datasets_models.GetJobResponse): ...
        def put_schema(_: datasets_models.GetDatasetSchemaResponse): ...
        def read_table(_: bytes): ...
        def transactions(_: datasets_models.ListTransactionsOfDatasetResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.get_schedules = core.with_streaming_response(get_schedules, client.get_schedules)
        self.get_schema = core.with_streaming_response(get_schema, client.get_schema)
        self.jobs = core.with_streaming_response(jobs, client.jobs)
        self.put_schema = core.with_streaming_response(put_schema, client.put_schema)
        self.read_table = core.with_streaming_response(read_table, client.read_table)
        self.transactions = core.with_streaming_response(transactions, client.transactions)


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
    def get_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        version_id: typing.Optional[core_models.VersionId] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.GetDatasetSchemaResponse]:
        """
        Gets a dataset's schema. If no `endTransactionRid` is provided, the latest committed version will be used.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param branch_name:
        :type branch_name: Optional[BranchName]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction. If a user does not provide a value, the RID of the latest committed transaction will be used.
        :type end_transaction_rid: Optional[TransactionRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param version_id: The schema version that should be used. If none is provided, the latest version will be used.
        :type version_id: Optional[VersionId]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.GetDatasetSchemaResponse]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DatasetViewNotFound: The requested dataset view could not be found. A dataset view represents the effective file contents of a dataset  for a branch at a point in time, calculated from transactions (SNAPSHOT, APPEND, UPDATE, DELETE). The view may not  exist if the dataset has no transactions, contains no files, the branch is not valid, or the client token does not have access to it.
        :raises GetDatasetSchemaPermissionDenied: Could not getSchema the Dataset.
        :raises InvalidParameterCombination: The given parameters are individually valid but cannot be used in the given combination.
        :raises SchemaNotFound: A schema could not be found for the given dataset and branch, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/getSchema",
                query_params={
                    "branchName": branch_name,
                    "endTransactionRid": end_transaction_rid,
                    "preview": preview,
                    "versionId": version_id,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=datasets_models.GetDatasetSchemaResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DatasetViewNotFound": datasets_errors.DatasetViewNotFound,
                    "GetDatasetSchemaPermissionDenied": datasets_errors.GetDatasetSchemaPermissionDenied,
                    "InvalidParameterCombination": core_errors.InvalidParameterCombination,
                    "SchemaNotFound": datasets_errors.SchemaNotFound,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def jobs(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        order_by: typing.List[datasets_models.GetDatasetJobsSort],
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        where: typing.Optional[datasets_models.GetDatasetJobsQuery] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.GetJobResponse]:
        """
        Get the RIDs of the Jobs for the given dataset. By default, returned Jobs are sorted in descending order by the Job start time.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param order_by:
        :type order_by: List[GetDatasetJobsSort]
        :param branch_name: The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used.
        :type branch_name: Optional[BranchName]
        :param page_size: Max number of results to return. A limit of 1000 on if no limit is supplied in the search request
        :type page_size: Optional[PageSize]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param where:
        :type where: Optional[GetDatasetJobsQuery]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.GetJobResponse]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises GetDatasetJobsPermissionDenied: Could not jobs the Dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/v2/datasets/{datasetRid}/jobs",
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
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "where": where,
                    "orderBy": order_by,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "where": typing.Optional[datasets_models.GetDatasetJobsQuery],
                        "orderBy": typing.List[datasets_models.GetDatasetJobsSort],
                    },
                ),
                response_type=datasets_models.GetJobResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "GetDatasetJobsPermissionDenied": datasets_errors.GetDatasetJobsPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def put_schema(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        schema: core_models.DatasetSchema,
        branch_name: typing.Optional[datasets_models.BranchName] = None,
        dataframe_reader: typing.Optional[datasets_models.DataframeReader] = None,
        end_transaction_rid: typing.Optional[datasets_models.TransactionRid] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> typing.Awaitable[datasets_models.GetDatasetSchemaResponse]:
        """
        Adds a schema on an existing dataset using a PUT request.

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param schema: The schema that will be added.
        :type schema: DatasetSchema
        :param branch_name:
        :type branch_name: Optional[BranchName]
        :param dataframe_reader: The dataframe reader used for reading the dataset schema. Defaults to PARQUET.
        :type dataframe_reader: Optional[DataframeReader]
        :param end_transaction_rid: The Resource Identifier (RID) of the end Transaction.
        :type end_transaction_rid: Optional[TransactionRid]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: typing.Awaitable[datasets_models.GetDatasetSchemaResponse]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        :raises DatasetViewNotFound: The requested dataset view could not be found. A dataset view represents the effective file contents of a dataset  for a branch at a point in time, calculated from transactions (SNAPSHOT, APPEND, UPDATE, DELETE). The view may not  exist if the dataset has no transactions, contains no files, the branch is not valid, or the client token does not have access to it.
        :raises InvalidSchema: The schema failed validations
        :raises PutDatasetSchemaPermissionDenied: Could not putSchema the Dataset.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/v2/datasets/{datasetRid}/putSchema",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "datasetRid": dataset_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "branchName": branch_name,
                    "dataframeReader": dataframe_reader,
                    "endTransactionRid": end_transaction_rid,
                    "schema": schema,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "branchName": typing.Optional[datasets_models.BranchName],
                        "dataframeReader": typing.Optional[datasets_models.DataframeReader],
                        "endTransactionRid": typing.Optional[datasets_models.TransactionRid],
                        "schema": core_models.DatasetSchema,
                    },
                ),
                response_type=datasets_models.GetDatasetSchemaResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                    "DatasetViewNotFound": datasets_errors.DatasetViewNotFound,
                    "InvalidSchema": core_errors.InvalidSchema,
                    "PutDatasetSchemaPermissionDenied": datasets_errors.PutDatasetSchemaPermissionDenied,
                },
                response_mode=_sdk_internal.get("response_mode"),
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

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def transactions(
        self,
        dataset_rid: datasets_models.DatasetRid,
        *,
        page_size: typing.Optional[core_models.PageSize] = None,
        page_token: typing.Optional[core_models.PageToken] = None,
        preview: typing.Optional[core_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> core.AsyncResourceIterator[datasets_models.Transaction]:
        """
        Get the Transaction history for the given Dataset

        :param dataset_rid:
        :type dataset_rid: DatasetRid
        :param page_size: The page size to use for the endpoint.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request.
        :type page_token: Optional[PageToken]
        :param preview: Enables the use of preview functionality.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: core.AsyncResourceIterator[datasets_models.Transaction]

        :raises BranchNotFound: The requested branch could not be found, or the client token does not have access to it.
        :raises DatasetNotFound: The requested dataset could not be found, or the client token does not have access to it.
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/v2/datasets/{datasetRid}/transactions",
                query_params={
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
                response_type=datasets_models.ListTransactionsOfDatasetResponse,
                request_timeout=request_timeout,
                throwable_errors={
                    "BranchNotFound": datasets_errors.BranchNotFound,
                    "DatasetNotFound": datasets_errors.DatasetNotFound,
                },
                response_mode=_sdk_internal.get("response_mode", "ITERATOR"),
            ),
        )


class _AsyncDatasetClientRaw:
    def __init__(self, client: AsyncDatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schedules(_: datasets_models.ListSchedulesResponse): ...
        def get_schema(_: datasets_models.GetDatasetSchemaResponse): ...
        def jobs(_: datasets_models.GetJobResponse): ...
        def put_schema(_: datasets_models.GetDatasetSchemaResponse): ...
        def read_table(_: bytes): ...
        def transactions(_: datasets_models.ListTransactionsOfDatasetResponse): ...

        self.create = core.async_with_raw_response(create, client.create)
        self.get = core.async_with_raw_response(get, client.get)
        self.get_schedules = core.async_with_raw_response(get_schedules, client.get_schedules)
        self.get_schema = core.async_with_raw_response(get_schema, client.get_schema)
        self.jobs = core.async_with_raw_response(jobs, client.jobs)
        self.put_schema = core.async_with_raw_response(put_schema, client.put_schema)
        self.read_table = core.async_with_raw_response(read_table, client.read_table)
        self.transactions = core.async_with_raw_response(transactions, client.transactions)


class _AsyncDatasetClientStreaming:
    def __init__(self, client: AsyncDatasetClient) -> None:
        def create(_: datasets_models.Dataset): ...
        def get(_: datasets_models.Dataset): ...
        def get_schedules(_: datasets_models.ListSchedulesResponse): ...
        def get_schema(_: datasets_models.GetDatasetSchemaResponse): ...
        def jobs(_: datasets_models.GetJobResponse): ...
        def put_schema(_: datasets_models.GetDatasetSchemaResponse): ...
        def read_table(_: bytes): ...
        def transactions(_: datasets_models.ListTransactionsOfDatasetResponse): ...

        self.create = core.async_with_streaming_response(create, client.create)
        self.get = core.async_with_streaming_response(get, client.get)
        self.get_schedules = core.async_with_streaming_response(get_schedules, client.get_schedules)
        self.get_schema = core.async_with_streaming_response(get_schema, client.get_schema)
        self.jobs = core.async_with_streaming_response(jobs, client.jobs)
        self.put_schema = core.async_with_streaming_response(put_schema, client.put_schema)
        self.read_table = core.async_with_streaming_response(read_table, client.read_table)
        self.transactions = core.async_with_streaming_response(transactions, client.transactions)
