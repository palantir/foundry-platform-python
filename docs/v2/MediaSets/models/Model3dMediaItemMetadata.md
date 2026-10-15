# Model3dMediaItemMetadata

Metadata for 3D model media items.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | Model3dDecodeFormat | Yes |  |
**model_type** | Model3dType | Yes |  |
**size_bytes** | int | Yes | Deprecated: use `sizeBytesLong`. Saturates at 2,147,483,647 for items of 2 GiB or larger.  |
**size_bytes_long** | MediaItemSizeBytes | Yes |  |
**type** | Literal["model3d"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
