# CreateOrganizationRequest

CreateOrganizationRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**administrators** | List[PrincipalId] | Yes | The initial administrators of the Organization. At least one principal must be provided.  |
**enrollment_rid** | EnrollmentRid | Yes | The RID of the Enrollment that this Organization belongs to. This must be provided.  |
**name** | OrganizationName | Yes |  |
**host** | Optional[HostName] | No | The primary host name of the Organization. This should be used when constructing URLs for users of this Organization.  |
**description** | Optional[str] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
