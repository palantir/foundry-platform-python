# Space

Space

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | SpaceRid | Yes |  |
**display_name** | ResourceDisplayName | Yes |  |
**description** | Optional[str] | No | The description of the Space. |
**path** | ResourcePath | Yes |  |
**file_system_id** | FileSystemId | Yes | The ID of the Filesystem for this Space, which is where the contents of the Space are stored. If not provided, the default Filesystem for this Enrollment will be used. |
**usage_account_rid** | UsageAccountRid | Yes | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used. |
**organizations** | List[OrganizationRid] | Yes | The list of Organizations that are provisioned access to this Space. In order to access this Space, a user must be a member of at least one of these Organizations.  |
**deletion_policy_organizations** | List[OrganizationRid] | Yes | By default, this Space will use a Last Out deletion policy, meaning that this Space and its projects will be deleted when the last Organization listed here is deleted. Only Organizations in the Space's Enrollment can be included here.  |
**default_role_set_id** | RoleSetId | Yes | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used.  |
**space_maven_identifier** | Optional[SpaceMavenIdentifier] | No | The maven identifier used as the prefix to the maven coordinate that uniquely identifies resources published from this space. This is only present if configured in control panel in the space settings.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
