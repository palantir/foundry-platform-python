# ObjectTypeV2Dict

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ObjectTypeApiName | Yes |  |
**displayName** | DisplayName | Yes |  |
**status** | ReleaseStatus | Yes |  |
**description** | NotRequired[StrictStr] | No | The description of the object type. |
**pluralDisplayName** | StrictStr | Yes | The plural display name of the object type. |
**icon** | IconDict | Yes |  |
**primaryKey** | PropertyApiName | Yes |  |
**properties** | Dict[PropertyApiName, PropertyV2Dict] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |
**titleProperty** | PropertyApiName | Yes |  |
**visibility** | NotRequired[ObjectTypeVisibility] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
