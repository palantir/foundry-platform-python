# AggregationGroupByV2Dict

Specifies a grouping for aggregation results.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
AggregationDurationGroupingV2Dict | duration
AggregationFixedWidthGroupingV2Dict | fixedWidth
AggregationRangesGroupingV2Dict | ranges
AggregationExactGroupingV2Dict | exact


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
