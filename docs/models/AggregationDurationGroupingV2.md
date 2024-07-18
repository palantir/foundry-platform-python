# AggregationDurationGroupingV2

Divides objects into groups according to an interval. Note that this grouping applies only on date and timestamp types.
When grouping by `YEARS`, `QUARTERS`, `MONTHS`, or `WEEKS`, the `value` must be set to `1`.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | PropertyApiName | Yes |  |
**unit** | TimeUnit | Yes |  |
**value** | StrictInt | Yes |  |
**type** | Literal["duration"] | Yes | None |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
