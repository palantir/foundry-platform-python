# CreateConnectionRequestJdbcConnectionConfiguration

CreateConnectionRequestJdbcConnectionConfiguration

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**credentials** | Optional[BasicCredentials] | No |  |
**driver_class** | str | Yes | The fully-qualified driver class name that is used to connect to the database. |
**jdbc_properties** | Dict[str, str] | Yes | A map of [properties](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Properties.html) passed  to the JDBC driver to configure behavior. Refer to the documentation of your specific connection type for additional  available JDBC properties to add to your connection configuration.  |
**url** | str | Yes | The URL that the JDBC driver uses to connect to a database. |
**type** | Literal["jdbc"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
