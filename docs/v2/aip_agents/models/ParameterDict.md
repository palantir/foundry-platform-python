# ParameterDict

A parameter configured for an Agent in [AIP Agent Studio](/docs/foundry/agent-studio/overview/).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**parameterType** | ParameterTypeDict | Yes | Details of the types of values accepted and defaults for this parameter. |
**access** | ParameterAccessMode | Yes | The access mode controls how the Agent is able to interact with the parameter. |
**description** | NotRequired[str] | No | A description to explain the use of this parameter. This description is injected with the parameter value into the Agent's prompt, to provide context for when to use the parameter.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
