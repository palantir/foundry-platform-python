# AnthropicMessagesRequest

AnthropicMessagesRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**messages** | List[AnthropicMessage] | Yes | Input messages to the model. This can include a single user-role message or multiple messages with alternating user and assistant roles.  |
**max_tokens** | int | Yes | The maximum number of tokens to generate before stopping. |
**stop_sequences** | Optional[List[str]] | No | Custom text sequences that will cause the model to stop generating. |
**system** | Optional[List[AnthropicSystemMessage]] | No | A system prompt is a way of providing context and instructions to Claude, such as specifying a  particular goal or role. As of now, sending multiple system prompts is not supported.  |
**temperature** | Optional[float] | No | Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Note that even with  temperature of 0.0, the results will not be fully deterministic. Defaults to 1.0  |
**thinking** | Optional[AnthropicThinkingConfig] | No | Configuration for enabling Claude's extended thinking. |
**tool_choice** | Optional[AnthropicToolChoice] | No | How the model should use the provided tools. |
**tools** | Optional[List[AnthropicTool]] | No | Definitions of tools that the model may use. |
**top_k** | Optional[int] | No | Only sample from the top K options for each subsequent token. |
**top_p** | Optional[float] | No | Use nucleus sampling. You should either alter temperature or top_p, but not both |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
