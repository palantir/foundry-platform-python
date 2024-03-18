# AggregationGroupByRequest

Specifies a grouping for aggregation results.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

Class | Value
------------ | -------------
[AggregationFixedWidthGroupingRequest](AggregationFixedWidthGroupingRequest.md) | fixedWidth
[AggregationRangesGroupingRequest](AggregationRangesGroupingRequest.md) | ranges
[AggregationExactGroupingRequest](AggregationExactGroupingRequest.md) | exact
[AggregationDurationGroupingRequest](AggregationDurationGroupingRequest.md) | duration


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
