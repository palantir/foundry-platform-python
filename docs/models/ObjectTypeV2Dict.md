# ObjectTypeV2Dict

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ObjectTypeApiName | Yes |  |
**displayName** | NotRequired[DisplayName] | No |  |
**status** | ReleaseStatus | Yes |  |
**description** | NotRequired[StrictStr] | No | The description of the object type. |
**primaryKey** | PropertyApiName | Yes |  |
**properties** | Dict[PropertyApiName, PropertyV2Dict] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |
**titleProperty** | PropertyApiName | Yes |  |
**visibility** | NotRequired[ObjectTypeVisibility] | No |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)