# ExtractImageLayoutAwareTextV2Operation

Extracts text blocks and bounding boxes from an image as structured JSON.
Replaces the deprecated `imageToText.extractLayoutAwareContent` operation
(`ImageExtractLayoutAwareContentOperation`). The block schema differs from the legacy
result, so consumers must update their result parsing when migrating.
The `format` option selects plain text, Markdown, or HTML for each block's content;
the result remains structured JSON.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | Optional[TextOutputFormat] | No |  |
**languages** | List[OcrLanguageOrScript] | Yes | List of OCR languages or scripts to use. |
**type** | Literal["extractLayoutAwareTextV2"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
