# LinkedObjectLocator

Does not contain information about the source object. Should be used in a nested type that provides information about source objects.
The `targetObject` Ontology Object in this response will only ever have the `__primaryKey` and `__apiName` 
fields present, thus functioning as object locators rather than full objects.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target_object** | Optional[OntologyObjectV2] | No |  |
**link_type** | Optional[LinkTypeApiName] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
