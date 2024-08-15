# ConnectingTarget

All datasets between the input datasets (exclusive) and the
target datasets (inclusive) except for the datasets to ignore.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**input_dataset_rids** | List[DatasetRid] | Yes | The upstream input datasets (exclusive). |
**target_dataset_rids** | List[DatasetRid] | Yes | The downstream target datasets (inclusive). |
**ignored_dataset_rids** | List[DatasetRid] | Yes | The datasets between the input datasets and target datasets to exclude. |
**type** | Literal["connecting"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
