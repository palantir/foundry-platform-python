# AgentDict

Agent

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | AgentRid | Yes | A RID identifying an AIP Agent created in AIP Agent Studio. |
**version** | AgentVersionString | Yes | The version of this instance of the Agent. |
**metadata** | AgentMetadataDict | Yes |  |
**parameters** | Dict[ParameterId, ParameterDict] | Yes | The types and names of parameters configured for the Agent in AIP Agent Studio. Parameters are variables within the prompt for an Agent which can be used to customize and control behavior of the Agent.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
