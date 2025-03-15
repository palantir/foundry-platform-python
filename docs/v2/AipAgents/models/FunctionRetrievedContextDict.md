# FunctionRetrievedContextDict

Context retrieved from running a function to include as additional context in the prompt to the Agent.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**functionRid** | FunctionRid | Yes |  |
**functionVersion** | FunctionVersion | Yes |  |
**retrievedPrompt** | str | Yes | String content returned from a context retrieval function.  |
**type** | Literal["functionRetrievedContext"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
