# ParameterDict

A variable configured in the application state of an Agent in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**parameterType** | ParameterTypeDict | Yes | Details of the types of values accepted and defaults for this variable. |
**access** | ParameterAccessMode | Yes | The access mode controls how the Agent is able to interact with the variable. |
**description** | NotRequired[str] | No | A description to explain the use of this variable. This description is injected into the Agent's prompt to provide context for when to use the variable.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
