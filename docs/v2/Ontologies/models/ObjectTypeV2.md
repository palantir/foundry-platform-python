# ObjectTypeV2

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | ObjectTypeApiName | Yes |  |
**display_name** | core_models.DisplayName | Yes |  |
**status** | core_models.ReleaseStatus | Yes |  |
**description** | typing.Optional[str] | No | The description of the object type. |
**plural_display_name** | str | Yes | The plural display name of the object type. |
**icon** | Icon | Yes |  |
**primary_key** | PropertyApiName | Yes |  |
**properties** | typing.Dict[PropertyApiName, PropertyV2] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |
**title_property** | PropertyApiName | Yes |  |
**visibility** | typing.Optional[ObjectTypeVisibility] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
