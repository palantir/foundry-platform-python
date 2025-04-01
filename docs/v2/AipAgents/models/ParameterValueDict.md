# ParameterValueDict

The value provided for a variable configured in the [application state](https://palantir.com/docs/foundry/agent-studio/application-state/) of an Agent.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
StringParameterValueDict | string
ObjectSetParameterValueDict | objectSet


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
