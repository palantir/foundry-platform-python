# Resource

Resource

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**display_name** | str | Yes | The display name of the Resource |
**description** | Optional[str] | No | The description of the Resource |
**documentation** | Optional[str] | No | The documentation associated with the Resource |
**path** | str | Yes | The full path to the resource, including the resource name itself |
**type** | ResourceType | Yes | The type of the Resource derived from the Resource Identifier (RID). |
**created_by** | str | Yes | The user that created the Resource. |
**updated_by** | UUID | Yes | The user that last updated the Resource. |
**created_time** | datetime | Yes | The timestamp that the Resource was last created. |
**updated_time** | datetime | Yes | The timestamp that the Resource was last modified. For folders, this includes any of its descendants. For top level folders (spaces and projects), this is not updated by child updates for performance reasons.  |
**trash_status** | TrashStatus | Yes | The trash status of the Resource. If trashed, this could either be because the Resource itself has been trashed or because one of its ancestors has been trashed.  |
**parent_folder_rid** | RID | Yes | The parent folder Resource Identifier (RID). For projects, this will be the Space RID. |
**project_rid** | RID | Yes | The Project Resource Identifier (RID) that the Resource lives in. If the Resource itself is a Project, this value will still be populated with the Project RID.  |
**space_rid** | RID | Yes | The Space Resource Identifier (RID) that the Resource lives in.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
