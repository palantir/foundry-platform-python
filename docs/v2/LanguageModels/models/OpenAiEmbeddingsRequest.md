# OpenAiEmbeddingsRequest

OpenAiEmbeddingsRequest

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**input** | OpenAiEmbeddingInput | Yes | Input text to embed, encoded as an array of strings. Each input must not exceed the max input  tokens for the model (8192 tokens for all embedding models).  |
**dimensions** | Optional[int] | No | The number of dimensions the resulting output embeddings should have.  Only supported in text-embedding-3 and later models.  |
**encoding_format** | Optional[OpenAiEncodingFormat] | No | The format to return the embeddings in. Can be either float or base64. |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
