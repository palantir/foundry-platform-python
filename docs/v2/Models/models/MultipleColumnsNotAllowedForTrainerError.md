# MultipleColumnsNotAllowedForTrainerError

Multiple columns were mapped but the trainer only allows a single column for this spec.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**dataset_rid** | DatasetRid | Yes | The RID of the dataset with multiple columns mapped. |
**column_type_spec_id** | ColumnTypeSpecId | Yes | The column type spec ID that does not allow multiple columns. |
**type** | Literal["multipleColumnsNotAllowedForTrainer"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
