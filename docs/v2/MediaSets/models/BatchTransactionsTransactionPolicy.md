# BatchTransactionsTransactionPolicy

All writes must be part of a transaction. Transactions are branch-scoped and created by calling
create transaction. Writes are not visible until commit transaction is called.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**type** | Literal["batchTransactions"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
