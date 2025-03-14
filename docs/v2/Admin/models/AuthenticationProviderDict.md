# AuthenticationProviderDict

AuthenticationProvider

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**name** | str | Yes |  |
**realm** | str | Yes |  |
**enabled** | bool | Yes | Whether users can log in using this provider. |
**supportedHosts** | List[HostName] | Yes | This provider can only be utilized from these hosts. |
**supportedUsernamePatterns** | List[str] | Yes | Users who enter usernames that match these patterns will be redirected to this authentication provider. |
**protocol** | AuthenticationProtocolDict | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
