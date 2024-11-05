# Project

Project

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ProjectRid | Yes |  |
**display_name** | ResourceDisplayName | Yes | The display name of the Project. Must be unique and cannot contain a / |
**description** | Optional[pydantic.StrictStr] | No | The description associated with the Project. |
**documentation** | Optional[pydantic.StrictStr] | No | The documentation associated with the Project. |
**path** | ResourcePath | Yes |  |
**created_by** | CreatedBy | Yes |  |
**updated_by** | UpdatedBy | Yes |  |
**created_time** | CreatedTime | Yes |  |
**updated_time** | UpdatedTime | Yes |  |
**trash_status** | TrashStatus | Yes | The trash status of the Project. |
**space_rid** | SpaceRid | Yes | The Space Resource Identifier (RID) that the Project lives in. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
