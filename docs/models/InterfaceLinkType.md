# InterfaceLinkType

A link type constraint defined at the interface level where the implementation of the links is provided
by the implementing object types.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**api_name** | InterfaceLinkTypeApiName | Yes |  |
**cardinality** | InterfaceLinkTypeCardinality | Yes |  |
**description** | Optional[StrictStr] | No | The description of the interface link type. |
**display_name** | DisplayName | Yes |  |
**linked_entity_api_name** | InterfaceLinkTypeLinkedEntityApiName | Yes |  |
**required** | StrictBool | Yes | Whether each implementing object type must declare at least one implementation of this link.  |
**rid** | InterfaceLinkTypeRid | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
