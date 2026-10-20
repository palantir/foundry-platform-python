# Agent

Agent

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | AgentRid | Yes | An RID identifying a Chatbot Studio Agent created in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/). |
**version** | AgentVersionString | Yes | The version of this instance of the Chatbot Studio Agent. |
**metadata** | AgentMetadata | Yes |  |
**parameters** | Dict[ParameterId, Parameter] | Yes | The types and names of variables configured for the Chatbot Studio Agent in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/) in the [application state](https://palantir.com/docs/foundry/chatbot-studio/application-state/). These variables can be used to send custom values in prompts sent to a Chatbot Studio Agent to customize and control the Chatbot Studio Agent's behavior.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
