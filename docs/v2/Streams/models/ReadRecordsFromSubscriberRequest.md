# ReadRecordsFromSubscriberRequest

ReadRecordsFromSubscriberRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**view_rid** | Optional[ViewRid] | No | The view RID to read from. If not provided, reads from the latest view for the dataset/branch.  |
**limit** | Optional[int] | No | Maximum number of records to return across all partitions. Defaults to 100, max 1000. If a value  greater than 1000 is requested, only 1000 records will be returned.  |
**partition_ids** | Optional[List[PartitionId]] | No | If specified, only read from these partitions. Otherwise, read from all partitions.  |
**auto_commit** | Optional[bool] | No | If true, the read position is automatically committed after reading records. The committed position will be the offset after the last record read. If false, you must call the `commitOffsets` endpoint to commit offsets. Defaults to false.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
