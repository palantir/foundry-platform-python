# ApproximatePercentileAggregationV2

Computes the approximate percentile value for the provided field. Requires Object Storage V2.
Either `field` or `propertyIdentifier` must be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No |  |
**property_identifier** | Optional[PropertyIdentifier] | No |  |
**name** | Optional[AggregationMetricName] | No |  |
**approximate_percentile** | float | Yes |  |
**direction** | Optional[OrderByDirection] | No |  |
**type** | Literal["approximatePercentile"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
