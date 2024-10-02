# FileImport

FileImport

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | FileImportRid | Yes |  |
**connection_rid** | ConnectionRid | Yes | The RID of the Connection (formerly known as a source) that the File Import uses to import data. |
**dataset_rid** | DatasetRid | Yes | The RID of the output dataset. |
**branch_name** | Optional[BranchName] | No | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. |
**display_name** | FileImportDisplayName | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
