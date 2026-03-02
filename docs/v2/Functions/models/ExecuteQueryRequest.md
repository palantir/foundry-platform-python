# ExecuteQueryRequest

ExecuteQueryRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**parameters** | Dict[ParameterId, Optional[DataValue]] | Yes |  |
**version** | Optional[FunctionVersion] | No | The version of the query to execute. When used with `branch`, the specified version must exist on the branch.  |
**branch** | Optional[FoundryBranch] | No | The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
