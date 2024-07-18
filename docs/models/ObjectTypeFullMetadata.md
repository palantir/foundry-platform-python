# ObjectTypeFullMetadata

ObjectTypeFullMetadata

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**implements_interfaces** | List[InterfaceTypeApiName] | Yes | A list of interfaces that this object type implements. |
**implements_interfaces2** | Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementation] | Yes | A list of interfaces that this object type implements and how it implements them. |
**link_types** | List[LinkTypeSideV2] | Yes |  |
**object_type** | ObjectTypeV2 | Yes |  |
**shared_property_type_mapping** | Dict[SharedPropertyTypeApiName, PropertyApiName] | Yes | A map from shared property type API name to backing local property API name for the shared property types  present on this object type.  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
