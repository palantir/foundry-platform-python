# IntegerColumnInitialIncrementalState

The state for an incremental table import using a numeric integer datatype.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**column_name** | str | Yes |  |
**current_value** | int | Yes | The initial incremental state value for the integer column to reference in the query.  |
**type** | Literal["integerColumnInitialIncrementalState"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
