# AnthropicModel

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**messages**](#messages) | **POST** /v2/languageModels/anthropic/{anthropicModelModelId}/messages | Private Beta |

# **messages**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**anthropic_model_model_id** | LanguageModelApiName |  |  |
**max_tokens** | int | The maximum number of tokens to generate before stopping. |  |
**messages** | List[AnthropicMessage] | Input messages to the model. This can include a single user-role message or multiple messages with alternating user and assistant roles.  |  |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |
**stop_sequences** | Optional[List[str]] | Custom text sequences that will cause the model to stop generating. | [optional] |
**system** | Optional[List[AnthropicSystemMessage]] | A system prompt is a way of providing context and instructions to Claude, such as specifying a  particular goal or role. As of now, sending multiple system prompts is not supported.  | [optional] |
**temperature** | Optional[float] | Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Note that even with  temperature of 0.0, the results will not be fully deterministic. Defaults to 1.0  | [optional] |
**thinking** | Optional[AnthropicThinkingConfig] | Configuration for enabling Claude's extended thinking. | [optional] |
**tool_choice** | Optional[AnthropicToolChoice] | How the model should use the provided tools. | [optional] |
**tools** | Optional[List[AnthropicTool]] | Definitions of tools that the model may use. | [optional] |
**top_k** | Optional[int] | Only sample from the top K options for each subsequent token. | [optional] |
**top_p** | Optional[float] | Use nucleus sampling. You should either alter temperature or top_p, but not both | [optional] |

### Return type
**AnthropicMessagesResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# LanguageModelApiName
anthropic_model_model_id = None
# int | The maximum number of tokens to generate before stopping.
max_tokens = None
# List[AnthropicMessage] | Input messages to the model. This can include a single user-role message or multiple messages with alternating user and assistant roles.
messages = [{"role": "user"}]
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None
# Optional[List[str]] | Custom text sequences that will cause the model to stop generating.
stop_sequences = None
# Optional[List[AnthropicSystemMessage]] | A system prompt is a way of providing context and instructions to Claude, such as specifying a  particular goal or role. As of now, sending multiple system prompts is not supported.
system = None
# Optional[float] | Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Note that even with  temperature of 0.0, the results will not be fully deterministic. Defaults to 1.0
temperature = None
# Optional[AnthropicThinkingConfig] | Configuration for enabling Claude's extended thinking.
thinking = None
# Optional[AnthropicToolChoice] | How the model should use the provided tools.
tool_choice = None
# Optional[List[AnthropicTool]] | Definitions of tools that the model may use.
tools = None
# Optional[int] | Only sample from the top K options for each subsequent token.
top_k = None
# Optional[float] | Use nucleus sampling. You should either alter temperature or top_p, but not both
top_p = None


try:
    api_response = client.language_models.AnthropicModel.messages(
        anthropic_model_model_id,
        max_tokens=max_tokens,
        messages=messages,
        preview=preview,
        stop_sequences=stop_sequences,
        system=system,
        temperature=temperature,
        thinking=thinking,
        tool_choice=tool_choice,
        tools=tools,
        top_k=top_k,
        top_p=top_p,
    )
    print("The messages response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling AnthropicModel.messages: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AnthropicMessagesResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

