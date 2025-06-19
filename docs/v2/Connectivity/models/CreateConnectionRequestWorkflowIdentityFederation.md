# CreateConnectionRequestWorkflowIdentityFederation

CreateConnectionRequestWorkflowIdentityFederation

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**audience** | str | Yes | Identifies the recipients that the access token is intended for as a string URI.  This should be the primary host name where the Connection lives.  |
**service_principal_application_id** | Optional[str] | No | The ID of the Databricks [service principal](https://docs.databricks.com/aws/en/admin/users-groups/service-principals).  If provided, a federated JWT token is exchanged using a service principal federation policy. If not provided, a federated JWT token is exchanged using an account federation policy.  |
**type** | Literal["workflowIdentityFederation"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
