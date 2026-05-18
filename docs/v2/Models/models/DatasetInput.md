# DatasetInput

Dataset input configuration.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes | The RID of the input dataset. |
**column_mapping** | Dict[ColumnTypeSpecId, List[ColumnName]] | Yes | Mapping of column type spec IDs to column names. |
**ignore_columns** | List[ColumnName] | Yes | Columns to ignore from the dataset. |
**select_columns** | List[ColumnName] | Yes | Columns to select from the dataset. If empty, all columns not in ignoreColumns will be used. |
**type** | Literal["dataset"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
