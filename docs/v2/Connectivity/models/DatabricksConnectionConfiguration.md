# DatabricksConnectionConfiguration

The configuration needed to connect to a [Databricks external system](https://palantir.com/docs/foundry/available-connectors/databricks).
Refer to the [official Databricks documentation](https://docs.databricks.com/aws/en/integrations/compute-details) 
for more information on how to obtain connection details for your system.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**host_name** | str | Yes | The hostname of the Databricks workspace. |
**http_path** | str | Yes | The Databricks compute resource’s HTTP Path value. |
**authentication** | DatabricksAuthenticationMode | Yes | The method of authentication to use.  |
**jdbc_properties** | JdbcProperties | Yes |  |
**type** | Literal["databricks"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
