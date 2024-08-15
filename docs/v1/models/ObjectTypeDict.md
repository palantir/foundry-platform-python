# ObjectTypeDict

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ObjectTypeApiName | Yes |  |
**displayName** | NotRequired[DisplayName] | No |  |
**status** | ReleaseStatus | Yes |  |
**description** | NotRequired[StrictStr] | No | The description of the object type. |
**visibility** | NotRequired[ObjectTypeVisibility] | No |  |
**primaryKey** | List[PropertyApiName] | Yes | The primary key of the object. This is a list of properties that can be used to uniquely identify the object. |
**properties** | Dict[PropertyApiName, PropertyDict] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |


[[Back to Model list]](../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
