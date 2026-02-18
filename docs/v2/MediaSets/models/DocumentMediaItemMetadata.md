# DocumentMediaItemMetadata

Metadata for document media items.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | DocumentDecodeFormat | Yes |  |
**pages** | Optional[int] | No | The number of pages in the document. |
**size_bytes** | int | Yes | The size of the media item in bytes. |
**title** | Optional[str] | No | The title of the document, if available. |
**author** | Optional[str] | No | The author of the document, if available. |
**type** | Literal["document"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
