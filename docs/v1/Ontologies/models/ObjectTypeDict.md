# ObjectTypeDict

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | ObjectTypeApiName | Yes |  |
**displayName** | typing_extensions.NotRequired[core_models.DisplayName] | No |  |
**status** | core_models.ReleaseStatus | Yes |  |
**description** | typing_extensions.NotRequired[str] | No | The description of the object type. |
**visibility** | typing_extensions.NotRequired[ObjectTypeVisibility] | No |  |
**primaryKey** | typing.List[PropertyApiName] | Yes | The primary key of the object. This is a list of properties that can be used to uniquely identify the object. |
**properties** | typing.Dict[PropertyApiName, PropertyDict] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
