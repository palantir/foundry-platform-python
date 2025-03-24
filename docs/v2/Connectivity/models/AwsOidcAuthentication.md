# AwsOidcAuthentication

[OpenID Connect (OIDC)](/docs/foundry/data-connection/oidc/) is an open authentication protocol that allows 
you to authenticate to external system resources without the use of static credentials.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**audience** | str | Yes | The configured audience that identifies the external system. |
**issuer_url** | str | Yes | The URL that identifies Foundry as an OIDC identity provider. |
**subject** | ConnectionRid | Yes | The RID of the Connection that is connecting to the external system. |
**type** | Literal["oidc"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
