# Project

Project

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**display_name** | str | Yes | The display name of the Project. Must be unique and cannot contain a / |
**description** | Optional[str] | No | The description associated with the Project. |
**documentation** | Optional[str] | No | The documentation associated with the Project. |
**path** | str | Yes |  |
**created_by** | str | Yes |  |
**updated_by** | UUID | Yes |  |
**created_time** | datetime | Yes |  |
**updated_time** | datetime | Yes |  |
**trash_status** | TrashStatus | Yes | The trash status of the Project. |
**space_rid** | RID | Yes | The Space Resource Identifier (RID) that the Project lives in. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
