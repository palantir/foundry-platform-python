# Project

A Foundry project.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**created_time** | Optional[CreatedTime] | No | The timestamp when the project was created. This field may be absent for legacy projects. |
**created_user_id** | Optional[UserId] | No | The ID of the user that created the project. This field may be absent for legacy projects. |
**description** | Optional[str] | No | The description of the project. Empty if no description is configured. |
**display_name** | DisplayName | Yes | The display name of the project. Must be unique and cannot contain a `/`. |
**documentation** | Optional[str] | No | The long-form, markdown-formatted documentation of the project. Empty if no documentation is configured, or the caller does not have permission to view it. |
**path** | ResourcePath | Yes | The full path to the project, including the project name itself. |
**resource_level_role_grants_allowed** | bool | Yes | Whether role grants are allowed on individual resources within the project. |
**rid** | ProjectRid | Yes |  |
**space_rid** | SpaceRid | Yes | The RID of the space that contains the project. |
**trash_status** | TrashStatus | Yes | The trash status of the project. |
**updated_time** | Optional[UpdatedTime] | No | The timestamp when the project was last modified. This field may be absent for legacy projects. |
**updated_user_id** | Optional[UserId] | No | The ID of the user that last modified the project. This field may be absent for legacy projects. |
**type** | Literal["value"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
