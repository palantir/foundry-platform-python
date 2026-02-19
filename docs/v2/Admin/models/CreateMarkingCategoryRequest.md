# CreateMarkingCategoryRequest

CreateMarkingCategoryRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**initial_permissions** | MarkingCategoryPermissions | Yes | The initial permissions for the Marking Category. This can be changed later through MarkingCategoryPermission operations. The provided permissions must include at least one ADMINISTER role assignment.  WARNING: If you do not list your own principal ID or the ID of a Group that you are a member of as an ADMINISTER, you will create a Marking Category that you cannot administer.  |
**name** | MarkingCategoryName | Yes |  |
**description** | MarkingCategoryDescription | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
