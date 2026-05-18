# ExecuteSqlQueryRequest

ExecuteSqlQueryRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**query** | str | Yes | The SQL query to execute. Queries should conform to the [Spark SQL dialect](https://spark.apache.org/docs/latest/sql-ref.html). This supports SELECT queries only. Datasets can be referenced in SQL queries by path or by RID. See the  [documentation](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets) for more details.  |
**fallback_branch_ids** | Optional[List[BranchName]] | No | The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments.  |
**serialization_format** | Optional[SerializationFormat] | No | The format used to serialize query results. If not specified, defaults to `ARROW`.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
