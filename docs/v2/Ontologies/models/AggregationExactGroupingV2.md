# AggregationExactGroupingV2

Divides objects into groups according to an exact value.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | PropertyApiName | Yes |  |
**max_group_count** | Optional[int] | No |  |
**default_value** | Optional[str] | No | Includes a group with the specified default value that includes all objects where the specified field's value is null. Cannot be used with includeNullValues.  |
**include_null_values** | Optional[bool] | No | Includes a group with a null value that includes all objects where the specified field's value is null. Cannot be used with defaultValue or orderBy clauses on the aggregation.  |
**type** | Literal["exact"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
