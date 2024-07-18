# ObjectTypeFullMetadataDict

ObjectTypeFullMetadata

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**implementsInterfaces** | List[InterfaceTypeApiName] | Yes | A list of interfaces that this object type implements. |
**implementsInterfaces2** | Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementationDict] | Yes | A list of interfaces that this object type implements and how it implements them. |
**linkTypes** | List[LinkTypeSideV2Dict] | Yes |  |
**objectType** | ObjectTypeV2Dict | Yes |  |
**sharedPropertyTypeMapping** | Dict[SharedPropertyTypeApiName, PropertyApiName] | Yes | A map from shared property type API name to backing local property API name for the shared property types  present on this object type.  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
