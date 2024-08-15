# ObjectTypeFullMetadataDict

ObjectTypeFullMetadata

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**objectType** | ObjectTypeV2Dict | Yes |  |
**linkTypes** | List[LinkTypeSideV2Dict] | Yes |  |
**implementsInterfaces** | List[InterfaceTypeApiName] | Yes | A list of interfaces that this object type implements. |
**implementsInterfaces2** | Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementationDict] | Yes | A list of interfaces that this object type implements and how it implements them. |
**sharedPropertyTypeMapping** | Dict[SharedPropertyTypeApiName, PropertyApiName] | Yes | A map from shared property type API name to backing local property API name for the shared property types  present on this object type.  |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
