# InterfaceTypeDict

Represents an interface type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | InterfaceTypeRid | Yes |  |
**apiName** | InterfaceTypeApiName | Yes |  |
**displayName** | core_models.DisplayName | Yes |  |
**description** | typing_extensions.NotRequired[str] | No | The description of the interface. |
**properties** | typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyTypeDict] | Yes | A map from a shared property type API name to the corresponding shared property type. The map describes the  set of properties the interface has. A shared property type must be unique across all of the properties.  |
**allProperties** | typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyTypeDict] | Yes | A map from a shared property type API name to the corresponding shared property type. The map describes the  set of properties the interface has, including properties from all directly and indirectly extended  interfaces.  |
**extendsInterfaces** | typing.List[InterfaceTypeApiName] | Yes | A list of interface API names that this interface extends. An interface can extend other interfaces to  inherit their properties.  |
**allExtendsInterfaces** | typing.List[InterfaceTypeApiName] | Yes | A list of interface API names that this interface extends, both directly and indirectly.  |
**implementedByObjectTypes** | typing.List[ObjectTypeApiName] | Yes | A list of object API names that implement this interface.  |
**links** | typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkTypeDict] | Yes | A map from an interface link type API name to the corresponding interface link type. The map describes the set of link types the interface has.  |
**allLinks** | typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkTypeDict] | Yes | A map from an interface link type API name to the corresponding interface link type. The map describes the set of link types the interface has, including links from all directly and indirectly extended interfaces.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
