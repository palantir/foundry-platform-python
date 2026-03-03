# CheckpointedResource

A Foundry resource that was captured as part of a checkpoint.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes |  |
**resource_type** | CheckpointedResourceType | Yes |  |
**name** | Optional[RedactableString] | No |  |
**project_rid** | Optional[ProjectRid] | No |  |
**namespace_rid** | Optional[NamespaceRid] | No |  |
**compass_path** | RedactableString | Yes |  |
**org_markings** | List[str] | Yes |  |
**type** | Literal["checkpointedResource"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
