# AuthenticationProvider

AuthenticationProvider

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | AuthenticationProviderRid | Yes |  |
**name** | AuthenticationProviderName | Yes |  |
**realm** | Realm | Yes |  |
**enabled** | AuthenticationProviderEnabled | Yes | Whether users can log in using this provider. |
**supported_hosts** | List[HostName] | Yes | This provider can only be utilized from these hosts. |
**supported_username_patterns** | List[str] | Yes | Users who enter usernames that match these patterns will be redirected to this authentication provider. |
**protocol** | AuthenticationProtocol | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
