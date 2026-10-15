# TrashStatus

Whether a resource is in the trash, and if so, whether it was trashed directly or through one of its ancestors.


Values:
- **ANCESTOR_TRASHED**: The resource is in the trash because one of its ancestors was trashed. Such a resource cannot be restored
on its own; restoring the trashed ancestor also restores this resource.

- **DIRECTLY_TRASHED**: The resource itself was trashed and can be restored.
- **NOT_TRASHED**: Neither the resource nor any of its ancestors is trashed.

| **Value** |
| --------- |
| `"NOT_TRASHED"` |
| `"DIRECTLY_TRASHED"` |
| `"ANCESTOR_TRASHED"` |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
