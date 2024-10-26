# AgentMetadataDict

Metadata for an Agent.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**displayName** | pydantic.StrictStr | Yes | The name of the Agent. |
**description** | NotRequired[pydantic.StrictStr] | No | The description for the Agent. |
**inputPlaceholder** | NotRequired[pydantic.StrictStr] | No | The default text to show as the placeholder input for chats with the Agent. |
**suggestedPrompts** | List[pydantic.StrictStr] | Yes | Prompts to show to the user as example messages to start a conversation with the Agent.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
