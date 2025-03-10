# VectorType

Represents a fixed size vector of floats. These can be used for vector similarity searches.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**dimension** | int | Yes | The dimension of the vector. |
**supports_search_with** | List[VectorSimilarityFunction] | Yes |  |
**embedding_model** | Optional[EmbeddingModel] | No |  |
**type** | Literal["vector"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
