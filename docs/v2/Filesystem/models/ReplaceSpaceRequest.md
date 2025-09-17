# ReplaceSpaceRequest

ReplaceSpaceRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**usage_account_rid** | Optional[UsageAccountRid] | No | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used. |
**display_name** | ResourceDisplayName | Yes |  |
**description** | Optional[str] | No | The description of the Space. |
**default_role_set_id** | Optional[RoleSetId] | No | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
