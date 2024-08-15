# QueryAggregationKeyType

A union of all the types supported by query aggregation keys.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[BooleanType](BooleanType.md) | boolean
[DateType](DateType.md) | date
[DoubleType](DoubleType.md) | double
[IntegerType](IntegerType.md) | integer
[StringType](StringType.md) | string
[TimestampType](TimestampType.md) | timestamp
[QueryAggregationRangeType](QueryAggregationRangeType.md) | range


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
