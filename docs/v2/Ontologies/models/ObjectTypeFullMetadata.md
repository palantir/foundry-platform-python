# ObjectTypeFullMetadata

ObjectTypeFullMetadata

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**object_type** | ObjectTypeV2 | Yes |  |
**link_types** | typing.List[LinkTypeSideV2] | Yes |  |
**implements_interfaces** | typing.List[InterfaceTypeApiName] | Yes | A list of interfaces that this object type implements. |
**implements_interfaces2** | typing.Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementation] | Yes | A list of interfaces that this object type implements and how it implements them. |
**shared_property_type_mapping** | typing.Dict[SharedPropertyTypeApiName, PropertyApiName] | Yes | A map from shared property type API name to backing local property API name for the shared property types  present on this object type.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
