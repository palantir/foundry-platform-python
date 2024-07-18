# ObjectTypeDict

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ObjectTypeApiName | Yes |  |
**description** | NotRequired[StrictStr] | No | The description of the object type. |
**displayName** | NotRequired[DisplayName] | No |  |
**primaryKey** | List[PropertyApiName] | Yes | The primary key of the object. This is a list of properties that can be used to uniquely identify the object. |
**properties** | Dict[PropertyApiName, PropertyDict] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |
**status** | ReleaseStatus | Yes |  |
**visibility** | NotRequired[ObjectTypeVisibility] | No |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
