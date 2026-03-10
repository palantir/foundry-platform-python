# CommitSubscriberOffsetsRequest

CommitSubscriberOffsetsRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**view_rid** | Optional[ViewRid] | No | The view RID to commit offsets for. If not provided, uses the latest view for the dataset/branch.  |
**offsets** | PartitionOffsets | Yes | The last processed offset for each partition. The server will store these as read positions (offset + 1), so the next read starts after the committed offset.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
