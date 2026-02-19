# SlicePdfRangeOperation

Slices a PDF to a specified page range.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**start_page_inclusive** | int | Yes | The zero-indexed start page (inclusive). |
**end_page_exclusive** | int | Yes | The zero-indexed end page (exclusive). |
**strictly_enforce_end_page** | Optional[bool] | No | If true (default), the operation fails if endPage exceeds the document's page count. If false, ends at min(endPage, lastPage).  |
**type** | Literal["slicePdfRange"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
