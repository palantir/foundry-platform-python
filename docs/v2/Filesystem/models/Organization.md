# Organization

[Organizations](/docs/foundry/security/orgs-and-spaces/#organizations) are access requirements applied to 
Projects that enforce strict silos between groups of users and resources. Every user is a member of only 
one Organization, but can be a guest member of multiple Organizations. In order to meet access requirements, 
users must be a member or guest member of at least one Organization applied to a Project.
Organizations are inherited via the file hierarchy and direct dependencies.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**marking_id** | core_models.MarkingId | Yes |  |
**organization_rid** | core_models.OrganizationRid | Yes |  |
**is_directly_applied** | IsDirectlyApplied | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
