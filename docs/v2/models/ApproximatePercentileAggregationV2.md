# ApproximatePercentileAggregationV2

Computes the approximate percentile value for the provided field. Requires Object Storage V2.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | PropertyApiName | Yes |  |
**name** | Optional[AggregationMetricName] | No |  |
**approximate_percentile** | StrictFloat | Yes |  |
**direction** | Optional[OrderByDirection] | No |  |
**type** | Literal["approximatePercentile"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v2-link) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to README]](../../../README.md)
