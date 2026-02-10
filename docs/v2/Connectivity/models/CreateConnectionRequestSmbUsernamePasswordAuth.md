# CreateConnectionRequestSmbUsernamePasswordAuth

CreateConnectionRequestSmbUsernamePasswordAuth

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**password** | CreateConnectionRequestEncryptedProperty | Yes |  |
**domain** | Optional[str] | No | Optionally specify a Windows domain to use when authenticating. Normal DNS domain restrictions apply but the top-level domain might be something non-standard like .local. Defaults to WORKGROUP  |
**username** | str | Yes |  |
**type** | Literal["usernamePassword"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
