# CreateConnectionRequestRestConnectionConfiguration

CreateConnectionRequestRestConnectionConfiguration

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**additional_secrets** | CreateConnectionRequestRestConnectionAdditionalSecrets | Yes | Additional secrets that can be referenced in code and webhook configurations. |
**oauth2_client_rid** | Optional[RID] | No | The RID of the [Outbound application](/docs/foundry/administration/configure-outbound-applications) that is used to authenticate to the external system via OAuth2. Currently, a connection may use only one outbound application for OAuth 2.0 authentication. Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization.  |
**domains** | List[Domain] | Yes | The domains that the connection is allowed to access. At least one domain must be specified.  |
**type** | Literal["rest"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
