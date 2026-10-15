# AudioMediaItemMetadata

Metadata for audio media items.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | AudioDecodeFormat | Yes |  |
**specification** | AudioSpecification | Yes |  |
**size_bytes** | int | Yes | Deprecated: use `sizeBytesLong`. Saturates at 2,147,483,647 for items of 2 GiB or larger.  |
**size_bytes_long** | MediaItemSizeBytes | Yes |  |
**type** | Literal["audio"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
