# InterfaceDefinedPropertyType

An interface property type with an additional field to indicate constraints that need to be satisfied by
implementing object property types.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | InterfacePropertyTypeRid | Yes |  |
**api_name** | InterfacePropertyApiName | Yes |  |
**display_name** | DisplayName | Yes |  |
**description** | Optional[str] | No | The description of the interface property type. |
**data_type** | ObjectPropertyType | Yes |  |
**value_type_api_name** | Optional[ValueTypeApiName] | No |  |
**require_implementation** | bool | Yes | Whether each implementing object type must declare an implementation for this property.  |
**type_classes** | List[TypeClass] | Yes |  |
**type** | Literal["interfaceDefinedPropertyType"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
