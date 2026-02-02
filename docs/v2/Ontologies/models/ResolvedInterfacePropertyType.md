# ResolvedInterfacePropertyType

An interface property type with additional fields to indicate constraints that need to be satisfied by
implementing object property types.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | InterfacePropertyTypeRid | Yes |  |
**api_name** | InterfacePropertyApiName | Yes |  |
**display_name** | DisplayName | Yes |  |
**description** | Optional[str] | No | A short text that describes the InterfacePropertyType. |
**data_type** | ObjectPropertyType | Yes |  |
**value_type_api_name** | Optional[ValueTypeApiName] | No |  |
**value_formatting** | Optional[PropertyValueFormattingRule] | No |  |
**require_implementation** | bool | Yes | Whether each implementing object type must declare an implementation for this property.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
