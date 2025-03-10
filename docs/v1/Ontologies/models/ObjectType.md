# ObjectType

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | ObjectTypeApiName | Yes |  |
**display_name** | typing.Optional[core_models.DisplayName] | No |  |
**status** | core_models.ReleaseStatus | Yes |  |
**description** | typing.Optional[str] | No | The description of the object type. |
**visibility** | typing.Optional[ObjectTypeVisibility] | No |  |
**primary_key** | typing.List[PropertyApiName] | Yes | The primary key of the object. This is a list of properties that can be used to uniquely identify the object. |
**properties** | typing.Dict[PropertyApiName, Property] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
