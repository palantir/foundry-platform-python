# AggregationRequest

Specifies an aggregation function.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

Class | Value
------------ | -------------
[MaxAggregationRequest](MaxAggregationRequest.md) | max
[MinAggregationRequest](MinAggregationRequest.md) | min
[AvgAggregationRequest](AvgAggregationRequest.md) | avg
[SumAggregationRequest](SumAggregationRequest.md) | sum
[CountAggregationRequest](CountAggregationRequest.md) | count
[ApproximateDistinctAggregationRequest](ApproximateDistinctAggregationRequest.md) | approximateDistinct


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
