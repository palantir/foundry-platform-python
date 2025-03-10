# ObjectSetParameterValueDict

A value passed for `ObjectSetParameter` application variable types.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**objectSet** | ontologies_models.ObjectSetDict | Yes |  |
**ontology** | ontologies_models.OntologyIdentifier | Yes | The API name of the Ontology for the provided `ObjectSet`. To find the API name, use the `List ontologies` endpoint or check the [Ontology Manager](/docs/foundry/ontology-manager/overview/).  |
**type** | typing.Literal["objectSet"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
