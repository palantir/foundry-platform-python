# SessionDict

Session

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | SessionRid | Yes | The Resource Identifier (RID) of the conversation session. |
**metadata** | SessionMetadataDict | Yes | Metadata about the session. |
**agentRid** | AgentRid | Yes | The Resource Identifier (RID) of the Agent that the session is with. |
**agentVersion** | AgentVersionString | Yes | The version of the Agent that the session is with. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
