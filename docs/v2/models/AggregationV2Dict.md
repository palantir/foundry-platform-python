# AggregationV2Dict

Specifies an aggregation function.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[MaxAggregationV2Dict](MaxAggregationV2Dict.md) | max
[MinAggregationV2Dict](MinAggregationV2Dict.md) | min
[AvgAggregationV2Dict](AvgAggregationV2Dict.md) | avg
[SumAggregationV2Dict](SumAggregationV2Dict.md) | sum
[CountAggregationV2Dict](CountAggregationV2Dict.md) | count
[ApproximateDistinctAggregationV2Dict](ApproximateDistinctAggregationV2Dict.md) | approximateDistinct
[ApproximatePercentileAggregationV2Dict](ApproximatePercentileAggregationV2Dict.md) | approximatePercentile


[[Back to Model list]](../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
