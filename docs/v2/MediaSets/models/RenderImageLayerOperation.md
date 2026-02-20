# RenderImageLayerOperation

Renders a frame of a DICOM file as an image.
If only one dimension is specified, the other is calculated to preserve aspect ratio.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**layer_number** | Optional[int] | No | The layer number to render. If not specified, renders the middle layer.  |
**height** | Optional[int] | No | The desired height in pixels. |
**width** | Optional[int] | No | The desired width in pixels. |
**type** | Literal["renderImageLayer"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
