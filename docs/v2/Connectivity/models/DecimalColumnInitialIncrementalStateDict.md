# DecimalColumnInitialIncrementalStateDict

The state for an incremental table import using a column with a decimal data type.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**columnName** | str | Yes |  |
**currentValue** | decimal.Decimal | Yes | The initial incremental state value for the decimal column to reference in the query.  |
**type** | Literal["decimalColumnInitialIncrementalState"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
