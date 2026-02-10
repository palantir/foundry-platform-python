# Domain

The domain that the connection is allowed to access.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**scheme** | Optional[UriScheme] | No | The scheme of the domain that the connection is allowed to access. If not specified, defaults to HTTPS.  |
**host** | str | Yes | The domain name, IPv4, or IPv6 address. |
**port** | Optional[int] | No | The port number of the domain that the connection is allowed to access. |
**auth** | Optional[RestAuthenticationMode] | No | The URI scheme must be HTTPS if using any authentication. If not specified, no authentication is required.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
