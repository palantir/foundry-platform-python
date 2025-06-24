# CreateConnectionRequestDatabricksConnectionConfiguration

CreateConnectionRequestDatabricksConnectionConfiguration

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**host_name** | str | Yes | The hostname of the Databricks workspace. |
**http_path** | str | Yes | The Databricks compute resource’s HTTP Path value. |
**jdbc_properties** | JdbcProperties | Yes |  |
**authentication** | CreateConnectionRequestDatabricksAuthenticationMode | Yes | The method of authentication to use.  |
**type** | Literal["databricks"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
