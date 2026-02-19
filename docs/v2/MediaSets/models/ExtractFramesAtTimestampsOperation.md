# ExtractFramesAtTimestampsOperation

Extracts frames from the video at specified timestamps.
If only one dimension is specified, the other is calculated to preserve aspect ratio.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**height** | Optional[int] | No | The desired height in pixels. |
**width** | Optional[int] | No | The desired width in pixels. |
**timestamp** | float | Yes | The timestamp in seconds. |
**type** | Literal["extractFramesAtTimestamps"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
