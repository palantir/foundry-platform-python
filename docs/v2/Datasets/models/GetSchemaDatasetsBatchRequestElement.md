# GetSchemaDatasetsBatchRequestElement

GetSchemaDatasetsBatchRequestElement

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**end_transaction_rid** | Optional[TransactionRid] | No | The Resource Identifier (RID) of the end Transaction. If a user does not provide a value, the RID of the latest committed transaction will be used.  |
**dataset_rid** | DatasetRid | Yes |  |
**version_id** | Optional[VersionId] | No | The schema version that should be used. If none is provided, the latest version will be used.  |
**branch_name** | Optional[BranchName] | No |  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
