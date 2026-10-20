# ResolvedInputOntologySchemaMigrationPolicy

Acknowledgements permitting automatic migrations of Ontology edits during installation or upgrade.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**allow_cast_migrations** | bool | Yes | Allow casting property edits, or dropping those edits when a safe cast is unavailable. |
**allow_drop_migrations** | bool | Yes | Allow dropping property edits. |
**allow_permanently_delete_migrations** | Optional[bool] | No | Allow permanently deleting all edits following a primary key change. Omission does not acknowledge this migration. |
**allow_rename_data_source_migrations** | Optional[bool] | No | Allow moving data source edits. Omission does not acknowledge this migration. |
**allow_rename_property_migrations** | Optional[bool] | No | Allow moving property edits, or dropping them when the move cannot be applied. Omission does not acknowledge this migration. |
**type** | Literal["ontologySchemaMigrationPolicy"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
