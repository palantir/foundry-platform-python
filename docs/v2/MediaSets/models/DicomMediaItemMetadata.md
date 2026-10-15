# DicomMediaItemMetadata

Metadata for DICOM (Digital Imaging and Communications in Medicine) media items.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**meta_information** | DicomMetaInformation | Yes |  |
**media_type** | DicomMediaType | Yes |  |
**common_data_elements** | CommonDicomDataElements | Yes |  |
**other_data_elements** | Dict[DicomDataElementKey, Any] | Yes | The data elements for a particular DICOM file outside of the media contained within it and the data elements within the commonDataElements field.  |
**size_bytes** | int | Yes | Deprecated: use `sizeBytesLong`. Saturates at 2,147,483,647 for items of 2 GiB or larger.  |
**size_bytes_long** | MediaItemSizeBytes | Yes |  |
**type** | Literal["dicom"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
