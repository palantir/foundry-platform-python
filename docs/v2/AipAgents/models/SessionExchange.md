# SessionExchange

Represents an individual exchange between a user and an Agent in a conversation session.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**user_input** | UserTextInput | Yes | The user message that initiated the exchange. |
**contexts** | typing.Optional[SessionExchangeContexts] | No | Additional retrieved context that was included in the prompt to the Agent. This may include context that was passed by the client with the user input, or relevant context that was automatically retrieved and added based on available data sources configured on the Agent. Empty if no additional context was included in the prompt.  |
**result** | SessionExchangeResult | Yes | The final result for the exchange.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
