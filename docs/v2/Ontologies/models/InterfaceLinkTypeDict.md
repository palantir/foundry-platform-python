# InterfaceLinkTypeDict

A link type constraint defined at the interface level where the implementation of the links is provided
by the implementing object types.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | InterfaceLinkTypeRid | Yes |  |
**apiName** | InterfaceLinkTypeApiName | Yes |  |
**displayName** | core_models.DisplayName | Yes |  |
**description** | typing_extensions.NotRequired[str] | No | The description of the interface link type. |
**linkedEntityApiName** | InterfaceLinkTypeLinkedEntityApiNameDict | Yes |  |
**cardinality** | InterfaceLinkTypeCardinality | Yes |  |
**required** | bool | Yes | Whether each implementing object type must declare at least one implementation of this link.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
