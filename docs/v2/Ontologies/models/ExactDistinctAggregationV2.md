# ExactDistinctAggregationV2

Computes an exact number of distinct values for the provided field. May be slower than an approximate
distinct aggregation. Requires Object Storage V2.
Either `field` or `propertyIdentifier` must be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No |  |
**property_identifier** | Optional[PropertyIdentifier] | No |  |
**name** | Optional[AggregationMetricName] | No |  |
**direction** | Optional[OrderByDirection] | No |  |
**type** | Literal["exactDistinct"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
