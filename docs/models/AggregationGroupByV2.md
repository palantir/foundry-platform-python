# AggregationGroupByV2

Specifies a grouping for aggregation results.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[AggregationFixedWidthGroupingV2](AggregationFixedWidthGroupingV2.md) | fixedWidth
[AggregationRangesGroupingV2](AggregationRangesGroupingV2.md) | ranges
[AggregationExactGroupingV2](AggregationExactGroupingV2.md) | exact
[AggregationDurationGroupingV2](AggregationDurationGroupingV2.md) | duration


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)