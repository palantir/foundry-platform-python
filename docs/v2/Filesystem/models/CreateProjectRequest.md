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
**resource_level_role_grants_allowed** | Optional[bool] | No | Whether role grants should be allowed on individual resources within the Project. When not specified, defaults to true.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
