# Resource

Resource

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | ResourceRid | Yes |  |
**display_name** | ResourceDisplayName | Yes | The display name of the Resource |
**description** | Optional[StrictStr] | No | The description of the Resource |
**documentation** | Optional[StrictStr] | No | The documentation associated with the Resource |
**path** | ResourcePath | Yes | The full path to the resource, including the resource name itself |
**type** | ResourceType | Yes | The type of the Resource derived from the Resource Identifier (RID). |
**created_by** | CreatedBy | Yes | The user that created the Resource. |
**updated_by** | UpdatedBy | Yes | The user that last updated the Resource. |
**created_time** | CreatedTime | Yes | The timestamp that the Resource was last created. |
**updated_time** | UpdatedTime | Yes | The timestamp that the Resource was last modified. For folders, this includes any of its descendants. For top level folders (spaces and projects), this is not updated by child updates for performance reasons.  |
**trashed** | TrashedStatus | Yes | The trash status of the resource. If trashed, a resource can either be directly trashed or one of its ancestors can be trashed.  |
**parent_folder_rid** | FolderRid | Yes | The parent folder Resource Identifier (RID). For projects, this will be the Space RID. |
**project_rid** | ProjectRid | Yes | The Project Resource Identifier (RID) that the Resource lives in. If the Resource itself is a Project, this value will still be populated with the Project RID.  |
**space_rid** | SpaceRid | Yes | The Space Resource Identifier (RID) that the Resource lives in.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
