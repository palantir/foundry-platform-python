# UpstreamTarget

Target the specified datasets along with all upstream datasets except the ignored datasets.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target_rids** | typing.List[BuildableRid] | Yes | The target datasets. |
**ignored_rids** | typing.List[BuildableRid] | Yes | The datasets to ignore when calculating the final set of dataset to build. |
**type** | typing.Literal["upstream"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
