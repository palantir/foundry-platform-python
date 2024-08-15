# Transaction

An operation that modifies the files within a dataset.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | TransactionRid | Yes |  |
**transaction_type** | TransactionType | Yes |  |
**status** | TransactionStatus | Yes |  |
**created_time** | datetime | Yes | The timestamp when the transaction was created, in ISO 8601 timestamp format. |
**closed_time** | Optional[datetime] | No | The timestamp when the transaction was closed, in ISO 8601 timestamp format. |


[[Back to Model list]](../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
