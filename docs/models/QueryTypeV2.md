# QueryTypeV2

Represents a query type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | QueryApiName | Yes |  |
**description** | Optional[StrictStr] | No |  |
**display_name** | Optional[DisplayName] | No |  |
**output** | QueryDataType | Yes |  |
**parameters** | Dict[ParameterId, QueryParameterV2] | Yes |  |
**rid** | FunctionRid | Yes |  |
**version** | FunctionVersion | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
