# FunctionRetrievedContext

Context retrieved from running a function to include as additional context in the prompt to the Agent.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**function_rid** | functions_models.FunctionRid | Yes |  |
**function_version** | functions_models.FunctionVersion | Yes |  |
**retrieved_prompt** | str | Yes | String content returned from a context retrieval function.  |
**type** | typing.Literal["functionRetrievedContext"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
