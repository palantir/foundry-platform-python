# QueryType

Represents a query type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | QueryApiName | Yes |  |
**description** | Optional[pydantic.StrictStr] | No |  |
**display_name** | Optional[DisplayName] | No |  |
**parameters** | Dict[ParameterId, Parameter] | Yes |  |
**output** | Optional[OntologyDataType] | No |  |
**rid** | FunctionRid | Yes |  |
**version** | FunctionVersion | Yes |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
