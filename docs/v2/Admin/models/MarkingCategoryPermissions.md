# MarkingCategoryPermissions

MarkingCategoryPermissions

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**organization_rids** | List[OrganizationRid] | Yes | Users must be members of at least one of the Organizations in this list to view Markings in the category, regardless of their assigned roles. |
**roles** | List[MarkingCategoryRoleAssignment] | Yes |  |
**is_public** | MarkingCategoryPermissionsIsPublic | Yes | If true, all users who are members of at least one of the Organizations from organizationRids can view the Markings in the category. If false, only users who are explicitly granted the VIEW role can view the Markings in the category. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
