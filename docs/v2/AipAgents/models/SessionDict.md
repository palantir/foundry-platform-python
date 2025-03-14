# SessionDict

Session

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | RID | Yes | The Resource Identifier (RID) of the conversation session. |
**metadata** | SessionMetadataDict | Yes | Metadata about the session. |
**agentRid** | RID | Yes | The Resource Identifier (RID) of the Agent associated with the session. |
**agentVersion** | str | Yes | The version of the Agent associated with the session. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
