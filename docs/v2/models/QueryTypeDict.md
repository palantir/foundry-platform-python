# QueryTypeDict

Represents a query type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | QueryApiName | Yes |  |
**description** | NotRequired[StrictStr] | No |  |
**displayName** | NotRequired[DisplayName] | No |  |
**parameters** | Dict[ParameterId, ParameterDict] | Yes |  |
**output** | NotRequired[OntologyDataTypeDict] | No |  |
**rid** | FunctionRid | Yes |  |
**version** | FunctionVersion | Yes |  |


[[Back to Model list]](../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
