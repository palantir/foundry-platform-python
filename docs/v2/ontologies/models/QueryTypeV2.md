# QueryTypeV2

Represents a query type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | QueryApiName | Yes |  |
**description** | Optional[pydantic.StrictStr] | No |  |
**display_name** | Optional[DisplayName] | No |  |
**parameters** | Dict[ParameterId, QueryParameterV2] | Yes |  |
**output** | QueryDataType | Yes |  |
**rid** | FunctionRid | Yes |  |
**version** | FunctionVersion | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
