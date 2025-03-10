# RestConnectionConfigurationDict

The configuration needed to connect to a [REST external system](/docs/foundry/available-connectors/rest-apis).

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**domains** | typing.List[DomainDict] | Yes | The domains that the connection is allowed to access. At least one domain must be specified.  |
**additionalSecrets** | typing_extensions.NotRequired[RestConnectionAdditionalSecretsDict] | No | Additional secrets that can be referenced in code and webhook configurations. If not provided, no additional secrets will be created.  |
**oauth2ClientRid** | typing_extensions.NotRequired[core.RID] | No | The RID of the [Outbound application](/docs/foundry/administration/configure-outbound-applications) that is used to authenticate to the external system via OAuth2. Currently, a connection may use only one outbound application for OAuth 2.0 authentication. Selecting a different outbound application will update the configuration for all domains with OAuth 2.0 as the selected authorization.  |
**type** | typing.Literal["rest"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
