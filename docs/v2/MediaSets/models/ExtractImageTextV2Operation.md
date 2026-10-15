# ExtractImageTextV2Operation

Extracts text from an image and returns JSON containing combined text and per-page text.
The `format` option selects plain text, Markdown, or HTML.
To include text blocks and bounding boxes, use `imageToText.extractLayoutAwareTextV2`
(`ExtractImageLayoutAwareTextV2Operation`) instead.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | Optional[TextOutputFormat] | No |  |
**languages** | List[OcrLanguageOrScript] | Yes | List of OCR languages or scripts to use. |
**type** | Literal["extractTextV2"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
