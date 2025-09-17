# CreateSpaceRequest

CreateSpaceRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**enrollment_rid** | EnrollmentRid | Yes | The RID of the Enrollment that this Space belongs to.  |
**usage_account_rid** | Optional[UsageAccountRid] | No | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used. |
**file_system_id** | Optional[FileSystemId] | No | The ID of the Filesystem for this Space, which is where the contents of the Space are stored. If not provided, the default Filesystem for this Enrollment will be used. |
**display_name** | ResourceDisplayName | Yes |  |
**organizations** | List[OrganizationRid] | Yes | The list of Organizations that are provisioned access to this Space. In order to access this Space, a user must be a member of at least one of these Organizations.  |
**description** | Optional[str] | No | The description of the Space. |
**deletion_policy_organizations** | List[OrganizationRid] | Yes | By default, this Space will use a Last Out deletion policy, meaning that this Space and its projects will be deleted when the last Organization listed here is deleted. Only Organizations in the Space's Enrollment can be included here.  |
**default_role_set_id** | Optional[RoleSetId] | No | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
