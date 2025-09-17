# CreateMarkingRequest

CreateMarkingRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**initial_role_assignments** | List[MarkingRoleUpdate] | Yes | The initial roles that will be assigned when the Marking is created. At least one ADMIN role must be provided. This can be changed later through the MarkingRoleAssignment operations.  WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer.  |
**initial_members** | List[PrincipalId] | Yes | Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations.  |
**name** | MarkingName | Yes |  |
**description** | Optional[str] | No |  |
**category_id** | MarkingCategoryId | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
