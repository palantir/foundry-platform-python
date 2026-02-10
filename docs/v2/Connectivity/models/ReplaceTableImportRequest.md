# ReplaceTableImportRequest

ReplaceTableImportRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**import_mode** | TableImportMode | Yes |  |
**display_name** | TableImportDisplayName | Yes |  |
**allow_schema_changes** | Optional[TableImportAllowSchemaChanges] | No | Allow the TableImport to succeed if the schema of imported rows does not match the existing dataset's schema. Defaults to false for new table imports. |
**config** | ReplaceTableImportRequestTableImportConfig | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
