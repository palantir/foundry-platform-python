# QueryAggregationKeyTypeDict

A union of all the types supported by query aggregation keys.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
core_models.DateTypeDict | date
core_models.BooleanTypeDict | boolean
core_models.StringTypeDict | string
core_models.DoubleTypeDict | double
QueryAggregationRangeTypeDict | range
core_models.IntegerTypeDict | integer
core_models.TimestampTypeDict | timestamp


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
