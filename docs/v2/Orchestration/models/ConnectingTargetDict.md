# ConnectingTargetDict

All datasets between the input datasets (exclusive) and the
target datasets (inclusive) except for the datasets to ignore.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**inputRids** | List[BuildableRid] | Yes | The upstream input datasets (exclusive). |
**targetRids** | List[BuildableRid] | Yes | The downstream target datasets (inclusive). |
**ignoredRids** | List[BuildableRid] | Yes | The datasets between the input datasets and target datasets to exclude. |
**type** | Literal["connecting"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
