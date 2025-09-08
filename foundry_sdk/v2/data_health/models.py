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
from foundry_sdk.v2.datasets import models as datasets_models


class BuildDurationCheckConfig(core.ModelBase):
    """Checks the total time a build takes to complete."""

    subject: DatasetSubject
    time_check_config: TimeCheckConfig = pydantic.Field(alias=str("timeCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["buildDuration"] = "buildDuration"


class BuildStatusCheckConfig(core.ModelBase):
    """Checks the status of the most recent build of the dataset."""

    subject: DatasetSubject
    status_check_config: StatusCheckConfig = pydantic.Field(alias=str("statusCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["buildStatus"] = "buildStatus"


class Check(core.ModelBase):
    """Check"""

    rid: CheckRid
    groups: typing.List[CheckGroupRid]
    config: CheckConfig
    intent: typing.Optional[CheckIntent] = None
    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]
    """The user that created the Check."""

    updated_time: typing.Optional[core_models.UpdatedTime] = pydantic.Field(alias=str("updatedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the Check was last updated."""


CheckConfig = typing_extensions.Annotated[
    typing.Union[
        "ColumnTypeCheckConfig",
        "JobStatusCheckConfig",
        "JobDurationCheckConfig",
        "TotalColumnCountCheckConfig",
        BuildDurationCheckConfig,
        "SchemaComparisonCheckConfig",
        BuildStatusCheckConfig,
    ],
    pydantic.Field(discriminator="type"),
]
"""Configuration of a check."""


CheckGroupRid = core.RID
"""The unique resource identifier (RID) of a CheckGroup."""


CheckIntent = str
"""A note about why the Check was set up."""


CheckRid = core.RID
"""The unique resource identifier (RID) of a Check."""


class ColumnCountConfig(core.ModelBase):
    """Configuration for column count validation with severity settings."""

    expected_value: core.Long = pydantic.Field(alias=str("expectedValue"))  # type: ignore[literal-required]
    severity: SeverityLevel


class ColumnInfo(core.ModelBase):
    """Information about a column including its name and type."""

    name: ColumnName
    column_type: typing.Optional[core_models.SchemaFieldType] = pydantic.Field(alias=str("columnType"), default=None)  # type: ignore[literal-required]


ColumnName = str
"""ColumnName"""


class ColumnTypeCheckConfig(core.ModelBase):
    """Checks the existence and optionally the type of a specific column."""

    subject: DatasetSubject
    column_type_config: ColumnTypeConfig = pydantic.Field(alias=str("columnTypeConfig"))  # type: ignore[literal-required]
    type: typing.Literal["columnType"] = "columnType"


class ColumnTypeConfig(core.ModelBase):
    """Configuration for column type validation with severity settings."""

    column_name: str = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    expected_type: typing.Optional[core_models.SchemaFieldType] = pydantic.Field(alias=str("expectedType"), default=None)  # type: ignore[literal-required]
    severity: SeverityLevel


class DatasetSubject(core.ModelBase):
    """A dataset resource type."""

    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    branch_id: datasets_models.BranchName = pydantic.Field(alias=str("branchId"))  # type: ignore[literal-required]


class EscalationConfig(core.ModelBase):
    """The configuration for when the severity of the failing health check should be escalated to CRITICAL – after a given number of failures, possibly within a time interval."""

    failures_to_critical: int = pydantic.Field(alias=str("failuresToCritical"))  # type: ignore[literal-required]
    time_interval_in_seconds: typing.Optional[core.Long] = pydantic.Field(alias=str("timeIntervalInSeconds"), default=None)  # type: ignore[literal-required]


class JobDurationCheckConfig(core.ModelBase):
    """Checks the total time a job takes to complete."""

    subject: DatasetSubject
    time_check_config: TimeCheckConfig = pydantic.Field(alias=str("timeCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["jobDuration"] = "jobDuration"


class JobStatusCheckConfig(core.ModelBase):
    """Checks the status of the most recent job run on the dataset."""

    subject: DatasetSubject
    status_check_config: StatusCheckConfig = pydantic.Field(alias=str("statusCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["jobStatus"] = "jobStatus"


class MedianDeviation(core.ModelBase):
    """The number of thresholds the build's duration differs from the median."""

    bounds_type: typing.Optional[MedianDeviationBoundsType] = pydantic.Field(alias=str("boundsType"), default=None)  # type: ignore[literal-required]
    data_points: int = pydantic.Field(alias=str("dataPoints"))  # type: ignore[literal-required]
    deviation_threshold: float = pydantic.Field(alias=str("deviationThreshold"))  # type: ignore[literal-required]


MedianDeviationBoundsType = typing.Literal["LOWER_BOUND", "UPPER_BOUND", "TWO_TAILED"]
"""The three types of median deviations a bounds type can have: - LOWER_BOUND – Tests for significant deviations below the median value, - UPPER_BOUND – Tests for significant deviations above the median value, - TWO_TAILED – Tests for significant deviations in either direction from the median value."""


class MedianDeviationConfig(core.ModelBase):
    """Configuration for median deviation check with severity settings."""

    median_deviation: MedianDeviation = pydantic.Field(alias=str("medianDeviation"))  # type: ignore[literal-required]
    severity: SeverityLevel


class SchemaComparisonCheckConfig(core.ModelBase):
    """Checks the dataset schema against an expected schema."""

    subject: DatasetSubject
    schema_comparison_config: SchemaComparisonConfig = pydantic.Field(alias=str("schemaComparisonConfig"))  # type: ignore[literal-required]
    type: typing.Literal["schemaComparison"] = "schemaComparison"


class SchemaComparisonConfig(core.ModelBase):
    """Configuration for schema comparison validation with severity settings."""

    expected_schema: SchemaInfo = pydantic.Field(alias=str("expectedSchema"))  # type: ignore[literal-required]
    schema_comparison_type: SchemaComparisonType = pydantic.Field(alias=str("schemaComparisonType"))  # type: ignore[literal-required]
    severity: SeverityLevel


SchemaComparisonType = typing.Literal[
    "EXACT_MATCH_ORDERED_COLUMNS",
    "EXACT_MATCH_UNORDERED_COLUMNS",
    "COLUMN_ADDITIONS_ALLOWED",
    "COLUMN_ADDITIONS_ALLOWED_STRICT",
]
"""
The type of schema comparison to perform:
- EXACT_MATCH_ORDERED_COLUMNS: Schemas must have identical columns in the same order.
- EXACT_MATCH_UNORDERED_COLUMNS: Schemas must have identical columns but order doesn't matter.
- COLUMN_ADDITIONS_ALLOWED: Expected schema columns must be present, additional columns are allowed and 
  missing column types are ignored.
- COLUMN_ADDITIONS_ALLOWED_STRICT: Expected schema columns must be present, additional columns are allowed. 
  Both expected and actual columns must specify types and they must match exactly.
"""


class SchemaInfo(core.ModelBase):
    """Information about a dataset schema including all columns."""

    columns: typing.List[ColumnInfo]


SeverityLevel = typing.Literal["LOW", "MODERATE", "CRITICAL"]
"""The severity level of the check. Possible values are LOW, MODERATE, or CRITICAL."""


class StatusCheckConfig(core.ModelBase):
    """StatusCheckConfig"""

    severity: SeverityLevel
    escalation_config: typing.Optional[EscalationConfig] = pydantic.Field(alias=str("escalationConfig"), default=None)  # type: ignore[literal-required]


class TimeBounds(core.ModelBase):
    """The configuration for the range of time between which the health check is expected to succeed."""

    lower_bound_in_seconds: typing.Optional[core.Long] = pydantic.Field(alias=str("lowerBoundInSeconds"), default=None)  # type: ignore[literal-required]
    upper_bound_in_seconds: typing.Optional[core.Long] = pydantic.Field(alias=str("upperBoundInSeconds"), default=None)  # type: ignore[literal-required]


class TimeBoundsConfig(core.ModelBase):
    """Configuration for time bounds check with severity settings."""

    time_bounds: TimeBounds = pydantic.Field(alias=str("timeBounds"))  # type: ignore[literal-required]
    severity: SeverityLevel


class TimeCheckConfig(core.ModelBase):
    """TimeCheckConfig"""

    time_bounds: typing.Optional[TimeBoundsConfig] = pydantic.Field(alias=str("timeBounds"), default=None)  # type: ignore[literal-required]
    median_deviation: typing.Optional[MedianDeviationConfig] = pydantic.Field(alias=str("medianDeviation"), default=None)  # type: ignore[literal-required]


class TotalColumnCountCheckConfig(core.ModelBase):
    """Checks the total number of columns in the dataset."""

    subject: DatasetSubject
    column_count_config: ColumnCountConfig = pydantic.Field(alias=str("columnCountConfig"))  # type: ignore[literal-required]
    type: typing.Literal["totalColumnCount"] = "totalColumnCount"


core.resolve_forward_references(CheckConfig, globalns=globals(), localns=locals())

__all__ = [
    "BuildDurationCheckConfig",
    "BuildStatusCheckConfig",
    "Check",
    "CheckConfig",
    "CheckGroupRid",
    "CheckIntent",
    "CheckRid",
    "ColumnCountConfig",
    "ColumnInfo",
    "ColumnName",
    "ColumnTypeCheckConfig",
    "ColumnTypeConfig",
    "DatasetSubject",
    "EscalationConfig",
    "JobDurationCheckConfig",
    "JobStatusCheckConfig",
    "MedianDeviation",
    "MedianDeviationBoundsType",
    "MedianDeviationConfig",
    "SchemaComparisonCheckConfig",
    "SchemaComparisonConfig",
    "SchemaComparisonType",
    "SchemaInfo",
    "SeverityLevel",
    "StatusCheckConfig",
    "TimeBounds",
    "TimeBoundsConfig",
    "TimeCheckConfig",
    "TotalColumnCountCheckConfig",
]
