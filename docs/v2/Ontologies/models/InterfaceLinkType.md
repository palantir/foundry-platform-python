# InterfaceLinkType

A link type constraint defined at the interface level where the implementation of the links is provided
by the implementing object types.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**api_name** | str | Yes |  |
**display_name** | str | Yes |  |
**description** | Optional[str] | No | The description of the interface link type. |
**linked_entity_api_name** | InterfaceLinkTypeLinkedEntityApiName | Yes |  |
**cardinality** | InterfaceLinkTypeCardinality | Yes |  |
**required** | bool | Yes | Whether each implementing object type must declare at least one implementation of this link.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
