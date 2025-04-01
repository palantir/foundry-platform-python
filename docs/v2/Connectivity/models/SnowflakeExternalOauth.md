# SnowflakeExternalOauth

Use an External OAuth security integration to connect and authenticate to Snowflake.

See https://docs.snowflake.com/en/user-guide/oauth-ext-custom


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**audience** | str | Yes | Identifies the recipients that the access token is intended for as a string URI. |
**issuer_url** | str | Yes | Identifies the principal that issued the access token as a string URI. |
**subject** | ConnectionRid | Yes | The RID of the Connection that is connecting to the external system. |
**type** | Literal["externalOauth"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
