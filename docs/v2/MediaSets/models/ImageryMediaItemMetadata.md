# ImageryMediaItemMetadata

Metadata for imagery (image) media items.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | ImageryDecodeFormat | Yes |  |
**dimensions** | Optional[Dimensions] | No |  |
**bands** | List[BandInfo] | Yes | Information about the bands of the image, if available. |
**attributes** | Dict[ImageAttributeDomain, Dict[ImageAttributeKey, str]] | Yes | The metadata attributes described in the image header in the form of a map <domain, <key, value>>. For the default domain, or when the domain is not specified, the domain key will be the empty string ("").  |
**icc_profile** | Optional[str] | No | The base64-encoded ICC profile for the image, if available. |
**geo** | Optional[GeoMetadata] | No |  |
**pages** | Optional[int] | No | The number of pages associated with this image. Usually 1, but may be more for some formats (multi-page TIFFs, for example).  |
**orientation** | Optional[Orientation] | No |  |
**size_bytes** | int | Yes | The size of the media item in bytes. |
**type** | Literal["imagery"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
