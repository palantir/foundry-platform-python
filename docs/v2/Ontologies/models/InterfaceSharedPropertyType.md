# InterfaceSharedPropertyType

A shared property type with an additional field to indicate whether the property must be included on every
object type that implements the interface, or whether it is optional.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | SharedPropertyTypeRid | Yes |  |
**api_name** | SharedPropertyTypeApiName | Yes |  |
**display_name** | DisplayName | Yes |  |
**description** | Optional[str] | No | A short text that describes the SharedPropertyType. |
**data_type** | ObjectPropertyType | Yes |  |
**value_type_api_name** | Optional[ValueTypeApiName] | No |  |
**value_formatting** | Optional[PropertyValueFormattingRule] | No |  |
**required** | bool | Yes | Whether each implementing object type must declare an implementation for this property.  |
**type_classes** | Optional[List[TypeClass]] | No |  |
**type** | Literal["interfaceSharedPropertyType"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
