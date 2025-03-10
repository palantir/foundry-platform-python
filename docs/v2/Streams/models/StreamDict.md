# StreamDict

Stream

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**branchName** | BranchName | Yes |  |
**schema_** | StreamSchemaDict | Yes | The Foundry schema for this stream. |
**viewRid** | ViewRid | Yes | The view that this stream corresponds to.  |
**partitionsCount** | PartitionsCount | Yes | The number of partitions for the Foundry stream. Defaults to 1.  Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended.  |
**streamType** | StreamType | Yes | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY.  |
**compressed** | Compressed | Yes | Whether or not compression is enabled for the stream. Defaults to false.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
