# ObjectTypeV2

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | str | Yes |  |
**display_name** | str | Yes |  |
**status** | ReleaseStatus | Yes |  |
**description** | Optional[str] | No | The description of the object type. |
**plural_display_name** | str | Yes | The plural display name of the object type. |
**icon** | BlueprintIcon | Yes |  |
**primary_key** | str | Yes |  |
**properties** | Dict[PropertyApiName, PropertyV2] | Yes | A map of the properties of the object type. |
**rid** | RID | Yes |  |
**title_property** | str | Yes |  |
**visibility** | Optional[ObjectTypeVisibility] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
