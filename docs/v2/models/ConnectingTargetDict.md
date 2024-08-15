# ConnectingTargetDict

All datasets between the input datasets (exclusive) and the
target datasets (inclusive) except for the datasets to ignore.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**inputDatasetRids** | List[DatasetRid] | Yes | The upstream input datasets (exclusive). |
**targetDatasetRids** | List[DatasetRid] | Yes | The downstream target datasets (inclusive). |
**ignoredDatasetRids** | List[DatasetRid] | Yes | The datasets between the input datasets and target datasets to exclude. |
**type** | Literal["connecting"] | Yes | None |


[[Back to Model list]](../../README.md#models-v2-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
