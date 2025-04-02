# TableImportInitialIncrementalState

The incremental configuration for a table import enables append-style transactions from the same table without duplication of data.
You must provide a monotonically increasing column such as a timestamp or id and an initial value for this column. 
An incremental table import will import rows where the value is greater than the largest already imported.

You can use the '?' character to reference the incremental state value when constructing your query. 
Normally this would be used in a WHERE clause or similar filter applied in order to only sync data with an incremental column value 
larger than the previously observed maximum value stored in the incremental state.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
StringColumnInitialIncrementalState | stringColumnInitialIncrementalState
DateColumnInitialIncrementalState | dateColumnInitialIncrementalState
IntegerColumnInitialIncrementalState | integerColumnInitialIncrementalState
TimestampColumnInitialIncrementalState | timestampColumnInitialIncrementalState
LongColumnInitialIncrementalState | longColumnInitialIncrementalState
DecimalColumnInitialIncrementalState | decimalColumnInitialIncrementalState


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
