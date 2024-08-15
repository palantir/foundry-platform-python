# AggregationDurationGroupingV2

Divides objects into groups according to an interval. Note that this grouping applies only on date and timestamp types.
When grouping by `YEARS`, `QUARTERS`, `MONTHS`, or `WEEKS`, the `value` must be set to `1`.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | PropertyApiName | Yes |  |
**value** | StrictInt | Yes |  |
**unit** | TimeUnit | Yes |  |
**type** | Literal["duration"] | Yes | None |


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)
