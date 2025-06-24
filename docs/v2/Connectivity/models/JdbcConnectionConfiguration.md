# JdbcConnectionConfiguration

The configuration needed to connect to an external system using the JDBC protocol.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**url** | str | Yes | The URL that the JDBC driver uses to connect to a database. |
**driver_class** | str | Yes | The fully-qualified driver class name that is used to connect to the database. |
**jdbc_properties** | JdbcProperties | Yes |  |
**credentials** | Optional[BasicCredentials] | No |  |
**type** | Literal["jdbc"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
