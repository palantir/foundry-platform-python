# ExactDistinctAggregationV2Dict

Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation. Requires Object Storage V2.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | PropertyApiName | Yes |  |
**name** | NotRequired[AggregationMetricName] | No |  |
**direction** | NotRequired[OrderByDirection] | No |  |
**type** | Literal["exactDistinct"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to README]](../../../README.md)
