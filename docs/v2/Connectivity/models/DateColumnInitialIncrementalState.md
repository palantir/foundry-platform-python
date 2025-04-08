# DateColumnInitialIncrementalState

The state for an incremental table import using a column with a date type.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**column_name** | str | Yes |  |
**current_value** | date | Yes | The initial incremental state value for the date column to reference in the query.  |
**type** | Literal["dateColumnInitialIncrementalState"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
