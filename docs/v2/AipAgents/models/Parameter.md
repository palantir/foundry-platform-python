# Parameter

A variable configured in the application state of a Chatbot Studio Agent in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/).


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**parameter_type** | ParameterType | Yes | Details of the types of values accepted and defaults for this variable. |
**access** | ParameterAccessMode | Yes | The access mode controls how the Chatbot Studio Agent is able to interact with the variable. |
**description** | Optional[str] | No | A description to explain the use of this variable. This description is injected into the Chatbot Studio Agent's prompt to provide context for when to use the variable.  |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
