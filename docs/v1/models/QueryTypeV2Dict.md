# QueryTypeV2Dict

Represents a query type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | QueryApiName | Yes |  |
**description** | NotRequired[StrictStr] | No |  |
**displayName** | NotRequired[DisplayName] | No |  |
**parameters** | Dict[ParameterId, QueryParameterV2Dict] | Yes |  |
**output** | QueryDataTypeDict | Yes |  |
**rid** | FunctionRid | Yes |  |
**version** | FunctionVersion | Yes |  |


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
