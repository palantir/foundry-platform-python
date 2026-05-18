# AggregationExactGroupingV2

Divides objects into groups according to an exact value.
Either `field` or `propertyIdentifier` must be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No |  |
**property_identifier** | Optional[PropertyIdentifier] | No |  |
**max_group_count** | Optional[int] | No | The maximum number of groups to return. If omitted, defaults to 10,000.  The server allocates resources based on the specified `maxGroupCount`. When the number of distinct values in your data is within this limit, results are accurate and the top N values are returned correctly. When distinct values exceed what the allocated resources can handle, results may become approximate.  If you need accurate results with high-cardinality properties, set `maxGroupCount` high enough to cover your distinct values. Items exceeding the limit are excluded from results and counted in `excludedItems`. The response `accuracy` field indicates whether the results are `ACCURATE` or `APPROXIMATE`.  |
**default_value** | Optional[str] | No | Includes a group with the specified default value that includes all objects where the specified field's value is null. Cannot be used with includeNullValues.  |
**include_null_values** | Optional[bool] | No | Includes a group with a null value that includes all objects where the specified field's value is null. Cannot be used with defaultValue or orderBy clauses on the aggregation.  |
**type** | Literal["exact"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
