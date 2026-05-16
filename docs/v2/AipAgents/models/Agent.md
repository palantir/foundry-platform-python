# Agent

Agent

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | AgentRid | Yes | An RID identifying an AIP Agent created in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/). |
**version** | AgentVersionString | Yes | The version of this instance of the Agent. |
**metadata** | AgentMetadata | Yes |  |
**parameters** | Dict[ParameterId, Parameter] | Yes | The types and names of variables configured for the Agent in [AIP Agent Studio](https://palantir.com/docs/foundry/agent-studio/overview/) in the [application state](https://palantir.com/docs/foundry/agent-studio/application-state/). These variables can be used to send custom values in prompts sent to an Agent to customize and control the Agent's behavior.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
