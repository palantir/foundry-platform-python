# Folder

A Foundry folder within a project.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**additional_fields** | AdditionalFields | Yes | Optional properties. Only the additional fields explicitly requested by the caller are populated. |
**created_time** | Optional[CreatedTime] | No | The timestamp when the folder was created. This field may be absent for legacy folders. |
**created_user_id** | Optional[UserId] | No | The ID of the user that created the folder. This field may be absent for legacy folders. |
**display_name** | DisplayName | Yes | The display name of the folder. |
**rid** | FolderRid | Yes |  |
**updated_time** | Optional[UpdatedTime] | No | The timestamp when the folder was last modified. This field may be absent for legacy folders. |
**updated_user_id** | Optional[UserId] | No | The ID of the user that last modified the folder. This field may be absent for legacy folders. |
**type** | Literal["value"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
