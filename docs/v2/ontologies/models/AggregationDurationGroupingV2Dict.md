# AggregationDurationGroupingV2Dict

Divides objects into groups according to an interval. Note that this grouping applies only on date and timestamp types.
When grouping by `YEARS`, `QUARTERS`, `MONTHS`, or `WEEKS`, the `value` must be set to `1`.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | PropertyApiName | Yes |  |
**value** | pydantic.StrictInt | Yes |  |
**unit** | TimeUnit | Yes |  |
**type** | Literal["duration"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
