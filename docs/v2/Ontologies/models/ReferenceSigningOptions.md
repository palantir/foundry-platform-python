# ReferenceSigningOptions

Options for signing references in the response.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**sign_media_references** | Optional[bool] | No | If set to true, the response will include a `token` on each `MediaReference` value that can be used to access the referenced media item directly. This enables item-level access control: the caller does not need view access on the parent media set, only access to the object whose property holds the reference.  Only applies to media references backed by a media set view. Arrays of media references are not signed. Defaults to false if not set.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
