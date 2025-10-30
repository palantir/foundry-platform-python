# ReplaceCheckConfig

Configuration of a check.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ReplaceColumnTypeCheckConfig | columnType
ReplaceNumericColumnRangeCheckConfig | numericColumnRange
ReplaceJobStatusCheckConfig | jobStatus
ReplaceNumericColumnMeanCheckConfig | numericColumnMean
ReplaceJobDurationCheckConfig | jobDuration
ReplaceNullPercentageCheckConfig | nullPercentage
ReplaceTotalColumnCountCheckConfig | totalColumnCount
ReplaceNumericColumnMedianCheckConfig | numericColumnMedian
ReplaceBuildDurationCheckConfig | buildDuration
ReplaceSchemaComparisonCheckConfig | schemaComparison
ReplaceBuildStatusCheckConfig | buildStatus
ReplacePrimaryKeyCheckConfig | primaryKey


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
