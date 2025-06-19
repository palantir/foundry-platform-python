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
**jdbc_properties** | Dict[str, str] | Yes | A map of [properties](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Properties.html) passed  to the JDBC driver to configure behavior. Refer to the documentation of your specific connection type for additional  available JDBC properties to add to your connection configuration. This should only contain unencrypted properties, all values specified here are sent unencrypted to Foundry.  |
**type** | Literal["databricks"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
