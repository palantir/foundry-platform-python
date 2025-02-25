# ApiKeyAuthentication

The API key used to authenticate to the external system.
This can be configured as a header or query parameter.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**location** | RestRequestApiKeyLocation | Yes | The location of the API key in the request. |
**api_key** | EncryptedProperty | Yes | The value of the API key. |
**type** | Literal["apiKey"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
