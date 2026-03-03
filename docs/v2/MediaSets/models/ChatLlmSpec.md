# ChatLlmSpec

Standard chat-based LLM specification with system and user prompts.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**model_locator** | LanguageModelLocator | Yes |  |
**system_prompt** | str | Yes | System prompt for the LLM. |
**user_prompt** | str | Yes | User prompt for the LLM. |
**max_tokens** | Optional[int] | No | Maximum number of tokens per request to generate. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
