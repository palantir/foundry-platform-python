# ChatCompletionRequest

ChatCompletionRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**messages** | List[ChatMessage] | Yes |  |
**parameters** | Dict[ParameterKey, ParameterValue] | Yes | Any additional model-specific parameters: - for global models, the keys can be one of the following     (refer to https://platform.openai.com/docs/api-reference/chat/create for documentation on these parameters):   - `temperature`   - `top_p`   - `n`   - `stop`   - `max_tokens`   - `presence_penalty`   - `frequency_penalty`   - `logit_bias`  |


[[Back to Model list]](../../../README.md#models-v1-link) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
