# ObjectTypeFullMetadata

ObjectTypeFullMetadata

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**object_type** | ObjectTypeV2 | Yes |  |
**link_types** | List[LinkTypeSideV2] | Yes |  |
**implements_interfaces** | List[InterfaceTypeApiName] | Yes | A list of interfaces that this object type implements. |
**implements_interfaces2** | Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementation] | Yes | A list of interfaces that this object type implements and how it implements them. |
**shared_property_type_mapping** | Dict[SharedPropertyTypeApiName, PropertyApiName] | Yes | A map from shared property type API name to backing local property API name for the shared property types  present on this object type.  |


[[Back to Model list]](../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
