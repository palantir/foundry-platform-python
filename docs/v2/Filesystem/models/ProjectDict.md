# ProjectDict

Project

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**displayName** | str | Yes | The display name of the Project. Must be unique and cannot contain a / |
**description** | NotRequired[str] | No | The description associated with the Project. |
**documentation** | NotRequired[str] | No | The documentation associated with the Project. |
**path** | str | Yes |  |
**createdBy** | str | Yes |  |
**updatedBy** | UUID | Yes |  |
**createdTime** | datetime | Yes |  |
**updatedTime** | datetime | Yes |  |
**trashStatus** | TrashStatus | Yes | The trash status of the Project. |
**spaceRid** | RID | Yes | The Space Resource Identifier (RID) that the Project lives in. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
