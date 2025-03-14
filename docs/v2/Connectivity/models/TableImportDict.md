# TableImportDict

TableImport

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**connectionRid** | RID | Yes | The RID of the Connection (also known as a source) that the Table Import uses to import data. |
**datasetRid** | RID | Yes | The RID of the output dataset. |
**branchName** | NotRequired[BranchName] | No | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. |
**displayName** | str | Yes |  |
**importMode** | TableImportMode | Yes |  |
**allowSchemaChanges** | bool | Yes | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. |
**config** | TableImportConfigDict | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
