# SelectedPropertyCollectSetAggregationDict

Lists all distinct values of a property up to the specified limit. The maximum supported limit is 100.

NOTE: A separate cardinality / exactCardinality aggregation should be used to determine the total count of
values, to account for a possible truncation of the returned set.

Ignores objects for which a property is absent, so the returned list will contain non-null values only.
Returns an empty list when none of the objects have values for a provided property.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**selectedPropertyApiName** | str | Yes |  |
**limit** | int | Yes | Maximum number of values to collect. The maximum supported limit is 100.  |
**type** | Literal["collectSet"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
