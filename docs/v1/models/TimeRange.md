# TimeRange

An absolute or relative range for a time series query.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[AbsoluteTimeRange](AbsoluteTimeRange.md) | absolute
[RelativeTimeRange](RelativeTimeRange.md) | relative


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to README]](../../../README.md)