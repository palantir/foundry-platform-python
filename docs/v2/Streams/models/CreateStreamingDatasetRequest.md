# CreateStreamingDatasetRequest

CreateStreamingDatasetRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**name** | DatasetName | Yes |  |
**parent_folder_rid** | FolderRid | Yes |  |
**schema_** | StreamSchema | Yes | The Foundry schema to apply to the new stream.  |
**branch_name** | Optional[BranchName] | No | The branch to create the initial stream on. If not specified, the default branch will be used ('master' for most enrollments).  |
**partitions_count** | Optional[PartitionsCount] | No | The number of partitions for the Foundry stream.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  If not specified, 1 partition is used.  This value cannot be changed later.  |
**stream_type** | Optional[StreamType] | No | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  |
**compressed** | Optional[Compressed] | No | Whether or not compression is enabled for the stream. Defaults to false.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
