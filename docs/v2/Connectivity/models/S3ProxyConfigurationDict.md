# S3ProxyConfigurationDict

S3ProxyConfiguration

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**host** | str | Yes | Domain name, IPv4, or IPv6 address.  `protocol` and `port` must be specified separately.  |
**port** | int | Yes |  |
**nonProxyHosts** | NotRequired[List[str]] | No | A list of hosts that can bypass the proxy, such as those used for STS Role. You can also use "*" wildcards. |
**protocol** | NotRequired[Protocol] | No | If defined, must be "HTTP" or "HTTPS". Defaults to "HTTPS".  |
**credentials** | NotRequired[BasicCredentialsDict] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
