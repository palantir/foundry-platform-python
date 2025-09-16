# CreateConnectionRequestConnectionWorker

[The worker of a Connection](https://palantir.com/docs/foundry/data-connection/core-concepts/#workers), which defines where
compute for capabilities are run.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
CreateConnectionRequestUnknownWorker | unknownWorker
CreateConnectionRequestFoundryWorker | foundryWorker


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
