# ObjectTypeV2

Represents an object type in the Ontology.

## Properties
Name | Type | Required | Description |
------------ | ------------- | ------------- | ------------- |
**api_name** | ObjectTypeApiName | Yes | The name of the object type in the API in camelCase format. To find the API name for your Object Type, use the `List object types` endpoint or check the **Ontology Manager**.  |
**display_name** | DisplayName | No | The display name of the entity. |
**status** | ReleaseStatus | Yes | The release status of the entity. |
**description** | StrictStr | No | The description of the object type. |
**primary_key** | PropertyApiName | Yes | The name of the property in the API. To find the API name for your property, use the `Get object type` endpoint or check the **Ontology Manager**.  |
**properties** | Dict[str, PropertyV2] | No | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes | The unique resource identifier of an object type, useful for interacting with other Foundry APIs. |
**visibility** | ObjectTypeVisibility | No | The suggested visibility of the object type. |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
