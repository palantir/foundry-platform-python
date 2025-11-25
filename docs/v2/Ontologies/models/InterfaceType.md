# InterfaceType

Represents an interface type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | InterfaceTypeRid | Yes |  |
**api_name** | InterfaceTypeApiName | Yes |  |
**display_name** | DisplayName | Yes |  |
**description** | Optional[str] | No | The description of the interface. |
**properties** | Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType] | Yes | A map from a shared property type API name to the corresponding shared property type. The map describes the  set of properties the interface has. A shared property type must be unique across all of the properties. This field only includes properties on the interface that are backed by shared property types.  |
**all_properties** | Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType] | Yes | A map from a shared property type API name to the corresponding shared property type. The map describes the  set of properties the interface has, including properties from all directly and indirectly extended  interfaces. This field only includes properties on the interface that are backed by shared property types.  |
**properties_v2** | Dict[InterfacePropertyApiName, InterfacePropertyType] | Yes | A map from a interface property type API name to the corresponding interface property type. The map describes the set of properties the interface has. An interface property can either be backed by a shared property or it can be defined directly on the interface.  |
**all_properties_v2** | Dict[InterfacePropertyApiName, ResolvedInterfacePropertyType] | Yes | A map from a interface property type API name to the corresponding interface property type. The map describes the set of properties the interface has, including properties from all directly and indirectly extended interfaces.  |
**extends_interfaces** | List[InterfaceTypeApiName] | Yes | A list of interface API names that this interface extends. An interface can extend other interfaces to  inherit their properties.  |
**all_extends_interfaces** | List[InterfaceTypeApiName] | Yes | A list of interface API names that this interface extends, both directly and indirectly.  |
**implemented_by_object_types** | List[ObjectTypeApiName] | Yes | A list of object API names that implement this interface.  |
**links** | Dict[InterfaceLinkTypeApiName, InterfaceLinkType] | Yes | A map from an interface link type API name to the corresponding interface link type. The map describes the set of link types the interface has.  |
**all_links** | Dict[InterfaceLinkTypeApiName, InterfaceLinkType] | Yes | A map from an interface link type API name to the corresponding interface link type. The map describes the set of link types the interface has, including links from all directly and indirectly extended interfaces.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
