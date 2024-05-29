# TimeRange

An absolute or relative range for a time series query.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[AbsoluteTimeRange](AbsoluteTimeRange.md) | absolute
[RelativeTimeRange](RelativeTimeRange.md) | relative


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)