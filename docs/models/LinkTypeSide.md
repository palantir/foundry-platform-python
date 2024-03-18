# LinkTypeSide

LinkTypeSide

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | LinkTypeApiName | Yes | The name of the link type in the API. To find the API name for your Link Type, check the **Ontology Manager** application.  |
**display_name** | DisplayName | Yes | The display name of the entity. |
**status** | ReleaseStatus | Yes | The release status of the entity. |
**object_type_api_name** | ObjectTypeApiName | Yes | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the `List object types` endpoint or check the **Ontology Manager**.  |
**cardinality** | LinkTypeSideCardinality | Yes | LinkTypeSideCardinality |
**foreign_key_property_api_name** | PropertyApiName | No | The name of the property in the API. To find the API name for your property, use the `Get object type` endpoint or check the **Ontology Manager**.  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
