# UnknownWorker

A ConnectionWorker that is not supported in the Platform APIs. This can happen because either the 
ConnectionWorker configuration is malformed, or because the ConnectionWorker is a legacy one.
The ConnectionWorker should be updated to use the [Foundry worker](https://palantir.com/docs/foundry/data-connection/core-concepts/#foundry-worker) 
with either direct egress policies or agent proxy egress policies.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**type** | Literal["unknownWorker"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
