# MediaItemMetadata

Detailed metadata about a media item, including type-specific information such as dimensions for images,
duration for audio/video, page count for documents, etc.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
CadMediaItemMetadata | cad
DocumentMediaItemMetadata | document
ImageryMediaItemMetadata | imagery
SpreadsheetMediaItemMetadata | spreadsheet
UntypedMediaItemMetadata | untyped
AudioMediaItemMetadata | audio
Model3dMediaItemMetadata | model3d
VideoMediaItemMetadata | video
DicomMediaItemMetadata | dicom
EmailMediaItemMetadata | email


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
