# GeotimeDestination

A remote Geotime destination. Its system identifier must differ from the local system identifier.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**destination_id** | UUID | Yes | The destination system's identifier. |
**namespace_rid** | Optional[NamespaceRid] | No | The destination namespace. Omit for a remote system that does not use namespaces. |
**type** | Literal["remote"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v3-link) [[Back to API list]](../../../../README.md#apis-v3-link) [[Back to README]](../../../../README.md)
