# Space

A Foundry space.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**default_role_set_id** | RoleSetId | Yes | The ID of the default role set for this space, which defines the set of roles that projects in this space must use. |
**deletion_policy_organization_rids** | List[OrganizationRid] | Yes | By default, this space will use a Last Out deletion policy, meaning that this space and its projects will be deleted when the last organization listed here is deleted. Only organizations in the space's enrollment can be included here. |
**description** | Optional[str] | No | The description of the space. Empty if no description is configured. |
**display_name** | DisplayName | Yes | The display name of the space. Must be unique and cannot contain a `/`. |
**file_system_id** | Optional[FileSystemId] | No | The ID of the filesystem for this space, which is where the contents of the space are stored. This field may be absent for legacy resources. |
**maven_identifier** | Optional[MavenIdentifier] | No | The Maven identifier used as the prefix to the maven coordinate that uniquely identifies resources published from this space. Only present if previously configured. |
**organization_rids** | List[OrganizationRid] | Yes | The list of organizations that are provisioned access to this space. To access this space, a user must be a member of at least one of these organizations. |
**path** | ResourcePath | Yes | The full path to the resource, including the resource name itself. |
**rid** | SpaceRid | Yes |  |
**usage_account_rid** | Optional[UsageAccountRid] | No | The RID of the usage account for this space. Resource usage for projects in this space will accrue to this usage account by default. This field may be absent for legacy resources. |
**type** | Literal["value"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
