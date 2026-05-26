# AggregateObjectSetRequestV2

AggregateObjectSetRequestV2

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**aggregation** | List[AggregationV2] | Yes |  |
**object_set** | ObjectSet | Yes |  |
**group_by** | List[AggregationGroupByV2] | Yes |  |
**accuracy** | Optional[AggregationAccuracyRequest] | No |  |
**include_compute_usage** | Optional[IncludeComputeUsage] | No |  |
**execute_in_memory_only** | Optional[bool] | No | If true, the request fails with an error when it cannot be computed in-memory. Use this to opt into fast failure on requests that would otherwise require heavier computation.  Defaults to false.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
