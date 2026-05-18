# DocumentToTextOperation

The operation to perform for document to text conversion.

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
ExtractTableOfContentsOperation | extractTableOfContents
GetPdfPageDimensionsOperation | getPdfPageDimensions
ExtractAllTextOperation | extractAllText
ExtractVlmTextOperation | extractVlmText
ExtractTextFromPagesToArrayOperation | extractTextFromPagesToArray
OcrOnPageOperation | ocrOnPage
ExtractFormFieldsOperation | extractFormFields
ExtractDocumentLayoutAwareTextV2Operation | extractLayoutAwareTextV2
ExtractDocumentTextV2Operation | extractTextV2
ExtractUnstructuredTextFromPageOperation | extractUnstructuredTextFromPage
DocumentExtractLayoutAwareContentOperation | extractLayoutAwareContent
OcrOnPagesOperation | ocrOnPages


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
