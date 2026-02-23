# Transformation

A transformation to apply to a media item. Each variant specifies the type of transformation
and any parameters required for the operation.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
EmailToTextTransformation | emailToText
ImageTransformation | image
SpreadsheetToTextTransformation | spreadsheetToText
VideoToAudioTransformation | videoToAudio
AudioToTextTransformation | audioToText
EmailToAttachmentTransformation | emailToAttachment
VideoToArchiveTransformation | videoToArchive
VideoToTextTransformation | videoToText
ImageToTextTransformation | imageToText
VideoToImageTransformation | videoToImage
VideoTransformation | video
ImageToDocumentTransformation | imageToDocument
DicomToImageTransformation | dicomToImage
DocumentToDocumentTransformation | documentToDocument
DocumentToImageTransformation | documentToImage
ImageToEmbeddingTransformation | imageToEmbedding
AudioTransformation | audio
DocumentToTextTransformation | documentToText


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
