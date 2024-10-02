# FileImportDict

FileImport

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | FileImportRid | Yes |  |
**connectionRid** | ConnectionRid | Yes | The RID of the Connection (formerly known as a source) that the File Import uses to import data. |
**datasetRid** | DatasetRid | Yes | The RID of the output dataset. |
**branchName** | NotRequired[BranchName] | No | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. |
**displayName** | FileImportDisplayName | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
