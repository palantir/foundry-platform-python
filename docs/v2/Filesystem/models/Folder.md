# Folder

Folder

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | FolderRid | Yes |  |
**display_name** | ResourceDisplayName | Yes |  |
**description** | typing.Optional[str] | No | The description associated with the Folder. |
**documentation** | typing.Optional[str] | No | The documentation associated with the Folder. |
**path** | ResourcePath | Yes |  |
**type** | FolderType | Yes |  |
**created_by** | core_models.CreatedBy | Yes |  |
**updated_by** | core_models.UpdatedBy | Yes |  |
**created_time** | core_models.CreatedTime | Yes |  |
**updated_time** | core_models.UpdatedTime | Yes |  |
**trash_status** | TrashStatus | Yes | The trash status of the Folder. If trashed, this could either be because the Folder itself has been trashed or because one of its ancestors has been trashed.  |
**parent_folder_rid** | FolderRid | Yes | The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).  |
**project_rid** | typing.Optional[ProjectRid] | No | The Project Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will not be defined.  |
**space_rid** | SpaceRid | Yes | The Space Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will be the same as the Folder RID.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
