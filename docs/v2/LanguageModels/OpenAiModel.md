# OpenAiModel

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**embeddings**](#embeddings) | **POST** /v2/languageModels/openAi/{openAiModelModelId}/embeddings | Private Beta |

# **embeddings**


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**open_ai_model_model_id** | LanguageModelApiName |  |  |
**input** | OpenAiEmbeddingInput | Input text to embed, encoded as an array of strings. Each input must not exceed the max input  tokens for the model (8192 tokens for all embedding models).  |  |
**dimensions** | Optional[int] | The number of dimensions the resulting output embeddings should have.  Only supported in text-embedding-3 and later models.  | [optional] |
**encoding_format** | Optional[OpenAiEncodingFormat] | The format to return the embeddings in. Can be either float or base64. | [optional] |
**preview** | Optional[PreviewMode] | Enables the use of preview functionality. | [optional] |

### Return type
**OpenAiEmbeddingsResponse**

### Example

```python
from foundry_sdk import FoundryClient
import foundry_sdk
from pprint import pprint

client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# LanguageModelApiName
open_ai_model_model_id = None
# OpenAiEmbeddingInput | Input text to embed, encoded as an array of strings. Each input must not exceed the max input  tokens for the model (8192 tokens for all embedding models).
input = None
# Optional[int] | The number of dimensions the resulting output embeddings should have.  Only supported in text-embedding-3 and later models.
dimensions = None
# Optional[OpenAiEncodingFormat] | The format to return the embeddings in. Can be either float or base64.
encoding_format = "FLOAT"
# Optional[PreviewMode] | Enables the use of preview functionality.
preview = None


try:
    api_response = client.language_models.OpenAiModel.embeddings(
        open_ai_model_model_id,
        input=input,
        dimensions=dimensions,
        encoding_format=encoding_format,
        preview=preview,
    )
    print("The embeddings response:\n")
    pprint(api_response)
except foundry_sdk.PalantirRPCException as e:
    print("HTTP error when calling OpenAiModel.embeddings: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | OpenAiEmbeddingsResponse  |  | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v2-link) [[Back to Model list]](../../../README.md#models-v2-link) [[Back to README]](../../../README.md)

