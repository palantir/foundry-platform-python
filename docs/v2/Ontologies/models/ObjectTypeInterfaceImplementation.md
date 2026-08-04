# ObjectTypeInterfaceImplementation

ObjectTypeInterfaceImplementation

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | Optional[InterfaceTypeApiName] | No |  |
**rid** | Optional[InterfaceTypeRid] | No |  |
**properties** | Dict[SharedPropertyTypeApiName, PropertyApiName] | Yes |  |
**properties_v2** | Dict[InterfacePropertyApiName, InterfacePropertyTypeImplementation] | Yes |  |
**links** | Dict[InterfaceLinkTypeApiName, List[LinkTypeApiName]] | Yes |  |
**action_types** | Dict[InterfaceActionTypeConstraintApiName, ActionTypeApiName] | Yes | A map from interface action type constraint API name to the API name of the concrete action type on this object type that implements it. Action types the caller is not authorized to access are omitted, so this map may not cover every action type constraint declared on the interface.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
