# SpreadsheetMediaItemMetadata

Metadata for spreadsheet media items.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | SpreadsheetDecodeFormat | Yes |  |
**sheet_names** | List[str] | Yes | The names of the sheets in the spreadsheet. |
**size_bytes** | int | Yes | Deprecated: use `sizeBytesLong`. Saturates at 2,147,483,647 for items of 2 GiB or larger.  |
**size_bytes_long** | MediaItemSizeBytes | Yes |  |
**title** | Optional[str] | No | The title of the spreadsheet, if available. |
**author** | Optional[str] | No | The author of the spreadsheet, if available. |
**type** | Literal["spreadsheet"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
