# S3ProxyConfiguration

S3ProxyConfiguration

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**host** | str | Yes | Domain name, IPv4, or IPv6 address.  `protocol` and `port` must be specified separately.  |
**port** | int | Yes |  |
**non_proxy_hosts** | typing.Optional[typing.List[str]] | No | A list of hosts that can bypass the proxy, such as those used for STS Role. You can also use "*" wildcards. |
**protocol** | typing.Optional[Protocol] | No | If defined, must be "HTTP" or "HTTPS". Defaults to "HTTPS".  |
**credentials** | typing.Optional[BasicCredentials] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
