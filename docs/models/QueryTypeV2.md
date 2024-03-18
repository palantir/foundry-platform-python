# QueryTypeV2

Represents a query type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | QueryApiName | Yes | The name of the Query in the API.  |
**description** | StrictStr | No | None |
**display_name** | DisplayName | No | The display name of the entity. |
**parameters** | Dict[str, QueryParameterV2] | No | None |
**output** | QueryDataType | Yes | A union of all the types supported by Ontology Query parameters or outputs.  |
**rid** | FunctionRid | Yes | The unique resource identifier of a Function, useful for interacting with other Foundry APIs.  |
**version** | FunctionVersion | Yes | The version of the given Function, written `<major>.<minor>.<patch>-<tag>`, where `-<tag>` is optional. Examples: `1.2.3`, `1.2.3-rc1`.  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
