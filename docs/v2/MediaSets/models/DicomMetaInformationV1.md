# DicomMetaInformationV1

DICOM meta information version 1.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**media_storage_sop** | str | Yes | The Media Storage SOP (Service-Object Pair) Class UID, which identifies  the type of DICOM object stored (e.g., CT Image, MR Image).  |
**media_storage_sop_instance** | str | Yes | The Media Storage SOP Instance UID. |
**transfer_syntax** | str | Yes | The Transfer Syntax UID, which specifies how the DICOM data is encoded  (e.g., compression method, byte ordering).  |
**type** | Literal["v1"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
