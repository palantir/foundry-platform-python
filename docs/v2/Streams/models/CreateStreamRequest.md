# CreateStreamRequest

CreateStreamRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**schema_** | CreateStreamRequestStreamSchema | Yes | The Foundry schema for this stream. |
**partitions_count** | Optional[PartitionsCount] | No | The number of partitions for the Foundry stream. Defaults to 1.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  |
**stream_type** | Optional[StreamType] | No | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  |
**branch_name** | BranchName | Yes |  |
**compressed** | Optional[Compressed] | No | Whether or not compression is enabled for the stream. Defaults to false.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
