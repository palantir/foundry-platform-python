# AggregationV2

Specifies an aggregation function.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ApproximateDistinctAggregationV2 | approximateDistinct
MinAggregationV2 | min
AvgAggregationV2 | avg
MaxAggregationV2 | max
ApproximatePercentileAggregationV2 | approximatePercentile
CountAggregationV2 | count
SumAggregationV2 | sum
ExactDistinctAggregationV2 | exactDistinct


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
