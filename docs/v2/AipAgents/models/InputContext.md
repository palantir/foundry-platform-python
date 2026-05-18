# InputContext

Custom retrieved [context](https://palantir.com/docs/foundry/chatbot-studio/retrieval-context/) to provide to an Agent for continuing a session.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
FunctionRetrievedContext | functionRetrievedContext
ObjectContext | objectContext


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
