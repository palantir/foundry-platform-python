# ObjectContextDict

Details of relevant retrieved object instances for a user's message to include as additional context in the prompt to the Agent.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**objectRids** | typing.List[ontologies_models.ObjectRid] | Yes | The RIDs of the relevant object instances to include in the prompt. |
**propertyTypeRids** | typing.List[ontologies_models.PropertyTypeRid] | Yes | The RIDs of the property types for the given objects to include in the prompt. |
**type** | typing.Literal["objectContext"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
