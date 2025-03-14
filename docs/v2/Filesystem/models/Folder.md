# Folder

Folder

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**display_name** | str | Yes |  |
**description** | Optional[str] | No | The description associated with the Folder. |
**documentation** | Optional[str] | No | The documentation associated with the Folder. |
**path** | str | Yes |  |
**type** | FolderType | Yes |  |
**created_by** | str | Yes |  |
**updated_by** | UUID | Yes |  |
**created_time** | datetime | Yes |  |
**updated_time** | datetime | Yes |  |
**trash_status** | TrashStatus | Yes | The trash status of the Folder. If trashed, this could either be because the Folder itself has been trashed or because one of its ancestors has been trashed.  |
**parent_folder_rid** | RID | Yes | The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).  |
**project_rid** | Optional[ProjectRid] | No | The Project Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will not be defined.  |
**space_rid** | RID | Yes | The Space Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will be the same as the Folder RID.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
