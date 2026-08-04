# CheckConfig

Configuration of a check.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
NumericColumnRangeCheckConfig | numericColumnRange
JobStatusCheckConfig | jobStatus
NumericColumnMeanCheckConfig | numericColumnMean
DateColumnRangeCheckConfig | dateColumnRange
JobDurationCheckConfig | jobDuration
ApproximateUniquePercentageCheckConfig | approximateUniquePercentage
BuildStatusCheckConfig | buildStatus
ColumnTypeCheckConfig | columnType
AllowedColumnValuesCheckConfig | allowedColumnValues
TimeSinceLastUpdatedCheckConfig | timeSinceLastUpdated
ScheduleStatusCheckConfig | scheduleStatus
NullPercentageCheckConfig | nullPercentage
ScheduleDurationCheckConfig | scheduleDuration
TotalColumnCountCheckConfig | totalColumnCount
NumericColumnMedianCheckConfig | numericColumnMedian
BuildDurationCheckConfig | buildDuration
SchemaComparisonCheckConfig | schemaComparison
PrimaryKeyCheckConfig | primaryKey


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
