# CreateScheduleRequestConnectingTargetDict

CreateScheduleRequestConnectingTarget

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**ignoredRids** | typing_extensions.NotRequired[typing.List[BuildableRid]] | No | The datasets between the input datasets and target datasets to exclude. |
**targetRids** | typing.List[BuildableRid] | Yes | The downstream target datasets (inclusive). |
**inputRids** | typing.List[BuildableRid] | Yes | The upstream input datasets (exclusive). |
**type** | typing.Literal["connecting"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
