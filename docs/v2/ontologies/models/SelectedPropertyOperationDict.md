# SelectedPropertyOperationDict

Operation on a selected property, can be an aggregation function or retrieval of a single selected property


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
SelectedPropertyApproximateDistinctAggregationDict | approximateDistinct
SelectedPropertyMinAggregationDict | min
SelectedPropertyAvgAggregationDict | avg
SelectedPropertyMaxAggregationDict | max
SelectedPropertyApproximatePercentileAggregationDict | approximatePercentile
GetSelectedPropertyOperationDict | get
SelectedPropertyCountAggregationDict | count
SelectedPropertySumAggregationDict | sum
SelectedPropertyCollectListAggregationDict | collectList
SelectedPropertyExactDistinctAggregationDict | exactDistinct
SelectedPropertyCollectSetAggregationDict | collectSet


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
