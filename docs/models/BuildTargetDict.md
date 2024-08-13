# BuildTargetDict

The targets of the build.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
[ManualTargetDict](ManualTargetDict.md) | manual
[UpstreamTargetDict](UpstreamTargetDict.md) | upstream
[ConnectingTargetDict](ConnectingTargetDict.md) | connecting


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)