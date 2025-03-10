# VectorType

Represents a fixed size vector of floats. These can be used for vector similarity searches.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**dimension** | int | Yes | The dimension of the vector. |
**supports_search_with** | typing.List[VectorSimilarityFunction] | Yes |  |
**embedding_model** | typing.Optional[EmbeddingModel] | No |  |
**type** | typing.Literal["vector"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
