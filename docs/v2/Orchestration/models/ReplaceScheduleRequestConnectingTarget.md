# ReplaceScheduleRequestConnectingTarget

ReplaceScheduleRequestConnectingTarget

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**ignored_rids** | typing.Optional[typing.List[BuildableRid]] | No | The datasets between the input datasets and target datasets to exclude. |
**target_rids** | typing.List[BuildableRid] | Yes | The downstream target datasets (inclusive). |
**input_rids** | typing.List[BuildableRid] | Yes | The upstream input datasets (exclusive). |
**type** | typing.Literal["connecting"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
