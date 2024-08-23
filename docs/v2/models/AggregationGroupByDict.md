# AggregationGroupByDict

Specifies a grouping for aggregation results.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[AggregationFixedWidthGroupingDict](AggregationFixedWidthGroupingDict.md) | fixedWidth
[AggregationRangesGroupingDict](AggregationRangesGroupingDict.md) | ranges
[AggregationExactGroupingDict](AggregationExactGroupingDict.md) | exact
[AggregationDurationGroupingDict](AggregationDurationGroupingDict.md) | duration


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)
