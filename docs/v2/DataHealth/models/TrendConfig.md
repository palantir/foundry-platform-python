# TrendConfig

Configuration for trend-based validation with severity settings. At least one of trendType or differenceBounds must be specified. Both may be provided to validate both the trend pattern and the magnitude of change.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**trend_type** | Optional[TrendType] | No |  |
**difference_bounds** | Optional[NumericBounds] | No |  |
**severity** | SeverityLevel | Yes |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
