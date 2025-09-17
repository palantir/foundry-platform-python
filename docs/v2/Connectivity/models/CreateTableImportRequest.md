# CreateTableImportRequest

CreateTableImportRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | Yes | The RID of the output dataset. Can not be modified after the table import is created. |
**import_mode** | TableImportMode | Yes |  |
**display_name** | TableImportDisplayName | Yes |  |
**allow_schema_changes** | Optional[TableImportAllowSchemaChanges] | No | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. |
**branch_name** | Optional[BranchName] | No | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. Can not be modified after the table import is created. |
**config** | CreateTableImportRequestTableImportConfig | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
