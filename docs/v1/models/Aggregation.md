# Aggregation

Specifies an aggregation function.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[MaxAggregation](MaxAggregation.md) | max
[MinAggregation](MinAggregation.md) | min
[AvgAggregation](AvgAggregation.md) | avg
[SumAggregation](SumAggregation.md) | sum
[CountAggregation](CountAggregation.md) | count
[ApproximateDistinctAggregation](ApproximateDistinctAggregation.md) | approximateDistinct


[[Back to Model list]](../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
