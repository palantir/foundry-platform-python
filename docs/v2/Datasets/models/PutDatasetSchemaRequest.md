# PutDatasetSchemaRequest

PutDatasetSchemaRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**branch_name** | Optional[BranchName] | No |  |
**dataframe_reader** | Optional[DataframeReader] | No | The dataframe reader used for reading the dataset schema. Defaults to PARQUET. |
**end_transaction_rid** | Optional[TransactionRid] | No | The Resource Identifier (RID) of the end Transaction.  |
**schema_** | DatasetSchema | Yes | The schema that will be added.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
