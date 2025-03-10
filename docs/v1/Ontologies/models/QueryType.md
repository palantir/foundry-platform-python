# QueryType

Represents a query type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | QueryApiName | Yes |  |
**description** | typing.Optional[str] | No |  |
**display_name** | typing.Optional[core_models.DisplayName] | No |  |
**parameters** | typing.Dict[ParameterId, Parameter] | Yes |  |
**output** | typing.Optional[OntologyDataType] | No |  |
**rid** | FunctionRid | Yes |  |
**version** | FunctionVersion | Yes |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
