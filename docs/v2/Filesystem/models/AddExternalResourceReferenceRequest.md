# AddExternalResourceReferenceRequest

A request to add an external resource as a reference to a project

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**resource_rid** | RID | Yes | The resource identifier of the external resource to add as a reference. Note that this is not a Foundry filesystem resource. |
**import_name** | str | Yes | A user-provided label for this reference, used to identify the import within the project. |
**type** | Literal["external"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
