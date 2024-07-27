# ObjectType

Represents an object type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | ObjectTypeApiName | Yes |  |
**display_name** | Optional[DisplayName] | No |  |
**status** | ReleaseStatus | Yes |  |
**description** | Optional[StrictStr] | No | The description of the object type. |
**visibility** | Optional[ObjectTypeVisibility] | No |  |
**primary_key** | List[PropertyApiName] | Yes | The primary key of the object. This is a list of properties that can be used to uniquely identify the object. |
**properties** | Dict[PropertyApiName, Property] | Yes | A map of the properties of the object type. |
**rid** | ObjectTypeRid | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
