# ObjectTypeV2Dict

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ObjectTypeApiName | Yes |  |
**displayName** | core_models.DisplayName | Yes |  |
**status** | core_models.ReleaseStatus | Yes |  |
**description** | typing_extensions.NotRequired[str] | No | The description of the object type. |
**pluralDisplayName** | str | Yes | The plural display name of the object type. |
**icon** | IconDict | Yes |  |
**primaryKey** | PropertyApiName | Yes |  |
**properties** | typing.Dict[PropertyApiName, PropertyV2Dict] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |
**titleProperty** | PropertyApiName | Yes |  |
**visibility** | typing_extensions.NotRequired[ObjectTypeVisibility] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
