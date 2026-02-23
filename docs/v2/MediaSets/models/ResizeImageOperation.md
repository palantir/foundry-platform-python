# ResizeImageOperation

Resizes an image to the specified dimensions.
If only one dimension is specified, the other is calculated to preserve aspect ratio.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**height** | Optional[int] | No | The desired height in pixels. |
**width** | Optional[int] | No | The desired width in pixels. |
**auto_orient** | Optional[bool] | No | Whether to automatically orient the image based on EXIF metadata.  |
**type** | Literal["resize"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
