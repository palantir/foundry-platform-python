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

import typing

import pydantic
import typing_extensions

from foundry_sdk import _core as core
from foundry_sdk.v2.core import models as core_models
from foundry_sdk.v2.filesystem import models as filesystem_models


class Branch(core.ModelBase):
    """Branch"""

    name: BranchName
    transaction_rid: typing.Optional[TransactionRid] = pydantic.Field(alias=str("transactionRid"), default=None)  # type: ignore[literal-required]
    """The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction."""


BranchName = str
"""The name of a Branch."""


DataframeReader = typing.Literal["AVRO", "CSV", "PARQUET", "DATASOURCE"]
"""The dataframe reader used for reading the dataset schema."""


class Dataset(core.ModelBase):
    """Dataset"""

    rid: DatasetRid
    name: DatasetName
    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]


DatasetName = str
"""DatasetName"""


DatasetRid = core.RID
"""The Resource Identifier (RID) of a Dataset."""


class File(core.ModelBase):
    """File"""

    path: core_models.FilePath
    transaction_rid: TransactionRid = pydantic.Field(alias=str("transactionRid"))  # type: ignore[literal-required]
    size_bytes: typing.Optional[core.Long] = pydantic.Field(alias=str("sizeBytes"), default=None)  # type: ignore[literal-required]
    updated_time: FileUpdatedTime = pydantic.Field(alias=str("updatedTime"))  # type: ignore[literal-required]


FileUpdatedTime = core.AwareDatetime
"""FileUpdatedTime"""


class GetDatasetJobsAndFilter(core.ModelBase):
    """GetDatasetJobsAndFilter"""

    items: typing.List[GetDatasetJobsQuery]
    type: typing.Literal["and"] = "and"


GetDatasetJobsComparisonType = typing.Literal["GTE", "LT"]
"""GetDatasetJobsComparisonType"""


class GetDatasetJobsOrFilter(core.ModelBase):
    """GetDatasetJobsOrFilter"""

    items: typing.List[GetDatasetJobsQuery]
    type: typing.Literal["or"] = "or"


GetDatasetJobsQuery = typing_extensions.Annotated[
    typing.Union[GetDatasetJobsOrFilter, GetDatasetJobsAndFilter, "GetDatasetJobsTimeFilter"],
    pydantic.Field(discriminator="type"),
]
"""Query for getting jobs on given dataset."""


class GetDatasetJobsSort(core.ModelBase):
    """GetDatasetJobsSort"""

    sort_type: GetDatasetJobsSortType = pydantic.Field(alias=str("sortType"))  # type: ignore[literal-required]
    sort_direction: GetDatasetJobsSortDirection = pydantic.Field(alias=str("sortDirection"))  # type: ignore[literal-required]


GetDatasetJobsSortDirection = typing.Literal["ASCENDING", "DESCENDING"]
"""GetDatasetJobsSortDirection"""


GetDatasetJobsSortType = typing.Literal["BY_STARTED_TIME", "BY_FINISHED_TIME"]
"""GetDatasetJobsSortType"""


class GetDatasetJobsTimeFilter(core.ModelBase):
    """GetDatasetJobsTimeFilter"""

    field: GetDatasetJobsTimeFilterField
    comparison_type: GetDatasetJobsComparisonType = pydantic.Field(alias=str("comparisonType"))  # type: ignore[literal-required]
    value: core.AwareDatetime
    type: typing.Literal["timeFilter"] = "timeFilter"


GetDatasetJobsTimeFilterField = typing.Literal["SUBMITTED_TIME", "FINISHED_TIME"]
"""GetDatasetJobsTimeFilterField"""


class GetDatasetSchemaResponse(core.ModelBase):
    """GetDatasetSchemaResponse"""

    branch_name: BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    end_transaction_rid: TransactionRid = pydantic.Field(alias=str("endTransactionRid"))  # type: ignore[literal-required]
    schema_: core_models.DatasetSchema = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    version_id: core_models.VersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]


class GetJobResponse(core.ModelBase):
    """GetJobResponse"""

    jobs: typing.List[JobDetails]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class JobDetails(core.ModelBase):
    """JobDetails"""

    job_rid: core_models.JobRid = pydantic.Field(alias=str("jobRid"))  # type: ignore[literal-required]


class ListBranchesResponse(core.ModelBase):
    """ListBranchesResponse"""

    data: typing.List[Branch]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListFilesResponse(core.ModelBase):
    """ListFilesResponse"""

    data: typing.List[File]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListSchedulesResponse(core.ModelBase):
    """ListSchedulesResponse"""

    data: typing.List[core_models.ScheduleRid]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListTransactionsOfDatasetResponse(core.ModelBase):
    """ListTransactionsOfDatasetResponse"""

    data: typing.List[Transaction]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class ListTransactionsResponse(core.ModelBase):
    """ListTransactionsResponse"""

    data: typing.List[Transaction]
    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]


class PrimaryKeyLatestWinsResolutionStrategy(core.ModelBase):
    """Picks the row with the highest value of a list of columns, compared in order."""

    columns: typing.List[str]
    type: typing.Literal["latestWins"] = "latestWins"


class PrimaryKeyResolutionDuplicate(core.ModelBase):
    """Duplicate primary key values may exist within the dataset – resolution required."""

    deletion_column: typing.Optional[str] = pydantic.Field(alias=str("deletionColumn"), default=None)  # type: ignore[literal-required]
    """
    The name of the boolean column that indicates whether a row should be considered deleted. Based on the 
    `resolutionStrategy`, if the final row selected for a given primary key has `true` in this column, that 
    row will be excluded from the results. Otherwise, it will be included.
    """

    resolution_strategy: PrimaryKeyResolutionStrategy = pydantic.Field(alias=str("resolutionStrategy"))  # type: ignore[literal-required]
    type: typing.Literal["duplicate"] = "duplicate"


class PrimaryKeyResolutionUnique(core.ModelBase):
    """Primary key values are unique within the dataset – no conflicts."""

    type: typing.Literal["unique"] = "unique"


TableExportFormat = typing.Literal["ARROW", "CSV"]
"""Format for tabular dataset export."""


class Transaction(core.ModelBase):
    """Transaction"""

    rid: TransactionRid
    transaction_type: TransactionType = pydantic.Field(alias=str("transactionType"))  # type: ignore[literal-required]
    status: TransactionStatus
    created_time: TransactionCreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp when the transaction was created, in ISO 8601 timestamp format."""

    closed_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("closedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the transaction was closed, in ISO 8601 timestamp format."""


TransactionCreatedTime = core.AwareDatetime
"""The timestamp when the transaction was created, in ISO 8601 timestamp format."""


TransactionRid = core.RID
"""The Resource Identifier (RID) of a Transaction."""


TransactionStatus = typing.Literal["ABORTED", "COMMITTED", "OPEN"]
"""The status of a Transaction."""


TransactionType = typing.Literal["APPEND", "UPDATE", "SNAPSHOT", "DELETE"]
"""The type of a Transaction."""


class View(core.ModelBase):
    """View"""

    view_name: DatasetName = pydantic.Field(alias=str("viewName"))  # type: ignore[literal-required]
    dataset_rid: DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The rid of the View."""

    parent_folder_rid: filesystem_models.FolderRid = pydantic.Field(alias=str("parentFolderRid"))  # type: ignore[literal-required]
    branch: typing.Optional[BranchName] = None
    """The branch name of the View. If not specified, defaults to `master` for most enrollments."""

    backing_datasets: typing.List[ViewBackingDataset] = pydantic.Field(alias=str("backingDatasets"))  # type: ignore[literal-required]
    primary_key: typing.Optional[ViewPrimaryKey] = pydantic.Field(alias=str("primaryKey"), default=None)  # type: ignore[literal-required]


class ViewBackingDataset(core.ModelBase):
    """One of the Datasets backing a View."""

    branch: BranchName
    dataset_rid: DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]


class ViewPrimaryKey(core.ModelBase):
    """
    The primary key of the dataset. Primary keys are treated as guarantees provided by the creator of the
    dataset.
    """

    columns: typing.List[str]
    """
    The columns that constitute the primary key. These columns must satisfy the following constraints:
    - The list of columns must be non-empty.
    - The list must not contain duplicate columns after applying column normalization.
    - Each referenced column must exist in the schema.
    - The type of each referenced column must be one of the following: `BYTE`, `SHORT`, `DECIMAL`, `INTEGER`,
      `LONG`, `STRING`, `BOOLEAN`, `TIMESTAMP` or `DATE`.
    """

    resolution: ViewPrimaryKeyResolution
    """
    The semantics of the primary key within the dataset. For example, the unique resolution means that every 
    row in the dataset has a distinct primary key. The value of this field represents a contract for writers 
    of the dataset. Writers are responsible for maintaining any related invariants, and readers may make 
    optimizations based on this. Violating the assumptions of the resolution can cause undefined behavior, 
    for example, having duplicate primary keys with the unique resolution.
    """


ViewPrimaryKeyResolution = typing_extensions.Annotated[
    typing.Union[PrimaryKeyResolutionUnique, PrimaryKeyResolutionDuplicate],
    pydantic.Field(discriminator="type"),
]
"""Specifies how primary key conflicts are resolved within the view."""


PrimaryKeyResolutionStrategy = PrimaryKeyLatestWinsResolutionStrategy
"""PrimaryKeyResolutionStrategy"""


core.resolve_forward_references(GetDatasetJobsQuery, globalns=globals(), localns=locals())
core.resolve_forward_references(ViewPrimaryKeyResolution, globalns=globals(), localns=locals())

__all__ = [
    "Branch",
    "BranchName",
    "DataframeReader",
    "Dataset",
    "DatasetName",
    "DatasetRid",
    "File",
    "FileUpdatedTime",
    "GetDatasetJobsAndFilter",
    "GetDatasetJobsComparisonType",
    "GetDatasetJobsOrFilter",
    "GetDatasetJobsQuery",
    "GetDatasetJobsSort",
    "GetDatasetJobsSortDirection",
    "GetDatasetJobsSortType",
    "GetDatasetJobsTimeFilter",
    "GetDatasetJobsTimeFilterField",
    "GetDatasetSchemaResponse",
    "GetJobResponse",
    "JobDetails",
    "ListBranchesResponse",
    "ListFilesResponse",
    "ListSchedulesResponse",
    "ListTransactionsOfDatasetResponse",
    "ListTransactionsResponse",
    "PrimaryKeyLatestWinsResolutionStrategy",
    "PrimaryKeyResolutionDuplicate",
    "PrimaryKeyResolutionStrategy",
    "PrimaryKeyResolutionUnique",
    "TableExportFormat",
    "Transaction",
    "TransactionCreatedTime",
    "TransactionRid",
    "TransactionStatus",
    "TransactionType",
    "View",
    "ViewBackingDataset",
    "ViewPrimaryKey",
    "ViewPrimaryKeyResolution",
]
