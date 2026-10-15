# CadMediaItemMetadata

Metadata for CAD media items.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | CadDecodeFormat | Yes |  |
**size_bytes** | int | Yes | Deprecated: use `sizeBytesLong`. Saturates at 2,147,483,647 for items of 2 GiB or larger.  |
**size_bytes_long** | MediaItemSizeBytes | Yes |  |
**units** | Optional[CadUnits] | No |  |
**type** | Literal["cad"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
