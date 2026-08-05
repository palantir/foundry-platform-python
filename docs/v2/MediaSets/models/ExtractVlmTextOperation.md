# ExtractVlmTextOperation

Extract text from a document using vision language models (VLMs).
VLMs can understand document layout and structure more intelligently than traditional OCR.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**llm_spec** | LlmSpec | Yes |  |
**preprocessing_configuration** | Optional[VlmPreprocessingConfig] | No |  |
**image_spec** | Optional[ImageSpec] | No |  |
**output_format** | VlmOutputFormat | Yes |  |
**page_range** | Optional[PageRange] | No |  |
**type** | Literal["extractVlmText"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
