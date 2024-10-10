# FolderDict

Folder

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | FolderRid | Yes |  |
**displayName** | ResourceDisplayName | Yes |  |
**description** | NotRequired[pydantic.StrictStr] | No | The description associated with the Folder. |
**documentation** | NotRequired[pydantic.StrictStr] | No | The documentation associated with the Folder. |
**path** | ResourcePath | Yes |  |
**type** | FolderType | Yes |  |
**createdBy** | CreatedBy | Yes |  |
**updatedBy** | UpdatedBy | Yes |  |
**createdTime** | CreatedTime | Yes |  |
**updatedTime** | UpdatedTime | Yes |  |
**trashStatus** | TrashStatus | Yes | The trash status of the Folder. If trashed, this could either be because the Folder itself has been trashed or because one of its ancestors has been trashed.  |
**parentFolderRid** | FolderRid | Yes | The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).  |
**projectRid** | NotRequired[ProjectRid] | No | The Project Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will not be defined.  |
**spaceRid** | SpaceRid | Yes | The Space Resource Identifier (RID) that the Folder lives in. If the Folder is a Space, this value will be the same as the Folder RID.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
