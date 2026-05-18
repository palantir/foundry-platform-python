# ProjectExternalResourceReference

A reference to a resource that exists outside of the Foundry filesystem such as a spark profile or an LLM model.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**resource_rid** | RID | Yes | The resource identifier of the external resource. |
**name** | str | Yes | The user-provided label for this reference, used to identify the import within the project. |
**imported_at** | datetime | Yes |  |
**imported_by** | UserId | Yes |  |
**type** | Literal["external"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
