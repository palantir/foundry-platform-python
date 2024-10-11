# QueryTypeDict

Represents a query type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | QueryApiName | Yes |  |
**description** | NotRequired[pydantic.StrictStr] | No |  |
**displayName** | NotRequired[DisplayName] | No |  |
**parameters** | Dict[ParameterId, ParameterDict] | Yes |  |
**output** | NotRequired[OntologyDataTypeDict] | No |  |
**rid** | FunctionRid | Yes |  |
**version** | FunctionVersion | Yes |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
