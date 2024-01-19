# QueryAggregationValueType

A union of all the types supported by query aggregation keys.

This is a discriminator class and does not contain any additional fields. Instead, it
is a union of of the classes listed below.

This discriminator class uses the `type` field to differentiate between classes.

Class | Value
------------ | -------------
[DateType](DateType.md) | date
[DoubleType](DoubleType.md) | double
[TimestampType](TimestampType.md) | timestamp

[\[Back to Model list\]](../README.md#documentation-for-models) [\[Back to API list\]](../README.md#documentation-for-api-endpoints) [\[Back to README\]](../README.md)
