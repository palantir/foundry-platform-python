# GetByRidQueriesRequest

GetByRidQueriesRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | FunctionRid | Yes |  |
**version** | Optional[FunctionVersion] | No |  |
**include_prerelease** | Optional[bool] | No | When no version is specified and this flag is set to true, the latest version resolution will consider prerelease versions (e.g., 1.2.3-beta could be returned as the latest). When false, only stable versions are considered when determining the latest version.  Defaults to false.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
