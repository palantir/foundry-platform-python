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


class AllowedColumnValuesCheckConfig(core.ModelBase):
    """Checks that values in a column are within an allowed set of values."""

    subject: DatasetSubject
    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    allowed_values: typing.List[ColumnValue] = pydantic.Field(alias=str("allowedValues"))  # type: ignore[literal-required]
    allow_null: typing.Optional[bool] = pydantic.Field(alias=str("allowNull"), default=None)  # type: ignore[literal-required]
    severity: SeverityLevel
    type: typing.Literal["allowedColumnValues"] = "allowedColumnValues"


class ApproximateUniquePercentageCheckConfig(core.ModelBase):
    """Checks the approximate percentage of unique values in a specific column."""

    subject: DatasetSubject
    percentage_check_config: PercentageCheckConfig = pydantic.Field(alias=str("percentageCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["approximateUniquePercentage"] = "approximateUniquePercentage"


class BooleanColumnValue(core.ModelBase):
    """A boolean column value."""

    value: bool
    type: typing.Literal["boolean"] = "boolean"


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

    rid: core_models.CheckRid
    groups: typing.List[CheckGroupRid]
    config: CheckConfig
    intent: typing.Optional[CheckIntent] = None
    created_by: typing.Optional[core_models.CreatedBy] = pydantic.Field(alias=str("createdBy"), default=None)  # type: ignore[literal-required]
    """The user that created the Check."""

    updated_time: typing.Optional[core_models.UpdatedTime] = pydantic.Field(alias=str("updatedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the Check was last updated."""


CheckConfig = typing_extensions.Annotated[
    typing.Union[
        "NumericColumnRangeCheckConfig",
        "JobStatusCheckConfig",
        "NumericColumnMeanCheckConfig",
        "DateColumnRangeCheckConfig",
        "JobDurationCheckConfig",
        "ApproximateUniquePercentageCheckConfig",
        "BuildStatusCheckConfig",
        "ColumnTypeCheckConfig",
        "AllowedColumnValuesCheckConfig",
        "NullPercentageCheckConfig",
        "TotalColumnCountCheckConfig",
        "NumericColumnMedianCheckConfig",
        "BuildDurationCheckConfig",
        "SchemaComparisonCheckConfig",
        "PrimaryKeyCheckConfig",
    ],
    pydantic.Field(discriminator="type"),
]
"""Configuration of a check."""


CheckGroupRid = core.RID
"""The unique resource identifier (RID) of a CheckGroup."""


CheckIntent = str
"""A note about why the Check was set up."""


class CheckReport(core.ModelBase):
    """CheckReport"""

    rid: core_models.CheckReportRid
    check: Check
    """Snapshot of the check configuration when this report was created. This will not change if the check is later modified."""

    result: CheckResult
    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]


class CheckResult(core.ModelBase):
    """The result of running a check."""

    status: CheckResultStatus
    message: typing.Optional[str] = None
    """Further details about the result of the check."""


CheckResultStatus = typing.Literal[
    "PASSED", "FAILED", "WARNING", "ERROR", "NOT_APPLICABLE", "NOT_COMPUTABLE"
]
"""The status of a check report execution."""


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

    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    expected_type: typing.Optional[core_models.SchemaFieldType] = pydantic.Field(alias=str("expectedType"), default=None)  # type: ignore[literal-required]
    severity: SeverityLevel


ColumnValue = typing_extensions.Annotated[
    typing.Union[
        "DateColumnValue", "BooleanColumnValue", "StringColumnValue", "NumericColumnValue"
    ],
    pydantic.Field(discriminator="type"),
]
"""A column value that can be of different types."""


class CreateCheckRequest(core.ModelBase):
    """CreateCheckRequest"""

    config: CheckConfig
    intent: typing.Optional[CheckIntent] = None


class DatasetSubject(core.ModelBase):
    """A dataset resource type."""

    dataset_rid: datasets_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    branch_id: datasets_models.BranchName = pydantic.Field(alias=str("branchId"))  # type: ignore[literal-required]


class DateBounds(core.ModelBase):
    """The range of date values a check is expected to be within."""

    lower_bound: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("lowerBound"), default=None)  # type: ignore[literal-required]
    upper_bound: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("upperBound"), default=None)  # type: ignore[literal-required]


class DateBoundsConfig(core.ModelBase):
    """Configuration for date bounds check with severity settings."""

    date_bounds: DateBounds = pydantic.Field(alias=str("dateBounds"))  # type: ignore[literal-required]
    severity: SeverityLevel


class DateColumnRangeCheckConfig(core.ModelBase):
    """Checks that values in a date column fall within a specified range."""

    subject: DatasetSubject
    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    date_bounds_config: DateBoundsConfig = pydantic.Field(alias=str("dateBoundsConfig"))  # type: ignore[literal-required]
    type: typing.Literal["dateColumnRange"] = "dateColumnRange"


class DateColumnValue(core.ModelBase):
    """A date column value."""

    value: core.AwareDatetime
    type: typing.Literal["date"] = "date"


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


class NullPercentageCheckConfig(core.ModelBase):
    """Checks the percentage of null values in a specific column."""

    subject: DatasetSubject
    percentage_check_config: PercentageCheckConfig = pydantic.Field(alias=str("percentageCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["nullPercentage"] = "nullPercentage"


class NumericBounds(core.ModelBase):
    """The range of numeric values a check is expected to be within."""

    lower_bound: typing.Optional[float] = pydantic.Field(alias=str("lowerBound"), default=None)  # type: ignore[literal-required]
    upper_bound: typing.Optional[float] = pydantic.Field(alias=str("upperBound"), default=None)  # type: ignore[literal-required]


class NumericBoundsConfig(core.ModelBase):
    """Configuration for numeric bounds check with severity settings."""

    numeric_bounds: NumericBounds = pydantic.Field(alias=str("numericBounds"))  # type: ignore[literal-required]
    severity: SeverityLevel


class NumericColumnCheckConfig(core.ModelBase):
    """Configuration for numeric column-based checks (such as mean or median). At least one of numericBounds or trend must be specified. Both may be provided to validate both the absolute value range and the trend behavior over time."""

    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    numeric_bounds: typing.Optional[NumericBoundsConfig] = pydantic.Field(alias=str("numericBounds"), default=None)  # type: ignore[literal-required]
    trend: typing.Optional[TrendConfig] = None


class NumericColumnMeanCheckConfig(core.ModelBase):
    """Checks the mean value of a numeric column."""

    subject: DatasetSubject
    numeric_column_check_config: NumericColumnCheckConfig = pydantic.Field(alias=str("numericColumnCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["numericColumnMean"] = "numericColumnMean"


class NumericColumnMedianCheckConfig(core.ModelBase):
    """Checks the median value of a numeric column."""

    subject: DatasetSubject
    numeric_column_check_config: NumericColumnCheckConfig = pydantic.Field(alias=str("numericColumnCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["numericColumnMedian"] = "numericColumnMedian"


class NumericColumnRangeCheckConfig(core.ModelBase):
    """Checks that values in a numeric column fall within a specified range."""

    subject: DatasetSubject
    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    numeric_bounds_config: NumericBoundsConfig = pydantic.Field(alias=str("numericBoundsConfig"))  # type: ignore[literal-required]
    type: typing.Literal["numericColumnRange"] = "numericColumnRange"


class NumericColumnValue(core.ModelBase):
    """A numeric column value."""

    value: float
    type: typing.Literal["numeric"] = "numeric"


class PercentageBounds(core.ModelBase):
    """The configuration for the range of percentage values between which the health check is expected to succeed."""

    lower_bound_percentage: typing.Optional[PercentageValue] = pydantic.Field(alias=str("lowerBoundPercentage"), default=None)  # type: ignore[literal-required]
    upper_bound_percentage: typing.Optional[PercentageValue] = pydantic.Field(alias=str("upperBoundPercentage"), default=None)  # type: ignore[literal-required]


class PercentageBoundsConfig(core.ModelBase):
    """Configuration for percentage bounds check with severity settings."""

    percentage_bounds: PercentageBounds = pydantic.Field(alias=str("percentageBounds"))  # type: ignore[literal-required]
    severity: SeverityLevel


class PercentageCheckConfig(core.ModelBase):
    """Configuration for percentage-based checks (such as null percentage)."""

    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    percentage_bounds: typing.Optional[PercentageBoundsConfig] = pydantic.Field(alias=str("percentageBounds"), default=None)  # type: ignore[literal-required]
    median_deviation: typing.Optional[MedianDeviationConfig] = pydantic.Field(alias=str("medianDeviation"), default=None)  # type: ignore[literal-required]


PercentageValue = float
"""
A percentage value in the range 0.0 to 100.0.

Validation rules:
 * must be greater than or equal to 0.0
 * must be less than or equal to 100.0
"""


class PrimaryKeyCheckConfig(core.ModelBase):
    """Checks the uniqueness and non-null values of one or more columns (primary key constraint)."""

    subject: DatasetSubject
    primary_key_config: PrimaryKeyConfig = pydantic.Field(alias=str("primaryKeyConfig"))  # type: ignore[literal-required]
    type: typing.Literal["primaryKey"] = "primaryKey"


class PrimaryKeyConfig(core.ModelBase):
    """Configuration for primary key validation with severity settings."""

    column_names: typing.List[ColumnName] = pydantic.Field(alias=str("columnNames"))  # type: ignore[literal-required]
    severity: SeverityLevel


class ReplaceAllowedColumnValuesCheckConfig(core.ModelBase):
    """ReplaceAllowedColumnValuesCheckConfig"""

    allowed_values: typing.List[ColumnValue] = pydantic.Field(alias=str("allowedValues"))  # type: ignore[literal-required]
    severity: SeverityLevel
    allow_null: typing.Optional[bool] = pydantic.Field(alias=str("allowNull"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["allowedColumnValues"] = "allowedColumnValues"


class ReplaceApproximateUniquePercentageCheckConfig(core.ModelBase):
    """ReplaceApproximateUniquePercentageCheckConfig"""

    percentage_check_config: ReplacePercentageCheckConfig = pydantic.Field(alias=str("percentageCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["approximateUniquePercentage"] = "approximateUniquePercentage"


class ReplaceBuildDurationCheckConfig(core.ModelBase):
    """ReplaceBuildDurationCheckConfig"""

    time_check_config: TimeCheckConfig = pydantic.Field(alias=str("timeCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["buildDuration"] = "buildDuration"


class ReplaceBuildStatusCheckConfig(core.ModelBase):
    """ReplaceBuildStatusCheckConfig"""

    status_check_config: StatusCheckConfig = pydantic.Field(alias=str("statusCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["buildStatus"] = "buildStatus"


ReplaceCheckConfig = typing_extensions.Annotated[
    typing.Union[
        "ReplaceNumericColumnRangeCheckConfig",
        "ReplaceJobStatusCheckConfig",
        "ReplaceNumericColumnMeanCheckConfig",
        "ReplaceDateColumnRangeCheckConfig",
        "ReplaceJobDurationCheckConfig",
        "ReplaceApproximateUniquePercentageCheckConfig",
        "ReplaceBuildStatusCheckConfig",
        "ReplaceColumnTypeCheckConfig",
        "ReplaceAllowedColumnValuesCheckConfig",
        "ReplaceNullPercentageCheckConfig",
        "ReplaceTotalColumnCountCheckConfig",
        "ReplaceNumericColumnMedianCheckConfig",
        "ReplaceBuildDurationCheckConfig",
        "ReplaceSchemaComparisonCheckConfig",
        "ReplacePrimaryKeyCheckConfig",
    ],
    pydantic.Field(discriminator="type"),
]
"""Configuration of a check."""


class ReplaceCheckRequest(core.ModelBase):
    """ReplaceCheckRequest"""

    config: ReplaceCheckConfig
    intent: typing.Optional[CheckIntent] = None


class ReplaceColumnTypeCheckConfig(core.ModelBase):
    """ReplaceColumnTypeCheckConfig"""

    column_type_config: ReplaceColumnTypeConfig = pydantic.Field(alias=str("columnTypeConfig"))  # type: ignore[literal-required]
    type: typing.Literal["columnType"] = "columnType"


class ReplaceColumnTypeConfig(core.ModelBase):
    """ReplaceColumnTypeConfig"""

    severity: SeverityLevel
    expected_type: typing.Optional[core_models.SchemaFieldType] = pydantic.Field(alias=str("expectedType"), default=None)  # type: ignore[literal-required]


class ReplaceDateColumnRangeCheckConfig(core.ModelBase):
    """ReplaceDateColumnRangeCheckConfig"""

    date_bounds_config: DateBoundsConfig = pydantic.Field(alias=str("dateBoundsConfig"))  # type: ignore[literal-required]
    type: typing.Literal["dateColumnRange"] = "dateColumnRange"


class ReplaceJobDurationCheckConfig(core.ModelBase):
    """ReplaceJobDurationCheckConfig"""

    time_check_config: TimeCheckConfig = pydantic.Field(alias=str("timeCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["jobDuration"] = "jobDuration"


class ReplaceJobStatusCheckConfig(core.ModelBase):
    """ReplaceJobStatusCheckConfig"""

    status_check_config: StatusCheckConfig = pydantic.Field(alias=str("statusCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["jobStatus"] = "jobStatus"


class ReplaceNullPercentageCheckConfig(core.ModelBase):
    """ReplaceNullPercentageCheckConfig"""

    percentage_check_config: ReplacePercentageCheckConfig = pydantic.Field(alias=str("percentageCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["nullPercentage"] = "nullPercentage"


class ReplaceNumericColumnCheckConfig(core.ModelBase):
    """ReplaceNumericColumnCheckConfig"""

    numeric_bounds: typing.Optional[NumericBoundsConfig] = pydantic.Field(alias=str("numericBounds"), default=None)  # type: ignore[literal-required]
    trend: typing.Optional[TrendConfig] = None


class ReplaceNumericColumnMeanCheckConfig(core.ModelBase):
    """ReplaceNumericColumnMeanCheckConfig"""

    numeric_column_check_config: ReplaceNumericColumnCheckConfig = pydantic.Field(alias=str("numericColumnCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["numericColumnMean"] = "numericColumnMean"


class ReplaceNumericColumnMedianCheckConfig(core.ModelBase):
    """ReplaceNumericColumnMedianCheckConfig"""

    numeric_column_check_config: ReplaceNumericColumnCheckConfig = pydantic.Field(alias=str("numericColumnCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["numericColumnMedian"] = "numericColumnMedian"


class ReplaceNumericColumnRangeCheckConfig(core.ModelBase):
    """ReplaceNumericColumnRangeCheckConfig"""

    numeric_bounds_config: NumericBoundsConfig = pydantic.Field(alias=str("numericBoundsConfig"))  # type: ignore[literal-required]
    type: typing.Literal["numericColumnRange"] = "numericColumnRange"


class ReplacePercentageCheckConfig(core.ModelBase):
    """ReplacePercentageCheckConfig"""

    median_deviation: typing.Optional[MedianDeviationConfig] = pydantic.Field(alias=str("medianDeviation"), default=None)  # type: ignore[literal-required]
    percentage_bounds: typing.Optional[PercentageBoundsConfig] = pydantic.Field(alias=str("percentageBounds"), default=None)  # type: ignore[literal-required]


class ReplacePrimaryKeyCheckConfig(core.ModelBase):
    """ReplacePrimaryKeyCheckConfig"""

    primary_key_config: ReplacePrimaryKeyConfig = pydantic.Field(alias=str("primaryKeyConfig"))  # type: ignore[literal-required]
    type: typing.Literal["primaryKey"] = "primaryKey"


class ReplacePrimaryKeyConfig(core.ModelBase):
    """ReplacePrimaryKeyConfig"""

    severity: SeverityLevel


class ReplaceSchemaComparisonCheckConfig(core.ModelBase):
    """ReplaceSchemaComparisonCheckConfig"""

    schema_comparison_config: SchemaComparisonConfig = pydantic.Field(alias=str("schemaComparisonConfig"))  # type: ignore[literal-required]
    type: typing.Literal["schemaComparison"] = "schemaComparison"


class ReplaceTotalColumnCountCheckConfig(core.ModelBase):
    """ReplaceTotalColumnCountCheckConfig"""

    column_count_config: ColumnCountConfig = pydantic.Field(alias=str("columnCountConfig"))  # type: ignore[literal-required]
    type: typing.Literal["totalColumnCount"] = "totalColumnCount"


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


SeverityLevel = typing.Literal["MODERATE", "CRITICAL"]
"""The severity level of the check. Possible values are MODERATE or CRITICAL."""


class StatusCheckConfig(core.ModelBase):
    """StatusCheckConfig"""

    severity: SeverityLevel
    escalation_config: typing.Optional[EscalationConfig] = pydantic.Field(alias=str("escalationConfig"), default=None)  # type: ignore[literal-required]


class StringColumnValue(core.ModelBase):
    """A string column value."""

    value: str
    type: typing.Literal["string"] = "string"


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


class TrendConfig(core.ModelBase):
    """Configuration for trend-based validation with severity settings. At least one of trendType or differenceBounds must be specified. Both may be provided to validate both the trend pattern and the magnitude of change."""

    trend_type: typing.Optional[TrendType] = pydantic.Field(alias=str("trendType"), default=None)  # type: ignore[literal-required]
    difference_bounds: typing.Optional[NumericBounds] = pydantic.Field(alias=str("differenceBounds"), default=None)  # type: ignore[literal-required]
    severity: SeverityLevel


TrendType = typing.Literal[
    "NON_INCREASING", "NON_DECREASING", "STRICTLY_INCREASING", "STRICTLY_DECREASING", "CONSTANT"
]
"""
The type of trend to validate:
- NON_INCREASING: Values should not increase over time
- NON_DECREASING: Values should not decrease over time
- STRICTLY_INCREASING: Values should strictly increase over time
- STRICTLY_DECREASING: Values should strictly decrease over time
- CONSTANT: Values should remain constant over time
"""


core.resolve_forward_references(CheckConfig, globalns=globals(), localns=locals())
core.resolve_forward_references(ColumnValue, globalns=globals(), localns=locals())
core.resolve_forward_references(ReplaceCheckConfig, globalns=globals(), localns=locals())

__all__ = [
    "AllowedColumnValuesCheckConfig",
    "ApproximateUniquePercentageCheckConfig",
    "BooleanColumnValue",
    "BuildDurationCheckConfig",
    "BuildStatusCheckConfig",
    "Check",
    "CheckConfig",
    "CheckGroupRid",
    "CheckIntent",
    "CheckReport",
    "CheckResult",
    "CheckResultStatus",
    "ColumnCountConfig",
    "ColumnInfo",
    "ColumnName",
    "ColumnTypeCheckConfig",
    "ColumnTypeConfig",
    "ColumnValue",
    "CreateCheckRequest",
    "DatasetSubject",
    "DateBounds",
    "DateBoundsConfig",
    "DateColumnRangeCheckConfig",
    "DateColumnValue",
    "EscalationConfig",
    "JobDurationCheckConfig",
    "JobStatusCheckConfig",
    "MedianDeviation",
    "MedianDeviationBoundsType",
    "MedianDeviationConfig",
    "NullPercentageCheckConfig",
    "NumericBounds",
    "NumericBoundsConfig",
    "NumericColumnCheckConfig",
    "NumericColumnMeanCheckConfig",
    "NumericColumnMedianCheckConfig",
    "NumericColumnRangeCheckConfig",
    "NumericColumnValue",
    "PercentageBounds",
    "PercentageBoundsConfig",
    "PercentageCheckConfig",
    "PercentageValue",
    "PrimaryKeyCheckConfig",
    "PrimaryKeyConfig",
    "ReplaceAllowedColumnValuesCheckConfig",
    "ReplaceApproximateUniquePercentageCheckConfig",
    "ReplaceBuildDurationCheckConfig",
    "ReplaceBuildStatusCheckConfig",
    "ReplaceCheckConfig",
    "ReplaceCheckRequest",
    "ReplaceColumnTypeCheckConfig",
    "ReplaceColumnTypeConfig",
    "ReplaceDateColumnRangeCheckConfig",
    "ReplaceJobDurationCheckConfig",
    "ReplaceJobStatusCheckConfig",
    "ReplaceNullPercentageCheckConfig",
    "ReplaceNumericColumnCheckConfig",
    "ReplaceNumericColumnMeanCheckConfig",
    "ReplaceNumericColumnMedianCheckConfig",
    "ReplaceNumericColumnRangeCheckConfig",
    "ReplacePercentageCheckConfig",
    "ReplacePrimaryKeyCheckConfig",
    "ReplacePrimaryKeyConfig",
    "ReplaceSchemaComparisonCheckConfig",
    "ReplaceTotalColumnCountCheckConfig",
    "SchemaComparisonCheckConfig",
    "SchemaComparisonConfig",
    "SchemaComparisonType",
    "SchemaInfo",
    "SeverityLevel",
    "StatusCheckConfig",
    "StringColumnValue",
    "TimeBounds",
    "TimeBoundsConfig",
    "TimeCheckConfig",
    "TotalColumnCountCheckConfig",
    "TrendConfig",
    "TrendType",
]
