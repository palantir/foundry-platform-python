# TableImportDict

TableImport

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | TableImportRid | Yes |  |
**connectionRid** | ConnectionRid | Yes | The RID of the Connection (also known as a source) that the Table Import uses to import data. |
**datasetRid** | datasets_models.DatasetRid | Yes | The RID of the output dataset. |
**branchName** | typing_extensions.NotRequired[datasets_models.BranchName] | No | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. |
**displayName** | TableImportDisplayName | Yes |  |
**importMode** | TableImportMode | Yes |  |
**allowSchemaChanges** | TableImportAllowSchemaChanges | Yes | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. |
**config** | TableImportConfigDict | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
