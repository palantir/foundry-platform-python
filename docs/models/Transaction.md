# Transaction

An operation that modifies the files within a dataset.


## Properties
Name | Type | Required | Description |
------------ | ------------- | ------------- | ------------- |
**rid** | TransactionRid | Yes | The Resource Identifier (RID) of a Transaction. Example: `ri.foundry.main.transaction.0a0207cb-26b7-415b-bc80-66a3aa3933f4`.  |
**transaction_type** | TransactionType | Yes | The type of a Transaction.  |
**status** | TransactionStatus | Yes | The status of a Transaction.  |
**created_time** | RFC3339DateTime | Yes | The timestamp when the transaction was created, in ISO 8601 timestamp format. |
**closed_time** | RFC3339DateTime | No | The timestamp when the transaction was closed, in ISO 8601 timestamp format. |


[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
