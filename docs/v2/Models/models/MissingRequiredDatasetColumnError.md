# MissingRequiredDatasetColumnError

The user-provided dataset is missing a column required by the trainer.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**dataset_rid** | RID | Yes | The RID of the dataset missing the required column. |
**column_type_spec_id** | ColumnTypeSpecId | Yes | The trainer column type spec ID for the required column. |
**column_names** | List[ColumnName] | Yes | The valid dataset column names that could map to this trainer column. |
**type** | Literal["missingRequiredDatasetColumn"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
