# TableImport

TableImport

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**connection_rid** | RID | Yes | The RID of the Connection (also known as a source) that the Table Import uses to import data. |
**dataset_rid** | RID | Yes | The RID of the output dataset. |
**branch_name** | Optional[BranchName] | No | The branch name in the output dataset that will contain the imported data. Defaults to `master` for most enrollments. |
**display_name** | str | Yes |  |
**import_mode** | TableImportMode | Yes |  |
**allow_schema_changes** | bool | Yes | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. |
**config** | TableImportConfig | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
