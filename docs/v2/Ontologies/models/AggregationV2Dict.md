# AggregationV2Dict

Specifies an aggregation function.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ApproximateDistinctAggregationV2Dict | approximateDistinct
MinAggregationV2Dict | min
AvgAggregationV2Dict | avg
MaxAggregationV2Dict | max
ApproximatePercentileAggregationV2Dict | approximatePercentile
CountAggregationV2Dict | count
SumAggregationV2Dict | sum
ExactDistinctAggregationV2Dict | exactDistinct


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
