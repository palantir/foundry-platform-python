# ReferenceSigningOptions

Options for signing references in the response.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**sign_media_references** | Optional[bool] | No | Deprecated and ignored. Media references backed by a media set view are signed by default: the response includes a `token` on each `MediaReference` value that can be used to access the referenced media item directly, enabling item-level access control (the caller needs access to the object whose property holds the reference, not view access on the parent media set).  This field no longer has any effect; setting it to true or false is ignored. Arrays of media references are not signed.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
