# ExtractDocumentLayoutAwareTextV2Operation

Extracts text blocks and bounding boxes from a PDF as structured JSON grouped by page.
Replaces the deprecated `documentToText.extractLayoutAwareContent` operation
(`DocumentExtractLayoutAwareContentOperation`). The response schema differs from the legacy
result, so consumers must update their result parsing when migrating.
The `config.format` option selects plain text, Markdown, or HTML for each block's content;
the result remains structured JSON. This operation only supports PDFs.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**page_range** | Optional[PageRange] | No |  |
**config** | ExtractDocumentLayoutAwareTextV2Config | Yes |  |
**type** | Literal["extractLayoutAwareTextV2"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
