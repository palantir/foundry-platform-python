# RelativeDateRangeQuery

Returns objects where the specified date or timestamp property falls within a relative date range.
The bounds are calculated relative to query execution time and rounded to midnight in the specified timezone.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No | The property API name to filter on (either field or propertyIdentifier must be provided). |
**property_identifier** | Optional[PropertyIdentifier] | No | The property identifier to filter on (either field or propertyIdentifier must be provided). |
**relative_start_time** | Optional[RelativeDateRangeBound] | No | The lower bound relative to query time (inclusive). Negative values go into the past. For example, { value: -7, timeUnit: DAY } means 7 days ago.  |
**relative_end_time** | Optional[RelativeDateRangeBound] | No | The upper bound relative to query time (exclusive). Negative values go into the past. For example, { value: 1, timeUnit: MONTH } means the start of next month.  |
**time_zone_id** | str | Yes | Time zone ID for midnight calculation (e.g., "America/New_York", "Europe/London", "Etc/UTC"). See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid values.  |
**type** | Literal["relativeDateRange"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
