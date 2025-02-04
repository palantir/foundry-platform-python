# GetSelectedPropertyOperationDict

Gets a single value of a property. Throws if the target object set is on the MANY side of the link and could
explode the cardinality.

Use collectList or collectSet which will return a list of values in that case.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**selectedPropertyApiName** | PropertyApiName | Yes |  |
**type** | Literal["get"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
