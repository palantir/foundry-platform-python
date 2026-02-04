# PublishRecordsToStreamRequest

PublishRecordsToStreamRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**records** | List[Record] | Yes | The records to publish to the stream  |
**view_rid** | Optional[ViewRid] | No | If provided, this endpoint will only write to the stream corresponding to the specified view RID. If not provided, this endpoint will write to the latest stream on the branch.  Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
