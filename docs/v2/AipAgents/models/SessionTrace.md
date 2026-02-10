# SessionTrace

SessionTrace

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | SessionTraceId | Yes | The unique identifier for the trace.  |
**status** | SessionTraceStatus | Yes | This indicates whether the Agent has finished generating the final response. Clients should keep polling the `getSessionTrace` endpoint until the status is `COMPLETE`.  |
**contexts** | Optional[SessionExchangeContexts] | No | Any additional context which was provided by the client or retrieved automatically by the agent, grouped by context type. Empty if no additional context was provided or configured to be automatically retrieved. A present SessionExchangeContexts object with empty lists indicates that context retrieval was attempted but no context was found. Note that this field will only be populated once the response generation has completed.  |
**tool_call_groups** | List[ToolCallGroup] | Yes | List of tool call groups that were triggered at the same point in the trace for the agent response generation. The groups are returned in the same order as they were triggered by the agent.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
