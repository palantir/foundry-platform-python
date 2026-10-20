# PipelineReplayOptionResetAndReplayFromOffset

Reset the pipeline with data received before the specified offset time.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**acknowledgement** | Optional[ReplayAcknowledgement] | No | Confirms the replay choice. If omitted, this choice is unacknowledged and will not be applied. |
**offset_millis** | Long | Yes | The replay offset time in milliseconds. Encoded as a decimal-integer string; must be between -9007199254740991 and 9007199254740991, inclusive. |
**type** | Literal["resetAndReplayFromOffset"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
