# OauthMachineToMachineAuth

Authenticate as a service principal using OAuth. Create a service principal in Databricks and generate an OAuth secret to obtain a client ID and secret.
Read the [official Databricks documentation](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) for more information about OAuth machine-to-machine 
authentication.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**client_id** | str | Yes | The client ID for the service principal. |
**client_secret** | EncryptedProperty | Yes | The value of the client secret. |
**type** | Literal["oauthM2M"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
