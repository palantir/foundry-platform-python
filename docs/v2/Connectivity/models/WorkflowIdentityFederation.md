# WorkflowIdentityFederation

Authenticate as a service principal using workload identity federation. This is the recommended way to connect to Databricks. 
Workload identity federation allows workloads running in Foundry to access Databricks APIs without the need for Databricks secrets. 
Refer to our [OIDC documentation](https://palantir.com/docs/foundry/data-connection/oidc) for an overview of how OpenID Connect is supported in Foundry.
A service principal federation policy must exist in Databricks to allow Foundry to act as an identity provider. 
Refer to the [official documentation](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation) for guidance.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**service_principal_application_id** | Optional[str] | No | The ID of the Databricks [service principal](https://docs.databricks.com/aws/en/admin/users-groups/service-principals).  If provided, a federated JWT token is exchanged using a service principal federation policy. If not provided, a federated JWT token is exchanged using an account federation policy.  |
**issuer_url** | str | Yes | Identifies the principal that issued the access token as a string URI. |
**audience** | str | Yes | Identifies the recipients that the access token is intended for as a string URI.  This should be the primary host name where the Connection lives.  |
**subject** | ConnectionRid | Yes | The RID of the Connection that is connecting to the external system. |
**type** | Literal["workflowIdentityFederation"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
