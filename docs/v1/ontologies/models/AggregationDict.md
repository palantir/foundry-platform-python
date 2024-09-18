# AggregationDict

Specifies an aggregation function.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ApproximateDistinctAggregationDict | approximateDistinct
MinAggregationDict | min
AvgAggregationDict | avg
MaxAggregationDict | max
CountAggregationDict | count
SumAggregationDict | sum


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
