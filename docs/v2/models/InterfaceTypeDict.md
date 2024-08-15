# InterfaceTypeDict

Represents an interface type in the Ontology.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | InterfaceTypeRid | Yes |  |
**apiName** | InterfaceTypeApiName | Yes |  |
**displayName** | DisplayName | Yes |  |
**description** | NotRequired[StrictStr] | No | The description of the interface. |
**properties** | Dict[SharedPropertyTypeApiName, SharedPropertyTypeDict] | Yes | A map from a shared property type API name to the corresponding shared property type. The map describes the  set of properties the interface has. A shared property type must be unique across all of the properties.  |
**extendsInterfaces** | List[InterfaceTypeApiName] | Yes | A list of interface API names that this interface extends. An interface can extend other interfaces to  inherit their properties.  |
**links** | Dict[InterfaceLinkTypeApiName, InterfaceLinkTypeDict] | Yes | A map from an interface link type API name to the corresponding interface link type. The map describes the set of link types the interface has.  |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
