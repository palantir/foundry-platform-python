# InterfaceType

Represents an interface type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | InterfaceTypeRid | Yes |  |
**api_name** | InterfaceTypeApiName | Yes |  |
**display_name** | core_models.DisplayName | Yes |  |
**description** | typing.Optional[str] | No | The description of the interface. |
**properties** | typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType] | Yes | A map from a shared property type API name to the corresponding shared property type. The map describes the  set of properties the interface has. A shared property type must be unique across all of the properties.  |
**all_properties** | typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType] | Yes | A map from a shared property type API name to the corresponding shared property type. The map describes the  set of properties the interface has, including properties from all directly and indirectly extended  interfaces.  |
**extends_interfaces** | typing.List[InterfaceTypeApiName] | Yes | A list of interface API names that this interface extends. An interface can extend other interfaces to  inherit their properties.  |
**all_extends_interfaces** | typing.List[InterfaceTypeApiName] | Yes | A list of interface API names that this interface extends, both directly and indirectly.  |
**implemented_by_object_types** | typing.List[ObjectTypeApiName] | Yes | A list of object API names that implement this interface.  |
**links** | typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkType] | Yes | A map from an interface link type API name to the corresponding interface link type. The map describes the set of link types the interface has.  |
**all_links** | typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkType] | Yes | A map from an interface link type API name to the corresponding interface link type. The map describes the set of link types the interface has, including links from all directly and indirectly extended interfaces.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
