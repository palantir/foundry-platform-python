# ApproximatePercentileAggregationV2

Computes the approximate percentile value for the provided field. Requires Object Storage V2.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | PropertyApiName | Yes |  |
**name** | typing.Optional[AggregationMetricName] | No |  |
**approximate_percentile** | float | Yes |  |
**direction** | typing.Optional[OrderByDirection] | No |  |
**type** | typing.Literal["approximatePercentile"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
