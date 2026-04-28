# BlockingContinueSessionRequest

BlockingContinueSessionRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**user_input** | UserTextInput | Yes | The user message for the Agent to respond to. |
**parameter_inputs** | Dict[ParameterId, ParameterValue] | Yes | Any supplied values for [application variables](https://palantir.com/docs/foundry/chatbot-studio/application-state/) to pass to the Agent for the exchange.  |
**contexts_override** | Optional[List[InputContext]] | No | If set, automatic [context retrieval](https://palantir.com/docs/foundry/chatbot-studio/retrieval-context/) is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.  |
**session_trace_id** | Optional[SessionTraceId] | No | The unique identifier to use for this continue session trace. By generating and passing this ID to the `blockingContinue` endpoint, clients can use this trace ID to separately load details of the trace used to generate a result, while the result is in progress. If omitted, it will be generated automatically. Clients can check the generated ID by inspecting the `sessionTraceId` in the `SessionExchangeResult`.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
