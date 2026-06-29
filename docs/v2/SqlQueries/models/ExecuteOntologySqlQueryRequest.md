# ExecuteOntologySqlQueryRequest

ExecuteOntologySqlQueryRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**query** | str | Yes | The SQL query to execute.  |
**parameters** | Optional[Parameters] | No | Parameters for the SQL query. Can be either unnamed positional parameters or a named parameter mapping.  |
**row_limit** | Optional[int] | No | Maximum number of rows to return.  |
**dry_run** | Optional[bool] | No | If true, parse and validate the query without executing it. Defaults to false.  |
**branch** | Optional[FoundryBranch] | No | The Foundry branch to execute the query against. If not specified, the default (main) branch is used.  |
**scenario_rid** | Optional[ScenarioRid] | No | The scenario to evaluate the query against. If not specified, no scenario is applied.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
