# InterfaceLinkType

A link type constraint defined at the interface level where the implementation of the links is provided
by the implementing object types.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | InterfaceLinkTypeRid | Yes |  |
**api_name** | InterfaceLinkTypeApiName | Yes |  |
**display_name** | DisplayName | Yes |  |
**description** | Optional[StrictStr] | No | The description of the interface link type. |
**linked_entity_api_name** | InterfaceLinkTypeLinkedEntityApiName | Yes |  |
**cardinality** | InterfaceLinkTypeCardinality | Yes |  |
**required** | StrictBool | Yes | Whether each implementing object type must declare at least one implementation of this link.  |


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to README]](../../../README.md)