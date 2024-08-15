# AggregationV2

Specifies an aggregation function.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[MaxAggregationV2](MaxAggregationV2.md) | max
[MinAggregationV2](MinAggregationV2.md) | min
[AvgAggregationV2](AvgAggregationV2.md) | avg
[SumAggregationV2](SumAggregationV2.md) | sum
[CountAggregationV2](CountAggregationV2.md) | count
[ApproximateDistinctAggregationV2](ApproximateDistinctAggregationV2.md) | approximateDistinct
[ApproximatePercentileAggregationV2](ApproximatePercentileAggregationV2.md) | approximatePercentile


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
