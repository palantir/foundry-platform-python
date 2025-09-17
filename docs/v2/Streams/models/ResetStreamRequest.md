# ResetStreamRequest

ResetStreamRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**schema_** | Optional[StreamSchema] | No | The Foundry schema to apply to the new stream.   If omitted, the schema of the existing stream on the branch will be used.  |
**partitions_count** | Optional[PartitionsCount] | No | The number of partitions for the Foundry stream. Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If omitted, the partitions count of the existing stream on the branch will be used.  |
**stream_type** | Optional[StreamType] | No | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  If omitted, the stream type of the existing stream on the branch will be used.  |
**compressed** | Optional[Compressed] | No | Whether or not compression is enabled for the stream.  If omitted, the compression setting of the existing stream on the branch will be used.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
