# CreateProjectRequest

CreateProjectRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**display_name** | ResourceDisplayName | Yes |  |
**description** | Optional[str] | No |  |
**space_rid** | SpaceRid | Yes |  |
**role_grants** | Dict[RoleId, List[PrincipalWithId]] | Yes |  |
**default_roles** | List[RoleId] | Yes |  |
**organization_rids** | List[OrganizationRid] | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
