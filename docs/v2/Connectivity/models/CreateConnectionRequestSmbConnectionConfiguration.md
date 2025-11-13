# CreateConnectionRequestSmbConnectionConfiguration

CreateConnectionRequestSmbConnectionConfiguration

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**proxy** | Optional[SmbProxyConfiguration] | No |  |
**hostname** | str | Yes | Any identifier that can resolve to a server hosting an SMB share. This includes IP addresses, local  network names (e.g. FS-SERVER-01) or FQDNs. Should not include any protocol information like https://, smb://, etc  |
**port** | Optional[int] | No | 445 by default |
**auth** | CreateConnectionRequestSmbAuth | Yes |  |
**share** | str | Yes | Must be a valid SMB share name. https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/dc9978d7-6299-4c5a-a22d-a039cdc716ea  |
**base_directory** | Optional[str] | No | All reads and writes in this source will happen in this subdirectory |
**require_message_signing** | Optional[bool] | No | If true, the client will request that the server sign all messages. If the server does not support  message signing, the connection will fail. Defaults to true. |
**type** | Literal["smb"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
