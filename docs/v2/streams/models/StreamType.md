# StreamType

LOW_LATENCY: The default stream type. Recommended for most use cases.

HIGH_THROUGHPUT: Best for streams that send large amounts of data every second. Using this stream type might
introduce some non-zero latency at the expense of a higher throughput. This stream type is only
recommended if you inspect your stream metrics in-platform and observe that the average batch size is equal
to the max match size, or if jobs using the stream are failing due to Kafka producer batches expiring. For
additional information on inspecting stream metrics, refer to the 
(stream monitoring)[/docs/foundry/data-integration/stream-monitoring/#viewing-metrics] documentation.

For more information, refer to the [stream types](/docs/foundry/data-integration/streams/#stream-types)
documentation.


| **Value** |
| --------- |
| `"LOW_LATENCY"` |
| `"HIGH_THROUGHPUT"` |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
