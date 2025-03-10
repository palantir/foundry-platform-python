# JdbcImportConfigDict

The import configuration for a [custom JDBC connection](docs/foundry/available-connectors/custom-jdbc-sources).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**query** | str | Yes | A single SQL query can be executed per sync, which should output a data table  and avoid operations like invoking stored procedures.  The query results are saved to the output dataset in Foundry.  |
**type** | typing.Literal["jdbcImportConfig"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
