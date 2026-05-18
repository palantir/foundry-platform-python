# Subscriber

Subscriber

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**subscriber_id** | SubscriberId | Yes |  |
**read_position** | Optional[ReadPosition] | No | Where to start reading from. Defaults to `earliest` if not specified.  The `readPosition` determines where the subscriber will start reading: - `earliest`: Start from the beginning of each partition (offset 0). Use this to process   all historical data. - `latest`: Start from the current end of each partition. Use this to skip historical data   and only process new records arriving after registration. - `specific`: Start from explicit offsets for each partition. Use this to resume from a   known checkpoint.  |
**dataset_rid** | DatasetRid | Yes | The RID of the dataset the subscriber is bound to. |
**branch_name** | BranchName | Yes | The branch of the stream the subscriber is bound to. |
**view_rid** | ViewRid | Yes | The current view RID being read from. This may change over time if the stream's schema is migrated to a new view.  |
**start_offsets** | PartitionOffsets | Yes | The offsets where reading began for each partition, based on the initial read position.  |
**created_time** | CreatedTime | Yes | Timestamp when the subscriber was registered. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
