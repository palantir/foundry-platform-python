# Resource

Resource

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ResourceRid | Yes |  |
**display_name** | ResourceDisplayName | Yes | The display name of the resource |
**description** | Optional[str] | No | The description of the resource |
**documentation** | Optional[str] | No | The documentation associated with the resource |
**path** | ResourcePath | Yes | The full path to the resource, including the resource name itself |
**type** | ResourceType | Yes | The type of the resource derived from the Resource Identifier (RID). |
**created_by** | CreatedBy | Yes | The user that created the resource |
**updated_by** | UpdatedBy | Yes | The user that last updated the resource. |
**created_time** | CreatedTime | Yes | The timestamp that the resource was last created. |
**updated_time** | UpdatedTime | Yes | The timestamp that the resource was last modified. For folders, this includes any of its descendants. For top level folders (spaces and projects), this is not updated by child updates for performance reasons.  |
**trash_status** | TrashStatus | Yes | The trash status of the resource. If trashed, this could either be because the resource itself has been trashed or because one of its ancestors has been trashed.  |
**parent_folder_rid** | FolderRid | Yes | The parent folder Resource Identifier (RID). For projects, this will be the Space RID. |
**project_rid** | ProjectRid | Yes | The Project Resource Identifier (RID) that the resource lives in. If the resource itself is a Project, this value will still be populated with the Project RID.  |
**space_rid** | SpaceRid | Yes | The Space Resource Identifier (RID) that the resource lives in.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
