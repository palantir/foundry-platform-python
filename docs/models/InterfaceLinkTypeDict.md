# InterfaceLinkTypeDict

A link type constraint defined at the interface level where the implementation of the links is provided
by the implementing object types.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**apiName** | InterfaceLinkTypeApiName | Yes |  |
**cardinality** | InterfaceLinkTypeCardinality | Yes |  |
**description** | NotRequired[StrictStr] | No | The description of the interface link type. |
**displayName** | DisplayName | Yes |  |
**linkedEntityApiName** | InterfaceLinkTypeLinkedEntityApiNameDict | Yes |  |
**required** | StrictBool | Yes | Whether each implementing object type must declare at least one implementation of this link.  |
**rid** | InterfaceLinkTypeRid | Yes |  |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
