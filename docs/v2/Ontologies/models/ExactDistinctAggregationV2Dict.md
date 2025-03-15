# ExactDistinctAggregationV2Dict

Computes an exact number of distinct values for the provided field. May be slower than an approximate distinct aggregation. Requires Object Storage V2.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | PropertyApiName | Yes |  |
**name** | NotRequired[AggregationMetricName] | No |  |
**direction** | NotRequired[OrderByDirection] | No |  |
**type** | Literal["exactDistinct"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
