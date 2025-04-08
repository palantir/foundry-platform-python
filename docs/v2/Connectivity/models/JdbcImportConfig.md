# JdbcImportConfig

The import configuration for a [custom JDBC connection](https://palantir.com/docs/foundry/available-connectors/custom-jdbc-sources).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**query** | TableImportQuery | Yes |  |
**initial_incremental_state** | Optional[TableImportInitialIncrementalState] | No |  |
**type** | Literal["jdbcImportConfig"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
