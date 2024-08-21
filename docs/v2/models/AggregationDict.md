# AggregationDict

Specifies an aggregation function.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[MaxAggregationDict](MaxAggregationDict.md) | max
[MinAggregationDict](MinAggregationDict.md) | min
[AvgAggregationDict](AvgAggregationDict.md) | avg
[SumAggregationDict](SumAggregationDict.md) | sum
[CountAggregationDict](CountAggregationDict.md) | count
[ApproximateDistinctAggregationDict](ApproximateDistinctAggregationDict.md) | approximateDistinct


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)
