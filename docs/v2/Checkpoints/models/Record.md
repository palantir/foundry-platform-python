# Record

Record

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RecordRid | Yes |  |
**config_rid** | Optional[ConfigRid] | No |  |
**type** | CheckpointType | Yes |  |
**scope** | Scope | Yes |  |
**acting_user** | ActingUser | Yes |  |
**delegate_user_id** | Optional[UserId] | No |  |
**created_at** | RecordCreatedAt | Yes |  |
**checkpointed_items** | List[CheckpointedItem] | Yes |  |
**justification** | Justification | Yes |  |
**project_rid** | Optional[ProjectRid] | No |  |
**organization_rid** | Optional[OrganizationRid] | No |  |
**namespace_rid** | Optional[NamespaceRid] | No |  |
**interaction_rid** | Optional[InteractionRid] | No |  |
**approvals_metadata** | Optional[ApprovalsMetadata] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
