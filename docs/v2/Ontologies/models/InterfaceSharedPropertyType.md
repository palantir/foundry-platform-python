# InterfaceSharedPropertyType

A shared property type with an additional field to indicate whether the property must be included on every
object type that implements the interface, or whether it is optional.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**api_name** | str | Yes |  |
**display_name** | str | Yes |  |
**description** | Optional[str] | No | A short text that describes the SharedPropertyType. |
**data_type** | ObjectPropertyType | Yes |  |
**required** | bool | Yes | Whether each implementing object type must declare an implementation for this property.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
